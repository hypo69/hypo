## Анализ кода модуля `test_alipromo_campaign.py`

**Качество кода**:

- **Соответствие стандартам**: 8
- **Плюсы**:
    - Хорошее использование фикстур для подготовки тестовых данных.
    - Покрытие тестами основных методов класса `AliPromoCampaign`.
    - Применение `mocker` для изоляции зависимостей и мокирования функций.
    - Понятные и лаконичные тесты.
- **Минусы**:
    - Не везде используется `j_loads_ns` для загрузки JSON, как указано в требованиях.
    - Отсутствуют docstring у модуля и некоторых функций.
    - В коде присутствуют лишние пустые строки.
    - Есть неточности в комментариях к модулю.

**Рекомендации по улучшению**:

1. **Документирование модуля**:
    - Добавьте docstring в начале файла с описанием модуля, его назначения, и примеров использования, следуя формату RST.
    - Включите информацию о фикстурах и тестах.
2. **Использование `j_loads_ns`**:
    - Замените все стандартные `json.load` на `j_loads_ns` из `src.utils.jjson` для загрузки JSON данных.
3. **Улучшение комментариев**:
    -  Добавить rst-документацию для всех функций.
    - Избегайте неясных фраз, вроде "делаем" или "получаем", замените на более точные "проверяем", "выполняем" и т.п..
4. **Импорт logger**:
    - Добавьте импорт logger из `src.logger.logger import logger` и используйте его для логирования ошибок.
5. **Форматирование**:
    - Удалите лишние пустые строки для улучшения читаемости кода.
    - Выровняйте импорты по PEP8.
6. **Расширение тестов**:
    -  Рассмотрите добавление тестов для обработки исключительных ситуаций и граничных случаев.
7. **Исправление ошибок в комментариях**:
    -  Исправьте неточности в комментариях к модулю и удалите дубликаты.
8. **Использование f-строк**:
    -  Вместо конкатенации строк используйте f-строки для форматирования, где это уместно.

**Оптимизированный код**:

