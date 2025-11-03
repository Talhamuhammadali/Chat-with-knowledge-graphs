"""Main application entry point for chat-with-knowledge-graphs."""

from connections import get_db_status, setup_basic_connection
from dotenv import load_dotenv
from utils.llm import test_langchain_init_models

load_dotenv()


def main():
    """Initialize and run the application."""
    print("Hello from chat-with-knowledge-graphs!")

    print("\nSetting up Neo4j connection...")
    db_url = setup_basic_connection()
    print(f"Database URL: {db_url}")
    print(f"Status: {get_db_status()}")

    print("\nTesting LLM models...")
    test_langchain_init_models()


if __name__ == "__main__":
    main()
