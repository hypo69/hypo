# Документация для `amazon_categories_desktops_lenovo_new.json`

## Обзор

Файл `amazon_categories_desktops_lenovo_new.json` содержит конфигурацию для сбора данных о настольных компьютерах Lenovo с сайта Amazon. Он определяет различные сценарии, каждый из которых соответствует определенной конфигурации процессора (Intel i3, i5, i7, i9 и AMD Ryzen 3). Каждый сценарий содержит URL-адрес для поиска на Amazon, категорию товара для PrestaShop, и другие параметры, необходимые для сбора данных.

## Оглавление

1. [Обзор](#обзор)
2. [Структура](#структура)
3. [Сценарии](#сценарии)
    - [NEW LENOVO DESKTOP INTEL I3](#new-lenovo-desktop-intel-i3)
    - [NEW LENOVO DESKTOP INTEL I5](#new-lenovo-desktop-intel-i5)
    - [NEW LENOVO DESKTOP INTEL I7](#new-lenovo-desktop-intel-i7)
    - [NEW LENOVO DESKTOP INTEL I9](#new-lenovo-desktop-intel-i9)
    - [NEW LENOVO DESKTOP AMD RYZEN 3](#new-lenovo-desktop-amd-ryzen-3)

## Структура

Файл представляет собой JSON-объект с одним ключом `scenarios`, значением которого является словарь. Каждый ключ этого словаря - это название сценария, а значение - это словарь с настройками для этого сценария.

## Сценарии

### NEW LENOVO DESKTOP INTEL I3
 
**Описание**: Сценарий для сбора данных о новых настольных компьютерах Lenovo с процессором Intel i3.

**Параметры**:
- `brand` (str): "LENOVO" - бренд товара.
- `url` (str): URL-адрес для поиска на Amazon.
- `active` (bool): `true` - указывает, что сценарий активен.
- `condition` (str): "new" - состояние товара.
- `presta_categories` (dict): Категории товара для PrestaShop.
    - `template` (dict):  Соответствие для категорий, в данном случае `{"lenovo": "DESKTOPS INTEL I3"}`.
- `checkbox` (bool): `false` -  флаг для checkbox.
- `price_rule` (int): `1` - правило ценообразования.
   
### NEW LENOVO DESKTOP INTEL I5
 
**Описание**: Сценарий для сбора данных о новых настольных компьютерах Lenovo с процессором Intel i5.

**Параметры**:
- `brand` (str): "LENOVO" - бренд товара.
- `url` (str): URL-адрес для поиска на Amazon.
- `active` (bool): `true` - указывает, что сценарий активен.
- `condition` (str): "new" - состояние товара.
- `presta_categories` (dict): Категории товара для PrestaShop.
    - `template` (dict):  Соответствие для категорий, в данном случае `{"lenovo": "DESKTOPS INTEL I5"}`.
- `checkbox` (bool): `false` -  флаг для checkbox.
- `price_rule` (int): `1` - правило ценообразования.

### NEW LENOVO DESKTOP INTEL I7
 
**Описание**: Сценарий для сбора данных о новых настольных компьютерах Lenovo с процессором Intel i7.

**Параметры**:
- `brand` (str): "LENOVO" - бренд товара.
- `url` (str): URL-адрес для поиска на Amazon.
- `active` (bool): `true` - указывает, что сценарий активен.
- `condition` (str): "new" - состояние товара.
- `presta_categories` (dict): Категории товара для PrestaShop.
    - `template` (dict):  Соответствие для категорий, в данном случае `{"lenovo": "DESKTOPS INTEL I7"}`.
- `checkbox` (bool): `false` -  флаг для checkbox.
- `price_rule` (int): `1` - правило ценообразования.
    
### NEW LENOVO DESKTOP INTEL I9
 
**Описание**: Сценарий для сбора данных о новых настольных компьютерах Lenovo с процессором Intel i9.

**Параметры**:
- `brand` (str): "LENOVO" - бренд товара.
- `url` (str): URL-адрес для поиска на Amazon.
- `active` (bool): `true` - указывает, что сценарий активен.
- `condition` (str): "new" - состояние товара.
- `presta_categories` (dict): Категории товара для PrestaShop.
    - `template` (dict):  Соответствие для категорий, в данном случае `{"lenovo": "DESKTOPS INTEL I9"}`.
- `checkbox` (bool): `false` -  флаг для checkbox.
- `price_rule` (int): `1` - правило ценообразования.

### NEW LENOVO DESKTOP AMD RYZEN 3

**Описание**: Сценарий для сбора данных о новых настольных компьютерах Lenovo с процессором AMD Ryzen 3.

**Параметры**:
- `brand` (str): "LENOVO" - бренд товара.
- `url` (str): URL-адрес для поиска на Amazon.
- `active` (bool): `true` - указывает, что сценарий активен.
- `condition` (str): "new" - состояние товара.
- `presta_categories` (dict): Категории товара для PrestaShop.
    - `template` (dict):  Соответствие для категорий, в данном случае `{"lenovo": "DESKTOPS AMD RYZEN 3"}`.
- `checkbox` (bool): `false` -  флаг для checkbox.
- `price_rule` (int): `1` - правило ценообразования.