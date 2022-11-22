from pages.automation_practice_form_page import AutomationPracticePage

def test_dimple(practice_page):

    practice_page.input_first_name.send_keys("Poopa")