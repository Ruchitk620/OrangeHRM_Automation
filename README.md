# OrangeHRM Automation Framework

## Project Overview

This project is a Selenium WebDriver automation framework developed in Python using pytest and the Page Object Model (POM) design pattern.

The framework automates key OrangeHRM web application functionalities such as authentication, dashboard/menu validation, employee information navigation, leave management, claims, user creation, and user search.

The project is designed to keep test cases separate from page-specific locators and actions, making the automation code easier to maintain and extend.

## Application Under Test

**Application:** OrangeHRM  
**URL:** https://opensource-demo.orangehrmlive.com/

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Automation Tool | Selenium WebDriver |
| Test Framework | pytest |
| Design Pattern | Page Object Model (POM) |
| Browser | Google Chrome |
| IDE | PyCharm |
| Test Data | Excel |
| Reporting | pytest-html |

## Project Structure

```text
OrangeHRM_Automation/
│
├── pages/
│   ├── __init__.py
│   ├── admin_page.py
│   ├── claim_page.py
│   ├── dashboard_page.py
│   ├── leave_page.py
│   ├── login_page.py
│   └── my_info_page.py
│
├── tests/
│   ├── __init__.py
│   ├── test_claim.py
│   ├── test_create_user.py
│   ├── test_forgot_password.py
│   ├── test_home.py
│   ├── test_leave.py
│   ├── test_login.py
│   ├── test_login_fields.py
│   ├── test_menu.py
│   ├── test_my_info.py
│   └── test_user_search.py
│
├── test_data/
│   └── LoginData.xlsx
│
├── conftest.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Test Coverage

### 1. Login Testing

The login automation covers:

- Valid login with valid credentials
- Invalid login with an incorrect password
- Invalid login with an incorrect username
- Invalid username and password combination
- Login field visibility and enabled-state validation
- Multiple login credentials using parameterized test data

### 2. Forgot Password

The forgot-password test verifies the password reset workflow from the login page.

The test navigates to the password reset page, enters the required username, submits the request, and validates the resulting application response.

### 3. Home / URL Validation

The home test verifies that the OrangeHRM application login URL is accessible.

### 4. Main Menu Validation

The framework validates that the main OrangeHRM menu items are visible and clickable, including:

- Admin
- PIM
- Leave
- Time
- Recruitment
- My Info
- Performance
- Dashboard

### 5. My Info Validation

The My Info automation validates navigation elements including:

- Personal Details
- Contact Details
- Emergency Contacts
- Dependents
- Immigration
- Job
- Salary
- Qualifications
- Memberships

### 6. Leave Management

The Leave test automates the Assign Leave workflow:

1. Login as Admin
2. Open Leave
3. Open Assign Leave
4. Select employee
5. Select leave type
6. Enter from date
7. Enter to date
8. Enter comment
9. Click Assign
10. Validate the confirmation popup
11. Confirm the operation
12. Validate the application response

The test records the actual response returned by the application, including valid business responses such as successful submission or a leave-validation rejection from the demo environment.

### 7. Claims

The Claim automation covers:

- Opening the Claim module
- Opening Submit Claim
- Selecting an event
- Selecting currency
- Entering remarks
- Creating a claim
- Adding an expense
- Entering expense information
- Adding an attachment
- Entering attachment comments
- Saving the attachment
- Submitting the claim
- Validating successful submission

### 8. User Creation

The Admin automation covers creation of a new user and validates the application's response after saving the user.

### 9. User Search

The Admin user-search automation verifies that a user can be searched and that the expected user is displayed in the user list.

## Framework Design

### Page Object Model

Each major application area has a dedicated page class under the `pages/` directory.

Examples:

- `LoginPage`
- `AdminPage`
- `DashboardPage`
- `LeavePage`
- `ClaimPage`
- `MyInfoPage`

The page classes contain:

- Element locators
- Page actions
- Synchronization logic
- Reusable validation methods

This keeps test cases focused on business flow rather than Selenium implementation details.

## Pytest Fixture

Browser setup and teardown are maintained in `conftest.py`.

The fixture is responsible for:

1. Creating the Chrome WebDriver
2. Maximizing the browser window
3. Providing the driver to tests
4. Closing the browser after test execution

## Explicit Waits

The framework uses Selenium explicit waits such as:

- `visibility_of_element_located`
- `element_to_be_clickable`
- `presence_of_element_located`

This helps synchronize automation with dynamically rendered OrangeHRM elements.

## Test Data

Login test data is maintained separately in:

`test_data/LoginData.xlsx`

This keeps the parameterized credential data separate from the test implementation.

## Installation

Clone the repository:

```bash
git clone https://github.com/Ruchitk620/OrangeHRM_Automation.git
cd OrangeHRM_Automation
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Running the Tests

Run the complete test suite:

```powershell
python -m pytest -v -s
```

Run a specific test file:

```powershell
python -m pytest -v -s tests/test_login.py
```

Run the suite with an HTML report:

```powershell
python -m pytest -v -s --html=report.html --self-contained-html
```

Or save reports under the reports directory:

```powershell
mkdir reports
python -m pytest -v -s --html=reports/report.html --self-contained-html
```

## Test Environment

| Environment Item | Value |
|---|---|
| Operating System | Windows 11 |
| Language | Python |
| Browser | Google Chrome |
| Automation | Selenium WebDriver |
| Test Runner | pytest |
| IDE | PyCharm |
| Pattern | Page Object Model |
| Report | pytest-html |

## Coding Practices

The framework follows these practices:

- Page Object Model for maintainability
- Reusable page actions
- Explicit waits for dynamic elements
- pytest fixtures for browser lifecycle
- Separate test data
- Clear test names
- Assertions for expected behavior
- Meaningful console output during execution
- Git-friendly project structure
- Generated reports and local environment files excluded through `.gitignore`

## Execution and Reporting

The final execution result should be taken from the actual test run in the local environment because the public OrangeHRM demo environment can change its state and business responses over time.

The generated HTML report provides the detailed execution result for the run.

## Known Demo Environment Considerations

This project uses the public OrangeHRM demo application. Some business workflows depend on the current state of the demo data, employee leave configuration, and application behavior.

For this reason, a functional test can reach the expected application workflow while the application itself returns a business-rule rejection. Such responses should be recorded and interpreted according to the test objective rather than being treated as successful data changes.

## Repository

GitHub repository:  
https://github.com/Ruchitk620/OrangeHRM_Automation

## Author

**Ruchit Kumar**

Python | Selenium | pytest | QA Automation
