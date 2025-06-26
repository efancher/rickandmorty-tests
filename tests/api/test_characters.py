import pytest
import requests

BASE_URL = "https://rickandmortyapi.com/api"

def test_get_all_characters():
    """ Check that the character api returns at least one character. """
    response = requests.get(f"{BASE_URL}/character")
    assert response.status_code == 200
    json_data = response.json()
    assert "results" in json_data
    assert len(json_data["results"]) > 0

@pytest.mark.parametrize("character_id", [1, 2, 3])
def test_get_character_by_id(character_id):
    """  verifies we can get characters by id """
    response = requests.get(f"{BASE_URL}/character/{character_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == character_id
    assert "name" in data

@pytest.mark.parametrize("status", ["alive", "dead", "unknown"])
def test_filter_by_status(status):
    """" Verifies we can filter by character status """
    response = requests.get(f"{BASE_URL}/character/?status={status}")
    assert response.status_code == 200
    assert all(c["status"].lower() == status for c in response.json().get("results", []))
