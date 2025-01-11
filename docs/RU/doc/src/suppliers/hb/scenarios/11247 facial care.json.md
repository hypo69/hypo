# Документация для `11247 facial care.json`

## Обзор

Файл `11247 facial care.json` содержит JSON-конфигурацию сценариев для парсинга товаров категории "Уход за лицом" с сайта hbdeadsea.co.il. Каждый сценарий описывает URL для парсинга, условие (например, "new"), категории PrestaShop и правило ценообразования.

## Оглавление

- [Обзор](#обзор)
- [Структура файла](#структура-файла)
  - [Сценарии](#сценарии)
    - [`moisture-face`](#moisture-face)
    - [`serums`](#serums)
    - [`face-masks`](#face-masks)
    - [`facial-cleaning-products`](#facial-cleaning-products)
    - [`multi-active-series`](#multi-active-series)
    - [`mineral-peptide`](#mineral-peptide)

## Структура файла

### Сценарии

Секция `scenarios` содержит набор сценариев, каждый из которых представляет собой объект с ключами, описывающими категорию товаров для парсинга.

#### `moisture-face`
**Описание**: Сценарий для парсинга товаров из категории "Увлажнение лица".

**Поля**:
- `url` (str): URL страницы категории.
- `condition` (str): Условие (например, "new").
- `presta_categories` (dict): Категории PrestaShop.
  - `default_category` (int): ID основной категории.
  - `additional_categories` (list): Список ID дополнительных категорий.
- `price_rule` (int): Правило ценообразования.

#### `serums`
**Описание**: Сценарий для парсинга товаров из категории "Сыворотки".

**Поля**:
- `url` (str): URL страницы категории.
- `condition` (str): Условие (например, "new").
- `presta_categories` (dict): Категории PrestaShop.
  - `default_category` (int): ID основной категории.
  - `additional_categories` (list): Список ID дополнительных категорий.
- `price_rule` (int): Правило ценообразования.

#### `face-masks`
**Описание**: Сценарий для парсинга товаров из категории "Маски для лица".

**Поля**:
- `url` (str): URL страницы категории.
- `condition` (str): Условие (например, "new").
- `presta_categories` (dict): Категории PrestaShop.
  - `default_category` (int): ID основной категории.
  - `additional_categories` (list): Список ID дополнительных категорий.
- `price_rule` (int): Правило ценообразования.

#### `facial-cleaning-products`
**Описание**: Сценарий для парсинга товаров из категории "Средства для очищения лица".

**Поля**:
- `url` (str): URL страницы категории.
- `condition` (str): Условие (например, "new").
- `presta_categories` (dict): Категории PrestaShop.
  - `default_category` (int): ID основной категории.
  - `additional_categories` (list): Список ID дополнительных категорий.
- `price_rule` (int): Правило ценообразования.

#### `multi-active-series`
**Описание**: Сценарий для парсинга товаров из категории "Мультиактивная серия".

**Поля**:
- `url` (str): URL страницы категории.
- `condition` (str): Условие (например, "new").
- `presta_categories` (dict): Категории PrestaShop.
  - `default_category` (int): ID основной категории.
  - `additional_categories` (list): Список ID дополнительных категорий.
- `price_rule` (int): Правило ценообразования.

#### `mineral-peptide`
**Описание**: Сценарий для парсинга товаров из категории "Минеральный пептид".

**Поля**:
- `url` (str): URL страницы категории.
- `condition` (str): Условие (например, "new").
- `presta_categories` (dict): Категории PrestaShop.
  - `default_category` (int): ID основной категории.
  - `additional_categories` (list): Список ID дополнительных категорий.
- `price_rule` (int): Правило ценообразования.