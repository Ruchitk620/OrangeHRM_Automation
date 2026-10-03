from pages.login_page import LoginPage
from pages.admin_page import AdminPage


def test_new_user_present_in_admin_list(driver):

    login_page = LoginPage(driver)
    admin_page = AdminPage(driver)

    # Login as Admin
    login_page.open()

    login_page.login(
        "Admin",
        "admin123"
    )

    assert login_page.is_login_successful()

    # Open Admin module
    admin_page.click_admin()

    # Search for the user created in TC5
    username = "testuser01"

    admin_page.search_user(username)

    # Verify user exists in the table
    assert admin_page.is_user_present(username), \
        f"User '{username}' was not found in the Admin user list"

    print(
        f"User '{username}' is present in the Admin user list"
    )