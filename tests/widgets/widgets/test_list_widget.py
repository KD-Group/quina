import unittest
from quina import core, widgets


class MyTestCase(unittest.TestCase):
    def test_list_widget_row(self):
        with core.EventLoop(0.1):
            list_widget = widgets.ListWidget()
            list_widget.show()
            executed = [False]

            @core.connect_with(list_widget.string.changed)
            def text_changed(text):
                self.assertEqual(text, '1')
                executed[0] = True

            list_widget.string_list.value = [str(i) for i in range(10)]
            list_widget.index.value = 1
            self.assertTrue(executed[0])

    def test_list_widget_string_list(self):
        with core.EventLoop(0.1):
            list_widget = widgets.ListWidget()
            list_widget.show()
            executed = [False]
            string_list = ['0', '3']

            @core.connect_with(list_widget.string_list.changed)
            def string_list_changed(string_list_now):
                self.assertEqual(string_list, string_list_now)
                executed[0] = True

            list_widget.string_list.value = string_list
            self.assertTrue(executed[0])

    def test_list_widget_set_text(self):
        with core.EventLoop(0.1):
            list_widget = widgets.ListWidget()
            list_widget.show()
            times = []

            @core.connect_with(list_widget.string.changed)
            def text_changed(string):
                if len(times) == 0:
                    self.assertEqual(string, 'first')
                elif len(times) == 1:
                    self.assertEqual(string, 'second')
                elif len(times) == 2:
                    self.assertEqual(string, 'first')
                elif len(times) == 3:
                    self.assertEqual(string, None)
                times.append(len(times))

            list_widget.string_list.value = ['first', 'second']
            list_widget.string.set_value('first')
            list_widget.string.set_value('second')
            list_widget.string.set_value('first')
            self.assertEqual(len(times), 3)
            self.assertEqual(list_widget.count(), 2)

            list_widget.clear()
            with self.assertRaises(ValueError):
                list_widget.string.set_value('first')

            list_widget.excited.emit_if_changed()


if __name__ == '__main__':
    unittest.main()
