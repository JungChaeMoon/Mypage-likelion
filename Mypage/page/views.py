from django.shortcuts import render

# Create your views here.


def service(request , *args, **kwargs):
    return render(request, 'page/service.html')


def introduce(request, *args, **kwargs):

    return render(request, 'page/introduce.html')