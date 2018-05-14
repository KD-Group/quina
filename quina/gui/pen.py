import typing
from ..core import Qt
from .utils import scaling_ratio
from PySide2.QtGui import QPen, QColor, QBrush


class Pen(QPen):
    def __init__(self,
                 para: typing.Union[QBrush, QColor, QPen],
                 width: typing.Optional[float] = None,
                 pen_style: Qt.PenStyle = Qt.SolidLine,
                 cap_style: Qt.PenCapStyle = Qt.SquareCap,
                 join_style: Qt.PenJoinStyle = Qt.BevelJoin
                 ):
        if width is None:
            super().__init__(para)
            self.width *= scaling_ratio
        else:
            super().__init__(para, width * scaling_ratio, pen_style, cap_style, join_style)

    @property
    def width(self) -> float:
        return self.widthF() / scaling_ratio

    @width.setter
    def width(self, value: float):
        self.setWidthF(value * scaling_ratio)
