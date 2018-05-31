import typing
from pathlib import Path
from ...model import base
from ..layouts import SquareLayout
from PySide2.QtCore import QPoint
from PySide2.QtGui import QPixmap
from PySide2.QtGui import QPicture
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import QWidget
from PySide2.QtSvg import QSvgGenerator
from PySide2.QtWidgets import QDockWidget
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtPrintSupport import QPrinter


class BaseWidget(QWidget, base.AttachMixin):
    @property
    def center_widget(self) -> typing.Optional['BaseWidget']:
        return self.attach(lambda: None)

    @center_widget.setter
    def center_widget(self, widget: 'BaseWidget'):
        self.assign(widget)

    def set_central_widget(self, widget: 'BaseWidget', spacing: int=0, layout_type=QHBoxLayout):
        if self.center_widget is not None:
            self.layout().replaceWidget(self.center_widget, widget)
            self.center_widget.deleteLater()
            self.center_widget = widget
            return

        if isinstance(self, QMainWindow):
            self.setCentralWidget(widget)
        elif isinstance(self, QDockWidget):
            self.setWidget(widget)
        else:
            layout = layout_type()
            layout.setSpacing(spacing)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(widget)
            self.setLayout(layout)

        self.center_widget = widget

    def set_square_widget(self, widget: QWidget, spacing: int = 0):
        self.set_central_widget(widget, spacing, layout_type=SquareLayout)

    def set_focus(self):
        return self.setFocus()

    def set_enabled(self):
        return self.setEnabled(True)

    def set_disabled(self):
        return self.setEnabled(False)

    @property
    def enabled(self) -> bool:
        return self.isEnabled()

    @enabled.setter
    def enabled(self, value: bool):
        if value:
            self.set_enabled()
        else:
            self.set_disabled()

    def export_to_pdf(self: 'BaseWidget', filename: Path):
        width_a4 = 730
        height_a4 = 1060

        is_landscape = self.width() > self.height()
        if is_landscape:
            self.resize(height_a4, width_a4)  # landscape
        else:
            self.resize(width_a4, height_a4)  # portrait

        # render widget to picture
        picture = QPicture()
        painter = QPainter(picture)
        self.render(painter, QPoint(0, 0))
        painter.end()

        # set up PDF printer
        printer = QPrinter()
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(str(filename))
        if is_landscape:
            printer.setOrientation(QPrinter.Landscape)

        # draw picture on printer
        painter = QPainter()
        ok = painter.begin(printer)
        if ok:
            painter.drawPicture(0, 0, picture)
            ok = painter.end()
        return ok

    def export_to_picture(self: 'BaseWidget', filename: Path):
        picture = QPixmap(self.width(), self.height())
        painter = QPainter(picture)
        self.render(painter, QPoint(0, 0))
        painter.end()

        return picture.save(str(filename))

    def export_to_svg(self, filename: Path) -> bool:
        generator = QSvgGenerator()
        generator.setFileName(str(filename))
        generator.setSize(self.size())
        generator.setViewBox(self.rect())
        self.render(generator)
        return True
