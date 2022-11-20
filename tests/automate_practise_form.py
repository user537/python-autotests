from selenium.webdriver.common.by import By


def test_automate_practise_form(browser_management, base_url):
    browser_management.get(base_url + '/automation-practice-form')

    first_name = browser_management.find_element(By.ID, "firstName").send_keys("Poopa")
    last_name = browser_management.find_element(By.ID, "lastName").send_keys("Loopa")
    user_email = browser_management.find_element(By.ID, "userEmail").send_keys("valide@qwe.qwe")

    # залупа не хочет кликать по элементу, хотя он displayed
    gen_radio_1 = browser_management.find_element(By.ID, "gender-radio-1").is_displayed()


