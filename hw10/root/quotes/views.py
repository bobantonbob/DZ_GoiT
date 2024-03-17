from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import AuthorForm, QuoteForm
from .models import Author
from .models import Quote  # Підключаємо модель для роботи з базою даних SQLite


def main(request, page=1):
    quotes = Quote.objects.all()  # Отримуємо всі цитати з бази даних SQLite
    per_page = 15
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'title': 'Home', 'quotes': quotes_on_page})


def authors(request, page=1):
    autors = Author.objects.all()  # Отримуємо всіх Автори з бази даних SQLite
    per_page = 24
    paginator = Paginator(autors, per_page)
    authors_on_page = paginator.page(page)
    return render(request, 'quotes/authors.html',
                  context={'title': 'Autors', 'page': 'autors', 'authors': authors_on_page})


def add_quote(request):
    form = QuoteForm(instance=Author())
    if request.method == 'POST':
        form = QuoteForm(request.POST, request.FILES, instance=Quote())
        if form.is_valid():
            form.save()
            return redirect(to='quotes:home')
    return render(request, 'quotes/add_quote.html', context={'title': 'Add Quote', 'page': 'add_quote', "form": form})




def author_detail(request, author_id):
    author = Author.objects.get(pk=author_id)
    return render(request, 'quotes/author_detail.html', {'author': author})














def add_author(request):
    form = AuthorForm(instance=Author())
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES, instance=Author())
        if form.is_valid():
            form.save()
            return redirect(to='quotes:home')
    return render(request, 'quotes/add_author.html',
                  context={'title': 'Add Author', 'page': 'add_author', "form": form})

    # from django.shortcuts import render
    # from django.core.paginator import Paginator
    #
    # from .utils import get_mongodb
    #
    #
    # def main(request, page=1):
    #     db = get_mongodb()
    #     quotes = db.quotes.find()
    #     per_page = 10
    #     paginator = Paginator(list(quotes), per_page)
    #     quotes_on_page = paginator.page(page)
    #     return render(request, 'quotes/about_author.html', context={'quotes': quotes_on_page})
