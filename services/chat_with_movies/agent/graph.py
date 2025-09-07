"""Main graph agent logic."""

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.memory import InMemoryStore
from services.chat_with_movies.agent.state import GraphAgentState

def temp_node():
    pass

AGENT_WORKFLOW = StateGraph(GraphAgentState)
AGENT_WORKFLOW.add_node("assistent", temp_node)
AGENT_WORKFLOW.add_node("tool", temp_node)
AGENT_WORKFLOW.add_node("ask_human", temp_node)


AGENT_WORKFLOW.add_conditional_edges(
    "assistent",
    temp_node,
    {
        "tool": "tool",
        "human": "ask_human",
        "finish": END,
    },    
)
