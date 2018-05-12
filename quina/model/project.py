import typing
from .base import AbstractContainer
from .types import DictTypeMixin


class AbstractProject(AbstractContainer, DictTypeMixin):
    def get_value(self) -> dict:
        return self.attach(creator=dict)

    def set_value(self, value) -> None:
        self.value.clear()
        self.value.update(value)
        self.changed.emit(self.value)

    def get_property(self, name) -> typing.Any:
        return self.value.get(name)

    def set_property(self, name, value) -> None:
        self.value.update({name: value})
        self.changed.emit(self.value)
