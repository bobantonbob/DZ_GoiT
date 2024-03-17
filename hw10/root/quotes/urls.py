from django.urls import path

from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='home'),  # quotes:home
    path('<int:page>', views.main, name='home_paginate'),
    path('authors', views.authors, name='authors'),
    path('authors/page/<int:page>/', views.authors, name='authors_paginated'),
    path('add_quote', views.add_quote, name='add_quote'),
    path('add_author', views.add_author, name='add_author'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail')
]
