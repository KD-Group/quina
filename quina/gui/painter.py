from . import Pen
from .utils import text_size
from ..core import PointF, RectF, Qt
from PySide2.QtGui import QPainter, QColor


class Painter(QPainter):  # pragma: no cover
    def draw_text(self, rect: RectF, text: str, color: QColor = None, align: Qt.TextAlignmentRole = Qt.AlignCenter):
        current_pen = self.pen()
        if color:
            self.setPen(Pen(color))

        self.drawText(rect, align, text)

        if color:
            self.setPen(current_pen)

    def draw_text_above(self, point: PointF, text, color: QColor = None, margin: float = 0.0):
        size = text_size(text=text, font=self.font())
        rect = RectF.bottom_center_at(point + PointF(0, -margin), size)
        self.draw_text(rect=rect, text=text, color=color)

    def draw_text_below(self, point: PointF, text, color: QColor = None, margin: float = 0.0):
        size = text_size(text=text, font=self.font())
        rect = RectF.top_center_at(point + PointF(0, margin), size)
        self.draw_text(rect=rect, text=text, color=color)

    def draw_text_left(self, point: PointF, text, color: QColor = None, margin: float = 0.0):
        size = text_size(text=text, font=self.font())
        rect = RectF.right_center_at(point + PointF(-margin, 0), size)
        self.draw_text(rect=rect, text=text, color=color)

    def draw_text_right(self, point: PointF, text, color: QColor = None, margin: float = 0.0):
        size = text_size(text=text, font=self.font())
        rect = RectF.left_center_at(point + PointF(margin, 0), size)
        self.draw_text(rect=rect, text=text, color=color)

    def draw_text_center(self, point: PointF, text, color: QColor = None):
        size = text_size(text=text, font=self.font())
        rect = RectF.center_at(point, size)
        self.draw_text(rect=rect, text=text, color=color)
