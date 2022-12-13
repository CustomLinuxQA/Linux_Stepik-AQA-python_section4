import pytest

from pages.product_page import ProductPage
from pages.test_link import ProductTestLink


@pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
def test_guest_can_open_product_page(browser, test_link):
    page = ProductPage(browser,
                       test_link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()  # открываем страницу
    page.should_be_product_url()  # проверка url


@pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
def test_guest_can_add_product_to_basket(browser, test_link):
    page = ProductPage(browser, test_link)
    page.open()
    page.add_item_to_basket()  # Проверка добавления товара в корзину.


@pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
def test_guest_can_see_added_item_in_notification(browser, test_link):
    page = ProductPage(browser, test_link)
    page.open()
    page.excepted_item_name_in_notification()  # Проверка соответствия названия товара в уведомлении.


@pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
def test_guest_can_see_total_price_in_notification(browser, test_link):
    page = ProductPage(browser, test_link)
    page.open()
    page.should_be_correct_total_price_notification()  # Проверка соответствия цены товара в уведомлении.


@pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
def test_guest_can_see_total_price_of_items(browser, test_link):
    page = ProductPage(browser, test_link)
    page.open()
    page.excepted_total_price_of_items()  # Стоимость корзины совпадает с ценой товара.

@pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, test_link):
    page = ProductPage(browser, test_link)
    page.open()
    page.add_item_to_basket()
    page.should_not_be_success_message()

@pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
def test_guest_cant_see_success_message(browser, test_link):
    page = ProductPage(browser, test_link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, test_link):
    page = ProductPage(browser, test_link)
    page.open()
    page.add_item_to_basket()
    page.should_be_disappeared()

@pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
def test_guest_should_see_login_link_on_product_page(browser, test_link):
    page = ProductPage(browser, test_link)
    page.open()
    page.should_be_login_link()

@pytest.mark.parametrize("test_link", ProductTestLink.TEST_LINK)
def test_guest_can_go_to_login_page_from_product_page(browser, test_link):
    page = ProductPage(browser, test_link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_form()
    page.should_be_register_form()
