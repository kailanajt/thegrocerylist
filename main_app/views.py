from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  return HttpResponse('<h1>Grocery List</h1>')

def about(request):
  return render(request, 'about.html')