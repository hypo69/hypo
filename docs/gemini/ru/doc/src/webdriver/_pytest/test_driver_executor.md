# Модуль `hypotez/src/webdriver/_pytest/test_driver_executor.py`

## Обзор

Этот модуль содержит тесты для проверки корректной работы модуля `src.webdriver.executor` и взаимодействия с `WebDriver`. Тесты охватывают навигацию по страницам, поиск элементов, отправку сообщений, получение атрибутов и обработку различных ситуаций, включая поиск несуществующих элементов и некорректные локаторы.

## Оглавление

- [Функции](#функции)


## Функции

### `test_navigate_to_page`

**Описание**: Проверяет, что `WebDriver` корректно загружает указанную страницу.

**Параметры**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет


### `test_get_webelement_by_locator_single_element`

**Описание**: Проверяет, что метод `get_webelement_by_locator` корректно возвращает элемент по локатору.

**Параметры**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет


### `test_get_webelement_by_locator_no_element`

**Описание**: Проверяет, что метод `get_webelement_by_locator` возвращает `False`, если элемент не найден.

**Параметры**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет


### `test_send_message`

**Описание**: Проверяет, что метод `send_message` корректно отправляет сообщение элементу.

**Параметры**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет


### `test_get_attribute_by_locator`

**Описание**: Проверяет, что метод `get_attribute_by_locator` корректно возвращает атрибут элемента.

**Параметры**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет


### `test_execute_locator_event`

**Описание**: Проверяет, что метод `execute_locator` корректно выполняет событие на локаторе.

**Параметры**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет


### `test_get_locator_keys`

**Описание**: Проверяет, что метод `get_locator_keys` возвращает правильные ключи локатора.

**Параметры**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет


### `test_navigate_and_interact`

**Описание**: Проверяет последовательность навигации и взаимодействия с элементами на другой странице.

**Параметры**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет


### `test_invalid_locator`

**Описание**: Проверяет обработку некорректных локаторов и соответствующее исключение.

**Параметры**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `ExecuteLocatorException`: Исключение, генерируемое при некорректном локаторе.


### `driver`

**Описание**: Fixture для настройки и завершения работы `WebDriver`.

**Параметры**:
- Нет

**Возвращает**:
- Экземпляр `WebDriver`.

**Вызывает исключения**:
- Нет


### `execute_locator`

**Описание**: Fixture для инициализации экземпляра `ExecuteLocator`.

**Параметры**:
- `driver`: Экземпляр `WebDriver`.

**Возвращает**:
- Экземпляр `ExecuteLocator`.

**Вызывает исключения**:
- Нет