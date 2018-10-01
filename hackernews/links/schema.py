import graphene
from graphene_django import DjangoObjectType

from .models import Link

from users.schema import UserType


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
    posted_by = graphene.Field(UserType)

    # Defines the data you can send to the server
    class Arguments:
        url = graphene.String()
        description = graphene.String()

    # The mutation method: it creates a link on the database using the data sent by the user
    # in this case the url and description.
    # After, the server returns the CreateLink class with the data just created.
    def mutate(self, info, url, description):
        user = info.context.user or None

        link = Link(url=url, description=description, posted_by=user)
        link.save()

        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
            posted_by=link.posted_by,
        )


# Creates a mutation class with a field to be resolved, which points to our mutation defined before
class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
