import pytest

from .pages.product_page import ProductPage
#
# links1 = ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
#           "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"]

base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

links = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                 marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
]


@pytest.mark.parametrize('product_link', links)
@pytest.mark.skip
def test_guest_can_add_product_to_cart(browser, product_link):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_have_add_to_cart_button()
    product_page.add_item_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_have_correct_item_title_in_message()
    product_page.should_have_correct_total_price_in_message()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    product_page = ProductPage(browser, base_link)
    product_page.open()
    product_page.add_item_to_cart()
    product_page.should_not_have_success_message()

def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, base_link)
    product_page.open()
    product_page.should_not_have_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_cart(browser):
    product_page = ProductPage(browser, base_link)
    product_page.open()
    product_page.add_item_to_cart()
    product_page.should_disappear_success_message()

