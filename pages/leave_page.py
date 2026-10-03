from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LeavePage:
    """
    Page Object Model for OrangeHRM Leave module.

    Handles:
    - Leave navigation
    - Assign Leave
    - Employee selection
    - Leave type selection
    - Date entry
    - Comment entry
    - Leave confirmation popup
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # =========================================================
    # LEAVE MENU
    # =========================================================

    leave_menu = (
        By.XPATH,
        "//span[normalize-space()='Leave']"
    )

    assign_leave = (
        By.XPATH,
        "//a[normalize-space()='Assign Leave']"
    )

    # =========================================================
    # EMPLOYEE
    # =========================================================

    employee_name = (
        By.XPATH,
        "//label[normalize-space()='Employee Name']"
        "/following::input[@placeholder='Type for hints...'][1]"
    )

    employee_suggestion = (
        By.XPATH,
        "//div[@role='option']"
        "//span[normalize-space()='Peter Mac Anderson']"
    )

    # =========================================================
    # LEAVE TYPE
    # =========================================================

    leave_type_dropdown = (
        By.XPATH,
        "//label[normalize-space()='Leave Type']"
        "/following::div[contains(@class,'oxd-select-text')][1]"
    )

    # =========================================================
    # DATES
    # =========================================================

    from_date = (
        By.XPATH,
        "//label[normalize-space()='From Date']"
        "/following::input[1]"
    )

    to_date = (
        By.XPATH,
        "//label[normalize-space()='To Date']"
        "/following::input[1]"
    )

    # =========================================================
    # COMMENT
    # =========================================================

    comments = (
        By.XPATH,
        "//textarea"
    )

    # =========================================================
    # ASSIGN BUTTON
    # =========================================================

    assign_button = (
        By.XPATH,
        "//button[normalize-space()='Assign']"
    )

    # =========================================================
    # CONFIRMATION POPUP
    # =========================================================

    confirmation_popup = (
        By.XPATH,
        "//div[contains(@class,'oxd-dialog-container')]"
        "//*[contains(normalize-space(),"
        "'sufficient leave balance')]"
    )

    popup_ok_button = (
        By.XPATH,
        "//div[contains(@class,'oxd-dialog-container')]"
        "//button[normalize-space()='Ok' or normalize-space()='OK']"
    )

    popup_cancel_button = (
        By.XPATH,
        "//div[contains(@class,'oxd-dialog-container')]"
        "//button[normalize-space()='Cancel']"
    )

    # =========================================================
    # TOAST MESSAGE
    # =========================================================

    success_message = (
        By.XPATH,
        "//p[contains(@class,'oxd-text--toast-message')]"
    )

    # =========================================================
    # NAVIGATION
    # =========================================================

    def click_leave(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.leave_menu
            )
        ).click()

    def click_assign_leave(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.assign_leave
            )
        ).click()

    # =========================================================
    # EMPLOYEE
    # =========================================================

    def enter_employee_name(self, name):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.employee_name
            )
        )

        field.click()
        field.clear()
        field.send_keys(name)

        suggestion = self.wait.until(
            EC.element_to_be_clickable(
                self.employee_suggestion
            )
        )

        suggestion.click()

    # =========================================================
    # LEAVE TYPE
    # =========================================================

    def open_leave_type_dropdown(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.leave_type_dropdown
            )
        ).click()

    def get_leave_type_options(self):

        self.open_leave_type_dropdown()

        options = self.wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    "//div[@role='option']"
                )
            )
        )

        return [
            option.text.strip()
            for option in options
        ]

    def select_leave_type(self, leave_type):

        self.open_leave_type_dropdown()

        option = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//div[@role='option']"
                    f"//span[normalize-space()='{leave_type}']"
                )
            )
        )

        option.click()

    # =========================================================
    # DATES
    # =========================================================

    def enter_from_date(self, date):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.from_date
            )
        )

        field.click()

        field.send_keys(
            Keys.CONTROL,
            "a"
        )

        field.send_keys(
            Keys.BACKSPACE
        )

        field.send_keys(date)

    def enter_to_date(self, date):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.to_date
            )
        )

        field.click()

        field.send_keys(
            Keys.CONTROL,
            "a"
        )

        field.send_keys(
            Keys.BACKSPACE
        )

        field.send_keys(date)

    # =========================================================
    # COMMENT
    # =========================================================

    def enter_comment(self, comment):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.comments
            )
        )

        field.click()
        field.clear()
        field.send_keys(comment)

    # =========================================================
    # ASSIGN
    # =========================================================

    def click_assign(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.assign_button
            )
        ).click()

    # =========================================================
    # CONFIRMATION POPUP
    # =========================================================

    def is_confirmation_popup_displayed(self):

        try:

            self.wait.until(
                EC.visibility_of_element_located(
                    self.confirmation_popup
                )
            )

            return True

        except Exception:

            return False

    def click_popup_ok(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.popup_ok_button
            )
        ).click()

    def click_popup_cancel(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.popup_cancel_button
            )
        ).click()

    # =========================================================
    # SUCCESS MESSAGE
    # =========================================================

    def get_success_message(self):

        message = self.wait.until(
            EC.visibility_of_element_located(
                self.success_message
            )
        )

        return message.text