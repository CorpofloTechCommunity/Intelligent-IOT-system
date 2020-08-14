import graphene

from ..payloads.farm import (
    CreateFarmPayload,
    EditFarmPayload,
    DeleteFarmPayload
)


class FarmMutation(graphene.ObjectType):
    create_farm = CreateFarmPayload.Field()
    edit_farm = EditFarmPayload.Field()
    delete_farm = DeleteFarmPayload.Field()
