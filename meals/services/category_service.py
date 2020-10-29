from typing import Dict, Any

from repository.models import Category
from repository.repository import Repository

from repository.serializers import CategorySerializer


class CategoryService:

    def __init__(self):
        self.repository = Repository(Category)

    def category_list(self, parameters: Dict[str, Any], prefetch=[]):

        categories = self.repository.list(parameters, prefetch)
        return CategorySerializer(categories, many=True).data

    def create_category(self, parameters: Dict[str, Any]):
        self.repository.create(parameters)

    def delete_category(self, parameters: Dict[str, Any]):
        category_id = parameters.pop('id')
        self.repository.delete(category_id)

    def update_category(self, parameters: Dict[str, Any]):
        category_id = parameters.pop('id')
        self.repository.update(category_id, parameters)

    def read_category(self, parameters: Dict[str, Any]):
        category_id = parameters.pop('id')
        return self.repository.read({'id': category_id})

    def get_category(self, parameters: Dict[str, Any]):
        category_id = parameters.pop('id')
        return self.repository.get({'id': category_id}, [])

    def validate(self, id, type):
        category = self.repository.get({'id': id, 'type': type.name}, [])
        assert category, f'Category for {type.name} with id \'{id}\' does not exist.'
