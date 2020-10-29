from typing import Any, Dict

from django.contrib.auth.models import User

from repository.repository import Repository
from repository.serializers import UserSerializer


class UserService:

    def __init__(self):
        self.repository = Repository(User)

    def user_list(self, parameters: Dict[str, Any]):
        users = self.repository.list(parameters, [])
        return UserSerializer(users, many=True).data

    def delete_user(self, parameters: Dict[str, Any]):
        user_id = parameters.pop('id')
        self.repository.delete(user_id)

    def update_user(self, parameters: Dict[str, Any]):
        user_id = parameters.pop('id')
        self.repository.update(user_id, parameters)

    def read_user(self, parameters: Dict[str, Any]):
        user_id = parameters.pop('id')
        return self.repository.read({'id': user_id})

    def get_user(self, parameters: Dict[str, Any]):
        user_id = parameters.pop('id')
        return self.repository.get({'id': user_id}, [])
