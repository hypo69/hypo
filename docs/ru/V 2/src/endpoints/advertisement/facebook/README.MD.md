# Модуль facebook

## Обзор

Модуль `facebook` предназначен для работы с рекламными кампаниями в Facebook.

## Содержание

- [Классы](#Классы)
    - [FacebookAdvertisement](#FacebookAdvertisement)
- [Функции](#Функции)
    - [get_facebook_advertisement](#get_facebook_advertisement)
    - [create_facebook_advertisement](#create_facebook_advertisement)
    - [update_facebook_advertisement](#update_facebook_advertisement)
    - [delete_facebook_advertisement](#delete_facebook_advertisement)

## Классы

### `FacebookAdvertisement`

**Описание**: Класс для представления рекламного объявления Facebook.

**Методы**:
- `__init__`: Инициализирует объект рекламного объявления.
- `to_dict`: Преобразует объект в словарь.
- `from_dict`: Создает объект из словаря.

#### `__init__`

**Описание**: Инициализирует объект `FacebookAdvertisement`.

**Параметры**:
- `advertisement_id` (str): Идентификатор рекламного объявления.
- `name` (str): Название рекламного объявления.
- `status` (str): Статус рекламного объявления.
- `campaign_id` (str): Идентификатор кампании.
- `creative_id` (str): Идентификатор креатива.
- `targeting` (dict): Параметры таргетинга.
- `budget` (float): Бюджет рекламной кампании.

#### `to_dict`

**Описание**: Преобразует объект `FacebookAdvertisement` в словарь.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `dict`: Словарь, представляющий объект `FacebookAdvertisement`.

#### `from_dict`

**Описание**: Создает объект `FacebookAdvertisement` из словаря.

**Параметры**:
- `data` (dict): Словарь с данными для создания объекта.

**Возвращает**:
- `FacebookAdvertisement`: Объект `FacebookAdvertisement`, созданный из словаря.

## Функции

### `get_facebook_advertisement`

**Описание**: Получает рекламное объявление Facebook по его идентификатору.

**Параметры**:
- `advertisement_id` (str): Идентификатор рекламного объявления.

**Возвращает**:
- `dict | None`: Словарь с данными рекламного объявления или `None`, если объявление не найдено.

**Вызывает исключения**:
- `FacebookRequestError`: Если возникает ошибка при запросе к Facebook API.

### `create_facebook_advertisement`

**Описание**: Создает новое рекламное объявление Facebook.

**Параметры**:
- `data` (dict): Словарь с данными для создания рекламного объявления.

**Возвращает**:
- `dict`: Словарь с данными созданного рекламного объявления.

**Вызывает исключения**:
- `FacebookRequestError`: Если возникает ошибка при запросе к Facebook API.

### `update_facebook_advertisement`

**Описание**: Обновляет существующее рекламное объявление Facebook.

**Параметры**:
- `advertisement_id` (str): Идентификатор рекламного объявления для обновления.
- `data` (dict): Словарь с данными для обновления рекламного объявления.

**Возвращает**:
- `dict`: Словарь с данными обновленного рекламного объявления.

**Вызывает исключения**:
- `FacebookRequestError`: Если возникает ошибка при запросе к Facebook API.

### `delete_facebook_advertisement`

**Описание**: Удаляет рекламное объявление Facebook по его идентификатору.

**Параметры**:
- `advertisement_id` (str): Идентификатор рекламного объявления для удаления.

**Возвращает**:
- `bool`: `True`, если объявление успешно удалено, `False` в противном случае.

**Вызывает исключения**:
- `FacebookRequestError`: Если возникает ошибка при запросе к Facebook API.