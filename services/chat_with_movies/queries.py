"""Some Test queries for the knowledge graph for Movies and actors."""
from services.connections import setup_basic_connection
from neomodel import db

def get_all_node_labels():
    """Get all node labels in the database."""
    query = "CALL db.labels()"
    results, _ = db.cypher_query(query)
    return [record[0] for record in results]

def get_all_relationship_types():
    """Get all relationship types in the database."""
    query = "CALL db.relationshipTypes()"
    results, _ = db.cypher_query(query)
    return [record[0] for record in results]


def get_all_nodes() -> dict:
    """
    Get all nodes with their labels and properties.
    
    Returns:
        dict: Dictionary with node data organized by labels
    """
    query = """
    MATCH (n)
    RETURN labels(n) AS labels, keys(n) AS properties, n
    """
    
    try:
        result, _ = db.cypher_query(query)
        
        nodes_by_label = {}
        
        for record in result:
            labels = record[0]  # labels
            properties = record[1]  # properties
            node_data = record[2]  # actual node

            primary_label = labels[0] if labels else 'Unlabeled'
            
            if primary_label not in nodes_by_label:
                nodes_by_label[primary_label] = {
                    'count': 0,
                    'properties': set(),
                    'sample_nodes': []
                }
            
            nodes_by_label[primary_label]['count'] += 1
            nodes_by_label[primary_label]['properties'].update(properties)
            
            if len(nodes_by_label[primary_label]['sample_nodes']) < 3:
                nodes_by_label[primary_label]['sample_nodes'].append(dict(node_data))
        
        for label_data in nodes_by_label.values():
            label_data['properties'] = list(label_data['properties'])
            
        return nodes_by_label
        
    except Exception as e:
        print(f"Error querying Neo4j: {e}")
        return {}

def get_nodes_count_by_label(label:str) -> int:
    """
    Get the total count of all nodes in the database.
    
    Returns:
        int: Total number of nodes
    """
    query = f"MATCH (n:{label}) RETURN count(n) AS total_nodes"
    
    try:
        result, _ = db.cypher_query(query)
        total_nodes = result[0][0] if result else 0
        return total_nodes
        
    except Exception as e:
        print(f"Error querying Neo4j: {e}")
        return 0

def get_by_label(label: str, limit: int = 10) -> list:
    """
    Get nodes by label with a limit on the number of results.
    
    Args:
        label (str): The label of the nodes to retrieve.
        limit (int): The maximum number of nodes to return.
        
    Returns:
        list: List of nodes with the specified label
    """
    query = f"""
    MATCH (n:{label})
    RETURN n
    LIMIT {limit}
    """
    
    try:
        result, _ = db.cypher_query(query)
        nodes = [dict(record[0]) for record in result]
        return nodes
        
    except Exception as e:
        print(f"Error querying Neo4j: {e}")
        return []

if __name__ == "__main__":
    from pprint import pprint
    setup_basic_connection()    
    pprint("Node Labels in the database:")
    labels = get_all_node_labels()
    pprint(labels)

    print("\nAll nodes in the database:")
    pprint(get_all_nodes())
    print("\nRelationship Types in the database:")
    pprint(get_all_relationship_types())
    print("\nTotal number of nodes in the database:")
    for label in labels:
        count = get_nodes_count_by_label(label)
        print(f"Label '{label}': {count} nodes")
    for label in labels:
        print(f"\nSample nodes with label '{label}':")
        pprint(get_by_label(label, limit=100))
    