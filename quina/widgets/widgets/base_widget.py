import typing
from ...model import base
from ..layouts import SquareLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QDockWidget
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QHBoxLayout


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
