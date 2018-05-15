import unittest
from quina import core, widgets


class MyTestCase(unittest.TestCase):
    def test_widget_exec(self):
        w = widgets.Widget()
        executed = [False]

        @core.connect_with(w.closed)
        def is_closed():
            executed[0] = True

        timer = core.Timer(single_shot=True)
        timer.timeout.connect(w.close)
        timer.start(0.1)

        w.exec()
        self.assertTrue(executed[0])

    def test_widget_cannot_close(self):
        w = widgets.Widget()
        w.can_close = False
        executed = [False]

        @core.connect_with(w.cannot_closed)
        def cannot_closed_event():
            executed[0] = True

        timer = core.Timer(single_shot=True)
        timer.timeout.connect(w.close)
        timer.start(0.1)

        self.assertFalse(executed[0])
        core.wait(0.2)
        self.assertTrue(executed[0])

        w.can_close = True
        w.close()

    def test_widget_background_color(self):
        w = widgets.Widget()
        w.background_color = core.Qt.blue
        self.assertEqual(w.background_color, core.Qt.blue)

        w.show()
        core.wait(0.1)
        w.close()


if __name__ == '__main__':
    unittest.main()
