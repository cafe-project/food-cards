from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict

class Repository:
    def __init__(self, model):
        self.model = model

    def list(self, parameters, prefetch):
        return list(self.model.objects.prefetch_related(*prefetch).filter(**parameters))

    def create(self, parameters):
        return self.model.objects.create(**parameters)

    def delete(self, object_id):
        self.model.objects.filter(id=object_id).delete()

    def delete_multiple(self, object_id):
        self.model.objects.filter(id__in=object_id).delete()

    def update(self, object_id, parameters):
        self.model.objects.filter(id=object_id).update(**parameters)

    def read(self, parameters):
        try:
            return model_to_dict(self.model.objects.get(**parameters))
        except self.model.DoesNotExist as ex:
            raise ObjectDoesNotExist(str(ex))

    def get(self, parameters, prefetch):
        try:
            return self.model.objects.prefetch_related(*prefetch).get(**parameters)
        except self.model.DoesNotExist as ex:
            raise ObjectDoesNotExist(str(ex))
