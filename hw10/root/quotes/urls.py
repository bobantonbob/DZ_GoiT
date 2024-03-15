from django.urls import path

from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='home'),  # quotes:home
    path('<int:page>', views.main, name='home_paginate'),
]
