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

:: Run the main Python script
python "%PROJECT_DIR%main.py"

:: Deactivate the virtual environment
deactivate

endlocal
