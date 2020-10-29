from django.contrib.auth.models import User
from repository.models import Meal
from repository.models import Product
from rest_framework.serializers import ModelSerializer
from repository.models import Category
from rest_framework import serializers


class ProductSerializer(ModelSerializer):
    # category = CategorySerializer(read_only=True)
    name = serializers.CharField(max_length=30)

    class Meta:
        model = Product
        fields = ('__all__')


class MealSerializer(ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    # category = CategorySerializer(read_only=True)
    name = serializers.CharField(max_length=30)
    class Meta:
        model = Meal
        fields = ('__all__')

class CategorySerializer(ModelSerializer):
    product_set = ProductSerializer(many=True, read_only=True)
    meal_set = MealSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'type', 'product_set', 'meal_set')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
