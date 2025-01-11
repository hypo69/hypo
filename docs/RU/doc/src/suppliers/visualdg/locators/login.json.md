# Документация для `login.json`

## Оглавление

1. [Обзор](#обзор)
2. [Раздел "login"](#раздел-login)
    - [open_login_inputs](#open_login_inputs)
    - [email_input](#email_input)
    - [continue_button](#continue_button)
    - [password_input](#password_input)
    - [keep_signed_in_checkbox](#keep_signed_in_checkbox)
    - [success_login_button](#success_login_button)

## Обзор

Файл `login.json` содержит JSON-объект, описывающий локаторы и действия для автоматизации процесса входа в систему. Он включает в себя локаторы для различных элементов формы входа, таких как поля ввода электронной почты и пароля, кнопки "Продолжить" и "Войти", а также чекбокса "Оставаться в системе". Каждый элемент имеет свои атрибуты, селекторы, параметры ожидания и события для имитации пользовательских действий.

## Раздел "login"

### `open_login_inputs`

**Описание**:
Локатор для открытия формы входа.

**Параметры**:
- `attribute` (null): Атрибут элемента.
- `by` (str): Тип селектора: "XPATH".
- `selector` (str): XPATH-выражение: "//span[@id='nav-link-accountList-nav-line-1']".
- `if_list` (str): Указывает, как работать со списком элементов: "first".
- `use_mouse` (bool): Указывает на использование мыши: `false`.
- `mandatory` (bool): Указывает, что элемент обязателен: `true`.
- `timeout` (int): Таймаут: `0`.
- `timeout_for_event` (str): Событие для таймаута: "presence_of_element_located".
- `event` (str): Событие для элемента: "click()".
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для действий: `null`.

### `email_input`

**Описание**:
Локатор для поля ввода электронной почты.

**Параметры**:
- `attribute` (null): Атрибут элемента.
- `by` (str): Тип селектора: "XPATH".
- `selector` (str): XPATH-выражение: "//input[@id='ap_email']".
- `if_list` (str): Указывает, как работать со списком элементов: "first".
- `use_mouse` (bool): Указывает на использование мыши: `false`.
- `mandatory` (bool): Указывает, что элемент обязателен: `true`.
- `timeout` (int): Таймаут: `0`.
- `timeout_for_event` (str): Событие для таймаута: "presence_of_element_located".
- `event` (str): Событие для элемента: "send_keys('972547519449')".
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для действий: `null`.

### `continue_button`

**Описание**:
Локатор для кнопки "Продолжить".

**Параметры**:
- `attribute` (null): Атрибут элемента.
- `by` (str): Тип селектора: "XPATH".
- `selector` (str): XPATH-выражение: "//input[@id='continue']".
- `if_list` (str): Указывает, как работать со списком элементов: "first".
- `use_mouse` (bool): Указывает на использование мыши: `false`.
- `mandatory` (bool): Указывает, что элемент обязателен: `true`.
- `timeout` (int): Таймаут: `0`.
- `timeout_for_event` (str): Событие для таймаута: "presence_of_element_located".
- `event` (str): Событие для элемента: "click()".
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для действий: `null`.

### `password_input`

**Описание**:
Локатор для поля ввода пароля.

**Параметры**:
- `attribute` (null): Атрибут элемента.
- `by` (str): Тип селектора: "XPATH".
- `selector` (str): XPATH-выражение: "//input[@id='ap_password']".
- `if_list` (str): Указывает, как работать со списком элементов: "first".
- `use_mouse` (bool): Указывает на использование мыши: `false`.
- `mandatory` (bool): Указывает, что элемент обязателен: `true`.
- `timeout` (int): Таймаут: `0`.
- `timeout_for_event` (str): Событие для таймаута: "presence_of_element_located".
- `event` (str): Событие для элемента: "send_keys('52UldxjzWGpdEQxWaNMY')".
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для действий: `null`.

### `keep_signed_in_checkbox`

**Описание**:
Локатор для чекбокса "Оставаться в системе".

**Параметры**:
- `attribute` (null): Атрибут элемента.
- `by` (str): Тип селектора: "XPATH".
- `selector` (str): XPATH-выражение: "//input[@name='rememberMe']".
- `if_list` (str): Указывает, как работать со списком элементов: "first".
- `use_mouse` (bool): Указывает на использование мыши: `false`.
- `mandatory` (bool): Указывает, что элемент обязателен: `true`.
- `timeout` (int): Таймаут: `0`.
- `timeout_for_event` (str): Событие для таймаута: "presence_of_element_located".
- `event` (str): Событие для элемента: "click()".
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для действий: `null`.

### `success_login_button`

**Описание**:
Локатор для кнопки подтверждения входа.

**Параметры**:
- `attribute` (null): Атрибут элемента.
- `by` (str): Тип селектора: "XPATH".
- `selector` (str): XPATH-выражение: "//input[@id='signInSubmit']".
- `if_list` (str): Указывает, как работать со списком элементов: "first".
- `use_mouse` (bool): Указывает на использование мыши: `false`.
- `mandatory` (bool): Указывает, что элемент обязателен: `true`.
- `timeout` (int): Таймаут: `0`.
- `timeout_for_event` (str): Событие для таймаута: "presence_of_element_located".
- `event` (str): Событие для элемента: "click()".
- `logic for action[AND|OR|XOR|VALUE|null]` (null): Логика для действий: `null`.