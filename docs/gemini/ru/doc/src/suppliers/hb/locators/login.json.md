# Локаторы для страницы входа HB

## Обзор

Этот файл содержит локаторы для элементов страницы входа в систему HB. Локаторы используются для автоматизированного взаимодействия с веб-страницей.

## Содержание

- [Локаторы](#locators)
    - [Поле ввода имени пользователя](#username_input)
    - [Поле ввода пароля](#password_input)
    - [Кнопка входа](#login_button)
    - [Заголовок страницы входа](#login_page_header)
    - [Ошибочное сообщение о логине](#login_error_message)

## Локаторы

### `username_input`

**Описание**: Локатор для поля ввода имени пользователя.

```json
"username_input": {
    "by": "xpath",
    "value": "//input[@id='username']"
}
```

### `password_input`

**Описание**: Локатор для поля ввода пароля.

```json
"password_input": {
    "by": "xpath",
    "value": "//input[@id='password']"
}
```

### `login_button`

**Описание**: Локатор для кнопки входа.

```json
"login_button": {
    "by": "xpath",
    "value": "//button[@type='submit']"
}
```
### `login_page_header`

**Описание**: Локатор для заголовка страницы входа.

```json
"login_page_header": {
    "by": "xpath",
     "value": "//h1[contains(text(),'Login')]"
    }
```

### `login_error_message`

**Описание**: Локатор для сообщения об ошибке при входе.

```json
"login_error_message": {
    "by": "xpath",
    "value": "//p[@class='alert alert-danger']"
}
```