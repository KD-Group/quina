import unittest
from quina import core, widgets


class MyTestCase(unittest.TestCase):
    def test_push_button_text(self):
        push_button = widgets.PushButton()
        push_button.show()
        times = []

        @core.connect_with(push_button.string.changed)
        def text_changed(text):
            if len(times) == 0:
                self.assertEqual(text, 'first')
            elif len(times) == 1:
                self.assertEqual(text, 'second')
            times.append(len(times))

        push_button.string.value = 'first'
        push_button.string.value = 'second'
        self.assertEqual(len(times), 2)

        push_button.close()

    def test_push_button_triggered(self):
        push_button = widgets.PushButton()
        push_button.show()
        times = []

        @core.connect_with(push_button.excited)
        def button_clicked():
            if len(times) == 0:
                self.assertEqual(push_button.string.value, 'first')
            elif len(times) == 1:
                self.assertEqual(push_button.string.value, 'second')
            times.append(len(times))

        push_button.string.value = 'first'
        push_button.click()
        push_button.string.value = 'second'
        push_button.click()
        self.assertEqual(len(times), 2)

        push_button.close()


if __name__ == '__main__':
    unittest.main()
