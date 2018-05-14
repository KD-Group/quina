from ..core import SizeF
from PySide2.QtGui import QFont, QFontMetrics


def text_size(text, font: QFont) -> 'SizeF':
    font_metrics = QFontMetrics(font)

    lines = text.split('\n')
    width = max(map(font_metrics.width, lines))
    height = font_metrics.height() * len(lines)
    return SizeF(width, height)


def __get_scaling_ratio__():
    base = 800.0  # the width of a character when dpi = 96
    width = text_size('Q', QFont('Courier New', 1000)).w
    return width / base


scaling_ratio = __get_scaling_ratio__()
