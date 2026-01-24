from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "library"]  # include all fields you want to edit/add

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']  # include the fields you want users to submit
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter book title'}),
            'author': forms.Select(),
        }
