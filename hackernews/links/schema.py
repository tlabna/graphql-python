import graphene
from graphene_django import DjangoObjectType

from .models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    def resolve_links(self, info, **kwargs):
        return Link.objects.all()


# Defines a mutation class
class CreateLink(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()

    # Defines the data you can send to the server
    class Arguments:
        url = graphene.String()
        description = graphene.String()

    # The mutation method: it creates a link on the database using the data sent by the user
    # in this case the url and description.
    # After, the server returns the CreateLink class with the data just created.
    def mutate(self, info, url, description):
        link = Link(url=url, description=description)
        link.save()

        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
        )


# Creates a mutation class with a field to be resolved, which points to our mutation defined before
class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
