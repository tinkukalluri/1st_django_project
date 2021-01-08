from django.shortcuts import render
from django.http import HttpResponse
import hello

# Create your views here.
def index(request):
   return render(request, "hello/index.html")
def tinku(request):
    return HttpResponse("tinku")
def greet(request,name):
    return HttpResponse(f"hello, {name.capitalize()}")