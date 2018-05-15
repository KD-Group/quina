import unittest
from quina.widgets.widgets import BaseWidget


class MyTestCase(unittest.TestCase):
    def test_set_layout(self):
        widget = BaseWidget()
        widget.setMinimumSize(400, 300)

        sub_widget = BaseWidget(widget)
        widget.set_square_widget(sub_widget)
        widget.show()

        widget.layout().setSpacing(1)
        widget.layout().update()

        sub_widget_2 = BaseWidget(widget)
        widget.set_square_widget(sub_widget_2)

        self.assertIsNotNone(widget.layout().takeAt(0))


if __name__ == '__main__':
    unittest.main()
