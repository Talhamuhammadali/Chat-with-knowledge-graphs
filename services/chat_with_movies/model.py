"""Schema for Knowledge Graph for movies data."""
from neomodel import (
    StructuredNode,
    StringProperty,
    IntegerProperty,
    RelationshipTo,
    RelationshipFrom,
)

class Movie(StructuredNode):
    title = StringProperty(unique_index=True, required=True)
    released = IntegerProperty()
    tagline = StringProperty()
    
    actors = RelationshipFrom('Person', 'ACTED_IN')
    directors = RelationshipFrom('Person', 'DIRECTED')
    producers = RelationshipFrom('Person', 'PRODUCED')


class Person(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    born = IntegerProperty()
    
    acted_in = RelationshipTo('Movie', 'ACTED_IN')
    directed = RelationshipTo('Movie', 'DIRECTED')
    produced = RelationshipTo('Movie', 'PRODUCED')
    wrote = RelationshipTo('Movie', 'WROTE')
    Reviewed = RelationshipTo('Movie', 'REVIEWED')
    FOLLOWS = RelationshipTo('Person', 'FOLLOWS')