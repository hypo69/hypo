## Анализ кода модуля `test_prepeare_campaigns.py`

**Качество кода**
8
-   Плюсы
    -   Код хорошо структурирован и разбит на отдельные тестовые функции, что облегчает понимание и поддержку.
    -   Используются фикстуры pytest для мокирования зависимостей, что делает тесты более изолированными и управляемыми.
    -   Присутствуют тесты для позитивных и негативных сценариев (успех и ошибка) для большинства функций.
    -   Код покрывает основные сценарии использования тестируемых функций.
-   Минусы
    -   Отсутствует описание модуля в формате reStructuredText (RST).
    -   Отсутствует описание функций в формате reStructuredText (RST).
    -   Используются старые конструкции импорта и не везде используется `src.logger.logger`.
    -   Не везде используется `asyncio.gather` для параллельного запуска тестов
    -   Дублирование кода в тестах, например, в настройке моков и тестовых данных.
    -   Необходимо использовать `logger.error` с выводом исключения.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Добавить описание модуля в формате RST.
    -   Добавить документацию в формате RST для всех функций, включая параметры и возвращаемые значения.

2.  **Импорты**:
    -   Использовать `from src.utils.jjson import j_loads, j_dumps` для импорта.
    -   Использовать `from src.logger.logger import logger` для логирования.

3.  **Логирование**:
    -   Вместо `mock_logger.error.assert_called_once()` использовать `mock_logger.error.assert_called_once_with(ANY, Error)`

4.  **Асинхронность**:
    -   Использовать `asyncio.gather` для параллельного запуска тестов в функции `process_campaign`.

5.  **Рефакторинг**:
    -   Устранить дублирование кода, вынеся общие части в отдельные переменные.

6.  **Улучшение тестов**:
    -   Добавить более конкретные проверки значений возвращаемых функциями.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль тестирования для подготовки кампаний AliExpress.
======================================================

Этот модуль содержит набор тестов для проверки функциональности
модуля `prepare_campaigns`, который отвечает за подготовку
рекламных кампаний AliExpress.

Он включает тесты для функций:
-   `update_category` - для обновления категорий.
-   `process_campaign_category` - для обработки категорий в кампании.
-   `process_campaign` - для обработки кампаний.
-   `main` - для основной функции подготовки кампаний.

Пример использования
--------------------

Запуск тестов выполняется с помощью pytest.

.. code-block:: bash

    pytest test_prepeare_campaigns.py
