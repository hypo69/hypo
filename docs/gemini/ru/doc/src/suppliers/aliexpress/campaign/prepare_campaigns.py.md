# Модуль для подготовки кампаний AliExpress

## Обзор

Модуль `prepare_campaigns.py` предназначен для подготовки рекламных кампаний на платформе AliExpress. Он включает в себя обработку категорий товаров, управление данными кампаний и генерацию рекламных материалов.

## Подробней

Этот скрипт позволяет автоматизировать процесс подготовки кампаний, принимая на вход название кампании, список категорий, язык и валюту. Он может быть использован для обработки как отдельных кампаний, так и всех кампаний в указанной директории. В проекте `hypotez` модуль используется для автоматизации процесса подготовки и запуска рекламных кампаний на AliExpress, что позволяет экономить время и ресурсы.

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
- `List[str]`: Список названий продуктов в рамках категории.

**Как работает функция**:
1. Функция создает экземпляр класса `AliCampaignEditor` с указанными параметрами кампании, языка и валюты.
2. Затем вызывает метод `process_campaign_category` этого экземпляра, передавая название категории.
3. Метод `process_campaign_category` класса `AliCampaignEditor` выполняет всю необходимую логику для обработки категории и возвращает список названий продуктов.

```ascii
Создание AliCampaignEditor --> Вызов process_campaign_category --> Возврат списка названий продуктов
```

**Примеры**:
```python
titles: List[str] = process_campaign_category("summer_sale", "electronics", "EN", "USD")
print(titles) # Вывод: ['Product 1', 'Product 2']
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

**Назначение**: Обрабатывает кампанию, выполняя настройку и обработку данных кампании.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `language` (Optional[str]): Язык для кампании. Если не указан, обрабатываются все локали.
- `currency` (Optional[str]): Валюта для кампании. Если не указана, обрабатываются все локали.
- `campaign_file` (Optional[str]): Необязательный путь к файлу кампании.

**Возвращает**:
- `bool`: `True`, если кампания успешно обработана, иначе `False`.

**Как работает функция**:
1.  Функция создает список кортежей `(language, currency)` на основе доступных локалей.
2.  Если указаны язык и валюта, список фильтруется только по ним.
3.  Для каждой пары `(language, currency)` создается экземпляр класса `AliCampaignEditor` и вызывается метод `process_campaign`.
4.  Предполагается, что кампания всегда обрабатывается успешно, поэтому функция всегда возвращает `True`.

```ascii
Создание списка локалей --> Фильтрация по языку и валюте (если указаны) -->
Для каждой локали:
    Создание AliCampaignEditor --> Вызов process_campaign
--> Возврат True
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

**Назначение**: Обрабатывает все кампании в директории `'campaigns'` для указанного языка и валюты.

**Параметры**:
- `language` (Optional[str]): Язык для кампаний.
- `currency` (Optional[str]): Валюта для кампаний.

**Возвращает**:
- `None`

**Как работает функция**:
1.  Функция определяет список локалей для обработки. Если `language` и `currency` не указаны, используются все доступные локали из `locales`.
2.  Получает список названий директорий кампаний из `campaigns_directory` с помощью `get_directory_names`.
3.  Для каждой кампании создает экземпляр `AliCampaignEditor` и вызывает метод `process_campaign`.

```ascii
Определение списка локалей --> Получение списка директорий кампаний -->
Для каждой кампании:
    Создание AliCampaignEditor --> Вызов process_campaign
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
- `categories` (List[str] | str): Список категорий для кампании. Если пустой, обрабатывается вся кампания без категорий.
- `language` (Optional[str]): Язык для кампании.
- `currency` (Optional[str]): Валюта для кампании.

**Возвращает**:
- `None`

**Как работает функция**:
1.  Определяет список локалей для обработки на основе предоставленных `language` и `currency`.
2.  Если указаны категории, обрабатывает каждую категорию с помощью `process_campaign_category`.
3.  Если категории не указаны, обрабатывает всю кампанию с помощью `process_campaign`.

```ascii
Определение списка локалей -->
Если категории указаны:
    Для каждой категории:
        Вызов process_campaign_category
Иначе:
    Вызов process_campaign
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

**Назначение**: Главная функция для разбора аргументов командной строки и запуска обработки кампании.

**Параметры**:
- Нет

**Возвращает**:
- `None`

**Как работает функция**:
1.  Создает парсер аргументов командной строки `argparse.ArgumentParser`.
2.  Определяет аргументы, которые можно передать скрипту (название кампании, список категорий, язык, валюта, флаг для обработки всех кампаний).
3.  Разбирает переданные аргументы с помощью `parser.parse_args()`.
4.  Если указан флаг `--all`, вызывает функцию `process_all_campaigns`.
5.  Иначе вызывает функцию `main_process` с переданными аргументами.

```ascii
Создание парсера аргументов --> Разбор аргументов командной строки -->
Если указан флаг --all:
    Вызов process_all_campaigns
Иначе:
    Вызов main_process
```

**Примеры**:
```python
main()
```
```