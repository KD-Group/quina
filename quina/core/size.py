import math
import typing
import operator
from PySide2.QtCore import QSizeF


class SizeF(QSizeF):
    def __init__(self, w: float = 0, h: float = 0):
        super().__init__(w, h)

    @property
    def w(self) -> float:
        return self.width()

    @property
    def h(self) -> float:
        return self.height()

    @property
    def horizontal(self) -> 'SizeF':
        return SizeF(self.w, 0)

    @property
    def vertical(self) -> 'SizeF':
        return SizeF(0, self.h)

    def __calc__(self, other: typing.Union[int, float, 'SizeF'], op: typing.Callable[[float, float], float]):
        if isinstance(other, SizeF):
            return SizeF(
                op(self.w, other.w),
                op(self.h, other.h)
            )
        else:
            return SizeF(
                op(self.w, other),
                op(self.h, other)
            )

    def __add__(self, other: typing.Union[int, float, 'SizeF']):
        return self.__calc__(other, operator.add)

    __radd__ = __add__

    def __sub__(self, other: typing.Union[int, float, 'SizeF']):
        return self.__calc__(other, operator.sub)

    __rsub__ = None

    def __mul__(self, other: typing.Union[int, float, 'SizeF']):
        return self.__calc__(other, operator.mul)

    __rmul__ = __mul__

    def __truediv__(self, other: typing.Union[int, float, 'SizeF']):
        return self.__calc__(other, operator.truediv)

    def __neg__(self):
        return SizeF(-self.w, -self.h)

    def __eq__(self, other: 'SizeF'):
        return math.isclose(self.w, other.w) and math.isclose(self.h, other.h)
