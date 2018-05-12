from ..base import ValueInterface
from ..base import ChangedValueEntity
from ..base import AbstractItem, AbstractProperty


class ListTypeMixin(ValueInterface):
    @property
    def value(self) -> list:
        return self.get_value()

    @value.setter
    def value(self, value):
        self.set_value(value)


class ListTypeProperty(AbstractProperty, ListTypeMixin):
    pass


class ListPropertyInterface(ChangedValueEntity):
    @property
    def list(self) -> ListTypeProperty:
        return self.attach(creator=ListTypeProperty, args=(
            self.get_list_value, self.set_list_value, self.changed
        ))

    def get_list_value(self) -> list:
        return self.get_value()

    def set_list_value(self, value: list):
        return self.set_value(value)


class ListItem(AbstractItem, ListPropertyInterface):
    pass
