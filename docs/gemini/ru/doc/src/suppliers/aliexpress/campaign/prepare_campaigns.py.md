# Модуль для подготовки кампаний AliExpress

## Обзор

Модуль `prepare_campaigns.py` предназначен для подготовки рекламных кампаний AliExpress. Он включает в себя обработку категорий, управление данными кампании и генерацию рекламных материалов. Модуль позволяет обрабатывать как отдельные категории в рамках кампании, так и кампании целиком, а также поддерживает мультиязычность и работу с разными валютами.

## Подробней

Модуль является частью проекта `hypotez` и располагается в директории `src/suppliers/aliexpress/campaign`. Он используется для автоматизации процесса подготовки рекламных кампаний на AliExpress, что позволяет оптимизировать усилия маркетологов и повысить эффективность рекламных кампаний.

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

**Назначение**: Обрабатывает конкретную категорию в рамках кампании для заданного языка и валюты.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `category_name` (str): Категория для кампании.
- `language` (str): Язык для кампании.
- `currency` (str): Валюта для кампании.

**Возвращает**:
- `List[str]`: Список названий продуктов в категории.

**Как работает функция**:
1. Функция `process_campaign_category` создает экземпляр класса `AliCampaignEditor`.
2. Вызывает метод `process_campaign_category` этого экземпляра, передавая имя категории.
3. Возвращает список заголовков продуктов, полученный в результате обработки категории.

**Примеры**:

```python
titles: List[str] = process_campaign_category("summer_sale", "electronics", "EN", "USD")
print(titles)
# Output: ['Product 1', 'Product 2']
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

**Назначение**: Обрабатывает кампанию, выполняя её настройку и обработку.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `language` (Optional[str]): Язык для кампании. Если не указан, обрабатываются все локали.
- `currency` (Optional[str]): Валюта для кампании. Если не указана, обрабатываются все локали.
- `campaign_file` (Optional[str]): Необязательный путь к файлу кампании.

**Возвращает**:
- `bool`: `True`, если кампания обработана, иначе `False`.

**Как работает функция**:
1. Функция `process_campaign` преобразует список словарей локалей в список пар (язык, валюта).
2. Если указаны язык и валюта, фильтрует список локалей по ним.
3. Для каждой пары (язык, валюта) создает экземпляр класса `AliCampaignEditor`.
4. Вызывает метод `process_campaign` этого экземпляра.
5. Все ошибки логируются с использованием `logger.error`.

**Примеры**:

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

**Назначение**: Обрабатывает все кампании в директории `campaigns` для указанного языка и валюты.

**Параметры**:
- `language` (Optional[str]): Язык для кампаний.
- `currency` (Optional[str]): Валюта для кампаний.

**Как работает функция**:
1. Функция `process_all_campaigns` получает список всех директорий кампаний.
2. Если язык и валюта не указаны, обрабатываются все локали.
3. Для каждой кампании и локали создает экземпляр класса `AliCampaignEditor`.
4. Вызывает метод `process_campaign` этого экземпляра.

**Примеры**:

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

**Назначение**: Главная функция для обработки кампании.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `categories` (List[str] | str): Список категорий для кампании. Если пуст, обрабатывается вся кампания без конкретных категорий.
- `language` (Optional[str]): Язык для кампании.
- `currency` (Optional[str]): Валюта для кампании.

**Как работает функция**:
1. Функция `main_process` определяет локали для обработки на основе предоставленных языка и валюты.
2. Если указаны категории, обрабатывает каждую категорию с помощью функции `process_campaign_category`.
3. Если категории не указаны, обрабатывает всю кампанию с помощью функции `process_campaign`.

**Примеры**:

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

**Назначение**: Главная функция для разбора аргументов командной строки и запуска обработки.

**Как работает функция**:
1. Функция `main` создает парсер аргументов командной строки с использованием `argparse`.
2. Определяет аргументы, которые можно передать скрипту, такие как название кампании, список категорий, язык и валюта.
3. Если указан аргумент `--all`, вызывается функция `process_all_campaigns`.
4. Иначе вызывается функция `main_process` с переданными аргументами.

**Примеры**:

```python
main()