from django.db import models


class CustomModelManager(models.Manager):
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})
