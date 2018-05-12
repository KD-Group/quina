__all__ = ('SignalSender', 'connect_with')
import typing
from PySide2.QtCore import QObject, Signal


class SignalWrapper(QObject):
    _signal = Signal(object)

    def emit_signal(self, value: tuple):
        # noinspection PyUnresolvedReferences
        self._signal.emit(value)

    def connect_slot(self, slot):
        # noinspection PyUnresolvedReferences
        self._signal.connect(slot)


class SignalSender:
    def __init__(self):
        self.signal = SignalWrapper()
        self.errors: typing.List[Exception] = []
        self.last_emit: typing.Tuple[list, dict] = None

    @property
    def last_error(self) -> Exception:
        return self.errors[-1] if len(self.errors) else None

    def emit(self, *args, **kwargs):
        self.errors.clear()

        self.last_emit = (args, kwargs)
        self.signal.emit_signal(self.last_emit)

        if self.last_error:
            raise self.last_error

    def emit_if_changed(self, *args, **kwargs):
        emit_value = (args, kwargs)
        if self.last_emit != emit_value:
            self.emit(*args, **kwargs)

    def connect(self, func, *args, **kwargs):
        errors = self.errors

        # never use `self` in slot function, which will cause a memory leak
        def slot_func(data, *_):
            try:
                return func(*args, *data[0], **kwargs, **data[1])
            except Exception as e:
                errors.append(e)
        slot_func.__name__ = getattr(func, '__name__', '<Lambda>')

        self.signal.connect_slot(slot_func)


def connect_with(signal: SignalSender, *args, **kwargs):
    def pack_func(func):
        signal.connect(func, *args, **kwargs)
        return func
    return pack_func
