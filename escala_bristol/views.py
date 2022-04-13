from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request,'escala_bristol/index.html')
