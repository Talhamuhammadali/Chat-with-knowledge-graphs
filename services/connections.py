"""Connections to the knowledge graph database."""
import os

from dotenv import load_dotenv
from neomodel import config, db

load_dotenv() 

def setup_basic_connection():
    """
    Set up basic connection to Neo4j
    
    Default connection assumes:
    - Neo4j running on localhost:7687
    - Username: neo4j
    - Password: password (change this!)
    """
    config.DATABASE_URL = os.getenv('NEO4J_URI', 'bolt://neo4j:password@localhost:7687')
    
    return config.DATABASE_URL

def get_db_status():
    """Check the status of the Neo4j database connection."""
    try:
        result = db.cypher_query("MATCH (n) RETURN n LIMIT 1")
        print(result)
        return "Connected to Neo4j"
    except Exception as e:
        return f"Connection failed: {e}"
    

if __name__ == "__main__":
    print("Setting up connection...")
    print(setup_basic_connection())
    print(get_db_status())