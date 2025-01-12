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
                'autofocus': 'autofocus',
            }),
        }


class UpdateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'is_completed']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control flex-grow-1 fs-5',
                'placeholder': 'Add a title',
            }),
            'is_completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input me-3',
            }),
        }
