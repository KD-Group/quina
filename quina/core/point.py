import math
import typing
import operator
from . import SizeF
from PySide2.QtCore import QPoint, QPointF


class PointF(QPointF):
    def __init__(self, para: typing.Union[float, QPoint, QPointF], y: float = 0):
        if isinstance(para, QPoint) or isinstance(para, QPointF):
            super().__init__(para)
        else:
            super().__init__(para, y)

    @property
    def x(self) -> float:
        return super().x()

    @x.setter
    def x(self, value: float):
        self.setX(value)

    @property
    def y(self) -> float:
        return super().y()

    @y.setter
    def y(self, value: float):
        self.setY(value)

    @property
    def horizontal(self) -> 'PointF':
        return PointF(self.x, 0)

    @property
    def vertical(self) -> 'PointF':
        return PointF(0, self.y)

    def __calc__(self, other: typing.Union[int, float, 'PointF', SizeF], op: typing.Callable[[float, float], float]):
        if isinstance(other, PointF):
            return PointF(
                op(self.x, other.x),
                op(self.y, other.y)
            )
        elif isinstance(other, SizeF):
            return PointF(
                op(self.x, other.w),
                op(self.y, other.h)
            )
        else:
            return PointF(
                op(self.x, other),
                op(self.y, other)
            )

    def __add__(self, other: typing.Union[int, float, 'PointF', SizeF]):
        return self.__calc__(other, operator.add)

    __radd__ = __add__

    def __sub__(self, other: typing.Union[int, float, 'PointF', SizeF]):
        return self.__calc__(other, operator.sub)

    __rsub__ = None

    def __mul__(self, other: typing.Union[int, float, 'PointF', SizeF]):
        return self.__calc__(other, operator.mul)

    __rmul__ = __mul__

    def __truediv__(self, other: typing.Union[int, float, 'PointF', SizeF]):
        return self.__calc__(other, operator.truediv)

    def __neg__(self):
        return PointF(-self.x, -self.y)

    def __eq__(self, other: 'PointF'):
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)
