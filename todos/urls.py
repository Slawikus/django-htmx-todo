from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.ListTodosView.as_view(), name='list'),
    path('<int:id>/toggle', views.ToggleTodoCompletionView.as_view(), name='toggle-completion'),
]
