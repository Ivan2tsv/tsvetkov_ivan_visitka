from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        'title': 'Цветков Визитка'
    }
    return render(request, 'main/index.html', data)



