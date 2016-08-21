from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    response = render(request, 'page/home/home.html')
    return HttpResponse(response)