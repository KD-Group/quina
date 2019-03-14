import unittest
from quina import core, widgets, connect_with


class MyTestCase(unittest.TestCase):
    header_labels = ['字符串', '整形', '浮点型']
    set_value_one = ['first', 1, 1.1]
    set_value_two = ['second', 2, 2.2]

    def setUp(self):
        self.table_widget = widgets.TableWidget()
        self.table_widget.set_just_show_mode()
        self.table_widget.header_labels = self.header_labels

    def test_table_widget_set_header(self):
        with core.EventLoop(0.1):
            self.assertEqual(self.table_widget.header_labels, self.header_labels)
            header_labels2 = ['first', 'second', 'third', 'fourth']
            self.table_widget.header_labels = header_labels2

    def test_table_widget_row(self):
        with core.EventLoop(0.1):
            self.table_widget.show()
            executed = [False]

            @core.connect_with(self.table_widget.index.changed)
            def text_changed(index):
                self.assertEqual(index, self.table_widget.currentRow())
                executed[0] = True

            set_value = ['first', 1, 1.1]
            for i in range(10):
                self.table_widget.string_list.value = set_value
                self.assertEqual(self.table_widget.index.value, self.table_widget.currentRow())
            self.table_widget.index.value = 2
            self.assertTrue(executed[0])

    def test_set_table_widget_string_list_value(self):
        with core.EventLoop(0.1):
            string_list_value = ['1', 2, 3.0]
            self.table_widget.string_list.value = string_list_value
            self.assertEqual(self.table_widget.string_list.value, [str(value) for value in string_list_value])

    def test_row_changed_signal_emitted(self):
        with core.EventLoop(0.1):
            executed = [False]
            changed_times = []

            @connect_with(self.table_widget.string_list.changed)
            def test_signal_emitted(string_list_value):
                executed[0] = True
                if len(changed_times) == 0:
                    self.assertEqual(self.table_widget.string_list.value, [str(value) for value in string_list_value])
                elif len(changed_times) == 1:
                    self.assertEqual(self.table_widget.string_list.value, [str(value) for value in string_list_value])
                changed_times.append(len(changed_times))

            self.table_widget.string_list.value = self.set_value_one
            self.table_widget.string_list.value = self.set_value_two
            self.assertTrue(executed[0])

    def test_get_string_list_by_index(self):
        with core.EventLoop(0.1):
            mock_value_one = ['first', 1, 1.1]
            mock_value_two = ['second', 2, 2.2]
            self.table_widget.string_list.value = mock_value_one
            self.table_widget.string_list.value = mock_value_two
            self.assertEqual(self.table_widget.get_string_list_by_index(self.table_widget.index.value),
                             [str(value) for value in mock_value_two])
            self.table_widget.index.value = 0
            self.assertEqual(self.table_widget.get_string_list_by_index(self.table_widget.index.value),
                             [str(value) for value in mock_value_one])
            with self.assertRaises(ValueError):
                self.table_widget.get_string_list_by_index(-1)
            with self.assertRaises(ValueError):
                self.table_widget.get_string_list_by_index(2)

    def test_header_labels_changed(self):
        with core.EventLoop(0.1):
            changed_times = []
            executed = [False]

            @core.connect_with(self.table_widget.header_labels_changed)
            def header_labels_changed(head_labels):
                executed[0] = True
                if len(changed_times) == 0:
                    self.assertEqual(head_labels, mock_labels)
                changed_times.append(len(changed_times))

            mock_labels = ['a', 'b', 'c']
            self.table_widget.header_labels = mock_labels
            self.assertTrue(executed[0])


if __name__ == '__main__':
    unittest.main()
