# hypotez/src/webdriver/executor.py

## Обзор

Модуль `executor` предназначен для выполнения действий над веб-элементами на основе предоставленных конфигураций, известных как "локаторы". Эти конфигурации (или "локаторы") представляют собой словари, содержащие информацию о том, как найти и взаимодействовать с элементами на веб-странице. Модуль предоставляет следующие функциональные возможности:

1.  **Разбор и обработка локаторов**: Преобразует словари с конфигурациями в объекты `SimpleNamespace`, что позволяет гибко манипулировать данными локатора.

2.  **Взаимодействие с веб-элементами**: В зависимости от предоставленных данных, модуль может выполнять различные действия, такие как клики, отправка сообщений, выполнение событий и получение атрибутов из веб-элементов.

3.  **Обработка ошибок**: Модуль поддерживает продолжение выполнения в случае ошибки, что позволяет обрабатывать веб-страницы, которые могут иметь нестабильные элементы или требовать особого подхода.

4.  **Поддержка нескольких типов локаторов**: Обрабатывает как одиночные, так и множественные локаторы, обеспечивая идентификацию и взаимодействие с одним или несколькими веб-элементами одновременно.

Этот модуль обеспечивает гибкость и универсальность при работе с веб-элементами, позволяя автоматизировать сложные сценарии веб-взаимодействия.

## Содержание

- [Классы](#Классы)
    - [`ExecuteLocator`](#ExecuteLocator)
- [Функции](#Функции)
    - [`execute_locator`](#execute_locator)
    - [`evaluate_locator`](#evaluate_locator)
    - [`get_attribute_by_locator`](#get_attribute_by_locator)
    - [`get_webelement_by_locator`](#get_webelement_by_locator)
    - [`get_webelement_as_screenshot`](#get_webelement_as_screenshot)
    - [`execute_event`](#execute_event)
    - [`send_message`](#send_message)

## Классы

### `ExecuteLocator`

**Описание**: Обработчик локаторов для веб-элементов с использованием Selenium.

**Параметры**:
- `driver` (Optional[object], optional): Экземпляр веб-драйвера Selenium. По умолчанию `None`.
- `actions` (ActionChains): Объект для выполнения цепочек действий. Инициализируется в `__post_init__`.
- `by_mapping` (dict): Словарь, сопоставляющий строки с константами `By` из Selenium.
- `mode` (str): Режим работы модуля (`'debug'` или `'dev'`). По умолчанию `'debug'`.

**Методы**:
- `__post_init__`: Инициализирует объект `ActionChains` при наличии драйвера.

## Функции

### `execute_locator`

**Описание**: Выполняет действия над веб-элементом на основе предоставленного локатора.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора (словарь или SimpleNamespace).
- `timeout` (Optional[float], optional): Таймаут для поиска элемента. По умолчанию `0`.
- `timeout_for_event` (Optional[str], optional): Условие ожидания ('presence_of_element_located', 'element_to_be_clickable'). По умолчанию `'presence_of_element_located'`.
- `message` (Optional[str], optional): Сообщение для отправки. По умолчанию `None`.
- `typing_speed` (Optional[float], optional): Скорость печати для событий send_keys. По умолчанию `0`.
- `continue_on_error` (Optional[bool], optional): Продолжать ли выполнение при ошибке. По умолчанию `True`.

**Возвращает**:
- `str | list | dict | WebElement | bool`: Результат выполнения в зависимости от инструкций локатора.

### `evaluate_locator`

**Описание**: Вычисляет и обрабатывает атрибуты локатора.

**Параметры**:
- `attribute` (str | List[str] | dict): Атрибуты для вычисления.

**Возвращает**:
- `Optional[str | List[str] | dict]`: Вычисленные атрибуты.

### `get_attribute_by_locator`

**Описание**: Получает атрибуты из элемента или списка элементов, найденных по заданному локатору.

**Параметры**:
- `locator` (dict | SimpleNamespace): Локатор в виде словаря или SimpleNamespace.
- `timeout` (float, optional): Максимальное время ожидания появления элемента. По умолчанию `0`.
- `timeout_for_event` (str, optional): Тип условия ожидания. По умолчанию `'presence_of_element_located'`.
- `message` (Optional[str], optional): Сообщение. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость набора. По умолчанию `0`.
- `continue_on_error` (bool, optional): Продолжать ли выполнение при ошибке. По умолчанию `True`.

**Возвращает**:
- `WebElement | list[WebElement] | None`: Значение атрибута(ов) или словарь с атрибутами.

### `get_webelement_by_locator`

**Описание**: Извлекает веб-элемент или список элементов по указанному локатору.

**Параметры**:
- `locator` (dict | SimpleNamespace): Локатор в виде словаря или SimpleNamespace.
- `timeout` (Optional[float], optional): Таймаут для поиска элемента. По умолчанию `0`.
- `timeout_for_event` (Optional[str], optional): Условие ожидания (`presence_of_element_located` или `visibility_of_all_elements_located`). По умолчанию `'presence_of_element_located'`.

**Возвращает**:
- `WebElement | List[WebElement] | None`: Найденный веб-элемент(ы) или None.

### `get_webelement_as_screenshot`

**Описание**: Делает скриншот найденного веб-элемента.

**Параметры**:
- `locator` (dict | SimpleNamespace): Локатор в виде словаря или SimpleNamespace.
- `timeout` (float, optional): Максимальное время ожидания элемента. По умолчанию `5`.
- `timeout_for_event` (str, optional): Тип условия ожидания. По умолчанию `'presence_of_element_located'`.
- `message` (Optional[str], optional): Сообщение. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость набора. По умолчанию `0`.
- `continue_on_error` (bool, optional): Продолжать ли выполнение при ошибке. По умолчанию `True`.
- `webelement` (Optional[WebElement], optional): Предварительно полученный веб-элемент. По умолчанию `None`.

**Возвращает**:
- `BinaryIO | None`: Двоичный поток скриншота или `None` в случае неудачи.

### `execute_event`

**Описание**: Выполняет события, связанные с локатором.

**Параметры**:
- `locator` (SimpleNamespace | dict): Локатор, определяющий элемент и событие для выполнения.
- `timeout` (float, optional): Таймаут для поиска элемента. По умолчанию `5`.
- `timeout_for_event` (str, optional): Таймаут ожидания события. По умолчанию `'presence_of_element_located'`.
- `message` (Optional[str], optional): Сообщение для отправки с событием, если применимо. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость печати для событий `send_keys`. По умолчанию `0`.
- `continue_on_error` (bool, optional): Продолжать ли выполнение при ошибке. По умолчанию `True`.

**Возвращает**:
- `str | list[str] | bytes | list[bytes] | bool`: Результат выполнения события или `False`.

### `send_message`

**Описание**: Отправляет сообщение в веб-элемент.

**Параметры**:
- `locator` (SimpleNamespace | dict): Информация о местоположении элемента на странице.
- `timeout` (float, optional): Максимальное время ожидания элемента. По умолчанию `5`.
- `timeout_for_event` (str, optional): Тип условия ожидания. По умолчанию `'presence_of_element_located'`.
- `message` (str, optional): Сообщение для отправки. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость набора сообщения в секундах. По умолчанию `0`.
- `continue_on_error` (bool, optional): Продолжать ли выполнение при ошибке. По умолчанию `True`.

**Возвращает**:
- `bool`: `True`, если сообщение отправлено успешно, `False` в противном случае.