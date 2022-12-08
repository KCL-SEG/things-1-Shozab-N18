from django.db import models
# from models import Model
# import django.db.models.Model

# Create your models here
class Things(models.Model):
    name = models.CharField(max_length=30,unique=True),
    description = models.CharField(max_length=120,unique=False),
    quantity = models.IntegerField(unique=False,
        validators=[
            min(1), 
            max(100)
            ]),