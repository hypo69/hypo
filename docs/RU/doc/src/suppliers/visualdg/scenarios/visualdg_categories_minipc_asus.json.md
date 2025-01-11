# Документация для `visualdg_categories_minipc_asus.json`

## Обзор

Данный файл в формате JSON содержит сценарии для мини-ПК марки ASUS, используемые для парсинга и обработки данных. Каждый сценарий включает информацию о бренде, URL-адресе, состоянии активности, условии и категориях PrestaShop.

## Оглавление

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
- [Сценарии](#сценарии)
    - [ASUS MINIPC I3](#asus-minipc-i3)
    - [ASUS MINIPC I5](#asus-minipc-i5)
    - [ASUS MINIPC I7](#asus-minipc-i7)
    - [ASUS MINIPC I9](#asus-minipc-i9)
    - [ASUS MINIPC AMD](#asus-minipc-amd)
    - [ASUS MINIPC Celeron](#asus-minipc-celeron)

## Структура JSON

JSON-файл содержит один корневой объект с ключом `scenarios`, значением которого является объект. Этот объект содержит именованные сценарии, где каждый ключ - это имя сценария, а значение - объект с информацией о конкретном продукте ASUS.

## Сценарии

### `ASUS MINIPC I3`

**Описание**: Сценарий для мини-ПК ASUS с процессором Intel Core i3.

**Поля**:
- `brand` (str): Бренд продукта ("ASUS").
- `url` (str): URL-адрес страницы продукта (`https://www.visualdg.co.il/169415-ASUS-MiniPC/253272`).
- `checkbox` (bool): Флаг для использования чекбокса ( `false`).
- `active` (bool): Флаг для активности сценария (`true`).
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (str): Категории PrestaShop, к которым относится товар (`159,160`).

### `ASUS MINIPC I5`

**Описание**: Сценарий для мини-ПК ASUS с процессором Intel Core i5.

**Поля**:
- `brand` (str): Бренд продукта ("ASUS").
- `url` (str): URL-адрес страницы продукта (`https://www.visualdg.co.il/169415-ASUS-MiniPC/253273`).
- `checkbox` (bool): Флаг для использования чекбокса (`false`).
- `active` (bool): Флаг для активности сценария (`true`).
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (str): Категории PrestaShop, к которым относится товар (`159,161`).

### `ASUS MINIPC I7`

**Описание**: Сценарий для мини-ПК ASUS с процессором Intel Core i7.

**Поля**:
- `brand` (str): Бренд продукта ("ASUS").
- `url` (str): URL-адрес страницы продукта (`https://www.visualdg.co.il/169415-ASUS-MiniPC/253274`).
- `checkbox` (bool): Флаг для использования чекбокса (`false`).
- `active` (bool): Флаг для активности сценария (`true`).
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (str): Категории PrestaShop, к которым относится товар (`159,162`).

### `ASUS MINIPC I9`

**Описание**: Сценарий для мини-ПК ASUS с процессором Intel Core i9.

**Поля**:
- `brand` (str): Бренд продукта ("ASUS").
- `url` (str): Заполнитель URL-адреса (`-------------ASUS  MINIPC I9---------------- `).
- `checkbox` (bool): Флаг для использования чекбокса (`false`).
- `active` (bool): Флаг для активности сценария (`true`).
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (str): Категории PrestaShop, к которым относится товар (`159,530`).

### `ASUS MINIPC AMD`

**Описание**: Сценарий для мини-ПК ASUS с процессором AMD.

**Поля**:
- `brand` (str): Бренд продукта ("ASUS").
- `url` (str): Заполнитель URL-адреса (`-------------ASUS MINIPC AMD---------------- `).
- `checkbox` (bool): Флаг для использования чекбокса (`false`).
- `active` (bool): Флаг для активности сценария (`true`).
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (str): Категории PrestaShop, к которым относится товар (`159,531`).

### `ASUS MINIPC Celeron`

**Описание**: Сценарий для мини-ПК ASUS с процессором Celeron.

**Поля**:
- `brand` (str): Бренд продукта ("ASUS").
- `url` (str): Заполнитель URL-адреса (`-------------ASUS MINIPC Celeron---------------- `).
- `checkbox` (bool): Флаг для использования чекбокса (`false`).
- `active` (bool): Флаг для активности сценария (`true`).
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (str): Категории PrestaShop, к которым относится товар (`159,532`).