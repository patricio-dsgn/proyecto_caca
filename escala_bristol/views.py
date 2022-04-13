from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request,'escala_bristol/index.html')

def history(request):
    return render(request,'escala_bristol/history.html')


def uses(request):
    return render(request,'escala_bristol/uses.html')


def scale(request):
    return render(request,'escala_bristol/scale.html')

def scale2(request):
    return render(request,'escala_bristol/doxa.html')


def interpretation(request):
    return render(request,'escala_bristol/interpretation.html')

