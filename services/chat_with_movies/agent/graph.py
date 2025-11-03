"""Main graph agent logic."""

from langgraph.graph import END, StateGraph

from services.chat_with_movies.agent.nodes import agent_node, human_node, temp_node
from services.chat_with_movies.agent.state import GraphAgentState
from services.chat_with_movies.agent.tools import TOOL_NODE

AGENT_WORKFLOW = StateGraph(GraphAgentState)
AGENT_WORKFLOW.add_node("agent", agent_node)
AGENT_WORKFLOW.add_node("tool", TOOL_NODE)
AGENT_WORKFLOW.add_node("ask_human", human_node)

AGENT_WORKFLOW.add_conditional_edges(
    "assistent",
    temp_node,
    {
        "tool": "tool",
        "human": "ask_human",
        "finish": END,
    },
)
