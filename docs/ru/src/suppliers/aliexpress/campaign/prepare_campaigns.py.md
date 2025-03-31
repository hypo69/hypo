# Модуль для подготовки кампаний AliExpress

## Обзор

Модуль `prepare_campaigns.py` предназначен для подготовки рекламных кампаний AliExpress. Он включает в себя функции для обработки категорий, данных кампаний и генерации рекламных материалов. Модуль поддерживает обработку как отдельных кампаний, так и всех кампаний в указанной директории, с возможностью указания языка и валюты.

## Подробней

Этот модуль играет важную роль в автоматизации процесса подготовки кампаний AliExpress. Он позволяет обрабатывать кампании для различных языковых и валютных настроек, а также фильтровать товары по категориям. Основная цель модуля - упростить и ускорить процесс создания и запуска рекламных кампаний.

## Оглавление

- [Функции](#Функции)
  - [`process_campaign_category`](#process_campaign_category)
  - [`process_campaign`](#process_campaign)
  - [`process_all_campaigns`](#process_all_campaigns)
  - [`main_process`](#main_process)
  - [`main`](#main)

## Функции

### `process_campaign_category`

```python
def process_campaign_category(
    campaign_name: str, category_name: str, language: str, currency: str
) -> List[str]:
    """Processes a specific category within a campaign for a given language and currency.

    Args:
        campaign_name (str): Name of the advertising campaign.
        category_name (str): Category for the campaign.
        language (str): Language for the campaign.
        currency (str): Currency for the campaign.

    Returns:
        List[str]: List of product titles within the category.

    Example:
        >>> titles: List[str] = process_campaign_category("summer_sale", "electronics", "EN", "USD")
        >>> print(titles)
        ['Product 1', 'Product 2']
    """
```

**Описание**: Обрабатывает указанную категорию в рамках кампании для заданного языка и валюты.

**Как работает функция**: Функция создает экземпляр класса `AliCampaignEditor` с указанными параметрами кампании (название, язык, валюта) и вызывает метод `process_campaign_category` этого экземпляра, передавая имя категории. Результатом является список названий продуктов в данной категории.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `category_name` (str): Категория для кампании.
- `language` (str): Язык для кампании.
- `currency` (str): Валюта для кампании.

**Возвращает**:
- `List[str]`: Список названий продуктов в указанной категории.

**Пример**:
```python
titles: List[str] = process_campaign_category("summer_sale", "electronics", "EN", "USD")
print(titles)
# Вывод: ['Product 1', 'Product 2']
```

### `process_campaign`

```python
def process_campaign(
    campaign_name: str,
    language: Optional[str] = None,
    currency: Optional[str] = None,
    campaign_file: Optional[str] = None,
) -> bool:
    """Processes a campaign and handles the campaign's setup and processing.

    Args:
        campaign_name (str): Name of the advertising campaign.
        language (Optional[str]): Language for the campaign. If not provided, process for all locales.
        currency (Optional[str]): Currency for the campaign. If not provided, process for all locales.
        campaign_file (Optional[str]): Optional path to a specific campaign file.

    Example:
        >>> res = process_campaign("summer_sale", "EN", "USD", "campaign_file.json")

    Returns:
        bool: True if campaign processed, else False.
    """
```

**Описание**: Обрабатывает кампанию, выполняет настройку и обработку кампании.

**Как работает функция**: Функция сначала преобразует список словарей локалей в список пар (язык, валюта). Если указаны язык и валюта, список фильтруется по ним. Затем для каждой пары (язык, валюта) создается экземпляр класса `AliCampaignEditor` и вызывается метод `process_campaign` этого экземпляра. Логируется начало обработки каждой кампании.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `language` (Optional[str]): Язык для кампании (необязательный). Если не указан, обрабатываются все локали.
- `currency` (Optional[str]): Валюта для кампании (необязательная). Если не указана, обрабатываются все локали.
- `campaign_file` (Optional[str]): Путь к файлу кампании (необязательный).

**Возвращает**:
- `bool`: `True`, если кампания обработана успешно, иначе `False`.

**Пример**:
```python
res = process_campaign("summer_sale", "EN", "USD", "campaign_file.json")
```

### `process_all_campaigns`

```python
def process_all_campaigns(language: Optional[str] = None, currency: Optional[str] = None) -> None:
    """Processes all campaigns in the 'campaigns' directory for the specified language and currency.

    Args:
        language (Optional[str]): Language for the campaigns.
        currency (Optional[str]): Currency for the campaigns.

    Example:
        >>> process_all_campaigns("EN", "USD")
    """
```

**Описание**: Обрабатывает все кампании в директории 'campaigns' для указанного языка и валюты.

**Как работает функция**: Функция получает список локалей (язык, валюта). Если язык и валюта не указаны, обрабатываются все доступные локали. Затем для каждой локали перебираются все директории кампаний и для каждой кампании создается экземпляр класса `AliCampaignEditor`, после чего вызывается метод `process_campaign`. Логируется начало обработки каждой кампании.

**Параметры**:
- `language` (Optional[str]): Язык для кампаний (необязательный).
- `currency` (Optional[str]): Валюта для кампаний (необязательная).

**Пример**:
```python
process_all_campaigns("EN", "USD")
```

### `main_process`

```python
def main_process(campaign_name: str, categories: List[str] | str, language: Optional[str] = None, currency: Optional[str] = None) -> None:
    """Main function to process a campaign.

    Args:
        campaign_name (str): Name of the advertising campaign.
        categories (List[str]): List of categories for the campaign. If empty, process the campaign without specific categories.
        language (Optional[str]): Language for the campaign.
        currency (Optional[str]): Currency for the campaign.

    Example:
        >>> main_process("summer_sale", ["electronics"], "EN", "USD")
        >>> main_process("summer_sale", [], "EN", "USD")
    """
```

**Описание**: Главная функция для обработки кампании.

**Как работает функция**: Функция определяет локали для обработки на основе предоставленных языка и валюты. Если указаны категории, то для каждой категории вызывается функция `process_campaign_category`. Если категории не указаны, вызывается функция `process_campaign` для обработки всей кампании. Логируется процесс обработки кампании и категорий.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `categories` (List[str] | str): Список категорий для кампании. Если пустой, обрабатывается вся кампания без фильтрации по категориям.
- `language` (Optional[str]): Язык для кампании (необязательный).
- `currency` (Optional[str]): Валюта для кампании (необязательная).

**Пример**:
```python
main_process("summer_sale", ["electronics"], "EN", "USD")
main_process("summer_sale", [], "EN", "USD")
```

### `main`

```python
def main() -> None:
    """Main function to parse arguments and initiate processing.

    Example:
        >>> main()
    """
```

**Описание**: Главная функция для разбора аргументов командной строки и инициации процесса обработки кампании.

**Как работает функция**: Функция использует `argparse` для разбора аргументов командной строки, таких как название кампании, список категорий, язык и валюта. В зависимости от переданных аргументов вызывается либо функция `process_all_campaigns` для обработки всех кампаний, либо функция `main_process` для обработки конкретной кампании.

**Пример**:
```python
main()