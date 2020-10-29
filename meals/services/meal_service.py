from typing import Dict, Any

from django.utils.functional import SimpleLazyObject
from meals.services.product_service import ProductService
from repository.models import Meal
from repository.repository import Repository
from repository.serializers import MealSerializer
from meals.services.category_service import CategoryService
from repository.models import CategoryTypeEnum
from repository.models import Category
from repository.serializers import CategorySerializer
from rest_framework.exceptions import PermissionDenied


class MealService:

    def __init__(self):
        self.repository = Repository(Meal)

    def meal_list(self):
        category = list(Category.objects.filter(type=CategoryTypeEnum.MEAL.name).prefetch_related('meal_set').all())
        return CategorySerializer(category, many=True).data

    def create_meal(self, parameters: Dict[str, Any], user=None):
        meal_parameters = {
            'category_id': parameters['category'],
            'name': parameters['name'],
            'owner': user if not type(user) == SimpleLazyObject else None
        }

        CategoryService().validate(parameters['category'], CategoryTypeEnum.MEAL)

        meal = self.repository.create(meal_parameters)

        product_service = ProductService()
        for product_id in parameters.get('product_ids', []):
            meal.products.add(product_service.get_product_instance({'id': product_id}))

        for product in parameters.get('products', []):
            meal.products.add(product_service.create_product(product))
        self._calcutate(meal)

        return meal

    def delete_meal(self, parameters: Dict[str, Any], user):
        if not user.is_superuser and not user.id == self.get_meal(parameters).id:
            raise PermissionDenied('User does not have permission')
        self.repository.delete_multiple(parameters.get('id'))

    def update_meal(self, parameters: Dict[str, Any]):
        meal_id = parameters.pop('id')
        product_ids = parameters.pop('product_ids', [])
        self.repository.update(meal_id, parameters)
        meal = self.get_meal({'id': meal_id})
        product_service = ProductService()
        meal.products.clear()
        for product_id in product_ids or []:
            meal.products.add(product_service.get_product_instance({'id': product_id}))
        if product_ids:
            self._calcutate(meal)

    def read_meal(self, parameters: Dict[str, Any]):
        instance = self.repository.get(parameters, ['products'])
        return MealSerializer(instance).data

    def get_meal(self, parameters: Dict[str, Any]):
        instance = self.repository.get(parameters, ['products'])
        return instance

    @classmethod
    def _calcutate(cls, meal):
        meal.calories = 0
        meal.fats = 0
        meal.carbs = 0
        meal.proteins = 0
        meal.bruto = 0
        meal.neto = 0
        for product in meal.products.all():
            meal.calories += product.calories
            meal.fats += product.fats
            meal.carbs += product.carbs
            meal.proteins += product.proteins
            meal.bruto += product.bruto
            meal.neto += product.neto
        meal.save()

