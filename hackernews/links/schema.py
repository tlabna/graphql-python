import graphene
from graphene_django import DjangoObjectType

from .models import Link, Vote

from users.schema import UserType

from graphql import GraphQLError

from django.db.models import Q


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class VoteType(DjangoObjectType):
    class Meta:
        model = Vote


class Query(graphene.ObjectType):
    links = graphene.List(
        LinkType,
        search=graphene.String(),
        first=graphene.Int(),
        skip=graphene.Int(),
    )
    votes = graphene.List(VoteType)

    def resolve_links(self, info, search=None, first=None, skip=None,
                      **kwargs):
        query_search = Link.objects.all()

        if search:
            filter = (
                Q(url__icontains=search) |
                Q(description__icontains=search)
            )

            return query_search.filter(filter)

        if skip:
            query_search = query_search[skip::]

        if first:
            query_search = query_search[:first]

        return query_search

    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()


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


class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    link = graphene.Field(LinkType)

    class Arguments:
        link_id = graphene.Int()

    def mutate(self, info, link_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('You must be logged in to vote!')

        link = Link.objects.filter(id=link_id).first()
        if not link:
            raise Exception('Invalid Link!')

        Vote.objects.create(user=user, link=link)

        return CreateVote(user=user, link=link)


# Creates a mutation class with a field to be resolved, which points to our mutation defined before
class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
    create_vote = CreateVote.Field()
