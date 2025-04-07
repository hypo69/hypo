# Модуль для подготовки кампаний AliExpress

## Обзор

Модуль `prepare_campaigns.py` предназначен для автоматизации процесса подготовки рекламных кампаний на платформе AliExpress. Он позволяет обрабатывать кампании по категориям, управлять данными кампаний и генерировать рекламные материалы. Модуль поддерживает обработку как отдельных кампаний, так и всех кампаний в указанной директории.

## Подробнее

Этот скрипт предназначен для автоматизации процесса подготовки рекламных кампаний на AliExpress. Он принимает аргументы командной строки для указания имени кампании, категорий, языка и валюты. Если указан параметр `--all`, скрипт обработает все кампании, найденные в каталоге `campaigns` на Google Drive.  Скрипт использует класс `AliCampaignEditor` для выполнения фактической обработки кампании, включая сбор данных о продуктах, перевод контента и создание рекламных материалов. Логика работы строится на обходе списка локалей (язык, валюта) и вызове соответствующих функций обработки кампаний и категорий.  Результаты работы скрипта включают подготовленные файлы кампаний, готовые для загрузки на платформу AliExpress.

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

**Назначение**: Обрабатывает определенную категорию в рамках рекламной кампании для указанного языка и валюты.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `category_name` (str): Категория для кампании.
- `language` (str): Язык для кампании.
- `currency` (str): Валюта для кампании.

**Возвращает**:
- `List[str]`: Список названий продуктов в категории.

**Как работает функция**:
1. Создает экземпляр класса `AliCampaignEditor` с переданными параметрами кампании, языка и валюты.
2. Вызывает метод `process_campaign_category` экземпляра `AliCampaignEditor` для обработки указанной категории.
3. Возвращает список названий продуктов, полученных в результате обработки категории.

```
    Начало
    │
    Создание экземпляра AliCampaignEditor
    │
    Вызов process_campaign_category
    │
    Возврат списка названий продуктов
    │
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

**Назначение**: Обрабатывает рекламную кампанию, выполняет настройку и обработку кампании для указанного языка и валюты.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `language` (Optional[str]): Язык для кампании. Если не указан, обрабатываются все локали.
- `currency` (Optional[str]): Валюта для кампании. Если не указана, обрабатываются все локали.
- `campaign_file` (Optional[str]): Необязательный путь к файлу кампании.

**Возвращает**:
- `bool`: `True`, если кампания успешно обработана, иначе `False`.

**Как работает функция**:
1. Определяет список локалей (`_l`) для обработки, если язык и валюта не указаны, то используются все доступные локали из `locales`.
2. Если указаны язык и валюта, фильтрует список локалей, оставляя только указанные значения.
3. Итерируется по списку локалей, создавая для каждой локали экземпляр `AliCampaignEditor`.
4. Вызывает метод `process_campaign` экземпляра `AliCampaignEditor` для обработки кампании.
5. Возвращает `True`, предполагая, что кампания всегда успешно обрабатывается.

```
    Начало
    │
    Определение списка локалей
    │
    Фильтрация списка локалей (если указаны язык и валюта)
    │
    Цикл по списку локалей
    │
    Создание экземпляра AliCampaignEditor
    │
    Вызов process_campaign
    │
    Конец цикла
    │
    Возврат True
    │
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

**Назначение**: Обрабатывает все кампании в директории `campaigns` для указанного языка и валюты.

**Параметры**:
- `language` (Optional[str]): Язык для кампаний. Если не указан, обрабатываются все локали.
- `currency` (Optional[str]): Валюта для кампаний. Если не указана, обрабатываются все локали.

**Как работает функция**:
1. Определяет список локалей (`_l`) для обработки, если язык и валюта не указаны, то используются все доступные локали из `locales`.
2. Получает список названий директорий кампаний из директории `campaigns_directory`.
3. Итерируется по списку названий директорий кампаний.
4. Для каждой кампании создает экземпляр `AliCampaignEditor` с указанными параметрами кампании, языка и валюты.
5. Вызывает метод `process_campaign` экземпляра `AliCampaignEditor` для обработки кампании.

```
    Начало
    │
    Определение списка локалей
    │
    Получение списка директорий кампаний
    │
    Цикл по списку директорий кампаний
    │
    Создание экземпляра AliCampaignEditor
    │
    Вызов process_campaign
    │
    Конец цикла
    │
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
- `categories` (List[str]  | str): Список категорий для кампании. Если пустой, обрабатывается вся кампания без конкретных категорий.
- `language` (Optional[str]): Язык для кампании.
- `currency` (Optional[str]): Валюта для кампании.

**Как работает функция**:
1. Определяет список локалей (`locales_to_process`) для обработки, если язык и валюта не указаны, то используются все доступные локали из `locales`.
2. Итерируется по списку локалей.
3. Если указаны категории, то для каждой категории вызывается функция `process_campaign_category`.
4. Если категории не указаны, то вызывается функция `process_campaign` для обработки всей кампании.

```
    Начало
    │
    Определение списка локалей
    │
    Цикл по списку локалей
    │
    Условие: указаны ли категории?
    ├─── Да ─── Цикл по категориям
    │           │
    │           Вызов process_campaign_category
    │           │
    │           Конец цикла
    │
    └─── Нет ─── Вызов process_campaign
    │
    Конец цикла
    │
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

**Назначение**: Главная функция для разбора аргументов командной строки и инициации обработки кампании.

**Как работает функция**:
1. Создает парсер аргументов командной строки `argparse.ArgumentParser`.
2. Добавляет аргументы для:
   - `campaign_name` (обязательный) - название кампании.
   - `-c`, `--categories` (необязательный) - список категорий.
   - `-l`, `--language` (необязательный) - язык кампании.
   - `-cu`, `--currency` (необязательный) - валюта кампании.
   - `--all` (необязательный) - флаг для обработки всех кампаний.
3. Разбирает аргументы командной строки с помощью `parser.parse_args()`.
4. Если указан флаг `--all`, вызывает функцию `process_all_campaigns` с переданными языком и валютой.
5. Иначе вызывает функцию `main_process` с переданными названием кампании, списком категорий (или пустым списком, если категории не указаны), языком и валютой.

```
    Начало
    │
    Создание парсера аргументов
    │
    Добавление аргументов
    │
    Разбор аргументов
    │
    Условие: указан ли флаг --all?
    ├─── Да ─── Вызов process_all_campaigns
    │
    └─── Нет ─── Вызов main_process
    │
    Конец
```

**Примеры**:

Примеры вызова функции `main` не могут быть продемонстрированы непосредственно в коде, так как она вызывается при запуске скрипта из командной строки.  Примеры запуска скрипта из командной строки:

```bash
python src/suppliers/aliexpress/campaigns/prepare_campaigns.py summer_sale -c electronics -l EN -cu USD
python src/suppliers/aliexpress/campaigns/prepare_campaigns.py --all -l EN -cu USD