from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket[type='submit']")

    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, ".alert-success:first-child")
    ITEM_TITLE = (By.CSS_SELECTOR, ".product_page h1")
    ADDED_TO_CART_ITEM_TITLE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) strong")

    MESSAGE_WITH_CART_TOTAL = (By.CSS_SELECTOR, "#messages .alert-info")
    ITEM_PRICE = (By.CSS_SELECTOR, "#content_inner .product_main .price_color")
    CART_TOTAL_PRICE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner p strong")
