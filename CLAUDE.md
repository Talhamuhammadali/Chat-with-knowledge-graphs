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

## Architecture Notes
- Early stage project with minimal code structure (main.py contains basic hello world)
- Designed for RAG systems using knowledge graphs
- Agent-based workflows with memory persistence
- Uses both Redis (short-term) and SQLite (long-term) for agent memory