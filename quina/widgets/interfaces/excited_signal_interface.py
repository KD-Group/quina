from ... import SignalSender
from ...model.base import AttachMixin


class ExcitedSignalInterface(AttachMixin):
    @property
    def excited(self) -> SignalSender:
        return self.attach(creator=SignalSender, after_created=self.set_excited_signal_connection)

    def set_excited_signal_connection(self):
        raise NotImplementedError
