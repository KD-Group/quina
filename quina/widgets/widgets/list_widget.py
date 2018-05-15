import typing
from . import BaseWidget
from PySide2.QtWidgets import QListWidget
from ...model import WidgetStringItem, WidgetIndexItem
from ...model.types import StringListItem
from ..interfaces import ExcitedSignalInterface


class ListWidget(QListWidget,
                 BaseWidget,
                 ExcitedSignalInterface,
                 WidgetStringItem,
                 WidgetIndexItem,
                 StringListItem
                 ):
    def set_excited_signal_connection(self):
        # noinspection PyUnresolvedReferences
        self.doubleClicked.connect(lambda *_: self.excited.emit())

    def get_string_value(self) -> typing.Optional[str]:
        if self.index.value >= 0:
            return self.currentItem().text()
        else:
            return None

    def set_string_value(self, value: str):
        texts = self.string_list.value
        assert isinstance(texts, list)

        if value in texts:
            self.index.value = texts.index(value)
        else:
            raise ValueError(f'Value {value} Not Found in List')

    def set_changed_connection(self):
        # noinspection PyUnresolvedReferences
        self.currentTextChanged.connect(self.string.check_change)
        # noinspection PyUnresolvedReferences
        self.currentRowChanged.connect(self.index.check_change)

    def get_index_value(self) -> int:
        return self.currentRow()

    def set_index_value(self, value: int):
        self.setCurrentRow(value or 0)

    def get_string_list_value(self) -> typing.List[str]:
        return [self.item(index).text() for index in range(self.count())]

    def set_string_list_value(self, value: typing.List[str]):
        value = value or []
        self.clear()
        self.addItems(value)
        self.string_list.check_change()
