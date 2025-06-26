
import pytest
import requests

GRAPHQL_URL = "https://rickandmortyapi.com/graphql"

@pytest.mark.parametrize("character_id,expected_name", [
    (1, "Rick Sanchez"),
    (2, "Morty Smith"),
    (9999, None)
])
def test_graphql_character_query_by_id(character_id, expected_name):
    """ Tests graphql fetch character by id
    """
    query = {
        "query": f"{{ character(id: {character_id}) {{ name status species }} }}"
    }
    response = requests.post(GRAPHQL_URL, json=query, timeout=10)
    assert response.status_code == 200
    data = response.json()
    if expected_name:
        assert data["data"]["character"]["name"] == expected_name
    else:
        assert data["data"]["character"] is None
