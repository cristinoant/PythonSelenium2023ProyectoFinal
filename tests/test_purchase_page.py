import time

from src.page_objects.purchase_page import PurchasePage


# Method to valite a purchase a diferents items and add to cart
def test_purchase_items(web_drivers):
    purchase_page = PurchasePage(*web_drivers)
    purchase_page.open()
    purchase_page.login("cristinoant@hotmail.com", "qamindslab.")
    purchase_page.click_product_phones()
    purchase_page.add_to_cart_htc()
    time.sleep(1)
    purchase_page.add_to_cart_iphone()
    time.sleep(1)
    purchase_page.add_to_cart_palm()
    time.sleep(1)
    purchase_page.find_cameras()
    time.sleep(2)
    purchase_page.add_to_cart_camera()
    time.sleep(1)
    purchase_page.validate_checkout_items()
    time.sleep(1)
    purchase_page.validate_htc_in_cart()
    purchase_page.validate_palm_in_cart()
    purchase_page.validate_iphone_in_cart()
    purchase_page.validate_camera_in_cart()

    # Validate the Subtotal amount
    expected_subtotal = "$560.99"
    actual_subtotal = purchase_page.validate_subtotal()
    assert expected_subtotal == actual_subtotal, f"The subtotal amount should be {expected_subtotal}"

    # Validate the Total amount
    expected_total = "$560.99"
    actual_total = purchase_page.validate_total()
    assert expected_total == actual_total, f"The total amoun should be {expected_total}"
