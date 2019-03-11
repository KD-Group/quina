import typing
from ..base import ValueInterface
from ..base import ChangedValueEntity
from ..base import AbstractItem, AbstractProperty


class StringListTypeMixin(ValueInterface):
    @property
    def value(self) -> typing.List[str]:
        return self.get_value()

    @value.setter
    def value(self, value):
        self.set_value(value)


class StringListTypeProperty(AbstractProperty, StringListTypeMixin):
    pass


class StringListPropertyInterface(ChangedValueEntity):
    @property
    def string_list(self) -> StringListTypeProperty:
        return self.attach(creator=StringListTypeProperty, args=(
            self.get_string_list_value, self.set_string_list_value, self.changed
        ))

    def get_string_list_value(self) -> typing.List[str]:
        return self.get_value()

    def set_string_list_value(self, value: typing.List[str]):
        return self.set_value(value)


class StringListItem(AbstractItem, StringListPropertyInterface):
    pass
