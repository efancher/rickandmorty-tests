
import pytest
import requests

BASE_URL = "https://rickandmortyapi.com/api"

@pytest.mark.parametrize("episode_id,expected_name", [
    (1, "Pilot"),
    (10, "Close Rick-counters of the Rick Kind"),
    (9999, None),  # Invalid ID
])
def test_episode_by_id(episode_id, expected_name):
    response = requests.get(f"{BASE_URL}/episode/{episode_id}", timeout=10)
    if expected_name:
        assert response.status_code == 200
        assert response.json()["name"] == expected_name
    else:
        assert response.status_code == 404
