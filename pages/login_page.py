from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    URL = "https://opensource-demo.orangehrmlive.com"

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    FORGOT_PASSWORD = (
        By.XPATH,
        "//p[contains(normalize-space(),'Forgot your password?')]"
    )

    RESET_USERNAME = (
        By.XPATH,
        "//label[text()='Username']/following::input[1]"
    )

    RESET_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Reset Password']"
    )

    CANCEL_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Cancel']"
    )

    RESET_SUCCESS_MESSAGE = (
        By.XPATH,
        "//h6[normalize-space()='Reset Password link sent successfully']"
    )

    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        ".oxd-alert-content-text"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # =========================================================
    # LOGIN
    # =========================================================

    def open(self):
        """Open OrangeHRM login page."""

        self.driver.get(self.URL)

    def enter_username(self, username):
        """Enter username."""

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.USERNAME
            )
        )

        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        """Enter password."""

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.PASSWORD
            )
        )

        field.clear()
        field.send_keys(password)

    def click_login(self):
        """Click Login button."""

        self.wait.until(
            EC.element_to_be_clickable(
                self.LOGIN_BUTTON
            )
        ).click()

    def login(self, username, password):
        """Login using supplied credentials."""

        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_login_successful(self):
        """Check whether login reached dashboard."""

        try:

            self.wait.until(
                EC.url_contains("/dashboard")
            )

            return True

        except Exception:

            return False

    def logout(self):
        """Logout from OrangeHRM."""

        user_dropdown = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    ".oxd-userdropdown-tab"
                )
            )
        )

        user_dropdown.click()

        logout_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[normalize-space()='Logout']"
                )
            )
        )

        logout_button.click()

        self.wait.until(
            EC.visibility_of_element_located(
                self.USERNAME
            )
        )

    # =========================================================
    # FORGOT PASSWORD
    # =========================================================

    def click_forgot_password(self):
        """Open Forgot Password page."""

        self.wait.until(
            EC.element_to_be_clickable(
                self.FORGOT_PASSWORD
            )
        ).click()

    def enter_reset_username(self, username):
        """Enter username for password reset."""

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.RESET_USERNAME
            )
        )

        field.clear()
        field.send_keys(username)

    def click_reset_password(self):
        """Submit password reset request."""

        self.wait.until(
            EC.element_to_be_clickable(
                self.RESET_BUTTON
            )
        ).click()

    def is_reset_successful(self):
        """Verify password reset confirmation."""

        try:

            self.wait.until(
                EC.visibility_of_element_located(
                    self.RESET_SUCCESS_MESSAGE
                )
            )

            return True

        except Exception:

            return False