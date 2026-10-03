from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    MENU_ITEMS = {
        "Admin": (By.XPATH, "//span[text()='Admin']"),
        "PIM": (By.XPATH, "//span[text()='PIM']"),
        "Leave": (By.XPATH, "//span[text()='Leave']"),
        "Time": (By.XPATH, "//span[text()='Time']"),
        "Recruitment": (By.XPATH, "//span[text()='Recruitment']"),
        "My Info": (By.XPATH, "//span[text()='My Info']"),
        "Performance": (By.XPATH, "//span[text()='Performance']"),
        "Dashboard": (By.XPATH, "//span[text()='Dashboard']")
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_menu_item_visible(self, menu_name):
        element = self.wait.until(
            EC.visibility_of_element_located(
                self.MENU_ITEMS[menu_name]
            )
        )

        return element.is_displayed()

    def is_menu_item_clickable(self, menu_name):
        element = self.wait.until(
            EC.element_to_be_clickable(
                self.MENU_ITEMS[menu_name]
            )
        )

        return element.is_enabled()