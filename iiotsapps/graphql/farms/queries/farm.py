import graphene
from django.contrib.postgres.search import SearchVector


from django.utils.translation import gettext_lazy as _
from graphql import GraphQLError

from ....farms.models import Farm

from ..types import FarmNode


class FarmQuery:
    all_farms = graphene.List(
        FarmNode,
        description=_('List of all farms'),
        search=graphene.String(
            description=_('Search farm by parameters'),
            required=False
        )
    )
    farm = graphene.Field(
        FarmNode,
        description=_('get farm by name, id or slug'),
        id=graphene.ID(description=_('ID of farm'), required=False),
        name=graphene.String(description=_('name of farm'), required=False),
        slug=graphene.String(description=_('slug of farm'), required=False),
    )

    def resolve_all_farms(self, info, **kwargs):
        if kwargs.get('search', None):
            return Farm.objects.annotate(
                search=SearchVector('id', 'name', 'slug')
            ).filter(search=kwargs['search'])
        return Farm.objects.all()

    def resolve_farm(self, info, **kwargs):
        if not kwargs:
            error_message = 'You must query a particular farm by either id, slug or name'
            raise GraphQLError(_(error_message))
        else:
            try:
                return Farm.objects.filter(**kwargs).first()
            except Farm.DoesNotExist:
                return None
