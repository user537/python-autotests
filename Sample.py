import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# если нужно, то можно задать как autouse или добавить маркер
@pytest.fixture()
def browser():
    #параметры нужно будет куда-то закинуть отдельно?
    base_url = 'https://demoqa.com/text-box'

    # эта хуета выполнится до теста
    browser = webdriver.Chrome()
    browser.get(base_url)
    browser.maximize_window()
    yield browser
    # эта хуета выполнится после теста
    sleep(2)
    browser.close()


def test_text_box_positive(browser):

    text = 'Name:Zalupa\nEmail:valide@mail.com\nCurrent Address :Pushkina\nPermananet Address :Kolotushkina'

    browser.find_element(By.ID, "userName").send_keys("Zalupa")
    browser.find_element(By.ID, "userEmail").send_keys("valide@mail.com")
    browser.find_element(By.ID, "currentAddress").send_keys("Pushkina")
    browser.find_element(By.ID, "permanentAddress").send_keys("Kolotushkina")
    # google about scroll method
    browser.execute_script("arguments[0].scrollIntoView();", browser.find_element(By.ID, "submit"))
    browser.find_element(By.ID, "submit").click()

    sleep(5)

    assert browser.find_element(By.ID, "output").is_displayed()
    assert browser.find_element(By.ID, "output").text.__contains__(text)
    #  use "in" instead of __contains