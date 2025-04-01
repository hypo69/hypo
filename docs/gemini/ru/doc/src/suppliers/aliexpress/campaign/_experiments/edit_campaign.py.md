# Модуль редактирования рекламной кампании AliExpress

## Обзор

Этот модуль предназначен для редактирования рекламных кампаний на платформе AliExpress. Он предоставляет функциональность для изменения параметров кампании, обработки категорий кампании и управления всеми кампаниями.

## Подробнее

Модуль `edit_campaign.py` является частью пакета `src.suppliers.aliexpress.campaign._experiments` и предназначен для экспериментов с редактированием рекламных кампаний AliExpress. Он использует другие модули из этого же пакета, такие как `AliCampaignEditor`, `process_campaign`, `process_campaign_category` и `process_all_campaigns`, а также утилиты из `src.utils` для получения имен файлов и каталогов.

## Импортированные модули

- `header`: Предположительно, содержит общие определения или настройки. (Требуется дополнительная информация о содержимом модуля).
- `pathlib.Path`: Используется для работы с путями к файлам и каталогам.
- `src.gs`: (Требуется дополнительная информация о содержимом модуля).
- `src.suppliers.aliexpress.campaign.AliCampaignEditor`: Класс для редактирования рекламных кампаний AliExpress.
- `src.suppliers.aliexpress.campaign.process_campaign`: Функция для обработки кампании.
- `src.suppliers.aliexpress.campaign.process_campaign_category`: Функция для обработки категории кампании.
- `src.suppliers.aliexpress.campaign.process_all_campaigns`: Функция для обработки всех кампаний.
- `src.utils.get_filenames`: Функция для получения имен файлов.
- `src.utils.get_directory_names`: Функция для получения имен каталогов.
- `src.utils.printer.pprint`: Функция для "красивой" печати данных.

## Переменные

- `locales (dict)`: Словарь, содержащий соответствия между кодами языков (`EN`, `HE`, `RU`) и кодами валют (`USD`, `ILS`).

## Пример использования

В коде заданы значения для `campaign_name` и `category_name`, которые используются для создания экземпляра класса `AliCampaignEditor`.

```python
campaign_name = "building_bricks"
category_name = "building_bricks"
a = AliCampaignEditor(campaign_name,'EN','USD')
...
```
## Классы

### `AliCampaignEditor`

**Описание**: Класс `AliCampaignEditor` используется для редактирования рекламных кампаний AliExpress.

**Принцип работы**:
   - Класс инициализируется с именем кампании, языком и валютой. Он предоставляет методы для изменения различных параметров кампании. (Более подробное описание требует анализа кода класса `AliCampaignEditor`).

```python
class AliCampaignEditor:
    """
    Класс для редактирования рекламных кампаний AliExpress.

    Args:
        campaign_name (str): Имя кампании.
        language (str): Язык кампании.
        currency (str): Валюта кампании.
    """
    ...
```

## Функции

### `process_campaign`

```python
def process_campaign(campaign_name: str) -> None:
    """
    Функция для обработки кампании.

    Args:
        campaign_name (str): Имя кампании.

    Returns:
        None
    """
    ...
```

### `process_campaign_category`

```python
def process_campaign_category(category_name: str) -> None:
    """
    Функция для обработки категории кампании.

    Args:
        category_name (str): Имя категории кампании.

    Returns:
        None
    """
    ...
```

### `process_all_campaigns`

```python
def process_all_campaigns() -> None:
    """
    Функция для обработки всех кампаний.

    Returns:
        None
    """
    ...
```

### `get_filenames`

```python
def get_filenames(path: str) -> list[str]:
    """
    Функция для получения имен файлов в указанном пути.

    Args:
        path (str): Путь к каталогу.

    Returns:
        list[str]: Список имен файлов.
    """
    ...
```

### `get_directory_names`

```python
def get_directory_names(path: str) -> list[str]:
    """
    Функция для получения имен каталогов в указанном пути.

    Args:
        path (str): Путь к каталогу.

    Returns:
        list[str]: Список имен каталогов.
    """
    ...