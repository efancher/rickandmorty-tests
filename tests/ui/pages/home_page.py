from selenium.webdriver.common.by import By
import requests
import logging
import time
from tests.ui.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.character_card_selector = (By.XPATH, "//article[contains(@class, 'characterCard')]")
        self.title = (By.XPATH, "//article[contains(@class, 'characterCard')]")
    def verify_loaded(self):

        self.wait_for_presence(self.title)

    def load(self):
        # test connection
        response = requests.get(f"{self.BASE_URL}/api/character", timeout=10)
        self.driver.get(f"{self.BASE_URL}")

    def has_character_cards(self):
        self.verify_loaded()
        number_character_card = len(self.driver.find_elements(*self.character_card_selector))
        logging.info(f"Number of character cards: {number_character_card}")
        return number_character_card > 0
