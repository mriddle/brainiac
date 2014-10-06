from django.shortcuts import render
import brainiac.models.bubble_sort as sorter


def index(request):
    return render(request, 'index.html')


def bubble_sort(request):
    return render(request, 'bubble_sort.html')


def bubble_submit(request):
    given_answer = request.POST.get('bubble_sort_answer')
    given_problem = [4, 1, 3, 2]
    bubble_sort = sorter.BubbleSort()
    valid = bubble_sort.compare(given_problem, given_answer)
    actual = None
    if not valid:
        actual = bubble_sort.sort_steps(given_problem)
    return render(request, 'bubble_sort.html', locals())
