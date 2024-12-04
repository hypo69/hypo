# Руководство по тестированию класса ExecuteLocator

## Обзор

Это руководство предназначено для тестировщиков, чтобы они могли протестировать класс `ExecuteLocator` в проекте. Оно охватывает шаги от настройки окружения до написания и запуска тестов.

## Оглавление

- [Руководство по тестированию класса ExecuteLocator](#руководство-по-тестированию-класса-executelocator)
- [Введение](#введение)
- [Подготовка окружения](#подготовка-окружения)
    - [Установка зависимостей](#установка-зависимостей)
    - [Настройка WebDriver](#настройка-webdriver)
- [Написание тестов](#написание-тестов)
    - [Структура тестов](#структура-тестов)
    - [Реализация тестов](#реализация-тестов)
        - [Пример: `test_get_webelement_by_locator_single_element`](#пример-test_get_webelement_by_locator_single_element)
        - [Пример: `test_get_webelement_by_locator_multiple_elements`](#пример-test_get_webelement_by_locator_multiple_elements)
        - [Пример: `test_get_webelement_by_locator_no_element`](#пример-test_get_webelement_by_locator_no_element)
        - [Пример: `test_get_attribute_by_locator`](#пример-test_get_attribute_by_locator)
        - [Пример: `test_send_message`](#пример-test_send_message)
        - [Пример: `test_send_message_typing_speed`](#пример-test_send_message_typing_speed)
- [Запуск тестов](#запуск-тестов)
- [Проверка результатов тестирования](#проверка-результатов-тестирования)
- [Обновление тестов](#обновление-тестов)
- [Документация](#документация)
- [Примеры тестов](#примеры-тестов)
    - [Описание тестов](#описание-тестов)
    - [Используемые библиотеки](#используемые-библиотеки)
    - [Как запустить тесты](#как-запустить-тесты)
    - [Как читать результаты тестов](#как-читать-результаты-тестов)
- [Дополнительные ресурсы](#дополнительные-ресурсы)


## Введение

Класс `ExecuteLocator` предназначен для взаимодействия с веб-элементами через Selenium WebDriver. Он предоставляет методы для выполнения различных действий с элементами веб-страницы, включая получение атрибутов и отправку сообщений.  Это руководство описывает, как настроить тестовое окружение, написать тесты для класса `ExecuteLocator`, и как запускать эти тесты.

## Подготовка окружения

### Установка зависимостей

Убедитесь, что у вас установлены необходимые библиотеки.  Выполните:

```bash
pip install -r requirements.txt
```

`requirements.txt` должен содержать:

```
pytest==7.4.0
selenium==4.16.1
```

### Настройка WebDriver

Установите WebDriver для вашего браузера (например, ChromeDriver для Chrome).

## Написание тестов

### Структура тестов

Создайте файл `test_executor.py` в директории `tests`.  В этом файле будут располагаться тесты для класса `ExecuteLocator`.

### Реализация тестов

#### Пример: `test_get_webelement_by_locator_single_element`

```python
import pytest
from unittest.mock import MagicMock, patch
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from src.webdriver.executor import ExecuteLocator
from src.logger.exceptions import ExecuteLocatorException

# ... (fixtures driver_mock и execute_locator) ...

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
```

(Аналогичные примеры для остальных тестов)


## Запуск тестов

В корневом каталоге проекта выполните:

```bash
pytest tests/test_executor.py
```

## Проверка результатов тестирования

`pytest` выведет результаты в терминале. Проверьте, все ли тесты прошли успешно.

## Обновление тестов

По мере изменений в коде класса `ExecuteLocator` обновите тесты, чтобы они проверяли новые или измененные функции.

## Документация

Обновляйте документацию, когда добавляете или изменяете тесты. Это поможет другим разработчикам и тестировщикам понимать, как тестируется класс `ExecuteLocator`.

## Примеры тестов

### Описание тестов

В примерах тестов проверяются различные сценарии для методов `get_webelement_by_locator`, `get_attribute_by_locator` и `send_message`.

### Используемые библиотеки

- `pytest`: для написания и запуска тестов.
- `unittest.mock`: для создания имитаций объектов и эмуляции поведения веб-драйвера.

### Как запустить тесты

```bash
pytest tests/test_executor.py
```

### Как читать результаты тестов

- **Passed**: Тест прошел успешно.
- **Failed**: Тест не прошел. Проверьте вывод `pytest` для деталей ошибки.

## Дополнительные ресурсы

- [Официальная документация pytest](https://docs.pytest.org/en/latest/)
- [Документация по Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/)