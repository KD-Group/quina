import unittest
from quina import core, widgets


class MyTestCase(unittest.TestCase):
    def test_set_central_widget(self):
        main_window = widgets.MainWindow()
        sub_widget = widgets.Widget()
        main_window.set_central_widget(sub_widget)
        self.assertIsNotNone(main_window.center_widget)
        main_window.close()

        dock_widget = widgets.DockWidget()
        sub_widget = widgets.Widget()
        dock_widget.set_central_widget(sub_widget)
        self.assertIsNotNone(dock_widget.center_widget)
        dock_widget.set_focus()
        dock_widget.close()


if __name__ == '__main__':
    unittest.main()
