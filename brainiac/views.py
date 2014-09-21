from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def sorts(request):
    return render(request, 'sorts.html')
