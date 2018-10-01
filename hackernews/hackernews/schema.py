import graphene
import graphql_jwt

import links.schema
import users.schema


# This query inherits queries from apps
# This way you are able to keep every part of the schema isolated in apps
class Query(users.schema.Query, links.schema.Query, graphene.ObjectType):
    pass


# This Mutation inherits queries from apps
class Mutation(users.schema.Mutation, links.schema.Mutation,
               graphene.ObjectType):
    # used to authenticate the User with its username and password to obtain the JSON Web token
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()

    # to confirm that the token is valid, passing it as an argument in gQL
    verify_token = graphql_jwt.Verify.Field()

    # to obtain a new token within the renewed expiration time for non-expired tokens
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
