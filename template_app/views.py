from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'template_app/index.html')


def second_page(request):
    return render(request, 'template_app/secondPage.html')


def third_page(request):
    return render(request, 'template_app/thirdPage.html')
