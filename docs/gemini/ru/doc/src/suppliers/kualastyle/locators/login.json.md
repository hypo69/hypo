# Локаторы страницы авторизации Kualastyle

## Обзор

Данный файл содержит JSON-объект с локаторами элементов для страницы авторизации Kualastyle. Локаторы используются для автоматизации действий на странице, таких как ввод данных и нажатие кнопок.

## Оглавление
1.  [Обзор](#обзор)
2.  [Локаторы](#локаторы)
    - [open_login_inputs](#open_login_inputs)
    - [email_input](#email_input)
    - [continue_button](#continue_button)
    - [password_input](#password_input)
    - [keep_signed_in_checkbox](#keep_signed_in_checkbox)
    - [success_login_button](#success_login_button)

## Локаторы

### `open_login_inputs`
**Описание**: Локатор для открытия поля ввода логина.
**Параметры**:
- `attribute` (null): Атрибут элемента.
- `by` (str): Метод поиска ("XPATH").
- `selector` (str): XPath-выражение для поиска элемента.
- `if_list` (str): Выбор элемента из списка ("first").
- `use_mouse` (bool): Использовать ли мышь (false).
- `mandatory` (bool): Является ли элемент обязательным (true).
- `timeout` (int): Тайм-аут ожидания (0).
- `timeout_for_event` (str): Тайм-аут для события ("presence_of_element_located").
- `event` (str): Событие для элемента ("click()").
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для действия.

### `email_input`
**Описание**: Локатор для поля ввода электронной почты.
**Параметры**:
- `attribute` (null): Атрибут элемента.
- `by` (str): Метод поиска ("XPATH").
- `selector` (str): XPath-выражение для поиска элемента.
- `if_list` (str): Выбор элемента из списка ("first").
- `use_mouse` (bool): Использовать ли мышь (false).
- `mandatory` (bool): Является ли элемент обязательным (true).
- `timeout` (int): Тайм-аут ожидания (0).
- `timeout_for_event` (str): Тайм-аут для события ("presence_of_element_located").
- `event` (str): Событие для элемента ("send_keys('972547519449')").
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для действия.

### `continue_button`
**Описание**: Локатор для кнопки "Продолжить".
**Параметры**:
- `attribute` (null): Атрибут элемента.
- `by` (str): Метод поиска ("XPATH").
- `selector` (str): XPath-выражение для поиска элемента.
- `if_list` (str): Выбор элемента из списка ("first").
- `use_mouse` (bool): Использовать ли мышь (false).
- `mandatory` (bool): Является ли элемент обязательным (true).
- `timeout` (int): Тайм-аут ожидания (0).
- `timeout_for_event` (str): Тайм-аут для события ("presence_of_element_located").
- `event` (str): Событие для элемента ("click()").
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для действия.

### `password_input`
**Описание**: Локатор для поля ввода пароля.
**Параметры**:
- `attribute` (null): Атрибут элемента.
- `by` (str): Метод поиска ("XPATH").
- `selector` (str): XPath-выражение для поиска элемента.
- `if_list` (str): Выбор элемента из списка ("first").
- `use_mouse` (bool): Использовать ли мышь (false).
- `mandatory` (bool): Является ли элемент обязательным (true).
- `timeout` (int): Тайм-аут ожидания (0).
- `timeout_for_event` (str): Тайм-аут для события ("presence_of_element_located").
- `event` (str): Событие для элемента ("send_keys('52UldxjzWGpdEQxWaNMY')").
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для действия.

### `keep_signed_in_checkbox`
**Описание**: Локатор для чекбокса "Оставаться в системе".
**Параметры**:
- `attribute` (null): Атрибут элемента.
- `by` (str): Метод поиска ("XPATH").
- `selector` (str): XPath-выражение для поиска элемента.
- `if_list` (str): Выбор элемента из списка ("first").
- `use_mouse` (bool): Использовать ли мышь (false).
- `mandatory` (bool): Является ли элемент обязательным (true).
- `timeout` (int): Тайм-аут ожидания (0).
- `timeout_for_event` (str): Тайм-аут для события ("presence_of_element_located").
- `event` (str): Событие для элемента ("click()").
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для действия.

### `success_login_button`
**Описание**: Локатор для кнопки "Войти".
**Параметры**:
- `attribute` (null): Атрибут элемента.
- `by` (str): Метод поиска ("XPATH").
- `selector` (str): XPath-выражение для поиска элемента.
- `if_list` (str): Выбор элемента из списка ("first").
- `use_mouse` (bool): Использовать ли мышь (false).
- `mandatory` (bool): Является ли элемент обязательным (true).
- `timeout` (int): Тайм-аут ожидания (0).
- `timeout_for_event` (str): Тайм-аут для события ("presence_of_element_located").
- `event` (str): Событие для элемента ("click()").
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для действия.