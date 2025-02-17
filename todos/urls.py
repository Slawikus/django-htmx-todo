from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.ListTodosView.as_view(), name='list'),
    path('<int:pk>/', views.TodoDetailView.as_view(), name='detail'),
    path('<int:pk>/toggle/', views.ToggleTodoCompletionView.as_view(), name='toggle-completion'),
    path('<int:pk>/delete/', views.DeleteTodoView.as_view(), name='delete'),
    path('<int:pk>/edit/', views.UpdateTodoView.as_view(), name='edit'),
    path('create/', views.CreateTodoView.as_view(), name='create'),
]
