#define source_path ReadIni(SourcePath + "\setup.ini", "Data", "source_path")
#define min_windows ReadIni(SourcePath + "\setup.ini", "Data", "min_windows")

#define MyAppName "TreZapalooza"
#define MyAppExeName "TreZapaloozaLauncher.exe"
#define MyAppIcon "data/icon.ico"
#dim VersionTuple[4]
#define MyAppVersion GetVersionComponents(source_path + '\TreZapaloozaLauncher.exe', VersionTuple[0], VersionTuple[1], VersionTuple[2], VersionTuple[3])
#define MyAppVersionText Str(VersionTuple[0])+"."+Str(VersionTuple[1])+"."+Str(VersionTuple[2])


[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
AppId={{918BA46A-FAB8-460C-9DFF-AE691E1C865C}}
AppName={#MyAppName}
AppCopyright=Distributed under MIT License
AppVerName={#MyAppName} {#MyAppVersionText}
VersionInfoVersion={#MyAppVersion}
DefaultDirName={autopf}\{#MyAppName}
DisableProgramGroupPage=yes
DefaultGroupName=TreZapalooza
OutputDir=setups
OutputBaseFilename=Setup {#MyAppName} {#MyAppVersionText}
Compression=lzma2
SolidCompression=yes
LZMANumBlockThreads=8
ArchitecturesInstallIn64BitMode=x64compatible arm64
ChangesAssociations=yes
ArchitecturesAllowed=x64compatible arm64
AllowNoIcons=yes
SetupIconFile={#MyAppIcon}
UninstallDisplayIcon={app}\{#MyAppExeName}
LicenseFile= LICENSE
WizardStyle= modern
SetupLogging=yes
MinVersion={#min_windows}

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}";

[Types]
Name: "full"; Description: "Full installation"
Name: "minimal"; Description: "Minimal installation"
Name: "custom"; Description: "Custom installation"; Flags: iscustom

[Components]
Name: "core";             Description: "TreZapalooza"; Types: full minimal custom; Flags: fixed
Name: "lttp_sprites";     Description: "Download ""A Link to the Past"" player sprites"; Types: full;

[Dirs]
NAME: "{app}"; Flags: setntfscompression; Permissions: everyone-modify users-modify authusers-modify;

[Files]
Source: "{#source_path}\*"; Excludes: "*.sfc, *.log, data\sprites\alttpr, SNI, EnemizerCLI"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#source_path}\SNI\*"; Excludes: "*.sfc, *.log"; DestDir: "{app}\SNI"; Flags: ignoreversion recursesubdirs createallsubdirs;
Source: "{#source_path}\EnemizerCLI\*"; Excludes: "*.sfc, *.log"; DestDir: "{app}\EnemizerCLI"; Flags: ignoreversion recursesubdirs createallsubdirs;
Source: "vc_redist.x64.exe"; DestDir: {tmp}; Flags: deleteafterinstall

[Icons]
Name: "{group}\{#MyAppName} Folder"; Filename: "{app}";
Name: "{group}\{#MyAppName} Launcher"; Filename: "{app}\TreZapaloozaLauncher.exe"

Name: "{commondesktop}\{#MyAppName} Folder"; Filename: "{app}"; Tasks: desktopicon
Name: "{commondesktop}\{#MyAppName} Launcher"; Filename: "{app}\TreZapaloozaLauncher.exe"; Tasks: desktopicon

[Run]

Filename: "{tmp}\vc_redist.x64.exe"; Parameters: "/passive /norestart"; Check: IsVCRedist64BitNeeded; StatusMsg: "Installing VC++ redistributable..."
Filename: "{app}\TreZapaloozaLttPAdjuster"; Parameters: "--update_sprites"; StatusMsg: "Updating Sprite Library..."; Components: lttp_sprites
Filename: "{app}\TreZapaloozaLauncher"; Parameters: "--update_settings"; StatusMsg: "Updating host.yaml..."; Flags: runasoriginaluser runhidden
Filename: "{app}\TreZapaloozaLauncher"; Description: "{cm:LaunchProgram,{#StringChange('Launcher', '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: dirifempty; Name: "{app}"

[InstallDelete]
Type: files; Name: "{app}\lib\worlds\_bizhawk.apworld"
Type: files; Name: "{app}\TreZapaloozaLttPClient.exe"
Type: files; Name: "{app}\TreZapaloozaPokemonClient.exe"
Type: files; Name: "{app}\data\lua\connector_pkmn_rb.lua"
Type: filesandordirs; Name: "{app}\lib\worlds\rogue-legacy"
Type: dirifempty; Name: "{app}\lib\worlds\rogue-legacy"
Type: files; Name: "{app}\lib\worlds\sc2wol.apworld"
Type: filesandordirs; Name: "{app}\lib\worlds\sc2wol"
Type: dirifempty; Name: "{app}\lib\worlds\sc2wol"
Type: filesandordirs; Name: "{app}\lib\worlds\bk_sudoku"
Type: dirifempty; Name: "{app}\lib\worlds\bk_sudoku"
Type: files; Name: "{app}\TreZapaloozaLauncher(DEBUG).exe"
Type: filesandordirs; Name: "{app}\SNI\lua*"
Type: filesandordirs; Name: "{app}\EnemizerCLI*"
#include "installdelete.iss"

[Registry]

Root: HKCR; Subkey: ".aplttp";                                   ValueData: "{#MyAppName}patch";        Flags: uninsdeletevalue; ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}patch";                         ValueData: "TreZapalooza Binary Patch"; Flags: uninsdeletekey;   ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}patch\DefaultIcon";             ValueData: "{app}\TreZapaloozaSNIClient.exe,0";                  ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}patch\shell\open\command";      ValueData: """{app}\TreZapaloozaSNIClient.exe"" ""%1""";         ValueType: string;  ValueName: "";

Root: HKCR; Subkey: ".apsm";                                     ValueData: "{#MyAppName}smpatch";        Flags: uninsdeletevalue; ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}smpatch";                       ValueData: "TreZapalooza Super Metroid Patch"; Flags: uninsdeletekey;   ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}smpatch\DefaultIcon";           ValueData: "{app}\TreZapaloozaSNIClient.exe,0";                           ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}smpatch\shell\open\command";    ValueData: """{app}\TreZapaloozaSNIClient.exe"" ""%1""";                  ValueType: string;  ValueName: "";

Root: HKCR; Subkey: ".apdkc3";                                   ValueData: "{#MyAppName}dkc3patch";        Flags: uninsdeletevalue; ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}dkc3patch";                     ValueData: "TreZapalooza Donkey Kong Country 3 Patch"; Flags: uninsdeletekey;   ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}dkc3patch\DefaultIcon";         ValueData: "{app}\TreZapaloozaSNIClient.exe,0";                           ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}dkc3patch\shell\open\command";  ValueData: """{app}\TreZapaloozaSNIClient.exe"" ""%1""";                  ValueType: string;  ValueName: "";

Root: HKCR; Subkey: ".apsmw";                                    ValueData: "{#MyAppName}smwpatch";        Flags: uninsdeletevalue; ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}smwpatch";                      ValueData: "TreZapalooza Super Mario World Patch"; Flags: uninsdeletekey;   ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}smwpatch\DefaultIcon";          ValueData: "{app}\TreZapaloozaSNIClient.exe,0";                           ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}smwpatch\shell\open\command";   ValueData: """{app}\TreZapaloozaSNIClient.exe"" ""%1""";                  ValueType: string;  ValueName: "";

Root: HKCR; Subkey: ".apzl";                                     ValueData: "{#MyAppName}zlpatch";        Flags: uninsdeletevalue; ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}zlpatch";                       ValueData: "TreZapalooza Zillion Patch"; Flags: uninsdeletekey;   ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}zlpatch\DefaultIcon";           ValueData: "{app}\TreZapaloozaZillionClient.exe,0";                           ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}zlpatch\shell\open\command";    ValueData: """{app}\TreZapaloozaZillionClient.exe"" ""%1""";                  ValueType: string;  ValueName: "";

Root: HKCR; Subkey: ".apsmz3";                                   ValueData: "{#MyAppName}smz3patch";        Flags: uninsdeletevalue; ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}smz3patch";                     ValueData: "TreZapalooza SMZ3 Patch"; Flags: uninsdeletekey;   ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}smz3patch\DefaultIcon";         ValueData: "{app}\TreZapaloozaSNIClient.exe,0";                           ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}smz3patch\shell\open\command";  ValueData: """{app}\TreZapaloozaSNIClient.exe"" ""%1""";                  ValueType: string;  ValueName: "";

Root: HKCR; Subkey: ".apsoe";                                    ValueData: "{#MyAppName}soepatch";        Flags: uninsdeletevalue; ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}soepatch";                      ValueData: "TreZapalooza Secret of Evermore Patch"; Flags: uninsdeletekey;   ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}soepatch\DefaultIcon";          ValueData: "{app}\TreZapaloozaSNIClient.exe,0";                           ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}soepatch\shell\open\command";   ValueData: """{app}\TreZapaloozaSNIClient.exe"" ""%1""";                  ValueType: string;  ValueName: "";

Root: HKCR; Subkey: ".apl2ac";                                   ValueData: "{#MyAppName}l2acpatch";        Flags: uninsdeletevalue; ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}l2acpatch";                     ValueData: "TreZapalooza Lufia II Ancient Cave Patch"; Flags: uninsdeletekey;   ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}l2acpatch\DefaultIcon";         ValueData: "{app}\TreZapaloozaSNIClient.exe,0";                           ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}l2acpatch\shell\open\command";  ValueData: """{app}\TreZapaloozaSNIClient.exe"" ""%1""";                  ValueType: string;  ValueName: "";

Root: HKCR; Subkey: ".apkdl3";                                   ValueData: "{#MyAppName}kdl3patch";        Flags: uninsdeletevalue; ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}kdl3patch";                     ValueData: "TreZapalooza Kirby's Dream Land 3 Patch"; Flags: uninsdeletekey;   ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}kdl3patch\DefaultIcon";         ValueData: "{app}\TreZapaloozaSNIClient.exe,0";                           ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}kdl3patch\shell\open\command";  ValueData: """{app}\TreZapaloozaSNIClient.exe"" ""%1""";                  ValueType: string;  ValueName: "";

Root: HKCR; Subkey: ".apmc";                                     ValueData: "{#MyAppName}mcdata";         Flags: uninsdeletevalue; ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}mcdata";                        ValueData: "TreZapalooza Minecraft Data"; Flags: uninsdeletekey;   ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}mcdata\DefaultIcon";            ValueData: "{app}\TreZapaloozaMinecraftClient.exe,0";                           ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}mcdata\shell\open\command";     ValueData: """{app}\TreZapaloozaMinecraftClient.exe"" ""%1""";                  ValueType: string;  ValueName: "";

Root: HKCR; Subkey: ".apz5";                                     ValueData: "{#MyAppName}n64zpf";         Flags: uninsdeletevalue; ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}n64zpf";                        ValueData: "TreZapalooza Ocarina of Time Patch"; Flags: uninsdeletekey;   ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}n64zpf\DefaultIcon";            ValueData: "{app}\TreZapaloozaOoTClient.exe,0";                           ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}n64zpf\shell\open\command";     ValueData: """{app}\TreZapaloozaOoTClient.exe"" ""%1""";                  ValueType: string;  ValueName: "";

Root: HKCR; Subkey: ".apred";                                    ValueData: "{#MyAppName}pkmnrpatch";        Flags: uninsdeletevalue; ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}pkmnrpatch";                    ValueData: "TreZapalooza Pokemon Red Patch"; Flags: uninsdeletekey;   ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}pkmnrpatch\DefaultIcon";        ValueData: "{app}\TreZapaloozaBizHawkClient.exe,0";                           ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}pkmnrpatch\shell\open\command"; ValueData: """{app}\TreZapaloozaBizHawkClient.exe"" ""%1""";                  ValueType: string;  ValueName: "";

Root: HKCR; Subkey: ".apblue";                                   ValueData: "{#MyAppName}pkmnbpatch";        Flags: uninsdeletevalue; ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}pkmnbpatch";                    ValueData: "TreZapalooza Pokemon Blue Patch"; Flags: uninsdeletekey;   ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}pkmnbpatch\DefaultIcon";        ValueData: "{app}\TreZapaloozaBizHawkClient.exe,0";                           ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}pkmnbpatch\shell\open\command"; ValueData: """{app}\TreZapaloozaBizHawkClient.exe"" ""%1""";                  ValueType: string;  ValueName: "";

Root: HKCR; Subkey: ".apbn3";                                    ValueData: "{#MyAppName}bn3bpatch";        Flags: uninsdeletevalue; ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}bn3bpatch";                     ValueData: "TreZapalooza MegaMan Battle Network 3 Patch"; Flags: uninsdeletekey;   ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}bn3bpatch\DefaultIcon";         ValueData: "{app}\TreZapaloozaMMBN3Client.exe,0";                           ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}bn3bpatch\shell\open\command";  ValueData: """{app}\TreZapaloozaMMBN3Client.exe"" ""%1""";                  ValueType: string;  ValueName: "";

Root: HKCR; Subkey: ".apemerald";                                 ValueData: "{#MyAppName}pkmnepatch";                               Flags: uninsdeletevalue; ValueType: string; ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}pkmnepatch";                     ValueData: "TreZapalooza Pokemon Emerald Patch";                    Flags: uninsdeletekey;   ValueType: string; ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}pkmnepatch\DefaultIcon";         ValueData: "{app}\TreZapaloozaBizHawkClient.exe,0";                                          ValueType: string; ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}pkmnepatch\shell\open\command";  ValueData: """{app}\TreZapaloozaBizHawkClient.exe"" ""%1""";                                 ValueType: string; ValueName: "";

Root: HKCR; Subkey: ".apmlss";                                 ValueData: "{#MyAppName}mlsspatch";                               Flags: uninsdeletevalue; ValueType: string; ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}mlsspatch";                     ValueData: "TreZapalooza Mario & Luigi Superstar Saga Patch";                    Flags: uninsdeletekey;   ValueType: string; ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}mlsspatch\DefaultIcon";         ValueData: "{app}\TreZapaloozaBizHawkClient.exe,0";                                          ValueType: string; ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}mlsspatch\shell\open\command";  ValueData: """{app}\TreZapaloozaBizHawkClient.exe"" ""%1""";                                 ValueType: string; ValueName: "";

Root: HKCR; Subkey: ".apcv64";                                 ValueData: "{#MyAppName}cv64patch";                               Flags: uninsdeletevalue; ValueType: string; ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}cv64patch";                     ValueData: "TreZapalooza Castlevania 64 Patch";                    Flags: uninsdeletekey;   ValueType: string; ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}cv64patch\DefaultIcon";         ValueData: "{app}\TreZapaloozaBizHawkClient.exe,0";                                          ValueType: string; ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}cv64patch\shell\open\command";  ValueData: """{app}\TreZapaloozaBizHawkClient.exe"" ""%1""";                                 ValueType: string; ValueName: "";

Root: HKCR; Subkey: ".apmm2";                                   ValueData: "{#MyAppName}mm2patch";                               Flags: uninsdeletevalue; ValueType: string; ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}mm2patch";                     ValueData: "TreZapalooza Mega Man 2 Patch";                    Flags: uninsdeletekey;   ValueType: string; ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}mm2patch\DefaultIcon";         ValueData: "{app}\TreZapaloozaBizHawkClient.exe,0";                                          ValueType: string; ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}mm2patch\shell\open\command";  ValueData: """{app}\TreZapaloozaBizHawkClient.exe"" ""%1""";                                 ValueType: string; ValueName: "";

Root: HKCR; Subkey: ".apladx";                                   ValueData: "{#MyAppName}ladxpatch";        Flags: uninsdeletevalue; ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}ladxpatch";                     ValueData: "TreZapalooza Links Awakening DX Patch"; Flags: uninsdeletekey;   ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}ladxpatch\DefaultIcon";         ValueData: "{app}\TreZapaloozaLinksAwakeningClient.exe,0";                           ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}ladxpatch\shell\open\command";  ValueData: """{app}\TreZapaloozaLinksAwakeningClient.exe"" ""%1""";                  ValueType: string;  ValueName: "";

Root: HKCR; Subkey: ".aptloz";                                   ValueData: "{#MyAppName}tlozpatch";        Flags: uninsdeletevalue; ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}tlozpatch";                     ValueData: "TreZapalooza The Legend of Zelda Patch"; Flags: uninsdeletekey;   ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}tlozpatch\DefaultIcon";         ValueData: "{app}\TreZapaloozaZelda1Client.exe,0";                           ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}tlozpatch\shell\open\command";  ValueData: """{app}\TreZapaloozaZelda1Client.exe"" ""%1""";                  ValueType: string;  ValueName: "";

Root: HKCR; Subkey: ".apadvn";                                   ValueData: "{#MyAppName}advnpatch";        Flags: uninsdeletevalue; ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}advnpatch";                     ValueData: "TreZapalooza Adventure Patch";  Flags: uninsdeletekey;   ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}advnpatch\DefaultIcon";         ValueData: "{app}\TreZapaloozaAdventureClient.exe,0";                ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}advnpatch\shell\open\command";  ValueData: """{app}\TreZapaloozaAdventureClient.exe"" ""%1""";       ValueType: string;  ValueName: "";

Root: HKCR; Subkey: ".apyi";                                   ValueData: "{#MyAppName}yipatch";        Flags: uninsdeletevalue; ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}yipatch";                     ValueData: "TreZapalooza Yoshi's Island Patch"; Flags: uninsdeletekey;   ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}yipatch\DefaultIcon";         ValueData: "{app}\TreZapaloozaSNIClient.exe,0";                           ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}yipatch\shell\open\command";  ValueData: """{app}\TreZapaloozaSNIClient.exe"" ""%1""";                  ValueType: string;  ValueName: "";

Root: HKCR; Subkey: ".apygo06";                                   ValueData: "{#MyAppName}ygo06patch";        Flags: uninsdeletevalue; ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}ygo06patch";                     ValueData: "TreZapalooza Yu-Gi-Oh 2006 Patch"; Flags: uninsdeletekey;   ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}ygo06patch\DefaultIcon";         ValueData: "{app}\TreZapaloozaBizHawkClient.exe,0";                           ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}ygo06patch\shell\open\command";  ValueData: """{app}\TreZapaloozaBizHawkClient.exe"" ""%1""";                  ValueType: string;  ValueName: "";

Root: HKCR; Subkey: ".TreZapalooza";                              ValueData: "{#MyAppName}multidata";        Flags: uninsdeletevalue; ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}multidata";                     ValueData: "TreZapalooza Server Data";      Flags: uninsdeletekey;   ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}multidata\DefaultIcon";         ValueData: "{app}\TreZapaloozaServer.exe,0";                         ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}multidata\shell\open\command";  ValueData: """{app}\TreZapaloozaServer.exe"" ""%1""";                ValueType: string;  ValueName: "";

Root: HKCR; Subkey: ".apworld";                                 ValueData: "{#MyAppName}worlddata";  Flags: uninsdeletevalue; ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}worlddata";                    ValueData: "TreZapalooza World Data"; Flags: uninsdeletekey;   ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}worlddata\DefaultIcon";        ValueData: "{app}\TreZapaloozaLauncher.exe,0";                 ValueType: string;  ValueName: "";
Root: HKCR; Subkey: "{#MyAppName}worlddata\shell\open\command"; ValueData: """{app}\TreZapaloozaLauncher.exe"" ""%1""";        ValueType: string;  ValueName: "";

Root: HKCR; Subkey: "trezapalooza"; ValueType: "string"; ValueData: "TreZapalooza Protocol"; Flags: uninsdeletekey;
Root: HKCR; Subkey: "trezapalooza"; ValueType: "string"; ValueName: "URL Protocol"; ValueData: "";
Root: HKCR; Subkey: "trezapalooza\DefaultIcon"; ValueType: "string"; ValueData: "{app}\TreZapaloozaLauncher.exe,0";
Root: HKCR; Subkey: "trezapalooza\shell\open\command"; ValueType: "string"; ValueData: """{app}\TreZapaloozaLauncher.exe"" ""%1""";

[Code]
// See: https://stackoverflow.com/a/51614652/2287576
function IsVCRedist64BitNeeded(): boolean;
var
  strVersion: string;
begin
  if (RegQueryStringValue(HKEY_LOCAL_MACHINE,
    'SOFTWARE\Microsoft\VisualStudio\14.0\VC\Runtimes\x64', 'Version', strVersion)) then
  begin
    // Is the installed version at least the packaged one ?
    Log('VC Redist x64 Version : found ' + strVersion);
    Result := (CompareStr(strVersion, 'v14.38.33130') < 0);
  end
  else
  begin
    // Not even an old version installed
    Log('VC Redist x64 is not already installed');
    Result := True;
  end;
end;
