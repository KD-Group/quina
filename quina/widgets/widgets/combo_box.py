import typing
from . import BaseWidget
from PySide2.QtWidgets import QComboBox
from ...model import WidgetStringItem, WidgetIndexItem
from ...model.types import StringListItem


class ComboBox(QComboBox,
               BaseWidget,
               WidgetStringItem,
               WidgetIndexItem,
               StringListItem
               ):
    def get_string_value(self) -> str:
        return self.currentText()

    def set_string_value(self, value: typing.Optional[str]):
        texts = self.string_list.value
        assert isinstance(texts, list)

        if value in texts:
            self.index.value = texts.index(value)
        else:
            raise ValueError(f'Value {value} Not Found in List')

    def set_changed_connection(self):
        # noinspection PyUnresolvedReferences
        self.currentIndexChanged[int].connect(self.index.check_change)
        # noinspection PyUnresolvedReferences
        self.currentIndexChanged[str].connect(self.string.check_change)

    def get_index_value(self) -> int:
        return self.currentIndex()

    def set_index_value(self, value: int):
        if isinstance(value, int):
            value = max(0, min(value, self.count() - 1))
            self.setCurrentIndex(value)

    def get_string_list_value(self) -> typing.List[str]:
        return [self.itemText(index) for index in range(self.count())]

    def set_string_list_value(self, value: typing.List[str]):
        value = value or []

        old_count = self.count()
        new_count = len(value)
        for i in range(min(old_count, new_count)):
            self.setItemText(i, value[i])
        for index in range(new_count, old_count):
            self.removeItem(index)
        self.addItems(value[old_count:new_count])

        self.index.check_change()
        self.string.check_change()
        self.string_list.check_change()
