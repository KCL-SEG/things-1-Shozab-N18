from . import model
from .model import Model
# import django.db.models.Model

# Create your models here
class Things(Model.model):
    name = model.CharField(max_length=30,unique=True),
    description = model.CharField(max_length=120,unique=False),
    quantity = model.IntegerField(unique=False,min=0,max=100),