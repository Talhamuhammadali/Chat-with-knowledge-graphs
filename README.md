# Chat with Knowledge Graphs
The objective of this repository is to learn about RAG systems that use knowledge graphs instead of conventional vector databases.

## Tech Stack
- **Neo4j**: For hosting knowledge graphs
- **LangChain and LangGraph**: For chaining different LLMs and creating complex agentic workflows
- **neomodel**: OGM (Object Graph Mapper) for managing knowledge graphs
- **Redis and SQLite checkpointers**: For short-term and long-term memory for our agents

## Project One
Experimenting with creating a basic agent that can use the available data to answer basic question from graph database. Its not graph rag yet but normal tool based retreival using parameterized queries.