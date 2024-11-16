## \file hypotez/src/webdriver/_docs/executor.2.ru.md
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.webdriver._docs """
MODE = 'debug'
подробные описания для каждой функции модуля `executor`:

### 1. `execute_locator`
```python
def execute_locator(locator: dict, message: str = '', typing_speed: float = 0.0, continue_on_error: bool = True) -> any:
    """ Executes actions on a web element based on the provided locator.

    @param locator: A dictionary or object containing locator information (e.g., type, selector).
    @param message: Optional message to send to the web element (e.g., text to enter).
    @param typing_speed: Speed of typing when sending a message (in seconds between keystrokes).
    @param continue_on_error: Flag indicating whether to continue execution if an error occurs.
    
    @return: The result of the locator execution, which could be the web element, a list of elements, an attribute value, or action result.
    """
    ...
```
- **Назначение**: Выполняет действия на веб-элементе, используя указанный локатор.
- **Параметры**:
  - `locator`: Словарь или объект с информацией о локаторе (например, тип поиска и селектор).
  - `message`: Сообщение для отправки элементу (например, текст для ввода).
  - `typing_speed`: Скорость набора текста, если отправляется сообщение.
  - `continue_on_error`: Флаг для продолжения выполнения в случае ошибки.
- **Возвращаемое значение**: Результат выполнения локатора, который может быть веб-элементом, списком элементов, значением атрибута или результатом действия.

### 2. `get_webelement_by_locator`
```python
def get_webelement_by_locator(locator: dict) -> any:
    """ Finds and returns a web element based on the provided locator.

    @param locator: A dictionary or object containing locator information (e.g., type, selector).
    
    @return: The found web element or a list of elements, depending on the locator's specification.
    """
    ...
```
- **Назначение**: Находит и возвращает веб-элемент(ы) на странице, используя локатор.
- **Параметры**:
  - `locator`: Словарь или объект с информацией о локаторе.
- **Возвращаемое значение**: Один или несколько веб-элементов, найденных по локатору.

### 3. `get_attribute_by_locator`
```python
def get_attribute_by_locator(locator: dict, message: str = '') -> any:
    """ Retrieves the attribute value of a web element identified by the locator.

    @param locator: A dictionary or object containing locator information (e.g., type, selector).
    @param message: Optional message to send to the web element (e.g., text to enter before retrieving attribute).
    
    @return: The value of the attribute of the found web element, or None if an error occurs.
    """
    ...
```
- **Назначение**: Получает значение атрибута веб-элемента, найденного по локатору.
- **Параметры**:
  - `locator`: Словарь или объект с информацией о локаторе.
  - `message`: Сообщение для отправки элементу перед получением атрибута (необязательно).
- **Возвращаемое значение**: Значение атрибута веб-элемента.

### 4. `send_message`
```python
def send_message(locator: dict, message: str, typing_speed: float = 0.0, continue_on_error: bool = True) -> bool:
    """ Sends a message (e.g., text) to a web element identified by the locator.

    @param locator: A dictionary or object containing locator information (e.g., type, selector).
    @param message: The message to send to the web element.
    @param typing_speed: Speed of typing when sending the message (in seconds between keystrokes).
    @param continue_on_error: Flag indicating whether to continue execution if an error occurs.
    
    @return: True if the message is sent successfully, otherwise False.
    """
    ...
```
- **Назначение**: Отправляет сообщение (например, текст) веб-элементу, используя локатор.
- **Параметры**:
  - `locator`: Словарь или объект с информацией о локаторе.
  - `message`: Сообщение для отправки элементу.
  - `typing_speed`: Скорость набора текста, если сообщение отправляется по частям.
  - `continue_on_error`: Флаг для продолжения выполнения в случае ошибки.
- **Возвращаемое значение**: `True`, если сообщение успешно отправлено, или `False`, если произошла ошибка.

### 5. `get_url`
```python
def get_url(url: str, protocol: str = 'https://') -> bool:
    """ Retrieves HTML content from a specified URL or file path.

    @param url: The URL or file path to fetch the HTML content from.
    @param protocol: The protocol to use for URL (default is 'https://').
    
    @return: True if the content is successfully fetched, otherwise False.
    """
    ...
```
- **Назначение**: Загружает HTML-контент с указанного URL-адреса или локального файла.
- **Параметры**:
  - `url`: URL-адрес или путь к файлу для получения HTML-контента.
  - `protocol`: Протокол для URL (по умолчанию `https://`).
- **Возвращаемое значение**: `True`, если контент успешно загружен, или `False`, если произошла ошибка.

Эти функции обеспечивают гибкий интерфейс для взаимодействия с веб-страницами и их элементами, позволяя выполнять автоматизированные действия и извлекать данные.