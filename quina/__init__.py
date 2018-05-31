__name__ = 'quina'
__version__ = '0.0.4'
__description__ = 'PySide2 MVVM Framework'
__github__ = 'https://github.com/KD-Group/quina'

__author__ = 'SF-Zhou'
__email__ = 'sfzhou.scut@gmail.com'

from .core import SignalSender, connect_with
from .core import Qt, wait

from . import core
from . import model
from . import gui
from . import widgets
