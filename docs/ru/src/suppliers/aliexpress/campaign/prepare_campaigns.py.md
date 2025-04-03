# Модуль для подготовки кампаний AliExpress

## Обзор

Модуль `prepare_campaigns.py` предназначен для подготовки рекламных кампаний на платформе AliExpress. Он включает в себя функции для обработки категорий, управления данными кампаний и генерации промо-материалов. Модуль позволяет обрабатывать как отдельные категории в рамках кампании, так и кампании целиком, а также поддерживает мультиязычность и работу с различными валютами.

## Подробнее

Этот скрипт используется для автоматизации процесса подготовки кампаний AliExpress, что включает в себя извлечение и обработку данных о товарах, адаптацию контента под разные языки и валюты, а также генерацию необходимых рекламных материалов. Он позволяет упростить и ускорить процесс запуска рекламных кампаний, уменьшая объем ручной работы и повышая эффективность.

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

**Назначение**: Обрабатывает конкретную категорию в рамках рекламной кампании для заданного языка и валюты.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `category_name` (str): Категория для кампании.
- `language` (str): Язык для кампании.
- `currency` (str): Валюта для кампании.

**Возвращает**:
- `List[str]`: Список названий товаров в категории.

**Как работает функция**:
1. Создает экземпляр класса `AliCampaignEditor` с указанными параметрами кампании (название, язык, валюта).
2. Вызывает метод `process_campaign_category` этого экземпляра, передавая название категории для обработки.
3. Возвращает список названий товаров, полученных в результате обработки категории.

```ascii
    Начало
     |
     V
Создание экземпляра AliCampaignEditor
     |
     V
Вызов process_campaign_category
     |
     V
  Возврат списка названий товаров
     |
    Конец
```

**Примеры**:
```python
titles: List[str] = process_campaign_category("summer_sale", "electronics", "EN", "USD")
print(titles) #  ['Product 1', 'Product 2']
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

**Назначение**: Обрабатывает рекламную кампанию, выполняет ее настройку и обработку.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `language` (Optional[str]): Язык для кампании. Если не указан, обрабатываются все локали.
- `currency` (Optional[str]): Валюта для кампании. Если не указана, обрабатываются все локали.
- `campaign_file` (Optional[str]): Необязательный путь к файлу кампании.

**Возвращает**:
- `bool`: `True`, если кампания успешно обработана, иначе `False`.

**Как работает функция**:
1. Определяет список локалей для обработки, основываясь на предоставленных языке и валюте. Если язык и валюта не указаны, используются все доступные локали.
2. Для каждой локали (язык и валюта) создает экземпляр класса `AliCampaignEditor` с соответствующими параметрами.
3. Вызывает метод `process_campaign` этого экземпляра для обработки кампании.
4. Возвращает `True`, предполагая, что кампания всегда успешно обрабатывается.

```ascii
    Начало
     |
     V
Определение списка локалей
     |
     V
Для каждой локали:
 |   Создание экземпляра AliCampaignEditor
 |   Вызов process_campaign
     |
     V
  Возврат True
     |
    Конец
```

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

**Назначение**: Обрабатывает все кампании, находящиеся в директории 'campaigns', для указанного языка и валюты.

**Параметры**:
- `language` (Optional[str]): Язык для кампаний.
- `currency` (Optional[str]): Валюта для кампаний.

**Как работает функция**:
1. Определяет список локалей для обработки, основываясь на предоставленных языке и валюте. Если язык и валюта не указаны, используются все доступные локали.
2. Получает список названий директорий в директории `campaigns`.
3. Для каждой кампании в списке создает экземпляр класса `AliCampaignEditor` с соответствующими параметрами (название кампании, язык, валюта).
4. Вызывает метод `process_campaign` этого экземпляра для обработки кампании.

```ascii
    Начало
     |
     V
Определение списка локалей
     |
     V
Получение списка кампаний
     |
     V
Для каждой кампании:
 |   Создание экземпляра AliCampaignEditor
 |   Вызов process_campaign
     |
    Конец
```

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
- `categories` (List[str] | str): Список категорий для кампании. Если список пуст, кампания обрабатывается без привязки к конкретным категориям.
- `language` (Optional[str]): Язык для кампании.
- `currency` (Optional[str]): Валюта для кампании.

**Как работает функция**:
1. Определяет список локалей для обработки, основываясь на предоставленных языке и валюте. Если язык и валюта не указаны, используются все доступные локали.
2. Для каждой локали (язык и валюта) проверяет, указаны ли категории.
3. Если категории указаны, вызывает функцию `process_campaign_category` для каждой категории.
4. Если категории не указаны, вызывает функцию `process_campaign` для обработки всей кампании.

```ascii
    Начало
     |
     V
Определение списка локалей
     |
     V
Для каждой локали:
 |   Проверка наличия категорий
 |   |
 |   Да: Для каждой категории:
 |   |    Вызов process_campaign_category
 |   |
 |   Нет: Вызов process_campaign
     |
    Конец
```

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

**Назначение**: Главная функция для разбора аргументов командной строки и инициации процесса обработки кампании.

**Как работает функция**:
1. Создает парсер аргументов командной строки с использованием `argparse`.
2. Определяет аргументы, которые можно передать скрипту: название кампании, список категорий, язык, валюта и флаг для обработки всех кампаний.
3. Разбирает аргументы, переданные скрипту.
4. Если указан флаг `--all`, вызывает функцию `process_all_campaigns` для обработки всех кампаний.
5. Иначе вызывает функцию `main_process` для обработки указанной кампании с заданными параметрами (название, категории, язык, валюта).

```ascii
    Начало
     |
     V
Создание парсера аргументов
     |
     V
Разбор аргументов
     |
     V
Проверка флага --all
     |
     V
Да: Вызов process_all_campaigns
     |
     V
Нет: Вызов main_process
     |
    Конец
```

**Примеры**:
```python
main()