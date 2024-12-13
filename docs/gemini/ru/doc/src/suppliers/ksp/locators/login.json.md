# Локаторы для страницы логина KSP

## Обзор

Этот файл содержит JSON-структуру с локаторами для элементов страницы логина на сайте KSP. Локаторы используются для автоматизации взаимодействия с веб-интерфейсом.

## Оглавление

1.  [Обзор](#обзор)
2.  [Структура JSON](#структура-json)
    -   [login](#login)
        -   [open_login_inputs](#open_login_inputs)
        -   [email_input](#email_input)
        -   [continue_button](#continue_button)
        -   [password_input](#password_input)
        -   [keep_signed_in_checkbox](#keep_signed_in_checkbox)
        -   [success_login_button](#success_login_button)

## Структура JSON

### `login`

Объект, содержащий локаторы для различных элементов страницы логина.

#### `open_login_inputs`

**Описание**: Локатор для открытия формы ввода логина.

**Параметры**:

-   `attribute` (null): Аттрибут не используется.
-   `by` (str): Метод поиска элемента - "XPATH".
-   `selector` (str): XPath-селектор элемента - `//span[@id='nav-link-accountList-nav-line-1']`.
-    `if_list` (str): Указывает, как обрабатывать список найденных элементов: "first".
-    `use_mouse` (bool): Использовать мышь для взаимодействия с элементом: `false`.
-    `mandatory` (bool): Элемент обязателен на странице: `true`.
-    `timeout` (int): Время ожидания элемента в секундах: `0`.
-    `timeout_for_event` (str): Событие, которое нужно отслеживать во время ожидания: `presence_of_element_located`.
-    `event` (str): Событие, которое нужно выполнить при нахождении элемента: `click()`.
-   `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика действия не используется.

#### `email_input`

**Описание**: Локатор для поля ввода электронной почты.

**Параметры**:

-   `attribute` (null): Аттрибут не используется.
-   `by` (str): Метод поиска элемента - "XPATH".
-   `selector` (str): XPath-селектор элемента - `//input[@id='ap_email']`.
-    `if_list` (str): Указывает, как обрабатывать список найденных элементов: "first".
-    `use_mouse` (bool): Использовать мышь для взаимодействия с элементом: `false`.
-    `mandatory` (bool): Элемент обязателен на странице: `true`.
-    `timeout` (int): Время ожидания элемента в секундах: `0`.
-    `timeout_for_event` (str): Событие, которое нужно отслеживать во время ожидания: `presence_of_element_located`.
-    `event` (str): Событие, которое нужно выполнить при нахождении элемента: `send_keys('972547519449')`.
-   `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика действия не используется.

#### `continue_button`

**Описание**: Локатор для кнопки "Продолжить".

**Параметры**:

-   `attribute` (null): Аттрибут не используется.
-   `by` (str): Метод поиска элемента - "XPATH".
-   `selector` (str): XPath-селектор элемента - `//input[@id='continue']`.
-    `if_list` (str): Указывает, как обрабатывать список найденных элементов: "first".
-    `use_mouse` (bool): Использовать мышь для взаимодействия с элементом: `false`.
-    `mandatory` (bool): Элемент обязателен на странице: `true`.
-    `timeout` (int): Время ожидания элемента в секундах: `0`.
-    `timeout_for_event` (str): Событие, которое нужно отслеживать во время ожидания: `presence_of_element_located`.
-    `event` (str): Событие, которое нужно выполнить при нахождении элемента: `click()`.
-   `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика действия не используется.

#### `password_input`

**Описание**: Локатор для поля ввода пароля.

**Параметры**:

-   `attribute` (null): Аттрибут не используется.
-   `by` (str): Метод поиска элемента - "XPATH".
-   `selector` (str): XPath-селектор элемента - `//input[@id='ap_password']`.
-    `if_list` (str): Указывает, как обрабатывать список найденных элементов: "first".
-    `use_mouse` (bool): Использовать мышь для взаимодействия с элементом: `false`.
-    `mandatory` (bool): Элемент обязателен на странице: `true`.
-    `timeout` (int): Время ожидания элемента в секундах: `0`.
-    `timeout_for_event` (str): Событие, которое нужно отслеживать во время ожидания: `presence_of_element_located`.
-    `event` (str): Событие, которое нужно выполнить при нахождении элемента: `send_keys('52UldxjzWGpdEQxWaNMY')`.
-   `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика действия не используется.

#### `keep_signed_in_checkbox`

**Описание**: Локатор для чекбокса "Оставаться в системе".

**Параметры**:

-   `attribute` (null): Аттрибут не используется.
-   `by` (str): Метод поиска элемента - "XPATH".
-   `selector` (str): XPath-селектор элемента - `//input[@name='rememberMe']`.
-    `if_list` (str): Указывает, как обрабатывать список найденных элементов: "first".
-    `use_mouse` (bool): Использовать мышь для взаимодействия с элементом: `false`.
-    `mandatory` (bool): Элемент обязателен на странице: `true`.
-    `timeout` (int): Время ожидания элемента в секундах: `0`.
-    `timeout_for_event` (str): Событие, которое нужно отслеживать во время ожидания: `presence_of_element_located`.
-    `event` (str): Событие, которое нужно выполнить при нахождении элемента: `click()`.
-   `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика действия не используется.

#### `success_login_button`

**Описание**: Локатор для кнопки подтверждения входа.

**Параметры**:

-   `attribute` (null): Аттрибут не используется.
-   `by` (str): Метод поиска элемента - "XPATH".
-   `selector` (str): XPath-селектор элемента - `//input[@id='signInSubmit']`.
-    `if_list` (str): Указывает, как обрабатывать список найденных элементов: "first".
-    `use_mouse` (bool): Использовать мышь для взаимодействия с элементом: `false`.
-    `mandatory` (bool): Элемент обязателен на странице: `true`.
-    `timeout` (int): Время ожидания элемента в секундах: `0`.
-    `timeout_for_event` (str): Событие, которое нужно отслеживать во время ожидания: `presence_of_element_located`.
-    `event` (str): Событие, которое нужно выполнить при нахождении элемента: `click()`.
-   `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика действия не используется.