__all__ = ('SignalSender', 'connect_with')
from PySide2.QtCore import QObject, Signal


class SignalWrapper(QObject):
    signal = Signal(object)


class SignalSender:
    def __init__(self):
        self.signal = SignalWrapper()
        self.last_error: Exception = None

    def emit(self, *args, **kwargs):
        self.last_error = None

        # noinspection PyUnresolvedReferences
        self.signal.signal.emit((args, kwargs))

        if self.last_error:
            raise self.last_error

    def connect(self, func, *args, **kwargs):
        def slot_func(data, *_):
            try:
                return func(*args, *data[0], **kwargs, **data[1])
            except Exception as e:
                self.last_error = e
        slot_func.__name__ = getattr(func, '__name__', '<Lambda>')

        # noinspection PyUnresolvedReferences
        self.signal.signal.connect(slot_func)


def connect_with(signal: SignalSender, *args, **kwargs):
    def pack_func(func):
        signal.connect(func, *args, **kwargs)
        return func
    return pack_func
