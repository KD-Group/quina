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


if __name__ == '__main__':
    unittest.main()
