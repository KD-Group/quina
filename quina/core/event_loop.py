from . import Timer
from PySide2.QtCore import QEventLoop


class EventLoop:
    def __init__(self, timeout_in_second: float=None):
        self.event = QEventLoop(None)
        self.timeout_in_second = timeout_in_second

    def quit(self):
        self.event.quit()

    def __enter__(self):
        return self

    def __exit__(self, *_):
        if self.timeout_in_second is not None:
            t = Timer()
            t.timeout.connect(self.quit)
            t.start(seconds=self.timeout_in_second)
        self.event.exec_()


# non-blocking synchronous
def wait(seconds: float = 0.01):
    seconds = max(0.01, seconds)
    with EventLoop(timeout_in_second=seconds):
        pass
