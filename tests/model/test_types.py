import unittest
import time
from quina import model


class MockProject(model.AbstractProject):
    def __init__(self):
        self.money = model.types.FloatItem(self)
        self.ids = model.types.ListItem(self)
        self.books = model.types.StringListItem(self)
        self.scores = model.types.DictItem(self)
        self.sell_time = model.types.TimePointItem(self)


class MyTestCase(unittest.TestCase):
    def test_multi_types(self):
        project = MockProject()

        mock_money = 3.26
        project.money.float.value = mock_money
        self.assertEqual(project.money.float.value, mock_money)
        mock_wrong_type_money = '3.26'
        with self.assertRaises(ValueError):
            project.money.float.value = mock_wrong_type_money

        mock_ids = [1, 2, 1, 3, 8]
        project.ids.list.value = mock_ids
        self.assertEqual(project.ids.list.value, mock_ids)
        mock_wrong_type_ids = (1, 2, 1, 3, 8)
        with self.assertRaises(ValueError):
            project.ids.list.value = mock_wrong_type_ids

        mock_books = [
            'Machine Learning',
            'The Little Prince'
        ]
        project.books.string_list.value = mock_books
        self.assertEqual(project.books.string_list.value, mock_books)
        mock_wrong_type_books = ('Machine Learning', 'The Little Prince')
        with self.assertRaises(ValueError):
            project.books.string_list.value = mock_wrong_type_books

        mock_scores = {
            'math': 100,
            'english': 98,
            'philosophy': 20
        }
        project.scores.dict.value = mock_scores
        self.assertEqual(project.scores.dict.value, mock_scores)
        mock_wrong_type_scores = [100, 98, 20]
        with self.assertRaises(ValueError):
            project.scores.dict.value = mock_wrong_type_scores

        self.assertEqual(project.value, {
            'money': mock_money,
            'ids': mock_ids,
            'books': mock_books,
            'scores': mock_scores
        })

        t_format = '%Y-%m-%d %H:%M:%S'
        project.sell_time.time.update(t_format)
        mock_time = time.strftime(t_format)
        self.assertEqual(project.sell_time.time.value, mock_time)
        mock_wrong_type_time = 1994.9
        with self.assertRaises(ValueError):
            project.sell_time.time.value = mock_wrong_type_time


if __name__ == '__main__':
    unittest.main()
