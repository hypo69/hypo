# Анализ кода модуля `test_alipromo_campaign`

**Качество кода: 8/10**

*   **Плюсы:**
    *   Код хорошо структурирован и разбит на отдельные тесты для каждой функции класса `AliPromoCampaign`.
    *   Используются фикстуры для создания экземпляра класса `AliPromoCampaign`, что упрощает написание тестов.
    *   Используется `mocker` для имитации внешних зависимостей, что делает тесты изолированными и надежными.
    *   Тесты покрывают основные методы класса, включая инициализацию, обработку продуктов и сохранение данных.
    *   Для сравнения ожидаемых и фактических значений используются `assert`, что упрощает проверку результатов тестов.
    *   Имена тестов соответствуют именам тестируемых методов, что упрощает понимание их назначения.

*   **Минусы:**
    *   Отсутствует документация в формате RST для модуля, классов и методов.
    *   Используется `SimpleNamespace` для создания тестовых данных, что может быть заменено на более явное представление данных.
    *   Некоторые тесты могут быть более подробными, например, проверять не только длину списка, но и его содержимое.
    *   Не используется логирование ошибок, что затрудняет отладку в случае проблем.
    *   Не все моки используют `assert_called_once()`, что снижает уверенность в правильности имитации.

**Рекомендации по улучшению:**

1.  **Добавить reStructuredText (RST) документацию:**
    *   Добавить docstring для модуля в начале файла.
    *   Добавить docstring для всех функций и методов, описывая их назначение, параметры и возвращаемые значения.

2.  **Улучшить использование `SimpleNamespace`:**
    *   Рассмотреть возможность использования словарей для представления данных, что может сделать код более читаемым.

3.  **Расширить тестовое покрытие:**
    *   Добавить более подробные проверки для списков продуктов, проверяя не только их длину, но и содержимое.
    *   Добавить тесты для обработки граничных случаев и ошибок.

4.  **Использовать логирование:**
    *   Добавить логирование ошибок с помощью `logger.error` вместо стандартных блоков `try-except`.

5.  **Добавить проверки вызовов моков:**
    *   Использовать `assert_called_once()` для всех моков, где это необходимо.

6.  **Переименовать переменные для большей читаемости:**
    *   Использовать более описательные имена переменных.

**Оптимизированный код:**

