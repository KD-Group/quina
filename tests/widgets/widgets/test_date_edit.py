import unittest
from quina import core, widgets


class MyTestCase(unittest.TestCase):
    def test_date_edit_text(self):
        with core.EventLoop(0.1):
            date_edit = widgets.DateEdit()
            date_edit.setDisplayFormat('yyyy-MM-dd')
            date_edit.show()
            times = []

            @core.connect_with(date_edit.string.changed)
            def text_changed(text):
                if len(times) == 0:
                    self.assertEqual(text, '2019-08-08')
                elif len(times) == 1:
                    self.assertEqual(text, '2020-08-08')
                times.append(len(times))

            date_edit.string.value = '2019-08-08'
            date_edit.string.value = '2020-08-08'
            self.assertEqual(len(times), 2)

            with self.assertRaises(ValueError):
                date_edit.string.value = '2019-08-08-11'


if __name__ == '__main__':
    unittest.main()
