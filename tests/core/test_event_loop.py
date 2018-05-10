import unittest
from time import time
from quina import wait


class MyTestCase(unittest.TestCase):
    def test_event_loop_timeout(self):
        wait_time_in_second = 0.1

        start_time = time()
        wait(seconds=wait_time_in_second)
        end_time = time()

        interval_in_seconds = end_time - start_time
        self.assertAlmostEqual(interval_in_seconds, wait_time_in_second, delta=0.05)


if __name__ == '__main__':
    unittest.main()
