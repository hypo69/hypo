# Модуль facebook

## Обзор

Модуль `facebook` предназначен для работы с API Facebook для рекламных кампаний. Он включает в себя функциональность для получения данных, таких как кампании, наборы объявлений и объявления, а также для управления ими.

## Содержание

- [Классы](#классы)
    - [`FacebookAds`](#facebookads)
- [Функции](#функции)
    - [`get_ads_insights`](#get_ads_insights)

## Классы

### `FacebookAds`

**Описание**:
Класс `FacebookAds` предоставляет интерфейс для взаимодействия с API Facebook Ads. Он позволяет инициализировать соединение с API, а также имеет методы для получения различных сущностей, связанных с рекламой.

**Методы**:

- `__init__`: Инициализирует объект `FacebookAds` с заданными параметрами доступа.
- `get_all_campaigns`: Возвращает все рекламные кампании.
- `get_all_adsets`: Возвращает все наборы объявлений.
- `get_all_ads`: Возвращает все объявления.
- `get_campaign`: Возвращает конкретную рекламную кампанию по ID.
- `get_adset`: Возвращает конкретный набор объявлений по ID.
- `get_ad`: Возвращает конкретное объявление по ID.

#### `__init__`

**Описание**:
Инициализирует объект `FacebookAds` с необходимыми параметрами для доступа к API.

**Параметры**:
- `account_id` (str): ID рекламного аккаунта Facebook.
- `access_token` (str): Токен доступа к API Facebook.
- `app_secret` (str): Секретный ключ приложения Facebook.
- `api_version` (str, optional): Версия API Facebook. По умолчанию 'v17.0'.

**Возвращает**:
- `None`

#### `get_all_campaigns`

**Описание**:
Получает все рекламные кампании из Facebook Ads.

**Параметры**:
- `fields` (str | list[str], optional): Поля, которые нужно вернуть. По умолчанию `None`.

**Возвращает**:
- `list[dict] | None`: Список словарей с информацией о кампаниях или `None` в случае ошибки.

#### `get_all_adsets`

**Описание**:
Получает все наборы объявлений из Facebook Ads.

**Параметры**:
- `fields` (str | list[str], optional): Поля, которые нужно вернуть. По умолчанию `None`.

**Возвращает**:
- `list[dict] | None`: Список словарей с информацией о наборах объявлений или `None` в случае ошибки.

#### `get_all_ads`

**Описание**:
Получает все объявления из Facebook Ads.

**Параметры**:
- `fields` (str | list[str], optional): Поля, которые нужно вернуть. По умолчанию `None`.

**Возвращает**:
- `list[dict] | None`: Список словарей с информацией об объявлениях или `None` в случае ошибки.

#### `get_campaign`

**Описание**:
Получает конкретную рекламную кампанию по ID.

**Параметры**:
- `campaign_id` (str): ID рекламной кампании.
- `fields` (str | list[str], optional): Поля, которые нужно вернуть. По умолчанию `None`.

**Возвращает**:
- `dict | None`: Словарь с информацией о кампании или `None` в случае ошибки.

#### `get_adset`

**Описание**:
Получает конкретный набор объявлений по ID.

**Параметры**:
- `adset_id` (str): ID набора объявлений.
- `fields` (str | list[str], optional): Поля, которые нужно вернуть. По умолчанию `None`.

**Возвращает**:
- `dict | None`: Словарь с информацией о наборе объявлений или `None` в случае ошибки.

#### `get_ad`

**Описание**:
Получает конкретное объявление по ID.

**Параметры**:
- `ad_id` (str): ID объявления.
- `fields` (str | list[str], optional): Поля, которые нужно вернуть. По умолчанию `None`.

**Возвращает**:
- `dict | None`: Словарь с информацией об объявлении или `None` в случае ошибки.

## Функции

### `get_ads_insights`

**Описание**:
Получает статистику по рекламным кампаниям, наборам объявлений и объявлениям.

**Параметры**:
- `facebook` (FacebookAds): Объект `FacebookAds` для взаимодействия с API.
- `level` (str): Уровень статистики (campaign, adset или ad).
- `ids` (list[str] | str): Список ID или ID сущности, для которой нужно получить статистику.
- `fields` (list[str], optional): Список полей для статистики. По умолчанию значения полей по умолчанию.
- `date_preset` (str, optional): Предустановленный диапазон дат. По умолчанию 'last_3d'.

**Возвращает**:
- `list[dict] | dict | None`: Список словарей с данными по статистике, словарь или `None` в случае ошибки.

**Вызывает исключения**:
- `ValueError`: Возникает если параметр `level` не является "campaign", "adset" или "ad".