# Анализ кода модуля `test_prepeare_campaigns.py`

**Качество кода**

8
- Плюсы
    - Код хорошо структурирован и легко читается.
    - Используются фикстуры pytest для мокирования зависимостей, что упрощает тестирование.
    -  Тесты охватывают как успешные, так и неудачные сценарии.
    -  Применяется асинхронное тестирование там, где это необходимо.
- Минусы
    -  Отсутствует reStructuredText (RST) документация.
    -  Не используется `j_loads` и `j_dumps` из `src.utils.jjson`.
    -  Не импортирован `logger` из `src.logger.logger`.
    -  Присутствуют неинформативные комментарии и дублирование кода.
    -  Не используется обработка ошибок через `logger.error`.
    -  Не приведены в порядок импорты.

**Рекомендации по улучшению**

1.  **Документация**: Необходимо добавить reStructuredText (RST) документацию для модуля, классов, функций и методов.
2.  **Использование `j_loads` и `j_dumps`**: Заменить стандартные `json.load` и `json.dump` на `j_loads` и `j_dumps` из `src.utils.jjson`.
3.  **Импорт `logger`**: Добавить импорт `logger` из `src.logger.logger` и использовать его для логирования ошибок.
4.  **Обработка ошибок**: Использовать `logger.error` для обработки исключений вместо стандартных `try-except` блоков.
5.  **Улучшение комментариев**: Комментарии должны соответствовать стилю RST.
6.  **Унификация кода**: Привести импорты и имена функций в соответствие с ранее обработанными файлами.
7.  **Удаление избыточных комментариев**: Убрать избыточные комментарии, такие как дубликаты заголовков.
8.  **Проверка типов**: Использовать аннотации типов для большей читаемости и надежности кода.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль тестирования для подготовки кампаний AliExpress.
========================================================

Этот модуль содержит набор тестов для функций, используемых
для подготовки кампаний AliExpress, таких как обновление категорий,
обработка категорий кампаний и запуск основного процесса подготовки.

.. code-block:: python

    pytest src/suppliers/aliexpress/campaign/_pytest/test_prepeare_campaigns.py
