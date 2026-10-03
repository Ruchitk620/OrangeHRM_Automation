import openpyxl
import pytest

from pages.login_page import LoginPage


def read_login_data():

    workbook = openpyxl.load_workbook("test_data/LoginData.xlsx")
    sheet = workbook.active

    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password, expected = row

        data.append((username, password, expected))

    workbook.close()

    return data


@pytest.mark.parametrize(
    "username,password,expected",
    read_login_data()
)
def test_login_with_multiple_credentials(driver, username, password, expected):

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(username, password)

    if expected == "PASS":

        assert login_page.is_login_successful(), \
            f"Login failed for valid user: {username}"

        print(f"Login successful for: {username}")

        login_page.logout()

    else:

        assert not login_page.is_login_successful(), \
            f"Invalid login unexpectedly succeeded for: {username}"

        print(f"Invalid login correctly rejected for: {username}")