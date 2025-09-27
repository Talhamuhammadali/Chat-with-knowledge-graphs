from dotenv import load_dotenv
from utils.llm import test_all_models, test_langchain_init_models
from connections import setup_basic_connection, get_db_status

load_dotenv()

def main():
    print("Hello from chat-with-knowledge-graphs!")

    print("\nSetting up Neo4j connection...")
    db_url = setup_basic_connection()
    print(f"Database URL: {db_url}")
    print(f"Status: {get_db_status()}")

    print("\nTesting LLM models...")
    test_langchain_init_models()


if __name__ == "__main__":
    main()