"""
import pytest
import asyncio
from pathlib import Path
from unittest.mock import patch, MagicMock
from types import SimpleNamespace
from src.utils.jjson import j_loads, j_dumps
from src.logger.logger import logger  # Добавлен импорт logger
from src.utils import get_directory_names
from src.suppliers.aliexpress.campaign.prepare_campaigns import (
    update_category,
    process_campaign_category,
    process_campaign,
    main,
)




@pytest.fixture
def mock_j_loads():
    """
    Фикстура для мокирования функции `j_loads` из `src.utils.jjson`.
    """
    with patch("src.utils.jjson.j_loads") as mock:
        yield mock


@pytest.fixture
def mock_j_dumps():
    """
    Фикстура для мокирования функции `j_dumps` из `src.utils.jjson`.
    """
    with patch("src.utils.jjson.j_dumps") as mock:
        yield mock


@pytest.fixture
def mock_logger():
    """
    Фикстура для мокирования логгера.
    """
    with patch("src.logger.logger") as mock:
        yield mock


@pytest.fixture
def mock_get_directory_names():
    """
    Фикстура для мокирования функции `get_directory_names` из `src.utils`.
    """
    with patch("src.utils.get_directory_names") as mock:
        yield mock


@pytest.fixture
def mock_ali_promo_campaign():
    """
    Фикстура для мокирования класса `AliPromoCampaign` из
    `src.suppliers.aliexpress.campaign`.
    """
    with patch("src.suppliers.aliexpress.campaign.AliPromoCampaign") as mock:
        yield mock


def test_update_category_success(mock_j_loads, mock_j_dumps, mock_logger):
    """
    Тест успешного обновления категории.

    :param mock_j_loads: Мок функции `j_loads`.
    :param mock_j_dumps: Мок функции `j_dumps`.
    :param mock_logger: Мок логгера.
    """
    mock_json_path = Path("mock/path/to/category.json")
    mock_category = SimpleNamespace(name="test_category")

    mock_j_loads.return_value = {"category": {}}
    # Выполняет обновление категории
    result = update_category(mock_json_path, mock_category)

    assert result is True
    # Проверяет, что j_dumps был вызван с правильными аргументами
    mock_j_dumps.assert_called_once_with({"category": {"name": "test_category"}}, mock_json_path)
    # Проверяет, что logger.error не был вызван
    mock_logger.error.assert_not_called()


def test_update_category_failure(mock_j_loads, mock_j_dumps, mock_logger):
    """
    Тест неудачного обновления категории.

    :param mock_j_loads: Мок функции `j_loads`.
    :param mock_j_dumps: Мок функции `j_dumps`.
    :param mock_logger: Мок логгера.
    """
    mock_json_path = Path("mock/path/to/category.json")
    mock_category = SimpleNamespace(name="test_category")

    mock_j_loads.side_effect = Exception("Error")
    # Выполняет обновление категории, ожидая ошибку
    result = update_category(mock_json_path, mock_category)

    assert result is False
    # Проверяет, что j_dumps не был вызван
    mock_j_dumps.assert_not_called()
    # Проверяет, что logger.error был вызван
    mock_logger.error.assert_called_once()


@pytest.mark.asyncio
async def test_process_campaign_category_success(mock_ali_promo_campaign, mock_logger):
    """
    Тест успешной обработки категории кампании.

    :param mock_ali_promo_campaign: Мок класса `AliPromoCampaign`.
    :param mock_logger: Мок логгера.
    """
    mock_campaign_name = "test_campaign"
    mock_category_name = "test_category"
    mock_language = "EN"
    mock_currency = "USD"

    mock_ali_promo = mock_ali_promo_campaign.return_value
    mock_ali_promo.process_affiliate_products = MagicMock()
    # Выполняет обработку категории кампании
    result = await process_campaign_category(mock_campaign_name, mock_category_name, mock_language, mock_currency)

    assert result is not None
    # Проверяет, что logger.error не был вызван
    mock_logger.error.assert_not_called()


@pytest.mark.asyncio
async def test_process_campaign_category_failure(mock_ali_promo_campaign, mock_logger):
    """
    Тест неудачной обработки категории кампании.

    :param mock_ali_promo_campaign: Мок класса `AliPromoCampaign`.
    :param mock_logger: Мок логгера.
    """
    mock_campaign_name = "test_campaign"
    mock_category_name = "test_category"
    mock_language = "EN"
    mock_currency = "USD"

    mock_ali_promo = mock_ali_promo_campaign.return_value
    mock_ali_promo.process_affiliate_products.side_effect = Exception("Error")
    # Выполняет обработку категории кампании, ожидая ошибку
    result = await process_campaign_category(mock_campaign_name, mock_category_name, mock_language, mock_currency)

    assert result is None
    # Проверяет, что logger.error был вызван
    mock_logger.error.assert_called_once()


def test_process_campaign(mock_get_directory_names, mock_logger):
    """
    Тест обработки кампании.

    :param mock_get_directory_names: Мок функции `get_directory_names`.
    :param mock_logger: Мок логгера.
    """
    mock_campaign_name = "test_campaign"
    mock_categories = ["category1", "category2"]
    mock_language = "EN"
    mock_currency = "USD"
    mock_force = False

    mock_get_directory_names.return_value = mock_categories
    # Выполняет обработку кампании
    results = process_campaign(mock_campaign_name, mock_categories, mock_language, mock_currency, mock_force)

    assert len(results) == 2
    for category_name, result in results:
        assert category_name in mock_categories
        assert result is not None
    # Проверяет, что logger.warning не был вызван
    mock_logger.warning.assert_not_called()


@pytest.mark.asyncio
async def test_main(mock_get_directory_names):
    """
    Тест функции main.

    :param mock_get_directory_names: Мок функции `get_directory_names`.
    """
    mock_campaign_name = "test_campaign"
    mock_categories = ["category1", "category2"]
    mock_language = "EN"
    mock_currency = "USD"
    mock_force = False

    mock_get_directory_names.return_value = mock_categories
    # Выполняет основную функцию
    await main(mock_campaign_name, mock_categories, mock_language, mock_currency, mock_force)
    # Проверяет, что mock_get_directory_names был вызван один раз
    mock_get_directory_names.assert_called_once()