# Модуль `prepare_all_campaigns.py`

## Обзор

Модуль предназначен для запуска подготовки рекламных кампаний для всех языков с использованием названий категорий, полученных из директорий. Он использует функциональность из модуля `prepare_campaigns` для обработки кампаний.

## Подробней

Этот модуль является частью процесса автоматизации подготовки рекламных кампаний для AliExpress. Он включает в себя запуск обработки всех кампаний, а также может быть использован для обработки конкретных кампаний для определенных языков и валют.

## Функции

### `process_campaign`

```python
def process_campaign(campaign_name: str, language: str, currency: str, campaign_file: str | None) -> None:
    """
    Запускает процесс подготовки рекламной кампании.

    Args:
        campaign_name (str): Имя рекламной кампании.
        language (str): Язык кампании.
        currency (str): Валюта кампании.
        campaign_file (str | None): Путь к файлу кампании (если существует).

    Returns:
        None

    Raises:
        Exception: Если возникает ошибка при подготовке кампании.
    """
    ...
```

**Как работает функция**:
1. Функция `process_campaign` принимает параметры рекламной кампании, такие как имя, язык и валюта.
2. Затем вызывается функция, которая подготавливает рекламную кампанию. Если файл кампании не указан, будет создана новая кампания.

**Примеры**:
```python
process_campaign(campaign_name='rc', language='EN', currency='USD', campaign_file=None)
```

### `main_process`

```python
def main_process(param1: str, param2: list[str]) -> None:
    """
    Запускает основной процесс подготовки кампаний для указанных брендов.

    Args:
        param1 (str):  Параметр `param1` (например, 'brands').
        param2 (list[str]): Список брендов для обработки.

    Returns:
        None

    Raises:
        Exception: Если возникает ошибка в процессе подготовки кампаний.
    """
    ...
```

**Как работает функция**:
1. Функция `main_process` принимает строку `param1` и список строк `param2`.
2. Она вызывает функцию `main_process` из модуля `prepare_campaigns`, передавая ей строку 'brands' и список брендов для обработки.

**Примеры**:
```python
main_process('brands', ['mrgreen'])
```

### `process_all_campaigns`

```python
def process_all_campaigns() -> None:
    """
    Запускает процесс подготовки всех рекламных кампаний.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: Если возникает ошибка при подготовке кампаний.
    """
    ...
```

**Как работает функция**:
1. Функция `process_all_campaigns` не принимает аргументов.
2. Она вызывает функцию `process_all_campaigns` из модуля `prepare_campaigns`, которая обрабатывает все рекламные кампании.

**Примеры**:
```python
process_all_campaigns()
```