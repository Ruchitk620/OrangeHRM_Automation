from pages.login_page import LoginPage
from pages.admin_page import AdminPage


def test_create_new_user_and_validate_login(driver):

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

    # Click Add
    admin_page.click_add()

    # Select Admin as User Role
    admin_page.select_user_role_admin()

    # Enter employee name and select Peter Mac Anderson
    admin_page.enter_employee_name("Peter")

    # Select Enabled status
    admin_page.select_status_enabled()

    # Enter new username
    admin_page.enter_username("testuser001")

    # Enter password
    admin_page.enter_password("Test@12345")

    # Confirm password
    admin_page.enter_confirm_password("Test@12345")

    # Save new user
    admin_page.click_save()

    # Verify successful creation
    message = admin_page.get_success_message()

    print("Success message:", message)

    assert "Successfully Saved" in message