from selenium.webdriver.common.by import By
import requests
import logging
import time
from tests.ui.pages.base_page import BasePage

class Documentation(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.docs_link_selector = (By.LINK_TEXT, "Docs")
        self.title = (By.XPATH, "//h1[text()='Documentation']")
    def verify_loaded(self):
        self.wait_for_presence(self.title)
