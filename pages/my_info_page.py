from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyInfoPage:
    """Page Object Model for the My Info section."""

    my_info_menu = (
        By.XPATH,
        "//span[normalize-space()='My Info']"
    )

    personal_details = (
        By.XPATH,
        "//a[contains(normalize-space(),'Personal Details')]"
    )

    contact_details = (
        By.XPATH,
        "//a[contains(normalize-space(),'Contact Details')]"
    )

    emergency_contacts = (
        By.XPATH,
        "//a[contains(normalize-space(),'Emergency Contacts')]"
    )

    dependents = (
        By.XPATH,
        "//a[contains(normalize-space(),'Dependents')]"
    )

    immigration = (
        By.XPATH,
        "//a[contains(normalize-space(),'Immigration')]"
    )

    job = (
        By.XPATH,
        "//a[contains(normalize-space(),'Job')]"
    )

    salary = (
        By.XPATH,
        "//a[contains(normalize-space(),'Salary')]"
    )

    qualifications = (
        By.XPATH,
        "//a[contains(normalize-space(),'Qualifications')]"
    )

    memberships = (
        By.XPATH,
        "//a[contains(normalize-space(),'Memberships')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_my_info(self):
        """Open My Info section."""
        self.wait.until(
            EC.element_to_be_clickable(self.my_info_menu)
        ).click()

    def is_section_visible(self, locator):
        """Check whether a My Info section is visible."""
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return element.is_displayed()

    def is_section_clickable(self, locator):
        """Check whether a My Info section is clickable."""
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        return element.is_enabled()