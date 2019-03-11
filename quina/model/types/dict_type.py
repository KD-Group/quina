from ..base import ValueInterface
from ..base import ChangedValueEntity
from ..base import AbstractItem, AbstractProperty


class DictTypeMixin(ValueInterface):
    @property
    def value(self) -> dict:
        return self.get_value()

    @value.setter
    def value(self, value):
        self.set_value(value)


class DictTypeProperty(AbstractProperty, DictTypeMixin):
    pass


class DictPropertyInterface(ChangedValueEntity):
    @property
    def dict(self) -> DictTypeProperty:
        return self.attach(creator=DictTypeProperty, args=(
            self.get_dict_value, self.set_dict_value, self.changed
        ))

    def get_dict_value(self) -> dict:
        return self.get_value()

    def set_dict_value(self, value: dict):
        return self.set_value(value)


class DictItem(AbstractItem, DictPropertyInterface):
    pass
