#!/bin/bash
set -e

# Define paths
TARGET_PATH="$(dirname "$(readlink -f "$0")")/quickrun.sh"  # Path to the script to create a shortcut for
ICON_PATH="$(dirname "$(readlink -f "$0")")/icon"     # Path to the icon file
SHORTCUT_NAME="QTube"
SHORTCUT_PATH="$HOME/Desktop/$SHORTCUT_NAME.desktop"         # Shortcut on the Desktop

# Create the .desktop shortcut file
echo "[Desktop Entry]" > "$SHORTCUT_PATH"
echo "Version=1.0" >> "$SHORTCUT_PATH"
echo "Name=$SHORTCUT_NAME" >> "$SHORTCUT_PATH"
echo "Exec=$TARGET_PATH" >> "$SHORTCUT_PATH"
echo "Icon=$ICON_PATH" >> "$SHORTCUT_PATH"
echo "Terminal=false" >> "$SHORTCUT_PATH"  # To hide the terminal
echo "Type=Application" >> "$SHORTCUT_PATH"
echo "Categories=Application;" >> "$SHORTCUT_PATH"

# Make the .desktop file executable
chmod +x "$SHORTCUT_PATH"

echo "Shortcut created at: $SHORTCUT_PATH"
