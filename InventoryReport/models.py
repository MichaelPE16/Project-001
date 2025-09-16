from django.db import models

# Create your models here.

class Products(models.Model): 
    name = models.CharField(max_length=50)
    picture = models.TextField(max_length=500)
    description = models.TextField(max_length=500)

class Clients(models.Model): 
    Factory_name = models.CharField(max_length=55)
    