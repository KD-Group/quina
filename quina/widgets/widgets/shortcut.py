import typing
from . import BaseWidget
from PySide2.QtGui import QKeySequence
from PySide2.QtWidgets import QShortcut
from ..interfaces import ExcitedSignalInterface


class Shortcut(QShortcut, BaseWidget, ExcitedSignalInterface):  # pragma: no cover
    def __init__(self, key: typing.Union[str, QKeySequence], parent):
        if isinstance(key, str):
            key = QKeySequence(key)
        super().__init__(key, parent)

    def set_excited_signal_connection(self):
        # noinspection PyUnresolvedReferences
        self.activated.connect(self.excited.emit)
