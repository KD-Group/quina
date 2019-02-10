import unittest
from quina import core, widgets


class MyTestCase(unittest.TestCase):
    def test_dialog(self):
        dialog = widgets.Dialog()
        executed = [False]

        @core.connect_with(dialog.closed)
        def is_closed():
            executed[0] = True

        timer = core.Timer(single_shot=True)
        timer.timeout.connect(dialog.close)
        timer.start(0.1)

        dialog.exec()
        self.assertTrue(executed[0])

    @staticmethod
    def test_message_box():
        dialog = widgets.Dialog()

        timer = core.Timer(single_shot=True)
        timer.timeout.connect(lambda: dialog.question("测试question"))
        timer.start(0.1)

        timer = core.Timer(single_shot=True)
        timer.timeout.connect(lambda: dialog.warning("测试warning"))
        timer.start(0.1)

        timer = core.Timer(single_shot=True)
        timer.timeout.connect(lambda: dialog.information("测试information"))
        timer.start(0.1)

        timer = core.Timer(single_shot=True)
        timer.timeout.connect(lambda: dialog.about("测试about"))
        timer.start(0.1)

        timer = core.Timer(single_shot=True)
        timer.timeout.connect(lambda: dialog.message())
        timer.start(0.1)

        timer = core.Timer(single_shot=True)
        timer.timeout.connect(lambda: dialog.message(ok=False))
        timer.start(0.1)


if __name__ == '__main__':
    unittest.main()
