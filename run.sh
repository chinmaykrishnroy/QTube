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

# Check if the virtual environment already exists
if [ ! -f "$VENV_DIR/bin/python" ]; then
    echo "Creating virtual environment..."
    python -m venv "$VENV_DIR"
fi

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

# Upgrade pip and install the required packages
python -m pip install -r "$PROJECT_DIR/requirements.txt" --no-cache-dir

# Check if FFmpeg is installed
if ! command -v ffmpeg &> /dev/null; then
    echo "FFmpeg not found. Installing FFmpeg..."
    sudo apt update && sudo apt install -y ffmpeg
    if [ $? -ne 0 ]; then
        echo "Failed to install FFmpeg. Please install it manually."
        exit 1
    fi
else
    echo "FFmpeg is already installed. Skipping installation."
fi

# Since K-Lite Codec Pack is Windows-specific, skip it or handle any Linux alternatives if needed
# For example, we could add installation instructions for a media codec package
# sudo apt install ubuntu-restricted-extras (optional, depending on your need)

# Clear terminal screen
clear

# Run the main Python script
python "$PROJECT_DIR/main.py"

# Deactivate the virtual environment
deactivate
