# Модуль `prepare_campaigns`

## Обзор

Модуль `prepare_campaigns` предназначен для подготовки рекламных кампаний AliExpress. Он обрабатывает категории, управляет данными кампании и генерирует рекламные материалы.

## Подробней

Этот модуль предоставляет функциональность для обработки рекламных кампаний AliExpress, включая возможность обработки кампаний по категориям, языкам и валютам. Он использует классы и функции из других модулей проекта для выполнения задач, связанных с обработкой данных и генерацией рекламных материалов. Модуль может быть запущен как скрипт с параметрами командной строки для обработки одной или всех кампаний.

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
    ...
```

**Описание**: Обрабатывает конкретную категорию в рамках кампании для заданного языка и валюты.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `category_name` (str): Категория для кампании.
- `language` (str): Язык для кампании.
- `currency` (str): Валюта для кампании.

**Возвращает**:
- `List[str]`: Список названий продуктов в категории.

**Пример**:
```python
titles: List[str] = process_campaign_category("summer_sale", "electronics", "EN", "USD")
print(titles)
# => ['Product 1', 'Product 2']
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
    ...
```

**Описание**: Обрабатывает кампанию и управляет её настройкой и обработкой.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `language` (Optional[str]): Язык для кампании. Если не указан, обрабатываются все локали.
- `currency` (Optional[str]): Валюта для кампании. Если не указана, обрабатываются все локали.
- `campaign_file` (Optional[str]): Необязательный путь к конкретному файлу кампании.

**Возвращает**:
- `bool`: `True`, если кампания обработана, иначе `False`.

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
    ...
```

**Описание**: Обрабатывает все кампании в каталоге 'campaigns' для указанного языка и валюты.

**Параметры**:
- `language` (Optional[str]): Язык для кампаний.
- `currency` (Optional[str]): Валюта для кампаний.

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
    ...
```

**Описание**: Основная функция для обработки кампании.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `categories` (List[str] | str): Список категорий для кампании. Если пустой, кампания обрабатывается без конкретных категорий.
- `language` (Optional[str]): Язык для кампании.
- `currency` (Optional[str]): Валюта для кампании.

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
    ...
```

**Описание**: Основная функция для разбора аргументов командной строки и запуска обработки.

**Пример**:
```python
main()