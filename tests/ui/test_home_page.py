import datetime
import pytest
import requests
from tests.ui.pages.home_page import HomePage
from tests.ui.pages.docs_page import Documentation

def test_bad_character_id(driver):
    """ Tests that you get an error for a bad character id """
    # --TODO-- should move url out to a paramter or config file
    response = requests.get("https://rickandmortyapi.com/api/character/4242", timeout=10)
    print(response.status_code)
    assert response.status_code == 404 

def test_character_cards_present(driver):
    """ Tests that the home page has character cards."""
    home = HomePage(driver)
    home.load()
    assert home.has_character_cards()

def test_docs_link(driver):
    """ Tests that the docs link in the navigation bar works """
    home = HomePage(driver)
    home.load()
    home.go_to_docs()
    Documentation(driver).verify_loaded()
    assert "documentation" in driver.current_url.lower()

def test_footer_copyright_date(driver):
    """ Tests that the footer copyright has the copyright date """
    home = HomePage(driver)
    home.load()
    footer = home.footer
    year = "2023" 
    assert year in footer.text

