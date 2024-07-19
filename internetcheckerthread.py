import socket
import threading
import time

from PyQt5.QtCore import pyqtSignal, QObject


class InternetChecker(threading.Thread):
    def __init__(self, signal_emitter):
        super().__init__()
        self._stop_event = threading.Event()
        self.connected_to_internet = False
        self.signal_emitter = signal_emitter

    def run(self):
        while not self._stop_event.is_set():
            new_status = self.check_internet_connection()
            if new_status != self.connected_to_internet:
                self.connected_to_internet = new_status
                self.signal_emitter.connection_status_changed.emit(
                    self.connected_to_internet)
            time.sleep(3)

    def stop(self):
        self._stop_event.set()

    @staticmethod
    def check_internet_connection():
        try:
            # Attempt to connect to Google's primary DNS server
            socket.create_connection(("8.8.8.8", 53), timeout=1)
            return True
        except OSError:
            return False


class SignalEmitter(QObject):
    connection_status_changed = pyqtSignal(bool)
