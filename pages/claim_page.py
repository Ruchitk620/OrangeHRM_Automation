from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ClaimPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # =========================================================
    # CLAIM
    # =========================================================

    claim_menu = (
        By.XPATH,
        "//span[normalize-space()='Claim']"
    )

    submit_claim = (
        By.XPATH,
        "//a[normalize-space()='Submit Claim']"
    )

    event_dropdown = (
        By.XPATH,
        "//label[normalize-space()='Event']"
        "/following::div[contains(@class,'oxd-select-text')][1]"
    )

    currency_dropdown = (
        By.XPATH,
        "//label[normalize-space()='Currency']"
        "/following::div[contains(@class,'oxd-select-text')][1]"
    )

    remarks = (
        By.XPATH,
        "//label[normalize-space()='Remarks']"
        "/following::textarea[1]"
    )

    create_button = (
        By.XPATH,
        "//button[normalize-space()='Create']"
    )

    # =========================================================
    # EXPENSES
    # =========================================================

    expenses_add_button = (
        By.XPATH,
        "//*[normalize-space()='Expenses']"
        "/following::button[normalize-space()='Add'][1]"
    )

    expense_dialog = (
        By.XPATH,
        "//div[contains(@class,'oxd-dialog-container')]"
    )

    expense_type_dropdown = (
        By.XPATH,
        "//div[contains(@class,'oxd-dialog-container')]"
        "//label[normalize-space()='Expense Type']"
        "/following::div[contains(@class,'oxd-select-text')][1]"
    )

    expense_date = (
        By.XPATH,
        "//div[contains(@class,'oxd-dialog-container')]"
        "//label[normalize-space()='Date']"
        "/following::input[1]"
    )

    expense_amount = (
        By.XPATH,
        "//div[contains(@class,'oxd-dialog-container')]"
        "//label[normalize-space()='Amount']"
        "/following::input[1]"
    )

    expense_note = (
        By.XPATH,
        "//div[contains(@class,'oxd-dialog-container')]"
        "//label[normalize-space()='Note']"
        "/following::textarea[1]"
    )

    expense_save_button = (
        By.XPATH,
        "//div[contains(@class,'oxd-dialog-container')]"
        "//button[normalize-space()='Save']"
    )

    # =========================================================
    # ATTACHMENTS
    # =========================================================

    # Find the Add button specifically associated with
    # the Attachments section.
    attachments_add_button = (
        By.XPATH,
        "//*[normalize-space()='Attachments']"
        "/following::button[normalize-space()='Add'][1]"
    )

    attachment_dialog = (
        By.XPATH,
        "//div[contains(@class,'oxd-dialog-container')]"
    )

    attachment_file = (
        By.XPATH,
        "//div[contains(@class,'oxd-dialog-container')]"
        "//input[@type='file']"
    )

    attachment_comment = (
        By.XPATH,
        "//div[contains(@class,'oxd-dialog-container')]"
        "//textarea"
    )

    attachment_save_button = (
        By.XPATH,
        "//div[contains(@class,'oxd-dialog-container')]"
        "//button[normalize-space()='Save']"
    )

    # =========================================================
    # FINAL SUBMIT
    # =========================================================

    submit_button = (
        By.XPATH,
        "//button[normalize-space()='Submit']"
    )

    success_message = (
        By.XPATH,
        "//p[contains(@class,'oxd-text--toast-message')]"
    )

    # =========================================================
    # CLAIM METHODS
    # =========================================================

    def click_claim(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.claim_menu
            )
        ).click()

    def click_submit_claim(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.submit_claim
            )
        ).click()

    def select_event(self, event_name):

        self.wait.until(
            EC.element_to_be_clickable(
                self.event_dropdown
            )
        ).click()

        option = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[@role='option']//span"
                    f"[normalize-space()='{event_name}']"
                )
            )
        )

        option.click()

    def select_currency(self, currency_name):

        self.wait.until(
            EC.element_to_be_clickable(
                self.currency_dropdown
            )
        ).click()

        option = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[@role='option']//span"
                    f"[normalize-space()='{currency_name}']"
                )
            )
        )

        option.click()

    def enter_remarks(self, text):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.remarks
            )
        )

        field.clear()
        field.send_keys(text)

    def click_create(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.create_button
            )
        ).click()

    # =========================================================
    # EXPENSE METHODS
    # =========================================================

    def click_add_expense(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.expenses_add_button
            )
        )

        button.click()

        self.wait.until(
            EC.visibility_of_element_located(
                self.expense_dialog
            )
        )

    def select_expense_type(self, expense_type):

        self.wait.until(
            EC.element_to_be_clickable(
                self.expense_type_dropdown
            )
        ).click()

        option = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[contains(@class,'oxd-select-dropdown')]"
                    f"//span[normalize-space()='{expense_type}']"
                )
            )
        )

        option.click()

    def enter_expense_date(self, date):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.expense_date
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

    def enter_expense_amount(self, amount):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.expense_amount
            )
        )

        field.click()
        field.clear()
        field.send_keys(str(amount))

    def enter_expense_note(self, note):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.expense_note
            )
        )

        field.click()
        field.clear()
        field.send_keys(note)

    def save_expense(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.expense_save_button
            )
        ).click()

        # IMPORTANT:
        # Wait until the Add Expense dialog is completely gone
        # before interacting with the Claim Details page.
        self.wait.until(
            EC.invisibility_of_element_located(
                self.expense_dialog
            )
        )

    # =========================================================
    # ATTACHMENT METHODS
    # =========================================================

    def click_add_attachment(self):

        # Make absolutely sure no dialog is covering the page.
        try:
            self.wait.until(
                EC.invisibility_of_element_located(
                    self.expense_dialog
                )
            )
        except Exception:
            pass

        # Find Attachments Add button.
        button = self.wait.until(
            EC.presence_of_element_located(
                self.attachments_add_button
            )
        )

        # Scroll the button into the visible area.
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            button
        )

        # Wait until it is clickable.
        button = self.wait.until(
            EC.element_to_be_clickable(
                self.attachments_add_button
            )
        )

        # Normal click first.
        try:
            button.click()

        except Exception:

            # Fallback for the OrangeHRM page when another
            # transparent/animation layer intercepts the click.
            self.driver.execute_script(
                "arguments[0].click();",
                button
            )

        # Wait for Add Attachment dialog.
        self.wait.until(
            EC.visibility_of_element_located(
                self.attachment_dialog
            )
        )

        self.wait.until(
            EC.presence_of_element_located(
                self.attachment_file
            )
        )

    def upload_attachment(self, file_path):

        file_input = self.wait.until(
            EC.presence_of_element_located(
                self.attachment_file
            )
        )

        file_input.send_keys(
            file_path
        )

    def enter_attachment_comment(self, comment):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.attachment_comment
            )
        )

        field.click()
        field.clear()
        field.send_keys(comment)

    def save_attachment(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.attachment_save_button
            )
        ).click()

        # Wait for attachment dialog to close.
        self.wait.until(
            EC.invisibility_of_element_located(
                self.attachment_dialog
            )
        )

    # =========================================================
    # FINAL SUBMIT
    # =========================================================

    def click_submit(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.submit_button
            )
        ).click()

    def is_success_message_displayed(self):

        try:

            self.wait.until(
                EC.visibility_of_element_located(
                    self.success_message
                )
            )

            return True

        except Exception:

            return False

    def get_success_message(self):

        message = self.wait.until(
            EC.visibility_of_element_located(
                self.success_message
            )
        )

        return message.text