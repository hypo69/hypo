# Анализ кода модуля `test_executor.py`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разбит на отдельные тестовые функции.
    - Используются фикстуры pytest для настройки тестовой среды.
    - Применяется `unittest.mock` для создания мок-объектов, что позволяет изолировать тесты.
    - Тесты покрывают основные сценарии работы `ExecuteLocator`, включая получение элементов, атрибутов и отправку сообщений.
- Минусы
    - Отсутствует документация в формате reStructuredText.
    - Присутствуют избыточные комментарии.
    - Не используется `from src.logger.logger import logger` для логирования.

**Рекомендации по улучшению**
1. Добавить документацию в формате reStructuredText для модуля, фикстур и тестовых функций.
2. Использовать `from src.logger.logger import logger` для логирования в случае ошибок.
3. Удалить лишние комментарии.
4. Заменить стандартный `patch` из `unittest` на `pytest.monkeypatch` для более удобного переопределения поведения функций.
5. Использовать более точные проверки `assert` вместо `assert result is True` там, где это возможно.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль тестов для класса :class:`ExecuteLocator`.
==================================================

Этот модуль содержит тесты, проверяющие корректность работы класса :class:`ExecuteLocator`,
который используется для взаимодействия с веб-элементами на странице.
Тесты включают проверку получения элементов, их атрибутов, отправки сообщений и обработки ошибок.
"""
import pytest
from unittest.mock import MagicMock
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# from src.logger.logger import logger #TODO:  не используется в текущем коде, добавить если требуется
from src.webdriver.executor import ExecuteLocator
from src.logger.exceptions import ExecuteLocatorException
from time import sleep

MODE = 'dev'


@pytest.fixture
def driver_mock():
    """
    Фикстура, создающая мок-объект веб-драйвера.

    :return: Мок-объект веб-драйвера.
    :rtype: MagicMock
    """
    return MagicMock()


@pytest.fixture
def execute_locator(driver_mock):
    """
    Фикстура, создающая экземпляр класса :class:`ExecuteLocator` с мок-драйвером.

    :param driver_mock: Мок-объект веб-драйвера.
    :type driver_mock: MagicMock
    :return: Экземпляр класса :class:`ExecuteLocator`.
    :rtype: ExecuteLocator
    """
    return ExecuteLocator(driver_mock)


def test_get_webelement_by_locator_single_element(execute_locator, driver_mock):
    """
    Проверяет получение одного веб-элемента по локатору.

    :param execute_locator: Экземпляр класса :class:`ExecuteLocator`.
    :type execute_locator: ExecuteLocator
    :param driver_mock: Мок-объект веб-драйвера.
    :type driver_mock: MagicMock
    """
    element = MagicMock(spec=WebElement)
    driver_mock.find_elements.return_value = [element]

    locator = {
        "by": "XPATH",
        "selector": "//div[@id='test']"
    }

    result = execute_locator.get_webelement_by_locator(locator)

    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//div[@id='test']")
    assert result == element


def test_get_webelement_by_locator_multiple_elements(execute_locator, driver_mock):
    """
    Проверяет получение нескольких веб-элементов по локатору.

    :param execute_locator: Экземпляр класса :class:`ExecuteLocator`.
    :type execute_locator: ExecuteLocator
    :param driver_mock: Мок-объект веб-драйвера.
    :type driver_mock: MagicMock
    """
    elements = [MagicMock(spec=WebElement) for _ in range(3)]
    driver_mock.find_elements.return_value = elements

    locator = {
        "by": "XPATH",
        "selector": "//div[@class='test']"
    }

    result = execute_locator.get_webelement_by_locator(locator)

    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//div[@class='test']")
    assert result == elements


def test_get_webelement_by_locator_no_element(execute_locator, driver_mock):
    """
    Проверяет случай, когда веб-элемент не найден по локатору.

    :param execute_locator: Экземпляр класса :class:`ExecuteLocator`.
    :type execute_locator: ExecuteLocator
    :param driver_mock: Мок-объект веб-драйвера.
    :type driver_mock: MagicMock
    """
    driver_mock.find_elements.return_value = []

    locator = {
        "by": "XPATH",
        "selector": "//div[@id='not_exist']"
    }

    result = execute_locator.get_webelement_by_locator(locator)

    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//div[@id='not_exist']")
    assert result is False


def test_get_attribute_by_locator(execute_locator, driver_mock):
    """
    Проверяет получение атрибута веб-элемента по локатору.

    :param execute_locator: Экземпляр класса :class:`ExecuteLocator`.
    :type execute_locator: ExecuteLocator
    :param driver_mock: Мок-объект веб-драйвера.
    :type driver_mock: MagicMock
    """
    element = MagicMock(spec=WebElement)
    element.get_attribute.return_value = "test_value"
    driver_mock.find_elements.return_value = [element]

    locator = {
        "by": "XPATH",
        "selector": "//div[@id='test']",
        "attribute": "data-test"
    }

    result = execute_locator.get_attribute_by_locator(locator)

    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//div[@id='test']")
    element.get_attribute.assert_called_once_with("data-test")
    assert result == "test_value"


def test_send_message(execute_locator, driver_mock):
    """
    Проверяет отправку сообщения веб-элементу по локатору.

    :param execute_locator: Экземпляр класса :class:`ExecuteLocator`.
    :type execute_locator: ExecuteLocator
    :param driver_mock: Мок-объект веб-драйвера.
    :type driver_mock: MagicMock
    """
    element = MagicMock(spec=WebElement)
    driver_mock.find_elements.return_value = [element]

    locator = {
        "by": "XPATH",
        "selector": "//input[@id='test']"
    }
    message = "Hello World"

    result = execute_locator.send_message(locator, message, typing_speed=0, continue_on_error=True)

    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//input[@id='test']")
    element.send_keys.assert_called_once_with(message)
    assert result is True


def test_send_message_typing_speed(execute_locator, driver_mock, monkeypatch):
    """
    Проверяет отправку сообщения веб-элементу по локатору с заданной скоростью печати.

    :param execute_locator: Экземпляр класса :class:`ExecuteLocator`.
    :type execute_locator: ExecuteLocator
    :param driver_mock: Мок-объект веб-драйвера.
    :type driver_mock: MagicMock
    :param monkeypatch:  фикстура для подмены поведения методов.
    :type monkeypatch: pytest.MonkeyPatch
    """
    element = MagicMock(spec=WebElement)
    driver_mock.find_elements.return_value = [element]

    locator = {
        "by": "XPATH",
        "selector": "//input[@id='test']"
    }
    message = "Hello"
    typing_speed = 0.1

    def mock_sleep(time):
        pass

    monkeypatch.setattr('time.sleep', mock_sleep)
    result = execute_locator.send_message(locator, message, typing_speed=typing_speed, continue_on_error=True)

    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//input[@id='test']")
    assert element.send_keys.call_count == len(message)
    assert result is True
```