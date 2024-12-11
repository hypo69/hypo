# Модуль `hypotez/src/suppliers/aliexpress/campaign/ali_promo_campaign.py`

## Обзор

Модуль `ali_promo_campaign` предназначен для управления рекламными кампаниями на AliExpress. Он предоставляет класс `AliPromoCampaign`, позволяющий загружать данные о кампаниях, обрабатывать категории и товары, а также использовать AI для генерации дополнительных данных. Модуль поддерживает различные языки и валюты.

## Оглавление

- [Модуль `ali_promo_campaign`](#модуль-ali-promo-campaign)
- [Класс `AliPromoCampaign`](#класс-alipromocampaign)
    - [Метод `__init__`](#метод-init)
    - [Метод `process_campaign`](#метод-processcampaign)
    - [Метод `process_campaign_category`](#метод-processcampaigncategory)
    - [Метод `process_new_campaign`](#метод-processnewcampaign)
    - [Метод `process_ai_category`](#метод-processaicategory)
    - [Метод `process_category_products`](#метод-processcategoryproducts)
    - [Метод `dump_category_products_files`](#метод-dumpcategoryproductsfiles)
    - [Метод `set_categories_from_directories`](#метод-setcategoriesfromdirectories)
    - [Метод `generate_output`](#метод-generateoutput)
    - [Метод `generate_html`](#метод-generatehtml)
    - [Метод `generate_html_for_campaign`](#метод-generatehtmlforcampaign)


## Классы

### `AliPromoCampaign`

**Описание**: Класс для управления рекламными кампаниями на AliExpress.  Позволяет загружать, обрабатывать и генерировать данные о кампаниях, категориях и товарах.

**Атрибуты**:

- `language`: Язык кампании.
- `currency`: Валюта кампании.
- `base_path`: Базовая директория кампании.
- `campaign_name`: Название кампании.
- `campaign`: Объект `SimpleNamespace` с данными о кампании (из файла).
- `campaign_ai`: Объект `SimpleNamespace` с данными о кампании для AI.
- `gemini`: Модель AI Gemini.
- `openai`: Модель AI OpenAI.


**Методы**:

#### `__init__`

```python
def __init__(
    self,
    campaign_name: str,
    language: Optional[str] = None,
    currency: Optional[str] = None,
    model: str = 'openai'
):
    """Инициализация объекта AliPromoCampaign для рекламной кампании.

    Args:
        campaign_name (str): Название кампании.
        language (Optional[str], optional): Язык кампании. По умолчанию None.
        currency (Optional[str], optional): Валюта кампании. По умолчанию None.
        model (str, optional): Выбранная модель AI ('openai' или 'gemini'). По умолчанию 'openai'.

    Returns:
        SimpleNamespace: Объект, представляющий кампанию.

    Raises:
        FileNotFoundError: Если файл кампании не найден.
    """
    ...
```

#### `process_campaign`

```python
def process_campaign(self):
    """Функция итерируется по категориям рекламной кампании и обрабатывает товары категории через генератор партнерских ссылок.
    """
    ...
```

#### `process_campaign_category`

```python
def process_campaign_category(self, campaign_name: str, category_name: str, language: str, currency: str) -> list[SimpleNamespace] | None:
    """Обрабатывает конкретную категорию в рамках кампании для всех языков и валют.
    """
    ...
```

#### `process_new_campaign`

```python
def process_new_campaign(
    self,
    campaign_name: str,
    language: Optional[str] = None,
    currency: Optional[str] = None,
):
    """Создание новой рекламной кампании.
    """
    ...
```

#### `process_ai_category`

```python
def process_ai_category(self, category_name: Optional[str] = None):
    """Обрабатывает категорию с помощью AI.
    """
    ...
```


#### `process_category_products`

```python
def process_category_products(self, category_name: str) -> Optional[List[SimpleNamespace]]:
    """Обрабатывает товары в определенной категории.
    """
    ...
```

#### `dump_category_products_files`

```python
def dump_category_products_files(
    self, category_name: str, products: List[SimpleNamespace]
):
    """Сохраняет данные о товарах в JSON файлы.
    """
    ...
```


#### `set_categories_from_directories`

```python
def set_categories_from_directories(self):
    """Устанавливает категории рекламной кампании из названий директорий.
    """
    ...
```

#### `generate_output`

```python
async def generate_output(self, campaign_name: str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace):
    """Сохраняет данные о товарах в различных форматах.
    """
    ...
```

#### `generate_html`

```python
async def generate_html(self, campaign_name: str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace):
   """ Создает HTML файлы для категории и корневого индекса.
    """
    ...

```

#### `generate_html_for_campaign`

```python
def generate_html_for_campaign(self, campaign_name: str):
    """Генерирует HTML-страницы для рекламной кампании.
    """
    ...
```

(Другие методы и атрибуты документируются аналогично)

## Функции


(Документация функций, если они есть, добавляется сюда)


## Примеры


(Примеры использования модуля и его методов добавляются сюда)