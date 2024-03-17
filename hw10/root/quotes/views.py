from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import AuthorForm, QuoteForm
from .models import Author
from .models import Quote  # Підключаємо модель для роботи з базою даних SQLite


def main(request, page=1):
    quotes = Quote.objects.all().order_by('-created_at')  # Отримуємо всі цитати з бази даних SQLite
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


def add_author(request):
    form = AuthorForm(instance=Author())
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES, instance=Author())
        if form.is_valid():
            form.save()
            return redirect(to='quotes:home')
    return render(request, 'quotes/add_author.html',
                  context={'title': 'Add Author', 'page': 'add_author', "form": form})


def author_detail(request, author_id):
    author = Author.objects.get(pk=author_id)
    return render(request, 'quotes/author_detail.html', {'author': author})







def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            # Отримайте об'єкт автора з форми
            author = form.cleaned_data['author']

            # Збережіть цитату з правильним автором
            quote = form.save(commit=False)
            quote.author = author
            quote.save()

            # Отримайте вибрані теги з форми
            tags = form.cleaned_data['tags']
            quote.tags.set(tags)  # Встановіть вибрані теги для цитати

            return redirect('/')  # або інша сторінка, куди ви хочете перейти після успішного додавання цитати
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})





# def add_quote(request):
#     form = QuoteForm(instance=Author())
#     if request.method == 'POST':
#         form = QuoteForm(request.POST, request.FILES, instance=Quote())
#         if form.is_valid():
#             form.save()
#             return redirect(to='quotes:home')
#     return render(request, 'quotes/add_quote.html', context={'title': 'Add Quote', 'page': 'add_quote', "form": form})
