from selenium.webdriver.common.by import By
from time import sleep


def test_text_box_positive(browser_management, base_url):
    browser_management.get(base_url + '/text-box')

    text = 'Name:Zalupa\nEmail:valide@mail.com\nCurrent Address :Pushkina\nPermananet Address :Kolotushkina'

    browser_management.find_element(By.ID, "userName").send_keys("Zalupa")
    browser_management.find_element(By.ID, "userEmail").send_keys("valide@mail.com")
    browser_management.find_element(By.ID, "currentAddress").send_keys("Pushkina")
    browser_management.find_element(By.ID, "permanentAddress").send_keys("Kolotushkina")
    # google about scroll method
    browser_management.execute_script("arguments[0].scrollIntoView();",
                                      browser_management.find_element(By.ID, "submit"))
    browser_management.find_element(By.ID, "submit").click()

    sleep(5)

    assert browser_management.find_element(By.ID, "output").is_displayed()
    assert text in browser_management.find_element(By.ID, "output").text
    #  use "in" instead of __contains


def test_text_box_negative(browser_management, base_url):
    browser_management.find_element(By.ID, "userEmail").send_keys("invalid")
    email_error_label = By.XPATH, '//input[@id="userEmail" and contains(@class,"error")]'
    assert browser_management.find_element(email_error_label).is_displayed()
    # запринтить get_attribute class - не понял, какой в этом смысл,
    # get attribute "class" вернет не error, а в xpath выше он уже прописан
