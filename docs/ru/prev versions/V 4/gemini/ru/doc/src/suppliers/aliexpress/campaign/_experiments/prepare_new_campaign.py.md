# Модуль `prepare_new_campaign.py`

## Обзор

Модуль `prepare_new_campaign.py` предназначен для экспериментов с процессом создания новой рекламной кампании на платформе AliExpress. Он использует функциональность класса `AliCampaignEditor` для управления и обработки кампаний.

## Подробнее

Этот модуль содержит логику для инициализации и запуска процесса создания новой рекламной кампании. Он включает импорт необходимых модулей и классов, таких как `AliCampaignEditor`, утилиты для работы с файлами и директориями, а также модуль логирования.

Модуль выполняет следующие основные шаги:

1.  Инициализирует имя кампании (`campaign_name`).
2.  Создает экземпляр класса `AliCampaignEditor` с указанным именем кампании.
3.  Запускает процесс создания новой кампании с помощью метода `process_new_campaign`.

Расположение файла `/src/suppliers/aliexpress/campaign/_experiments/prepare_new_campaign.py` указывает на то, что данный модуль является частью подсистемы управления рекламными кампаниями AliExpress, и используется для проведения экспериментов с процессом подготовки и запуска новых кампаний.

## Импортированные модули

-   `header`: Импортируется модуль `header`, назначение которого не указано в предоставленном коде.
-   `pathlib.Path`: Используется для работы с путями к файлам и директориям.
-   `src.gs`: Импортируется модуль `gs` из пакета `src`, назначение которого не указано в предоставленном коде.
-   `src.suppliers.aliexpress.campaign.AliCampaignEditor`: Класс для управления рекламными кампаниями AliExpress.
-   `src.utils.get_filenames`, `src.utils.get_directory_names`: Утилиты для получения списка файлов и директорий.
-   `src.utils.printer.pprint`: Функция для "pretty" печати данных.
-   `src.logger.logger.logger`: Модуль для логирования событий.

## Переменные

-   `campaign_name` (str): Имя рекламной кампании, по умолчанию `'rc'`.
-   `aliexpress_editor` (AliCampaignEditor): Экземпляр класса `AliCampaignEditor`, используемый для управления кампанией.

## Классы

### `AliCampaignEditor`

**Описание**: Класс, предназначенный для управления рекламными кампаниями AliExpress.

**Методы**:

-   `process_new_campaign`: Метод для запуска процесса создания новой рекламной кампании.

## Функции

### `process_new_campaign`

```python
def process_new_campaign(campaign_name: str) -> None:
    """
    Args:
        campaign_name (str): Имя кампании.

    Returns:
        None:

    Raises:
        Exception: Описание ситуации, в которой возникает исключение.

    Example:
        >>> aliexpress_editor = AliCampaignEditor('test_campaign')
        >>> aliexpress_editor.process_new_campaign('test_campaign')
    """
    ...
```

**Описание**: Запускает процесс создания новой рекламной кампании.

**Параметры**:

-   `campaign_name` (str): Имя кампании, которую необходимо создать.

**Возвращает**:

-   `None`

**Примеры**:

```python
aliexpress_editor = AliCampaignEditor('test_campaign')
aliexpress_editor.process_new_campaign('test_campaign')