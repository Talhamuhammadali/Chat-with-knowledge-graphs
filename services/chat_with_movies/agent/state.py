"""State of the graph agent."""
from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class GraphAgentState(TypedDict):
    """State of the graph agent."""
    message: str
    messages: Annotated[Sequence[BaseMessage], "List of messages exchanged so far."]
    