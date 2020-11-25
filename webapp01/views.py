from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDolist, Item


def index(response, id):
    ls = ToDolist.objects.get(id=id)
    return render(response, "webapp01/list.html", {"ls":ls})


def home(response):
    return render(response, "webapp01/home.html", {"name": "test"})
