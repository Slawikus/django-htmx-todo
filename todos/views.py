from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from todos.models import Todo


class ListTodosView(ListView, LoginRequiredMixin):
    model = Todo
    template_name = 'todos/list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        return self.request.user.todos.order_by('created_at').all()
