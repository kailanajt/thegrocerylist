from django.shortcuts import render
from .models import Item



# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def items_index(request):
  items = Item.objects.all()
  return render(request, 'items/index.html', {'items': items})