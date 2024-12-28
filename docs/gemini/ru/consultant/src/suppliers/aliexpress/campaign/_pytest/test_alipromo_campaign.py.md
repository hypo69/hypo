# Анализ кода модуля `test_alipromo_campaign.py`

**Качество кода**
7
- Плюсы
    - Код хорошо структурирован и разбит на отдельные тестовые функции, каждая из которых проверяет конкретную функциональность.
    - Использование фикстур `pytest` для создания экземпляра класса `AliPromoCampaign` улучшает читаемость и поддерживаемость тестов.
    - Применение `mocker` для имитации зависимостей делает тесты более изолированными и предсказуемыми.
    - Тесты покрывают основные методы класса `AliPromoCampaign`.
- Минусы
    - Отсутствует описание модуля в формате reStructuredText (RST).
    - Не все функции и методы имеют docstring в формате RST.
    - Не используется `from src.logger.logger import logger` для логирования ошибок.
    - Некоторые комментарии не соответствуют стилю RST.
    - Используются избыточные `try-except` блоки.
    - Не используется `j_loads` или `j_loads_ns` для загрузки данных в тестах, где это применимо.

**Рекомендации по улучшению**
1.  Добавить описание модуля в формате RST в начале файла.
2.  Добавить docstring в формате RST для всех тестовых функций и фикстуры.
3.  Использовать `from src.logger.logger import logger` для логирования ошибок.
4.  Избегать избыточных `try-except` блоков, использовать `logger.error` для обработки ошибок.
5.  Использовать `j_loads_ns` для загрузки данных из JSON файлов в тестах.
6.  Привести комментарии в соответствие со стилем RST.
7.  Обеспечить соответствие всех имён переменных и функций с ранее обработанными файлами.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для тестирования класса AliPromoCampaign.
=========================================================================================

Этот модуль содержит набор тестов для проверки функциональности класса :class:`AliPromoCampaign`,
который используется для управления рекламными кампаниями AliExpress.

Тесты охватывают различные аспекты, включая инициализацию кампании, обработку данных о продуктах,
создание пространств имен и сохранение данных.

