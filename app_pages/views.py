from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello, world. You're at the main page<h1>")


def about(request):
    return HttpResponse("<h1>Hello, world. You're at the about page<h1>")
