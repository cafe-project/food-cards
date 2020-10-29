import datetime
from datetime import timezone
from enum import Enum

from django.db import models
from rest_framework_simplejwt.state import User

class CategoryTypeEnum(Enum):
    MEAL = 'meal'
    PRODUCT = 'product'
    UNDEFINED = 'undefined'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class Category(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30, choices=CategoryTypeEnum.choices(), default=CategoryTypeEnum.UNDEFINED.name)


class Product(models.Model):
    name = models.CharField(max_length=30)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    calories = models.IntegerField(default=0)
    fats = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    proteins = models.IntegerField(default=0)
    bruto = models.IntegerField(blank=True, null=True)
    neto = models.IntegerField(blank=True, null=True)


class Cook(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)


class Meal(models.Model):
    name = models.CharField(max_length=30)

    products = models.ManyToManyField(Product, related_name='Product', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    notes = models.TextField(default='')
    describe = models.TextField(default='')
    storage = models.TextField(default='')
    serving = models.TextField(default='')
    expiry = models.IntegerField(blank=True, null=True)
    calories = models.IntegerField(blank=True, null=True)
    fats = models.IntegerField(blank=True, null=True)
    carbs = models.IntegerField(blank=True, null=True)
    proteins = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=30, default='')
    card_number = models.CharField(max_length=30, default='')
    bruto = models.IntegerField(blank=True, null=True)
    neto = models.IntegerField(blank=True, null=True)

