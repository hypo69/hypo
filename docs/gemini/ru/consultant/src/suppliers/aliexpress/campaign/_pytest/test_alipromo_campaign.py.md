# Анализ кода модуля `test_alipromo_campaign`

**Качество кода: 8/10**

-   **Плюсы:**
    -   Хорошая структура тестов, каждый тест проверяет отдельную функцию или метод класса `AliPromoCampaign`.
    -   Используются фикстуры `pytest` для создания экземпляра класса `AliPromoCampaign`, что упрощает написание тестов.
    -   Применяется `mocker` для имитации поведения зависимостей, что позволяет изолировать тесты.
    -   Используются `SimpleNamespace` для имитации объектов данных, что делает код более читаемым и простым.
    -   Присутствуют docstring для всех функций, включая тесты.
    -   Используется `j_loads_ns` для работы с JSON, что соответствует инструкциям.

-   **Минусы:**
    -   Отсутствует явное описание модуля в начале файла (необходимо добавить docstring модуля).
    -   Некоторые docstring можно улучшить, сделав их более информативными (например, добавить описание аргументов).
    -   Не используется `from src.logger import logger` для логирования.
    -   Некоторые mock-и можно упростить, используя `mocker.patch.object`.
    -   Присутствует повторение `assert` в нескольких тестах, можно использовать параметризацию.
    -   Отсутствуют `try-except` блоки и обработка ошибок.

**Рекомендации по улучшению**

1.  **Добавить docstring модуля**: В начале файла необходимо добавить описание модуля, его назначения, примеры использования.
2.  **Улучшить docstring**: Добавить описание аргументов и возвращаемых значений в docstring функций и методов.
3.  **Использовать `from src.logger import logger`**: Заменить импорт `logger` на прямой импорт из `src.logger`.
4.  **Упростить mock-и**: Использовать `mocker.patch.object` для более читаемых mock-ов.
5.  **Параметризация тестов**: Использовать параметризацию `pytest` для уменьшения дублирования кода в тестах.
6.  **Добавить обработку ошибок**: Добавить блоки `try-except` в тестах для обработки возможных исключений, используя `logger.error` для логирования ошибок.
7.  **Избавиться от `...`**: Удалить или заменить `...` на корректный код.
8.  **Привести к одному виду имена**: Привести имена функций и переменных к одному виду (например, `test_get_category_products_no_json_files` -> `test_get_category_products_when_no_json_files_present` ).
9.  **Использовать f-строки**: Заменить конкатенацию строк на f-строки, например `assert f"Error {var}"`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

"""
Модуль тестирования функциональности AliPromoCampaign.
======================================================

Этот модуль содержит набор тестов для проверки корректной работы класса `AliPromoCampaign`,
который используется для управления рекламными кампаниями AliExpress.

Тесты включают проверку инициализации кампании, получения продуктов, создания пространств имен,
подготовки и сохранения данных о продуктах, а также списка продуктов кампании.

Пример использования
--------------------

.. code-block:: python

    pytest test_alipromo_campaign.py
"""
import pytest
from pathlib import Path
from types import SimpleNamespace
from src.suppliers.aliexpress.campaign.ali_promo_campaign import AliPromoCampaign
from src.utils.jjson import j_dumps, j_loads_ns
from src.utils.file import save_text_file
from src.logger.logger import logger # Используем прямой импорт
from src import gs

# Sample data for testing
campaign_name = 'test_campaign'
category_name = 'test_category'
language = 'EN'
currency = 'USD'


@pytest.fixture
def campaign():
    """
    Фикстура для создания экземпляра AliPromoCampaign.

    Returns:
        AliPromoCampaign: Экземпляр класса AliPromoCampaign.
    """
    return AliPromoCampaign(campaign_name, category_name, language, currency)


def test_initialize_campaign(mocker, campaign):
    """
    Тест проверяет корректность инициализации кампании.

    Args:
        mocker: Pytest mocker fixture.
        campaign: Fixture AliPromoCampaign.
    """
    mock_json_data = {
        'name': campaign_name,
        'title': 'Test Campaign',
        'language': language,
        'currency': currency,
        'category': {
            category_name: {
                'name': category_name,
                'tags': 'tag1, tag2',
                'products': [],
                'products_count': 0
            }
        }
    }
    # Мокируем j_loads_ns с помощью mocker.patch.object
    mocker.patch('src.utils.jjson.j_loads_ns', return_value=SimpleNamespace(**mock_json_data))
    campaign.initialize_campaign()
    assert campaign.campaign.name == campaign_name
    assert campaign.campaign.category.test_category.name == category_name