"""
import asyncio
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch, ANY

import pytest

from src.logger.logger import logger
from src.suppliers.aliexpress.campaign.prepare_campaigns import (
    main,
    process_campaign,
    process_campaign_category,
    update_category,
)
from src.utils.jjson import j_dumps, j_loads
from src.utils import get_directory_names


MODE = 'dev'


@pytest.fixture
def mock_j_loads():
    """Фикстура для мокирования функции j_loads."""
    with patch("src.utils.jjson.j_loads") as mock:
        yield mock


@pytest.fixture
def mock_j_dumps():
    """Фикстура для мокирования функции j_dumps."""
    with patch("src.utils.jjson.j_dumps") as mock:
        yield mock


@pytest.fixture
def mock_logger():
    """Фикстура для мокирования логгера."""
    with patch("src.logger.logger") as mock:
        yield mock


@pytest.fixture
def mock_get_directory_names():
    """Фикстура для мокирования функции get_directory_names."""
    with patch("src.utils.get_directory_names") as mock:
        yield mock


@pytest.fixture
def mock_ali_promo_campaign():
    """Фикстура для мокирования класса AliPromoCampaign."""
    with patch("src.suppliers.aliexpress.campaign.AliPromoCampaign") as mock:
        yield mock


def test_update_category_success(mock_j_loads, mock_j_dumps, mock_logger):
    """
    Тест для успешного обновления категории.

    :param mock_j_loads: Мок для функции j_loads.
    :param mock_j_dumps: Мок для функции j_dumps.
    :param mock_logger: Мок для логгера.
    """
    mock_json_path = Path("mock/path/to/category.json")
    mock_category = SimpleNamespace(name="test_category")

    mock_j_loads.return_value = {"category": {}}

    result = update_category(mock_json_path, mock_category)

    assert result is True
    mock_j_dumps.assert_called_once_with({"category": {"name": "test_category"}}, mock_json_path)
    mock_logger.error.assert_not_called()


def test_update_category_failure(mock_j_loads, mock_j_dumps, mock_logger):
    """
    Тест для неудачного обновления категории.

    :param mock_j_loads: Мок для функции j_loads.
    :param mock_j_dumps: Мок для функции j_dumps.
    :param mock_logger: Мок для логгера.
    """
    mock_json_path = Path("mock/path/to/category.json")
    mock_category = SimpleNamespace(name="test_category")

    mock_j_loads.side_effect = Exception("Error")

    result = update_category(mock_json_path, mock_category)

    assert result is False
    mock_j_dumps.assert_not_called()
    mock_logger.error.assert_called_once_with(ANY, Exception("Error"))


@pytest.mark.asyncio
async def test_process_campaign_category_success(mock_ali_promo_campaign, mock_logger):
    """
    Тест для успешной обработки категории кампании.

    :param mock_ali_promo_campaign: Мок для класса AliPromoCampaign.
    :param mock_logger: Мок для логгера.
    """
    mock_campaign_name = "test_campaign"
    mock_category_name = "test_category"
    mock_language = "EN"
    mock_currency = "USD"

    mock_ali_promo = mock_ali_promo_campaign.return_value
    mock_ali_promo.process_affiliate_products = MagicMock()

    result = await process_campaign_category(mock_campaign_name, mock_category_name, mock_language, mock_currency)

    assert result is not None
    mock_logger.error.assert_not_called()


@pytest.mark.asyncio
async def test_process_campaign_category_failure(mock_ali_promo_campaign, mock_logger):
    """
    Тест для неудачной обработки категории кампании.

    :param mock_ali_promo_campaign: Мок для класса AliPromoCampaign.
    :param mock_logger: Мок для логгера.
    """
    mock_campaign_name = "test_campaign"
    mock_category_name = "test_category"
    mock_language = "EN"
    mock_currency = "USD"

    mock_ali_promo = mock_ali_promo_campaign.return_value
    mock_ali_promo.process_affiliate_products.side_effect = Exception("Error")

    result = await process_campaign_category(mock_campaign_name, mock_category_name, mock_language, mock_currency)

    assert result is None
    mock_logger.error.assert_called_once_with(ANY, Exception("Error"))


def test_process_campaign(mock_get_directory_names, mock_logger):
    """
    Тест для обработки кампании.

    :param mock_get_directory_names: Мок для функции get_directory_names.
    :param mock_logger: Мок для логгера.
    """
    mock_campaign_name = "test_campaign"
    mock_categories = ["category1", "category2"]
    mock_language = "EN"
    mock_currency = "USD"
    mock_force = False

    mock_get_directory_names.return_value = mock_categories

    results = process_campaign(mock_campaign_name, mock_categories, mock_language, mock_currency, mock_force)

    assert len(results) == 2
    for category_name, result in results:
        assert category_name in mock_categories
        assert result is not None
    mock_logger.warning.assert_not_called()


@pytest.mark.asyncio
async def test_main(mock_get_directory_names):
    """
    Тест для основной функции main.

    :param mock_get_directory_names: Мок для функции get_directory_names.
    """
    mock_campaign_name = "test_campaign"
    mock_categories = ["category1", "category2"]
    mock_language = "EN"
    mock_currency = "USD"
    mock_force = False

    mock_get_directory_names.return_value = mock_categories

    await main(mock_campaign_name, mock_categories, mock_language, mock_currency, mock_force)

    mock_get_directory_names.assert_called_once()