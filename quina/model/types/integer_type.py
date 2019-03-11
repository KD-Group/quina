from ..base import ValueInterface
from ..base import ChangedValueEntity
from ..base import AbstractItem, AbstractProperty


class IntegerTypeMixin(ValueInterface):
    @property
    def value(self) -> int:
        return self.get_value()

    @value.setter
    def value(self, value):
        self.set_value(value)


class IntegerTypeProperty(AbstractProperty, IntegerTypeMixin):
    pass


class IntegerPropertyInterface(ChangedValueEntity):
    @property
    def integer(self) -> IntegerTypeProperty:
        return self.attach(creator=IntegerTypeProperty, args=(
            self.get_integer_value, self.set_integer_value, self.changed
        ))

    def get_integer_value(self) -> int:
        return self.get_value()

    def set_integer_value(self, value: int):
        return self.set_value(value)


class IntegerItem(AbstractItem, IntegerPropertyInterface):
    pass
