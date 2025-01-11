# Документация для `ksp_categories_watches_amazfit.json`

## Обзор

Файл `ksp_categories_watches_amazfit.json` содержит конфигурацию сценариев для парсинга категорий часов AMAZFIT с веб-сайта KSP. Он определяет бренд, URL-адрес, активность и сопоставления категорий PrestaShop.

## Содержание

- [Обзор](#обзор)
- [Структура файла](#структура-файла)
    - [Сценарии](#сценарии)
        - [AMAZFIT](#amazfit)
            - [brand](#brand)
            - [url](#url)
            - [checkbox](#checkbox)
            - [active](#active)
            - [condition](#condition)
            - [presta_categories](#presta_categories)

## Структура файла

### Сценарии

Содержит объект, который хранит конфигурации для конкретных брендов.

#### AMAZFIT

Конфигурация для бренда AMAZFIT.

##### brand

**Описание**: Название бренда.
-   Тип: `str`
-   Значение: `"AMAZFIT"`

##### url

**Описание**: URL-адрес, с которого будет происходить парсинг.
-   Тип: `str`
-   Значение: `"https://ksp.co.il/web/cat/2085..14295"`

##### checkbox

**Описание**: Флаг для указания наличия чекбокса (не используется в данном контексте).
-   Тип: `bool`
-   Значение: `false`

##### active

**Описание**: Флаг, определяющий, активен ли сценарий парсинга.
-   Тип: `bool`
-   Значение: `true`

##### condition

**Описание**: Условие товаров в сценарии (новый).
-   Тип: `str`
-   Значение: `"new"`

##### presta_categories

**Описание**: Словарь сопоставлений категорий PrestaShop. Ключ - ID категории, значение - название.

-   Тип: `dict`
-   Примеры:
    -   `"3405": "GOOGLE PIXEL PRO"`
    -    `"3198": "CONSUMER ELECTRONICS"`
    -  `"3202": "computer,smartphone,gaming console,smart device"`
    -   `"6471": "Smartphones"`
    -   `"3403": "GOOGLE"`