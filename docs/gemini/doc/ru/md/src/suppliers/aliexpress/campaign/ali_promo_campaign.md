# Модуль `hypotez/src/suppliers/aliexpress/campaign/ali_promo_campaign.py`

## Обзор

Этот модуль предоставляет класс `AliPromoCampaign` для управления рекламными кампаниями на AliExpress. Он позволяет загружать и обрабатывать данные о кампаниях, категориях и товарах, а также использовать ИИ для генерации дополнительных данных. Модуль поддерживает различные языки и валюты, что обеспечивает гибкость в настройке кампаний.

## Классы

### `AliPromoCampaign`

**Описание**: Класс для управления рекламной кампанией на AliExpress.  Позволяет загружать данные, обрабатывать категории и товары, а также использовать ИИ для генерации описаний и другой информации.

**Атрибуты**:

- `language`: Язык кампании.
- `currency`: Валюта кампании.
- `base_path`: Путь к директории с данными кампании.
- `campaign_name`: Название кампании.
- `campaign`: Объект `SimpleNamespace` с данными о кампании.
- `campaign_ai`: Объект `SimpleNamespace` для данных кампании, генерируемых ИИ.
- `gemini`: Модель ИИ Gemini.
- `openai`: Модель ИИ OpenAI.


**Методы**:

#### `__init__(self, campaign_name: str, language: Optional[str] = None, currency: Optional[str] = None, model: str = 'openai')`

**Описание**: Инициализирует объект `AliPromoCampaign` для работы с указанной рекламной кампанией.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (Optional[str], optional): Язык кампании. По умолчанию `None`.
- `currency` (Optional[str], optional): Валюта кампании. По умолчанию `None`.
- `model` (str, optional): Тип модели ИИ (`openai` или `gemini`). По умолчанию `'openai'`.

**Возвращает**:
- `SimpleNamespace`: Объект, представляющий данные кампании.


#### `process_campaign(self)`

**Описание**: Обрабатывает все категории в рамках рекламной кампании, используя генератор партнерских ссылок.

**Пример**:
```python
campaign.process_campaign()
```


#### `process_category_products(self, category_name: str) -> Optional[List[SimpleNamespace]]`

**Описание**: Обрабатывает товары в указанной категории.

**Параметры**:
- `category_name` (str): Название категории.

**Возвращает**:
- `Optional[List[SimpleNamespace]]`: Список объектов `SimpleNamespace`, представляющих товары, или `None`, если товары не найдены.


#### `process_ai_category(self, category_name: Optional[str] = None)`

**Описание**: Обрабатывает данные категории с помощью ИИ.

**Параметры**:
- `category_name` (Optional[str], optional): Название категории для обработки. Если не указано, обрабатываются все категории.

**Пример**:
```python
campaign.process_ai_category("Electronics")
```


#### `process_new_campaign(self, campaign_name: str, language: Optional[str] = None, currency: Optional[str] = None)`

**Описание**: Создаёт новую рекламную кампанию.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (Optional[str], optional): Язык. По умолчанию `None`.
- `currency` (Optional[str], optional): Валюта. По умолчанию `None`.


#### `dump_category_products_files(self, category_name: str, products: List[SimpleNamespace])`

**Описание**: Сохраняет данные о товарах в файлы JSON.

**Параметры**:
- `category_name` (str): Имя категории.
- `products` (List[SimpleNamespace]): Список объектов, представляющих товары.


#### `set_categories_from_directories(self)`

**Описание**: Устанавливает категории кампании из названий директорий.


#### `generate_output(self, campaign_name: str, category_path: str | Path, products_list: list[SimpleNamespace] | SimpleNamespace)`

**Описание**: Сохраняет данные о товарах в различных форматах (JSON, HTML).


#### `generate_html_for_campaign(self, campaign_name: str)`

**Описание**: Генерирует HTML-страницы для рекламной кампании.


## Функции

(Здесь будут описания функций, если они существуют)


## Примеры использования

```python
# Пример инициализации кампании
campaign = AliPromoCampaign("SummerSale", "EN", "USD")
print(campaign.campaign_name)

# Пример обработки категории
products = campaign.process_category_products("Electronics")
```

**Примечание**:  В данном ответе подробные описания параметров, возвращаемых значений и исключений для всех методов и функций были взяты из комментариев внутри исходного кода Python.  Так как исходный код довольно обширный, этот ответ охватывает основные аспекты.