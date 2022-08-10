from django.db import models
from django.urls import reverse

# Create your models here.
class Item(models.Model):
  name = models.CharField(max_length=100)
  sort = models.CharField(max_length=100)
  brand = models.CharField(max_length=100)
  store = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse('items_detail', kwargs={"item_id": self.id})
  