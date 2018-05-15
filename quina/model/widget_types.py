from .base import AbstractItem, ChangedValueEntity
from .types import StringItem, IntegerItem, FloatItem
from .types import IntegerTypeProperty


class WidgetStringItem(StringItem, IntegerItem, FloatItem):
    def get_integer_value(self) -> int:
        try:
            return int(self.get_string_value())
        except ValueError:
            return 0

    def set_integer_value(self, value: int):
        self.set_string_value(str(value))

    def get_float_value(self) -> float:
        try:
            return float(self.get_string_value())
        except ValueError:
            return 0

    def set_float_value(self, value: float):
        self.set_string_value(str(value))


class IndexPropertyInterface(ChangedValueEntity):
    @property
    def index(self) -> IntegerTypeProperty:
        return self.attach(creator=IntegerTypeProperty, args=(
            self.get_index_value, self.set_index_value, self.changed
        ))

    def get_index_value(self) -> int:
        raise NotImplementedError

    def set_index_value(self, value: int):
        raise NotImplementedError


class WidgetIndexItem(AbstractItem, IndexPropertyInterface):
    def get_index_value(self) -> int:
        raise NotImplementedError

    def set_index_value(self, value: int):
        raise NotImplementedError
