from http import HTTPStatus

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from todos.forms import AddTodoForm, UpdateTodoForm
from todos.models import Todo


class ListTodosView(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = 'todos'
    paginate_by = 10

    def get_queryset(self):
        queryset = self.request.user.todos.order_by('created_at').all()

        query = self.request.GET.get('query', None)
        if query:
            queryset = queryset.filter(title__icontains=query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_todo_form'] = CreateTodoView().get_form_class()

        return context

    def get_template_names(self):
        return ['todos/list.html#todo-item-partial'] if "HX-Request" in self.request.headers else ['todos/list.html']


class ToggleTodoCompletionView(LoginRequiredMixin, View):
    http_method_names = ['put']

    def put(self, request, pk, *args, **kwargs):
        todo: Todo = get_object_or_404(request.user.todos, id=pk)

        todo.is_completed = not todo.is_completed
        todo.save(update_fields=['is_completed'])

        return render(request, 'todos/list.html#todo-item-partial', {'todos': [todo]})


class CreateTodoView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = AddTodoForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        todo = form.save()

        return render(self.request, 'todos/list.html#todo-item-partial', {'todos': [todo]})


class DeleteTodoView(LoginRequiredMixin, DeleteView):
    model = Todo

    def get_queryset(self):
        return self.request.user.todos.all()

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()

        response = HttpResponse(status=HTTPStatus.NO_CONTENT)
        response['HX-Trigger'] = 'todo-deleted'

        return response


class UpdateTodoView(LoginRequiredMixin, UpdateView):
    model = Todo
    form_class = UpdateTodoForm
    context_object_name = 'todo'
    template_name = 'todos/update.html'

    def get_queryset(self):
        return self.request.user.todos.all()

    def form_valid(self, form):
        todo = form.save()

        return render(self.request, 'todos/list.html#todo-item-partial', {'todos': [todo]})


class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Todo
    context_object_name = 'todo'

    def get_queryset(self):
        return self.request.user.todos.all()

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        return render(self.request, 'todos/list.html#todo-item-partial', {'todos': [self.object]})
