"""Node for Movie Agent."""

from langchain.messages import HumanMessage
from langgraph.prebuilt import interrupt
from langgraph.runtime import Runtime

from services.chat_with_movies.agent.state import GraphAgentState


async def temp_node():
    """Temporary placeholder node for agent workflow."""
    pass


async def agent_node(state: GraphAgentState, runtime: Runtime):
    """Node for Movie Agent."""
    return state


async def human_node(state: GraphAgentState, runtime: Runtime):
    """Node to handle human input."""
    message = interrupt("Please provide input for the agent:")
    message = HumanMessage(content=message)
    return {"messages": [message]}
