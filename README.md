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

MainWindow UI

This project implements the main user interface (UI) for a multimedia downloader and player using PyQt5 in Python.

### MainThread

The `MainWindow` class in this PyQt5 application orchestrates a comprehensive multimedia management interface. It inherits from QMainWindow and integrates various features and functionalities. Upon initialization, it sets up the UI defined in Ui_MainWindow, configures window flags for a frameless appearance, and initializes several default settings and variables related to playback, file management, and UI state. Key components include a media player (MediaPlayer), file watching system (FileWatcherSystem), history manager (HistoryManager), and internet checker (InternetChecker). Signals and slots are extensively utilized for updating UI elements dynamically and handling user interactions, such as toggling sidebar visibility, managing download actions, updating file lists, and controlling multimedia playback. The class supports drag-and-drop functionality for local file playback and integrates web browser redirections for external links. Notably, it includes state management methods (loadState, saveState) for persisting user preferences and application settings. Overall, MainWindow encapsulates a robust multimedia application interface with responsive user controls and integrated multimedia handling capabilities

- **Frameless Window Design**: Utilizes `Qt.FramelessWindowHint` to create a modern and sleek user interface.
- **Multimedia Playback**: Integrates MediaPlayer for local media playback and manages playback controls such as play, pause, stop, and volume adjustment.
- **Drag-and-Drop Support**: Enables users to drag and drop files for playback or to add them to the download queue.
- **File Management**: Includes features like sorting files, refreshing file lists, and handling default download directories.
- **Internet Connectivity**: Monitors internet status using `InternetChecker` and provides notifications based on connectivity changes.
- **Search Functionality**: Allows users to search YouTube for videos, displaying results and enabling download directly from search queries.
- **Settings and Help Menus**: Includes settings for default download directories, notification preferences, and theme selection. Also provides a help menu with additional information.
- **Notification System**: Implements a notification framework to alert users of events such as download completions and internet connectivity status.
- **Theme Customization**: Supports loading and switching between dark and light themes based on user preference.
- **External Links Integration**: Provides buttons to open external links to YouTube, GitHub, LinkedIn, and Instagram profiles for further interaction.

### Interface

The `Ui_MainWindow` class in this PyQt5 application serves as the central hub for a multimedia downloader and player interface. It orchestrates a rich set of features, beginning with a responsive menu toggle button that controls the visibility of the menu bar. The class dynamically manages video containers populated with thumbnails and duration labels, facilitating intuitive video browsing. Download functionality is robust, allowing users to initiate downloads with customizable video resolutions, while progress indicators and real-time internet speed updates enhance user feedback during downloads. A comprehensive history display chronicles downloaded items, providing details such as title, URL, elapsed time, and storage location. File management capabilities include playback controls and detailed metadata (size, type, modification time) for listed files. Error handling mechanisms ensure users are promptly notified of download errors, while resume and pause functionalities add flexibility to ongoing downloads. Overall, the Ui_MainWindow class seamlessly integrates PyQt5 widgets and custom components to deliver a user-friendly interface for multimedia management and playback.

- **Menu and Toggle Button**: Includes a menu toggle button with an icon for toggling the menu bar visibility.
- **Video Management**: Dynamically adds video containers with thumbnails and duration labels based on provided video data.
- **Download Control**: Provides buttons for starting downloads with options for different video resolutions.
- **Download Progress**: Updates download progress, internet speed, and status labels dynamically.
- **History Display**: Shows a history of downloaded items with details like title, URL, time elapsed, and location.
- **File Management**: Displays files with options for playback and file details (size, type, last modified time).
- **Error Handling**: Displays notifications for download errors and handles resume/pause functionalities.

### Directory Scanner and File Watcher System

The `DirectoryScanner` and `FileWatcherSystem` classes are PyQt5-based components for monitoring and managing directories and files within a PyQt5 application. The `DirectoryScanner` class scans a specified directory for files and emits a signal when files are changed.

- **Continuous Scanning**: Continuously scans the directory for changes.
- **Rescan Request**: Allows requesting a manual rescan of the directory.
- **File Information**: Emits a signal with detailed information about the files (name, path, type, size, modification time) when changes are detected.

### Media Player

`MediaPlayer` is a PyQt5-based class that manages audio and video playback within a PyQt5 application. It provides a feature-rich media player with capabilities such as full-screen video playback, volume and playback control, and integration with a playlist.

- **Fullscreen Video Playback**: Supports a separate window for fullscreen video playback.
- **Mouse and Keyboard Events**: Handles double-click events for toggling fullscreen mode and various keyboard shortcuts for playback control.
- **Window Movement**: Allows dragging the window using the mouse when not in fullscreen mode.
- **Volume Control**: Adjust volume and mute/unmute functionality.
- **Playback Control**: Play, pause, stop, next, previous, seek forward, and seek backward functionality.
- **Playlist Management**: Supports loading, shuffling, and repeating media files from a specified directory.
- **Playback Speed Control**: Allows changing the playback speed.
- **UI Integration**: Connects to a UI with buttons and sliders for interactive control.

### Video Window

The video window defines a separate window for fullscreen video playback. It uses QVideoWidget to display video content and manages fullscreen toggling and window movement. Key features include:

