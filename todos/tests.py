from django.test import TestCase

from ddf import G

from todos.models import Todo
from users.models import User


class TodoTest(TestCase):
    def test_it_defines_reverse_relation_on_user(self):
        # Arrange
        user_1, user_2 = G(User, n=2)

        todo_1 = G(Todo, user=user_1)
        todo_2, todo_3 = G(Todo, user=user_2, n=2)
        # Act & Assert
        self.assertCountEqual([todo_1], user_1.todos.all())
        self.assertCountEqual([todo_2, todo_3], user_2.todos.all())

    def test_it_has_string_representation(self):
        # Arrange
        todo = G(Todo, title="Buy milk")
        # Act & Assert
        self.assertEqual(f'User {todo.user.id}: [{todo.id}] Buy milk', str(todo))
