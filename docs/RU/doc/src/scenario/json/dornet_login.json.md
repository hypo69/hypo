# Документация для `dornet_login.json`

## Обзор

Файл `dornet_login.json` содержит JSON-структуру с данными, необходимыми для выполнения входа в систему.
Он включает в себя учетные данные пользователя (email и пароль), а также локаторы элементов веб-страницы для автоматизации процесса входа.

## Оглавление

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
  - [`email`](#email)
  - [`password`](#password)
  - [`open_login_dialog_locator`](#open_login_dialog_locator)
  - [`email_locator`](#email_locator)
  - [`password_locator`](#password_locator)
  - [`loginbutton_locator`](#loginbutton_locator)

## Структура JSON

### `email`
**Описание**:
Email пользователя для входа в систему.
- **Тип**: `строка`
- **Пример**: `"513404160"`

### `password`
**Описание**:
Пароль пользователя для входа в систему.
- **Тип**: `строка`
- **Пример**: `"513404160"`

### `open_login_dialog_locator`
**Описание**:
Локатор элемента веб-страницы для открытия диалога входа.
- **Тип**: `объект`
- **Поля**:
    - `by` (str): Метод поиска элемента (`css selector`).
    - `selector` (str): CSS селектор для определения элемента (`.fancyboxdiller`).
- **Пример**:
    ```json
    {
        "by": "css selector",
        "selector": ".fancyboxdiller"
    }
    ```

### `email_locator`
**Описание**:
Локатор поля ввода email.
- **Тип**: `объект`
- **Поля**:
    - `by` (str): Метод поиска элемента (`css selector`).
    - `selector` (str): CSS селектор для определения элемента (`input[id='UserName_61']`).
- **Пример**:
    ```json
    {
        "by": "css selector",
        "selector": "input[id='UserName_61']"
    }
    ```

### `password_locator`
**Описание**:
Локатор поля ввода пароля.
- **Тип**: `объект`
- **Поля**:
    - `by` (str): Метод поиска элемента (`css selector`).
    - `selector` (str): CSS селектор для определения элемента (`input[id='IDNum_61']`).
- **Пример**:
    ```json
     {
        "by": "css selector",
        "selector": "input[id='IDNum_61']"
    }
    ```

### `loginbutton_locator`
**Описание**:
Локатор кнопки входа.
- **Тип**: `объект`
- **Поля**:
    - `by` (str): Метод поиска элемента (`css selector`).
    - `selector` (str): CSS селектор для определения элемента (`div.actions button[title='Войти']`).
- **Пример**:
    ```json
   {
        "by": "css selector",
        "selector": "div.actions button[title='���']"
    }
    ```