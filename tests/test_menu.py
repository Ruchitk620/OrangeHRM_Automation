from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_main_menu_items_visible_and_clickable(driver):

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    # Open OrangeHRM
    login_page.open()

    # Login with valid admin credentials
    login_page.login(
        "Admin",
        "admin123"
    )

    # Verify successful login
    assert login_page.is_login_successful()

    menu_items = [
        "Admin",
        "PIM",
        "Leave",
        "Time",
        "Recruitment",
        "My Info",
        "Performance",
        "Dashboard"
    ]

    for menu_item in menu_items:

        assert dashboard_page.is_menu_item_visible(menu_item), \
            f"{menu_item} is not visible"

        assert dashboard_page.is_menu_item_clickable(menu_item), \
            f"{menu_item} is not clickable"

        print(
            f"{menu_item}: visible and clickable"
        )