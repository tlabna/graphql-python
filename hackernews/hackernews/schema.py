import graphene

import links.schema


# This query inherits queries from apps
# This way you are able to keep every part of the schema isolated in apps
class Query(links.schema.Query, graphene.ObjectType):
    pass


# This Mutation inherits queries from apps
class Mutation(links.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
