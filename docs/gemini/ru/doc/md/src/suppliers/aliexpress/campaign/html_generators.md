# Модуль `hypotez/src/suppliers/aliexpress/campaign/html_generators.py`

## Обзор

Этот модуль содержит классы для генерации HTML-контента для рекламных кампаний AliExpress.  Он предоставляет инструменты для создания страниц отдельных продуктов, категорий продуктов и обзора всей кампании.

## Оглавление

* [Генератор HTML для отдельных продуктов](#генератор-html-для-отдельных-продуктов)
* [Генератор HTML для категорий продуктов](#генератор-html-для-категорий-продуктов)
* [Генератор HTML для всей кампании](#генератор-html-для-всей-кампании)


## Генератор HTML для отдельных продуктов

### `ProductHTMLGenerator`

**Описание**: Класс для генерации HTML для отдельных продуктов.

**Методы**:

#### `set_product_html`

**Описание**: Создает HTML-файл для отдельного продукта.

**Параметры**:
- `product` (SimpleNamespace): Объект, содержащий подробности о продукте (например, `product_id`, `product_title`, `local_saved_image`, `target_sale_price`, `target_sale_price_currency`, `target_original_price`, `target_original_price_currency`, `second_level_category_name`, `promotion_link`).
- `category_path` (str | Path): Путь к каталогу для сохранения HTML-файла.

**Возвращает**:
-  Не возвращает значений. Сохраняет HTML-контент в файл.

**Вызывает исключения**:
- Нет.


## Генератор HTML для категорий продуктов

### `CategoryHTMLGenerator`

**Описание**: Класс для генерации HTML для категорий продуктов.

**Методы**:

#### `set_category_html`

**Описание**: Создает HTML-файл для категории, содержащий список продуктов.

**Параметры**:
- `products_list` (list[SimpleNamespace] | SimpleNamespace): Список объектов `SimpleNamespace`, содержащих подробности о продуктах, или отдельный объект `SimpleNamespace`, представляющий продукт.
- `category_path` (str | Path): Путь к каталогу для сохранения HTML-файла.

**Возвращает**:
- Не возвращает значений. Сохраняет HTML-контент в файл.

**Вызывает исключения**:
- Нет.


## Генератор HTML для всей кампании

### `CampaignHTMLGenerator`

**Описание**: Класс для генерации HTML для всей рекламной кампании.

**Методы**:

#### `set_campaign_html`

**Описание**: Создает HTML-файл для обзора кампании, перечисляющий все категории.

**Параметры**:
- `categories` (list[str]): Список имен категорий.
- `campaign_path` (str | Path): Путь к каталогу для сохранения HTML-файла.

**Возвращает**:
- Не возвращает значений. Сохраняет HTML-контент в файл.

**Вызывает исключения**:
- Нет.