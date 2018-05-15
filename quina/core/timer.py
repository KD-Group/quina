from . import SignalSender
from PySide2.QtCore import QTimer


class Timer(QTimer):
    def __init__(self, single_shot: bool = False):
        super().__init__()
        self.setSingleShot(single_shot)

        # replace original Signal to SignalSender, trick of type
        self.triggered = SignalSender()
        self.timeout.connect(self.triggered.emit)
        self.timeout = self.triggered

    def start(self, seconds: float):
        super().start(int(seconds * 1000))
