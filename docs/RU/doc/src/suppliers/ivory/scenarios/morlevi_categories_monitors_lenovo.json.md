# Документация для `morlevi_categories_monitors_lenovo.json`

## Обзор

Данный файл содержит JSON-конфигурацию для сценариев обработки категорий мониторов бренда Lenovo с сайта Morlevi. Каждый сценарий определяет URL для сбора данных, фильтры по размеру экрана и соответствие категориям в PrestaShop.

## Оглавление

1.  [Сценарии](#сценарии)
    -   [LENOVO 21 - 22](#lenovo-21---22)
    -   [LENOVO 23 - 24](#lenovo-23---24)
    -   [LENOVO 26 - 28](#lenovo-26---28)
    -   [LENOVO 27 - 29](#lenovo-27---29)

## Сценарии

### LENOVO 21 - 22

**Описание**: Сценарий для мониторов Lenovo с размером экрана 21-22 дюйма.

**Параметры**:
- `brand` (str): Значение "LENOVO", указывающее на бренд.
- `url` (str): URL для сбора данных с сайта Morlevi.
- `checkbox` (bool): Значение `false`, указывающее на отсутствие чекбокса.
- `active` (bool): Значение `true`, указывающее, что сценарий активен.
- `condition` (str): Значение "new", указывающее состояние товара.
- `presta_categories` (dict): Словарь категорий PrestaShop.
  - `template` (dict): Шаблон для категорий PrestaShop.
    - `lenovo` (str): Категория "PC MONITORS 21 - 22" для Lenovo.

### LENOVO 23 - 24

**Описание**: Сценарий для мониторов Lenovo с размером экрана 23-24 дюйма.

**Параметры**:
- `brand` (str): Значение "LENOVO", указывающее на бренд.
- `url` (str): URL для сбора данных с сайта Morlevi.
- `checkbox` (bool): Значение `false`, указывающее на отсутствие чекбокса.
- `active` (bool): Значение `true`, указывающее, что сценарий активен.
- `condition` (str): Значение "new", указывающее состояние товара.
- `presta_categories` (dict): Словарь категорий PrestaShop.
  - `template` (dict): Шаблон для категорий PrestaShop.
    - `lenovo` (str): Категория "PC MONITORS 23 - 24" для Lenovo.

### LENOVO 26 - 28

**Описание**: Сценарий для мониторов Lenovo с размером экрана 26-28 дюймов.

**Параметры**:
- `brand` (str): Значение "LENOVO", указывающее на бренд.
- `url` (str): URL для сбора данных с сайта Morlevi.
- `checkbox` (bool): Значение `false`, указывающее на отсутствие чекбокса.
- `active` (bool): Значение `true`, указывающее, что сценарий активен.
- `condition` (str): Значение "new", указывающее состояние товара.
- `presta_categories` (dict): Словарь категорий PrestaShop.
  - `template` (dict): Шаблон для категорий PrestaShop.
    - `lenovo` (str): Категория "PC MONITORS 26 - 28" для Lenovo.

### LENOVO 27 - 29

**Описание**: Сценарий для мониторов Lenovo с размером экрана 27-29 дюймов.

**Параметры**:
- `brand` (str): Значение "LENOVO", указывающее на бренд.
- `url` (str): URL для сбора данных с сайта Morlevi.
- `checkbox` (bool): Значение `false`, указывающее на отсутствие чекбокса.
- `active` (bool): Значение `true`, указывающее, что сценарий активен.
- `condition` (str): Значение "new", указывающее состояние товара.
- `presta_categories` (dict): Словарь категорий PrestaShop.
  - `template` (dict): Шаблон для категорий PrestaShop.
    - `lenovo` (str): Категория "PC MONITORS 27 - 29" для Lenovo.