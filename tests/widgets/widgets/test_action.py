import unittest
from quina import core, widgets


class MyTestCase(unittest.TestCase):
    def test_action(self):
        main_window = widgets.MainWindow()
        action = widgets.Action(main_window)
        executed = []

        @core.connect_with(action.excited)
        def action_excite():
            executed.append(True)

        action.enabled = True
        action.click()
        action.enabled = False
        action.click()

        self.assertEqual(executed, [True])


if __name__ == '__main__':
    unittest.main()
