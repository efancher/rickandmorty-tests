import pytest
from tests.ui.pages.home_page import HomePage
from tests.ui.pages.docs_page import Documentation

def test_character_cards_present(driver):
    home = HomePage(driver)
    home.load()
    assert home.has_character_cards()

def test_docs_link(driver):
    home = HomePage(driver)
    home.load()
    home.go_to_docs()
    Documentation(driver).verify_loaded()
    assert "documentation" in driver.current_url.lower()