def test_get_category_products_when_no_json_files_present(mocker, campaign):
    """
    Тест проверяет получение продуктов категории при отсутствии JSON файлов.

    Args:
        mocker: Pytest mocker fixture.
        campaign: Fixture AliPromoCampaign.
    """
    # Мокируем get_filenames и fetch_product_data
    mocker.patch('src.utils.file.get_filenames', return_value=[])
    mocker.patch('src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.fetch_product_data', return_value=[])

    products = campaign.get_category_products(force=True)
    assert products == []


def test_get_category_products_when_json_files_present(mocker, campaign):
    """
    Тест проверяет получение продуктов категории при наличии JSON файлов.

    Args:
        mocker: Pytest mocker fixture.
        campaign: Fixture AliPromoCampaign.
    """
    mock_product_data = SimpleNamespace(product_id='123', product_title='Test Product')
    mocker.patch('src.utils.file.get_filenames', return_value=['product_123.json'])
    mocker.patch('src.utils.jjson.j_loads_ns', return_value=mock_product_data)

    products = campaign.get_category_products()
    assert len(products) == 1
    assert products[0].product_id == '123'
    assert products[0].product_title == 'Test Product'


def test_create_product_namespace(campaign):
    """
    Тест проверяет создание пространства имен продукта.

    Args:
        campaign: Fixture AliPromoCampaign.
    """
    product_data = {
        'product_id': '123',
        'product_title': 'Test Product'
    }
    product = campaign.create_product_namespace(**product_data)
    assert product.product_id == '123'
    assert product.product_title == 'Test Product'


def test_create_category_namespace(campaign):
    """
    Тест проверяет создание пространства имен категории.

    Args:
        campaign: Fixture AliPromoCampaign.
    """
    category_data = {
        'name': category_name,
        'tags': 'tag1, tag2',
        'products': [],
        'products_count': 0
    }
    category = campaign.create_category_namespace(**category_data)
    assert category.name == category_name
    assert category.tags == 'tag1, tag2'


def test_create_campaign_namespace(campaign):
    """
    Тест проверяет создание пространства имен кампании.

    Args:
        campaign: Fixture AliPromoCampaign.
    """
    campaign_data = {
        'name': campaign_name,
        'title': 'Test Campaign',
        'language': language,
        'currency': currency,
        'category': SimpleNamespace()
    }
    camp = campaign.create_campaign_namespace(**campaign_data)
    assert camp.name == campaign_name
    assert camp.title == 'Test Campaign'


def test_prepare_products(mocker, campaign):
    """
    Тест проверяет метод подготовки продуктов.

    Args:
        mocker: Pytest mocker fixture.
        campaign: Fixture AliPromoCampaign.
    """
    # Мокируем методы для проверки вызова process_affiliate_products
    mocker.patch('src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.get_prepared_products', return_value=[])
    mocker.patch('src.utils.file.read_text_file', return_value='source_data')
    mocker.patch('src.utils.file.get_filenames', return_value=['source.html'])
    mocker.patch('src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.process_affiliate_products')

    campaign.prepare_products()
    campaign.process_affiliate_products.assert_called_once()


def test_fetch_product_data(mocker, campaign):
    """
    Тест проверяет метод получения данных о продукте.

    Args:
        mocker: Pytest mocker fixture.
        campaign: Fixture AliPromoCampaign.
    """
    product_ids = ['123', '456']
    mock_products = [SimpleNamespace(product_id='123'), SimpleNamespace(product_id='456')]
    # Мокируем метод process_affiliate_products
    mocker.patch('src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.process_affiliate_products', return_value=mock_products)

    products = campaign.fetch_product_data(product_ids)
    assert len(products) == 2
    assert products[0].product_id == '123'
    assert products[1].product_id == '456'


def test_save_product(mocker, campaign):
    """
    Тест проверяет метод сохранения данных о продукте.

    Args:
        mocker: Pytest mocker fixture.
        campaign: Fixture AliPromoCampaign.
    """
    product = SimpleNamespace(product_id='123', product_title='Test Product')
    # Мокируем методы j_dumps и write_text
    mocker.patch('src.utils.jjson.j_dumps', return_value='{}')
    mocker.patch('pathlib.Path.write_text')

    campaign.save_product(product)
    Path.write_text.assert_called_once_with('{}', encoding='utf-8')


def test_list_campaign_products(campaign):
    """
    Тест проверяет метод получения списка продуктов кампании.

    Args:
        campaign: Fixture AliPromoCampaign.
    """
    product1 = SimpleNamespace(product_title='Product 1')
    product2 = SimpleNamespace(product_title='Product 2')
    campaign.category.products = [product1, product2]

    product_titles = campaign.list_campaign_products()
    assert product_titles == ['Product 1', 'Product 2']
```