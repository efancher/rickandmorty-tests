
import requests

BASE_URL = "https://rickandmortyapi.com/api"

def test_get_all_episodes():
    """ Verifies we can get all the episodes """ 
    response = requests.get(f"{BASE_URL}/episode", timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert isinstance(data["results"], list)

def test_episode_detail():
    """ Verifies we can get an episode
        --TODO-- make data drivern
    """
    response = requests.get(f"{BASE_URL}/episode/1", timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Pilot"
