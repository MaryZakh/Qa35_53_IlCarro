from pages.login_page import LoginPage

VALID_EMAIL = "margo@gmail.com"
VALID_PASSWORD = "Mmar123456$"
INVALID_EMAIL = "margogmail.com"
INVALID_PASSWORD = "Mm123"

def test_login_success(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()
    assert login_page.confirmation_text() == "You are logged in success"
    login_page.close_window()
    assert login_page.is_logged() is True


def test_login_success_1(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.login(VALID_EMAIL,VALID_PASSWORD)
    assert login_page.confirmation_text() == "You are logged in success"
    login_page.close_window()
    assert login_page.is_logged() is True

def test_login_wrong_email(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(INVALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()

    assert login_page.error_message_text()=="Wrong email format"
    assert login_page.submit_button_disabled()

def test_login_empty_email(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email("")
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()

    assert login_page.error_message_text()=="Email is required"
    assert login_page.submit_button_disabled()

def test_login_wrong_password(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(INVALID_PASSWORD)
    login_page.submit_login()

    assert login_page.confirmation_text()== "Login failed"
    assert login_page.confirmation_text_1()== '"Login or Password incorrect"'

def test_login_empty_password(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password("")
    login_page.submit_login()

    assert login_page.error_message_text()=="Password is required"
    assert login_page.submit_button_disabled()
