from graphene_django.types import DjangoObjectType

from ....farms.models import Farm


class FarmType(DjangoObjectType):
    class Meta:
        model = Farm
