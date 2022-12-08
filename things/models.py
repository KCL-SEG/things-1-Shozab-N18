from django.db import models
from models import Model
# import django.db.models.Model

# Create your models here
class Things(Model.model):
    name = models.CharField(max_length=10),
    description = models.CharField(max_length=100),
    quantity = models.IntegerField(),