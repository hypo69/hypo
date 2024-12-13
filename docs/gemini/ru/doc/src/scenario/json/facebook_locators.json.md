# Документация `facebook_locators.json`

## Обзор

Файл `facebook_locators.json` содержит JSON-объект, описывающий локаторы элементов для автоматизации действий на сайте Facebook. Разделён на несколько ключевых подразделов: `login` для данных авторизации, `locators` для основных элементов взаимодействия и `govno-vsjqko-razno` для тестовых данных.

## Оглавление

1. [Обзор](#обзор)
2. [Раздел `login`](#раздел-login)
3. [Раздел `locators`](#раздел-locators)
4. [Раздел `govno-vsjqko-razno`](#раздел-govno-vsjqko-razno)

## Раздел `login`

### Описание

Содержит данные для авторизации в Facebook, такие как логин, пароль и селекторы для полей ввода.

### Структура

- `email` (str): Адрес электронной почты для входа.
- `password` (str): Пароль для входа.
- `email_selector` (dict):
  - `by` (str): Тип селектора (например, "ID").
  - `selector` (str): Значение селектора для поля ввода электронной почты.
- `password_locator` (dict):
  - `by` (str): Тип селектора для поля ввода пароля.
  - `selector` (str): Значение селектора для поля ввода пароля.
- `loginbutton_locator` (dict):
  - `by` (str): Тип селектора для кнопки входа.
  - `selector` (str): Значение селектора для кнопки входа.

### Пример

```json
{
  "login": {
    "email": "one.last.bit@gmail.com",
    "password": "@o533368048",
    "email_selector": {
      "by": "ID",
      "selector": "email"
    },
    "password_locator": {
      "by": "ID",
      "selector": "..."
    },
    "loginbutton_locator": {
      "by": "ID",
      "selector": "u_0_b"
    }
  }
}
```

## Раздел `locators`

### Описание

Содержит локаторы для различных элементов пользовательского интерфейса на Facebook, таких как кнопки отправки сообщений, кнопки загрузки изображений и поля ввода.

### Структура

Каждый элемент в данном разделе имеет следующую структуру:

- `имя_локатора` (dict):
    - `by` (str): Тип селектора (например, "CSS_SELECTOR", "css selector").
    - `selector` (str): Значение селектора для соответствующего элемента.

#### Подробности по локаторам:

- `btn_send_message` (dict): Селектор кнопки отправки сообщения.
- `btn_start_write_message` (dict): Селектор кнопки начала написания сообщения.
- `btn_upload_image` (dict): Селектор кнопки загрузки изображения.
- `div_before_btn_upload_image_text` (dict): Селектор для div'а перед кнопкой загрузки изображения по тексту.
- `div_before_btn_upload_image_class` (dict): Селектор для div'а перед кнопкой загрузки изображения по классу.
- `input_image_element_id` (list): Список возможных ID для input-элемента загрузки изображения.
- `input_text_message___` (dict): Селектор для поля ввода текста сообщения (альтернативный вариант).
- `input_text_message` (dict): Селектор для поля ввода текста сообщения.
- `textarea_navigationFocus` (dict): Селектор для поля textarea для навигационного фокуса.

### Пример

```json
{
  "locators": {
    "btn_send_message": {
      "by": "CSS_SELECTOR",
      "selector": "._1mf7._4jy0._4jy3._4jy1._51sy"
    },
    "btn_start_write_message": {
      "by": "css selector",
      "selector": "span._5qtp"
    },
    "btn_upload_image": {
      "by": "CSS_SELECTOR",
      "selector": "._n._5f0v"
    },
    "div_before_btn_upload_image_text": {
      "by": "CSS_SELECTOR",
      "selector": "text^='Файл/Фото'"
    },
    "div_before_btn_upload_image_class": {
      "by": "CSS_SELECTOR",
      "selector": "._5qtp"
    },
     "input_image_element_id": [
      "js_r",
      "js_31"
    ],
    "input_text_message___": {
      "by": "css selector",
      "selector": "._1mf._1mk"
    },
    "input_text_message": {
      "by": "css selector",
      "selector": "._2cuy._3dgx"
    },
      "textarea_navigationFocus": {
      "by": "css selector",
      "selector": "js_1z"
    }
  }
}
```

## Раздел `govno-vsjqko-razno`

### Описание
Содержит тестовые данные и альтернативные локаторы, которые могут использоваться для отладки или тестирования.

### Структура

- `input_text_message` (list): Список возможных селекторов для поля ввода текста сообщения.

### Пример

```json
{
    "govno-vsjqko-razno": {
        "input_text_message": [ "._1mf._1mk", "._1p1v", "textarea[placeholder*=\"Сообщение\"]" ]
    }
}
```