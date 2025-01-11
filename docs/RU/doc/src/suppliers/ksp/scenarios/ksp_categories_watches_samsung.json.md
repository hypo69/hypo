# Документация для `ksp_categories_watches_samsung.json`

## Обзор

Файл `ksp_categories_watches_samsung.json` содержит JSON-конфигурацию для сценариев парсинга категорий умных часов Samsung с веб-сайта KSP. Он определяет различные модели часов Samsung (GALAXY Watch, GALAXY Watch Active 2, GALAXY Watch 3, GALAXY Watch 4) и их соответствующие URL-адреса на сайте KSP, а также необходимые параметры для парсинга, такие как бренд, флаги `checkbox` и `active`, и предустановленные категории PrestaShop.

## Оглавление

1. [Обзор](#обзор)
2. [Структура файла](#структура-файла)
3. [Сценарии](#сценарии)
    - [GALAXY Watch](#galaxy-watch)
    - [GALAXY Watch Active 2](#galaxy-watch-active-2)
    - [GALAXY Watch 3](#galaxy-watch-3)
    - [GALAXY Watch 4](#galaxy-watch-4)

## Структура файла

Файл представляет собой JSON-объект, содержащий ключ "scenarios", значением которого является объект, содержащий ключи, представляющие собой названия моделей умных часов Samsung. Каждая модель имеет свои настройки.

## Сценарии

### GALAXY Watch

**Описание**: Настройки для парсинга товаров категории GALAXY Watch.

**Параметры**:
*   `brand` (str): Бренд товара - "SAMSUNG".
*   `url` (str): URL-адрес страницы категории на сайте KSP.
*   `checkbox` (bool): Флаг для установки чекбокса, значение `false`.
*   `active` (bool): Флаг активации сценария, значение `true`.
*   `condition` (str): Условие товара, значение `new`.
*   `presta_categories` (dict): Соответствие категорий KSP категориям PrestaShop:
    *   `3405` (str): "GOOGLE PIXEL PRO".
    *   `3198` (str): "CONSUMER ELECTRONICS".
    *   `3202` (str): "computer,smartphone,gaming console,smart device".
    *   `6471` (str): "Smartphones".
    *   `3403` (str): "GOOGLE".

### GALAXY Watch Active 2

**Описание**: Настройки для парсинга товаров категории GALAXY Watch Active 2.

**Параметры**:
*   `brand` (str): Бренд товара - "SAMSUNG".
*   `url` (str): URL-адрес страницы категории на сайте KSP.
*   `checkbox` (bool): Флаг для установки чекбокса, значение `false`.
*   `active` (bool): Флаг активации сценария, значение `true`.
*   `condition` (str): Условие товара, значение `new`.
*   `presta_categories` (dict): Соответствие категорий KSP категориям PrestaShop:
    *   `3405` (str): "GOOGLE PIXEL PRO".
    *   `3198` (str): "CONSUMER ELECTRONICS".
    *   `3202` (str): "computer,smartphone,gaming console,smart device".
    *   `6471` (str): "Smartphones".
    *   `3403` (str): "GOOGLE".

### GALAXY Watch 3

**Описание**: Настройки для парсинга товаров категории GALAXY Watch 3.

**Параметры**:
*   `brand` (str): Бренд товара - "SAMSUNG".
*   `url` (str): URL-адрес страницы категории на сайте KSP.
*   `checkbox` (bool): Флаг для установки чекбокса, значение `false`.
*   `active` (bool): Флаг активации сценария, значение `true`.
*   `condition` (str): Условие товара, значение `new`.
*   `presta_categories` (dict): Соответствие категорий KSP категориям PrestaShop:
    *   `3405` (str): "GOOGLE PIXEL PRO".
    *   `3198` (str): "CONSUMER ELECTRONICS".
    *   `3202` (str): "computer,smartphone,gaming console,smart device".
    *   `6471` (str): "Smartphones".
    *   `3403` (str): "GOOGLE".

### GALAXY Watch 4

**Описание**: Настройки для парсинга товаров категории GALAXY Watch 4.

**Параметры**:
*   `brand` (str): Бренд товара - "SAMSUNG".
*   `url` (str): URL-адрес страницы категории на сайте KSP.
*   `checkbox` (bool): Флаг для установки чекбокса, значение `false`.
*   `active` (bool): Флаг активации сценария, значение `true`.
*   `condition` (str): Условие товара, значение `new`.
*   `presta_categories` (dict): Соответствие категорий KSP категориям PrestaShop:
    *   `3405` (str): "GOOGLE PIXEL PRO".
    *   `3198` (str): "CONSUMER ELECTRONICS".
    *   `3202` (str): "computer,smartphone,gaming console,smart device".
    *   `6471` (str): "Smartphones".
    *   `3403` (str): "GOOGLE".