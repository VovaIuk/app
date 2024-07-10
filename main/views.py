from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
        'content': 'Магазин - HOME',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'ABOUT',
        'content': "О нас",
        'text_on_page': 'Почему магазин хороший'
    }
    return render(request, 'main/about.html', context)

