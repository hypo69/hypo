# Модуль tinytroupe.enrichment

## Обзор

Этот модуль предоставляет класс `TinyEnricher`, предназначенный для обогащения контента с использованием больших языковых моделей (LLM). Он использует шаблоны Mustache для составления запросов к LLM и парсит полученный ответ для извлечения кода.

## Классы

### `TinyEnricher`

**Описание**: Класс `TinyEnricher` реализует механизм обогащения контента, используя API больших языковых моделей. Он сохраняет контекст для последующих запросов и обрабатывает исключения.

**Конструктор**:

```python
def __init__(self, use_past_results_in_context=False) -> None:
    """
    Инициализирует объект TinyEnricher.

    Args:
        use_past_results_in_context (bool, optional): Флаг, определяющий использование предыдущих результатов в контексте. По умолчанию False.
    """
```

**Методы**:

#### `enrich_content`

```python
def enrich_content(self, requirements: str, content: str, content_type: str = None, context_info: str = "", context_cache: list = None, verbose: bool = False) -> dict | None:
    """
    Обогащает контент с помощью больших языковых моделей.

    Args:
        requirements (str): Требования к обогащению контента.
        content (str): Контент, который необходимо обогатить.
        content_type (str, optional): Тип контента. По умолчанию None.
        context_info (str, optional): Дополнительная контекстная информация. По умолчанию "".
        context_cache (list, optional): Кэш контекста. По умолчанию None.
        verbose (bool, optional): Флаг для вывода дополнительной информации. По умолчанию False.

    Returns:
        dict | None: Результат обогащения контента в виде словаря или None, если запрос не удался.

    Raises:
        Exception: Общее исключение в случае ошибки во взаимодействии с LLM.
    """
```


## Функции

(Нет функций в этом модуле)


## Модули, импортированные в этом файле

- `os`
- `json`
- `chevron`
- `logging`
- `pandas` as `pd`
- `tinytroupe.agent`
- `tinytroupe.environment`
- `tinytroupe.factory`
- `tinytroupe.utils`
- `JsonSerializableRegistry`
- `openai_utils`
- `tinytroupe.utils` as `utils`



## Обработка исключений

В методе `enrich_content` и других методах, использующих внешние ресурсы (например, API LLM), необходимо учитывать возможные исключения (например, проблемы с подключением, ошибки в ответе API и т.д.).  Для этого используется обработка исключений с использованием `try...except` блоков.  Пример обработки исключений, который следует использовать в данном модуле:

```python
try:
    # Код, который может вызвать исключение
    result = openai_utils.client().send_message(...)
except Exception as ex:
    logger.error(f"Ошибка при взаимодействии с LLM: {ex}")
    return None
```