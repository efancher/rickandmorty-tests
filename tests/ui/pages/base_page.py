from selenium.webdriver.common.by import By
import requests
import logging
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    """ Represents a common page, should have elements common to other pages, such as navigation bars, footers
    """
    def __init__(self, driver):
        self.driver = driver
        self.BASE_URL="https://rickandmortyapi.com"
        self.logger = logging.getLogger(__name__) 
        self.docs_link_selector = (By.LINK_TEXT, "Docs")
        self.graphql_link_selector = (By.LINK_TEXT, "GraphQL")
        self.footer_selector = (By.TAG_NAME, "footer")
    def wait_for_presence(self, locator, waittime=10):
        return WebDriverWait(self.driver, waittime).until(EC.presence_of_element_located(locator))

    @property
    def docs_link(self):
        return self.wait_for_presence(self.docs_link_selector)

    def go_to_docs(self):
        self.docs_link.click()

    @property
    def graphql_link(self):
        return self.wait_for_presence(self.graphql_link_selector)

    def go_to_graphql(self):
        self.graphql_link.click()

    @property
    def footer(self):
        return self.wait_for_presence(self.footer_selector)

