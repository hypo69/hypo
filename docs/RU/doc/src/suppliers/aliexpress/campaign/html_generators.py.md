# Модуль `html_generators`

## Обзор

Модуль `html_generators.py` предназначен для генерации HTML-контента для рекламных кампаний, включая HTML-страницы для отдельных продуктов, категорий продуктов и общую страницу кампании.

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

**Описание**: Класс для генерации HTML для отдельных продуктов.

#### `set_product_html`

```python
@staticmethod
def set_product_html(product: SimpleNamespace, category_path: str | Path):
    """
    Args:
        product (SimpleNamespace): Детали продукта для включения в HTML.
        category_path (str | Path): Путь для сохранения HTML-файла.

    Returns:
        None: Функция ничего не возвращает.

    Raises:
        None: Функция не вызывает исключений.
    """
```

**Описание**: Создает HTML-файл для отдельного продукта.
  
**Параметры**:
   - `product` (`SimpleNamespace`): Детали продукта, которые будут включены в HTML.
   - `category_path` (`str | Path`): Путь, по которому будет сохранен HTML-файл.
  
**Возвращает**:
  - `None`: Функция ничего не возвращает.
  
**Вызывает исключения**:
  - Нет.

### `CategoryHTMLGenerator`

**Описание**: Класс для генерации HTML для категорий продуктов.

#### `set_category_html`

```python
@staticmethod
def set_category_html(products_list: list[SimpleNamespace] | SimpleNamespace, category_path: str | Path):
    """
    Args:
        products_list (list[SimpleNamespace] | SimpleNamespace): Список продуктов для включения в HTML.
        category_path (str | Path): Путь для сохранения HTML-файла.

    Returns:
        None: Функция ничего не возвращает.

    Raises:
        None: Функция не вызывает исключений.
    """
```

**Описание**: Создает HTML-файл для категории.
  
**Параметры**:
  - `products_list` (`list[SimpleNamespace] | SimpleNamespace`): Список продуктов, которые будут включены в HTML.
  - `category_path` (`str | Path`): Путь, по которому будет сохранен HTML-файл.
  
**Возвращает**:
  - `None`: Функция ничего не возвращает.
  
**Вызывает исключения**:
  - Нет.

### `CampaignHTMLGenerator`

**Описание**: Класс для генерации HTML для кампании.

#### `set_campaign_html`

```python
@staticmethod
def set_campaign_html(categories: list[str], campaign_path: str | Path):
    """
    Args:
        categories (list[str]): Список названий категорий.
        campaign_path (str | Path): Путь для сохранения HTML-файла.

    Returns:
        None: Функция ничего не возвращает.

    Raises:
        None: Функция не вызывает исключений.
    """
```

**Описание**: Создает HTML-файл для кампании, в котором перечислены все категории.
  
**Параметры**:
  - `categories` (`list[str]`): Список названий категорий.
  - `campaign_path` (`str | Path`): Путь, по которому будет сохранен HTML-файл.
  
**Возвращает**:
  - `None`: Функция ничего не возвращает.
  
**Вызывает исключения**:
  - Нет.