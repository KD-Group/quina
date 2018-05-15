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


if __name__ == '__main__':
    unittest.main()
