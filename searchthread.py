import random

from PyQt5.QtCore import pyqtSignal, QThread
from youtubesearchpython import VideosSearch


class SearchThread(QThread):
    search_finished = pyqtSignal(list)

    def __init__(self, query, mainwindow):
        super().__init__()
        self.query = query
        self._is_running = True
        self.mainwindow = mainwindow

    def run(self):
        try:
            videos_search = VideosSearch(self.query, limit=50)
            result = videos_search.result()
            video_list = []
            for video in result['result']:
                if not self._is_running:
                    break
                video_data = {
                    'id': video['id'],
                    'thumbnail': video['thumbnails'][0]['url'],
                    'title': video['title'],
                    'duration': video['duration'],
                    'views': video['viewCount']['short'],
                    'channel': video['channel']['name'],
                    'channel_icon': video['channel']['thumbnails'][0]['url'],
                    'time': video['publishedTime']
                }
                video_list.append(video_data)
        except Exception as e:
            print("Can't Search YouTube! ", e)
            self.mainwindow.ui.currentInfoLabel.setText("Cant Reach Youtube! Exception: %s" % e)
            video_list = []
            for _ in range(random.randint(9, 12)):
                video_data = {
                    "id": f"{_}",
                    "title": f"Video Title Will Appear Here",
                    "duration": f"{random.randint(0, 59)}:{random.randint(1, 59)}",
                    "views": f"{random.randint(1, 1000)}B views",
                    "channel": f"Channel Name",
                    "time": f"{random.randint(50, 90)} years ago"
                }
                video_list.append(video_data)

        if self._is_running:
            self.search_finished.emit(video_list)

    def stop(self):
        self._is_running = False
