from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:
    """Page Object Model for the OrangeHRM Admin page."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    admin_menu = (By.XPATH, "//span[text()='Admin']")
    add_button = (By.XPATH, "//button[normalize-space()='Add']")
    user_role_dropdown = (By.XPATH, "//label[text()='User Role']/following::div[contains(@class,'oxd-select-text')][1]")
    employee_name = (By.XPATH, "//label[text()='Employee Name']/following::input[@placeholder='Type for hints...'][1]")
    employee_suggestion = (By.XPATH, "//div[@role='option']//span[contains(text(),'Peter Mac Anderson')]")
    status_dropdown = (By.XPATH, "//label[text()='Status']/following::div[contains(@class,'oxd-select-text')][1]")
    username = (By.XPATH, "//label[text()='Username']/following::input[1]")
    password = (By.XPATH, "//label[text()='Password']/following::input[1]")
    confirm_password = (By.XPATH, "//label[text()='Confirm Password']/following::input[1]")
    save_button = (By.XPATH, "//button[normalize-space()='Save']")
    success_message = (By.XPATH, "//p[contains(@class,'oxd-text--toast-message')]")
    search_username = (By.XPATH, "//div[contains(@class,'oxd-input-group')]//label[text()='Username']/following::input[1]")
    search_button = (By.XPATH, "//button[normalize-space()='Search']")
    reset_button = (By.XPATH, "//button[normalize-space()='Reset']")

    def click_admin(self):
        self.wait.until(EC.element_to_be_clickable(self.admin_menu)).click()

    def click_add(self):
        self.wait.until(EC.element_to_be_clickable(self.add_button)).click()

    def select_user_role_admin(self):
        self.wait.until(EC.element_to_be_clickable(self.user_role_dropdown)).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='option']//span[text()='Admin']"))).click()

    def enter_employee_name(self, name):
        field = self.wait.until(EC.visibility_of_element_located(self.employee_name))
        field.clear()
        field.send_keys(name)
        self.wait.until(EC.element_to_be_clickable(self.employee_suggestion)).click()

    def select_status_enabled(self):
        self.wait.until(EC.element_to_be_clickable(self.status_dropdown)).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='option']//span[text()='Enabled']"))).click()

    def enter_username(self, username):
        field = self.wait.until(EC.visibility_of_element_located(self.username))
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.wait.until(EC.visibility_of_element_located(self.password))
        field.clear()
        field.send_keys(password)

    def enter_confirm_password(self, password):
        field = self.wait.until(EC.visibility_of_element_located(self.confirm_password))
        field.clear()
        field.send_keys(password)

    def click_save(self):
        self.wait.until(EC.element_to_be_clickable(self.save_button)).click()

    def get_success_message(self):
        message = self.wait.until(EC.visibility_of_element_located(self.success_message))
        return message.text

    def search_user(self, username):
        field = self.wait.until(EC.visibility_of_element_located(self.search_username))
        field.clear()
        field.send_keys(username)
        self.wait.until(EC.element_to_be_clickable(self.search_button)).click()

    def is_user_present(self, username):
        user = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, f"//div[@role='row']//div[normalize-space()='{username}']")
        ))
        return user.is_displayed()
