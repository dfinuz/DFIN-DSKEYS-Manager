import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import webbrowser
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

APP_TITLE = "DSKEYS E-IMZO Expiry Manager"
APP_VERSION = "2.1"

try:
    from send2trash import send2trash
except Exception:
    send2trash = None

PS_SCRIPT = r'''$ErrorActionPreference = "Stop"
$socket = New-Object System.Net.WebSockets.ClientWebSocket
$uri = [Uri]"wss://127.0.0.1:64443/service/cryptapi"
$token = [Threading.CancellationToken]::None
$socket.ConnectAsync($uri, $token).GetAwaiter().GetResult()
$request = @{ plugin = "pfx"; name = "list_all_certificates" } | ConvertTo-Json -Compress
$bytes = [Text.Encoding]::UTF8.GetBytes($request)
$segment = New-Object ArraySegment[byte] -ArgumentList (, $bytes)
$socket.SendAsync($segment, [Net.WebSockets.WebSocketMessageType]::Text, $true, $token).GetAwaiter().GetResult()
$stream = New-Object System.IO.MemoryStream
try {
    do {
        $buffer = New-Object byte[] 65536
        $resultBuffer = New-Object ArraySegment[byte] -ArgumentList (, $buffer)
        $result = $socket.ReceiveAsync($resultBuffer, $token).GetAwaiter().GetResult()
        if ($result.MessageType -eq [Net.WebSockets.WebSocketMessageType]::Close) { break }
        $stream.Write($buffer, 0, $result.Count)
    } while (-not $result.EndOfMessage)
    $text = [Text.Encoding]::UTF8.GetString($stream.ToArray())
    [IO.File]::WriteAllText($args[0], $text, (New-Object Text.UTF8Encoding($false)))
} finally {
    $stream.Dispose()
    $socket.Dispose()
}
'''

@dataclass
class Record:
    name: str
    path: Path | None
    owner: str
    tin: str
    pinfl: str
    serial: str
    valid_from: datetime | None
    valid_to: datetime | None
    status: str
    details: str = ""


def alias_value(alias, field):
    patterns = {
        "TIN": [r"(?:^|,)inn=([^,]*)", r"(?:^|,)uid=([^,]*)"],
        "PINFL": [r"(?:^|,)1\.2\.860\.3\.16\.1\.2=([^,]*)", r"(?:^|,)pinfl=([^,]*)"],
    }
    candidates = patterns.get(field, [rf"(?:^|,){re.escape(field)}=([^,]*)"])
    for pattern in candidates:
        match = re.search(pattern, alias, flags=re.I)
        if match:
            return match.group(1).strip()
    return ""


