from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    task = forms.CharField(widget=forms.TextInput(attrs = {'placeholder': 'Enter Task.......'}))
    
    class Meta:
        model = Todo
        fields = '__all__'