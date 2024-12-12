# Модуль `src.endpoints.advertisement.facebook`

## Обзор

Модуль `src.endpoints.advertisement.facebook` предоставляет функциональность для взаимодействия с Facebook API в рамках рекламных кампаний. Он содержит классы и функции для управления рекламными объявлениями и получения связанных данных.

## Содержание

- [Обзор](#обзор)
- [Переменные](#переменные)
- [Импортированные модули](#импортированные-модули)
- [Классы](#классы)
    - [`Facebook`](#facebook)
    -  [`FacebookFields`](#facebookfields)
    -  [`FacebookPromoter`](#facebookpromoter)
- [Функции](#функции)
    - [`get_event_url`](#get_event_url)

## Переменные

### `MODE`
- **Описание**: Указывает текущий режим работы (например, 'dev' для разработки).
- **Тип**: `str`

## Импортированные модули

- `from .facebook import Facebook`: Импортирует класс `Facebook` из модуля `facebook.py`.
- `from .facebook_fields import FacebookFields`: Импортирует класс `FacebookFields` из модуля `facebook_fields.py`.
- `from .promoter import FacebookPromoter, get_event_url`: Импортирует класс `FacebookPromoter` и функцию `get_event_url` из модуля `promoter.py`.

## Классы

### `Facebook`

- **Описание**: Класс для взаимодействия с API Facebook.
- **Методы**:
  - Методы класса `Facebook` описаны в файле `facebook.py`.

### `FacebookFields`

- **Описание**: Класс для хранения полей Facebook.
- **Методы**:
  - Методы класса `FacebookFields` описаны в файле `facebook_fields.py`.

### `FacebookPromoter`

- **Описание**: Класс для управления рекламными кампаниями в Facebook.
- **Методы**:
  - Методы класса `FacebookPromoter` описаны в файле `promoter.py`.

## Функции

### `get_event_url`

- **Описание**: Функция для получения URL события.
- **Параметры**:
  - Параметры функции `get_event_url` описаны в файле `promoter.py`.
- **Возвращает**:
  - Возвращает URL события.
- **Вызывает исключения**:
  - Исключения, вызываемые функцией, описаны в файле `promoter.py`.