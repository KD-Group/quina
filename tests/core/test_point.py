import unittest
from quina.core import PointF, SizeF


class MyTestCase(unittest.TestCase):
    def test_point_property(self):
        mock_x = 40.0
        mock_y = 30.0
        point = PointF(mock_x, mock_y)

        self.assertEqual(point.x, mock_x)
        self.assertEqual(point.y, mock_y)

        point.x += 10
        point.y -= 10
        self.assertEqual(point, PointF(mock_x + 10, mock_y - 10))

    def test_point_calculation(self):
        mock_x = 40.0
        mock_y = 30.0

        point = PointF(mock_x, mock_y)
        self.assertEqual(point + point, PointF(80, 60))
        self.assertEqual(point - point, PointF(0, 0))
        self.assertEqual(point * 1.5, PointF(60, 45))
        self.assertEqual(1.5 * point, PointF(60, 45))
        self.assertEqual(point / 2.0, PointF(20, 15))

        mock_margin = 5
        self.assertEqual(point + mock_margin, PointF(45, 35))
        self.assertEqual(mock_margin + point, PointF(45, 35))

        self.assertEqual(-point, PointF(-40, -30))

    def test_point_size_calculation(self):
        mock_x = 40.0
        mock_y = 30.0
        point = PointF(mock_x, mock_y)

        mock_width = 20
        mock_height = 10
        size = SizeF(mock_width, mock_height)
        self.assertEqual(point + size, PointF(mock_x + mock_width, mock_y + mock_height))

    def test_point_split(self):
        mock_x = 40.0
        mock_y = 30.0
        point = PointF(mock_x, mock_y)

        self.assertEqual(point.horizontal, PointF(mock_x, 0))
        self.assertEqual(point.vertical, PointF(0, mock_y))


if __name__ == '__main__':
    unittest.main()
