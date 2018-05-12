from ..base import ValueInterface
from ..base import ChangedValueEntity
from ..base import AbstractItem, AbstractProperty


class StringTypeMixin(ValueInterface):
    @property
    def value(self) -> str:
        return self.get_value()

    @value.setter
    def value(self, value):
        self.set_value(value)


class StringTypeProperty(AbstractProperty, StringTypeMixin):
    pass


class StringPropertyInterface(ChangedValueEntity):
    @property
    def string(self) -> StringTypeProperty:
        return self.attach(creator=StringTypeProperty, args=(
            self.get_string_value, self.set_string_value, self.changed
        ))

    def get_string_value(self) -> str:
        return self.get_value()

    def set_string_value(self, value: str):
        return self.set_value(value)


class StringItem(AbstractItem, StringPropertyInterface):
    pass
