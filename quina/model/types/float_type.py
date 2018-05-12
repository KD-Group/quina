from ..base import ValueInterface
from ..base import ChangedValueEntity
from ..base import AbstractItem, AbstractProperty


class FloatTypeMixin(ValueInterface):
    @property
    def value(self) -> float:
        return self.get_value()

    @value.setter
    def value(self, value):
        self.set_value(value)


class FloatTypeProperty(AbstractProperty, FloatTypeMixin):
    pass


class FloatPropertyInterface(ChangedValueEntity):
    @property
    def float(self) -> FloatTypeProperty:
        return self.attach(creator=FloatTypeProperty, args=(
            self.get_float_value, self.set_float_value, self.changed
        ))

    def get_float_value(self) -> float:
        return self.get_value()

    def set_float_value(self, value: float):
        return self.set_value(value)


class FloatItem(AbstractItem, FloatPropertyInterface):
    pass
