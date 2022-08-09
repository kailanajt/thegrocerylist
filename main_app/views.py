from django.shortcuts import render
from django.http import HttpResponse

class Item: 
  def __init__(self, name, sort, brand, store):
    self.name = name
    self.sort = sort
    self.brand = brand
    self.store = store

items = [
  Item('Bread', 'Gluten', 'Honey Wheat', 'Walmart'),
  Item('Eggs', 'Animal Product', 'Great Value', 'Sams Club'),
  Item('Milk', 'Dairy', 'Oaks Farm', 'Walmart'),
  Item('Dog Food', 'Pets', 'Purina Puppy', 'Sams Club')
]

# Create your views here.

def home(request):
  return HttpResponse('<h1>Grocery List</h1>')

def about(request):
  return render(request, 'about.html')

def items_index(request):
  return render(request, 'items/index.html', { 'items': items})