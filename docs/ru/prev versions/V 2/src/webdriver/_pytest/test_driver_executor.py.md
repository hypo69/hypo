# Модуль `test_driver_executor`

## Обзор

Модуль `test_driver_executor.py` содержит набор тестов для проверки функциональности взаимодействия WebDriver и `ExecuteLocator`. Эти тесты проверяют различные сценарии, такие как навигация по страницам, поиск элементов, отправка сообщений, получение атрибутов, выполнение событий и обработка некорректных локаторов.

## Оглавление

- [Классы](#классы)
- [Фикстуры](#фикстуры)
- [Функции](#функции)
    - [`test_navigate_to_page`](#test_navigate_to_page)
    - [`test_get_webelement_by_locator_single_element`](#test_get_webelement_by_locator_single_element)
    - [`test_get_webelement_by_locator_no_element`](#test_get_webelement_by_locator_no_element)
    - [`test_send_message`](#test_send_message)
    - [`test_get_attribute_by_locator`](#test_get_attribute_by_locator)
    - [`test_execute_locator_event`](#test_execute_locator_event)
    - [`test_get_locator_keys`](#test_get_locator_keys)
    - [`test_navigate_and_interact`](#test_navigate_and_interact)
    - [`test_invalid_locator`](#test_invalid_locator)

## Классы

В данном модуле нет классов.

## Фикстуры

### `driver`

**Описание**: Фикстура для настройки и завершения работы WebDriver.

**Возвращает**:
- `webdriver.Chrome`: Экземпляр WebDriver.

### `execute_locator`

**Описание**: Фикстура для инициализации экземпляра `ExecuteLocator`.

**Параметры**:
- `driver` : Экземпляр WebDriver, используемый для инициализации `ExecuteLocator`.

**Возвращает**:
- `ExecuteLocator`: Экземпляр `ExecuteLocator`.

## Функции

### `test_navigate_to_page`

**Описание**: Проверяет, что WebDriver корректно загружает указанную страницу.

**Параметры**:
- `execute_locator` (`ExecuteLocator`): Фикстура `execute_locator`.
- `driver` (`webdriver.Chrome`): Фикстура `driver`.

### `test_get_webelement_by_locator_single_element`

**Описание**: Проверяет, что метод `get_webelement_by_locator` корректно возвращает элемент по локатору.

**Параметры**:
- `execute_locator` (`ExecuteLocator`): Фикстура `execute_locator`.
- `driver` (`webdriver.Chrome`): Фикстура `driver`.

### `test_get_webelement_by_locator_no_element`

**Описание**: Проверяет, что метод `get_webelement_by_locator` возвращает `False`, если элемент не найден.

**Параметры**:
- `execute_locator` (`ExecuteLocator`): Фикстура `execute_locator`.
- `driver` (`webdriver.Chrome`): Фикстура `driver`.

### `test_send_message`

**Описание**: Проверяет, что метод `send_message` корректно отправляет сообщение элементу.

**Параметры**:
- `execute_locator` (`ExecuteLocator`): Фикстура `execute_locator`.
- `driver` (`webdriver.Chrome`): Фикстура `driver`.

### `test_get_attribute_by_locator`

**Описание**: Проверяет, что метод `get_attribute_by_locator` корректно возвращает атрибут элемента.

**Параметры**:
- `execute_locator` (`ExecuteLocator`): Фикстура `execute_locator`.
- `driver` (`webdriver.Chrome`): Фикстура `driver`.

### `test_execute_locator_event`

**Описание**: Проверяет, что метод `execute_locator` корректно выполняет событие на локаторе.

**Параметры**:
- `execute_locator` (`ExecuteLocator`): Фикстура `execute_locator`.
- `driver` (`webdriver.Chrome`): Фикстура `driver`.

### `test_get_locator_keys`

**Описание**: Проверяет, что метод `get_locator_keys` возвращает правильные ключи локатора.

**Параметры**:
- `execute_locator` (`ExecuteLocator`): Фикстура `execute_locator`.
- `driver` (`webdriver.Chrome`): Фикстура `driver`.

### `test_navigate_and_interact`

**Описание**: Проверяет последовательность навигации и взаимодействия с элементами на другой странице.

**Параметры**:
- `execute_locator` (`ExecuteLocator`): Фикстура `execute_locator`.
- `driver` (`webdriver.Chrome`): Фикстура `driver`.

### `test_invalid_locator`

**Описание**: Проверяет обработку некорректных локаторов и соответствующее исключение.

**Параметры**:
- `execute_locator` (`ExecuteLocator`): Фикстура `execute_locator`.
- `driver` (`webdriver.Chrome`): Фикстура `driver`.

**Вызывает исключения**:
- `ExecuteLocatorException`: Если локатор некорректен.