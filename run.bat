@echo off
setlocal

:: Get the absolute path of the current directory
set "PROJECT_DIR=%~dp0"
cd /d "%PROJECT_DIR%"

:: Check if Python is installed
where /q python
if errorlevel 1 (
    echo Python not found. Please install Python to continue.
    exit /b 1
)

:: Set the virtual environment directory
set "VENV_DIR=%PROJECT_DIR%venv"

:: Check if the virtual environment already exists
if not exist "%VENV_DIR%\Scripts\python.exe" (
    echo Creating virtual environment...
    python -m venv "%VENV_DIR%"
)

:: Activate the virtual environment
call "%VENV_DIR%\Scripts\activate.bat"

:: Upgrade pip and install the required packages
python -m pip install -r "%PROJECT_DIR%requirements.txt" --no-cache-dir

:: Check if the system is Windows 10 or above
ver | findstr /r "10\..* [1-9][0-9]*\." >nul
if errorlevel 1 (
    echo Windows version is below 10. Please manually install FFmpeg and K-Lite Codec Pack.
) else (
    :: Check if FFmpeg is already installed
    where /q ffmpeg
    if errorlevel 1 (
        echo FFmpeg not found. Installing FFmpeg using winget...
        winget install Gyan.FFmpeg
        if errorlevel 1 (
            echo Failed to install FFmpeg. Please download and install it manually.
        )
    ) else (
        echo FFmpeg is already installed. Skipping installation.
    )

    :: Check if K-Lite Codec Pack is already installed
    winget list | findstr /i "K-Lite Codec Pack" >nul
    if errorlevel 1 (
        echo K-Lite Codec Pack not found. Installing K-Lite Codec Pack using winget...
        winget install CodecGuide.K-LiteCodecPack.Full
        if errorlevel 1 (
            echo Failed to install K-Lite Codec Pack. Please download and install it manually.
        )
    ) else (
        echo K-Lite Codec Pack is already installed. Skipping installation.
    )
)

cls
:: Run the main Python script
python "%PROJECT_DIR%main.py"

:: Deactivate the virtual environment
deactivate

endlocal
