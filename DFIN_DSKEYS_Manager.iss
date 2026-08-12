#define MyAppName "DFIN DSKEYS Manager"
#define MyAppVersion "2.1"
#define MyAppPublisher "dfin.uz"
#define MyAppURL "https://dfin.uz"
#define MyAppExeName "DFIN_DSKEYS_Manager.exe"

[Setup]
AppId={{E0D8B8A1-9FAE-4A69-9239-DF17D9CF93F1}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
DefaultDirName={autopf}\DFIN DSKEYS Manager
DefaultGroupName=DFIN DSKEYS Manager
DisableProgramGroupPage=yes
OutputDir=installer
OutputBaseFilename=DFIN_DSKEYS_Manager_Setup_v2.1
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
UninstallDisplayIcon={app}\{#MyAppExeName}

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "russian"; MessagesFile: "compiler:Languages\\Russian.isl"

[Files]
Source: "dist\\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\\DFIN DSKEYS Manager"; Filename: "{app}\\{#MyAppExeName}"
Name: "{autodesktop}\\DFIN DSKEYS Manager"; Filename: "{app}\\{#MyAppExeName}"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional shortcuts:"; Flags: unchecked

[Run]
Filename: "{app}\\{#MyAppExeName}"; Description: "Launch DFIN DSKEYS Manager"; Flags: nowait postinstall skipifsilent
