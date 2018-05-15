import typing
from . import BaseWidget
from ...gui import Painter
from ...core import EventLoop
from PySide2.QtGui import QCloseEvent, QColor
from ..interfaces import ClosedSignalInterface, ClassExecInterface


class Widget(BaseWidget, ClosedSignalInterface, ClassExecInterface):
    def __init__(self, parent: typing.Optional['Widget'] = None, *args):
        super().__init__(parent, *args)

    def closeEvent(self, event: QCloseEvent):
        self.deal_with_close(event)

    def exec(self):
        with EventLoop() as event:
            self.show()
            self.closed.connect(event.quit)

    @property
    def background_color(self) -> typing.Optional[QColor]:
        return self.attach(lambda: None)

    @background_color.setter
    def background_color(self, value: QColor):
        self.assign(value)
        self.update()

    def paintEvent(self, *args, **kwargs):
        painter = Painter(self)

        if self.background_color is not None:
            painter.fillRect(self.rect(), self.background_color)

        self.paint(painter)
        painter.end()

    def paint(self, painter: Painter):
        pass
