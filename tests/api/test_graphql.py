
import requests

GRAPHQL_URL = "https://rickandmortyapi.com/graphql"

def test_graphql_character_query():
    """" Tests character more complex query"""
    query = {
        "query": "{ characters(page: 1) { results { name status species } } }"
    }
    response = requests.post(GRAPHQL_URL, json=query, timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert "characters" in data["data"]
    assert "results" in data["data"]["characters"]
    assert isinstance(data["data"]["characters"]["results"], list)
