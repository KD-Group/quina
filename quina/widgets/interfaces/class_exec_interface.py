class ClassExecInterface:
    def exec(self):
        raise NotImplementedError

    @classmethod
    def class_exec(cls, *args, **kwargs):
        # noinspection PyArgumentList
        cls(*args, **kwargs).exec()  # pragma: no cover
