from typing import Dict, Any
from repository.models import Product
from repository.repository import Repository
from meals.services.category_service import CategoryService
from repository.serializers import ProductSerializer
from repository.models import CategoryTypeEnum

from repository.models import Category

from repository.serializers import CategorySerializer


class ProductService:

    def __init__(self):
        self.repository = Repository(Product)

        self.category_repository = Repository(Category)

    def product_list(self):
        category = list(Category.objects.filter(type=CategoryTypeEnum.PRODUCT.name).prefetch_related('product_set').all())
        return CategorySerializer(category, many=True).data

    def create_product(self, parameters: Dict[str, Any]):
        CategoryService().validate(parameters['category'], CategoryTypeEnum.PRODUCT)

        parameters['category'] = CategoryService().get_category({'id': parameters['category']})
        return self.repository.create(parameters)

    def delete_product(self, parameters: Dict[str, Any]):
        self.repository.delete_multiple(parameters.get('id'))

    def update_product(self, parameters: Dict[str, Any]):
        self.get_product_instance(parameters)
        product_id = parameters.pop('id')
        self.repository.update(product_id, parameters)

    def get_product(self, parameters: Dict[str, Any]):
        instance = self.repository.get(parameters, [])
        return ProductSerializer(instance).data

    def get_product_instance(self, parameters: Dict[str, Any]):
        return self.repository.get(parameters, [])
