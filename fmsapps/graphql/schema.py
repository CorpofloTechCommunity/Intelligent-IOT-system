import graphene
import graphql_jwt

from .farms.schemas import FarmQueries, FarmMutations

class Query(FarmQueries, graphene.ObjectType):
    pass


class Mutation(FarmMutations, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
