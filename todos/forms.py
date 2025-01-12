from django import forms

from todos.models import Todo


class AddTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control flex-grow-1 fs-5',
                'placeholder': 'Add a new todo',
            }),
        }
