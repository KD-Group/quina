import typing
import traceback
from .. import SignalSender


class ValueInterface:
    def get_value(self) -> typing.Any:
        pass  # pragma: no cover

    def set_value(self, value) -> None:
        pass  # pragma: no cover


class AttachMixin:
    AttachFlag = '_attach_{}_'

    def attach(self, creator, args: tuple = (), after_created: typing.Callable[[], None] = None):
        name = AttachMixin.AttachFlag.format(self.current_property_name)

        obj = getattr(self, name, None)
        if obj is None:
            obj = creator(*args)
            setattr(self, name, obj)
            if after_created:
                after_created()
        return obj

    def assign(self, value):
        name = AttachMixin.AttachFlag.format(self.current_property_name)
        setattr(self, name, value)

    @property
    def current_property_name(self):
        return traceback.extract_stack(None, 3)[0][2]


class ChangedMixin(ValueInterface, AttachMixin):
    @property
    def changed(self) -> SignalSender:
        return self.attach(creator=SignalSender, after_created=self.set_changed_connection)

    def check_change(self, *_):
        self.changed.emit_if_changed(self.get_value())

    def set_changed_connection(self):
        pass  # pragma: no cover


class ValueEntity(ValueInterface):
    pass


class ChangedValueEntity(ValueEntity, ChangedMixin):
    def connect(self, other: 'ChangedValueEntity'):
        self.changed.connect(other.set_value)
        other.changed.connect(self.set_value)
        other.set_value(self.get_value())


class AbstractProperty(ChangedValueEntity):
    def __init__(self,
                 source_getter: typing.Callable[[], typing.Any],
                 source_setter: typing.Callable[[typing.Any], None] = None,
                 source_changed: SignalSender = None
                 ):
        self.source_getter = source_getter
        self.source_setter = source_setter
        self.source_changed = source_changed

    def set_changed_connection(self) -> None:
        if self.source_changed is not None:
            self.source_changed.connect(self.check_change)

    def get_value(self) -> typing.Any:
        return self.source_getter()

    def set_value(self, value) -> None:
        self.source_setter(value)


class AbstractContainer(ChangedValueEntity):
    def get_property(self, name) -> typing.Any:
        raise NotImplementedError

    def set_property(self, name, value) -> None:
        raise NotImplementedError

    # children property
    @property
    def children(self) -> typing.List['AbstractItem']:
        return self.attach(list)

    def add(self, item: 'AbstractItem') -> None:
        self.children.append(item)
        self.changed.connect(item.check_change)

    # name property
    def __setattr__(self, key: str, value) -> None:
        if isinstance(value, AbstractItem):
            value.name = key
        super().__setattr__(key, value)


class AbstractItem(ChangedValueEntity):
    def __init__(self, container: AbstractContainer = None):
        self.name: str = None
        self._storage: typing.Any = None

        self.container = container
        if container is not None:
            container.add(self)

    def get_value(self) -> typing.Any:
        if self.container is not None:
            return self.container.get_property(self.name)
        else:
            return self._storage

    def set_value(self, value) -> None:
        if self.container is not None:
            self.container.set_property(self.name, value)
        else:
            self._storage = value
            self.check_change()
