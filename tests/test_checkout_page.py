from src.page_objects.checkout_page import CheckoutPage


# Method to login in webpage and complete checkout process
def test_checkout_user(web_drivers):
    checkout_page = CheckoutPage(*web_drivers)
    checkout_page.open()
    checkout_page.login("cristinoant@hotmail.com", "qamindslab.")
    checkout_page.click_checkout()
    checkout_page.new_address()
    checkout_page.fill_items("Jose", "Perez", "QA Minds", "Calle Centro", "Mexico", "09440")
    checkout_page.continue_btn_payment()
    checkout_page.radio_btn_adress()
    checkout_page.continue_delivery_btn_method()
    checkout_page.contiue_btn_shipping_method()
    checkout_page.checkbox_agree()
    checkout_page.continue_btn_payment_method()

    # Validate the subtotal amount
    expected_subtotal = "$560.99"
    actual_subtotal = checkout_page.validate_subtotal()
    assert expected_subtotal == actual_subtotal, f"The subtotal amount should be {expected_subtotal}"

    # Validate the Total amount
    expected_total = "$565.99"
    actual_total = checkout_page.validate_total()
    assert expected_total == actual_total, f"The total amoun should be {expected_total}"

    checkout_page.confirm_order()