```python
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
Модуль тестирования функциональности AliPromoCampaign.
====================================================

Модуль содержит набор тестов для проверки корректности работы
класса :class:`AliPromoCampaign` из модуля `src.suppliers.aliexpress.campaign.ali_promo_campaign`.
Тесты проверяют инициализацию кампании, получение данных о продуктах,
создание namespace объектов, сохранение и вывод списка продуктов.

Фикстуры:
----------
- `campaign`: Фикстура для создания экземпляра `AliPromoCampaign` для использования в тестах.

Тесты:
------
- `test_initialize_campaign`: Проверяет корректность инициализации данных кампании.
- `test_get_category_products_no_json_files`: Проверяет `get_category_products` при отсутствии JSON файлов.
- `test_get_category_products_with_json_files`: Проверяет `get_category_products` при наличии JSON файлов.
- `test_create_product_namespace`: Проверяет корректность создания namespace продукта.
- `test_create_category_namespace`: Проверяет корректность создания namespace категории.
- `test_create_campaign_namespace`: Проверяет корректность создания namespace кампании.
- `test_prepare_products`: Проверяет, что `prepare_products` вызывает `process_affiliate_products`.
- `test_fetch_product_data`: Проверяет корректность получения данных о продуктах.
- `test_save_product`: Проверяет корректность сохранения данных о продукте.
- `test_list_campaign_products`: Проверяет корректность вывода списка заголовков продуктов кампании.

Пример использования:
---------------------
.. code-block:: python

    import pytest
    from src.suppliers.aliexpress.campaign.ali_promo_campaign import AliPromoCampaign

    @pytest.fixture
    def campaign():
        return AliPromoCampaign("test_campaign", "test_category", "EN", "USD")

    def test_example(campaign):
        assert campaign.campaign.name == "test_campaign"
"""

import pytest
from pathlib import Path
from types import SimpleNamespace
from src.suppliers.aliexpress.campaign.ali_promo_campaign import AliPromoCampaign
from src.utils.jjson import j_dumps, j_loads_ns
from src.utils.file import save_text_file
from src import gs
from src.logger.logger import logger # импортируем logger


# Sample data for testing
campaign_name = 'test_campaign' # задаём имя кампании
category_name = 'test_category' # задаём имя категории
language = 'EN' # задаём язык
currency = 'USD' # задаём валюту


@pytest.fixture
def campaign():
    """
    Фикстура для создания экземпляра AliPromoCampaign.

    :return: Экземпляр AliPromoCampaign.
    :rtype: AliPromoCampaign
    """
    return AliPromoCampaign(campaign_name, category_name, language, currency)


def test_initialize_campaign(mocker, campaign):
    """
    Тестирует метод initialize_campaign.

    Проверяет, что метод корректно инициализирует данные кампании.

    :param mocker: Объект mocker для мокирования.
    :type mocker: pytest_mock.MockerFixture
    :param campaign: Экземпляр AliPromoCampaign, созданный фикстурой.
    :type campaign: AliPromoCampaign
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
    mocker.patch('src.utils.jjson.j_loads_ns', return_value=SimpleNamespace(**mock_json_data)) # мокируем j_loads_ns

    campaign.initialize_campaign() # вызываем метод
    assert campaign.campaign.name == campaign_name # проверяем имя кампании
    assert campaign.campaign.category.test_category.name == category_name # проверяем имя категории


def test_get_category_products_no_json_files(mocker, campaign):
    """
    Тестирует метод get_category_products при отсутствии JSON файлов.

    Проверяет, что метод возвращает пустой список, когда нет файлов.

    :param mocker: Объект mocker для мокирования.
    :type mocker: pytest_mock.MockerFixture
    :param campaign: Экземпляр AliPromoCampaign, созданный фикстурой.
    :type campaign: AliPromoCampaign
    """
    mocker.patch('src.utils.file.get_filenames', return_value=[]) # мокируем get_filenames
    mocker.patch('src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.fetch_product_data', return_value=[]) # мокируем fetch_product_data

    products = campaign.get_category_products(force=True) # вызываем метод
    assert products == [] # проверяем результат


def test_get_category_products_with_json_files(mocker, campaign):
    """
    Тестирует метод get_category_products при наличии JSON файлов.

    Проверяет, что метод корректно загружает и возвращает данные о продуктах.

    :param mocker: Объект mocker для мокирования.
    :type mocker: pytest_mock.MockerFixture
    :param campaign: Экземпляр AliPromoCampaign, созданный фикстурой.
    :type campaign: AliPromoCampaign
    """
    mock_product_data = SimpleNamespace(product_id='123', product_title='Test Product')
    mocker.patch('src.utils.file.get_filenames', return_value=['product_123.json']) # мокируем get_filenames
    mocker.patch('src.utils.jjson.j_loads_ns', return_value=mock_product_data) # мокируем j_loads_ns

    products = campaign.get_category_products() # вызываем метод
    assert len(products) == 1 # проверяем кол-во продуктов
    assert products[0].product_id == '123' # проверяем id продукта
    assert products[0].product_title == 'Test Product' # проверяем заголовок продукта


def test_create_product_namespace(campaign):
    """
    Тестирует метод create_product_namespace.

    Проверяет, что метод корректно создает namespace продукта.

    :param campaign: Экземпляр AliPromoCampaign, созданный фикстурой.
    :type campaign: AliPromoCampaign
    """
    product_data = {
        'product_id': '123',
        'product_title': 'Test Product'
    }
    product = campaign.create_product_namespace(**product_data) # вызываем метод
    assert product.product_id == '123' # проверяем id продукта
    assert product.product_title == 'Test Product' # проверяем заголовок продукта


def test_create_category_namespace(campaign):
    """
    Тестирует метод create_category_namespace.

    Проверяет, что метод корректно создает namespace категории.

    :param campaign: Экземпляр AliPromoCampaign, созданный фикстурой.
    :type campaign: AliPromoCampaign
    """
    category_data = {
        'name': category_name,
        'tags': 'tag1, tag2',
        'products': [],
        'products_count': 0
    }
    category = campaign.create_category_namespace(**category_data) # вызываем метод
    assert category.name == category_name # проверяем имя категории
    assert category.tags == 'tag1, tag2' # проверяем теги категории


def test_create_campaign_namespace(campaign):
    """
    Тестирует метод create_campaign_namespace.

    Проверяет, что метод корректно создает namespace кампании.

    :param campaign: Экземпляр AliPromoCampaign, созданный фикстурой.
    :type campaign: AliPromoCampaign
    """
    campaign_data = {
        'name': campaign_name,
        'title': 'Test Campaign',
        'language': language,
        'currency': currency,
        'category': SimpleNamespace()
    }
    camp = campaign.create_campaign_namespace(**campaign_data) # вызываем метод
    assert camp.name == campaign_name # проверяем имя кампании
    assert camp.title == 'Test Campaign' # проверяем заголовок кампании


def test_prepare_products(mocker, campaign):
    """
    Тестирует метод prepare_products.

    Проверяет, что метод вызывает process_affiliate_products.

    :param mocker: Объект mocker для мокирования.
    :type mocker: pytest_mock.MockerFixture
    :param campaign: Экземпляр AliPromoCampaign, созданный фикстурой.
    :type campaign: AliPromoCampaign
    """
    mocker.patch('src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.get_prepared_products', return_value=[]) # мокируем get_prepared_products
    mocker.patch('src.utils.file.read_text_file', return_value='source_data') # мокируем read_text_file
    mocker.patch('src.utils.file.get_filenames', return_value=['source.html']) # мокируем get_filenames
    mocker.patch('src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.process_affiliate_products') # мокируем process_affiliate_products

    campaign.prepare_products() # вызываем метод
    campaign.process_affiliate_products.assert_called_once() # проверяем, что метод был вызван


def test_fetch_product_data(mocker, campaign):
    """
    Тестирует метод fetch_product_data.

    Проверяет, что метод корректно получает данные о продуктах.

    :param mocker: Объект mocker для мокирования.
    :type mocker: pytest_mock.MockerFixture
    :param campaign: Экземпляр AliPromoCampaign, созданный фикстурой.
    :type campaign: AliPromoCampaign
    """
    product_ids = ['123', '456']
    mock_products = [SimpleNamespace(product_id='123'), SimpleNamespace(product_id='456')]
    mocker.patch('src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.process_affiliate_products', return_value=mock_products) # мокируем process_affiliate_products

    products = campaign.fetch_product_data(product_ids) # вызываем метод
    assert len(products) == 2 # проверяем кол-во продуктов
    assert products[0].product_id == '123' # проверяем id продукта
    assert products[1].product_id == '456' # проверяем id продукта


def test_save_product(mocker, campaign):
    """
    Тестирует метод save_product.

    Проверяет, что метод корректно сохраняет данные о продукте.

    :param mocker: Объект mocker для мокирования.
    :type mocker: pytest_mock.MockerFixture
    :param campaign: Экземпляр AliPromoCampaign, созданный фикстурой.
    :type campaign: AliPromoCampaign
    """
    product = SimpleNamespace(product_id='123', product_title='Test Product')
    mocker.patch('src.utils.jjson.j_dumps', return_value='{}') # мокируем j_dumps
    mocker.patch('pathlib.Path.write_text') # мокируем write_text

    campaign.save_product(product) # вызываем метод
    Path.write_text.assert_called_once_with('{}', encoding='utf-8') # проверяем, что метод был вызван


def test_list_campaign_products(campaign):
    """
    Тестирует метод list_campaign_products.

    Проверяет, что метод корректно выводит список заголовков продуктов.

    :param campaign: Экземпляр AliPromoCampaign, созданный фикстурой.
    :type campaign: AliPromoCampaign
    """
    product1 = SimpleNamespace(product_title='Product 1')
    product2 = SimpleNamespace(product_title='Product 2')
    campaign.category.products = [product1, product2] # задаем продукты

    product_titles = campaign.list_campaign_products() # вызываем метод
    assert product_titles == ['Product 1', 'Product 2'] # проверяем результат