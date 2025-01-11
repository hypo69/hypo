# Документация для `hypotez/src/suppliers/bangood/locators/login.json`

## Обзор

Файл `login.json` содержит JSON-объект, описывающий локаторы веб-элементов для страницы входа в аккаунт Bangood. Каждый локатор определяет способ поиска элемента на веб-странице, а также необходимые действия для взаимодействия с ним.

## Оглавление

- [Обзор](#обзор)
- [Локаторы](#локаторы)
  - [open_login_inputs](#open_login_inputs)
  - [email_input](#email_input)
  - [continue_button](#continue_button)
  - [password_input](#password_input)
  - [keep_signed_in_checkbox](#keep_signed_in_checkbox)
  - [success_login_button](#success_login_button)

## Локаторы

### `open_login_inputs`

**Описание**: Локатор для кнопки или ссылки, открывающей форму входа.

**Параметры**:
- `attribute`:  `null`, атрибут, по которому не выполняется поиск.
- `by`: `"XPATH"`,  метод поиска элемента.
- `selector`:  `"//span[@id='nav-link-accountList-nav-line-1']"`,  Xpath селектор элемента.
- `if_list`: `"first"`,  брать первый элемент из списка.
- `use_mouse`: `false`,  не использовать мышь для взаимодействия.
- `mandatory`: `true`,  элемент является обязательным для взаимодействия.
- `timeout`: `0`,  таймаут поиска элемента.
- `timeout_for_event`: `"presence_of_element_located"`, событие ожидания появления элемента.
- `event`: `"click()"`,  событие, которое нужно выполнить на элементе.
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`, логика для действия.

### `email_input`

**Описание**: Локатор для поля ввода электронной почты.

**Параметры**:
- `attribute`: `null`, атрибут, по которому не выполняется поиск.
- `by`: `"XPATH"`, метод поиска элемента.
- `selector`: `"//input[@id='ap_email']"`, Xpath селектор элемента.
- `if_list`: `"first"`, брать первый элемент из списка.
- `use_mouse`: `false`, не использовать мышь для взаимодействия.
- `mandatory`: `true`, элемент является обязательным для взаимодействия.
- `timeout`: `0`, таймаут поиска элемента.
- `timeout_for_event`: `"presence_of_element_located"`, событие ожидания появления элемента.
- `event`: `"send_keys('972547519449')"`,  событие, которое нужно выполнить на элементе.
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`, логика для действия.

### `continue_button`

**Описание**: Локатор для кнопки "Продолжить" после ввода электронной почты.

**Параметры**:
- `attribute`: `null`, атрибут, по которому не выполняется поиск.
- `by`: `"XPATH"`,  метод поиска элемента.
- `selector`: `"//input[@id='continue']"`,  Xpath селектор элемента.
- `if_list`: `"first"`, брать первый элемент из списка.
- `use_mouse`: `false`,  не использовать мышь для взаимодействия.
- `mandatory`: `true`,  элемент является обязательным для взаимодействия.
- `timeout`: `0`, таймаут поиска элемента.
- `timeout_for_event`: `"presence_of_element_located"`,  событие ожидания появления элемента.
- `event`: `"click()"`, событие, которое нужно выполнить на элементе.
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`, логика для действия.

### `password_input`

**Описание**: Локатор для поля ввода пароля.

**Параметры**:
- `attribute`: `null`, атрибут, по которому не выполняется поиск.
- `by`: `"XPATH"`,  метод поиска элемента.
- `selector`: `"//input[@id='ap_password']"`,  Xpath селектор элемента.
- `if_list`: `"first"`, брать первый элемент из списка.
- `use_mouse`: `false`,  не использовать мышь для взаимодействия.
- `mandatory`: `true`,  элемент является обязательным для взаимодействия.
- `timeout`: `0`, таймаут поиска элемента.
- `timeout_for_event`: `"presence_of_element_located"`, событие ожидания появления элемента.
- `event`: `"send_keys('52UldxjzWGpdEQxWaNMY')"`, событие, которое нужно выполнить на элементе.
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`, логика для действия.

### `keep_signed_in_checkbox`

**Описание**: Локатор для чекбокса "Запомнить меня".

**Параметры**:
- `attribute`: `null`, атрибут, по которому не выполняется поиск.
- `by`: `"XPATH"`,  метод поиска элемента.
- `selector`: `"//input[@name='rememberMe']"`,  Xpath селектор элемента.
- `if_list`: `"first"`, брать первый элемент из списка.
- `use_mouse`: `false`,  не использовать мышь для взаимодействия.
- `mandatory`: `true`,  элемент является обязательным для взаимодействия.
- `timeout`: `0`, таймаут поиска элемента.
- `timeout_for_event`: `"presence_of_element_located"`, событие ожидания появления элемента.
- `event`: `"click()"`, событие, которое нужно выполнить на элементе.
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`, логика для действия.

### `success_login_button`

**Описание**: Локатор для кнопки подтверждения входа.

**Параметры**:
- `attribute`: `null`, атрибут, по которому не выполняется поиск.
- `by`: `"XPATH"`,  метод поиска элемента.
- `selector`: `"//input[@id='signInSubmit']"`,  Xpath селектор элемента.
- `if_list`: `"first"`, брать первый элемент из списка.
- `use_mouse`: `false`,  не использовать мышь для взаимодействия.
- `mandatory`: `true`,  элемент является обязательным для взаимодействия.
- `timeout`: `0`, таймаут поиска элемента.
- `timeout_for_event`: `"presence_of_element_located"`, событие ожидания появления элемента.
- `event`: `"click()"`, событие, которое нужно выполнить на элементе.
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`, логика для действия.