```python
# -*- coding: utf-8 -*-
"""
Модуль содержит тесты для проверки функциональности класса AliPromoCampaign.
==========================================================================

Этот модуль использует pytest для тестирования методов класса AliPromoCampaign,
включая инициализацию, получение и обработку данных о продуктах.

Пример использования
--------------------

Для запуска тестов:

.. code-block:: bash

    pytest test_alipromo_campaign.py

"""
import pytest
from pathlib import Path
from types import SimpleNamespace
#from src.suppliers.aliexpress.campaign.ali_promo_campaign import AliPromoCampaign # исправлено в соответствии с другими файлами
from src.suppliers.aliexpress.campaign.ali_promo_campaign import AliPromoCampaign
from src.utils.jjson import j_dumps, j_loads_ns
from src.utils.file import save_text_file
from src.logger.logger import logger
from src import gs


# Sample data for testing
campaign_name = 'test_campaign'
category_name = 'test_category'
language = 'EN'
currency = 'USD'


@pytest.fixture
def campaign():
    """
    Фикстура для создания экземпляра класса AliPromoCampaign.

    :return: Экземпляр класса AliPromoCampaign.
    """
    return AliPromoCampaign(campaign_name, category_name, language, currency)


def test_initialize_campaign(mocker, campaign):
    """
    Тест метода initialize_campaign.

    Проверяет, что метод корректно инициализирует данные кампании.

    :param mocker: Mocker fixture для имитации зависимостей.
    :param campaign: Фикстура с экземпляром AliPromoCampaign.
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
    # Мокирование функции j_loads_ns, чтобы вернуть тестовые данные
    mocker.patch('src.utils.jjson.j_loads_ns', return_value=SimpleNamespace(**mock_json_data))

    campaign.initialize_campaign()
    # Проверка корректности инициализации данных кампании
    assert campaign.campaign.name == campaign_name
    assert campaign.campaign.category.test_category.name == category_name


def test_get_category_products_no_json_files(mocker, campaign):
    """
    Тест метода get_category_products при отсутствии JSON файлов.

    Проверяет, что метод возвращает пустой список, если нет файлов с данными о продуктах.

    :param mocker: Mocker fixture для имитации зависимостей.
    :param campaign: Фикстура с экземпляром AliPromoCampaign.
    """
    # Мокирование функции get_filenames, чтобы вернуть пустой список
    mocker.patch('src.utils.file.get_filenames', return_value=[])
    # Мокирование метода fetch_product_data, чтобы вернуть пустой список
    mocker.patch('src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.fetch_product_data', return_value=[])

    # Вызов метода get_category_products и проверка результата
    products = campaign.get_category_products(force=True)
    assert products == []


def test_get_category_products_with_json_files(mocker, campaign):
    """
    Тест метода get_category_products при наличии JSON файлов.

    Проверяет, что метод корректно загружает данные о продуктах из JSON файлов.

    :param mocker: Mocker fixture для имитации зависимостей.
    :param campaign: Фикстура с экземпляром AliPromoCampaign.
    """
    mock_product_data = SimpleNamespace(product_id='123', product_title='Test Product')
    # Мокирование функции get_filenames, чтобы вернуть список с именем файла
    mocker.patch('src.utils.file.get_filenames', return_value=['product_123.json'])
     # Мокирование функции j_loads_ns, чтобы вернуть тестовые данные о продукте
    mocker.patch('src.utils.jjson.j_loads_ns', return_value=mock_product_data)

    # Вызов метода get_category_products и проверка результата
    products = campaign.get_category_products()
    assert len(products) == 1
    assert products[0].product_id == '123'
    assert products[0].product_title == 'Test Product'


def test_create_product_namespace(campaign):
    """
    Тест метода create_product_namespace.

    Проверяет, что метод корректно создает пространство имен для продукта.

    :param campaign: Фикстура с экземпляром AliPromoCampaign.
    """
    product_data = {
        'product_id': '123',
        'product_title': 'Test Product'
    }
    # Вызов метода create_product_namespace и проверка результата
    product = campaign.create_product_namespace(**product_data)
    assert product.product_id == '123'
    assert product.product_title == 'Test Product'


def test_create_category_namespace(campaign):
    """
    Тест метода create_category_namespace.

    Проверяет, что метод корректно создает пространство имен для категории.

    :param campaign: Фикстура с экземпляром AliPromoCampaign.
    """
    category_data = {
        'name': category_name,
        'tags': 'tag1, tag2',
        'products': [],
        'products_count': 0
    }
    # Вызов метода create_category_namespace и проверка результата
    category = campaign.create_category_namespace(**category_data)
    assert category.name == category_name
    assert category.tags == 'tag1, tag2'


def test_create_campaign_namespace(campaign):
    """
    Тест метода create_campaign_namespace.

    Проверяет, что метод корректно создает пространство имен для кампании.

    :param campaign: Фикстура с экземпляром AliPromoCampaign.
    """
    campaign_data = {
        'name': campaign_name,
        'title': 'Test Campaign',
        'language': language,
        'currency': currency,
        'category': SimpleNamespace()
    }
    # Вызов метода create_campaign_namespace и проверка результата
    camp = campaign.create_campaign_namespace(**campaign_data)
    assert camp.name == campaign_name
    assert camp.title == 'Test Campaign'


def test_prepare_products(mocker, campaign):
    """
    Тест метода prepare_products.

    Проверяет, что метод вызывает process_affiliate_products.

    :param mocker: Mocker fixture для имитации зависимостей.
    :param campaign: Фикстура с экземпляром AliPromoCampaign.
    """
    # Мокирование метода get_prepared_products, чтобы вернуть пустой список
    mocker.patch('src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.get_prepared_products', return_value=[])
     # Мокирование функции read_text_file, чтобы вернуть тестовые данные
    mocker.patch('src.utils.file.read_text_file', return_value='source_data')
    # Мокирование функции get_filenames, чтобы вернуть список с именем файла
    mocker.patch('src.utils.file.get_filenames', return_value=['source.html'])
    # Мокирование метода process_affiliate_products
    mocker.patch('src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.process_affiliate_products')

    campaign.prepare_products()
    # Проверка, что метод process_affiliate_products был вызван
    campaign.process_affiliate_products.assert_called_once()


def test_fetch_product_data(mocker, campaign):
    """
    Тест метода fetch_product_data.

    Проверяет, что метод корректно обрабатывает данные продуктов.

    :param mocker: Mocker fixture для имитации зависимостей.
    :param campaign: Фикстура с экземпляром AliPromoCampaign.
    """
    product_ids = ['123', '456']
    mock_products = [SimpleNamespace(product_id='123'), SimpleNamespace(product_id='456')]
     # Мокирование метода process_affiliate_products, чтобы вернуть список тестовых продуктов
    mocker.patch('src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.process_affiliate_products', return_value=mock_products)

    # Вызов метода fetch_product_data и проверка результата
    products = campaign.fetch_product_data(product_ids)
    assert len(products) == 2
    assert products[0].product_id == '123'
    assert products[1].product_id == '456'


def test_save_product(mocker, campaign):
    """
    Тест метода save_product.

    Проверяет, что метод корректно сохраняет данные продукта.

    :param mocker: Mocker fixture для имитации зависимостей.
    :param campaign: Фикстура с экземпляром AliPromoCampaign.
    """
    product = SimpleNamespace(product_id='123', product_title='Test Product')
     # Мокирование функции j_dumps, чтобы вернуть тестовые данные
    mocker.patch('src.utils.jjson.j_dumps', return_value='{}')
     # Мокирование метода write_text класса Path
    mocker.patch('pathlib.Path.write_text')

    campaign.save_product(product)
    # Проверка, что метод write_text был вызван с ожидаемыми аргументами
    Path.write_text.assert_called_once_with('{}', encoding='utf-8')


def test_list_campaign_products(campaign):
    """
    Тест метода list_campaign_products.

    Проверяет, что метод корректно возвращает список заголовков продуктов.

    :param campaign: Фикстура с экземпляром AliPromoCampaign.
    """
    product1 = SimpleNamespace(product_title='Product 1')
    product2 = SimpleNamespace(product_title='Product 2')
    campaign.category.products = [product1, product2]

    # Вызов метода list_campaign_products и проверка результата
    product_titles = campaign.list_campaign_products()
    assert product_titles == ['Product 1', 'Product 2']
```