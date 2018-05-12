import unittest
from quina import model


class MockProject(model.AbstractProject):
    def __init__(self):
        self.name = model.types.StringItem(self)
        self.age = model.types.IntegerItem(self)


class MyTestCase(unittest.TestCase):
    def test_project_item_changed(self):
        project = MockProject()

        executed = []
        project.changed.connect(lambda _: executed.append('project changed'))
        project.name.changed.connect(lambda _: executed.append('project.name changed'))

        project.name.string.value = 'Swallow'
        self.assertEqual(project.value, {'name': 'Swallow'})
        self.assertEqual(executed, ['project.name changed', 'project changed'])

    def test_project_set_value(self):
        project = MockProject()

        name, age = 'Swallow', 25
        project.value = {
            'name': name,
            'age': age
        }

        self.assertEqual(project.name.string.value, name)
        self.assertEqual(project.age.integer.value, age)

        project.age.integer.value += 1
        self.assertEqual(project.value, {
            'name': name,
            'age': age + 1
        })


if __name__ == '__main__':
    unittest.main()
