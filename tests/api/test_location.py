
import requests

BASE_URL = "https://rickandmortyapi.com/api"

def test_get_all_locations():
    """ Tests fetch all locations """
    response = requests.get(f"{BASE_URL}/location", timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert isinstance(data["results"], list)

def test_location_detail():
    response = requests.get(f"{BASE_URL}/location/1", timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Earth (C-137)"
