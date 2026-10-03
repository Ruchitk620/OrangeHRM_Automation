from pages.login_page import LoginPage


def test_forgot_password(driver):

    login_page = LoginPage(driver)

    # Open OrangeHRM login page
    login_page.open()

    # Click Forgot your password?
    login_page.click_forgot_password()

    # Enter a registered username
    login_page.enter_reset_username("Admin")

    # Submit password reset request
    login_page.click_reset_password()

    # Verify confirmation
    assert login_page.is_reset_successful(), \
        "Password reset confirmation was not displayed"

    print("Password reset confirmation displayed successfully")