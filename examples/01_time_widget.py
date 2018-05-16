import time
import quina
from quina.widgets import Widget
from quina.core import PointF, Qt
from quina.gui import Painter, Pen


class NumberWidget(Widget):
    def __init__(self, value: str, parent: Widget):
        super().__init__(parent)
        self.value = value
        self.background_color = Qt.black

    def paint(self, painter: Painter):
        painter.setPen(Pen(Qt.white))
        right_bottom = PointF(self.width(), self.height())
        painter.draw_text_center(right_bottom / 2, self.value)


if __name__ == '__main__':
    widget = Widget()
    widget.setMinimumSize(400, 300)

    timer = quina.core.Timer()
    timer.start(0.1)

    @quina.connect_with(timer.timeout)
    def replace_center_widget():
        sub_widget = NumberWidget(str(time.time()), widget)
        widget.set_square_widget(sub_widget)

    widget.exec()
