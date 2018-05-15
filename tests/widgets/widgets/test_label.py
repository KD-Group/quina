import unittest
from quina import core, widgets


class MyTestCase(unittest.TestCase):
    def test_label_text(self):
        with core.EventLoop(0.1):
            label = widgets.Label()
            label.show()
            times = []

            @core.connect_with(label.string.changed)
            def text_changed(text):
                if len(times) == 0:
                    self.assertEqual(text, 'first')
                elif len(times) == 1:
                    self.assertEqual(text, 'second')
                times.append(len(times))

            label.string.value = 'first'
            label.string.value = 'second'
            self.assertEqual(len(times), 2)


if __name__ == '__main__':
    unittest.main()
