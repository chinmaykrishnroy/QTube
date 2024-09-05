import math
import os
import re
import yt_dlp
from PyQt5.QtCore import pyqtSignal, QThread, QWaitCondition, QMutex


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    try:
        i = int(math.log(size_bytes, 1024))
        s = round(size_bytes / (1024 ** i), 2)
        return f"{s} {size_name[i]}"
    except Exception as e:
        print("Error in conversion due to:", e)
        return "--"


def format_time(sec):
    try:
        h, m, s = int(sec // 3600), int((sec % 3600) // 60), int(sec % 60)
        return f"{h:02}:{m:02}:{s:02}" if h > 0 else f"{m:02}:{s:02}"
    except:
        return "00:00"


class DownloadThread(QThread):
    progress = pyqtSignal(dict)
    status = pyqtSignal(str)

    def __init__(self, id, type, download_directory="Downloads/", audio_ext='default', video_ext='default', mainwindow=None):
        super().__init__()
        self.id = id
        self.paused = False
        self._pause_cond = QWaitCondition()
        self._mutex = QMutex()
        self._is_running = True
        self.format = self.get_format(type)
        self.extension = self.get_extension(type, audio_ext, video_ext)
        self.mainwindow = mainwindow
        self.download_path = os.path.join(
            download_directory, '%(title)s.%(ext)s')

    @staticmethod
    def get_extension(type, audio_ext, video_ext):
        return 'default' if audio_ext == 'default' or video_ext == 'default' else (audio_ext if type in {1, 2} else video_ext).replace('.', '')

    def get_format(self, type):
        formats = {
            5: 'bestvideo[height<=2160]+bestaudio/best[height<=2160]',
            4: 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
            3: 'bestvideo[height<=720]+bestaudio/best[height<=720]',
            2: 'bestaudio[ext=m4a]/best[ext=mp3]/best',
            1: 'bestaudio[abr<=192]/best[ext=mp3]/best',
        }
        return formats.get(type, 'bestaudio[ext=m4a]/best[ext=mp3]/best')

    def run(self):
        ydl_opts = {
            'format': self.format,
            'progress_hooks': [self.my_hook],
            'outtmpl': self.download_path,
            'subtitleslangs': ['en', 'hin'],
            'quiet': True,
            'logger': self.MyLogger(self.mainwindow),
            'verbose': True
        }
        if self.extension != 'default':
            ydl_opts['postprocessors'] = [
                {'key': 'FFmpegVideoConvertor', 'preferedformat': self.extension}]

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.id])
        except Exception as e:
            self._handle_error(e)
        self._is_running = False

    def my_hook(self, d):
        if not self._is_running:
            return
        status = d['status']
        if status == 'downloading':
            self._emit_progress(d)
            self.status.emit("Downloading")
            self._check_pause()
        elif status in {'finished', 'error'}:
            self.status.emit("Finished" if status == 'finished' else "ERROR")
            self._is_running = False
            self.quit()

    def _emit_progress(self, d):
        verbose = {
            'downloaded': convert_size(d['downloaded_bytes']),
            'progress': (d.get('fragment_index', 0) / d.get('fragment_count', 1)) * 100,
            'size': convert_size(d.get('total_bytes') or d.get('total_bytes_estimate')),
            'eta': format_time(d.get('eta')),
            'speed': convert_size(d.get('speed')),
            'elapsed': format_time(d.get('elapsed')),
            'filename': d.get('filename'),
            'tempfile': d.get('tempfilename'),
            'status': d.get('status')
        }
        self.progress.emit(verbose)

    def _handle_error(self, e):
        error_message = f"ERROR WHILE DOWNLOADING! Exception: {e}"
        if self.mainwindow:
            self.mainwindow.pushNotification(error_message, 25)
            self.mainwindow.ui.currentInfoLabel.setText(f"ERROR! {e}")
        print("Download Error:", e)

    def _check_pause(self):
        self._mutex.lock()
        while self.paused:
            self._pause_cond.wait(self._mutex)
        self._mutex.unlock()

    def toggle_pause(self):
        self._mutex.lock()
        self.paused = not self.paused
        self.status.emit("Resume" if not self.paused else "Pause")
        if not self.paused:
            self._pause_cond.wakeAll()
        self._mutex.unlock()

    def stop(self):
        self._is_running = False
        self._pause_cond.wakeAll()

    def force_terminate(self):
        self.terminate()
        self.wait()

    class MyLogger:
        def __init__(self, mainwindow=None):
            self.mainwindow = mainwindow

        def log_message(self, level, msg):
            print(f"{level}: {msg}")
            if self.mainwindow:
                clean_msg = re.sub(r'\x1B[@-_][0-?]*[ -/]*[@-~]', '', msg)
                self.mainwindow.ui.currentInfoLabel.setText(clean_msg)

        def debug(self, msg): self.log_message("DEBUG", msg)
        def info(self, msg): self.log_message("INFO", msg)
        def warning(self, msg): self.log_message("WARNING", msg)
        def error(self, msg): self.log_message("ERROR", msg)
