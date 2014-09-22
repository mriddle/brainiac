from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def bubble_sort(request):
    return render(request, 'bubble_sort.html')
