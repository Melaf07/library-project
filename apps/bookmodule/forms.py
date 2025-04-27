from django import forms
from django.db import models
from .models import Book

# forms.py
from django import forms
from django.db import models
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'edition', 'author']

    title = forms.CharField(
        max_length=100,
        required=True,
        label="Title",
        widget=forms.TextInput(attrs={
            'placeholder': '',
            'class': "mycssclass",
            'id': 'jsID'
        })
    )
    price = forms.DecimalField(
        required=True,
        label="Price",
        initial=0
    )
    edition = forms.IntegerField(
        required=True,
        initial=0,
        widget=forms.NumberInput()
    )
