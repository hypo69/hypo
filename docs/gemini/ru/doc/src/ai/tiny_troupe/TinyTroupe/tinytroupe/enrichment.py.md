# Модуль `enrichment`

## Обзор

Модуль `enrichment` предоставляет класс `TinyEnricher` для обогащения контента с использованием языковых моделей. Он позволяет добавлять контекстную информацию к контенту на основе заданных требований и использовать прошлые результаты в качестве контекста.

## Содержание

- [Классы](#Классы)
  - [`TinyEnricher`](#TinyEnricher)
- [Функции](#Функции)
  - [`enrich_content`](#enrich_content)

## Классы

### `TinyEnricher`

**Описание**: Класс для обогащения контента с использованием языковых моделей.

**Методы**:
- `__init__`: Инициализирует объект `TinyEnricher`.
- `enrich_content`: Обогащает предоставленный контент, используя языковую модель.

#### `__init__`
```python
def __init__(self, use_past_results_in_context=False) -> None:
    """
    Args:
        use_past_results_in_context (bool, optional): Определяет, следует ли использовать прошлые результаты в контексте. По умолчанию `False`.

    Returns:
        None:
    """
```
**Описание**: Инициализирует объект `TinyEnricher`.

**Параметры**:
- `use_past_results_in_context` (bool, optional): Определяет, следует ли использовать прошлые результаты в контексте. По умолчанию `False`.

#### `enrich_content`
```python
def enrich_content(self, requirements: str, content:str, content_type:str =None, context_info:str ="", context_cache:list=None, verbose:bool=False) -> str | None:
    """
    Args:
        requirements (str): Требования к обогащению контента.
        content (str): Контент, который необходимо обогатить.
        content_type (str, optional): Тип контента. По умолчанию `None`.
        context_info (str, optional): Дополнительная контекстная информация. По умолчанию `""`.
        context_cache (list, optional): Кэш контекста. По умолчанию `None`.
        verbose (bool, optional): Флаг для вывода отладочной информации. По умолчанию `False`.

    Returns:
        str | None: Обогащенный контент в виде строки или `None`, если не удалось обогатить.
    """
```
**Описание**: Обогащает предоставленный контент, используя языковую модель.

**Параметры**:
- `requirements` (str): Требования к обогащению контента.
- `content` (str): Контент, который необходимо обогатить.
- `content_type` (str, optional): Тип контента. По умолчанию `None`.
- `context_info` (str, optional): Дополнительная контекстная информация. По умолчанию `""`.
- `context_cache` (list, optional): Кэш контекста. По умолчанию `None`.
- `verbose` (bool, optional): Флаг для вывода отладочной информации. По умолчанию `False`.

**Возвращает**:
- `str | None`: Обогащенный контент в виде строки или `None`, если не удалось обогатить.

## Функции
### `enrich_content`
```python
def enrich_content(self, requirements: str, content:str, content_type:str =None, context_info:str ="", context_cache:list=None, verbose:bool=False) -> str | None:
    """
    Args:
        requirements (str): Требования к обогащению контента.
        content (str): Контент, который необходимо обогатить.
        content_type (str, optional): Тип контента. По умолчанию `None`.
        context_info (str, optional): Дополнительная контекстная информация. По умолчанию `""`.
        context_cache (list, optional): Кэш контекста. По умолчанию `None`.
        verbose (bool, optional): Флаг для вывода отладочной информации. По умолчанию `False`.

    Returns:
        str | None: Обогащенный контент в виде строки или `None`, если не удалось обогатить.
    """
```
**Описание**: Обогащает предоставленный контент, используя языковую модель.

**Параметры**:
- `requirements` (str): Требования к обогащению контента.
- `content` (str): Контент, который необходимо обогатить.
- `content_type` (str, optional): Тип контента. По умолчанию `None`.
- `context_info` (str, optional): Дополнительная контекстная информация. По умолчанию `""`.
- `context_cache` (list, optional): Кэш контекста. По умолчанию `None`.
- `verbose` (bool, optional): Флаг для вывода отладочной информации. По умолчанию `False`.

**Возвращает**:
- `str | None`: Обогащенный контент в виде строки или `None`, если не удалось обогатить.