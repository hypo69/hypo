# Локаторы для страницы логина ETZMaleh

## Обзор

Этот файл содержит JSON-объект с локаторами для страницы логина ETZMaleh. Локаторы используются для поиска элементов на веб-странице во время автоматизированного тестирования или веб-скрейпинга.

## Оглавление

- [Обзор](#обзор)
- [Локаторы](#локаторы)
    - [`open_login_inputs`](#open_login_inputs)
    - [`email_input`](#email_input)
    - [`continue_button`](#continue_button)
    - [`password_input`](#password_input)
    - [`keep_signed_in_checkbox`](#keep_signed_in_checkbox)
    - [`success_login_button`](#success_login_button)

## Локаторы

### `open_login_inputs`

**Описание**: Локатор для кнопки открытия формы логина.

**Параметры**:
- `attribute` (null): Атрибут элемента, который не используется.
- `by` (str): Тип локатора - `XPATH`.
- `selector` (str): XPATH-выражение для поиска элемента `//span[@id='nav-link-accountList-nav-line-1']`.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка. Значение `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь. Значение `false`.
- `mandatory` (bool): Указывает, что локатор обязателен. Значение `true`.
- `timeout` (int): Таймаут для ожидания элемента. Значение `0`.
- `timeout_for_event` (str): Событие, которое нужно ожидать. Значение `presence_of_element_located`.
- `event` (str): Событие, которое нужно совершить. Значение `click()`.
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для выполнения действий, не используется.

### `email_input`

**Описание**: Локатор для поля ввода электронной почты.

**Параметры**:
- `attribute` (null): Атрибут элемента, который не используется.
- `by` (str): Тип локатора - `XPATH`.
- `selector` (str): XPATH-выражение для поиска элемента `//input[@id='ap_email']`.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка. Значение `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь. Значение `false`.
- `mandatory` (bool): Указывает, что локатор обязателен. Значение `true`.
- `timeout` (int): Таймаут для ожидания элемента. Значение `0`.
- `timeout_for_event` (str): Событие, которое нужно ожидать. Значение `presence_of_element_located`.
- `event` (str): Событие, которое нужно совершить. Значение `send_keys('972547519449')`.
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для выполнения действий, не используется.

### `continue_button`

**Описание**: Локатор для кнопки "Продолжить".

**Параметры**:
- `attribute` (null): Атрибут элемента, который не используется.
- `by` (str): Тип локатора - `XPATH`.
- `selector` (str): XPATH-выражение для поиска элемента `//input[@id='continue']`.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка. Значение `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь. Значение `false`.
- `mandatory` (bool): Указывает, что локатор обязателен. Значение `true`.
- `timeout` (int): Таймаут для ожидания элемента. Значение `0`.
- `timeout_for_event` (str): Событие, которое нужно ожидать. Значение `presence_of_element_located`.
- `event` (str): Событие, которое нужно совершить. Значение `click()`.
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для выполнения действий, не используется.

### `password_input`

**Описание**: Локатор для поля ввода пароля.

**Параметры**:
- `attribute` (null): Атрибут элемента, который не используется.
- `by` (str): Тип локатора - `XPATH`.
- `selector` (str): XPATH-выражение для поиска элемента `//input[@id='ap_password']`.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка. Значение `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь. Значение `false`.
- `mandatory` (bool): Указывает, что локатор обязателен. Значение `true`.
- `timeout` (int): Таймаут для ожидания элемента. Значение `0`.
- `timeout_for_event` (str): Событие, которое нужно ожидать. Значение `presence_of_element_located`.
- `event` (str): Событие, которое нужно совершить. Значение `send_keys('52UldxjzWGpdEQxWaNMY')`.
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для выполнения действий, не используется.

### `keep_signed_in_checkbox`

**Описание**: Локатор для чекбокса "Оставаться в системе".

**Параметры**:
- `attribute` (null): Атрибут элемента, который не используется.
- `by` (str): Тип локатора - `XPATH`.
- `selector` (str): XPATH-выражение для поиска элемента `//input[@name='rememberMe']`.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка. Значение `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь. Значение `false`.
- `mandatory` (bool): Указывает, что локатор обязателен. Значение `true`.
- `timeout` (int): Таймаут для ожидания элемента. Значение `0`.
- `timeout_for_event` (str): Событие, которое нужно ожидать. Значение `presence_of_element_located`.
- `event` (str): Событие, которое нужно совершить. Значение `click()`.
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для выполнения действий, не используется.

### `success_login_button`

**Описание**: Локатор для кнопки "Войти".

**Параметры**:
- `attribute` (null): Атрибут элемента, который не используется.
- `by` (str): Тип локатора - `XPATH`.
- `selector` (str): XPATH-выражение для поиска элемента `//input[@id='signInSubmit']`.
- `if_list` (str): Указывает, что нужно взять первый элемент из списка. Значение `first`.
- `use_mouse` (bool): Указывает, нужно ли использовать мышь. Значение `false`.
- `mandatory` (bool): Указывает, что локатор обязателен. Значение `true`.
- `timeout` (int): Таймаут для ожидания элемента. Значение `0`.
- `timeout_for_event` (str): Событие, которое нужно ожидать. Значение `presence_of_element_located`.
- `event` (str): Событие, которое нужно совершить. Значение `click()`.
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для выполнения действий, не используется.