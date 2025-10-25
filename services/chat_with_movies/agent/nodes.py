"""Node for Movie Agent."""
from langgraph.prebuilt import ToolNode
from services.chat_with_movies.agent.state import GraphAgentState

tool_node = ToolNode()

async def agent_node(state: GraphAgentState):
    """Node for Movie Agent."""
    
    return state