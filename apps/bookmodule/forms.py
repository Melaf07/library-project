
# forms.py
from django import forms
from django.db import models
from .models import Book , Student, Address,Student3,Address2 ,Author

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

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']

    name = forms.CharField(
        max_length=100,
        required=True,
        label="Name",
        widget=forms.TextInput(attrs={
            'placeholder': '',
            'class': "mycssclass",
            'id': 'jsID'
        })
    )
    age = forms.IntegerField(
        required=True,
        label="Age",
        initial=0
    )
    address = forms.ModelChoiceField(
        queryset=Address.objects.all(),
        empty_label="choose city",  
        widget=forms.Select(attrs={'class': 'form-control'})  
    ) 


class StudentForm2(forms.ModelForm):
    class Meta:
        model = Student3
        fields = ['name', 'age', 'address']

    name = forms.CharField(
        max_length=100,
        required=True,
        label="Name",
        widget=forms.TextInput(attrs={
            'placeholder': '',
            'class': "mycssclass",
            'id': 'jsID'
        })
    )
    age = forms.IntegerField(
        required=True,
        label="Age",
        initial=0
    )
    address = forms.ModelMultipleChoiceField(
        queryset=Address2.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False  
    )


from django import forms
from apps.bookmodule.models import Book2, Author

GENRE = ( ("fiction","Fiction"), ("mystrery","Mystrery"), ("fantasy","Fantasy"), ("biography","Biography") )

class BookForm2(forms.ModelForm):
    class Meta:
        model = Book2
        fields= ['title', 'price', "genre", "authors", "coverPage"]
        
    title = forms.CharField(label="Title", required=True)
    price = forms.FloatField(label="Price (with decimal point))", 
        required=True, initial=0.00)
    genre = forms.ChoiceField(label="Genre", choices=GENRE, 
        widget=forms.RadioSelect())
    
    authors = forms.CharField(label="auther", required=True)

