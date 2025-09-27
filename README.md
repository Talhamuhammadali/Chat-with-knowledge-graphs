# Chat with Knowledge Graphs
The objective of this repository is to learn about RAG systems that use knowledge graphs instead of conventional vector databases.

## Tech Stack
- **Neo4j**: For hosting knowledge graphs
- **LangChain and LangGraph**: For chaining different LLMs and creating complex agentic workflows
- **neomodel**: OGM (Object Graph Mapper) for managing knowledge graphs
- **Redis and SQLite checkpointers**: For short-term and long-term memory for our agents

## Project One
Experimenting with creating a basic agent that can use available data to answer basic questions from a graph database. This is not graph RAG yet, but rather normal tool-based retrieval using parameterized queries.

### Learnings
- I am creating my own LLM router, but I will also use LangChain's `init_chat_model`. It overrides the initialization of chat models while keeping the arguments consistent, so I can easily switch between custom and init-based implementations. Check `llm.py` to see what i mean.