# Модуль `test_executor.py`

## Обзор

Модуль `test_executor.py` содержит набор тестов для проверки корректности работы класса `ExecuteLocator` из модуля `src.webdriver.executor`. Тесты используют фикстуры pytest для создания мок-объектов веб-драйвера и экземпляров `ExecuteLocator`.

## Содержание

1.  [Фикстуры](#Фикстуры)
    *   [`driver_mock`](#driver_mock)
    *   [`execute_locator`](#execute_locator)
2.  [Тесты](#Тесты)
    *   [`test_get_webelement_by_locator_single_element`](#test_get_webelement_by_locator_single_element)
    *   [`test_get_webelement_by_locator_multiple_elements`](#test_get_webelement_by_locator_multiple_elements)
    *   [`test_get_webelement_by_locator_no_element`](#test_get_webelement_by_locator_no_element)
    *   [`test_get_attribute_by_locator`](#test_get_attribute_by_locator)
    *   [`test_send_message`](#test_send_message)
    *   [`test_send_message_typing_speed`](#test_send_message_typing_speed)

## Фикстуры

### `driver_mock`

**Описание**: Создает фиктивный объект веб-драйвера.

**Возвращает**:

- `MagicMock`: Мок-объект веб-драйвера.

### `execute_locator`

**Описание**: Создает экземпляр класса `ExecuteLocator` с фиктивным веб-драйвером.

**Параметры**:

-   `driver_mock` (`MagicMock`): Мок-объект веб-драйвера.

**Возвращает**:

-   `ExecuteLocator`: Экземпляр класса `ExecuteLocator`.

## Тесты

### `test_get_webelement_by_locator_single_element`

**Описание**: Проверяет получение одного элемента с помощью метода `get_webelement_by_locator`.

**Параметры**:

-   `execute_locator` (`ExecuteLocator`): Экземпляр класса `ExecuteLocator`.
-   `driver_mock` (`MagicMock`): Мок-объект веб-драйвера.

**Проверяет**:

-   Вызов метода `find_elements` у мок-объекта драйвера с правильными параметрами.
-   Возвращение найденного элемента.

### `test_get_webelement_by_locator_multiple_elements`

**Описание**: Проверяет получение нескольких элементов с помощью метода `get_webelement_by_locator`.

**Параметры**:

-   `execute_locator` (`ExecuteLocator`): Экземпляр класса `ExecuteLocator`.
-   `driver_mock` (`MagicMock`): Мок-объект веб-драйвера.

**Проверяет**:

-   Вызов метода `find_elements` у мок-объекта драйвера с правильными параметрами.
-   Возвращение списка найденных элементов.

### `test_get_webelement_by_locator_no_element`

**Описание**: Проверяет случай, когда элемент не найден с помощью метода `get_webelement_by_locator`.

**Параметры**:

-   `execute_locator` (`ExecuteLocator`): Экземпляр класса `ExecuteLocator`.
-   `driver_mock` (`MagicMock`): Мок-объект веб-драйвера.

**Проверяет**:

-   Вызов метода `find_elements` у мок-объекта драйвера с правильными параметрами.
-   Возвращение `False`, если элементы не найдены.

### `test_get_attribute_by_locator`

**Описание**: Проверяет получение атрибута элемента с помощью метода `get_attribute_by_locator`.

**Параметры**:

-   `execute_locator` (`ExecuteLocator`): Экземпляр класса `ExecuteLocator`.
-   `driver_mock` (`MagicMock`): Мок-объект веб-драйвера.

**Проверяет**:

-   Вызов метода `find_elements` у мок-объекта драйвера с правильными параметрами.
-   Вызов метода `get_attribute` у мок-объекта элемента с правильным параметром.
-   Возвращение значения атрибута.

### `test_send_message`

**Описание**: Проверяет отправку сообщения элементу с помощью метода `send_message`.

**Параметры**:

-   `execute_locator` (`ExecuteLocator`): Экземпляр класса `ExecuteLocator`.
-   `driver_mock` (`MagicMock`): Мок-объект веб-драйвера.

**Проверяет**:

-   Вызов метода `find_elements` у мок-объекта драйвера с правильными параметрами.
-   Вызов метода `send_keys` у мок-объекта элемента с правильным сообщением.
-   Возвращение `True`, если сообщение отправлено успешно.

### `test_send_message_typing_speed`

**Описание**: Проверяет отправку сообщения элементу с задержкой между символами с помощью метода `send_message`.

**Параметры**:

-   `execute_locator` (`ExecuteLocator`): Экземпляр класса `ExecuteLocator`.
-   `driver_mock` (`MagicMock`): Мок-объект веб-драйвера.

**Проверяет**:

-   Вызов метода `find_elements` у мок-объекта драйвера с правильными параметрами.
-   Множественный вызов метода `send_keys` у мок-объекта элемента (по количеству символов в сообщении).
-   Вызов функции `time.sleep` с заданным временем задержки.
-    Возвращение `True`, если сообщение отправлено успешно.