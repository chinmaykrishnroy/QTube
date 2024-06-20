import os
import pickle


class HistoryManager:
    def __init__(self, app_directory):
        self.app_directory = app_directory
        self.history_file = os.path.join(app_directory, 'history.zip')
        os.makedirs(self.app_directory, exist_ok=True)
        self.history = self.load_history()

    def add_history(self, history_time, history_elapsed_time, history_location, history_url, history_title):
        history_item = {
            'time': history_time,
            'elapsed': history_elapsed_time,
            'path': history_location,
            'url': history_url,
            'title': history_title
        }
        self.history.append(history_item)
        self.save_history()
        return self.get_history()

    def get_history(self):
        return self.history

    def save_history(self):
        with open(self.history_file, 'wb') as f:
            pickle.dump(self.history, f)

    def load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, 'rb') as f:
                return pickle.load(f)
        return []

    def rearrange_history(self):
        return self.get_history()
