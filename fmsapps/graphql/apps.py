from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GraphQLConfig(AppConfig):
    name = 'fmsapps.graphql'
    label = 'fms_graphql'
    verbose_name = _('FMS GraphQL')
    models_module = None
