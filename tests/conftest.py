# For global fixtures
import pytest
from selenium import webdriver
from time import sleep


# scope = 'session' - calling fixture ONCE before all tests
# scope = 'function' - calling fixture before any test case USED BY DEFAULT but Explicit is better than implicit
@pytest.fixture(scope='function', autouse=True)
def browser_management():
    # эта хуета выполнится до теста
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    # эта хуета выполнится после теста
    sleep(2)
    browser.close()

@pytest.fixture(autouse=True)
def base_url():
    base_url = 'https://demoqa.com'
    return base_url
