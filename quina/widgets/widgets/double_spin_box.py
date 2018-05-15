from . import BaseWidget
from ...model import WidgetStringItem
from PySide2.QtWidgets import QDoubleSpinBox


class DoubleSpinBox(QDoubleSpinBox, BaseWidget, WidgetStringItem):
    def get_string_value(self) -> str:
        return str(self.get_float_value())

    def set_string_value(self, value: str):
        self.set_float_value(float(value))

    def get_float_value(self) -> float:
        return self.value()

    def set_float_value(self, value: float):
        self.setValue(value)

    def set_changed_connection(self):
        # noinspection PyUnresolvedReferences
        self.valueChanged[float].connect(self.float.check_change)
        # noinspection PyUnresolvedReferences
        self.valueChanged[str].connect(self.string.check_change)
