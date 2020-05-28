from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):

    def should_be_empty(self):
        self.should_have_no_items()
        self.should_have_message_about_empty_cart()

    def should_have_no_items(self):
        assert self.is_not_element_present(*CartPageLocators.CART_ITEMS), "Items in cart are present, but should not " \
                                                                          "be. "

    def should_have_message_about_empty_cart(self):
        assert self.is_element_present(
            *CartPageLocators.MESSAGE_ABOUT_EMPTY_CART), "Message about empty cart is not present but should be."
