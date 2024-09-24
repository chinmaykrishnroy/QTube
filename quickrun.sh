#!/bin/bash
set -e

# Get the absolute path of the current directory
PROJECT_DIR="$(dirname "$(readlink -f "$0")")"
cd "$PROJECT_DIR"

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "Python not found. Please install Python to continue."
    exit 1
fi

# Set the virtual environment directory
VENV_DIR="$PROJECT_DIR/venv"

# Check if the virtual environment directory exists
if [ ! -f "$VENV_DIR/bin/python" ]; then
    echo "Virtual environment not found. Running run.sh to create it..."
    bash "$PROJECT_DIR/run.sh"
    exit
fi

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

# Clear terminal screen
clear

# Run the main Python script
python "$PROJECT_DIR/main.py"

# Deactivate the virtual environment
deactivate
