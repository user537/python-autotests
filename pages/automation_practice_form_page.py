from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

INPUT_FIRST_NAME = By.ID, "firstName"


class AutomationPracticePage:
    def __init__(self, browser: WebDriver, base_url):
        self.browser = browser
        self.base_url = base_url

    @property
    def input_first_name(self):
        return self.browser.find_element(*INPUT_FIRST_NAME)

    def open(self):
        self.browser.get(self.base_url + '/automation-practice-form')
