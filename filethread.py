import os

from PyQt5.QtCore import QThread, pyqtSignal, QFileSystemWatcher, QMutex, QObject


class DirectoryScanner(QThread):
    files_changed = pyqtSignal(list)

    def __init__(self, directory, ):
        super().__init__()
        self.directory = directory
        self.running = True
        self.rescan_requested = False
        self.mutex = QMutex()

    def run(self):
        previous_files = set()
        while self.running:
            self.mutex.lock()
            rescan = self.rescan_requested
            self.rescan_requested = False
            self.mutex.unlock()

            if rescan or not previous_files:
                current_files = self.scan_directory()
                if current_files != previous_files:
                    previous_files = current_files
                    file_list = [{'name': name, 'path': path, 'type': ext, 'size': size, 'time': time}
                                 for name, path, ext, size, time in current_files]
                    self.files_changed.emit(file_list)

    def scan_directory(self):
        current_files = set()
        for root, _, files in os.walk(self.directory):
            for file in files:
                path = os.path.join(root, file)
                name, ext = os.path.splitext(file)
                try:
                    size = os.path.getsize(path)
                    time = os.path.getmtime(path)
                    current_files.add((name, path, ext, size, time))
                except FileNotFoundError:
                    continue
        return current_files

    def request_rescan(self):
        self.mutex.lock()
        self.rescan_requested = True
        self.mutex.unlock()

    def stop(self):
        self.running = False
        self.wait()


class FileWatcherSystem(QObject):
    files_changed = pyqtSignal(list)

    def __init__(self, directory, mainwindow):
        super().__init__()
        self.mainwindow = mainwindow
        self.directory = directory
        self.scanner_thread = DirectoryScanner(directory)
        self.scanner_thread.files_changed.connect(self.files_changed.emit)
        self.scanner_thread.start()

        self.file_watcher = QFileSystemWatcher([directory])
        self.file_watcher.directoryChanged.connect(self.directory_changed)
        self.file_watcher.fileChanged.connect(self.file_changed)

    def directory_changed(self, path):
        #print(f"Directory changed: {path}")
        self.mainwindow.ui.currentInfoLabel.setText(
            f"Directory changed: {path}")
        self.scanner_thread.request_rescan()

    def file_changed(self, path):
        #print(f"File changed: {path}")
        self.mainwindow.ui.currentInfoLabel.setText(f"File changed: {path}")
        self.scanner_thread.request_rescan()

    def stop(self):
        self.scanner_thread.stop()
