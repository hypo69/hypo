# Модуль `prepare_all_campaigns`

## Обзор

Модуль `prepare_all_campaigns` предназначен для запуска обработки рекламных кампаний AliExpress для всех языков с извлечением названий категорий из директорий. Он использует функции из модуля `prepare_campaigns` для подготовки и обработки кампаний.

## Подробней

Этот модуль является частью экспериментов по подготовке рекламных кампаний AliExpress. Он импортирует и использует функции `process_all_campaigns` и `main_process` из модуля `src.suppliers.aliexpress.campaign.prepare_campaigns`. Модуль выполняет настройку и запуск процесса подготовки рекламных кампаний для указанных языков и валют.

## Функции

### `process_campaign`

```python
process_campaign(campaign_name: str, language: str, currency: str, campaign_file: str) -> None:
    """
    Args:
        campaign_name (str): Название рекламной кампании.
        language (str): Язык кампании.
        currency (str): Валюта кампании.
        campaign_file (str): Путь к файлу кампании (может быть `None`).
    Returns:
        None: Функция ничего не возвращает.
    """
```

**Описание**: Запускает процесс подготовки рекламной кампании с заданными параметрами. Если рекламная кампания не существует, будет создана новая.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.
- `campaign_file` (str): Путь к файлу кампании.

**Примеры**:
```python
process_campaign(campaign_name = 'rc', language = 'EN', currency = 'USD', campaign_file = None)
```

### `main_process`

```python
main_process(arg1: str, arg2: list[str]) -> None:
    """
    Args:
        arg1 (str): Первый аргумент для main_process.
        arg2 (list[str]): Второй аргумент для main_process.
    Returns:
        None: Функция ничего не возвращает.
    """
```

**Описание**: Выполняет основной процесс подготовки кампаний для указанных брендов.

**Параметры**:
- `arg1` (str): Первый аргумент для `main_process`.
- `arg2` (list[str]): Второй аргумент для `main_process`.

**Примеры**:
```python
main_process('brands', ['mrgreen'])