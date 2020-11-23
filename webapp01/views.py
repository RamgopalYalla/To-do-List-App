from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1> My website page 1</h1>")

def index2(response):
    return HttpResponse("<h1> My website page 2</h1>")
