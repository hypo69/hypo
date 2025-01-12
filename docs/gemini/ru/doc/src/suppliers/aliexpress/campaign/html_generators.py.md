# src.suppliers.aliexpress.campaign.html_generators

## Обзор

Модуль `html_generators.py` предоставляет классы для генерации HTML-контента для рекламной кампании. Он включает классы для генерации HTML-страниц для отдельных продуктов, категорий продуктов и общей кампании.

## Содержание

- [Классы](#Классы)
  - [`ProductHTMLGenerator`](#ProductHTMLGenerator)
    - [`set_product_html`](#set_product_html)
  - [`CategoryHTMLGenerator`](#CategoryHTMLGenerator)
    - [`set_category_html`](#set_category_html)
  - [`CampaignHTMLGenerator`](#CampaignHTMLGenerator)
    - [`set_campaign_html`](#set_campaign_html)

## Классы

### `ProductHTMLGenerator`

**Описание**: Класс для генерации HTML-кода для отдельных продуктов.

#### `set_product_html`

**Описание**: Создает HTML-файл для отдельного продукта.

**Параметры**:
- `product` (`SimpleNamespace`): Детали продукта, которые будут включены в HTML.
- `category_path` (`str | Path`): Путь для сохранения HTML-файла.

**Возвращает**:
- `None`: Функция ничего не возвращает.

### `CategoryHTMLGenerator`

**Описание**: Класс для генерации HTML-кода для категорий продуктов.

#### `set_category_html`

**Описание**: Создает HTML-файл для категории.

**Параметры**:
- `products_list` (`list[SimpleNamespace] | SimpleNamespace`): Список продуктов, которые будут включены в HTML. Может быть как списком, так и отдельным объектом `SimpleNamespace`.
- `category_path` (`str | Path`): Путь для сохранения HTML-файла.

**Возвращает**:
- `None`: Функция ничего не возвращает.

### `CampaignHTMLGenerator`

**Описание**: Класс для генерации HTML-кода для кампании.

#### `set_campaign_html`

**Описание**: Создает HTML-файл для кампании, перечисляя все категории.

**Параметры**:
- `categories` (`list[str]`): Список названий категорий.
- `campaign_path` (`str | Path`): Путь для сохранения HTML-файла.

**Возвращает**:
- `None`: Функция ничего не возвращает.