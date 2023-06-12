from src.page_objects.home_page import HomePage


# Method to find element iMac and validate the price
def test_search(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    home_page.search("iMac")
    expected_price = "$122.00"
    home_page.validate_price()
    assert home_page.validate_price() == expected_price, "iPhone price is wrong"



