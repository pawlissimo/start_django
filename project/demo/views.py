from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<p>index view</p>')

def upload(request):
    return HttpResponse('<p>upload view</p>')

def cleanup(request):
    return HttpResponse('<p>cleanup view</p>')
