from . import BaseWidget
from ...model import WidgetStringItem
from PySide2.QtWidgets import QPushButton
from ..interfaces import ExcitedSignalInterface


class PushButton(QPushButton, BaseWidget, ExcitedSignalInterface, WidgetStringItem):
    def set_excited_signal_connection(self):
        # noinspection PyUnresolvedReferences
        self.clicked.connect(self.excited.emit)

    def get_value(self) -> str:
        return self.text()

    def set_value(self, value: str):
        self.setText(value)
        self.check_change()
