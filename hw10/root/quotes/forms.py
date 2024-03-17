from django.forms import ModelForm, CharField, DateField, TextInput, DateInput, Textarea
from .models import Author, Quote


class AuthorForm(ModelForm):
    fullname = CharField(max_length=50, widget=TextInput(attrs={"class": "form-control", "id": "fullname"}))
    born_date = CharField(max_length=50, widget=TextInput(attrs={"class": "form-control", "id": "born_date"}))
    born_location = CharField(max_length=150, widget=TextInput(attrs={"class": "form-control", "id": "born_location"}))
    description = CharField(widget=Textarea(attrs={"class": "form-control", "id": "description"}))

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(ModelForm):
    quote = CharField(max_length=50, widget=TextInput(attrs={"class": "form-control", "id": "quote"}))
    tags = CharField(max_length=50, widget=TextInput(attrs={"class": "form-control", "id": "tags"}))
    author = CharField(max_length=150, widget=TextInput(attrs={"class": "form-control", "id": "author"}))

    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author']
