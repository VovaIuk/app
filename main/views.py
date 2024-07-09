from django.http import HttpResponse
from django.shortcuts import render

def index(reqest):
    context = {
        'name': 'Vova',
        'title': 'Main',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'bool': True,
        }
    return render(reqest, 'main/index.html')

def about(reqest):
    return HttpResponse('About page')

