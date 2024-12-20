# Документация для файла `amazon_categories_desktops_lenovo_used.json`

## Обзор

Данный файл содержит JSON-конфигурацию для сценария сбора данных с Amazon, конкретно для настольных компьютеров Lenovo с процессорами Intel i5, бывших в употреблении. Он определяет параметры поиска, условия, категории PrestaShop и правила ценообразования.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
  - [scenarios](#scenarios)
    - [USEDlenovo DESKTOP INTEL I5](#usedlenovo-desktop-intel-i5)
      - [brand](#brand)
      - [url](#url)
      - [active](#active)
      - [condition](#condition)
      - [presta_categories](#presta_categories)
        - [template](#template)
      - [checkbox](#checkbox)
      - [price_rule](#price_rule)

## Структура JSON

### `scenarios`

Словарь, содержащий сценарии сбора данных. Ключи словаря представляют собой уникальные идентификаторы сценариев.

#### `USEDlenovo DESKTOP INTEL I5`

Сценарий для сбора данных о бывших в употреблении настольных компьютерах Lenovo с процессорами Intel i5.

##### `brand`

- **Описание**: Бренд товара (в данном случае "LENOVO").
- **Тип**: `str`

##### `url`

- **Описание**: URL-адрес страницы Amazon для поиска товаров.
- **Тип**: `str`

##### `active`

- **Описание**: Флаг, указывающий, активен ли сценарий (в данном случае `true`).
- **Тип**: `bool`

##### `condition`

- **Описание**: Состояние товара (в данном случае "used").
- **Тип**: `str`

##### `presta_categories`

- **Описание**:  Словарь, содержащий сопоставления категорий PrestaShop для товаров.

###### `template`
    
- **Описание**: Шаблон соответствия категорий. В данном случае "lenovo" будет отнесено к категории "DESKTOPS INTEL I5".
- **Тип**: `dict`

##### `checkbox`
    
- **Описание**: Флаг, указывающий на наличие чекбокса (в данном случае `false`).
- **Тип**: `bool`

##### `price_rule`

- **Описание**: Правило ценообразования (в данном случае `1`).
- **Тип**: `int`