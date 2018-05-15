from . import BaseWidget
from ...model import WidgetStringItem
from PySide2.QtWidgets import QLabel


class Label(QLabel, BaseWidget, WidgetStringItem):
    def get_value(self):
        return self.text()

    def set_value(self, value: str):
        self.setText(value)
        self.check_change()
