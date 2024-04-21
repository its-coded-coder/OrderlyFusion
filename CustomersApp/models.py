from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    phone = models.TextField(unique=True, max_length=20)
    email = models.EmailField(unique=True)