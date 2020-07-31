import graphene

from ..queries import FarmQuery


class FarmQueries(FarmQuery):
    pass


class FarmMutations(graphene.ObjectType):
    pass
