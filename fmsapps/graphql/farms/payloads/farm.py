import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation

from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from ....farms.forms.farm import NewFarmForm
from ....farms.models import Farm

from ...utils import DictifyNestedInput as DictifyInput

from ..inputs.farm import EditFarmInput
from ..types import FarmNode


class CreateFarmPayload(DjangoModelFormMutation):
    """Create new farm type"""

    class Meta:
        form_class = NewFarmForm


class EditFarmPayload(graphene.Mutation):
    """edit exiting farm"""
    farm = graphene.Field(FarmNode, description=_('Updated farm'))
    is_modified = graphene.Boolean(description=_('confirm if edited'))

    class Arguments:
        input = EditFarmInput(
            description=_('existing farm type to be modified'),
            required=True
        )

    def mutate(self, info, input):
        dictifier = DictifyInput(input)
        serialize_patch = dictifier.get_fields_or_field('patch')
        if 'slug' in serialize_patch:
            serialize_patch.update({'slug': slugify(serialize_patch['slug'])})
        get_farm = get_object_or_404(
            Farm,
            id=input.id,
            slug__iexact=input.slug
        )
        edited_farm = Farm(**serialize_patch)
        edited_farm.save()
        return EditFarmPayload(farm=get_farm, is_modified=True)


class DeleteFarmPayload(graphene.Mutation):
    """Remove a farm by ID and slug"""
    all_farms = graphene.List(FarmNode, description=_('list of remaining farms'))
    is_deleted = graphene.Boolean(description=_('confirm if action was successful'))

    class Arguments:
        id = graphene.ID(description=_('ID of farm to be deleted'), required=True)
        slug = graphene.String(description=_('slug of farm to be deleted'), required=True)

    def mutate(self, info, id, slug):
        get_farm = get_object_or_404(Farm, id=id, slug__iexact=slug)
        get_farm.delete()
        return DeleteFarmPayload(all_farms=Farm.objects.all(), is_deleted=True)
