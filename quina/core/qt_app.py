import sys
from PySide2 import QtCore, QtWidgets


Qt = QtCore.Qt
# noinspection PyArgumentList
qt_app = QtWidgets.QApplication.instance()

if not qt_app:
    if getattr(sys, 'frozen', None):  # pragma: no cover
        # noinspection PyArgumentList
        QtWidgets.QApplication.addLibraryPath(QtCore.QDir.currentPath())

    qt_app = QtWidgets.QApplication([])