- **Fullscreen Video**: Provides a fullscreen window for video playback.
- **Mouse and Keyboard Events**: Handles double-click events for toggling fullscreen mode and various keyboard shortcuts for playback control.
- **Window Movement**: Allows dragging the window using the mouse when not in fullscreen mode.

### History Manager

The `HistoryManager` class manages a history of items with time, elapsed time, location, URL, and title attributes, storing them in a pickle file. It also allows storing and retrieving history items, enabling management of user activity records within an application.

- **History Storage**: Saves history items including time, elapsed time, location, URL, and title to a file.
- **Persistence**: Uses pickle serialization for saving and loading history data.
- **Data Integrity**: Ensures existing data directory and handles file operations safely.

### Download Thread

The `DownloadThread` class is a PyQt5-based thread for downloading media content using `yt_dlp`. It provides functionality for downloading audio and video files from various sources such as YouTube, with progress reporting and error handling. It enables downloading media content with support for pausing, resuming, and terminating downloads. It integrates with PyQt5 for signals and threading management.

- **Download Formats**: Supports different download formats based on the type (audio or video) specified during initialization.
- **Progress Reporting**: Reports download progress including downloaded size, progress percentage, estimated time remaining, and download speed.
- **Pause and Resume**: Allows pausing and resuming downloads.
- **Error Handling**: Handles download errors and reports them to the UI if provided.
- **Custom Logging**: Provides custom logging for debug, info, warning, and error messages, displaying them in the UI if provided.

### Search Thread

The `SearchThread` class in PyQt5 encapsulates searching functionality using the YouTube API or generating random video data in case of an error. It runs asynchronously in a thread, emitting a signal with a list of video data upon completion. This class allows searching YouTube videos based on a query using the `youtubesearchpython` library. It handles errors gracefully by generating random video data when unable to perform the search. This class is designed to be used in PyQt5 applications for background tasks that involve fetching or generating video information.

- **YouTube Video Search**: Searches YouTube videos based on a query using the `youtubesearchpython` library.
- **Random Video Generation**: Generates random video data in case of search errors.
- **Asynchronous Execution**: Runs in a separate thread (`QThread`) to keep the UI responsive.
- **Error Handling**: Handles exceptions during YouTube searches and updates the UI accordingly.

### Image Downloader

The `ImageDownloader` class is a PyQt5-based thread for downloading images from a URL using `requests` and emitting signals upon successful download. This class facilitates asynchronous image downloads in PyQt5 applications. It fetches images from a specified URL and emits a signal containing a `QPixmap` and associated `QPushButton` upon successful completion.

- **Image Download**: Downloads an image from a given URL using `requests`.
- **Signal Emission**: Emits a signal containing a `QPixmap` and associated `QPushButton` upon successful image download.
- **Thread Safety**: Ensures thread safety during the download process.

### Resizable IconButton

The `ResizableIconButton` class extends `QPushButton` in PyQt5 to create a button that dynamically resizes its icon while maintaining the aspect ratio. It supports setting icons from file paths or raw image data. This class provides a resizable button in PyQt5 with dynamic icon resizing capabilities. It adjusts the icon size based on the button's size and maintains the aspect ratio using Qt's `KeepAspectRatio` scaling mode.

- **Dynamic Icon Resizing**: Automatically adjusts the icon size to fit within the button while maintaining the aspect ratio.
- **Icon Setting**: Supports setting icons from file paths or raw image data (`QPixmap`).
- **Resizable Button**: Resizes itself based on its parent or layout constraints.

## Usage

1. **Download and Install**: Clone the repository and install the required dependencies.
2. **Run the Application**: Execute the main script to launch the QTube application.
3. **Download YouTube Videos**: Use the downloader feature to download videos.
4. **Play Media**: Use the integrated media player to play downloaded videos or other media files.
5. **Manage Playback**: Utilize playback controls, adjust volume, seek within media files, and toggle fullscreen mode.
6. **Organize Media**: Add media files to the playlist and manage your media library.
7. **Track History**: Access the download history to see previously downloaded media and mediaplayer states.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- Ensure you have the `venv` module available for managing virtual environments.

### Installation Steps

1. **Clone the Repository:**
```
git clone https://github.com/chinmaykrishnroy/QTube.git
cd QTube
```
2. **Activate the Virtual Environment (venv):**
If using Windows, run:
```
venv\Scripts\activate
```
If using macOS or Linux, run:
```
source venv/bin/activate
```
3. **Run the Application:**
Execute the run script to start QTube:
```
run.bat
```
4. **Usage:**
- **Download YouTube Videos:** Use the YouTube downloader feature to download videos.
- **Play Media:** Utilize the integrated media player to play downloaded videos or other media files.
- **Manage Playback:** Adjust volume, seek within media files, and toggle fullscreen mode as needed.
- **Organize Media:** Add media files to playlists and manage your media library.
- **Track History:** Access the download history to view previously downloaded media and their playback states.

5. **Close the Application:**
To exit QTube, simply close the application window or use any provided exit functionality within the UI.

## Troubleshooting

- **Dependency Errors:** If encountering dependency issues, ensure that Python 3.x and the `venv` module are correctly installed and activated.

## Contributing

Contributions to QTube are welcome! Fork the repository, make your changes, and submit a pull request detailing your modifications.

## License

This project is licensed under the [MIT License](LICENSE).
