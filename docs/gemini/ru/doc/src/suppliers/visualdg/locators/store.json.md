# `store.json`

## Обзор

Файл `store.json` содержит определения локаторов для взаимодействия с веб-элементами, связанными с поставщиком VisualDG. Локаторы сгруппированы по разделам и используются для автоматизации тестирования и взаимодействия с пользовательским интерфейсом.

## Содержание

- [Поля](#Поля)
- [Кнопки](#Кнопки)
- [Ввод](#Ввод)
- [Переключатели](#Переключатели)
- [Таблицы](#Таблицы)
- [Модальные окна](#Модальные-окна)
- [Уведомления](#Уведомления)
- [Списки](#Списки)

## Поля

### `fields`

Набор локаторов для текстовых полей.

#### `first_name`

**Описание**: Локатор для поля ввода имени.
- `css`: "input[name='firstName']"

#### `last_name`

**Описание**: Локатор для поля ввода фамилии.
- `css`: "input[name='lastName']"

#### `email`

**Описание**: Локатор для поля ввода электронной почты.
- `css`: "input[name='email']"

#### `password`

**Описание**: Локатор для поля ввода пароля.
- `css`: "input[name='password']"

#### `confirm_password`

**Описание**: Локатор для поля подтверждения пароля.
- `css`: "input[name='confirmPassword']"

#### `company_name`

**Описание**: Локатор для поля ввода названия компании.
- `css`: "input[name='companyName']"

#### `position`

**Описание**: Локатор для поля ввода должности.
- `css`: "input[name='position']"

#### `phone_number`

**Описание**: Локатор для поля ввода номера телефона.
- `css`: "input[name='phoneNumber']"

#### `website`

**Описание**: Локатор для поля ввода веб-сайта.
- `css`: "input[name='website']"

#### `street_address`

**Описание**: Локатор для поля ввода улицы.
- `css`: "input[name='streetAddress']"

#### `city`

**Описание**: Локатор для поля ввода города.
- `css`: "input[name='city']"

#### `state_province_region`

**Описание**: Локатор для поля ввода штата/провинции/региона.
- `css`: "input[name='stateProvinceRegion']"

#### `zip_postal_code`

**Описание**: Локатор для поля ввода почтового индекса.
- `css`: "input[name='zipPostalCode']"

#### `country`

**Описание**: Локатор для поля выбора страны.
- `css`: "div[name='country']"

#### `search_field`

**Описание**: Локатор для поля поиска.
- `css`: "input[type='search']"
- `xpath`: "//input[@type='search']"

#### `name`

**Описание**: Локатор для поля ввода имени (обычно для сущности).
- `css`: "input[name='name']"

#### `description`

**Описание**: Локатор для поля ввода описания.
- `css`: "textarea[name='description']"

#### `price`

**Описание**: Локатор для поля ввода цены.
- `css`: "input[name='price']"

## Кнопки

### `buttons`

Набор локаторов для кнопок.

#### `create_account`

**Описание**: Локатор для кнопки "Создать аккаунт".
- `css`: "button[type='submit']"
- `xpath`: "//button[@type='submit' and contains(text(), 'Создать аккаунт')]"

#### `back`

**Описание**: Локатор для кнопки "Назад".
- `css`: "button[type='button']"
- `xpath`: "//button[@type='button' and contains(text(), 'Назад')]"

#### `cancel`

**Описание**: Локатор для кнопки "Отмена".
- `css`: "button[type='button']"
- `xpath`: "//button[@type='button' and contains(text(), 'Отмена')]"

#### `save`

**Описание**: Локатор для кнопки "Сохранить".
- `css`: "button[type='button']"
- `xpath`: "//button[contains(text(), 'Сохранить')]"

#### `close`

**Описание**: Локатор для кнопки "Закрыть".
- `css`: "button[aria-label='close']"
- `xpath`: "//button[@aria-label='close']"

#### `add_new`

**Описание**: Локатор для кнопки "Добавить новое".
- `css`: "button[type='button']"
- `xpath`: "//button[@type='button' and contains(text(), 'Добавить новое')]"

#### `continue`

**Описание**: Локатор для кнопки "Продолжить".
- `css`: "button[type='button']"
- `xpath`: "//button[@type='button' and contains(text(), 'Продолжить')]"

#### `sign_in`

**Описание**: Локатор для кнопки "Войти".
- `css`: "button[type='button']"
- `xpath`: "//button[@type='button' and contains(text(), 'Войти')]"
    
#### `upload_button`

**Описание**: Локатор для кнопки "Загрузить".
- `css`: "button[type='button']"
- `xpath`: "//button[@type='button' and contains(text(), 'Загрузить')]"

#### `more_button`

**Описание**: Локатор для кнопки "Еще".
- `css`: "button[type='button']"
- `xpath`: "//button[@type='button' and contains(text(), 'Еще')]"

#### `apply_filters`

**Описание**: Локатор для кнопки "Применить фильтры".
- `css`: "button[type='button']"
- `xpath`: "//button[@type='button' and contains(text(), 'Применить фильтры')]"

#### `reset_filters`

**Описание**: Локатор для кнопки "Сбросить фильтры".
- `css`: "button[type='button']"
- `xpath`: "//button[@type='button' and contains(text(), 'Сбросить фильтры')]"

## Ввод

### `inputs`

Набор локаторов для текстовых полей ввода.

#### `search`

**Описание**: Локатор для поля ввода поиска.
- `css`: "input[type='search']"

## Переключатели

### `switches`

Набор локаторов для переключателей (чекбоксов).

#### `agree_to_terms`

**Описание**: Локатор для переключателя согласия с условиями.
- `css`: "input[name='agreeToTerms']"

## Таблицы

### `tables`

Набор локаторов для таблиц.

#### `main_table`

**Описание**: Локатор для основной таблицы.
- `css`: "table"

## Модальные окна

### `modals`

Набор локаторов для модальных окон.

#### `modal_window`

**Описание**: Локатор для модального окна.
- `css`: "div[role='dialog']"

## Уведомления

### `notifications`

Набор локаторов для уведомлений.

#### `notification_message`

**Описание**: Локатор для сообщения уведомления.
- `css`: "div[role='alert']"

## Списки

### `lists`

Набор локаторов для списков.

#### `list_item`

**Описание**: Локатор для элемента списка.
- `css`: "li[role='option']"