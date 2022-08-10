from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Item



# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def items_index(request):
  items = Item.objects.filter(user=request.user)
  return render(request, 'items/index.html', {'items': items})


def items_detail(request, item_id):
  item = Item.objects.get(id=item_id)
  return render(request, 'items/detail.html', {'item': item})

class ItemCreate(LoginRequiredMixin, CreateView):
  model = Item
  fields = ['name', 'sort', 'brand', 'store']
  

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class ItemUpdate(LoginRequiredMixin, UpdateView):
  model = Item
  fields = [ 'sort', 'brand', 'store']


class ItemDelete(LoginRequiredMixin, DeleteView):
  model = Item
  success_url = '/items/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('items_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)