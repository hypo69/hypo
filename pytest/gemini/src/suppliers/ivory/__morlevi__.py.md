```python
import pytest
from unittest.mock import MagicMock
from hypotez.src.suppliers.ivory import __morlevi__
from src.suppliers.Product import Product
import logging


# Mocking necessary external dependencies
@pytest.fixture
def mock_supplier():
    """Mocks a supplier object with necessary attributes."""
    supplier_mock = MagicMock()
    supplier_mock.driver = MagicMock()
    supplier_mock.locators = {
        'login': {
            'close_pop_up_locator': 'close_pop_up_locator',
            'open_login_dialog_locator': 'open_login_dialog_locator',
            'email_locator': 'email_locator',
            'password_locator': 'password_locator',
            'loginbutton_locator': 'loginbutton_locator'
        },
        'product':{
             'sku_locator':'sku_locator',
             'summary_locator':'summary_locator',
             'description_locator':'description_locator',
             'price_locator':'price_locator',
             'main_image_locator':'main_image_locator',
             'product_name_locator':'product_name_locator',
             'link_to_product_locator':'link_to_product_locator',
        },
        'pagination':{'a':'a'}

    }
    supplier_mock.settings = {'price_rule': '*1.1'}
    supplier_mock.supplier_prefix = 'mlv'
    supplier_mock.save_and_send_via_ftp = MagicMock()
    return supplier_mock


@pytest.fixture
def mock_product():
        """Mocks a product object with necessary attributes."""
        product_mock = MagicMock()
        product_mock.fields = {}
        return product_mock

@pytest.fixture
def mock_logger():
    """Mocks logger object """
    logger_mock = MagicMock()
    return logger_mock
@pytest.fixture
def mock_string_formatter():
    formatter_mock = MagicMock()
    formatter_mock.clear_price = MagicMock(return_value='100')
    return formatter_mock

def test_login_success(mock_supplier,monkeypatch,mock_logger):
    """Test successful login scenario."""
    monkeypatch.setattr(__morlevi__.settings,'logger',mock_logger)
    mock_supplier.driver.get_url = MagicMock(return_value=True)
    mock_supplier.driver.execute_locator = MagicMock(return_value=True)
    __morlevi__._login = MagicMock(return_value=True)
    assert __morlevi__.login(mock_supplier) == True
    mock_supplier.driver.get_url.assert_called_once()
    __morlevi__._login.assert_called_once()
def test_login_popup_close_success(mock_supplier,monkeypatch,mock_logger):
    """Test successful login scenario after closing popup."""
    monkeypatch.setattr(__morlevi__.settings,'logger',mock_logger)
    mock_supplier.driver.get_url = MagicMock(return_value=True)
    mock_supplier.driver.execute_locator = MagicMock(return_value=True)
    __morlevi__._login = MagicMock(side_effect=[False,True])
    mock_supplier.driver.page_refresh = MagicMock(return_value=True)
    mock_supplier.driver.wait = MagicMock(return_value=True)
    mock_supplier.driver.execute_locator.return_value = MagicMock( __class__ =['webelement'])
    
    assert __morlevi__.login(mock_supplier) == True
    mock_supplier.driver.get_url.assert_called_once()
    assert mock_supplier.driver.execute_locator.call_count == 1
    assert __morlevi__._login.call_count == 2


def test_login_popup_close_fail(mock_supplier,monkeypatch,mock_logger):
    """Test unsuccessful login scenario after popup close failure."""
    monkeypatch.setattr(__morlevi__.settings,'logger',mock_logger)
    mock_supplier.driver.get_url = MagicMock(return_value=True)
    mock_supplier.driver.execute_locator = MagicMock(side_effect=Exception('error'))
    mock_supplier.driver.wait = MagicMock(return_value=True)

    assert __morlevi__.login(mock_supplier) is None
    mock_supplier.driver.get_url.assert_called_once()


def test_login_fail(mock_supplier,monkeypatch,mock_logger):
    """Test unsuccessful login scenario."""
    monkeypatch.setattr(__morlevi__.settings,'logger',mock_logger)
    mock_supplier.driver.get_url = MagicMock(return_value=True)
    __morlevi__._login = MagicMock(return_value=False)
    mock_supplier.driver.page_refresh = MagicMock(return_value=True)
    mock_supplier.driver.execute_locator = MagicMock(side_effect=Exception('error'))
    assert __morlevi__.login(mock_supplier) is None
    mock_supplier.driver.get_url.assert_called_once()

def test_login_exception(mock_supplier,monkeypatch,mock_logger):
    """Test login exception handling."""
    monkeypatch.setattr(__morlevi__.settings,'logger',mock_logger)
    mock_supplier.driver.get_url = MagicMock(return_value=True)
    __morlevi__._login = MagicMock(side_effect=Exception("Test exception"))
    mock_supplier.driver.page_refresh = MagicMock(return_value=True)
    mock_supplier.driver.execute_locator = MagicMock(side_effect=Exception('error'))

    assert __morlevi__.login(mock_supplier) is None
    mock_supplier.driver.get_url.assert_called_once()


def test_grab_product_page_success(mock_supplier,monkeypatch,mock_logger, mock_string_formatter):
    """Test successful product page grabbing."""
    monkeypatch.setattr(__morlevi__.settings,'logger',mock_logger)
    monkeypatch.setattr(__morlevi__,'StringFormatter',mock_string_formatter)
    mock_supplier.driver.execute_locator = MagicMock(side_effect=['12345','test description','100,00','test title','test summary','main_image_url'])
    mock_supplier.driver.title = "Test Product Title"
    mock_supplier.driver.click = MagicMock(return_value=True)

    product = __morlevi__.grab_product_page(mock_supplier)
    assert isinstance(product, Product)
    assert product.fields['id'] == '12345'
    assert product.fields['sku suppl'] == '12345'
    assert product.fields['sku'] == 'mlv-12345'
    assert product.fields['title'] == 'Test Product Title'
    assert product.fields['summary'] == 'test summary'
    assert product.fields['meta description'] == 'test summary'
    assert product.fields['description'] == 'test description'
    assert product.fields['cost price'] == 110
    assert product.fields['price tax excluded'] == 110
    assert product.fields['img url'] == 'main_image_url'
    assert product.fields['supplier'] == '2784'
    mock_string_formatter.clear_price.assert_called_once()

def test_grab_product_page_no_price(mock_supplier,monkeypatch,mock_logger, mock_string_formatter):
    """Test product page grabbing when price is not found."""
    monkeypatch.setattr(__morlevi__.settings,'logger',mock_logger)
    monkeypatch.setattr(__morlevi__,'StringFormatter',mock_string_formatter)
    mock_supplier.driver.execute_locator = MagicMock(side_effect=['12345','test description',False,'test title','test summary','main_image_url'])
    mock_supplier.driver.title = "Test Product Title"
    mock_supplier.driver.click = MagicMock(return_value=True)


    product = __morlevi__.grab_product_page(mock_supplier)
    assert isinstance(product, Product)
    assert 'cost price' not in product.fields

def test_grab_product_page_no_images(mock_supplier,monkeypatch,mock_logger, mock_string_formatter):
    """Test product page grabbing when images are not found."""
    monkeypatch.setattr(__morlevi__.settings,'logger',mock_logger)
    monkeypatch.setattr(__morlevi__,'StringFormatter',mock_string_formatter)
    mock_supplier.driver.execute_locator = MagicMock(side_effect=['12345','test description','100,00','test title','test summary',False])
    mock_supplier.driver.title = "Test Product Title"
    mock_supplier.driver.click = MagicMock(return_value=True)


    product = __morlevi__.grab_product_page(mock_supplier)
    assert isinstance(product, Product)
    assert 'img url' not in product.fields

def test_grab_product_page_list_sku(mock_supplier,monkeypatch,mock_logger, mock_string_formatter):
        """Test successful product page grabbing."""
        monkeypatch.setattr(__morlevi__.settings,'logger',mock_logger)
        monkeypatch.setattr(__morlevi__,'StringFormatter',mock_string_formatter)
        mock_supplier.driver.execute_locator = MagicMock(side_effect=[['12345',' url '],'test description','100,00','test title','test summary','main_image_url'])
        mock_supplier.driver.title = "Test Product Title"
        mock_supplier.driver.click = MagicMock(return_value=True)

        product = __morlevi__.grab_product_page(mock_supplier)
        assert isinstance(product, Product)
        assert product.fields['id'] == '12345'
        assert product.fields['Rewritten URL'] == 'url'
        assert product.fields['sku suppl'] == '12345'
        assert product.fields['sku'] == 'mlv-12345'
        assert product.fields['title'] == 'Test Product Title'
        assert product.fields['summary'] == 'test summary'
        assert product.fields['meta description'] == 'test summary'
        assert product.fields['description'] == 'test description'
        assert product.fields['cost price'] == 110
        assert product.fields['price tax excluded'] == 110
        assert product.fields['img url'] == 'main_image_url'
        assert product.fields['supplier'] == '2784'
        mock_string_formatter.clear_price.assert_called_once()


def test_list_products_in_category_from_pagination_no_products(mock_supplier,monkeypatch,mock_logger):
    """Test when no products found in category."""
    monkeypatch.setattr(__morlevi__.settings,'logger',mock_logger)
    mock_supplier.driver.execute_locator = MagicMock(return_value=None)

    result = __morlevi__.list_products_in_category_from_pagination(mock_supplier)
    assert result == []

def test_list_products_in_category_from_pagination_single_page(mock_supplier,monkeypatch,mock_logger):
    """Test single page of products."""
    monkeypatch.setattr(__morlevi__.settings,'logger',mock_logger)
    mock_supplier.driver.execute_locator = MagicMock(side_effect=['product1_url'])
    result = __morlevi__.list_products_in_category_from_pagination(mock_supplier)
    assert result == ['product1_url']

def test_list_products_in_category_from_pagination_multi_page(mock_supplier,monkeypatch,mock_logger):
    """Test multiple pages of products."""
    monkeypatch.setattr(__morlevi__.settings,'logger',mock_logger)
    mock_supplier.driver.execute_locator = MagicMock(side_effect=[['product1_url','product2_url'],['page2'],['product3_url','product4_url']])
    mock_supplier.driver.current_url = 'test_url'
    mock_supplier.driver.click= MagicMock(side_effect=[True,False])


    result = __morlevi__.list_products_in_category_from_pagination(mock_supplier)
    assert set(result) == set(['product1_url','product2_url','product3_url','product4_url'])
def test_list_products_in_category_from_pagination_multi_page_no_new_products(mock_supplier,monkeypatch,mock_logger):
    """Test multiple pages of products, no new products in last page."""
    monkeypatch.setattr(__morlevi__.settings,'logger',mock_logger)
    mock_supplier.driver.execute_locator = MagicMock(side_effect=[['product1_url','product2_url'],['page2'],['product3_url','product4_url'],['product3_url','product4_url']])
    mock_supplier.driver.current_url = 'test_url'
    mock_supplier.driver.click= MagicMock(side_effect=[True,False])

    result = __morlevi__.list_products_in_category_from_pagination(mock_supplier)
    assert set(result) == set(['product1_url','product2_url','product3_url','product4_url'])


def test_list_products_in_category_from_pagination_single_product_per_page(mock_supplier,monkeypatch,mock_logger):
    """Test  single product per page."""
    monkeypatch.setattr(__morlevi__.settings,'logger',mock_logger)
    mock_supplier.driver.execute_locator = MagicMock(side_effect=['product1_url',['page2'],'product2_url'])
    mock_supplier.driver.current_url = 'test_url'
    mock_supplier.driver.click= MagicMock(side_effect=[True,False])


    result = __morlevi__.list_products_in_category_from_pagination(mock_supplier)
    assert set(result) == set(['product1_url','product2_url'])
def test_list_products_in_category_from_pagination_one_page_string_result(mock_supplier,monkeypatch,mock_logger):
    """Test one page products, string return."""
    monkeypatch.setattr(__morlevi__.settings,'logger',mock_logger)
    mock_supplier.driver.execute_locator = MagicMock(side_effect=['product1_url'])
    result = __morlevi__.list_products_in_category_from_pagination(mock_supplier)
    assert result == ['product1_url']

def test_get_list_products_in_category():
     """Test get_list_products_in_category function"""
     mock_supplier = MagicMock()
     scenario = {}
     presath = {}
     __morlevi__.list_products_in_category_from_pagination = MagicMock()
     __morlevi__.get_list_products_in_category(mock_supplier,scenario,presath)
     __morlevi__.list_products_in_category_from_pagination.assert_called_once()


def test_get_list_categories_from_site():
    """Test get_list_categories_from_site function"""
    mock_supplier = MagicMock()
    scenario_file = 'test'
    __morlevi__.get_list_categories_from_site(mock_supplier,scenario_file)
    ...
```