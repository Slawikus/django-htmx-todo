from http import HTTPStatus

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView

from todos.forms import AddTodoForm
from todos.models import Todo


class ListTodosView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'todos/list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        return self.request.user.todos.order_by('created_at').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_todo_form'] = CreateTodoView().get_form_class()

        return context


class ToggleTodoCompletionView(LoginRequiredMixin, View):
    http_method_names = ['put']

    def put(self, request, pk, *args, **kwargs):
        todo: Todo = get_object_or_404(request.user.todos, id=pk)

        todo.is_completed = not todo.is_completed
        todo.save(update_fields=['is_completed', 'updated_at'])

        return render(request, 'todos/list.html#todo-item-partial', {'todo': todo})


class CreateTodoView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = AddTodoForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        todo = form.save()

        return render(self.request, 'todos/list.html#todo-item-partial', {'todo': todo})


class DeleteTodoView(LoginRequiredMixin, DeleteView):
    model = Todo

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()

        response = HttpResponse(status=HTTPStatus.NO_CONTENT)
        response['HX-Trigger'] = 'todo-deleted'

        return response


