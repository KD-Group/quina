import unittest
from quina import core, widgets


class MyTestCase(unittest.TestCase):
    def test_combo_box_row(self):
        with core.EventLoop(0.1):
            combo_box = widgets.ComboBox()
            combo_box.show()

            mock_string_list = ['0', '3', '2', '6']
            combo_box.string_list.value = mock_string_list
            self.assertEqual(combo_box.string_list.value, mock_string_list)

            mock_string_list.pop(-1)
            combo_box.string_list.value = mock_string_list
            self.assertEqual(combo_box.string_list.value, mock_string_list)
            self.assertEqual(combo_box.count(), len(mock_string_list))

    def test_combo_box_string_list(self):
        with core.EventLoop(0.1):
            combo_box = widgets.ComboBox()
            combo_box.show()
            executed = [False]

            mock_string_list = ['0', '3', '2', '6']

            @core.connect_with(combo_box.string_list.changed)
            def string_list_changed(string_list_now):
                self.assertEqual(mock_string_list, string_list_now)
                executed[0] = True

            combo_box.string_list.value = mock_string_list
            self.assertTrue(executed[0])

    def test_combo_box_set_text(self):
        with core.EventLoop(0.1):
            combo_box = widgets.ComboBox()
            combo_box.show()
            times = []

            @core.connect_with(combo_box.string.changed)
            def text_changed(text):
                if len(times) == 0:
                    self.assertEqual(text, 'first')
                elif len(times) == 1:
                    self.assertEqual(text, 'second')
                elif len(times) == 2:
                    self.assertEqual(text, 'first')
                elif len(times) == 3:
                    self.assertEqual(text, '')
                times.append(len(times))

            combo_box.string_list.value = ['first', 'second']
            combo_box.string.set_value('first')
            combo_box.string.set_value('second')
            combo_box.string.set_value('first')
            self.assertEqual(len(times), 3)
            self.assertEqual(combo_box.count(), 2)

            with self.assertRaises(ValueError):
                combo_box.string.value = 'third'

            combo_box.clear()
            self.assertEqual(len(times), 4)
            self.assertEqual(combo_box.count(), 0)

    def test_combo_box_text_more_than_once(self):
        with core.EventLoop(0.1):
            combo_box = widgets.ComboBox()
            combo_box.show()

            mock_string_list_1 = ['TTL']
            mock_string_list_2 = ['LVTTL', 'LVPECL', 'LVDS', 'ECL']
            combo_box.string_list.value = mock_string_list_1
            combo_box.string_list.value = mock_string_list_2
            combo_box.string_list.value = mock_string_list_1

            self.assertEqual(combo_box.string_list.value, mock_string_list_1)


if __name__ == '__main__':
    unittest.main()
