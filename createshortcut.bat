@echo off
setlocal

:: Define paths
set "TARGET_PATH=%~dp0run.bat"  :: Path to the batch file you want to create a shortcut for
set "ICON_PATH=%~dp0youtube.ico" :: Path to the icon file in the current directory
set "SHORTCUT_NAME=QTube"
set "SHORTCUT_PATH=%~dp0%SHORTCUT_NAME%.lnk"

:: Create the shortcut using PowerShell
powershell -command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%SHORTCUT_PATH%'); $s.TargetPath = '%TARGET_PATH%'; $s.IconLocation = '%ICON_PATH%'; $s.Save()"

echo Shortcut created: %SHORTCUT_PATH%

endlocal
