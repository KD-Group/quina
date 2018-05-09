import pathlib
import unittest


class MyTestCase(unittest.TestCase):
    def test_import_requirements(self):
        root_path = pathlib.Path(__file__).parent.parent
        requirements_path = root_path / 'requirements.txt'
        with open(requirements_path) as f:
            requirement_list = f.read().splitlines()

        for requirement in requirement_list:
            self.assertIsNotNone(__import__(requirement))
        self.assertIsNotNone(__import__('quina'))


if __name__ == '__main__':
    unittest.main()
