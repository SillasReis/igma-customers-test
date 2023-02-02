from uuid import uuid1

from django.db import models


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid1, editable=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False, unique=True)
    birth_date = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.name
