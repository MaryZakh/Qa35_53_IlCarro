from pages.login_page import LoginPage

VALID_EMAIL = "margo@gmail.com"
VALID_PASSWORD = "Mmar123456$"

def test_login_success(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()
    assert login_page.login_success_text() == "You are logged in success"
    login_page.close_window()
    assert login_page.is_logged() is True


def test_login_success_1(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.login(VALID_EMAIL,VALID_PASSWORD)
    assert login_page.login_success_text() == "You are logged in success"
    login_page.close_window()
    assert login_page.is_logged() is True