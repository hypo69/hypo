# Модуль `tiny_word_processor.py`

## Обзор

Модуль `tiny_word_processor.py` предоставляет класс `TinyWordProcessor`, который является инструментом для создания и обработки текстовых документов. Он позволяет агентам (agents) писать документы, обогащать их контент и экспортировать в различные форматы (Markdown, DOCX, JSON).

## Подробней

Модуль предназначен для использования в системе, где требуется автоматизированное создание документов с возможностью расширения контента и экспорта в разные форматы. Класс `TinyWordProcessor` наследуется от `TinyTool` и интегрируется с другими инструментами, такими как `enricher` (для обогащения контента) и `exporter` (для экспорта документов).

## Классы

### `TinyWordProcessor`

**Описание**: Класс `TinyWordProcessor` предоставляет функциональность для создания, обогащения и экспорта текстовых документов.

**Наследует**:
- `TinyTool`: Класс `TinyWordProcessor` наследует от `TinyTool`, что позволяет интегрировать его в систему инструментов `tinytroupe`.

**Атрибуты**:
- `owner` (Any): Владелец инструмента.
- `exporter` (Any): Инструмент для экспорта документов.
- `enricher` (Any): Инструмент для обогащения контента документов.

**Методы**:
- `__init__(self, owner=None, exporter=None, enricher=None)`: Инициализирует экземпляр класса `TinyWordProcessor`.
- `write_document(self, title, content, author=None)`: Создает и экспортирует документ с заданным заголовком, контентом и автором.
- `_process_action(self, agent, action) -> bool`: Обрабатывает действие агента, создавая новый документ, если действие имеет тип "WRITE_DOCUMENT".
- `actions_definitions_prompt(self) -> str`: Возвращает строку с описанием возможных действий, которые может выполнять инструмент.
- `actions_constraints_prompt(self) -> str`: Возвращает строку с описанием ограничений на действия, выполняемые инструментом.

### `__init__(self, owner=None, exporter=None, enricher=None)`

```python
def __init__(self, owner=None, exporter=None, enricher=None):
    """
    Инициализирует экземпляр класса `TinyWordProcessor`.

    Args:
        owner (Any, optional): Владелец инструмента. По умолчанию `None`.
        exporter (Any, optional): Инструмент для экспорта документов. По умолчанию `None`.
        enricher (Any, optional): Инструмент для обогащения контента документов. По умолчанию `None`.
    """
    ...
```

### `write_document(self, title, content, author=None)`

```python
def write_document(self, title, content, author=None):
    """
    Создает и экспортирует документ с заданным заголовком, контентом и автором.

    Args:
        title (str): Заголовок документа.
        content (str): Содержание документа.
        author (str, optional): Автор документа. По умолчанию `None`.
    """
    ...
```

### `_process_action(self, agent, action) -> bool`

```python
def _process_action(self, agent, action) -> bool:
    """
    Обрабатывает действие агента, создавая новый документ, если действие имеет тип "WRITE_DOCUMENT".

    Args:
        agent (Any): Агент, выполняющий действие.
        action (dict): Словарь с информацией о действии.

    Returns:
        bool: `True`, если действие было успешно обработано, иначе `False`.
    """
    ...
```

### `actions_definitions_prompt(self) -> str`

```python
def actions_definitions_prompt(self) -> str:
    """
    Возвращает строку с описанием возможных действий, которые может выполнять инструмент.

    Returns:
        str: Строка с описанием действий.
    """
    ...
```

### `actions_constraints_prompt(self) -> str`

```python
def actions_constraints_prompt(self) -> str:
    """
    Возвращает строку с описанием ограничений на действия, выполняемые инструментом.

    Returns:
        str: Строка с описанием ограничений.
    """
    ...
```

## Функции

### `write_document`

**Назначение**: Создает и экспортирует документ с заданным заголовком, контентом и автором. Если указан `enricher`, контент документа обогащается. Документ экспортируется в форматы Markdown, DOCX и JSON.

**Параметры**:
- `title` (str): Заголовок документа.
- `content` (str): Содержание документа.
- `author` (str, optional): Автор документа. По умолчанию `None`.

**Возвращает**:
- `None`: Функция ничего не возвращает явно.

**Вызывает исключения**:
- Отсутствуют явные исключения в коде функции, но исключения могут быть вызваны методами `enricher.enrich_content` и `exporter.export`.

**Как работает функция**:

1. Логирует информацию о создании документа с указанным заголовком и контентом.
2. Если `enricher` определен, обогащает контент документа, используя `self.enricher.enrich_content`.
3. Если `exporter` определен, экспортирует документ в форматы Markdown, DOCX и JSON, используя `self.exporter.export`.

```
Начало
│
├── Логирование информации о создании документа
│
├── Проверка наличия `enricher`
│   └───> Если `enricher` есть: Обогащение контента документа
│
├── Проверка наличия `exporter`
│   └───> Если `exporter` есть: Экспорт документа в Markdown, DOCX и JSON
│
Конец
```

**Примеры**:

```python
# Пример создания документа без автора
word_processor.write_document(title="Пример документа", content="Это пример контента.")

# Пример создания документа с автором
word_processor.write_document(title="Пример документа с автором", content="Это пример контента.", author="Иванов")
```

