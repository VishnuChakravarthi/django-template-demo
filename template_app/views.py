from django.shortcuts import render

# Create your views here.


def index(request):
    context_dict = {'text': "Hello World"}
    return render(request, 'template_app/index.html', context=context_dict)


def second_page(request):
    return render(request, 'template_app/secondPage.html')


def third_page(request):
    return render(request, 'template_app/thirdPage.html')
