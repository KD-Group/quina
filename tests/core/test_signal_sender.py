import unittest
import quina


class MyTestCase(unittest.TestCase):
    def test_signal(self):
        signal = quina.SignalSender()
        executed = [False]

        def slot():
            self.assertEqual(True, True)
            executed[0] = True
        signal.connect(slot)

        signal.emit()
        self.assertTrue(executed[0])

    def test_signal_with_parameters(self):
        signal = quina.SignalSender()
        executed = [False]

        def slot(a: int, b: int, c: int):
            self.assertEqual(a, 1)
            self.assertEqual(b, 2)
            self.assertEqual(c, 3)
            executed[0] = True
        signal.connect(slot)

        signal.emit(a=1, b=2, c=3)
        self.assertTrue(executed[0])

    def test_connect_with(self):
        signal = quina.SignalSender()
        executed = [False]

        @quina.connect_with(signal, 1, b=2)
        def slot(a: int, b: int, c: int):
            self.assertEqual(a, 1)
            self.assertEqual(b, 2)
            self.assertEqual(c, 3)
            executed[0] = True

        signal.emit(c=3)
        self.assertTrue(executed[0])

    def test_slot_exception(self):
        def slot():
            raise ValueError('03 26')

        signal = quina.SignalSender()
        signal.connect(slot)

        with self.assertRaises(ValueError):
            signal.emit()  # oops, slot raise a ValueError


if __name__ == '__main__':
    unittest.main()
