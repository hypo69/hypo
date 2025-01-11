# Локаторы для страницы входа Grandadvance

## Обзор

Этот файл JSON содержит определения локаторов для элементов страницы входа Grandadvance. Локаторы используются для автоматизированного тестирования и взаимодействия с веб-интерфейсом. Каждый элемент определен с помощью `XPATH`, атрибутов и необходимых действий.

## Содержание

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

**Описание**: Локатор для кнопки открытия формы входа.

**Свойства**:
- **attribute**: null
- **by**: XPATH
- **selector**: `//span[@id='nav-link-accountList-nav-line-1']`
- **if_list**: first
- **use_mouse**: false
- **mandatory**: true
- **timeout**: 0
- **timeout_for_event**: presence_of_element_located
- **event**: `click()`
- **logic for action**: null

### `email_input`

**Описание**: Локатор для поля ввода электронной почты.

**Свойства**:
- **attribute**: null
- **by**: XPATH
- **selector**: `//input[@id='ap_email']`
- **if_list**: first
- **use_mouse**: false
- **mandatory**: true
- **timeout**: 0
- **timeout_for_event**: presence_of_element_located
- **event**: `send_keys('972547519449')`
- **logic for action**: null

### `continue_button`

**Описание**: Локатор для кнопки "Продолжить" после ввода электронной почты.

**Свойства**:
- **attribute**: null
- **by**: XPATH
- **selector**: `//input[@id='continue']`
- **if_list**: first
- **use_mouse**: false
- **mandatory**: true
- **timeout**: 0
- **timeout_for_event**: presence_of_element_located
- **event**: `click()`
- **logic for action**: null

### `password_input`

**Описание**: Локатор для поля ввода пароля.

**Свойства**:
- **attribute**: null
- **by**: XPATH
- **selector**: `//input[@id='ap_password']`
- **if_list**: first
- **use_mouse**: false
- **mandatory**: true
- **timeout**: 0
- **timeout_for_event**: presence_of_element_located
- **event**: `send_keys('52UldxjzWGpdEQxWaNMY')`
- **logic for action**: null

### `keep_signed_in_checkbox`

**Описание**: Локатор для чекбокса "Оставаться в системе".

**Свойства**:
- **attribute**: null
- **by**: XPATH
- **selector**: `//input[@name='rememberMe']`
- **if_list**: first
- **use_mouse**: false
- **mandatory**: true
- **timeout**: 0
- **timeout_for_event**: presence_of_element_located
- **event**: `click()`
- **logic for action**: null

### `success_login_button`

**Описание**: Локатор для кнопки "Войти".

**Свойства**:
- **attribute**: null
- **by**: XPATH
- **selector**: `//input[@id='signInSubmit']`
- **if_list**: first
- **use_mouse**: false
- **mandatory**: true
- **timeout**: 0
- **timeout_for_event**: presence_of_element_located
- **event**: `click()`
- **logic for action**: null