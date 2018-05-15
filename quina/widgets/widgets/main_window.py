from . import BaseWidget
from ...core import EventLoop
from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import QMainWindow
from ..interfaces import ClosedSignalInterface, ClassExecInterface


class MainWindow(QMainWindow, BaseWidget, ClosedSignalInterface, ClassExecInterface):
    def closeEvent(self, event: QCloseEvent):
        self.deal_with_close(event)

    def exec(self):
        with EventLoop() as event:
            self.show()
            self.closed.connect(event.quit)
