from django.db import models

from users.models import User


class Todo(models.Model):
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        related_name="todos",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'User {self.user_id}: [{self.id}] {self.title}'
