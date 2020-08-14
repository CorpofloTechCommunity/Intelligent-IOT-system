import graphene

from django.utils.translation import gettext_lazy as _


class BaseFarmInput(graphene.InputObjectType):
    name = graphene.String(description=_('Name of the farm'))
    slug = graphene.String(description=_('Slug identifier for farm'))
    ph = graphene.Decimal(description=_('pH of farm soil'))
    speed = graphene.Int(description=_('Wind speed of farm'))
    temperature = graphene.Decimal(description=_('Temperature of farm'))
    humidity = graphene.Int(description=_('Humidity of farm environment'))
    pressure = graphene.Int(description=_('Pressure of soil'))
    soil_content = graphene.Int(description=_('Soil water content'))


class EditFarmInput(graphene.InputObjectType):
    id = graphene.ID(
        description=_('ID for farm to b modified'),
        required=True
    )
    slug = graphene.String(
        description=_('slug for farm to be modified'),
        required=True
    )
    patch = graphene.InputField(
        BaseFarmInput,
        description=_('Fields to edit'),
    )
