$Env:ENEMIZER_VERSION = '7.1'
$Env:APPIMAGETOOL_VERSION = '13'
Write-Output "### Clean up old builds ###"
Remove-Item -path .\build\  -Recurse
Remove-Item -path .\dist\  -Recurse
Write-Output "### Starting Build ###"
python setup.py build_exe --yes
Write-Output "### Preparing Folder structure ###"
New-Item -Path dist -ItemType Directory -Force
$NAME="$(ls build | Select-String -Pattern 'exe')".Split('.',2)[1]
$ZIP_NAME="Trezipelago_latest_$NAME.7z"
cd .\build\
Rename-Item "exe.$NAME" Archipelago
Write-Output "### Adding Dolphin memory engine and other libs ###"
Copy-Item -Path "..\lib\*" -Destination ".\Archipelago\lib\" -Recurse
Write-Output "### Archive Build ###"
C:\"Program Files"\7-Zip\7z.exe a -mx=9 -mhe=on -ms "../dist/$ZIP_NAME" Archipelago
cd ..