from . import BaseWidget
from PySide2.QtWidgets import QDialog
from PySide2.QtGui import QCloseEvent
from ..interfaces import ClosedSignalInterface, ClassExecInterface


class Dialog(QDialog, BaseWidget, ClosedSignalInterface, ClassExecInterface):
    def closeEvent(self, event: QCloseEvent):
        self.deal_with_close(event)

    def exec(self):
        super().exec_()
