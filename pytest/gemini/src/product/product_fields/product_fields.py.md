```python
import pytest
from hypotez.src.product.product_fields.product_fields import ProductFields, ProductFieldException
from sqlite3 import Date
from datetime import date as dt_date


@pytest.fixture
def product_fields():
    """Provides an instance of ProductFields for testing."""
    return ProductFields()

def test_product_fields_init(product_fields):
    """Tests the initialization of ProductFields class."""
    assert product_fields.product_fields_list is not None
    assert isinstance(product_fields.product_fields_list, list)
    assert product_fields.language == {'en': 1, 'he': 2, 'ru': 3}
    assert product_fields.presta_fields is not None
    assert product_fields.assist_fields_dict == {'default_image_url': '', 'images_urls': []}
    #check that all fields have None value
    for key in product_fields.product_fields_list:
        assert getattr(product_fields.presta_fields, key) is None

def test_load_product_fields_list(product_fields):
     """Tests the _load_product_fields_list method."""
     fields = product_fields._load_product_fields_list()
     assert isinstance(fields, list)
     assert len(fields) > 0

def test_payload_load_default_values(product_fields):
    """Tests if default values are loaded correctly"""
    assert product_fields._payload() is True
    assert hasattr(product_fields, 'active')
    assert product_fields.active == 1 # check value from json file
    assert hasattr(product_fields, 'additional_delivery_times')
    assert product_fields.additional_delivery_times is None

def test_payload_load_default_values_file_not_found(product_fields, monkeypatch):
    """Test behavior when the default values JSON file is not found."""
    def mock_j_loads(path):
        return None
    monkeypatch.setattr("hypotez.src.product.product_fields.product_fields.j_loads", mock_j_loads)

    assert product_fields._payload() is False
    
def test_associations_property(product_fields):
    """Tests the associations getter and setter."""
    assert product_fields.associations is None
    test_dict = {"categories": [1,2,3]}
    product_fields.associations = test_dict
    assert product_fields.associations == test_dict
    
def test_associations_setter_with_none(product_fields):
    """Test that `associations` can be set to `None`."""
    product_fields.associations = None
    assert product_fields.associations is None
    
def test_id_product_property(product_fields):
    """Tests the id_product getter and setter."""
    assert product_fields.id_product is None
    product_fields.id_product = 123
    assert product_fields.id_product == 123

def test_id_product_setter_with_exception(product_fields, monkeypatch):
    """Test that `id_product` can be set with error"""
    def mock_setattr(*args):
        raise ProductFieldException("Test exception")
    monkeypatch.setattr(product_fields.presta_fields, 'id_product', mock_setattr)
    
    product_fields.id_product = 123
    assert product_fields.id_product is None

def test_id_supplier_property(product_fields):
    """Tests the id_supplier getter and setter."""
    assert product_fields.id_supplier is None
    product_fields.id_supplier = 456
    assert product_fields.id_supplier == 456

def test_id_supplier_setter_with_exception(product_fields, monkeypatch):
     """Test that `id_supplier` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'id_supplier', mock_setattr)

     product_fields.id_supplier = 123
     assert product_fields.id_supplier is None

def test_id_manufacturer_property(product_fields):
    """Tests the id_manufacturer getter and setter."""
    assert product_fields.id_manufacturer is None
    product_fields.id_manufacturer = 789
    assert product_fields.id_manufacturer == 789

def test_id_manufacturer_setter_with_exception(product_fields, monkeypatch):
    """Test that `id_manufacturer` can be set with error"""
    def mock_setattr(*args):
        raise ProductFieldException("Test exception")
    monkeypatch.setattr(product_fields.presta_fields, 'id_manufacturer', mock_setattr)

    product_fields.id_manufacturer = 123
    assert product_fields.id_manufacturer is None
    
def test_id_category_default_property(product_fields):
    """Tests the id_category_default getter and setter."""
    assert product_fields.id_category_default is None
    product_fields.id_category_default = 100
    assert product_fields.id_category_default == 100

def test_id_category_default_setter_with_exception(product_fields, monkeypatch):
     """Test that `id_category_default` can be set with error"""
     def mock_setattr(*args):
         raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'id_category_default', mock_setattr)

     product_fields.id_category_default = 123
     assert product_fields.id_category_default is None

def test_additional_categories_property(product_fields):
     """Tests the additional_categories getter and setter."""
     assert product_fields.additional_categories is None
     
     product_fields.associations = {'categories': {}}

     product_fields.additional_categories = 200
     assert product_fields.additional_categories == {'id': 200}
    
     product_fields.additional_categories = [300, 400]
     assert product_fields.additional_categories == {'id': 400} #last value is assigned
    
def test_additional_categories_setter_with_wrong_type(product_fields):
    """Tests the additional_categories setter with wrong type"""
    product_fields.associations = {'categories': {}}
    product_fields.additional_categories = 'wrong type'
    assert product_fields.additional_categories is None
    

def test_additional_categories_setter_with_exception(product_fields, monkeypatch):
     """Test that `additional_categories` can be set with error"""
     def mock_update(*args):
        raise ProductFieldException("Test exception")
     product_fields.associations = {'categories': {}}
     monkeypatch.setattr(product_fields.presta_fields.associations.categories, 'update', mock_update)

     product_fields.additional_categories = 123
     assert product_fields.additional_categories is None


def test_id_shop_default_property(product_fields):
    """Tests the id_shop_default getter and setter."""
    assert product_fields.id_shop_default == ''
    product_fields.id_shop_default = 500
    assert product_fields.id_shop_default == 500

def test_id_shop_default_setter_with_exception(product_fields, monkeypatch):
     """Test that `id_shop_default` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'id_shop_default', mock_setattr)

     product_fields.id_shop_default = 123
     assert product_fields.id_shop_default == ''
     
def test_id_shop_property(product_fields):
    """Tests the id_shop getter and setter."""
    assert product_fields.id_shop == ''
    product_fields.id_shop = 500
    assert product_fields.id_shop == 500

def test_id_shop_setter_with_exception(product_fields, monkeypatch):
     """Test that `id_shop` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'id_shop', mock_setattr)

     product_fields.id_shop = 123
     assert product_fields.id_shop == ''

def test_id_tax_property(product_fields):
    """Tests the id_tax getter and setter."""
    assert product_fields.id_tax == ''
    product_fields.id_tax = 13
    assert product_fields.id_tax == 13
    
def test_id_tax_setter_with_exception(product_fields, monkeypatch):
     """Test that `id_tax` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'id_tax', mock_setattr)

     product_fields.id_tax = 123
     assert product_fields.id_tax == ''

def test_on_sale_property(product_fields):
    """Tests the on_sale getter and setter."""
    assert product_fields.on_sale == ''
    product_fields.on_sale = 1
    assert product_fields.on_sale == 1

def test_on_sale_setter_with_exception(product_fields, monkeypatch):
     """Test that `on_sale` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'on_sale', mock_setattr)

     product_fields.on_sale = 1
     assert product_fields.on_sale == ''

def test_online_only_property(product_fields):
    """Tests the online_only getter and setter."""
    assert product_fields.online_only == ''
    product_fields.online_only = 1
    assert product_fields.online_only == 1

def test_online_only_setter_with_exception(product_fields, monkeypatch):
     """Test that `online_only` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'online_only', mock_setattr)

     product_fields.online_only = 1
     assert product_fields.online_only == ''
     
def test_ean13_property(product_fields):
     """Tests the ean13 getter and setter."""
     assert product_fields.ean13 == ''
     product_fields.ean13 = '1234567890123'
     assert product_fields.ean13 == '1234567890123'

def test_ean13_setter_with_exception(product_fields, monkeypatch):
     """Test that `ean13` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'ean13', mock_setattr)

     product_fields.ean13 = '1234567890123'
     assert product_fields.ean13 == ''
     
def test_isbn_property(product_fields):
     """Tests the isbn getter and setter."""
     assert product_fields.isbn == ''
     product_fields.isbn = '978-3-16-148410-0'
     assert product_fields.isbn == '978-3-16-148410-0'

def test_isbn_setter_with_exception(product_fields, monkeypatch):
     """Test that `isbn` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'isbn', mock_setattr)

     product_fields.isbn = '978-3-16-148410-0'
     assert product_fields.isbn == ''

def test_upc_property(product_fields):
    """Tests the upc getter and setter."""
    assert product_fields.upc == ''
    product_fields.upc = '123456789012'
    assert product_fields.upc == '123456789012'

def test_upc_setter_with_exception(product_fields, monkeypatch):
     """Test that `upc` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'upc', mock_setattr)

     product_fields.upc = '123456789012'
     assert product_fields.upc == ''

def test_mpn_property(product_fields):
     """Tests the mpn getter and setter."""
     assert product_fields.mpn == ''
     product_fields.mpn = 'MPN12345'
     assert product_fields.mpn == 'MPN12345'

def test_mpn_setter_with_exception(product_fields, monkeypatch):
     """Test that `mpn` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'mpn', mock_setattr)

     product_fields.mpn = 'MPN12345'
     assert product_fields.mpn == ''

def test_ecotax_property(product_fields):
    """Tests the ecotax getter and setter."""
    assert product_fields.ecotax == ''
    product_fields.ecotax = '12.34'
    assert product_fields.ecotax == '12.34'

def test_ecotax_setter_with_exception(product_fields, monkeypatch):
     """Test that `ecotax` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'ecotax', mock_setattr)

     product_fields.ecotax = '12.34'
     assert product_fields.ecotax == ''
     
# def test_quantity_property(product_fields):
#      """Tests the quantity getter and setter."""
#      assert product_fields.quantity == None
#      product_fields.quantity = 100
#      assert product_fields.quantity == 100
     
# def test_quantity_setter_with_exception(product_fields, monkeypatch):
#      """Test that `quantity` can be set with error"""
#      def mock_setattr(*args):
#         raise ProductFieldException("Test exception")
#      monkeypatch.setattr(product_fields.presta_fields, 'quantity', mock_setattr)

#      product_fields.quantity = 100
#      assert product_fields.quantity is None

def test_minimal_quantity_property(product_fields):
    """Tests the minimal_quantity getter and setter."""
    assert product_fields.minimal_quantity == ''
    product_fields.minimal_quantity = 1
    assert product_fields.minimal_quantity == 1

def test_minimal_quantity_setter_with_exception(product_fields, monkeypatch):
     """Test that `minimal_quantity` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'minimal_quantity', mock_setattr)

     product_fields.minimal_quantity = 1
     assert product_fields.minimal_quantity == ''

def test_low_stock_threshold_property(product_fields):
     """Tests the low_stock_threshold getter and setter."""
     assert product_fields.low_stock_threshold == ''
     product_fields.low_stock_threshold = 5
     assert product_fields.low_stock_threshold == 5

def test_low_stock_threshold_setter_with_exception(product_fields, monkeypatch):
     """Test that `low_stock_threshold` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'low_stock_threshold', mock_setattr)

     product_fields.low_stock_threshold = 5
     assert product_fields.low_stock_threshold == ''

def test_low_stock_alert_property(product_fields):
    """Tests the low_stock_alert getter and setter."""
    assert product_fields.low_stock_alert == ''
    product_fields.low_stock_alert = 1
    assert product_fields.low_stock_alert == 1

def test_low_stock_alert_setter_with_exception(product_fields, monkeypatch):
     """Test that `low_stock_alert` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'low_stock_alert', mock_setattr)

     product_fields.low_stock_alert = 1
     assert product_fields.low_stock_alert == ''
     
def test_price_property(product_fields):
    """Tests the price getter and setter."""
    assert product_fields.price == 0
    product_fields.price = 123.45
    assert product_fields.price == 123.45
    product_fields.price = '123.45'
    assert product_fields.price == '123.45'
    product_fields.price = 123
    assert product_fields.price == 123
    

def test_price_setter_with_exception(product_fields, monkeypatch):
     """Test that `price` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'price', mock_setattr)

     product_fields.price = 123.45
     assert product_fields.price == 0
     
def test_wholesale_price_property(product_fields):
     """Tests the wholesale_price getter and setter."""
     assert product_fields.wholesale_price == ''
     product_fields.wholesale_price = 50.0
     assert product_fields.wholesale_price == 50.0

def test_wholesale_price_setter_with_exception(product_fields, monkeypatch):
     """Test that `wholesale_price` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'wholesale_price', mock_setattr)

     product_fields.wholesale_price = 50.0
     assert product_fields.wholesale_price == ''
     
def test_unity_property(product_fields):
    """Tests the unity getter and setter."""
    assert product_fields.unity == ''
    product_fields.unity = 'kg'
    assert product_fields.unity == 'kg'

def test_unity_setter_with_exception(product_fields, monkeypatch):
     """Test that `unity` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'unity', mock_setattr)

     product_fields.unity = 'kg'
     assert product_fields.unity == ''

def test_unit_price_ratio_property(product_fields):
     """Tests the unit_price_ratio getter and setter."""
     assert product_fields.unit_price_ratio == ''
     product_fields.unit_price_ratio = 1.5
     assert product_fields.unit_price_ratio == 1.5

def test_unit_price_ratio_setter_with_exception(product_fields, monkeypatch):
     """Test that `unit_price_ratio` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'unit_price_ratio', mock_setattr)

     product_fields.unit_price_ratio = 1.5
     assert product_fields.unit_price_ratio == ''

def test_additional_shipping_cost_property(product_fields):
    """Tests the additional_shipping_cost getter and setter."""
    assert product_fields.additional_shipping_cost == ''
    product_fields.additional_shipping_cost = 5
    assert product_fields.additional_shipping_cost == 5

def test_additional_shipping_cost_setter_with_exception(product_fields, monkeypatch):
     """Test that `additional_shipping_cost` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'additional_shipping_cost', mock_setattr)

     product_fields.additional_shipping_cost = 5
     assert product_fields.additional_shipping_cost == ''

def test_reference_property(product_fields):
    """Tests the reference getter and setter."""
    assert product_fields.reference == ''
    product_fields.reference = 'REF123'
    assert product_fields.reference == 'REF123'
    product_fields.reference = 123
    assert product_fields.reference == '123'

def test_reference_setter_with_exception(product_fields, monkeypatch):
     """Test that `reference` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'reference', mock_setattr)

     product_fields.reference = 'REF123'
     assert product_fields.reference == ''
     
def test_supplier_reference_property(product_fields):
    """Tests the supplier_reference getter and setter."""
    assert product_fields.supplier_reference == ''
    product_fields.supplier_reference = 'SUP123'
    assert product_fields.supplier_reference == 'SUP123'
    
def test_supplier_reference_setter_with_exception(product_fields, monkeypatch):
     """Test that `supplier_reference` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'supplier_reference', mock_setattr)

     product_fields.supplier_reference = 'SUP123'
     assert product_fields.supplier_reference == ''

def test_location_property(product_fields):
     """Tests the location getter and setter."""
     assert product_fields.location == ''
     product_fields.location = 'Shelf A1'
     assert product_fields.location == 'Shelf A1'

def test_location_setter_with_exception(product_fields, monkeypatch):
     """Test that `location` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'location', mock_setattr)

     product_fields.location = 'Shelf A1'
     assert product_fields.location == ''

def test_width_property(product_fields):
     """Tests the width getter and setter."""
     assert product_fields.width == ''
     product_fields.width = 10.5
     assert product_fields.width == 10.5

def test_width_setter_with_exception(product_fields, monkeypatch):
     """Test that `width` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'width', mock_setattr)

     product_fields.width = 10.5
     assert product_fields.width == ''
     
def test_height_property(product_fields):
     """Tests the height getter and setter."""
     assert product_fields.height == ''
     product_fields.height = 20.5
     assert product_fields.height == 20.5

def test_height_setter_with_exception(product_fields, monkeypatch):
     """Test that `height` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'height', mock_setattr)

     product_fields.height = 20.5
     assert product_fields.height == ''

def test_depth_property(product_fields):
     """Tests the depth getter and setter."""
     assert product_fields.depth == ''
     product_fields.depth = 30.5
     assert product_fields.depth == 30.5

def test_depth_setter_with_exception(product_fields, monkeypatch):
     """Test that `depth` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'depth', mock_setattr)

     product_fields.depth = 30.5
     assert product_fields.depth == ''
     
def test_weight_property(product_fields):
     """Tests the weight getter and setter."""
     assert product_fields.weight == ''
     product_fields.weight = 5.2
     assert product_fields.weight == 5.2

def test_weight_setter_with_exception(product_fields, monkeypatch):
     """Test that `weight` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'weight', mock_setattr)

     product_fields.weight = 5.2
     assert product_fields.weight == ''

def test_volume_property(product_fields):
     """Tests the volume getter and setter."""
     assert product_fields.volume == ''
     product_fields.volume = 10
     assert product_fields.volume == 10

def test_volume_setter_with_exception(product_fields, monkeypatch):
     """Test that `volume` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'volume', mock_setattr)

     product_fields.volume = 10
     assert product_fields.volume == ''
     
def test_out_of_stock_property(product_fields):
     """Tests the out_of_stock getter and setter."""
     assert product_fields.out_of_stock == ''
     product_fields.out_of_stock = 1
     assert product_fields.out_of_stock == 1

def test_out_of_stock_setter_with_exception(product_fields, monkeypatch):
     """Test that `out_of_stock` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'out_of_stock', mock_setattr)

     product_fields.out_of_stock = 1
     assert product_fields.out_of_stock == ''

def test_additional_delivery_times_property(product_fields):
    """Tests the additional_delivery_times getter and setter."""
    assert product_fields.additional_delivery_times == ''
    product_fields.additional_delivery_times = 1
    assert product_fields.additional_delivery_times == 1

def test_additional_delivery_times_setter_with_exception(product_fields, monkeypatch):
     """Test that `additional_delivery_times` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'additional_delivery_times', mock_setattr)

     product_fields.additional_delivery_times = 1
     assert product_fields.additional_delivery_times == ''

def test_quantity_discount_property(product_fields):
    """Tests the quantity_discount getter and setter."""
    assert product_fields.quantity_discount == ''
    product_fields.quantity_discount = 1
    assert product_fields.quantity_discount == 1
    
def test_quantity_discount_setter_with_exception(product_fields, monkeypatch):
     """Test that `quantity_discount` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'quantity_discount', mock_setattr)

     product_fields.quantity_discount = 1
     assert product_fields.quantity_discount == ''

def test_customizable_property(product_fields):
    """Tests the customizable getter and setter."""
    assert product_fields.customizable == ''
    product_fields.customizable = 1
    assert product_fields.customizable == 1
    
def test_customizable_setter_with_exception(product_fields, monkeypatch):
     """Test that `customizable` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'customizable', mock_setattr)

     product_fields.customizable = 1
     assert product_fields.customizable == ''
     
def test_uploadable_files_property(product_fields):
    """Tests the uploadable_files getter and setter."""
    assert product_fields.uploadable_files == ''
    product_fields.uploadable_files = 1
    assert product_fields.uploadable_files == 1

def test_uploadable_files_setter_with_exception(product_fields, monkeypatch):
     """Test that `uploadable_files` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'uploadable_files', mock_setattr)

     product_fields.uploadable_files = 1
     assert product_fields.uploadable_files == ''

def test_text_fields_property(product_fields):
    """Tests the text_fields getter and setter."""
    assert product_fields.text_fields == ''
    product_fields.text_fields = 1
    assert product_fields.text_fields == 1

def test_text_fields_setter_with_exception(product_fields, monkeypatch):
     """Test that `text_fields` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'text_fields', mock_setattr)

     product_fields.text_fields = 1
     assert product_fields.text_fields == ''

def test_active_property(product_fields):
    """Tests the active getter and setter."""
    assert product_fields.active == ''
    product_fields.active = 1
    assert product_fields.active == 1

def test_active_setter_with_exception(product_fields, monkeypatch):
     """Test that `active` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'active', mock_setattr)

     product_fields.active = 1
     assert product_fields.active == ''

def test_redirect_type_property(product_fields):
     """Tests the redirect_type getter and setter."""
     assert product_fields.redirect_type == ''
     product_fields.redirect_type = '404'
     assert product_fields.redirect_type == '404'
     product_fields.redirect_type = product_fields.EnumRedirect.REDIRECT_301_PRODUCT
     assert product_fields.redirect_type == '301-product'
     
def test_redirect_type_setter_with_exception(product_fields, monkeypatch):
     """Test that `redirect_type` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_fields, 'redirect_type', mock_setattr)

     product_fields.redirect_type = '404'
     assert product_fields.redirect_type == ''

def test_id_type_redirected_property(product_fields):
     """Tests the id_type_redirected getter and setter."""
     assert product_fields.id_type_redirected == ''
     product_fields.id_type_redirected = 10
     assert product_fields.id_type_redirected == 10

def test_id_type_redirected_setter_with_exception(product_fields, monkeypatch):
     """Test that `id_type_redirected` can be set with error"""
     def mock_setattr(*args):
        raise ProductFieldException("Test exception")
     monkeypatch.setattr(product_fields.presta_