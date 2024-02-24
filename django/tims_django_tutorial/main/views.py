from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>Hello world</h1>")

def view_1(response):
    return HttpResponse("<h1>view_1</h1>")

def view_2(response):
    return HttpResponse("<h1>view_2</h1>")