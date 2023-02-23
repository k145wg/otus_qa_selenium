from src.RegisterPage import RegisterPage


def test_privacy_agree(browser):
    registerPage = RegisterPage(browser)
    alert = registerPage.get_privacy_agree_alert()
    assert alert.text == 'Warning: You must agree to the Privacy Policy!'


def test_privacy_policy(browser):
    registerPage = RegisterPage(browser)
    privacy_policy_title, privacy_policy_body = registerPage.get_privacy_policy()
    assert privacy_policy_title.text == "Privacy Policy"
    assert privacy_policy_body.text == "Privacy Policy"


def test_mask_password(browser):
    registerPage = RegisterPage(browser)
    input_password = registerPage.get_password('qwerty')
    assert input_password.text == ''


def test_mask_confirm_password(browser):
    registerPage = RegisterPage(browser)
    input_password = registerPage.get_password('qwerty')
    assert input_password.text == ''


def test_mask_confirm_password(browser):
    registerPage = RegisterPage(browser)
    input_confirm_password = registerPage.get_confirm_password('qwerty')
    assert input_confirm_password.text == ''


def test_diff_pass_confirm(browser):
    registerPage = RegisterPage(browser)
    diff_pass_confirm_alert = registerPage.get_diff_pass_confirm_alert()
    assert len(diff_pass_confirm_alert) == 1
    assert diff_pass_confirm_alert[0].text == 'Password must be between 4 and 20 characters!'
    diff_pass_confirm_alert = registerPage.get_diff_pass_confirm_alert('qwerty', '123456')
    assert len(diff_pass_confirm_alert) == 1
    assert diff_pass_confirm_alert[0].text == 'Password confirmation does not match password!'
