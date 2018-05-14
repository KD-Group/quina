from . import SizeF, PointF
from PySide2.QtCore import QRectF


class RectF(QRectF):
    @staticmethod
    def left_top_at(point: PointF, size: SizeF) -> 'RectF':
        return RectF(point, size)

    @staticmethod
    def right_top_at(point: PointF, size: SizeF) -> 'RectF':
        return RectF(point - size.horizontal, size)

    @staticmethod
    def left_bottom_at(point: PointF, size: SizeF) -> 'RectF':
        return RectF(point - size.vertical, size)

    @staticmethod
    def right_bottom_at(point: PointF, size: SizeF) -> 'RectF':
        return RectF(point - size, size)

    @staticmethod
    def center_at(point: PointF, size: SizeF) -> 'RectF':
        return RectF(point - size / 2, size)

    @staticmethod
    def top_center_at(point: PointF, size: SizeF) -> 'RectF':
        return RectF(point - size.horizontal / 2, size)

    @staticmethod
    def bottom_center_at(point: PointF, size: SizeF) -> 'RectF':
        return RectF(point - size.horizontal / 2 - size.vertical, size)

    @staticmethod
    def left_center_at(point: PointF, size: SizeF) -> 'RectF':
        return RectF(point - size.vertical / 2, size)

    @staticmethod
    def right_center_at(point: PointF, size: SizeF) -> 'RectF':
        return RectF(point - size.horizontal - size.vertical / 2, size)

    @property
    def left_top(self) -> PointF:
        return PointF(self.topLeft())

    @property
    def right_top(self) -> PointF:
        return PointF(self.topRight())

    @property
    def left_bottom(self) -> PointF:
        return PointF(self.bottomLeft())

    @property
    def right_bottom(self) -> PointF:
        return PointF(self.bottomRight())

    @property
    def center(self) -> PointF:
        return PointF(super().center())

    @property
    def size(self) -> SizeF:
        return SizeF(self.width(), self.height())

    def __eq__(self, other: 'RectF') -> bool:
        return self.left_top == other.left_top and self.size == other.size
