# QTube

QTube is a comprehensive YouTube downloader with a modern GUI, featuring an integrated media player with advanced playback capabilities. This application is designed to efficiently manage and play media files, leveraging multithreading for smooth performance. It includes robust features for video and audio playback, media management, and user interaction.

## Features

- **YouTube Downloader**: Easily download videos from YouTube with a user-friendly interface.
- **Integrated Media Player**: Play downloaded videos or other media files directly within the application.
- **Multithreading**: Ensures smooth performance and responsive user experience.
- **Media Management**: Organize and manage your media library with ease.
- **Customizable Playback**: Control playback speed, volume, and seek within media files.
- **History Tracking**: Keeps a record of played media and their playback states.
- **Fullscreen Video Playback**: Enjoy videos in fullscreen mode with easy toggling.
- **Playback Controls**: Includes play, pause, stop, next, previous, seek, and volume control functionalities.
- **Playlist Support**: Create and manage playlists for seamless media playback.
- **Repeat and Shuffle**: Toggle repeat and shuffle modes for personalized listening experiences.
- **Volume Control**: Mute, unmute, and adjust volume levels.
- **Media Notifications**: Provides notifications for various media states and actions.

## File Descriptions

### `mediaplayerthread.py`

This file defines the core media player functionality using the PyQt5 framework. It sets up the media player, manages the media playlist, and handles various playback controls. Key features include:

- **Media Player Initialization**: Sets up the QMediaPlayer and QMediaPlaylist for video and audio playback.
- **UI Connection**: Connects UI elements like buttons, sliders, and labels to their respective functions.
- **Signal Handling**: Connects media player signals to update the UI and handle state changes.
- **Playback Control**: Implements play, pause, stop, next, previous, seek, volume control, mute, repeat, and shuffle functionalities.
- **Fullscreen Toggle**: Manages fullscreen mode for video playback.
- **Media Loading**: Loads media files into the playlist and handles new folder selections.
- **State Persistence**: Keeps a record of the application's state using JSON for session management.

### `videowindow.py`

This file defines a separate window for fullscreen video playback. It uses QVideoWidget to display video content and manages fullscreen toggling and window movement. Key features include:

- **Fullscreen Video**: Provides a fullscreen window for video playback.
- **Mouse and Keyboard Events**: Handles double-click events for toggling fullscreen mode and various keyboard shortcuts for playback control.
- **Window Movement**: Allows dragging the window using the mouse when not in fullscreen mode.

### `historymanager.py`

This file manages the history of media playback using a history file stored in a specified application directory. It tracks played media, including their playback times and locations. Key features include:

- **History Management**: Adds, retrieves, and saves playback history.
- **Persistence**: Uses pickle to serialize and deserialize history data.
- **Directory Management**: Ensures the application directory exists and creates it if necessary.

## Usage

1. **Download and Install**: Clone the repository and install the required dependencies.
2. **Run the Application**: Execute the main script to launch the QTube application.
3. **Download YouTube Videos**: Use the downloader feature to download videos.
4. **Play Media**: Use the integrated media player to play downloaded videos or other media files.
5. **Manage Playback**: Utilize playback controls, adjust volume, seek within media files, and toggle fullscreen mode.
6. **Organize Media**: Add media files to the playlist and manage your media library.
7. **Track History**: Access the playback history to see previously played media and their states.

## Installation

To install and run QTube, follow these steps:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/QTube.git
   cd QTube
