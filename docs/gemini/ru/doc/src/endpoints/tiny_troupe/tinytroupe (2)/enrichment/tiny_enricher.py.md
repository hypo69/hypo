# Модуль tiny_enricher.py

## Обзор

Модуль `tiny_enricher.py` предназначен для обогащения контента с использованием моделей обработки естественного языка (LLM). Он содержит класс `TinyEnricher`, который позволяет на основе заданных требований и контекстной информации генерировать обогащенный контент.

## Подробней

Этот модуль является частью системы `tinytroupe` и используется для улучшения качества и релевантности контента. Класс `TinyEnricher` применяет шаблоны Mustache для формирования запросов к LLM и извлекает результаты из ответов.

## Классы

### `TinyEnricher`

**Описание**: Класс для обогащения контента с использованием моделей обработки естественного языка.

**Принцип работы**: Класс инициализируется с возможностью использования предыдущих результатов в контексте. Метод `enrich_content` формирует запросы к LLM на основе шаблонов и извлекает обогащенный контент из ответов модели.

**Аттрибуты**:

- `use_past_results_in_context` (bool): Флаг, определяющий, использовать ли предыдущие результаты в контексте. По умолчанию `False`.
- `context_cache` (list): Список для хранения контекстной информации.

**Методы**:

- `__init__(self, use_past_results_in_context: bool = False) -> None`: Инициализирует экземпляр класса `TinyEnricher`.
- `enrich_content(self, requirements: str, content: str, content_type: str = None, context_info: str = "", context_cache: list = None, verbose: bool = False)`: Обогащает контент на основе заданных требований и контекстной информации.

## Функции

### `__init__`

```python
def __init__(self, use_past_results_in_context: bool = False) -> None:
    """
    Инициализирует экземпляр класса `TinyEnricher`.

    Args:
        use_past_results_in_context (bool, optional): Флаг, определяющий, использовать ли предыдущие результаты в контексте. По умолчанию `False`.

    Returns:
        None
    """
    ...
```

**Назначение**: Инициализация экземпляра класса `TinyEnricher`. Устанавливает флаг `use_past_results_in_context` и инициализирует пустой список `context_cache`.

**Параметры**:

- `use_past_results_in_context` (bool): Флаг, определяющий, следует ли использовать предыдущие результаты в контексте при обогащении контента. По умолчанию установлено значение `False`.

**Возвращает**:

- `None`

**Как работает функция**:
1. Функция принимает параметр `use_past_results_in_context`, который определяет, будет ли использоваться контекст из предыдущих результатов.
2.  Инициализирует атрибут `use_past_results_in_context` значением переданного параметра.
3.  Инициализирует атрибут `context_cache` пустым списком, который будет использоваться для хранения контекстной информации.

```
Инициализация TinyEnricher
│
├── use_past_results_in_context (bool)
│   │
│   └── Установка значения атрибута self.use_past_results_in_context
│
└── Инициализация self.context_cache = []
```

**Примеры**:

```python
enricher = TinyEnricher()
enricher = TinyEnricher(use_past_results_in_context=True)
```

### `enrich_content`

```python
def enrich_content(self, requirements: str, content: str, content_type: str = None, context_info: str = "", context_cache: list = None, verbose: bool = False):
    """
    Обогащает контент на основе заданных требований и контекстной информации.

    Args:
        requirements (str): Требования к обогащению контента.
        content (str): Контент, который необходимо обогатить.
        content_type (str, optional): Тип контента. По умолчанию `None`.
        context_info (str, optional): Дополнительная контекстная информация. По умолчанию "".
        context_cache (list, optional): Список с контекстной информацией. По умолчанию `None`.
        verbose (bool, optional): Флаг для вывода отладочной информации. По умолчанию `False`.

    Returns:
        str | None: Обогащенный контент или `None`, если обогащение не удалось.
    """
    ...
```

**Назначение**: Обогащение предоставленного контента на основе заданных требований, типа контента и контекстной информации с использованием LLM.

**Параметры**:

- `requirements` (str): Описание требований к обогащению контента.
- `content` (str): Контент, который необходимо обогатить.
- `content_type` (str, optional): Тип контента (например, "текст", "HTML"). По умолчанию `None`.
- `context_info` (str, optional): Дополнительная контекстная информация, используемая для обогащения. По умолчанию "".
- `context_cache` (list, optional): Список с контекстной информацией, который может использоваться для обогащения контента. По умолчанию `None`.
- `verbose` (bool, optional): Флаг для включения или отключения подробного вывода отладочной информации. По умолчанию `False`.

**Возвращает**:

- `str | None`: Обогащенный контент в виде строки или `None`, если не удалось получить результат.

**Как работает функция**:

1.  Формирует словарь `rendering_configs`, содержащий все входные параметры, необходимые для шаблонов Mustache.
2.  Использует функцию `utils.compose_initial_LLM_messages_with_templates` для создания сообщений для LLM на основе шаблонов "enricher.system.mustache" и "enricher.user.mustache". Эти шаблоны определяют системные инструкции и пользовательские запросы для LLM.
3.  Отправляет сообщение в LLM, используя `openai_utils.client().send_message` с параметрами температуры, штрафов за частоту и присутствие.
4.  Извлекает обогащенный контент из ответа LLM с помощью функции `utils.extract_code_block`.
5.  Логирует и, если `verbose` установлен в `True`, выводит отладочное сообщение.

```
enrich_content
│
├── Формирование rendering_configs
│   │
│   ├── requirements (str)
│   ├── content (str)
│   ├── content_type (str)
│   ├── context_info (str)
│   └── context_cache (list)
│
├── Создание сообщений для LLM
│   │
│   └── utils.compose_initial_LLM_messages_with_templates
│
├── Отправка сообщения в LLM
│   │
│   └── openai_utils.client().send_message
│
├── Извлечение обогащенного контента
│   │
│   └── utils.extract_code_block
│
└── Логирование результата
```

**Примеры**:

```python
enricher = TinyEnricher()
requirements = "Добавить ключевые слова"
content = "Текст для обогащения"
enriched_content = enricher.enrich_content(requirements, content)
if enriched_content:
    print(f"Обогащенный контент: {enriched_content}")
else:
    print("Не удалось обогатить контент")