from src.page_objects.register_page import RegisterPage


# Method to register a new user
def test_register_user(web_drivers):
    expected_title = "Register Account"
    register_page = RegisterPage(*web_drivers)
    register_page.open()
    register_page.register("Lalo", "Ramirez", "jose.perez@qaminds.com", "5511223344", "qaminds", "qaminds")
    actual_title = register_page.get_title()
    assert expected_title == actual_title, f"Page title after login should be {expected_title}"


# Method to register with a email existing in System
def test_email_alredy_exist(web_drivers):
    expected_msg = "Warning: E-Mail Address is already registered!"
    register_page = RegisterPage(*web_drivers)
    register_page.open()
    register_page.email_alredy_register("Lalo", "Perez", "tester@qaminds.com", "5511223344", "qaminds", "qaminds")
    actual_msg = register_page.get_warning_message_email_already()
    assert expected_msg == actual_msg, f"Warning message should {expected_msg}"


# MethodRegister a user and don't press checkbox Privacy Policy
def test_checkbox_terms(web_drivers):
    expected_msg = "Warning: You must agree to the Privacy Policy!"
    register_page = RegisterPage(*web_drivers)
    register_page.open()
    register_page.missing_checkbox_select("Lalo", "Rojas", "tester@qaminds.com", "5511223344", "qaminds", "qaminds")
    actual_msg = register_page.get_warning_message_checkbox_select()
    assert expected_msg == actual_msg, f"Warning message should {expected_msg}"
