from django.shortcuts import render
import brainiac.models.bubble_sort as sorter
import ast


def index(request):
    return render(request, 'index.html')


def bubble_sort(request):
    return render(request, 'bubble_sort.html')


def bubble_submit(request):
    try:
        given_answer = ast.literal_eval(request.POST.get('bubble_sort_answer'))
    except:
        given_answer = request.POST.get('bubble_sort_answer')
    bubble_sort = sorter.BubbleSort()
    valid = bubble_sort.compare([4, 1, 3, 2], given_answer)
    if not valid:
        actual = bubble_sort.sort_steps([4, 1, 3, 2])
    return render(request, 'bubble_sort.html', locals())
