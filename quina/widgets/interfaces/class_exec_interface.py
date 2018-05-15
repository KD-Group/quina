class ClassExecInterface:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError

    def exec(self):
        raise NotImplementedError

    @classmethod
    def class_exec(cls, *args, **kwargs):
        cls(*args, **kwargs).exec()  # pragma: no cover
