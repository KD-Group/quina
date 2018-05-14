import unittest
from quina import Qt
from quina.gui import Pen, Brush


class MyTestCase(unittest.TestCase):
    def test_pen_init(self):
        mock_width = 1.0

        pen_1 = Pen(Qt.blue)
        pen_2 = Pen(Brush(Qt.blue), width=mock_width)

        self.assertAlmostEqual(pen_2.width, mock_width)
        self.assertAlmostEqual(pen_1.width, pen_2.width)


if __name__ == '__main__':
    unittest.main()