### `_process_action`

**Назначение**: Обрабатывает действие агента, проверяя, является ли действие созданием документа (`WRITE_DOCUMENT`). Если да, извлекает параметры документа из контента действия и вызывает метод `write_document` для создания документа.

**Параметры**:
- `agent` (Any): Агент, выполняющий действие.
- `action` (dict): Словарь с информацией о действии.

**Возвращает**:
- `bool`: `True`, если действие было успешно обработано, иначе `False`.

**Вызывает исключения**:
- `json.JSONDecodeError`: Если не удается распарсить JSON контент действия.
- `Exception`: При возникновении других ошибок во время обработки действия.

**Как работает функция**:

1. Проверяет, является ли тип действия `WRITE_DOCUMENT` и не является ли контент действия `None`.
2. Пытается распарсить контент действия как JSON. Если контент уже является словарем, использует его напрямую.
3. Проверяет наличие недопустимых ключей в спецификации документа (`doc_spec`).
4. Вызывает метод `write_document` с параметрами, извлеченными из `doc_spec`.
5. В случае ошибок логирует информацию об ошибке и возвращает `False`.

```
Начало
│
├── Проверка типа действия и наличия контента
│   └───> Если тип действия `WRITE_DOCUMENT` и контент не `None`:
│       │
│       ├── Парсинг контента действия как JSON
│       │   └───> Если контент - строка: Извлечение JSON из строки
│       │   └───> Если контент - словарь: Использование словаря напрямую
│       │
│       ├── Проверка наличия недопустимых ключей
│       │
│       ├── Вызов `write_document` с параметрами из `doc_spec`
│       │
│       └── Возврат `True`
│
└── Возврат `False` (если тип действия не `WRITE_DOCUMENT` или контент `None`)
│
Обработка ошибок:
│
├── `json.JSONDecodeError`: Логирование ошибки парсинга JSON и возврат `False`
│
└── `Exception`: Логирование общей ошибки и возврат `False`
│
Конец
```

**Примеры**:

```python
# Пример успешной обработки действия
action = {"type": "WRITE_DOCUMENT", "content": '{"title": "Пример", "content": "Текст"}'}
result = word_processor._process_action(agent, action)
print(result)  # Вывод: True

# Пример неуспешной обработки действия из-за ошибки JSON
action = {"type": "WRITE_DOCUMENT", "content": '{"title": "Пример", "content": "Текст"'}  # Ошибка в JSON
result = word_processor._process_action(agent, action)
print(result)  # Вывод: False
```

### `actions_definitions_prompt`

**Назначение**: Возвращает строку с описанием возможных действий, которые может выполнять инструмент. В данном случае, описывает действие `WRITE_DOCUMENT` и его параметры (title, content, author).

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `str`: Строка с описанием действия `WRITE_DOCUMENT` и его параметров.

**Как работает функция**:

1. Определяет строку `prompt` с описанием действия `WRITE_DOCUMENT` и его параметров (title, content, author).
2. Удаляет лишние отступы из строки `prompt` с помощью `utils.dedent`.
3. Возвращает полученную строку.

```
Начало
│
├── Определение строки с описанием действия `WRITE_DOCUMENT`
│
├── Удаление лишних отступов из строки
│
└── Возврат строки с описанием действия
│
Конец
```

**Примеры**:

```python
# Пример вызова функции
prompt = word_processor.actions_definitions_prompt()
print(prompt)
# Вывод:
# - WRITE_DOCUMENT: you can create a new document. The content of the document has many fields, and you **must** use a JSON format to specify them. Here are the possible fields:
#     * title: The title of the document. Mandatory.
#     * content: The actual content of the document. You **must** use Markdown to format this content. Mandatory.
#     * author: The author of the document. You should put your own name. Optional.
```

### `actions_constraints_prompt`

**Назначение**: Возвращает строку с описанием ограничений на действия, выполняемые инструментом. В данном случае, описывает ограничения на действие `WRITE_DOCUMENT`, такие как обязательное использование JSON формата, необходимость длинного и подробного контента, и дополнительные рекомендации по форматированию контента.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `str`: Строка с описанием ограничений на действие `WRITE_DOCUMENT`.

**Как работает функция**:

1. Определяет строку `prompt` с описанием ограничений на действие `WRITE_DOCUMENT`.
2. Удаляет лишние отступы из строки `prompt` с помощью `utils.dedent`.
3. Возвращает полученную строку.

```
Начало
│
├── Определение строки с описанием ограничений на действие `WRITE_DOCUMENT`
│
├── Удаление лишних отступов из строки
│
└── Возврат строки с описанием ограничений
│
Конец
```

**Примеры**:

```python
# Пример вызова функции
prompt = word_processor.actions_constraints_prompt()
print(prompt)
# Вывод:
# - Whenever you WRITE_DOCUMENT, you write all the content at once. Moreover, the content should be long and detailed, unless there's a good reason for it not to be.
# - Whenever you WRITE_DOCUMENT, you **must** embed the content in a JSON object. Use only valid escape sequences in the JSON content.
# - When you WRITE_DOCUMENT, you follow these additional guidelines:
#     * For any milestones or timelines mentioned, try mentioning specific owners or partner teams, unless there's a good reason not to do so.