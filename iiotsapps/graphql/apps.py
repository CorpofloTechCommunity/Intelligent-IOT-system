from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GraphQLConfig(AppConfig):
    name = 'iiotsapps.graphql'
    label = 'iiots_graphql'
    verbose_name = _('IIOTS GraphQL')
    models_module = None
