import typing
from . import BaseWidget
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QTableWidget, QAbstractItemView, QTableWidgetItem
from ...model import WidgetStringItem, WidgetIndexItem
from ...model.types import StringListItem
from ..interfaces import ExcitedSignalInterface


class TableWidget(QTableWidget,
                  BaseWidget,
                  ExcitedSignalInterface,
                  WidgetStringItem,
                  WidgetIndexItem,
                  StringListItem
                  ):
    _header_labels: list

    def set_index_value(self, value: int):
        self.selectRow(value or 0)

    def get_index_value(self) -> int:
        return self.currentRow()

    def get_string_list_value(self) -> typing.List[str]:
        if self.index.value < 0:
            return []
        return [self.item(self.index.value, col).text() for col in range(self.column_count)]

    def set_string_list_value(self, value: typing.List[typing.Any]):
        if not isinstance(value, list):
            raise ValueError('Only Support List Type Value')
        if len(value) != self.column_count:
            raise ValueError('Value Length Must Equal to TableWidget Column Count')

        self.row_count += 1
        for col in range(self.column_count):
            table_item = QTableWidgetItem(str(value[col]))
            table_item.setTextAlignment(Qt.AlignCenter)
            self.setItem(self.row_count - 1, col, table_item)
        self.index.value = self.row_count - 1
        self.auto_resize_column_width()
        self.string_list.check_change()

    @property
    def row_count(self):
        return self.rowCount()

    @row_count.setter
    def row_count(self, value: int):
        self.setRowCount(value)

    @property
    def column_count(self):
        return self.columnCount()

    @column_count.setter
    def column_count(self, value: int):
        self.setColumnCount(value)

    def set_changed_connection(self):
        # noinspection PyUnresolvedReferences
        self.currentCellChanged.connect(self.index.check_change)

    def set_excited_signal_connection(self):
        # noinspection PyUnresolvedReferences
        self.doubleClicked.connect(lambda *_: self.excited.emit())

    def set_just_show_mode(self):
        self.auto_resize = True
        self.verticalHeader().hide()
        self.resizeColumnsToContents()
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def set_select_rows_mode(self):
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setStyleSheet("selection-background-color: lightBlue;selection-color: black;")
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)

    @property
    def selected_rows(self) -> list:
        return sorted(list({self.indexFromItem(item).row() for item in self.selectedItems()}))

    @property
    def auto_resize(self):
        return getattr(self, 'resize', False)

    @auto_resize.setter
    def auto_resize(self, value: bool):
        setattr(self, 'resize', value)

    @property
    def header_labels(self) -> typing.List[str]:
        return self._header_labels or []

    @header_labels.setter
    def header_labels(self, labels: list):
        self.setColumnCount(len(labels))
        self.setHorizontalHeaderLabels(labels)
        self._header_labels = labels

    def auto_resize_column_width(self):
        if self.auto_resize:
            self.resizeColumnsToContents()
            col_count = self.columnCount()
            col_width = sum(list([self.columnWidth(i) for i in range(col_count)]))
            if col_width < self.width():
                for i in range(col_count):
                    self.setColumnWidth(i, self.columnWidth(i) / col_width * self.width())

    def resizeEvent(self, event):
        super(TableWidget, self).resizeEvent(event)
        self.auto_resize_column_width()
