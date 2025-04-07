# Модуль для рендеринга и разметки в Tiny Troupe
=================================================

Модуль предоставляет утилиты для обработки текста, стилизации и форматирования, используемые для рендеринга контента в проекте Tiny Troupe. Включает функции для инъекции стилей, обрезки текста, форматирования дат и времени, а также управления стилями текста.

## Обзор

Модуль содержит функции и класс `RichTextStyle`, которые используются для стилизации текста и форматирования данных, предназначенных для отображения в интерфейсе пользователя или логах. Функции модуля позволяют добавлять CSS стили, обрезать длинные строки, форматировать даты и удалять лишние пробелы.

## Подробнее

Этот модуль предоставляет набор инструментов для улучшения читаемости и представления текста и данных. Он включает методы для динамического изменения стилей HTML, обрезки длинных текстов, форматирования дат и управления стилями для консольного вывода с использованием библиотеки `rich`.

## Функции

### `inject_html_css_style_prefix`

```python
def inject_html_css_style_prefix(html, style_prefix_attributes):
    """
    Injects a style prefix to all style attributes in the given HTML string.

    For example, if you want to add a style prefix to all style attributes in the HTML string
    ``<div style="color: red;">Hello</div>``, you can use this function as follows:
    inject_html_css_style_prefix(\'<div style="color: red;">Hello</div>\', \'font-size: 20px;\')
    """
    ...
```

**Назначение**: Добавляет префикс стиля ко всем атрибутам `style` в переданной HTML строке.

**Параметры**:
- `html`: HTML строка, в которой необходимо добавить префикс к стилям.
- `style_prefix_attributes`: Строка с префиксом стилей, которую нужно добавить.

**Возвращает**:
- HTML строка с добавленным префиксом стилей.

**Как работает функция**:
1. Функция берет входную HTML строку и строку с префиксом стилей.
2. Использует метод `replace` для поиска всех вхождений `style="` и заменяет их на `style="{style_prefix_attributes};`, добавляя указанный префикс.
3. Возвращает измененную HTML строку.

```
HTML_String --> Replace 'style="' with 'style="{style_prefix_attributes};' --> Измененная_HTML_Строка
```

**Примеры**:

```python
html = '<div style="color: red;">Hello</div>'
style_prefix = 'font-size: 20px'
result = inject_html_css_style_prefix(html, style_prefix)
print(result) # Вывод: <div style="font-size: 20px;color: red;">Hello</div>
```

### `break_text_at_length`

```python
def break_text_at_length(text: Union[str, dict], max_length: int=None) -> str:
    """
    Breaks the text (or JSON) at the specified length, inserting a "(...)" string at the break point.
    If the maximum length is `None`, the content is returned as is.
    """
    ...
```

**Назначение**: Обрезает текст или JSON до указанной длины, добавляя строку "(...)" в точке обрыва.

**Параметры**:
- `text` (str | dict): Текст или словарь, который нужно обрезать.
- `max_length` (int, optional): Максимальная длина текста. Если `None`, текст не обрезается. По умолчанию `None`.

**Возвращает**:
- Обрезанная строка с добавленным "(...)" или исходный текст, если `max_length` равен `None` или длина текста меньше `max_length`.

**Как работает функция**:
1. Функция проверяет, является ли входной параметр словарем. Если да, преобразует его в JSON строку с отступами.
2. Проверяет, равен ли `max_length` `None` или длина текста меньше или равна `max_length`. Если да, возвращает текст без изменений.
3. Иначе, обрезает текст до `max_length` символов и добавляет в конце строку "(...)".

```
Text --> Is_Dictionary? --> Yes: Convert_to_JSON
|       No: -
|
Check max_length --> None or len(text) <= max_length? --> Yes: Return Text
|                                                     No: обрезанный_текст + " (...)"
```

**Примеры**:

```python
text = "This is a long text that needs to be broken."
result = break_text_at_length(text, max_length=20)
print(result)  # Вывод: This is a long text (...)

data = {"key": "value", "another_key": "another_value"}
result = break_text_at_length(data, max_length=30)
print(result)
```

### `pretty_datetime`

```python
def pretty_datetime(dt: datetime) -> str:
    """
    Returns a pretty string representation of the specified datetime object.
    """
    ...
```

**Назначение**: Преобразует объект `datetime` в строку в формате "YYYY-MM-DD HH:MM".

**Параметры**:
- `dt` (datetime): Объект `datetime`, который нужно отформатировать.

**Возвращает**:
- Строковое представление даты и времени в формате "YYYY-MM-DD HH:MM".

**Как работает функция**:
1. Функция принимает объект `datetime`.
2. Использует метод `strftime` для форматирования даты и времени в указанный формат.
3. Возвращает отформатированную строку.

```
Datetime_Object --> strftime("%Y-%m-%d %H:%M") --> Отформатированная_Строка
```

**Примеры**:

```python
from datetime import datetime

dt = datetime(2023, 1, 1, 12, 30)
result = pretty_datetime(dt)
print(result)  # Вывод: 2023-01-01 12:30
```

### `dedent`

```python
def dedent(text: str) -> str:
    """
    Dedents the specified text, removing any leading whitespace and identation.
    """
    ...
```

**Назначение**: Удаляет общие начальные пробелы из каждой строки текста.

**Параметры**:
- `text` (str): Текст, из которого нужно удалить отступы.

