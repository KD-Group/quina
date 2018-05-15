from . import BaseWidget
from ...model import WidgetStringItem
from PySide2.QtWidgets import QSpinBox


class SpinBox(QSpinBox, BaseWidget, WidgetStringItem):
    def get_string_value(self) -> str:
        return str(self.get_integer_value())

    def set_string_value(self, value: str):
        self.set_integer_value(int(value))

    def get_integer_value(self) -> int:
        return self.value()

    def set_integer_value(self, value: int):
        self.setValue(value)

    def set_changed_connection(self):
        # noinspection PyUnresolvedReferences
        self.valueChanged[int].connect(self.integer.check_change)
        # noinspection PyUnresolvedReferences
        self.valueChanged[str].connect(self.string.check_change)
