# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## ⚠️ IMPORTANT: Learning-First Approach
**This is a learn-first project. The user prefers to learn and implement solutions themselves.**
- When help is requested, provide options, possible issues, and guidance rather than directly fixing problems
- Use tools only when explicitly asked (e.g., "edit this file", "create this file")
- For bash commands, provide the command as text with detailed breakdown rather than executing it
- Enable learning, don't do the work for the user

## Project Overview
This project implements RAG (Retrieval-Augmented Generation) systems using knowledge graphs instead of conventional vector databases. The tech stack includes Neo4j for hosting knowledge graphs, Langchain/Langgraph for LLM chaining and agentic workflows, neomodel as an OGM for knowledge graph management, and Redis/SQLite checkpointers for agent memory.

## Development Environment
- **Python Version**: 3.13+ (see .python-version)
- **Package Manager**: UV (uses pyproject.toml and uv.lock)
- **Virtual Environment**: Uses venv/ directory

## Common Commands
```bash
# Setup and dependencies
uv sync                    # Install dependencies from lock file
uv add <package>          # Add new dependency
uv run python main.py     # Run the main application

# Development
python main.py            # Run main application
jupyter notebook         # Start Jupyter for development notebooks
```

## Key Dependencies
- **LangChain Stack**: langchain-anthropic, langchain-community, langchain-core, langchain-openai, langchain-huggingface
- **LangGraph**: langgraph, langgraph-cli, langgraph-sdk, langgraph-prebuilt
- **Knowledge Graph**: neo4j, neomodel
- **Memory/Checkpointing**: langgraph-checkpoint-redis, langgraph-checkpoint-sqlite
- **Tools**: tavily-python (search), trustcall, wikipedia, notebook

## Project Structure
```
services/
├── main.py                      # Main application entry point
├── connections.py               # Neo4j database connection setup
├── utils/
│   └── llm.py                  # LLM provider abstraction (Anthropic, OpenAI, Google)
└── chat_with_movies/            # Movie recommendation agent service
    ├── model.py                 # Neomodel schema (Movie, Person nodes)
    ├── queries.py               # Neo4j query utilities
    └── agent/                   # LangGraph agent implementation
        ├── state.py             # Agent state definition
        ├── graph.py             # LangGraph workflow (agent, subagent, tool, ask_human nodes)
        ├── nodes.py             # Agent node implementations
        ├── tools.py             # Agent tools
        ├── prompts.py           # System prompts
        └── models.py            # Pydantic models
```

## Architecture Notes
- Service-based structure: Each use case in its own service directory
- Designed for RAG systems using knowledge graphs instead of vector databases
- Agent-based workflows with memory persistence
- Uses both Redis (short-term) and SQLite (long-term) for agent memory

### Current Services
**chat_with_movies**: Movie recommendation agent using Neo4j knowledge graph
- Knowledge graph model with Movie and Person nodes (ACTED_IN, DIRECTED, etc. relationships)
- LangGraph-based agent with conditional routing
- Query utilities for graph traversal
- Status: WIP - agent nodes, tools, and routing logic being implemented
