# Документация для `morlevi_categories_cases_generic.json`

## Обзор

Этот файл содержит JSON-структуру, описывающую сценарии для категорий компьютерных корпусов бренда GENERIC, используемые при интеграции с PrestaShop. Каждый сценарий определяет соответствие между внутренними названиями категорий и их представлениями в PrestaShop.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
  - [scenarios](#scenarios)
    - [GENERIC MID TOWER](#generic-mid-tower)
    - [GENERIC full tower](#generic-full-tower)
    - [GENERIC mini tower](#generic-mini-tower)
    - [GENERIC gaming MID TOWER](#generic-gaming-mid-tower)
    - [GENERIC gaming full tower](#generic-gaming-full-tower)
    - [GENERIC mini itx](#generic-mini-itx)

## Структура JSON

### `scenarios`

Корневой объект JSON, содержащий все сценарии для категорий.

#### `GENERIC MID TOWER`

**Описание**: Сценарий для компьютерных корпусов типа MID TOWER бренда GENERIC.

**Параметры**:
- `brand` (str): Название бренда - `"GENERIC"`.
- `template` (str): Шаблон, в данном случае пустая строка - `""`.
- `url` (str): URL-адрес, связанный с этой категорией на веб-сайте Morlevi - `"https://www.morlevi.co.il/Cat/97"`.
- `checkbox` (bool): Флаг, указывающий на использование чекбокса - `false`.
- `active` (bool): Флаг, указывающий на активность сценария - `true`.
- `condition` (str): Условие, в данном случае `"new"`.
- `presta_categories` (dict): Словарь, определяющий соответствие категорий PrestaShop.
  - `template` (dict): Словарь, связывающий внутренние категории с категориями PrestaShop.
    - `"computer cases"` (str): Внутренняя категория, сопоставленная с категорией PrestaShop `"MID TOWER"`.

#### `GENERIC full tower`

**Описание**: Сценарий для компьютерных корпусов типа FULL TOWER бренда GENERIC.

**Параметры**:
- `brand` (str): Название бренда - `"GENERIC"`.
- `template` (str): Шаблон, в данном случае пустая строка - `""`.
- `url` (str): URL-адрес, в данном случае заполнитель - `"----------------------------GENERIC FULL TOWER--------------------------------"`.
- `checkbox` (bool): Флаг, указывающий на использование чекбокса - `false`.
- `active` (bool): Флаг, указывающий на активность сценария - `true`.
- `condition` (str): Условие, в данном случае `"new"`.
- `presta_categories` (dict): Словарь, определяющий соответствие категорий PrestaShop.
  - `template` (dict): Словарь, связывающий внутренние категории с категориями PrestaShop.
    - `"computer cases"` (str): Внутренняя категория, сопоставленная с категорией PrestaShop `"FULL TOWER"`.

#### `GENERIC mini tower`

**Описание**: Сценарий для компьютерных корпусов типа MINI TOWER бренда GENERIC.

**Параметры**:
- `brand` (str): Название бренда - `"GENERIC"`.
- `template` (str): Шаблон, в данном случае пустая строка - `""`.
- `url` (str): URL-адрес, связанный с этой категорией на веб-сайте Morlevi - `"https://www.morlevi.co.il/Cat/97"`.
- `checkbox` (bool): Флаг, указывающий на использование чекбокса - `false`.
- `active` (bool): Флаг, указывающий на активность сценария - `true`.
- `condition` (str): Условие, в данном случае `"new"`.
- `presta_categories` (dict): Словарь, определяющий соответствие категорий PrestaShop.
  - `template` (dict): Словарь, связывающий внутренние категории с категориями PrestaShop.
    - `"computer cases"` (str): Внутренняя категория, сопоставленная с категорией PrestaShop `"MINI TOWER"`.

#### `GENERIC gaming MID TOWER`

**Описание**: Сценарий для игровых компьютерных корпусов типа MID TOWER бренда GENERIC.

**Параметры**:
- `brand` (str): Название бренда - `"GENERIC"`.
- `template` (str): Шаблон, в данном случае пустая строка - `""`.
- `url` (str): URL-адрес, в данном случае заполнитель - `"----------------------------GENERIC gaming mid--------------------------------"`.
- `checkbox` (bool): Флаг, указывающий на использование чекбокса - `false`.
- `active` (bool): Флаг, указывающий на активность сценария - `true`.
- `condition` (str): Условие, в данном случае `"new"`.
- `presta_categories` (dict): Словарь, определяющий соответствие категорий PrestaShop.
  - `template` (dict): Словарь, связывающий внутренние категории с категориями PrestaShop.
    - `"computer cases"` (str): Внутренняя категория, сопоставленная с категорией PrestaShop `"MID TOWER"`.

#### `GENERIC gaming full tower`

**Описание**: Сценарий для игровых компьютерных корпусов типа FULL TOWER бренда GENERIC.

**Параметры**:
- `brand` (str): Название бренда - `"GENERIC"`.
- `template` (str): Шаблон, в данном случае пустая строка - `""`.
- `url` (str): URL-адрес, в данном случае заполнитель - `"----------------------------GENERIC gaming full TOWER--------------------------------"`.
- `checkbox` (bool): Флаг, указывающий на использование чекбокса - `false`.
- `active` (bool): Флаг, указывающий на активность сценария - `true`.
- `condition` (str): Условие, в данном случае `"new"`.
- `presta_categories` (dict): Словарь, определяющий соответствие категорий PrestaShop.
  - `template` (dict): Словарь, связывающий внутренние категории с категориями PrestaShop.
    - `"computer cases"` (str): Внутренняя категория, сопоставленная с категорией PrestaShop `"FULL TOWER"`.

#### `GENERIC mini itx`

**Описание**: Сценарий для компьютерных корпусов типа MINI ITX бренда GENERIC.

**Параметры**:
- `brand` (str): Название бренда - `"GENERIC"`.
- `template` (str): Шаблон, в данном случае пустая строка - `""`.
- `url` (str): URL-адрес, в данном случае заполнитель - `"----------------------------GENERIC mini itxR--------------------------------"`.
- `checkbox` (bool): Флаг, указывающий на использование чекбокса - `false`.
- `active` (bool): Флаг, указывающий на активность сценария - `true`.
- `condition` (str): Условие, в данном случае `"new"`.
- `presta_categories` (dict): Словарь, определяющий соответствие категорий PrestaShop.
  - `template` (dict): Словарь, связывающий внутренние категории с категориями PrestaShop.
    - `"computer cases"` (str): Внутренняя категория, сопоставленная с категорией PrestaShop `"MINI ITX"`.