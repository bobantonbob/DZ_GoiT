from django import forms
from django.forms import ModelForm, CharField, DateField, TextInput, DateInput, Textarea
from django.db import models  # Імпортуємо ForeignKey з django.db
from .models import Author, Quote, Tag


class AuthorForm(ModelForm):
    fullname = CharField(max_length=50, widget=TextInput(attrs={"class": "form-control", "id": "fullname"}))
    born_date = CharField(max_length=50, widget=TextInput(attrs={"class": "form-control", "id": "born_date"}))
    born_location = CharField(max_length=150, widget=TextInput(attrs={"class": "form-control", "id": "born_location"}))
    description = CharField(widget=Textarea(attrs={"class": "form-control", "id": "description"}))

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(forms.ModelForm):
    quote = forms.CharField(max_length=1200, widget=forms.Textarea(attrs={"class": "form-control", "id": "quote"}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.SelectMultiple(attrs={"class": "form-control", "id": "tags"}))
    author = forms.ModelChoiceField(queryset=Author.objects.all(), widget=forms.Select(attrs={"class": "form-control", "id": "author"}), error_messages={'required': 'Виберіть автора зі списку'})

    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author']


