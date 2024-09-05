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

:: Function to delete the virtual environment
:DELETE_VENV
echo Attempting to delete virtual environment...
rmdir /s /q "%VENV_DIR%"
if exist "%VENV_DIR%" (
    echo Deletion failed, retrying...
    timeout 3
    rmdir /s /q "%VENV_DIR%"
    if exist "%VENV_DIR%" (
        echo Deletion failed again. Please manually remove the virtual environment.
        exit /b 1
    )
)
echo Virtual environment deleted successfully.

:: Check if the virtual environment already exists
if not exist "%VENV_DIR%\Scripts\python.exe" (
    echo Creating virtual environment...
    python -m venv "%VENV_DIR%"
    if errorlevel 1 (
        echo Failed to create virtual environment.
        call :DELETE_VENV
        timeout 3 /nobreak >nul
        exit /b 1
    )
)

:: Activate the virtual environment
call "%VENV_DIR%\Scripts\activate.bat"
if errorlevel 1 (
    echo Failed to activate virtual environment.
    call :DELETE_VENV
    timeout 3 /nobreak >nul
    exit /b 1
)

:: Upgrade pip and install the required packages
python -m pip install --upgrade pip --no-cache-dir
if errorlevel 1 (
    echo Failed to upgrade pip.
    call :DELETE_VENV
    timeout 3 /nobreak >nul
    exit /b 1
)
python -m pip install -r "%PROJECT_DIR%requirements.txt" --no-cache-dir
if errorlevel 1 (
    echo Failed to install required packages.
    call :DELETE_VENV
    timeout 3 /nobreak >nul
    exit /b 1
)

:: Run the main Python script
python "%PROJECT_DIR%main.py"
if errorlevel 1 (
    echo Python script encountered a fatal error.
    call :DELETE_VENV
    timeout 3 /nobreak >nul
    deactivate
    exit /b 1
)

:: Deactivate the virtual environment
deactivate

timeout 3 /nobreak >nul

endlocal