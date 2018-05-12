import unittest
from quina import model


class MyTestCase(unittest.TestCase):
    def test_attach_mixin(self):
        class MockEntity(model.base.AttachMixin):
            @property
            def mock_property(self):
                return self.attach(list, args=(range(10),))

            @mock_property.setter
            def mock_property(self, value):
                self.assign(value)

        mock_entity = MockEntity()
        self.assertEqual(mock_entity.mock_property, list(range(10)))

        mock_list = [0, 3, 2, 6]
        mock_entity.mock_property = mock_list
        self.assertEqual(mock_entity.mock_property, mock_list)

    def test_item_connect(self):
        string_love_peace = 'love & peace'
        string_live_evil = 'live & evil'
        string_make_great = 'make great again!'
        string_steins_gate = 'Steins Gate~'

        a = model.types.StringItem()
        a.string.value = string_love_peace

        b = model.types.StringItem()
        b.string.value = string_live_evil

        a.string.connect(b.string)
        self.assertEqual(a.string.value, string_love_peace)
        self.assertEqual(b.string.value, string_love_peace)

        a.string.value = string_make_great
        self.assertEqual(a.string.value, string_make_great)
        self.assertEqual(b.string.value, string_make_great)

        b.set_value(string_steins_gate)
        self.assertEqual(a.string.value, string_steins_gate)
        self.assertEqual(b.string.value, string_steins_gate)


if __name__ == '__main__':
    unittest.main()
