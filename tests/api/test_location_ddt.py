
import pytest
import requests

BASE_URL = "https://rickandmortyapi.com/api"

@pytest.mark.parametrize("location_id,expected_name", [
    (1, "Earth (C-137)"),
    (20, "Earth (Replacement Dimension)"),
    (9999, None),  # Non-existent location
])
def test_location_by_id(location_id, expected_name):
    """ Tests episode locations names """
    response = requests.get(f"{BASE_URL}/location/{location_id}", timeout=10)
    if expected_name:
        assert response.status_code == 200
        assert response.json()["name"] == expected_name
    else:
        assert response.status_code == 404
