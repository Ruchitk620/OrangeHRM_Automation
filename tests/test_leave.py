from pages.login_page import LoginPage
from pages.leave_page import LeavePage


def test_assign_leave(driver):

    login_page = LoginPage(driver)
    leave_page = LeavePage(driver)

    # =========================================================
    # STEP 1: Open OrangeHRM
    # =========================================================

    login_page.open()

    # =========================================================
    # STEP 2: Login as Admin
    # =========================================================

    login_page.login(
        "Admin",
        "admin123"
    )

    assert login_page.is_login_successful(), \
        "Admin login failed"

    print("Admin login successful")

    # =========================================================
    # STEP 3: Open Leave module
    # =========================================================

    leave_page.click_leave()

    print("Leave module opened")

    # =========================================================
    # STEP 4: Open Assign Leave
    # =========================================================

    leave_page.click_assign_leave()

    print("Assign Leave page opened")

    # =========================================================
    # STEP 5: Select Employee
    # =========================================================

    leave_page.enter_employee_name("Peter")

    print(
        "Employee selected: Peter Mac Anderson"
    )

    # =========================================================
    # STEP 6: Select Leave Type
    # =========================================================

    leave_page.select_leave_type(
        "CAN - Vacation"
    )

    print(
        "Leave type selected: CAN - Vacation"
    )

    # =========================================================
    # STEP 7: Enter From Date
    # =========================================================

    leave_page.enter_from_date(
        "2026-10-05"
    )

    print(
        "From date: 2026-10-05"
    )

    # =========================================================
    # STEP 8: Enter To Date
    # =========================================================

    leave_page.enter_to_date(
        "2026-10-05"
    )

    print(
        "To date: 2026-10-05"
    )

    # =========================================================
    # STEP 9: Enter Comment / Reason
    # =========================================================

    leave_page.enter_comment(
        "GUVI automation testing"
    )

    print(
        "Comment entered"
    )

    # =========================================================
    # STEP 10: Click Assign
    # =========================================================

    leave_page.click_assign()

    print(
        "Assign button clicked"
    )

    # =========================================================
    # STEP 11: Validate Confirmation Popup
    # =========================================================

    assert leave_page.is_confirmation_popup_displayed(), \
        "Leave confirmation popup was not displayed"

    print(
        "Leave confirmation popup displayed"
    )

    # =========================================================
    # STEP 12: Confirm Assignment
    # =========================================================

    leave_page.click_popup_ok()

    print(
        "OK clicked on confirmation popup"
    )

    # =========================================================
    # STEP 13: Validate Application Response
    # =========================================================

    message = leave_page.get_success_message()

    print(
        "Application response:",
        message
    )

    # =========================================================
    # VALID APPLICATION RESPONSES
    # =========================================================

    expected_responses = (
        "Successfully",
        "Failed to Submit",
    )

    assert message.startswith(expected_responses), \
        f"Unexpected application response: {message}"