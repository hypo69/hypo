# Модуль `enrichment`

## Обзор

Модуль `enrichment.py` предоставляет класс `TinyEnricher` для обогащения контента с использованием языковых моделей. Он использует шаблоны для формирования запросов к модели и обрабатывает результаты, извлекая из них необходимую информацию.

## Содержание

1.  [Класс `TinyEnricher`](#класс-tinyenricher)
    *   [Метод `__init__`](#метод-__init__)
    *   [Метод `enrich_content`](#метод-enrich_content)

## Классы

### `TinyEnricher`

**Описание**: Класс для обогащения контента с использованием языковых моделей.

**Методы**:
*   [`__init__`](#__init__): Инициализирует экземпляр `TinyEnricher`.
*   [`enrich_content`](#enrich_content): Обогащает контент с использованием языковой модели.

#### `__init__`

```python
def __init__(self, use_past_results_in_context=False) -> None:
    """
    Args:
        use_past_results_in_context (bool, optional): Флаг, определяющий, использовать ли прошлые результаты в контексте. По умолчанию `False`.

    Returns:
        None: Метод ничего не возвращает.

    """
```

**Описание**: Инициализирует экземпляр `TinyEnricher`.

**Параметры**:

*   `use_past_results_in_context` (bool, optional): Флаг, определяющий, использовать ли прошлые результаты в контексте. По умолчанию `False`.

**Возвращает**:
    
    None: Метод ничего не возвращает.

#### `enrich_content`

```python
def enrich_content(self, requirements: str, content: str, content_type: str = None, context_info: str = "", context_cache: list = None, verbose: bool = False) -> str | None:
    """
    Args:
        requirements (str): Требования к обогащению контента.
        content (str): Контент для обогащения.
        content_type (Optional[str], optional): Тип контента. По умолчанию `None`.
        context_info (str, optional): Дополнительная информация о контексте. По умолчанию `""`.
        context_cache (Optional[list], optional): Кэш контекста. По умолчанию `None`.
        verbose (bool, optional): Флаг для вывода отладочной информации. По умолчанию `False`.

    Returns:
         str | None: Обогащенный контент в виде строки или `None`, если обогащение не удалось.
    """
```

**Описание**: Обогащает контент, используя языковую модель.

**Параметры**:
*   `requirements` (str): Требования к обогащению контента.
*   `content` (str): Контент для обогащения.
*   `content_type` (Optional[str], optional): Тип контента. По умолчанию `None`.
*   `context_info` (str, optional): Дополнительная информация о контексте. По умолчанию `""`.
*   `context_cache` (Optional[list], optional): Кэш контекста. По умолчанию `None`.
*   `verbose` (bool, optional): Флаг для вывода отладочной информации. По умолчанию `False`.

**Возвращает**:
*   `str | None`: Обогащенный контент в виде строки или `None`, если обогащение не удалось.