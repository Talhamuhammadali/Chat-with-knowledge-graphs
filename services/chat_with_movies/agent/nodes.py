"""Node for Movie Agent."""
from services.chat_with_movies.agent.state import GraphAgentState

async def agent_node(state: GraphAgentState):
    """Node for Movie Agent."""
    
    return state