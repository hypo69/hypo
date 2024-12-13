# Руководство для тестера по запуску и выполнению тестов

## Обзор

Этот документ содержит руководство для тестировщиков по запуску и выполнению тестов, описанных в файле `test_driver_executor.py`. Руководство охватывает настройку окружения, запуск тестов и описание целей каждого теста.

## Содержание

1. [Введение](#введение)
2. [Структура тестов](#структура-тестов)
   - [Тестируемые методы и функции](#тестируемые-методы-и-функции)
3. [Запуск тестов](#запуск-тестов)
   - [Установка зависимостей](#установка-зависимостей)
   - [Настройка WebDriver](#настройка-webdriver)
   - [Запуск тестов](#запуск-тестов)
4. [Описание тестов](#описание-тестов)
   - [`test_navigate_to_page`](#1-test_navigate_to_page)
   - [`test_get_webelement_by_locator_single_element`](#2-test_get_webelement_by_locator_single_element)
   - [`test_get_webelement_by_locator_no_element`](#3-test_get_webelement_by_locator_no_element)
   - [`test_send_message`](#4-test_send_message)
   - [`test_get_attribute_by_locator`](#5-test_get_attribute_by_locator)
   - [`test_execute_locator_event`](#6-test_execute_locator_event)
   - [`test_get_locator_keys`](#7-test_get_locator_keys)
   - [`test_navigate_and_interact`](#8-test_navigate_and_interact)
   - [`test_invalid_locator`](#9-test_invalid_locator)
5. [Отчеты о тестах](#отчеты-о-тестах)
6. [Чеклист](#чеклист)
7. [Заключение](#заключение)

## Введение

Это руководство описывает, как запустить и выполнить тесты для классов `Driver` и `ExecuteLocator`, находящиеся в файле `test_driver_executor.py`. Эти тесты проверяют работоспособность методов классов и их взаимодействие.

## Структура тестов

Файл `test_driver_executor.py` содержит тесты для классов `Driver` и `ExecuteLocator`. Тесты проверяют правильность работы методов классов, их взаимодействие и сценарии использования в различных ситуациях.

### Тестируемые методы и функции

- **`test_navigate_to_page`**: Проверяет, что WebDriver корректно загружает указанную страницу.
- **`test_get_webelement_by_locator_single_element`**: Проверяет, что метод `get_webelement_by_locator` корректно возвращает элемент по локатору.
- **`test_get_webelement_by_locator_no_element`**: Проверяет, что метод `get_webelement_by_locator` возвращает `False`, если элемент не найден.
- **`test_send_message`**: Проверяет, что метод `send_message` корректно отправляет сообщение элементу.
- **`test_get_attribute_by_locator`**: Проверяет, что метод `get_attribute_by_locator` корректно возвращает атрибут элемента.
- **`test_execute_locator_event`**: Проверяет, что метод `execute_locator` корректно выполняет событие на локаторе.
- **`test_get_locator_keys`**: Проверяет, что метод `get_locator_keys` возвращает правильные ключи локатора.
- **`test_navigate_and_interact`**: Проверяет последовательность навигации и взаимодействия с элементами на другой странице.
- **`test_invalid_locator`**: Проверяет обработку некорректных локаторов и соответствующее исключение.

## Запуск тестов

### Установка зависимостей

Перед запуском тестов убедитесь, что у вас установлены необходимые зависимости. Используйте команду:

```bash
pip install -r requirements.txt
```

`requirements.txt` должен содержать необходимые библиотеки, например, `pytest` и `selenium`.

### Настройка WebDriver

В тестах используется Chrome WebDriver. Убедитесь, что у вас установлен [ChromeDriver](https://sites.google.com/chromium.org/driver/) и укажите путь к `chromedriver` в коде:

```python
service = Service(executable_path="/path/to/chromedriver")  # Путь к вашему chromedriver
```

### Запуск тестов

Для запуска тестов используйте команду:

```bash
pytest src/webdriver/_pytest/test_driver_executor.py
```

Эта команда запустит все тесты, определенные в файле `test_driver_executor.py`.

## Описание тестов

### 1. `test_navigate_to_page`

- **Цель**: Проверить, что WebDriver корректно загружает указанную страницу.
- **Ожидаемый результат**: URL текущей страницы должен соответствовать `"http://example.com"`.

### 2. `test_get_webelement_by_locator_single_element`

- **Цель**: Проверить, что метод `get_webelement_by_locator` возвращает элемент по локатору.
- **Ожидаемый результат**: Элемент должен быть экземпляром `WebElement` и содержать текст `"Example Domain"`.

### 3. `test_get_webelement_by_locator_no_element`

- **Цель**: Проверить, что метод `get_webelement_by_locator` возвращает `False`, если элемент не найден.
- **Ожидаемый результат**: Возвращаемое значение должно быть `False`.

### 4. `test_send_message`

- **Цель**: Проверить, что метод `send_message` корректно отправляет сообщение элементу.
- **Ожидаемый результат**: Метод должен вернуть `True`.

### 5. `test_get_attribute_by_locator`

- **Цель**: Проверить, что метод `get_attribute_by_locator` возвращает атрибут элемента.
- **Ожидаемый результат**: Атрибут `href` элемента должен быть `"https://www.iana.org/domains/example"`.

### 6. `test_execute_locator_event`

- **Цель**: Проверить, что метод `execute_locator` выполняет событие на локаторе.
- **Ожидаемый результат**: Метод должен вернуть `True`.

### 7. `test_get_locator_keys`

- **Цель**: Проверить, что метод `get_locator_keys` возвращает правильные ключи локатора.
- **Ожидаемый результат**: Ключи локатора должны включать `attribute`, `by`, `selector`, `event`, `use_mouse`, `mandatory`, `locator_description`.

### 8. `test_navigate_and_interact`

- **Цель**: Проверить последовательность навигации и взаимодействия с элементами на другой странице.
- **Ожидаемый результат**: Должна быть выполнена навигация на страницу Википедии, отправлено сообщение в поле поиска, выполнен клик на кнопку поиска и проверены результаты поиска.

### 9. `test_invalid_locator`

- **Цель**: Проверить обработку некорректных локаторов и соответствующее исключение.
- **Ожидаемый результат**: Должно быть выброшено исключение `ExecuteLocatorException`.

## Отчеты о тестах

По завершении тестов `pytest` создаст отчет с результатами тестирования. Вы можете просмотреть его в консоли или использовать флаги командной строки для создания подробных отчетов:

- **Текстовый отчет**:

```bash
pytest src/webdriver/_pytest/test_driver_executor.py -v
```

- **HTML-отчет**:

Установите `pytest-html` и создайте отчет:

```bash
pip install pytest-html
pytest src/webdriver/_pytest/test_driver_executor.py --html=report.html
```

Отчет будет сохранен в файле `report.html`.

## Чеклист

Перед запуском тестов убедитесь, что:

- [x] Установлены все зависимости из `requirements.txt`.
- [x] Указан правильный путь к `chromedriver` в `test_driver_executor.py`.
- [x] Настроен `headless` режим в `Options` (при необходимости).
- [x] Запуск тестов производится командой `pytest`.

## Заключение

Следуя этому руководству, вы сможете запустить и проверить тесты для классов `Driver` и `ExecuteLocator`. Если возникнут вопросы или проблемы, обратитесь к разработчикам или проверьте документацию для получения дополнительной информации.