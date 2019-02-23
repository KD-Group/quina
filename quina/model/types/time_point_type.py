import time

from ..base import ValueInterface
from ..base import ChangedValueEntity
from ..base import AbstractItem, AbstractProperty


class TimePointTypeMixin(ValueInterface):
    @property
    def value(self) -> str:
        return self.get_value()

    @value.setter
    def value(self, value):
        self.set_value(value)


class TimePointTypeProperty(AbstractProperty, TimePointTypeMixin):
    def update(self, t_format='%Y-%m-%d %H:%M:%S'):
        self.value = time.strftime(t_format)


class TimePointPropertyInterface(ChangedValueEntity):
    @property
    def time(self) -> TimePointTypeProperty:
        return self.attach(creator=TimePointTypeProperty, args=(
            self.get_time_value, self.set_time_value, self.changed
        ))

    def get_time_value(self) -> str:
        return self.get_value()

    def set_time_value(self, value: str):
        if not isinstance(value, str):
            raise ValueError(f'UnSupport Set Value Type {type(value)} to Type str')
        return self.set_value(value)


class TimePointItem(AbstractItem, TimePointPropertyInterface):
    pass
