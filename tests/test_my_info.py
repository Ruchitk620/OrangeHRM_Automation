from pages.login_page import LoginPage
from pages.my_info_page import MyInfoPage


def test_my_info_menu_items(driver):

    login_page = LoginPage(driver)
    my_info_page = MyInfoPage(driver)

    # Open OrangeHRM
    login_page.open()

    # Login as Admin
    login_page.login(
        "Admin",
        "admin123"
    )

    assert login_page.is_login_successful()

    # Open My Info
    my_info_page.click_my_info()

    sections = {
        "Personal Details": my_info_page.personal_details,
        "Contact Details": my_info_page.contact_details,
        "Emergency Contacts": my_info_page.emergency_contacts,
        "Dependents": my_info_page.dependents,
        "Immigration": my_info_page.immigration,
        "Job": my_info_page.job,
        "Salary": my_info_page.salary,
        "Qualifications": my_info_page.qualifications,
        "Memberships": my_info_page.memberships
    }

    for section_name, locator in sections.items():

        assert my_info_page.is_section_visible(locator), \
            f"{section_name} is not visible"

        assert my_info_page.is_section_clickable(locator), \
            f"{section_name} is not clickable"

        print(
            f"{section_name}: visible and clickable"
        )