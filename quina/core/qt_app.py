import os
import sys
import PySide2
from PySide2 import QtCore, QtWidgets

pyside2_plugins = os.path.join(os.path.dirname(PySide2.__file__), "plugins")
QtWidgets.QApplication.addLibraryPath(pyside2_plugins)

Qt = QtCore.Qt
# noinspection PyArgumentList
qt_app = QtWidgets.QApplication.instance()

if not qt_app:
    if getattr(sys, 'frozen', None):  # pragma: no cover
        # noinspection PyArgumentList
        QtWidgets.QApplication.addLibraryPath(QtCore.QDir.currentPath())

    qt_app = QtWidgets.QApplication([])
