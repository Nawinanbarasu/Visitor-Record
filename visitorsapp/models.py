from django.db import models

class Visitor(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
