# Модуль `executor`

Этот модуль предоставляет функции для взаимодействия с веб-элементами на веб-страницах.  Он позволяет выполнять различные операции, такие как поиск элементов, отправка сообщений (ввода текста), получение атрибутов и загрузка контента с URL.

## Функции:

### `execute_locator`

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

**Описание:** Выполняет заданное действие на элементе веб-страницы, используя указанные параметры локатора.  Функция может выполнять различные действия, включая отправку сообщений, получение атрибутов и поиск других элементов. Важно, что функция позволяет задавать скорость ввода текста (`typing_speed`) и обрабатывает ошибки (`continue_on_error`).


### `get_webelement_by_locator`

```python
def get_webelement_by_locator(locator: dict) -> any:
    """ Finds and returns a web element based on the provided locator.

    @param locator: A dictionary or object containing locator information (e.g., type, selector).

    @return: The found web element or a list of elements, depending on the locator's specification.
    """
    ...
```

**Описание:**  Ищет и возвращает один или несколько веб-элементов на странице, используя предоставленный локатор. Возвращаемый тип зависит от спецификаций локатора (например, если локатор указывает на группу элементов, то будет возвращён список).

### `get_attribute_by_locator`

```python
def get_attribute_by_locator(locator: dict, message: str = '') -> any:
    """ Retrieves the attribute value of a web element identified by the locator.

    @param locator: A dictionary or object containing locator information (e.g., type, selector).
    @param message: Optional message to send to the web element (e.g., text to enter before retrieving attribute).

    @return: The value of the attribute of the found web element, or None if an error occurs.
    """
    ...
```

**Описание:** Получает значение атрибута указанного веб-элемента.  Дополнительно, функция может принимать `message`, чтобы выполнить действие (например, ввод текста) перед чтением атрибута.

### `send_message`

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

**Описание:** Отправляет сообщение (текст) указанному веб-элементу.  Возможность задавать `typing_speed` делает отправку более реалистичной.  Флаг `continue_on_error` позволяет функции продолжать работу при ошибках, вместо прерывания.

### `get_url`

```python
def get_url(url: str, protocol: str = 'https://') -> bool:
    """ Retrieves HTML content from a specified URL or file path.

    @param url: The URL or file path to fetch the HTML content from.
    @param protocol: The protocol to use for URL (default is 'https://').

    @return: True if the content is successfully fetched, otherwise False.
    """
    ...
```

**Описание:** Загружает HTML-контент с заданного URL-адреса или локального файла.  Позволяет указать протокол (по умолчанию `https://`). Возвращает `True`, если загрузка успешна, и `False` в случае ошибок.


В целом, модуль `executor` предоставляет удобный и гибкий инструментарий для работы с веб-элементами, обеспечивая высокую степень автоматизации и контроля.