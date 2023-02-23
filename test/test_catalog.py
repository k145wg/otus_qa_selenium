from src.CatalogPage import CatalogPage


def test_link(browser):
    catalogPage = CatalogPage(browser)
    link = catalogPage.get_link()
    assert link.text == 'Phones & PDAs'


def test_product_cards(browser):
    catalogPage = CatalogPage(browser)
    product_cards = catalogPage.get_product_cards()
    assert len(product_cards) == 3


def test_compare_total(browser):
    catalogPage = CatalogPage(browser)
    compare_total = catalogPage.get_compare_total()
    assert compare_total.text == 'Product Compare (0)'


def test_input_sort(browser):
    catalogPage = CatalogPage(browser)
    input_sort = catalogPage.get_input_sort()
    assert input_sort.text == "Default\nName (A - Z)\nName (Z - A)\nPrice (Low > High)\nPrice (High > Low)\nRating (" \
                              "Highest)\nRating (Lowest)\nModel (A - Z)\nModel (Z - A)"


def test_input_limit(browser):
    catalogPage = CatalogPage(browser)
    input_limit = catalogPage.get_input_limit()
    assert input_limit.text == "20\n25\n50\n75\n100"
