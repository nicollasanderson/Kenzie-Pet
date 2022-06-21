from tokenize import group
from django.db import models

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.FloatField()
    weight = models.FloatField()
    sex = models.CharField(max_length=15)
    group = models.ForeignKey("groups.Group", on_delete=models.CASCADE, related_name="group",null=True)
    characteristics = models.ManyToManyField("characteristics.Characteristic", related_name="animal")