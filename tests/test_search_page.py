from src.page_objects.search_page import SearchPage


def test_search_product(web_drivers):
    search_page = SearchPage(*web_drivers)
    search_page.open()

    # Find product Macbook and validate the price
    search_page.find_product_macbook()
    expected_price = "$602.00"
    search_page.validate_price_macbook()
    assert search_page.validate_price_macbook() == expected_price, "Macbook is wrong"
    search_page.back_page()

    # Find product iPhone and validate the price
    search_page.find_product_iphone()
    expected_price = "$123.20"
    search_page.validate_price_iphone()
    assert search_page.validate_price_iphone() == expected_price, "Macbook is wrong"
    search_page.back_page()

    # Find product Apple Cinmea and validate the price
    search_page.find_product_cinema()
    expected_price = "$110.00"
    search_page.validate_price_cinema()
    assert search_page.validate_price_cinema() == expected_price, "Macbook is wrong"
    search_page.back_page()

    # Find product Canon and validate the price
    search_page.find_product_canon()
    expected_price = "$198.00"
    search_page.validate_price_canon()
    assert search_page.validate_price_canon() == expected_price, "Macbook is wrong"
    search_page.back_page()
