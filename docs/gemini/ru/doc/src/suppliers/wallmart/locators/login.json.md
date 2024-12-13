# Локаторы для страницы логина Walmart

## Обзор

Этот файл содержит JSON-структуру с локаторами для элементов страницы логина на сайте Walmart. Локаторы используются для автоматизации взаимодействия с элементами интерфейса во время тестирования или скрапинга.

## Оглавление
- [Обзор](#обзор)
- [Структура JSON](#структура-json)
- [Раздел `login`](#раздел-login)
    - [`open_login_inputs`](#open_login_inputs)
    - [`email_input`](#email_input)
    - [`continue_button`](#continue_button)
    - [`password_input`](#password_input)
    - [`keep_signed_in_checkbox`](#keep_signed_in_checkbox)
    - [`success_login_button`](#success_login_button)

## Структура JSON

Файл представлен в формате JSON и содержит единственный объект с ключом `login`, который содержит локаторы для различных элементов формы логина. Каждый локатор имеет следующие поля:

- `attribute` - Атрибут элемента (обычно `null`).
- `by` - Метод поиска элемента, в данном случае всегда `XPATH`.
- `selector` - XPATH-выражение для поиска элемента.
- `if_list` - Указание, какой элемент из списка нужно использовать, в данном случае всегда `first`.
- `use_mouse` - Флаг, указывающий, нужно ли использовать мышь для взаимодействия (всегда `false`).
- `mandatory` - Флаг, указывающий, является ли локатор обязательным (всегда `true`).
- `timeout` - Тайм-аут для поиска элемента (всегда `0`).
- `timeout_for_event` - Условие ожидания для события (всегда `presence_of_element_located`).
- `event` - Событие, которое нужно выполнить с элементом.
- `logic for action[AND|OR|XOR|VALUE|null]` - Логика для действий (всегда `null`).

## Раздел `login`

### `open_login_inputs`

**Описание**: Локатор для кнопки открытия формы логина.
**Поля**:
- `attribute` (null): Атрибут элемента.
- `by` (XPATH): Метод поиска.
- `selector` (`//span[@id='nav-link-accountList-nav-line-1']`): XPATH-выражение для поиска кнопки.
- `if_list` (`first`): Указание, какой элемент из списка нужно использовать.
- `use_mouse` (false): Указывает, использовать ли мышь.
- `mandatory` (true): Является ли локатор обязательным.
- `timeout` (0): Тайм-аут поиска элемента.
- `timeout_for_event` (`presence_of_element_located`): Условие ожидания для события.
- `event` (`click()`): Событие, которое нужно выполнить.
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для действий.

### `email_input`

**Описание**: Локатор для поля ввода электронной почты.
**Поля**:
- `attribute` (null): Атрибут элемента.
- `by` (XPATH): Метод поиска.
- `selector` (`//input[@id='ap_email']`): XPATH-выражение для поиска поля ввода.
- `if_list` (`first`): Указание, какой элемент из списка нужно использовать.
- `use_mouse` (false): Указывает, использовать ли мышь.
- `mandatory` (true): Является ли локатор обязательным.
- `timeout` (0): Тайм-аут поиска элемента.
- `timeout_for_event` (`presence_of_element_located`): Условие ожидания для события.
- `event` (`send_keys('972547519449')`): Событие, которое нужно выполнить.
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для действий.

### `continue_button`

**Описание**: Локатор для кнопки "Продолжить" после ввода электронной почты.
**Поля**:
- `attribute` (null): Атрибут элемента.
- `by` (XPATH): Метод поиска.
- `selector` (`//input[@id='continue']`): XPATH-выражение для поиска кнопки.
- `if_list` (`first`): Указание, какой элемент из списка нужно использовать.
- `use_mouse` (false): Указывает, использовать ли мышь.
- `mandatory` (true): Является ли локатор обязательным.
- `timeout` (0): Тайм-аут поиска элемента.
- `timeout_for_event` (`presence_of_element_located`): Условие ожидания для события.
- `event` (`click()`): Событие, которое нужно выполнить.
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для действий.

### `password_input`

**Описание**: Локатор для поля ввода пароля.
**Поля**:
- `attribute` (null): Атрибут элемента.
- `by` (XPATH): Метод поиска.
- `selector` (`//input[@id='ap_password']`): XPATH-выражение для поиска поля ввода.
- `if_list` (`first`): Указание, какой элемент из списка нужно использовать.
- `use_mouse` (false): Указывает, использовать ли мышь.
- `mandatory` (true): Является ли локатор обязательным.
- `timeout` (0): Тайм-аут поиска элемента.
- `timeout_for_event` (`presence_of_element_located`): Условие ожидания для события.
- `event` (`send_keys('52UldxjzWGpdEQxWaNMY')`): Событие, которое нужно выполнить.
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для действий.

### `keep_signed_in_checkbox`

**Описание**: Локатор для чекбокса "Оставаться в системе".
**Поля**:
- `attribute` (null): Атрибут элемента.
- `by` (XPATH): Метод поиска.
- `selector` (`//input[@name='rememberMe']`): XPATH-выражение для поиска чекбокса.
- `if_list` (`first`): Указание, какой элемент из списка нужно использовать.
- `use_mouse` (false): Указывает, использовать ли мышь.
- `mandatory` (true): Является ли локатор обязательным.
- `timeout` (0): Тайм-аут поиска элемента.
- `timeout_for_event` (`presence_of_element_located`): Условие ожидания для события.
- `event` (`click()`): Событие, которое нужно выполнить.
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для действий.

### `success_login_button`

**Описание**: Локатор для кнопки "Войти" после ввода пароля.
**Поля**:
- `attribute` (null): Атрибут элемента.
- `by` (XPATH): Метод поиска.
- `selector` (`//input[@id='signInSubmit']`): XPATH-выражение для поиска кнопки.
- `if_list` (`first`): Указание, какой элемент из списка нужно использовать.
- `use_mouse` (false): Указывает, использовать ли мышь.
- `mandatory` (true): Является ли локатор обязательным.
- `timeout` (0): Тайм-аут поиска элемента.
- `timeout_for_event` (`presence_of_element_located`): Условие ожидания для события.
- `event` (`click()`): Событие, которое нужно выполнить.
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для действий.