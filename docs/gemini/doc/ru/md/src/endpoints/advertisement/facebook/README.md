# Модуль facebook

## Обзор

Этот модуль содержит функции для работы с рекламными объявлениями на платформе Facebook. Он предоставляет инструменты для создания, редактирования и управления объявлениями.

## Оглавление

* [Функции](#функции)


## Функции

### `create_facebook_ad`

**Описание**: Функция создания нового рекламного объявления на Facebook.

**Параметры**:
- `campaign_id` (int): Идентификатор рекламной кампании.
- `ad_set_id` (int): Идентификатор набора объявлений.
- `creative_data` (dict): Данные о креативе объявления (текст, изображения, ссылки и т.д.).
- `targeting_data` (dict, optional): Данные о целевой аудитории. По умолчанию `None`.
- `budget` (float, optional): Бюджет для объявления. По умолчанию `None`.

**Возвращает**:
- `dict | None`: Возвращает словарь с результатами создания объявления или `None` в случае ошибки.

**Вызывает исключения**:
- `FacebookAPIError`: Возникает при ошибке в API Facebook.
- `InvalidInputError`: Возникает при некорректном вводе данных.


```