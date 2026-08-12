DFIN DSKEYS MANAGER v2.1 - WINDOWS DISTRIBUTION KIT

CONSUMER EXPERIENCE
- Install DFIN_DSKEYS_Manager_Setup_v2.1.exe
- Launch from the Desktop or Start menu
- No Python installation
- No pip commands
- No cryptography package
- E-IMZO must already be installed and running

BRANDING
The main application window permanently displays "POWERED BY DFIN.UZ" in the footer.
Clicking the brand opens https://dfin.uz.

HOW THE DEVELOPER BUILDS THE INSTALLER
Option A, local Windows build:
1. Install Python 3.13.
2. Double-click BUILD_WINDOWS_EXE.bat.
3. Install Inno Setup 6.
4. Open DFIN_DSKEYS_Manager.iss and click Build > Compile.
5. Installer appears in installer\DFIN_DSKEYS_Manager_Setup_v2.1.exe.

Option B, GitHub Actions:
1. Put all files in a GitHub repository.
2. Copy build-windows.yml to .github\workflows\build-windows.yml.
3. Open Actions and run "Build Windows installer".
4. Download the DFIN-DSKEYS-Windows artifact.

IMPORTANT FOR PUBLIC DISTRIBUTION
Digitally sign the installer and EXE with a Windows code-signing certificate. Without signing,
Microsoft SmartScreen may show an unknown publisher warning. The permanent in-app branding
is not a substitute for code signing.
