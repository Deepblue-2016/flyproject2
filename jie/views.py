from django.shortcuts import render


# Create your views here.
def jindex(request):
    return render(request, 'html/jie/index.html')


def add(request):
    return render(request, 'html/jie/add.html')


def detail(request):
    return render(request, 'html/jie/detail.html')
