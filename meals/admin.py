from django.contrib import admin

from repository.models import Category, Meal, Product

admin.site.register(Category)
admin.site.register(Meal)
admin.site.register(Product)
