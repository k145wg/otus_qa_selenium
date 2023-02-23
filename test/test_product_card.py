from src.ProductCardPage import ProductCardPage

PAGE_NAME = "/laptop-notebook/hp-lp3065"


def test_tab_description(browser):
    productCardPage = ProductCardPage(browser)
    tab_description = productCardPage.get_tab_description()
    assert tab_description.text == "Stop your co-workers in their tracks with the stunning new 30-inch diagonal HP LP3065 Flat " \
                                   "Panel Monitor. This flagship monitor features best-in-class performance and presentation " \
                                   "features on a huge wide-aspect screen while letting you work as comfortably as possible - you " \
                                   "might even forget you're at the office"


def test_tab_specification(browser):
    productCardPage = ProductCardPage(browser)
    productCardPage.get_tab_specification()


def test_tab_review(browser):
    productCardPage = ProductCardPage(browser)
    productCardPage.get_tab_review()


def test_add_to_wish(browser):
    productCardPage = ProductCardPage(browser)
    wish = productCardPage.add_to_wish()
    assert wish.text == "You must login or create an account to save HP LP3065 to your wish list!\n×"


def test_add_to_compare(browser):
    productCardPage = ProductCardPage(browser)
    compare = productCardPage.add_to_compare()
    assert compare.text == "Success: You have added HP LP3065 to your product comparison!\n×"
