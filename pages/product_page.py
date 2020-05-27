from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        add_button.click()

    def should_have_correct_total_price_in_message(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "Message about adding item to card " \
                                                                                   "is not present. "
        assert self.is_element_present(*ProductPageLocators.ITEM_PRICE), "Item price is not present."
        assert self.is_element_present(*ProductPageLocators.CART_TOTAL_PRICE), "Total price is not present."
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        card_total_price = self.browser.find_element(*ProductPageLocators.CART_TOTAL_PRICE).text
        assert item_price == card_total_price, f"Item price doesn't equal to total price in card. Expected {item_price}, got {card_total_price}. "

    def should_have_correct_item_title_in_message(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_WITH_CART_TOTAL), "Message with total price is not " \
                                                                                      "present. "
        assert self.is_element_present(*ProductPageLocators.ITEM_TITLE), "Item title is not present."
        assert self.is_element_present(*ProductPageLocators.ADDED_TO_CART_ITEM_TITLE), "Added item title is " \
                                                                                       "not present. "
        title = self.browser.find_element(*ProductPageLocators.ITEM_TITLE).text
        added_title = self.browser.find_element(*ProductPageLocators.ADDED_TO_CART_ITEM_TITLE).text
        assert title == added_title, f"Item title isn't equal to item title in card. Expected {title}, got {added_title}."

    def should_have_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_CART), "Add to card button is not present."

    def should_not_have_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), \
            "Success message is present, but should not be."

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "Success message is not disappeared, " \
                                                                               "but should be. "

