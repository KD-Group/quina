import unittest
from quina.core import SizeF


class MyTestCase(unittest.TestCase):
    def test_size_property(self):
        mock_width = 40.0
        mock_height = 30.0
        size = SizeF(mock_width, mock_height)

        self.assertEqual(size.w, mock_width)
        self.assertEqual(size.h, mock_height)

    def test_size_calculation(self):
        mock_width = 40.0
        mock_height = 30.0

        size = SizeF(mock_width, mock_height)
        self.assertEqual(size + size, SizeF(80, 60))
        self.assertEqual(size - size, SizeF(0, 0))
        self.assertEqual(size * 1.5, SizeF(60, 45))
        self.assertEqual(1.5 * size, SizeF(60, 45))
        self.assertEqual(size / 2.0, SizeF(20, 15))

        mock_margin = 5
        self.assertEqual(size + mock_margin, SizeF(45, 35))
        self.assertEqual(mock_margin + size, SizeF(45, 35))

        self.assertEqual(-size, SizeF(-40, -30))

    def test_size_split(self):
        mock_width = 40.0
        mock_height = 30.0

        size = SizeF(mock_width, mock_height)
        self.assertEqual(size.horizontal, SizeF(mock_width, 0))
        self.assertEqual(size.vertical, SizeF(0, mock_height))


if __name__ == '__main__':
    unittest.main()
