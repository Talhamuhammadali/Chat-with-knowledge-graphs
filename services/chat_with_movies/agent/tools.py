"""Tools used by the Movie Agent."""

from typing import Annotated

from langchain.tools import tool
from langgraph.prebuilt import InjectedState


@tool
def todos(todo_writes: list[dict[str, str]], state_todos: Annotated[dict, InjectedState]) -> str:
    """Manage a todo list."""

    return f"Todo list updated with {len(todo_writes)} items."


"Ensure to keep using this tool to manage your tasks effectively where applicable."
