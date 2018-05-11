__all__ = ('SignalSender', 'connect_with')
import typing
from PySide2.QtCore import QObject, Signal


class SignalWrapper(QObject):
    signal = Signal(object)


class SignalSender:
    def __init__(self):
        self.signal = SignalWrapper()
        self.errors: typing.List[Exception] = []

    @property
    def last_error(self) -> Exception:
        return self.errors[-1] if len(self.errors) else None

    def emit(self, *args, **kwargs):
        self.errors.clear()

        # noinspection PyUnresolvedReferences
        self.signal.signal.emit((args, kwargs))

        if self.last_error:
            raise self.last_error

    def connect(self, func, *args, **kwargs):
        errors = self.errors

        # never use `self` in slot function, which will cause a memory leak
        def slot_func(data, *_):
            try:
                return func(*args, *data[0], **kwargs, **data[1])
            except Exception as e:
                errors.append(e)
        slot_func.__name__ = getattr(func, '__name__', '<Lambda>')

        # noinspection PyUnresolvedReferences
        self.signal.signal.connect(slot_func)


def connect_with(signal: SignalSender, *args, **kwargs):
    def pack_func(func):
        signal.connect(func, *args, **kwargs)
        return func
    return pack_func
