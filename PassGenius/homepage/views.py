from django.shortcuts import render


def index(request):
    return render(request, template_name='homepage/index.html')


def about(request):
    return render(request, template_name='homepage/about.html')
