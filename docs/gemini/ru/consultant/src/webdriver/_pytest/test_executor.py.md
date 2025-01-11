# Анализ кода модуля `test_executor.py`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован, тесты разделены на отдельные функции.
    - Используются фикстуры pytest для настройки окружения тестов.
    - Применяются моки для изоляции тестируемого кода.
    - Покрыты основные варианты использования методов `ExecuteLocator`
- Минусы
    -  Отсутствует документация модуля и функций.
    -  Не используется `from src.logger.logger import logger` для логирования ошибок.
    -  Некоторые строки не соответсвуют `PEP8`

**Рекомендации по улучшению**
- Добавить описание модуля в начале файла.
- Добавить документацию в формате RST для всех функций и фикстур.
- Использовать `from src.logger.logger import logger` для логирования ошибок.
-  В методе `test_send_message_typing_speed` добавить проверку каждого вызова `mock_sleep`  с  задержкой `typing_speed`.
-  Добавить проверку  `element.send_keys.call_args_list` в методе `test_send_message_typing_speed`.
-  Оформить код в соответствии со стандартами `PEP8`.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль тестирования executor.py
=========================================================================================

Этот модуль содержит тесты для проверки корректности работы класса :class:`ExecuteLocator`
из модуля `src.webdriver.executor`.
Тесты проверяют основные функции получения элементов, атрибутов и отправки сообщений с и без задержки.

Пример использования
--------------------

.. code-block:: python

    pytest src/webdriver/_pytest/test_executor.py

"""
import pytest
from unittest.mock import MagicMock, patch
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from src.webdriver.executor import ExecuteLocator
# from src.logger.exceptions import ExecuteLocatorException #не используется
from src.logger.logger import logger

@pytest.fixture
def driver_mock():
    """
    Создает фиктивный объект веб-драйвера.

    Returns:
        MagicMock: фиктивный объект веб-драйвера.
    """
    return MagicMock()

@pytest.fixture
def execute_locator(driver_mock):
    """
    Создает экземпляр класса ExecuteLocator с фиктивным веб-драйвером.

    Args:
        driver_mock (MagicMock): Фиктивный объект веб-драйвера.

    Returns:
        ExecuteLocator: Экземпляр ExecuteLocator с фиктивным драйвером.
    """
    return ExecuteLocator(driver_mock)

def test_get_webelement_by_locator_single_element(execute_locator, driver_mock):
    """
    Проверяет получение одного элемента.

    Args:
        execute_locator (ExecuteLocator): Экземпляр ExecuteLocator.
        driver_mock (MagicMock): Фиктивный объект веб-драйвера.
    """
    element = MagicMock(spec=WebElement)
    driver_mock.find_elements.return_value = [element]

    locator = {
        'by': 'XPATH',
        'selector': '//div[@id=\'test\']'
    }
    
    result = execute_locator.get_webelement_by_locator(locator)
    
    driver_mock.find_elements.assert_called_once_with(By.XPATH, '//div[@id=\'test\']')
    assert result == element

def test_get_webelement_by_locator_multiple_elements(execute_locator, driver_mock):
    """
    Проверяет получение нескольких элементов.

    Args:
        execute_locator (ExecuteLocator): Экземпляр ExecuteLocator.
        driver_mock (MagicMock): Фиктивный объект веб-драйвера.
    """
    elements = [MagicMock(spec=WebElement) for _ in range(3)]
    driver_mock.find_elements.return_value = elements

    locator = {
        'by': 'XPATH',
        'selector': '//div[@class=\'test\']'
    }

    result = execute_locator.get_webelement_by_locator(locator)
    
    driver_mock.find_elements.assert_called_once_with(By.XPATH, '//div[@class=\'test\']')
    assert result == elements

def test_get_webelement_by_locator_no_element(execute_locator, driver_mock):
    """
    Проверяет случай, когда элемент не найден.

    Args:
        execute_locator (ExecuteLocator): Экземпляр ExecuteLocator.
        driver_mock (MagicMock): Фиктивный объект веб-драйвера.
    """
    driver_mock.find_elements.return_value = []

    locator = {
        'by': 'XPATH',
        'selector': '//div[@id=\'not_exist\']'
    }

    result = execute_locator.get_webelement_by_locator(locator)
    
    driver_mock.find_elements.assert_called_once_with(By.XPATH, '//div[@id=\'not_exist\']')
    assert result is False

def test_get_attribute_by_locator(execute_locator, driver_mock):
    """
    Проверяет получение атрибута элемента.

    Args:
        execute_locator (ExecuteLocator): Экземпляр ExecuteLocator.
        driver_mock (MagicMock): Фиктивный объект веб-драйвера.
    """
    element = MagicMock(spec=WebElement)
    element.get_attribute.return_value = 'test_value'
    driver_mock.find_elements.return_value = [element]

    locator = {
        'by': 'XPATH',
        'selector': '//div[@id=\'test\']',
        'attribute': 'data-test'
    }

    result = execute_locator.get_attribute_by_locator(locator)
    
    driver_mock.find_elements.assert_called_once_with(By.XPATH, '//div[@id=\'test\']')
    element.get_attribute.assert_called_once_with('data-test')
    assert result == 'test_value'

def test_send_message(execute_locator, driver_mock):
    """
    Проверяет отправку сообщения элементу.

    Args:
        execute_locator (ExecuteLocator): Экземпляр ExecuteLocator.
        driver_mock (MagicMock): Фиктивный объект веб-драйвера.
    """
    element = MagicMock(spec=WebElement)
    driver_mock.find_elements.return_value = [element]

    locator = {
        'by': 'XPATH',
        'selector': '//input[@id=\'test\']'
    }
    message = 'Hello World'

    result = execute_locator.send_message(locator, message, typing_speed=0, continue_on_error=True)
    
    driver_mock.find_elements.assert_called_once_with(By.XPATH, '//input[@id=\'test\']')
    element.send_keys.assert_called_once_with(message)
    assert result is True

def test_send_message_typing_speed(execute_locator, driver_mock):
    """
    Проверяет отправку сообщения элементу с задержкой между символами.

    Args:
        execute_locator (ExecuteLocator): Экземпляр ExecuteLocator.
        driver_mock (MagicMock): Фиктивный объект веб-драйвера.
    """
    element = MagicMock(spec=WebElement)
    driver_mock.find_elements.return_value = [element]

    locator = {
        'by': 'XPATH',
        'selector': '//input[@id=\'test\']'
    }
    message = 'Hello'
    typing_speed = 0.1

    with patch('time.sleep', return_value=None) as mock_sleep:
        result = execute_locator.send_message(locator, message, typing_speed=typing_speed, continue_on_error=True)
    
    driver_mock.find_elements.assert_called_once_with(By.XPATH, '//input[@id=\'test\']')
    assert element.send_keys.call_count == len(message)
    assert mock_sleep.call_count == len(message)
    mock_sleep.assert_called_with(typing_speed)
    assert  [call[0][0] for call in mock_sleep.call_args_list] == [typing_speed] * len(message)
    assert [call[0][0] for call in element.send_keys.call_args_list] == list(message)
    assert result is True