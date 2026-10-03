from pages.login_page import LoginPage


def test_home_url_accessible(driver):

    login_page = LoginPage(driver)

    login_page.open()

    assert "orangehrmlive.com" in driver.current_url

    print("Home URL is accessible:", driver.current_url)