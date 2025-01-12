from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.ListTodosView.as_view(), name='list'),
]
