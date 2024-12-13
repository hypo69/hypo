# Документация для `login.json`

## Обзор

Файл `login.json` содержит JSON-конфигурацию локаторов для элементов веб-страницы, используемых для процесса входа в аккаунт на Gearbest. Каждый локатор содержит информацию для нахождения элемента, а также действия, которые нужно с ним произвести.

## Содержание

- [Структура JSON](#структура-json)
    - [`login`](#login)
        - [`open_login_inputs`](#open_login_inputs)
        - [`email_input`](#email_input)
        - [`continue_button`](#continue_button)
        - [`password_input`](#password_input)
        - [`keep_signed_in_checkbox`](#keep_signed_in_checkbox)
        - [`success_login_button`](#success_login_button)

## Структура JSON

### `login`

Объект `login` содержит локаторы для элементов, участвующих в процессе входа в аккаунт.

#### `open_login_inputs`

**Описание**: Локатор кнопки для открытия формы входа.

**Параметры**:
- `attribute`: (`null`) Атрибут элемента.
- `by`: (`XPATH`) Метод поиска элемента.
- `selector`: (`//span[@id='nav-link-accountList-nav-line-1']`) XPATH-селектор элемента.
- `if_list`: (`first`) Указывает, какой элемент из списка следует выбрать (если селектор возвращает список).
- `use_mouse`: (`false`) Указывает, нужно ли использовать мышь для действия.
- `mandatory`: (`true`) Указывает, является ли элемент обязательным.
- `timeout`: (`0`) Тайм-аут ожидания элемента.
- `timeout_for_event`: (`presence_of_element_located`) Тип ожидания элемента.
- `event`: (`click()`) Событие для выполнения.
- `logic for action[AND|OR|XOR|VALUE|null]`: (`null`) Логика для действия.

#### `email_input`

**Описание**: Локатор для поля ввода email.

**Параметры**:
- `attribute`: (`null`) Атрибут элемента.
- `by`: (`XPATH`) Метод поиска элемента.
- `selector`: (`//input[@id='ap_email']`) XPATH-селектор элемента.
- `if_list`: (`first`) Указывает, какой элемент из списка следует выбрать (если селектор возвращает список).
- `use_mouse`: (`false`) Указывает, нужно ли использовать мышь для действия.
- `mandatory`: (`true`) Указывает, является ли элемент обязательным.
- `timeout`: (`0`) Тайм-аут ожидания элемента.
- `timeout_for_event`: (`presence_of_element_located`) Тип ожидания элемента.
- `event`: (`send_keys('972547519449')`) Событие для выполнения.
- `logic for action[AND|OR|XOR|VALUE|null]`: (`null`) Логика для действия.

#### `continue_button`

**Описание**: Локатор для кнопки "Продолжить".

**Параметры**:
- `attribute`: (`null`) Атрибут элемента.
- `by`: (`XPATH`) Метод поиска элемента.
- `selector`: (`//input[@id='continue']`) XPATH-селектор элемента.
- `if_list`: (`first`) Указывает, какой элемент из списка следует выбрать (если селектор возвращает список).
- `use_mouse`: (`false`) Указывает, нужно ли использовать мышь для действия.
- `mandatory`: (`true`) Указывает, является ли элемент обязательным.
- `timeout`: (`0`) Тайм-аут ожидания элемента.
- `timeout_for_event`: (`presence_of_element_located`) Тип ожидания элемента.
- `event`: (`click()`) Событие для выполнения.
- `logic for action[AND|OR|XOR|VALUE|null]`: (`null`) Логика для действия.

#### `password_input`

**Описание**: Локатор для поля ввода пароля.

**Параметры**:
- `attribute`: (`null`) Атрибут элемента.
- `by`: (`XPATH`) Метод поиска элемента.
- `selector`: (`//input[@id='ap_password']`) XPATH-селектор элемента.
- `if_list`: (`first`) Указывает, какой элемент из списка следует выбрать (если селектор возвращает список).
- `use_mouse`: (`false`) Указывает, нужно ли использовать мышь для действия.
- `mandatory`: (`true`) Указывает, является ли элемент обязательным.
- `timeout`: (`0`) Тайм-аут ожидания элемента.
- `timeout_for_event`: (`presence_of_element_located`) Тип ожидания элемента.
- `event`: (`send_keys('52UldxjzWGpdEQxWaNMY')`) Событие для выполнения.
- `logic for action[AND|OR|XOR|VALUE|null]`: (`null`) Логика для действия.

#### `keep_signed_in_checkbox`

**Описание**: Локатор для чекбокса "Оставаться в системе".

**Параметры**:
- `attribute`: (`null`) Атрибут элемента.
- `by`: (`XPATH`) Метод поиска элемента.
- `selector`: (`//input[@name='rememberMe']`) XPATH-селектор элемента.
- `if_list`: (`first`) Указывает, какой элемент из списка следует выбрать (если селектор возвращает список).
- `use_mouse`: (`false`) Указывает, нужно ли использовать мышь для действия.
- `mandatory`: (`true`) Указывает, является ли элемент обязательным.
- `timeout`: (`0`) Тайм-аут ожидания элемента.
- `timeout_for_event`: (`presence_of_element_located`) Тип ожидания элемента.
- `event`: (`click()`) Событие для выполнения.
- `logic for action[AND|OR|XOR|VALUE|null]`: (`null`) Логика для действия.

#### `success_login_button`

**Описание**: Локатор для кнопки подтверждения входа в аккаунт.

**Параметры**:
- `attribute`: (`null`) Атрибут элемента.
- `by`: (`XPATH`) Метод поиска элемента.
- `selector`: (`//input[@id='signInSubmit']`) XPATH-селектор элемента.
- `if_list`: (`first`) Указывает, какой элемент из списка следует выбрать (если селектор возвращает список).
- `use_mouse`: (`false`) Указывает, нужно ли использовать мышь для действия.
- `mandatory`: (`true`) Указывает, является ли элемент обязательным.
- `timeout`: (`0`) Тайм-аут ожидания элемента.
- `timeout_for_event`: (`presence_of_element_located`) Тип ожидания элемента.
- `event`: (`click()`) Событие для выполнения.
- `logic for action[AND|OR|XOR|VALUE|null]`: (`null`) Логика для действия.