import os
import tempfile

from pages.login_page import LoginPage
from pages.claim_page import ClaimPage


def create_test_attachment():

    file_path = os.path.join(
        tempfile.gettempdir(),
        "medical_expense_receipt.txt"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "Medical Expense Receipt\n"
            "Expense Type: Accommodation\n"
            "Amount: 1000 INR\n"
            "Test automation attachment\n"
        )

    return file_path


def test_claim_request(driver):

    # =========================================================
    # TEST DATA
    # =========================================================

    username = "Admin"
    password = "admin123"

    event_name = "Medical Reimbursement"
    currency_name = "Indian Rupee"

    claim_remarks = "Medical reimbursement claim"

    # Expense
    expense_type = "Accommodation"
    expense_date = "2026-10-02"
    expense_amount = "1000"
    expense_note = "Medical expense for claim"

    # Attachment
    attachment_comment = "Medical expense receipt"

    attachment_path = None

    # =========================================================
    # LOGIN
    # =========================================================

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(
        username,
        password
    )

    assert login_page.is_login_successful(), \
        "Admin login failed"

    print("Admin login successful")

    # =========================================================
    # CLAIM
    # =========================================================

    claim_page = ClaimPage(driver)

    claim_page.click_claim()

    print("Claim module opened")

    claim_page.click_submit_claim()

    print("Submit Claim page opened")

    # =========================================================
    # CLAIM DETAILS
    # =========================================================

    claim_page.select_event(
        event_name
    )

    print(
        f"Event selected: {event_name}"
    )

    claim_page.select_currency(
        currency_name
    )

    print(
        f"Currency selected: {currency_name}"
    )

    claim_page.enter_remarks(
        claim_remarks
    )

    print(
        "Claim remarks entered"
    )

    # =========================================================
    # CREATE CLAIM
    # =========================================================

    claim_page.click_create()

    print(
        "Create button clicked"
    )

    # =========================================================
    # EXPENSE
    # =========================================================

    claim_page.click_add_expense()

    print(
        "Expenses Add button clicked"
    )

    print(
        "Add Expense dialog opened"
    )

    claim_page.select_expense_type(
        expense_type
    )

    print(
        f"Expense Type selected: {expense_type}"
    )

    claim_page.enter_expense_date(
        expense_date
    )

    print(
        f"Expense Date entered: {expense_date}"
    )

    claim_page.enter_expense_amount(
        expense_amount
    )

    print(
        f"Expense Amount entered: {expense_amount}"
    )

    claim_page.enter_expense_note(
        expense_note
    )

    print(
        "Expense Note entered"
    )

    claim_page.save_expense()

    print(
        "Expense saved successfully"
    )

    # =========================================================
    # ATTACHMENT
    # =========================================================

    attachment_path = create_test_attachment()

    claim_page.click_add_attachment()

    print(
        "Attachments Add button clicked"
    )

    print(
        "Add Attachment dialog opened"
    )

    # =========================================================
    # FILE
    # =========================================================

    claim_page.upload_attachment(
        attachment_path
    )

    print(
        "Attachment file selected"
    )

    # =========================================================
    # COMMENT
    # =========================================================

    claim_page.enter_attachment_comment(
        attachment_comment
    )

    print(
        "Attachment comment entered"
    )

    # =========================================================
    # SAVE ATTACHMENT
    # =========================================================

    claim_page.save_attachment()

    print(
        "Attachment saved successfully"
    )

    # =========================================================
    # FINAL SUBMIT
    # =========================================================

    claim_page.click_submit()

    print(
        "Final Submit button clicked"
    )

    # =========================================================
    # VERIFY
    # =========================================================

    assert claim_page.is_success_message_displayed(), \
        "Claim submission success message was not displayed"

    print(
        "Claim submitted successfully"
    )

    # =========================================================
    # CLEANUP
    # =========================================================

    if attachment_path and os.path.exists(
        attachment_path
    ):
        os.remove(
            attachment_path
        )