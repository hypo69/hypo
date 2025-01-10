```python
import pytest
from unittest.mock import AsyncMock, MagicMock
from types import SimpleNamespace
import asyncio
import datetime
from src.suppliers.graber import Graber, Context, close_pop_up
from src.product.product_fields import ProductFields
from src.logger.exceptions import ExecuteLocatorException
from src import gs


# Mocking necessary modules and classes
class MockDriver:
    async def execute_locator(self, locator):
        return None
    
    def __init__(self):
       self.name = 'MockDriver'


@pytest.fixture
def mock_driver():
    return MockDriver()

@pytest.fixture
def mock_locator():
    return SimpleNamespace(
        additional_shipping_cost=SimpleNamespace(attribute='test_attribute'),
        delivery_in_stock=SimpleNamespace(attribute='test_attribute'),
        active=SimpleNamespace(attribute='test_attribute'),
        additional_delivery_times=SimpleNamespace(attribute='test_attribute'),
        advanced_stock_management=SimpleNamespace(attribute='test_attribute'),
        affiliate_short_link=SimpleNamespace(attribute='test_attribute'),
        affiliate_summary=SimpleNamespace(attribute='test_attribute'),
        affiliate_summary_2=SimpleNamespace(attribute='test_attribute'),
        affiliate_text=SimpleNamespace(attribute='test_attribute'),
        affiliate_image_large=SimpleNamespace(attribute='test_attribute'),
        affiliate_image_medium=SimpleNamespace(attribute='test_attribute'),
        affiliate_image_small=SimpleNamespace(attribute='test_attribute'),
        available_date=SimpleNamespace(attribute='test_attribute'),
        available_for_order=SimpleNamespace(attribute='test_attribute'),
        available_later=SimpleNamespace(attribute='test_attribute'),
        available_now=SimpleNamespace(attribute='test_attribute'),
        cache_default_attribute=SimpleNamespace(attribute='test_attribute'),
        cache_has_attachments=SimpleNamespace(attribute='test_attribute'),
        cache_is_pack=SimpleNamespace(attribute='test_attribute'),
        condition=SimpleNamespace(attribute='test_attribute'),
        customizable=SimpleNamespace(attribute='test_attribute'),
        date_add=SimpleNamespace(attribute='test_attribute'),
        date_upd=SimpleNamespace(attribute='test_attribute'),
        delivery_out_stock=SimpleNamespace(attribute='test_attribute'),
        depth=SimpleNamespace(attribute='test_attribute'),
        description=SimpleNamespace(attribute='test_attribute'),
        description_short=SimpleNamespace(attribute='test_attribute'),
        id_category_default=SimpleNamespace(attribute='test_attribute'),
        id_default_combination=SimpleNamespace(attribute='test_attribute'),
        id_product=SimpleNamespace(attribute='test_attribute'),
        id_default_image=SimpleNamespace(attribute='test_attribute'),
        ean13=SimpleNamespace(attribute='test_attribute'),
        ecotax=SimpleNamespace(attribute='test_attribute'),
        height=SimpleNamespace(attribute='test_attribute'),
        how_to_use=SimpleNamespace(attribute='test_attribute'),
        id_manufacturer=SimpleNamespace(attribute='test_attribute'),
        id_supplier=SimpleNamespace(attribute='test_attribute', selector='none', by='VALUE', if_list='first', use_mouse=False, mandatory=True, timeout=2, timeout_for_event='presence_of_element_located', locator_description='SKU ksp', attribute='1234'),
        id_tax=SimpleNamespace(attribute='test_attribute'),
        id_type_redirected=SimpleNamespace(attribute='test_attribute'),
        images_urls=SimpleNamespace(attribute='test_attribute'),
        indexed=SimpleNamespace(attribute='test_attribute'),
        ingredients=SimpleNamespace(attribute='test_attribute'),
        meta_description=SimpleNamespace(attribute='test_attribute'),
        meta_keywords=SimpleNamespace(attribute='test_attribute'),
        meta_title=SimpleNamespace(attribute='test_attribute'),
        is_virtual=SimpleNamespace(attribute='test_attribute'),
        isbn=SimpleNamespace(attribute='test_attribute'),
        link_rewrite=SimpleNamespace(attribute='test_attribute'),
        location=SimpleNamespace(attribute='test_attribute'),
        low_stock_alert=SimpleNamespace(attribute='test_attribute'),
        low_stock_threshold=SimpleNamespace(attribute='test_attribute'),
        minimal_quantity=SimpleNamespace(attribute='test_attribute'),
        mpn=SimpleNamespace(attribute='test_attribute'),
        name=SimpleNamespace(attribute='test_attribute'),
        online_only=SimpleNamespace(attribute='test_attribute'),
        on_sale=SimpleNamespace(attribute='test_attribute'),
        out_of_stock=SimpleNamespace(attribute='test_attribute'),
        pack_stock_type=SimpleNamespace(attribute='test_attribute'),
        price=SimpleNamespace(attribute='test_attribute'),
        product_type=SimpleNamespace(attribute='test_attribute'),
        quantity=SimpleNamespace(attribute='test_attribute'),
        quantity_discount=SimpleNamespace(attribute='test_attribute'),
        redirect_type=SimpleNamespace(attribute='test_attribute'),
        reference=SimpleNamespace(attribute='test_attribute'),
        show_condition=SimpleNamespace(attribute='test_attribute'),
        show_price=SimpleNamespace(attribute='test_attribute'),
        state=SimpleNamespace(attribute='test_attribute'),
        text_fields=SimpleNamespace(attribute='test_attribute'),
        unit_price_ratio=SimpleNamespace(attribute='test_attribute'),
        unity=SimpleNamespace(attribute='test_attribute'),
        upc=SimpleNamespace(attribute='test_attribute'),
        uploadable_files=SimpleNamespace(attribute='test_attribute'),
        default_image_url=SimpleNamespace(attribute='test_attribute'),
        visibility = SimpleNamespace(attribute='test_attribute'),
        weight = SimpleNamespace(attribute='test_attribute'),
        wholesale_price = SimpleNamespace(attribute='test_attribute'),
        width = SimpleNamespace(attribute='test_attribute'),
        specification = SimpleNamespace(attribute='test_attribute'),
        link=SimpleNamespace(attribute='test_attribute'),
        byer_protection=SimpleNamespace(attribute='test_attribute'),
        customer_reviews=SimpleNamespace(attribute='test_attribute'),
        link_to_video=SimpleNamespace(attribute='test_attribute'),
        local_image_path=SimpleNamespace(attribute='test_attribute'),
        local_video_path=SimpleNamespace(attribute='test_attribute'),
        close_pop_up=SimpleNamespace(attribute='test_attribute')
        )


@pytest.fixture
def graber_instance(mock_driver, mock_locator):
    return Graber(supplier_prefix='test', driver=mock_driver)


def test_context_attributes():
    """Проверяет установку атрибутов класса Context."""
    driver_mock = AsyncMock()
    locator_mock = SimpleNamespace()
    supplier_prefix_mock = 'test_prefix'

    Context.driver = driver_mock
    Context.locator_for_decorator = locator_mock
    Context.supplier_prefix = supplier_prefix_mock

    assert Context.driver == driver_mock
    assert Context.locator_for_decorator == locator_mock
    assert Context.supplier_prefix == supplier_prefix_mock

    # Clean up mock data
    Context.driver = None
    Context.locator_for_decorator = None
    Context.supplier_prefix = None


@pytest.mark.asyncio
async def test_close_pop_up_decorator_no_locator(graber_instance, mock_driver):
    """Проверяет работу декоратора close_pop_up, когда locator_for_decorator не установлен."""
    @close_pop_up()
    async def test_func():
        return "test_result"

    result = await test_func()
    assert result == "test_result"
    mock_driver.execute_locator.assert_not_called()


@pytest.mark.asyncio
async def test_close_pop_up_decorator_with_locator(graber_instance, mock_driver, mock_locator):
    """Проверяет работу декоратора close_pop_up с установленным locator_for_decorator."""
    Context.locator_for_decorator = mock_locator.close_pop_up
    
    @close_pop_up()
    async def test_func():
        return "test_result"
    
    result = await test_func()
    assert result == "test_result"
    mock_driver.execute_locator.assert_called_once_with(mock_locator.close_pop_up)

    # Clean up mock data
    Context.locator_for_decorator = None


@pytest.mark.asyncio
async def test_close_pop_up_decorator_exception(graber_instance, mock_driver, mock_locator):
    """Проверяет обработку исключения декоратором close_pop_up."""
    Context.locator_for_decorator = mock_locator.close_pop_up
    mock_driver.execute_locator = AsyncMock(side_effect=ExecuteLocatorException("Test Exception"))

    @close_pop_up()
    async def test_func():
        return "test_result"

    result = await test_func()
    assert result == "test_result"

    mock_driver.execute_locator.assert_called_once_with(mock_locator.close_pop_up)
    # Clean up mock data
    Context.locator_for_decorator = None



def test_graber_init(mock_driver, mock_locator):
    """Проверяет инициализацию класса Graber."""
    graber = Graber(supplier_prefix='test_supplier', driver=mock_driver)
    assert graber.supplier_prefix == 'test_supplier'
    assert isinstance(graber.locator, SimpleNamespace)
    assert graber.driver == mock_driver
    assert isinstance(graber.fields, ProductFields)
    assert Context.driver == mock_driver
    assert Context.supplier_prefix == 'test_supplier'


@pytest.mark.asyncio
async def test_set_field_value_with_value(graber_instance):
    """Проверяет функцию set_field_value, когда передано значение value."""
    result = await graber_instance.set_field_value(value='test_value', locator_func=lambda: 'locator_value', field_name='test_field')
    assert result == 'test_value'


@pytest.mark.asyncio
async def test_set_field_value_with_locator_result(graber_instance):
     """Проверяет функцию set_field_value, когда нет значения value, но есть результат локатора."""
     result = await graber_instance.set_field_value(value=None, locator_func=lambda: 'locator_value', field_name='test_field')
     assert result == 'locator_value'


@pytest.mark.asyncio
async def test_set_field_value_with_default(graber_instance):
    """Проверяет функцию set_field_value, когда нет значения и результата локатора, используется значение по умолчанию."""
    result = await graber_instance.set_field_value(value=None, locator_func=lambda: None, field_name='test_field', default='default_value')
    assert result == 'default_value'


@pytest.mark.asyncio
async def test_set_field_value_error(graber_instance, caplog):
    """Проверяет функцию set_field_value при возникновении ошибки."""
    await graber_instance.set_field_value(value=None, locator_func=lambda: None, field_name='test_field')
    assert "Ошибка заполнения поля test_field" in caplog.text


@pytest.mark.asyncio
async def test_grab_page(graber_instance, mock_locator):
     """Проверяет функцию grab_page, которая динамически вызывает другие методы."""
     graber_instance.name = AsyncMock(return_value=True)
     graber_instance.price = AsyncMock(return_value=True)
     graber_instance.description = AsyncMock(return_value=True)

     fields = await graber_instance.grab_page('name', 'price', 'description', name='test_name', price=123, description='test description' )
     
     graber_instance.name.assert_called_once_with('test_name')
     graber_instance.price.assert_called_once_with(123)
     graber_instance.description.assert_called_once_with('test description')
     assert isinstance(fields, ProductFields)


@pytest.mark.asyncio
async def test_error(graber_instance, caplog):
    """Проверяет функцию error."""
    graber_instance.error("test_field")
    assert "Ошибка заполнения поля test_field" in caplog.text


@pytest.mark.asyncio
async def test_additional_shipping_cost_with_value(graber_instance):
    """Проверяет метод additional_shipping_cost с передачей значения."""
    await graber_instance.additional_shipping_cost(value='10')
    assert graber_instance.fields.additional_shipping_cost == '10'


@pytest.mark.asyncio
async def test_additional_shipping_cost_with_locator(graber_instance, mock_driver):
    """Проверяет метод additional_shipping_cost с использованием локатора."""
    mock_driver.execute_locator = AsyncMock(return_value='20')
    await graber_instance.additional_shipping_cost()
    assert graber_instance.fields.additional_shipping_cost == '20'
    mock_driver.execute_locator.assert_called_once()


@pytest.mark.asyncio
async def test_additional_shipping_cost_exception(graber_instance, mock_driver, caplog):
    """Проверяет метод additional_shipping_cost при возникновении исключения."""
    mock_driver.execute_locator = AsyncMock(side_effect=Exception('Test Exception'))
    await graber_instance.additional_shipping_cost()
    assert "Ошибка получения значения в поле `additional_shipping_cost`" in caplog.text


@pytest.mark.asyncio
async def test_delivery_in_stock_with_value(graber_instance):
    """Проверяет метод delivery_in_stock с передачей значения."""
    await graber_instance.delivery_in_stock(value='In Stock')
    assert graber_instance.fields.delivery_in_stock == 'In Stock'


@pytest.mark.asyncio
async def test_delivery_in_stock_with_locator(graber_instance, mock_driver):
    """Проверяет метод delivery_in_stock с использованием локатора."""
    mock_driver.execute_locator = AsyncMock(return_value='Out of Stock')
    await graber_instance.delivery_in_stock()
    assert graber_instance.fields.delivery_in_stock == 'Out of Stock'
    mock_driver.execute_locator.assert_called_once()


@pytest.mark.asyncio
async def test_delivery_in_stock_exception(graber_instance, mock_driver, caplog):
    """Проверяет метод delivery_in_stock при возникновении исключения."""
    mock_driver.execute_locator = AsyncMock(side_effect=Exception('Test Exception'))
    await graber_instance.delivery_in_stock()
    assert "Ошибка получения значения в поле `delivery_in_stock`" in caplog.text

@pytest.mark.asyncio
async def test_active_with_value(graber_instance):
    """Проверяет метод active с передачей значения."""
    await graber_instance.active(value=1)
    assert graber_instance.fields.active == 1


@pytest.mark.asyncio
async def test_active_with_locator(graber_instance, mock_driver):
    """Проверяет метод active с использованием локатора."""
    mock_driver.execute_locator = AsyncMock(return_value='0')
    await graber_instance.active()
    assert graber_instance.fields.active == 0
    mock_driver.execute_locator.assert_called_once()


@pytest.mark.asyncio
async def test_active_exception(graber_instance, mock_driver, caplog):
    """Проверяет метод active при возникновении исключения."""
    mock_driver.execute_locator = AsyncMock(side_effect=Exception('Test Exception'))
    await graber_instance.active()
    assert "Ошибка получения значения в поле `active`" in caplog.text


@pytest.mark.asyncio
async def test_active_invalid_value(graber_instance, mock_driver, caplog):
    """Проверяет метод active с невалидным результатом."""
    mock_driver.execute_locator = AsyncMock(return_value=None)
    await graber_instance.active()
    assert 'Невалидный результат value=None' in caplog.text
    mock_driver.execute_locator.assert_called_once()
    assert graber_instance.fields.active is None

@pytest.mark.asyncio
async def test_additional_delivery_times_with_value(graber_instance):
    """Проверяет метод additional_delivery_times с передачей значения."""
    await graber_instance.additional_delivery_times(value='2-3 days')
    assert graber_instance.fields.additional_delivery_times == '2-3 days'


@pytest.mark.asyncio
async def test_additional_delivery_times_with_locator(graber_instance, mock_driver):
    """Проверяет метод additional_delivery_times с использованием локатора."""
    mock_driver.execute_locator = AsyncMock(return_value='1-2 weeks')
    await graber_instance.additional_delivery_times()
    assert graber_instance.fields.additional_delivery_times == '1-2 weeks'
    mock_driver.execute_locator.assert_called_once()


@pytest.mark.asyncio
async def test_additional_delivery_times_exception(graber_instance, mock_driver, caplog):
    """Проверяет метод additional_delivery_times при возникновении исключения."""
    mock_driver.execute_locator = AsyncMock(side_effect=Exception('Test Exception'))
    await graber_instance.additional_delivery_times()
    assert "Ошибка получения значения в поле `additional_delivery_times`" in caplog.text


@pytest.mark.asyncio
async def test_additional_delivery_times_invalid_value(graber_instance, mock_driver, caplog):
    """Проверяет метод additional_delivery_times с невалидным результатом."""
    mock_driver.execute_locator = AsyncMock(return_value=None)
    await graber_instance.additional_delivery_times()
    assert 'Невалидный результат value=None' in caplog.text
    mock_driver.execute_locator.assert_called_once()
    assert graber_instance.fields.additional_delivery_times is None

@pytest.mark.asyncio
async def test_advanced_stock_management_with_value(graber_instance):
    """Проверяет метод advanced_stock_management с передачей значения."""
    await graber_instance.advanced_stock_management(value='enabled')
    assert graber_instance.fields.advanced_stock_management == 'enabled'


@pytest.mark.asyncio
async def test_advanced_stock_management_with_locator(graber_instance, mock_driver):
    """Проверяет метод advanced_stock_management с использованием локатора."""
    mock_driver.execute_locator = AsyncMock(return_value='disabled')
    await graber_instance.advanced_stock_management()
    assert graber_instance.fields.advanced_stock_management == 'disabled'
    mock_driver.execute_locator.assert_called_once()


@pytest.mark.asyncio
async def test_advanced_stock_management_exception(graber_instance, mock_driver, caplog):
     """Проверяет метод advanced_stock_management при возникновении исключения."""
     mock_driver.execute_locator = AsyncMock(side_effect=Exception('Test Exception'))
     await graber_instance.advanced_stock_management()
     assert "Ошибка получения значения в поле `advanced_stock_management`" in caplog.text


@pytest.mark.asyncio
async def test_advanced_stock_management_invalid_value(graber_instance, mock_driver, caplog):
    """Проверяет метод advanced_stock_management с невалидным результатом."""
    mock_driver.execute_locator = AsyncMock(return_value=None)
    await graber_instance.advanced_stock_management()
    assert 'Невалидный результат value=None' in caplog.text
    mock_driver.execute_locator.assert_called_once()
    assert graber_instance.fields.advanced_stock_management is None


@pytest.mark.asyncio
async def test_affiliate_short_link_with_value(graber_instance):
    """Проверяет метод affiliate_short_link с передачей значения."""
    await graber_instance.affiliate_short_link(value='test_link')
    assert graber_instance.fields.affiliate_short_link == 'test_link'


@pytest.mark.asyncio
async def test_affiliate_short_link_with_locator(graber_instance, mock_driver):
    """Проверяет метод affiliate_short_link с использованием локатора."""
    mock_driver.execute_locator = AsyncMock(return_value='locator_link')
    await graber_instance.affiliate_short_link()
    assert graber_instance.fields.affiliate_short_link == 'locator_link'
    mock_driver.execute_locator.assert_called_once()


@pytest.mark.asyncio
async def test_affiliate_short_link_exception(graber_instance, mock_driver, caplog):
    """Проверяет метод affiliate_short_link при возникновении исключения."""
    mock_driver.execute_locator = AsyncMock(side_effect=Exception('Test Exception'))
    await graber_instance.affiliate_short_link()
    assert "Ошибка получения значения в поле `affiliate_short_link`" in caplog.text


@pytest.mark.asyncio
async def test_affiliate_summary_with_value(graber_instance):
    """Проверяет метод affiliate_summary с передачей значения."""
    await graber_instance.affiliate_summary(value='test_summary')
    assert graber_instance.fields.affiliate_summary == 'test_summary'


@pytest.mark.asyncio
async def test_affiliate_summary_with_locator(graber_instance, mock_driver):
    """Проверяет метод affiliate_summary с использованием локатора."""
    mock_driver.execute_locator = AsyncMock(return_value='locator_summary')
    await graber_instance.affiliate_summary()
    assert graber_instance.fields.affiliate_summary == 'locator_summary'
    mock_driver.execute_locator.assert_called_once()


@pytest.mark.asyncio
async def test_affiliate_summary_exception(graber_instance, mock_driver, caplog):
    """Проверяет метод affiliate_summary при возникновении исключения."""
    mock_driver.execute_locator = AsyncMock(side_effect=Exception('Test Exception'))
    await graber_instance.affiliate_summary()
    assert "Ошибка получения значения в поле `affiliate_summary`" in caplog.text

@pytest.mark.asyncio
async def test_affiliate_summary_2_with_value(graber_instance):
    """Проверяет метод affiliate_summary_2 с передачей значения."""
    await graber_instance.affiliate_summary_2(value='test_summary_2')
    assert graber_instance.fields.affiliate_summary_2 == 'test_summary_2'


@pytest.mark.asyncio
async def test_affiliate_summary_2_with_locator(graber_instance, mock_driver):
    """Проверяет метод affiliate_summary_2 с использованием локатора."""
    mock_driver.execute_locator = AsyncMock(return_value='locator_summary_2')
    await graber_instance.affiliate_summary_2()
    assert graber_instance.fields.affiliate_summary_2 == 'locator_summary_2'
    mock_driver.execute_locator.assert_called_once()


@pytest.mark.asyncio
async def test_affiliate_summary_2_exception(graber_instance, mock_driver, caplog):
    """Проверяет метод affiliate_summary_2 при возникновении исключения."""
    mock_driver.execute_locator = AsyncMock(side_effect=Exception('Test Exception'))
    await graber_instance.affiliate_summary_2()
    assert "Ошибка получения значения в поле `affiliate_summary_2`" in caplog.text


@pytest.mark.asyncio
async def test_affiliate_summary_2_invalid_value(graber_instance, mock_driver, caplog):
    """Проверяет метод affiliate_summary_2 с невалидным результатом."""
    mock_driver.execute_locator = AsyncMock(return_value=None)
    await graber_instance.affiliate_summary_2()
    assert 'Невалидный результат value=None' in caplog.text
    mock_driver.execute_locator.assert_called_once()
    assert graber_instance.fields.affiliate_summary_2 is None


@pytest.mark.asyncio
async def test_affiliate_text_with_value(graber_instance):
    """Проверяет метод affiliate_text с передачей значения."""
    await graber_instance.affiliate_text(value='test_text')
    assert graber_instance.fields.affiliate_text == 'test_text'


@pytest.mark.asyncio
async def test_affiliate_text_with_locator(graber_instance, mock_driver):
    """Проверяет метод affiliate_text с использованием локатора."""
    mock_driver.execute_locator = AsyncMock(return_value='locator_text')
    await graber_instance.affiliate_text()
    assert graber_instance.fields.affiliate_text == 'locator_text'
    mock_driver.execute_locator.assert_called_once()


@pytest.mark.asyncio
async def test_affiliate_text_exception(graber_instance, mock_driver, caplog):
    """Проверяет метод affiliate_text при возникновении исключения."""
    mock_driver.execute_locator = AsyncMock(side_effect=Exception('Test Exception'))
    await graber_instance.affiliate_text()
    assert "Ошибка получения значения в поле `affiliate_text`" in caplog.text


@pytest.mark.asyncio
async def test_affiliate_text_invalid_value(graber_instance, mock_driver, caplog):
    """Проверяет метод affiliate_text с невалидным результатом."""
    mock_driver.execute_locator = AsyncMock(return_value=None)
    await graber_instance.affiliate_text()
    assert 'Невалидный результат value=None' in caplog.text
    mock_driver.execute_locator.assert_called_once()
    assert graber_instance.fields.affiliate_text is None

@pytest.mark.asyncio
async def test_affiliate_image_large_with_value(graber_instance):
    """Проверяет метод affiliate_image_large с передачей значения."""
    await graber_instance.affiliate_image_large(value='test_image_url')
    assert graber_instance.fields.affiliate_image_large == 'test_image_url'


@pytest.mark.asyncio
async def test_affiliate_image_large_with_locator(graber_instance, mock_driver):
    """Проверяет метод affiliate_image_large с использованием локатора."""
    mock_driver.execute_locator = AsyncMock(return_value='locator_image_url')
    await graber_instance.affiliate_image_large()
    assert graber_instance.fields.affiliate_image_large == 'locator_image_url'
    mock_driver.execute_locator.assert_called_once()


@pytest.mark.asyncio
async def test_affiliate_image_large_exception(graber_instance, mock_driver, caplog):
     """Проверяет метод affiliate_image_large при возникновении исключения."""
     mock_driver.execute_locator = AsyncMock(side_effect=Exception('Test Exception'))
     await graber_instance.affiliate_image_large()
     assert "Ошибка получения значения в поле `affiliate_image_large`" in caplog.text



@pytest.mark.asyncio
async def test_affiliate_image_medium_with_value(graber_instance):
    """Проверяет метод affiliate_image_medium с передачей значения."""
    await graber_instance.affiliate_image_medium(value='test_image_url')
    assert graber_instance.fields.affiliate_image_medium == 'test_image_url'


@pytest.mark.asyncio
async def test_affiliate_image_medium_with_locator(graber_instance, mock_driver):
    """Проверяет метод affiliate_image_medium с использованием локатора."""
    mock_driver.execute_locator = AsyncMock(return_value='locator_image_url')
    await graber_instance.affiliate_image_medium()
    assert graber_instance.fields.affiliate_image_medium == 'locator_image_url'
    mock_driver.execute_locator.assert_called_once()


@pytest.mark.asyncio
async def test_affiliate_image_medium_exception(graber_instance, mock_driver, caplog):
     """Проверяет метод affiliate_image_medium при возникновении исключения."""
     mock_driver.execute_locator = AsyncMock(side_effect=Exception('Test Exception'))
     await graber_instance.affiliate_image_medium()
     assert "Ошибка получения значения в поле `affiliate_image_medium`" in caplog.text


@pytest.mark.asyncio
async def test_affiliate_image_medium_invalid_value(graber_instance, mock_driver, caplog):
    """Проверяет метод affiliate_image_medium с невалидным результатом."""
    mock_driver.execute_locator = AsyncMock(return_value=None)
    await graber_instance.affiliate_image_medium()
    assert 'Невалидный результат locator_result=None' in caplog.text
    mock_driver.execute_locator.assert_called_once()
    assert graber_instance.fields.affiliate_image_medium is None


@pytest.mark.asyncio
async def test_affiliate_image_small_with_value(graber_instance):
    """Проверяет метод affiliate_image_small с передачей значения."""
    await graber_instance.affiliate_image_small(value='test_image_url')
    assert graber_instance.fields.affiliate_image_small == 'test_image_url'


@pytest.mark.asyncio
async def test_affiliate_image_small_with_locator(graber_instance, mock_driver):
    """Проверяет метод affiliate_image_small с использованием локатора."""
    mock_driver.execute_locator = AsyncMock(return_value='locator_image_url')
    await graber_instance.affiliate_image_small()
    assert graber_instance.fields.affiliate_image_small == 'locator_image_url'
    mock_driver.execute_locator.assert_called_once()


@pytest.mark.asyncio
async def test_affiliate_image_small_exception(graber_instance, mock_driver, caplog):
    """Проверяет метод affiliate_image_small при возникновении исключения."""
    mock_driver.execute_locator = AsyncMock(side_effect=Exception('Test Exception'))
    await graber_instance.affiliate_image_small()
    assert "Ошибка получения значения в поле `affiliate_image_small`" in caplog.text


@pytest.mark.asyncio
async def test_affiliate_image_small_invalid_value(graber_instance, mock_driver, caplog):
    """Проверяет метод affiliate_image_small с невалидным результатом."""
    mock_driver.execute_locator = AsyncMock(return_value=None)
    await graber_instance.affiliate_image_small()
    assert 'Невалидный результат locator_result=None' in caplog.text
    mock_driver.execute_locator.assert_called_once()
    assert graber_instance.fields.affiliate_image_small is None


@pytest.mark.asyncio
async def test_available_date_with_value(graber_instance):
    """Проверяет метод available_date с передачей значения."""
    await graber_instance.available_date(value='2024-01-01')
    assert graber_instance.fields.available_date == '2024-01-01'


@pytest.mark.asyncio
async def test_available_date_with_locator(graber_instance, mock_driver):
    """Проверяет метод available_date с использованием локатора."""
    mock_driver.execute_locator = AsyncMock(return_value='2024-02-01')
    await graber_instance.available_date()
    assert graber_instance.fields.available_date == '2024-02-01'
    mock_driver.execute_locator.assert_called_once()


@pytest.mark.asyncio
async def test_available_date_exception(graber_instance, mock_driver, caplog):
    """Проверяет метод available_date при возникновении исключения."""
    mock_driver.execute_locator = AsyncMock(side_effect=Exception('Test Exception'))
    await graber_instance.available_date()
    assert "Ошибка получения значения в поле `available_date`" in caplog.text


@pytest.mark.asyncio
async def test_available_date_invalid_value(graber_instance, mock_driver, caplog):
    """Проверяет метод available_date с невалидным результатом."""
    mock_driver.execute_locator = AsyncMock(return_value=None)
    await graber_instance.available_date()
    assert 'Невалидный результат locator_result=None' in caplog.text
    mock_driver.execute_locator.assert_called_once()
    assert graber_instance.fields.available_date is None

@pytest