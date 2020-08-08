import graphene

from django.utils.translation import gettext_lazy as _


class BaseFarmInput(graphene.InputObjectType):
    name = graphene.String(description=_('Name of the farm'))
    slug = graphene.String(description=_('slug identifier for farm'))
    ph = graphene.Int(description=_('pH of farm soil'))
    speed = graphene.Int(description=_('pH of farm soil'))
    temperature = graphene.Int(description=_('temperature of farm'))
    humidity = graphene.Int(description=_('humidity of farm environment'))
    pressure = graphene.Int(description=_('pressure of soil'))
    soil_content = graphene.Int(description=_('soil water content'))


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
