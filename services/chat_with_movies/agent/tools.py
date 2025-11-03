"""Tools used by the Movie Agent."""

from langchain.messages import ToolMessage
from langchain.tools import ToolRuntime, tool
from langgraph.prebuilt import ToolNode
from langgraph.types import Command


@tool(name_or_callable="todos", parse_docstring=True)
def todos(todo_writes: list[dict[str, str]], tool_runtime: ToolRuntime) -> Command:
    """Manage a todo list."""
    return Command(
        update={
            "messages": [
                ToolMessage(f"Todo list updated with {len(todo_writes)} items.", tool_call_id=tool_runtime.tool_call_id)
            ]
        }
    )


@tool(name_or_callable="QueryKG", parse_docstring=True)
def query_kg(query: str, tool_runtime: ToolRuntime) -> Command:
    """Query the knowledge graph with a Cypher query.

    Arguments:
    ----
        query (str): The Cypher query string to execute against the knowledge graph.
    """
    # Placeholder implementation
    result = f"Executed query: {query}"
    return Command(update={"messages": [ToolMessage(result, tool_call_id=tool_runtime.tool_call_id)]})


Tools = [todos, query_kg]
TOOL_NODE = ToolNode(tools=Tools)