:platform: Windows, Unix
:synopsis: Тесты для класса AliPromoCampaign.
"""

import pytest
from pathlib import Path
from types import SimpleNamespace
from src.suppliers.aliexpress.campaign.ali_promo_campaign import AliPromoCampaign
from src.utils.jjson import j_dumps, j_loads_ns
from src.utils.file import save_text_file
from src.logger.logger import logger
from src import gs

MODE = 'dev'

# Sample data for testing
campaign_name = "test_campaign"
category_name = "test_category"
language = "EN"
currency = "USD"

@pytest.fixture
def campaign() -> AliPromoCampaign:
    """
    Фикстура для создания экземпляра класса AliPromoCampaign.

    :return: Экземпляр класса AliPromoCampaign.
    """
    return AliPromoCampaign(campaign_name, category_name, language, currency)

def test_initialize_campaign(mocker, campaign: AliPromoCampaign):
    """
    Тест метода initialize_campaign.

    Проверяет корректность инициализации данных кампании.
    """
    mock_json_data = {
        "name": campaign_name,
        "title": "Test Campaign",
        "language": language,
        "currency": currency,
        "category": {
            category_name: {
                "name": category_name,
                "tags": "tag1, tag2",
                "products": [],
                "products_count": 0
            }
        }
    }
    #  Имитация загрузки данных из json
    mocker.patch("src.utils.jjson.j_loads_ns", return_value=SimpleNamespace(**mock_json_data))

    campaign.initialize_campaign()
    #  Проверка, что имя кампании установлено верно
    assert campaign.campaign.name == campaign_name
    #  Проверка, что имя категории установлено верно
    assert campaign.campaign.category.test_category.name == category_name

def test_get_category_products_no_json_files(mocker, campaign: AliPromoCampaign):
    """
    Тест метода get_category_products при отсутствии JSON файлов.

    Проверяет, что метод возвращает пустой список, когда нет файлов.
    """
    #  Имитация отсутствия файлов
    mocker.patch("src.utils.file.get_filenames", return_value=[])
    #  Имитация того, что нет данных о продуктах
    mocker.patch("src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.fetch_product_data", return_value=[])

    products = campaign.get_category_products(force=True)
    #  Проверка, что список продуктов пуст
    assert products == []

def test_get_category_products_with_json_files(mocker, campaign: AliPromoCampaign):
    """
    Тест метода get_category_products при наличии JSON файлов.

    Проверяет, что метод возвращает список продуктов, когда файлы есть.
    """
    mock_product_data = SimpleNamespace(product_id="123", product_title="Test Product")
    #  Имитация наличия файлов
    mocker.patch("src.utils.file.get_filenames", return_value=["product_123.json"])
    #  Имитация загрузки данных о продукте из json
    mocker.patch("src.utils.jjson.j_loads_ns", return_value=mock_product_data)

    products = campaign.get_category_products()
    #  Проверка, что список продуктов не пуст
    assert len(products) == 1
    #  Проверка идентификатора продукта
    assert products[0].product_id == "123"
    #  Проверка заголовка продукта
    assert products[0].product_title == "Test Product"

def test_create_product_namespace(campaign: AliPromoCampaign):
    """
    Тест метода create_product_namespace.

    Проверяет, что метод правильно создает пространство имен продукта.
    """
    product_data = {
        "product_id": "123",
        "product_title": "Test Product"
    }
    product = campaign.create_product_namespace(**product_data)
    #  Проверка идентификатора продукта в пространстве имен
    assert product.product_id == "123"
    #  Проверка заголовка продукта в пространстве имен
    assert product.product_title == "Test Product"

def test_create_category_namespace(campaign: AliPromoCampaign):
    """
    Тест метода create_category_namespace.

    Проверяет, что метод правильно создает пространство имен категории.
    """
    category_data = {
        "name": category_name,
        "tags": "tag1, tag2",
        "products": [],
        "products_count": 0
    }
    category = campaign.create_category_namespace(**category_data)
    #  Проверка имени категории в пространстве имен
    assert category.name == category_name
    #  Проверка тегов категории в пространстве имен
    assert category.tags == "tag1, tag2"

def test_create_campaign_namespace(campaign: AliPromoCampaign):
    """
    Тест метода create_campaign_namespace.

    Проверяет, что метод правильно создает пространство имен кампании.
    """
    campaign_data = {
        "name": campaign_name,
        "title": "Test Campaign",
        "language": language,
        "currency": currency,
        "category": SimpleNamespace()
    }
    camp = campaign.create_campaign_namespace(**campaign_data)
    #  Проверка имени кампании в пространстве имен
    assert camp.name == campaign_name
    #  Проверка заголовка кампании в пространстве имен
    assert camp.title == "Test Campaign"

def test_prepare_products(mocker, campaign: AliPromoCampaign):
    """
    Тест метода prepare_products.

    Проверяет, что метод вызывает process_affiliate_products.
    """
    #  Имитация возврата пустого списка подготовленных продуктов
    mocker.patch("src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.get_prepared_products", return_value=[])
    #  Имитация чтения исходных данных
    mocker.patch("src.utils.file.read_text_file", return_value="source_data")
    #  Имитация наличия исходного файла
    mocker.patch("src.utils.file.get_filenames", return_value=["source.html"])
    #  Имитация вызова метода обработки продуктов
    mocker.patch("src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.process_affiliate_products")

    campaign.prepare_products()
    #  Проверка, что метод обработки продуктов был вызван
    campaign.process_affiliate_products.assert_called_once()

def test_fetch_product_data(mocker, campaign: AliPromoCampaign):
    """
    Тест метода fetch_product_data.

    Проверяет, что метод возвращает данные о продуктах.
    """
    product_ids = ["123", "456"]
    mock_products = [SimpleNamespace(product_id="123"), SimpleNamespace(product_id="456")]
    #  Имитация обработки продуктов
    mocker.patch("src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.process_affiliate_products", return_value=mock_products)

    products = campaign.fetch_product_data(product_ids)
    #  Проверка количества полученных продуктов
    assert len(products) == 2
    #  Проверка идентификатора первого продукта
    assert products[0].product_id == "123"
    #  Проверка идентификатора второго продукта
    assert products[1].product_id == "456"

def test_save_product(mocker, campaign: AliPromoCampaign):
    """
    Тест метода save_product.

    Проверяет, что метод правильно сохраняет данные продукта.
    """
    product = SimpleNamespace(product_id="123", product_title="Test Product")
    #  Имитация преобразования в json
    mocker.patch("src.utils.jjson.j_dumps", return_value="{}")
    #  Имитация сохранения в файл
    mocker.patch("pathlib.Path.write_text")

    campaign.save_product(product)
    #  Проверка, что метод сохранения был вызван
    Path.write_text.assert_called_once_with("{}", encoding='utf-8')

def test_list_campaign_products(campaign: AliPromoCampaign):
    """
    Тест метода list_campaign_products.

    Проверяет, что метод правильно возвращает список заголовков продуктов.
    """
    product1 = SimpleNamespace(product_title="Product 1")
    product2 = SimpleNamespace(product_title="Product 2")
    campaign.category.products = [product1, product2]

    product_titles = campaign.list_campaign_products()
    #  Проверка списка заголовков продуктов
    assert product_titles == ["Product 1", "Product 2"]
```