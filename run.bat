@echo off
REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python and try again.
    timeout /t 3
    exit /b
)

REM Check if the venv package is available
python -c "import venv" >nul 2>&1
if errorlevel 1 (
    echo venv package is not available. Installing venv...
    pip install virtualenv
    if errorlevel 1 (
        echo Failed to install virtualenv. Please check your Python and pip installation.
        timeout /t 3
        exit /b
    )
)

REM Check if the virtual environment exists
if not exist .venv (
    echo Creating virtual environment...
    python -m venv .venv
)

REM Activate the virtual environment and install packages
call .venv\Scripts\activate.bat
pip install PyQt5==5.15.11 yt-dlp==2024.8.6 youtube-search-python==1.6.6
python main.py
call .venv\Scripts\deactivate.bat
