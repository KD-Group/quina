import unittest
from quina import core, widgets


class MyTestCase(unittest.TestCase):
    def test_line_edit_text(self):
        with core.EventLoop(0.1):
            line_edit = widgets.LineEdit()
            line_edit.show()
            times = []

            @core.connect_with(line_edit.string.changed)
            def text_changed(text):
                if len(times) == 0:
                    self.assertEqual(text, 'first')
                elif len(times) == 1:
                    self.assertEqual(text, 'second')
                times.append(len(times))

            line_edit.string.value = 'first'
            line_edit.string.value = 'second'
            self.assertEqual(len(times), 2)

    def test_line_edit_int_change(self):
        line_edit = widgets.LineEdit()
        times = []
        mock_integer_1 = 3
        mock_integer_2 = 2
        mock_not_integer = '雾失楼台，月迷津渡'
        mock_float = 0.6

        @core.connect_with(line_edit.integer.changed)
        def integer_changed(value: int):
            if len(times) == 0:
                self.assertEqual(value, mock_integer_1)
            elif len(times) == 1:
                self.assertEqual(value, 0)
            elif len(times) == 2:
                self.assertEqual(value, mock_integer_2)
            times.append(len(times))

        @core.connect_with(line_edit.float.changed)
        def float_changed(_: float):
            pass

        line_edit.string.value = str(mock_integer_1)
        self.assertEqual(len(times), 1)

        line_edit.string.value = str(mock_not_integer)
        self.assertEqual(len(times), 2)

        line_edit.string.value = str(mock_integer_2)
        self.assertEqual(len(times), 3)

        line_edit.string.value = str(mock_float)
        self.assertEqual(len(times), 4)
        self.assertEqual(line_edit.float.value, mock_float)

        line_edit.integer.value = 0
        self.assertEqual(line_edit.string.value, '0')
        line_edit.float.value = 0.26
        self.assertEqual(line_edit.string.value, '0.26')


if __name__ == '__main__':
    unittest.main()
