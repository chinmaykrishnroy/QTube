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
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return f"{s} {size_name[i]}"
    except Exception as e:
        print("Error in conversion due to: ", e)
        return f"--"


def format_time(sec):
    try:
        seconds, minutes, hours = (sec % 60), ((
            sec / 60) % 60), ((sec / (60 * 60)) % 24)
    except:
        seconds, minutes, hours = 0, 0, 0
    if int(hours) > 0:
        return "%02d:%02d:%02d" % (hours, minutes, seconds)
    else:
        return "%02d:%02d" % (minutes, seconds)


class DownloadThread(QThread):
    progress = pyqtSignal(dict)
    status = pyqtSignal(str)

    def __init__(self, id, type, download_directory="Downloads/", audio_extension='default', video_extension='default',
                 mainwindow=None):
        super().__init__()
        self.id = id
        self.paused = False
        self._pause_cond = QWaitCondition()
        self._mutex = QMutex()
        self._is_running = True
        self.format = self.getformat(type)
        self.mainwindow = mainwindow
        self.extension = self.getextension(
            type, audio_extension, video_extension)
        self.download_path = os.path.join(
            download_directory, '%(title)s.%(ext)s')

    @staticmethod
    def getextension(type, audio_extension, video_extension):
        if audio_extension == 'default' or video_extension == 'default':
            return 'default'
        if type == 2 or type == 1:
            audio_extension = audio_extension.replace('.', '')
            return audio_extension
        else:
            video_extension = video_extension.replace('.', '')
            return video_extension

    def getformat(self, type):
        if type == 5:
            return 'bestvideo[height<=2160]+bestaudio/best[height<=2160]'
        elif type == 4:
            return 'bestvideo[height<=1080]+bestaudio/best[height<=1080]'
        elif type == 3:
            return 'bestvideo[height<=720]+bestaudio/best[height<=720]'
        elif type == 2:
            return 'bestaudio[ext=m4a]/best[ext=mp3]/best'
        elif type == 1:
            return 'bestaudio[abr<=192]/best[ext=mp3]/best'
        else:
            return 'bestaudio[ext=m4a]/best[ext=mp3]/best'

    def run(self):

        formatted_opts = {
            'format': self.format,
            'progress_hooks': [self.my_hook],
            'outtmpl': self.download_path,
            'subtitleslangs': ['en', 'hin'],
            'quiet': True,
            'ffmpeg_location': 'bin',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': self.extension}],
            'logger': self.MyLogger(self.mainwindow),
            'verbose': True
        }

        default_opts = {
            'format': self.format,
            'progress_hooks': [self.my_hook],
            'outtmpl': self.download_path,
            'subtitleslangs': ['en', 'hin'],
            'quiet': True,
            'ffmpeg_location': 'bin',
            'logger': self.MyLogger(self.mainwindow),
            'verbose': True
        }

        ydl_opts = default_opts if self.extension == 'default' else formatted_opts
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.id])
        except Exception as e:
            if self.mainwindow:
                self.mainwindow.pushNotification(
                    f"ERROR WHILE DOWNLOADING! Exception: {e}", 25)
                self.mainwindow.ui.currentInfoLabel.setText(f"ERROR! {e}")
            print("Download Error: ", e)
        self._is_running = False

    def my_hook(self, d):
        if not self._is_running:
            return
        if d['status'] == 'downloading':
            total_size = d.get('total_bytes') or d.get('total_bytes_estimate')
            downloaded_size = d['downloaded_bytes']
            verbose = {
                'downloaded': convert_size(d['downloaded_bytes']),
                'progress': (downloaded_size / total_size) * 100,
                'size': convert_size(d.get('total_bytes') or d.get('total_bytes_estimate')),
                'eta': format_time(d.get('eta')),
                'speed': convert_size(d.get('speed')),
                'elapsed': format_time(d.get('elapsed')),
                'filename': d.get('filename'),
                'tempfile': d.get('tempfilename'),
                'status': d.get('status')
            }
            self.progress.emit(verbose)
            self.status.emit("Downloading")
            self._check_pause()
        elif d['status'] == 'finished':
            self.status.emit("Finished")
            self._is_running = False
            self.quit()
        elif d['status'] == 'error':
            self.status.emit("ERROR")
            self._is_running = False
            self.quit()

    def _check_pause(self):
        self._mutex.lock()
        while self.paused:
            self._pause_cond.wait(self._mutex)
        self._mutex.unlock()

    def toggle_pause(self):
        self._mutex.lock()
        if self.paused:
            self.paused = False
            self.status.emit("Resume")
            self._pause_cond.wakeAll()
        else:
            self.paused = True
            self.status.emit("Pause")
        self._mutex.unlock()

    def stop(self):
        self._is_running = False
        self._pause_cond.wakeAll()

    def force_terminate(self):
        self.terminate()
        self.wait()

    class MyLogger():
        def __init__(self, mainwindow=None):
            self.mainwindow = mainwindow

        def debug(self, msg):
            print(f"DEBUG: {msg}")
            info = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]').sub('', msg)
            self.mainwindow.ui.currentInfoLabel.setText(info)

        def info(self, msg):
            print(f"INFO: {msg}")
            info = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]').sub('', msg)
            self.mainwindow.ui.currentInfoLabel.setText(info)

        def warning(self, msg):
            print(f"WARNING: {msg}")
            info = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]').sub('', msg)
            self.mainwindow.ui.currentInfoLabel.setText(info)

        def error(self, msg):
            print(f"ERROR: {msg}")
            info = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]').sub('', msg)
            self.mainwindow.ui.currentInfoLabel.setText(info)
