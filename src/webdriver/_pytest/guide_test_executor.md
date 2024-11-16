## \file hypotez/src/webdriver/_pytest/guide_test_executor.md
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.webdriver._pytest """
MODE = 'debug'
Вот подробное руководство для тестировщика, чтобы он мог протестировать класс `ExecuteLocator` в проекте. Это руководство охватывает основные шаги от установки окружения до написания и запуска тестов.

---

## Руководство по тестированию класса `ExecuteLocator`

### Введение

Класс `ExecuteLocator` предназначен для работы с веб-элементами через Selenium WebDriver. Он включает в себя методы для выполнения различных действий на элементах веб-страницы, таких как получение атрибутов и отправка сообщений. В этом руководстве вы найдете информацию о том, как настроить тестовое окружение, написать тесты для класса `ExecuteLocator`, и как запускать эти тесты.

### 1. Подготовка окружения

#### 1.1 Установка зависимостей

Убедитесь, что у вас установлены все необходимые библиотеки для работы с проектом и тестирования. Для этого выполните следующую команду:

```bash
pip install -r requirements.txt
```

`requirements.txt` должен содержать следующие зависимости:

```text
pytest==7.4.0
selenium==4.16.1
```

#### 1.2 Настройка WebDriver

Убедитесь, что у вас установлен WebDriver для браузера, который вы будете использовать для тестирования (например, [ChromeDriver](https://sites.google.com/chromium.org/driver/) для Chrome).

### 2. Написание тестов

#### 2.1 Структура тестов

Создайте файл тестов `test_executor.py` в директории `tests`. В этом файле будут находиться тесты для класса `ExecuteLocator`. Вот пример структуры файла тестов:

```python
import pytest
from unittest.mock import MagicMock, patch
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from src.webdriver.executor import ExecuteLocator
from src.logger.exceptions import ExecuteLocatorException

@pytest.fixture
def driver_mock():
    return MagicMock()

@pytest.fixture
def execute_locator(driver_mock):
    return ExecuteLocator(driver_mock)

# Примеры тестов для методов класса ExecuteLocator
def test_get_webelement_by_locator_single_element(execute_locator, driver_mock):
    pass  # Реализация теста

def test_get_webelement_by_locator_multiple_elements(execute_locator, driver_mock):
    pass  # Реализация теста

def test_get_webelement_by_locator_no_element(execute_locator, driver_mock):
    pass  # Реализация теста

def test_get_attribute_by_locator(execute_locator, driver_mock):
    pass  # Реализация теста

def test_send_message(execute_locator, driver_mock):
    pass  # Реализация теста

def test_send_message_typing_speed(execute_locator, driver_mock):
    pass  # Реализация теста
```

#### 2.2 Реализация тестов

Вам нужно реализовать тесты для методов `get_webelement_by_locator`, `get_attribute_by_locator` и `send_message`, как показано в примере ниже:

```python
def test_get_webelement_by_locator_single_element(execute_locator, driver_mock):
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
    driver_mock.find_elements.return_value = []

    locator = {
        "by": "XPATH",
        "selector": "//div[@id='not_exist']"
    }

    result = execute_locator.get_webelement_by_locator(locator)
    
    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//div[@id='not_exist']")
    assert result is False

def test_get_attribute_by_locator(execute_locator, driver_mock):
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

def test_send_message_typing_speed(execute_locator, driver_mock):
    element = MagicMock(spec=WebElement)
    driver_mock.find_elements.return_value = [element]

    locator = {
        "by": "XPATH",
        "selector": "//input[@id='test']"
    }
    message = "Hello"
    typing_speed = 0.1

    with patch('time.sleep', return_value=None) as mock_sleep:
        result = execute_locator.send_message(locator, message, typing_speed=typing_speed, continue_on_error=True)
    
    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//input[@id='test']")
    assert element.send_keys.call_count == len(message)
    mock_sleep.assert_called_with(typing_speed)
    assert result is True
```

### 3. Запуск тестов

Для запуска тестов выполните следующую команду в корневой директории проекта:

```bash
pytest tests/test_executor.py
```

### 4. Проверка результатов тестирования

После запуска тестов, `pytest` выведет результаты в терминале. Убедитесь, что все тесты прошли успешно. Если какой-то тест не прошел, `pytest` укажет на ошибку или неудачу, и вам нужно будет проанализировать, что пошло не так, и исправить соответствующие проблемы в тестах или коде.

### 5. Обновление тестов

По мере изменений в коде класса `ExecuteLocator`, тесты могут потребовать обновлений. Убедитесь, что тесты актуальны и проверяют все новые или измененные функции.

### 6. Документация

Если вы добавили новые тесты или изменили существующие, обновите соответствующую документацию. Это поможет другим разработчикам и тестировщикам понять, как тестируются функции `ExecuteLocator`.

---

### Пример документации для тестов

Если вам нужно создать документацию для тестов, вы можете использовать следующий шаблон:

---

## Документация по тестам для класса `ExecuteLocator`

### Описание тестов

- **Тестирование метода `get_webelement_by_locator`**:
  - Проверяет случаи, когда найден один элемент, несколько элементов и когда элемент не найден.

- **Тестирование метода `get_attribute_by_locator`**:
  - Проверяет получение атрибута у элемента.

- **Тестирование метода `send_message`**:
  - Проверяет отправку сообщения элементу и работу с задержкой между символами.

### Используемые библиотеки

- `pytest`: для написания и запуска тестов.
- `unittest.mock`: для создания мок-объектов и имитации поведения веб-драйвера.

### Как запустить тесты

```bash
pytest tests/test_executor.py
```

### Как читать результаты тестов

- **Passed**: Тест прошел успешно.
- **Failed**: Тест не прошел. Проверьте вывод `pytest` для деталей ошибки и исправьте соответствующие проблемы.

---

### Дополнительные ресурсы

- [Официальная документация pytest](https://docs.pytest.org/en/latest/)
- [Документация по Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/)
- [Руководство по написанию тестов для Python](https://docs.python.org/3/library/unittest.html)

Следуйте этому руководству, чтобы эффективно тестировать класс `ExecuteLocator` и обеспечивать его правильную работу.

---

Если у вас возникнут вопросы или потребуется помощь, не стесняйтесь обращаться к разработчикам или старшим тестировщикам в вашей команде.

