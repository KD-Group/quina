from ... import SignalSender
from PySide2.QtGui import QCloseEvent
from ...model.base import AttachMixin


class ClosedSignalInterface(AttachMixin):
    @property
    def closed(self) -> SignalSender:
        return self.attach(SignalSender)

    @property
    def cannot_closed(self) -> SignalSender:
        return self.attach(SignalSender)

    @property
    def can_close(self) -> bool:
        return self.attach(lambda: True)

    @can_close.setter
    def can_close(self, value: bool):
        self.assign(value)

    def deal_with_close(self, event: QCloseEvent):
        if self.can_close:
            self.closed.emit()
            event.accept()
        else:
            self.cannot_closed.emit()
            event.ignore()
