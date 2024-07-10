from django.http import HttpResponse
from django.shortcuts import render

def index(reqest):
    context = {
        'title': 'Home',
        'content': 'Магазин - HOME',
    }
    return render(reqest, 'main/index.html', context)

def about(reqest):
    context = {
        'title': 'ABOUT',
        'content': "О нас",
        'text_on_page': 'Почему магазин хороший'
    }
    return render(reqest, 'main/about.html', context)

