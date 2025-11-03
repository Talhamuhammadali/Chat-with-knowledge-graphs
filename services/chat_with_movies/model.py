"""Schema for Knowledge Graph for movies data."""

from neomodel import (
    AsyncRelationshipFrom,
    AsyncRelationshipTo,
    AsyncStructuredNode,
    IntegerProperty,
    StringProperty,
)


class Movie(AsyncStructuredNode):
    """Node representing a movie in the knowledge graph.

    Description:
        Represents a film with its associated metadata and relationships to people
        involved in its production.

    Attributes
    ----------
        title (str): The title of the movie.
        released (int): The year the movie was released.
        tagline (str): The tagline of the movie.
    Relationships:
        acted_in -> Movie via "ACTED_IN"
            Actors who performed in the movie.
        directed -> Movie via "DIRECTED"
            Directors who directed the movie.
        produced -> Movie via "PRODUCED"
            Producers who produced the movie.
    """

    title = StringProperty(unique_index=True, required=True)
    released = IntegerProperty()
    tagline = StringProperty()

    actors = AsyncRelationshipFrom("Person", "ACTED_IN")
    directors = AsyncRelationshipFrom("Person", "DIRECTED")
    producers = AsyncRelationshipFrom("Person", "PRODUCED")


class Person(AsyncStructuredNode):
    """Node representing a person in the knowledge graph.

    Description:
        Represents individuals involved in movie production including actors,
        directors, producers, writers, and reviewers.

    Attributes
    ----------
        name (str) [unique, required, indexed]: Full name of the person
            - Format: "FirstName LastName" or single name
            - Example: "Tom Hanks", "Keanu Reeves"

        born (int) [optional]: Birth year of the person
            - Format: Four-digit year (YYYY)
            - Example: 1956, 1964
            - Valid range: 1800-present

    Relationships:
        acted_in -> Movie via "ACTED_IN":
            Movies in which this person performed as an actor
            Direction: outgoing

        directed -> Movie via "DIRECTED":
            Movies this person directed
            Direction: outgoing

        produced -> Movie via "PRODUCED":
            Movies this person produced
            Direction: outgoing

        wrote -> Movie via "WROTE":
            Movies this person wrote/co-wrote
            Direction: outgoing

        reviewed -> Movie via "REVIEWED":
            Movies this person reviewed
            Direction: outgoing

        follows -> Person via "FOLLOWS":
            Other people this person follows
            Direction: outgoing
    """

    name = StringProperty(unique_index=True, required=True)
    born = IntegerProperty()

    acted_in = AsyncRelationshipTo("Movie", "ACTED_IN")
    directed = AsyncRelationshipTo("Movie", "DIRECTED")
    produced = AsyncRelationshipTo("Movie", "PRODUCED")
    wrote = AsyncRelationshipTo("Movie", "WROTE")
    reviewed = AsyncRelationshipTo("Movie", "REVIEWED")
    follows = AsyncRelationshipTo("Person", "FOLLOWS")
