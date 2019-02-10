import unittest
from quina import core, widgets


class MyTestCase(unittest.TestCase):
    def test_main_window(self):
        main_window = widgets.MainWindow()
        executed = [False]

        @core.connect_with(main_window.closed)
        def is_closed():
            executed[0] = True

        timer = core.Timer(single_shot=True)
        timer.timeout.connect(main_window.close)
        timer.start(0.1)

        main_window.exec()
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
