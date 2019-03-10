from . import BaseWidget
from ...model import WidgetStringItem
from PySide2.QtWidgets import QDateEdit
from PySide2.QtCore import QDate


class DateEdit(QDateEdit, BaseWidget, WidgetStringItem):
    def get_value(self) -> str:
        return self.text()

    def set_value(self, value: str):
        value = value or ''
        if value != self.get_value():
            date = value.split('-')
            if len(date) != 3:
                raise ValueError('Date format is invalid')
            self.setDate(QDate(int(date[0]), int(date[1]), int(date[2])))

    def set_changed_connection(self):
        # noinspection PyUnresolvedReferences
        self.dateChanged.connect(self.check_change)
