from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello Chano!")

def brian(request):
    return HttpResponse("Hello Brian!")