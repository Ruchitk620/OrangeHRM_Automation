from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage


def test_login_fields_visible_and_enabled(driver):

    login_page = LoginPage(driver)
    login_page.open()

    wait = WebDriverWait(driver, 10)

    username = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "username")
        )
    )

    password = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "password")
        )
    )

    assert username.is_displayed()
    assert username.is_enabled()

    assert password.is_displayed()
    assert password.is_enabled()

    print("Username field is visible and enabled")
    print("Password field is visible and enabled")