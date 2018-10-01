import graphene

import links.schema
import users.schema


# This query inherits queries from apps
# This way you are able to keep every part of the schema isolated in apps
class Query(users.schema.Query, links.schema.Query, graphene.ObjectType):
    pass


# This Mutation inherits queries from apps
class Mutation(users.schema.Mutation, links.schema.Mutation,
               graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
