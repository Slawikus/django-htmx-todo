from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import ListView

from todos.models import Todo


class ListTodosView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'todos/list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        return self.request.user.todos.order_by('created_at').all()


class ToggleTodoCompletionView(LoginRequiredMixin, View):
    http_method_names = ["put"]

    def put(self, request, id, *args, **kwargs):
        todo: Todo = get_object_or_404(request.user.todos, id=id)

        todo.is_completed = not todo.is_completed
        todo.save(update_fields=['is_completed', 'updated_at'])

        return render(request, "todos/list.html#todo-item-partial", {"todo": todo})
