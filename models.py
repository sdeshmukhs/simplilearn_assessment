from django.db import models

# Create your models here.

class Userinfo(models.Model):
    Name = models.CharField(max_length =100, unique = True)
    email = models.EmailField(max_length=254)
    Address = models.CharField(max_length=200)