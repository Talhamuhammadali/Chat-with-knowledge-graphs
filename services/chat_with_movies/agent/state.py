"""State of the graph agent."""

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Annotated, TypedDict

from langchain_core.messages import BaseMessage


class GraphAgentState(TypedDict):
    """State of the graph agent."""

    message: str
    messages: Annotated[Sequence[BaseMessage], "List of messages exchanged so far."]


@dataclass
class Context:
    """Context for the graph agent."""

    user_name: str
    favorite_genres: list[str] = []
    favorite_actors: list[str] = []