**Возвращает**:
- Текст без начальных пробелов и отступов.

**Как работает функция**:
1. Функция принимает строку текста.
2. Использует `textwrap.dedent` для удаления общих начальных пробелов.
3. Использует `strip()` для удаления всех начальных и конечных пробелов.
4. Возвращает обработанный текст.

```
Текст --> textwrap.dedent() --> strip() --> Текст_Без_Отступов
```

**Примеры**:

```python
text = "   Hello\n    World"
result = dedent(text)
print(result)  # Вывод: Hello\nWorld
```

### `wrap_text`

```python
def wrap_text(text: str, width: int=100) -> str:
    """
    Wraps the text at the specified width.
    """
    ...
```

**Назначение**: Переносит текст на новую строку, если он превышает указанную ширину.

**Параметры**:
- `text` (str): Текст, который нужно перенести.
- `width` (int, optional): Максимальная ширина строки. По умолчанию 100.

**Возвращает**:
- Текст, перенесенный на новые строки в соответствии с заданной шириной.

**Как работает функция**:
1. Функция принимает строку текста и ширину.
2. Использует `textwrap.fill` для переноса текста на новые строки с учетом заданной ширины.
3. Возвращает переформатированный текст.

```
Текст, Ширина --> textwrap.fill(text, width=width) --> Переформатированный_Текст
```

**Примеры**:

```python
text = "This is a long text that needs to be wrapped."
result = wrap_text(text, width=20)
print(result)
```

## Классы

### `RichTextStyle`

**Описание**: Класс, определяющий стили текста для использования с библиотекой `rich`.

**Атрибуты**:
- `STIMULUS_CONVERSATION_STYLE` (str): Стиль для текста стимула в контексте разговора (bold italic cyan1).
- `STIMULUS_THOUGHT_STYLE` (str): Стиль для текста стимула, представляющего мысль (dim italic cyan1).
- `STIMULUS_DEFAULT_STYLE` (str): Стиль для текста стимула по умолчанию (italic).
- `ACTION_DONE_STYLE` (str): Стиль для текста действия, которое завершено (grey82).
- `ACTION_TALK_STYLE` (str): Стиль для текста действия, представляющего речь (bold green3).
- `ACTION_THINK_STYLE` (str): Стиль для текста действия, представляющего мысль (green).
- `ACTION_DEFAULT_STYLE` (str): Стиль для текста действия по умолчанию (purple).
- `INTERVENTION_DEFAULT_STYLE` (str): Стиль для текста интервенции по умолчанию (bright_magenta).

**Методы**:
- `get_style_for(kind: str, event_type: str = None)`: Возвращает стиль для указанного типа события и категории.

#### `get_style_for`

```python
@classmethod
def get_style_for(cls, kind:str, event_type:str=None):
    """
    Возвращает стиль для указанного типа события и категории.
    """
    ...
```

**Назначение**: Определяет и возвращает стиль текста на основе типа события и категории (stimulus, action, intervention).

**Параметры**:
- `kind` (str): Тип категории ("stimulus", "action", "intervention").
- `event_type` (str, optional): Тип события ("CONVERSATION", "THOUGHT", "DONE", "TALK", "THINK"). По умолчанию `None`.

**Возвращает**:
- Строка, представляющая стиль текста.

**Как работает функция**:
1. Принимает тип категории (`kind`) и тип события (`event_type`).
2. Если `kind` равен "stimulus" или "stimuli":
   - Если `event_type` равен "CONVERSATION", возвращает `STIMULUS_CONVERSATION_STYLE`.
   - Если `event_type` равен "THOUGHT", возвращает `STIMULUS_THOUGHT_STYLE`.
   - Иначе возвращает `STIMULUS_DEFAULT_STYLE`.
3. Если `kind` равен "action":
   - Если `event_type` равен "DONE", возвращает `ACTION_DONE_STYLE`.
   - Если `event_type` равен "TALK", возвращает `ACTION_TALK_STYLE`.
   - Если `event_type` равен "THINK", возвращает `ACTION_THINK_STYLE`.
   - Иначе возвращает `ACTION_DEFAULT_STYLE`.
4. Если `kind` равен "intervention", возвращает `INTERVENTION_DEFAULT_STYLE`.

```
Kind, Event_Type --> Kind == "stimulus" or "stimuli"? --> Yes: Event_Type == "CONVERSATION"? --> Yes: STIMULUS_CONVERSATION_STYLE
|                                                         No: Event_Type == "THOUGHT"? --> Yes: STIMULUS_THOUGHT_STYLE
|                                                         No: STIMULUS_DEFAULT_STYLE
|                   No: Kind == "action"? --> Yes: Event_Type == "DONE"? --> Yes: ACTION_DONE_STYLE
|                                          No: Event_Type == "TALK"? --> Yes: ACTION_TALK_STYLE
|                                          No: Event_Type == "THINK"? --> Yes: ACTION_THINK_STYLE
|                                          No: ACTION_DEFAULT_STYLE
|                   No: Kind == "intervention"? --> Yes: INTERVENTION_DEFAULT_STYLE
```

**Примеры**:

```python
style = RichTextStyle.get_style_for("stimulus", "CONVERSATION")
print(style)  # Вывод: bold italic cyan1

style = RichTextStyle.get_style_for("action", "TALK")
print(style)  # Вывод: bold green3
```