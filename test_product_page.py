from .pages.product_page import ProductPage
import time

link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_guest_can_add_product_to_card(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_add_to_card_button()
    product_page.add_item_to_card()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_correct_item_title_in_message()
    product_page.should_be_correct_total_price_in_message()
