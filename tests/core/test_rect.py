import unittest
from quina.core import RectF, PointF, SizeF


class MyTestCase(unittest.TestCase):
    def test_rect_creation(self):
        mock_x, mock_y = 100, 120
        point = PointF(mock_x, mock_y)

        mock_width, mock_height = 30, 40
        size = SizeF(mock_width, mock_height)

        self.assertEqual(RectF.left_top_at(point=point, size=size), RectF(
            mock_x, mock_y,
            mock_width, mock_height
        ))
        self.assertEqual(RectF.right_top_at(point=point, size=size), RectF(
            mock_x - mock_width, mock_y,
            mock_width, mock_height
        ))
        self.assertEqual(RectF.left_bottom_at(point=point, size=size), RectF(
            mock_x, mock_y - mock_height,
            mock_width, mock_height
        ))
        self.assertEqual(RectF.right_bottom_at(point=point, size=size), RectF(
            mock_x - mock_width, mock_y - mock_height,
            mock_width, mock_height
        ))

        self.assertEqual(RectF.center_at(point=point, size=size), RectF(
            mock_x - mock_width / 2, mock_y - mock_height / 2,
            mock_width, mock_height
        ))
        self.assertEqual(RectF.top_center_at(point=point, size=size), RectF(
            mock_x - mock_width / 2, mock_y,
            mock_width, mock_height
        ))
        self.assertEqual(RectF.bottom_center_at(point=point, size=size), RectF(
            mock_x - mock_width / 2, mock_y - mock_height,
            mock_width, mock_height
        ))
        self.assertEqual(RectF.left_center_at(point=point, size=size), RectF(
            mock_x, mock_y - mock_height / 2,
            mock_width, mock_height
        ))
        self.assertEqual(RectF.right_center_at(point=point, size=size), RectF(
            mock_x - mock_width, mock_y - mock_height / 2,
            mock_width, mock_height
        ))

    def test_rect_vertices(self):
        mock_x, mock_y = 100, 120
        point = PointF(mock_x, mock_y)

        mock_width, mock_height = 30, 40
        size = SizeF(mock_width, mock_height)

        rect = RectF(point, size)
        self.assertEqual(rect.left_top, point)
        self.assertEqual(rect.right_top, point + size.horizontal)
        self.assertEqual(rect.left_bottom, point + size.vertical)
        self.assertEqual(rect.right_bottom, point + size)
        self.assertEqual(rect.center, point + size / 2)


if __name__ == '__main__':
    unittest.main()