def parse_date(value):
    if not value:
        return None
    for fmt in ("%Y.%m.%d %H:%M:%S", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            pass
    return None


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(f"{APP_TITLE} v{APP_VERSION}")
        self.geometry("1160x720")
        self.minsize(900, 570)
        self.folder_var = tk.StringVar(value=str(Path(os.environ.get("SystemDrive", "C:")) / "DSKEYS"))
        self.status_var = tk.StringVar(value="Click Scan E-IMZO. No PFX password is required.")
        self.records = []
        self.build_ui()

    def build_ui(self):
        top = ttk.Frame(self, padding=12)
        top.pack(fill="x")
        ttk.Label(top, text="DSKEYS folder:").grid(row=0, column=0, sticky="w")
        ttk.Entry(top, textvariable=self.folder_var).grid(row=0, column=1, sticky="ew", padx=8)
        ttk.Button(top, text="Browse...", command=self.browse).grid(row=0, column=2)
        ttk.Button(top, text="Scan E-IMZO", command=self.scan).grid(row=0, column=3, padx=(8, 0))
        top.columnconfigure(1, weight=1)

        ttk.Label(self, text="Reads expiry metadata from the local E-IMZO service. It does not request, read, or store PFX passwords.",
                  foreground="#526070", padding=(12, 0, 12, 10)).pack(fill="x")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=12)
        self.trees = {}
        for status, title in [("working", "Working"), ("soon", "Expiring in 30 days"),
                              ("expired", "Expired"), ("unmatched", "File not matched"),
                              ("unknown", "Metadata unavailable")]:
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=title)
            tree = ttk.Treeview(frame, columns=("name", "expiry", "owner", "id", "file"), show="headings", selectmode="extended")
            for col, text, width in [("name", "E-IMZO name", 250), ("expiry", "Expiry", 105),
                                     ("owner", "Owner / company", 310), ("id", "STIR / PINFL", 150),
                                     ("file", "Matched file", 330)]:
                tree.heading(col, text=text)
                tree.column(col, width=width, anchor="center" if col == "expiry" else "w")
            ys = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
            xs = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
            tree.configure(yscrollcommand=ys.set, xscrollcommand=xs.set)
            tree.grid(row=0, column=0, sticky="nsew"); ys.grid(row=0, column=1, sticky="ns"); xs.grid(row=1, column=0, sticky="ew")
            frame.rowconfigure(0, weight=1); frame.columnconfigure(0, weight=1)
            self.trees[status] = tree

        actions = ttk.Frame(self, padding=12)
        actions.pack(fill="x")
        ttk.Button(actions, text="Move all expired", command=self.move_all).pack(side="left")
        ttk.Button(actions, text="Move selected expired", command=self.move_selected).pack(side="left", padx=8)
        ttk.Button(actions, text="Recycle selected expired", command=self.recycle_selected).pack(side="left")
        ttk.Button(actions, text="Open selected location", command=self.open_location).pack(side="right")

        branding = tk.Frame(self, bg="#0B2F5E", height=38)
        branding.pack(fill="x")
        branding.pack_propagate(False)
        brand_label = tk.Label(
            branding,
            text="POWERED BY DFIN.UZ",
            bg="#0B2F5E",
            fg="#FFFFFF",
            font=("Segoe UI", 10, "bold"),
            cursor="hand2",
        )
        brand_label.pack(side="right", padx=14, pady=9)
        brand_label.bind("<Button-1>", lambda _event: webbrowser.open("https://dfin.uz"))
        tk.Label(
            branding,
            text="DSKEYS Certificate Manager",
            bg="#0B2F5E",
            fg="#D8E8F5",
            font=("Segoe UI", 9),
        ).pack(side="left", padx=14, pady=9)

        ttk.Separator(self).pack(fill="x")
        ttk.Label(self, textvariable=self.status_var, padding=10).pack(fill="x")

    def browse(self):
        value = filedialog.askdirectory(initialdir=self.folder_var.get())
        if value:
            self.folder_var.set(value)

    def fetch_eimzo(self):
        with tempfile.TemporaryDirectory() as temp:
            temp = Path(temp)
            ps1 = temp / "read_eimzo.ps1"
            output = temp / "response.json"
            ps1.write_text(PS_SCRIPT, encoding="utf-8")
            command = ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(ps1), str(output)]
            completed = subprocess.run(command, capture_output=True, text=True, timeout=60)
            if completed.returncode != 0:
                raise RuntimeError((completed.stderr or completed.stdout or "PowerShell/E-IMZO request failed").strip())
            if not output.exists():
                raise RuntimeError("E-IMZO returned no response file")
            return json.loads(output.read_text(encoding="utf-8-sig"))

    def file_index(self, folder):
        result = {}
        if not folder.is_dir():
            return result
        for path in folder.rglob("*"):
            if not path.is_file():
                continue
            keys = {path.name.casefold(), path.stem.casefold()}
            for key in keys:
                result.setdefault(key, []).append(path)
        return result

    def match_file(self, cert, index):
        name = str(cert.get("name", "")).strip()
        for key in (name.casefold(), Path(name).stem.casefold(), f"{name}.pfx".casefold()):
            paths = index.get(key)
            if paths:
                return paths[0]
        return None

    def scan(self):
        folder = Path(self.folder_var.get().strip())
        self.status_var.set("Connecting to local E-IMZO and receiving all certificate metadata...")
        self.update_idletasks()
        try:
            data = self.fetch_eimzo()
        except Exception as exc:
            messagebox.showerror("E-IMZO connection failed", f"Keep E-IMZO running, then try again.\n\n{exc}")
            self.status_var.set("E-IMZO scan failed.")
            return
        if not data.get("success"):
            messagebox.showerror("E-IMZO error", str(data.get("reason") or data))
            return

        for tree in self.trees.values():
            tree.delete(*tree.get_children())
        self.records = []
        index = self.file_index(folder)
        now = datetime.now()
        certificates = data.get("certificates") or []

        for number, cert in enumerate(certificates):
            alias = str(cert.get("alias") or "")
            owner = alias_value(alias, "cn") or alias_value(alias, "o")
            tin = alias_value(alias, "TIN")
            pinfl = alias_value(alias, "PINFL")
            serial = alias_value(alias, "serialnumber")
            valid_from = parse_date(alias_value(alias, "validfrom"))
            valid_to = parse_date(alias_value(alias, "validto"))
            path = self.match_file(cert, index)

            if valid_to is None:
                status = "unknown"
                details = "E-IMZO alias does not contain VALIDTO"
            elif path is None:
                status = "unmatched"
                details = "Certificate metadata found, but physical file was not matched"
            elif valid_to <= now:
                status = "expired"
                details = "Expired"
            elif (valid_to - now).days <= 30:
                status = "soon"
                details = "Expires within 30 days"
            else:
                status = "working"
                details = "Working"

            record = Record(str(cert.get("name") or ""), path, owner, tin, pinfl, serial, valid_from, valid_to, status, details)
            self.records.append(record)
            iid = f"{status}-{number}"
            self.trees[status].insert("", "end", iid=iid, values=(record.name,
                record.valid_to.strftime("%Y-%m-%d") if record.valid_to else "",
                record.owner, record.tin or record.pinfl, str(record.path) if record.path else record.details))

        self.update_counts("Scan complete")
        self.notebook.select(2 if any(r.status == "expired" for r in self.records) else 0)

    def update_counts(self, prefix):
        counts = {key: sum(r.status == key for r in self.records) for key in self.trees}
        self.status_var.set(f"{prefix}. Working: {counts['working']} | Soon: {counts['soon']} | Expired: {counts['expired']} | Unmatched: {counts['unmatched']} | Unknown: {counts['unknown']}")

    def selected_records(self, status):
        selected = self.trees[status].selection()
        numbers = {int(iid.rsplit("-", 1)[1]) for iid in selected}
        candidates = [r for r in self.records if r.status == status]
        # Tree suffix is global certificate number, so map from displayed values instead.
        paths = {self.trees[status].item(iid, "values")[4] for iid in selected}
        return [r for r in candidates if r.path and str(r.path) in paths]

    def expired_records(self):
        return [r for r in self.records if r.status == "expired" and r.path and r.path.exists()]

    def target_folder(self):
        base = Path(self.folder_var.get().strip())
        target = base.parent / f"Expired_Keys_{datetime.now().strftime('%Y-%m-%d_%H%M%S')}"
        target.mkdir(parents=True, exist_ok=False)
        return target

    def move_records(self, records):
        if not records:
            messagebox.showinfo("Nothing to move", "No matched expired files were selected.")
            return
        target = self.target_folder()
        moved, failed = 0, []
        for record in records:
            try:
                destination = target / record.path.name
                counter = 1
                while destination.exists():
                    destination = target / f"{record.path.stem}_{counter}{record.path.suffix}"
                    counter += 1
                shutil.move(str(record.path), str(destination)); moved += 1
            except Exception as exc:
                failed.append(f"{record.name}: {exc}")
        message = f"Moved {moved} expired file(s) to:\n{target}"
        if failed:
            message += "\n\nFailures:\n" + "\n".join(failed[:10])
        messagebox.showinfo("Move complete", message)
        self.scan()

    def move_all(self):
        records = self.expired_records()
        if records and messagebox.askyesno("Move all expired", f"Move {len(records)} positively matched expired file(s)?\n\nWorking files will remain in DSKEYS."):
            self.move_records(records)
        elif not records:
            messagebox.showinfo("No expired files", "No matched expired files are available.")

    def move_selected(self):
        self.move_records(self.selected_records("expired"))

    def recycle_selected(self):
        records = self.selected_records("expired")
        if not records:
            messagebox.showinfo("Nothing selected", "Select expired files first.")
            return
        if send2trash is None:
            messagebox.showerror("Package needed", f"Run:\n\n\"{sys.executable}\" -m pip install send2trash")
            return
        if not messagebox.askyesno("Recycle expired files", f"Send {len(records)} expired file(s) to the Windows Recycle Bin?", icon="warning"):
            return
        for record in records:
            send2trash(str(record.path))
        self.scan()

    def open_location(self):
        status = list(self.trees)[self.notebook.index(self.notebook.select())]
        selected = self.selected_records(status)
        if not selected:
            messagebox.showinfo("Nothing selected", "Select a matched file first.")
            return
        subprocess.Popen(["explorer", "/select,", str(selected[0].path)])


if __name__ == "__main__":
    App().mainloop()
