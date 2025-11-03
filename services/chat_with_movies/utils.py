"""Utility functions for the chat_with_movies service."""

from neomodel import AsyncStructuredNode


def get_knowledge_graph_prompt_instructions(
    models: list[AsyncStructuredNode],
    isolation: bool = True,
) -> str:
    """Get prompt instructions specific to the movies knowledge graph.

    Arguments:
    ----
        models (list[AsyncStructuredNode]): List of neomodel node classes representing the KG schema.
        isolation (bool): If true it means the generated prompt is a subset of larger graph isolated for just desired
        nodes.
    """
    prompt = """# Knowledge Graph Schema
You are to work with a knowledge graph with the following schema:
    """
    for model in models:
        prompt += f"\n## Node: {model.__name__}\n"
        prompt += f"{model.__doc__}\n\n"
    if isolation:
        prompt += """
  ## Usage Notes

  This schema represents a **subset** of a larger knowledge graph, isolated for specific query purposes.
  Only the node types and relationships shown above are relevant for your current task.

  When querying or reasoning about this graph:
  - Focus only on the nodes and relationships defined above
  - Follow relationship directions as specified
  - Respect property constraints when suggesting queries or filters
  """
    else:
        prompt += """
  ## Usage Notes

  This is the **complete schema** for the knowledge graph.

  When querying or reasoning about this graph:
  - All available node types and relationships are shown above
  - Follow relationship directions as specified
  - Respect property constraints when suggesting queries or filters
  - Consider traversing relationships to answer complex queries
  """
    return prompt
