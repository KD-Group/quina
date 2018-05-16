# reference: http://www.qtcentre.org/threads/21329-keeping-a-widget-to-be-square
import typing
from PySide2.QtWidgets import QLayout, QLayoutItem
from PySide2.QtWidgets import QWidget, QWidgetItem
from PySide2.QtCore import Qt, QSize, QPoint, QRect


class SquareLayout(QLayout):
    def __init__(self, parent: QWidget = None,
                 default_item: QWidget = None):
        super().__init__(parent)

        self.item = default_item
        self.last_received_rect = QRect(0, 0, 0, 0)
        self.geometry_rect = QRect(0, 0, 0, 0)

        self.setSpacing(0)

    def addItem(self, item: QLayoutItem):
        self.takeAt(0)
        self.item = item
        self.setGeometry(self.geometry_rect)

    def addWidget(self, w: QWidget):
        self.addItem(QWidgetItem(w))

    def replaceWidget(self, old_widget: QWidget, new_widget: QWidget):
        self.addWidget(new_widget)

    def take(self) -> QLayoutItem:
        item, self.item = self.item, None
        return item

    def takeAt(self, index: int) -> typing.Optional[QLayoutItem]:
        return self.take() if index == 0 else None

    def itemAt(self, index: int) -> typing.Optional[QLayoutItem]:
        return self.item if index == 0 else None

    def count(self):
        return 1 if self.item is not None else 0

    def expandingDirections(self):
        return Qt.Horizontal | Qt.Vertical

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        return self.item.minimumSize() if self.item is not None else QSize()

    def hasHeightForWidth(self):
        return False

    def geometry(self):
        return QRect(self.geometry_rect)

    def setGeometry(self, rect: QRect):
        if self.item is None or self.last_received_rect == rect:
            return

        self.last_received_rect = rect

        proper_size = self.calculate_proper_size(rect.size())
        proper_location = SquareLayout.calculate_center_location(rect.size(), proper_size)

        self.geometry_rect = QRect(proper_location, proper_size)
        self.item.setGeometry(self.geometry_rect)
        self.item.widget().show()

        super().setGeometry(self.geometry_rect)

    def calculate_proper_size(self, from_size: QSize):
        minimum_length = min(from_size.width(), from_size.height())
        return QSize(minimum_length - self.spacing(), minimum_length - self.spacing())

    def update(self):
        self.setGeometry(self.geometry())

    @staticmethod
    def calculate_center_location(from_size: QSize, item_size: QSize):
        x = max(from_size.width() // 2 - item_size.width() // 2, 0)
        y = max(from_size.height() // 2 - item_size.height() // 2, 0)
        return QPoint(x, y)
