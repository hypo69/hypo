# Документация для `ksp_categories_consoles_microsoft.json`

## Обзор

Данный файл содержит JSON-конфигурацию для сценариев сбора данных о консолях Microsoft (Xbox Series X и Xbox Series S) с сайта KSP. Каждый сценарий включает информацию о бренде, URL, чекбоксе, активности, состоянии товара, категориях PrestaShop и правиле цены.

## Оглавление

1. [Сценарии](#сценарии)
   - [Xbox Series X](#xbox-series-x)
   - [Xbox Series S](#xbox-series-s)

## Сценарии

### Xbox Series X

**Описание**:
Сценарий для сбора данных о консоли Xbox Series X.

**Параметры**:
- `brand` (str): Бренд консоли - `"MICROSOFT"`.
- `url` (str): URL страницы с консолью Xbox Series X на сайте KSP - `"https://ksp.co.il/web/cat/219..255..15733..9335"`.
- `checkbox` (bool): Флаг, указывающий на необходимость использования чекбокса, значение - `false`.
- `active` (bool): Флаг, указывающий на активность сценария, значение - `true`.
- `condition` (str): Состояние товара, значение - `"new"`.
- `presta_categories` (dict): Категории PrestaShop, в которых размещается товар.
  - `template` (dict): Шаблон категорий, где ключ `"microsoft"` соответствует значению `"Xbox Series X"`.
- `price_rule` (int): Правило цены, значение - `1`.

### Xbox Series S

**Описание**:
Сценарий для сбора данных о консоли Xbox Series S.

**Параметры**:
- `brand` (str): Бренд консоли - `"MICROSOFT"`.
- `url` (str): URL страницы с консолью Xbox Series S на сайте KSP - `"https://ksp.co.il/web/cat/219..255..15734..9335"`.
- `checkbox` (bool): Флаг, указывающий на необходимость использования чекбокса, значение - `false`.
- `active` (bool): Флаг, указывающий на активность сценария, значение - `true`.
- `condition` (str): Состояние товара, значение - `"new"`.
- `presta_categories` (dict): Категории PrestaShop, в которых размещается товар.
  - `template` (dict): Шаблон категорий, где ключ `"microsoft"` соответствует значению `"Xbox Series S"`.
- `price_rule` (int): Правило цены, значение - `1`.