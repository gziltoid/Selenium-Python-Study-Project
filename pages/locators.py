from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CLASS_NAME, "icon-user")
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class CartPageLocators:
    CART_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    MESSAGE_ABOUT_EMPTY_CART = (By.CSS_SELECTOR, "#content_inner>p")


class ProductPageLocators:
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket[type='submit']")

    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, ".alert-success:first-child")
    ITEM_TITLE = (By.CSS_SELECTOR, ".product_page h1")
    ADDED_TO_CART_ITEM_TITLE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) strong")

    MESSAGE_WITH_CART_TOTAL = (By.CSS_SELECTOR, "#messages .alert-info")
    ITEM_PRICE = (By.CSS_SELECTOR, "#content_inner .product_main .price_color")
    CART_TOTAL_PRICE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner p strong")
