from . import BaseWidget
from PySide2.QtWidgets import QAction
from ..interfaces import ExcitedSignalInterface


class Action(QAction, BaseWidget, ExcitedSignalInterface):
    def set_excited_signal_connection(self):
        # noinspection PyUnresolvedReferences
        self.triggered.connect(self.excited.emit)

    def click(self):
        if self.enabled:
            self.trigger()
