from . import BaseWidget
from ...model import WidgetStringItem
from PySide2.QtWidgets import QLineEdit


class LineEdit(QLineEdit, BaseWidget, WidgetStringItem):
    def get_value(self) -> str:
        return self.text()

    def set_value(self, value: str):
        value = value or ''
        if value != self.get_value():
            self.setText(value)

    def set_changed_connection(self):
        # noinspection PyUnresolvedReferences
        self.textChanged.connect(self.check_change)
