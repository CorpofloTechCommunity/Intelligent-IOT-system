import graphene

from ..queries import FarmQuery
from ..mutations import FarmMutation


class FarmQueries(FarmQuery):
    pass


class FarmMutations(FarmMutation, graphene.ObjectType):
    pass
