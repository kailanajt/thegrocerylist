from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
  name = models.CharField(max_length=100)
  sort = models.CharField(max_length=100)
  brand = models.CharField(max_length=100)
  store = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse('items_detail', kwargs={"item_id": self.id})
  