# Модуль AuxiliaryClasses.py

## Обзор

Модуль содержит вспомогательные классы для работы с Telegram ботом, такие как `keyboards` для создания клавиатур и `PromptsCompressor` для обработки и форматирования текстовых запросов.

## Подробней

Модуль `AuxiliaryClasses.py` предоставляет классы для упрощения создания пользовательских интерфейсов и обработки текстовых запросов в Telegram боте. Класс `keyboards` содержит методы для создания различных типов клавиатур, а класс `PromptsCompressor` предназначен для сжатия и форматирования текстовых запросов с использованием предопределенных шаблонов.

## Классы

### `keyboards`

**Описание**: Класс для создания различных типов клавиатур Telegram бота.

**Методы**:
- `_keyboard_two_blank`: Создает inline-клавиатуру с кнопками в два столбца.
- `_reply_keyboard`: Создает reply-клавиатуру.

#### `_keyboard_two_blank`

```python
def _keyboard_two_blank(self, data: list[str], name: list[str]) -> types.InlineKeyboardMarkup:
    """
    Args:
        data (list[str]): Список данных для callback_data кнопок.
        name (list[str]): Список отображаемых имен кнопок.

    Returns:
        types.InlineKeyboardMarkup: Объект inline-клавиатуры.
    """
```

**Описание**: Создает inline-клавиатуру с кнопками, расположенными в два столбца.

**Параметры**:
- `data` (list[str]): Список данных, которые будут переданы в качестве `callback_data` для каждой кнопки.
- `name` (list[str]): Список имен, отображаемых на кнопках.

**Возвращает**:
- `types.InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup`, представляющий созданную клавиатуру.

**Примеры**:

```python
# Пример создания inline-клавиатуры
keyboard = keyboards()._keyboard_two_blank(data=['1', '2', '3'], name=['Один', 'Два', 'Три'])
```

#### `_reply_keyboard`

```python
def _reply_keyboard(self, name: list[str]):
    """
    Args:
        name (list[str]): Список имен кнопок.

    Returns:
        types.ReplyKeyboardMarkup: Объект reply-клавиатуры.
    """
```

**Описание**: Создает reply-клавиатуру с кнопками на основе предоставленного списка имен.

**Параметры**:
- `name` (list[str]): Список имен, отображаемых на кнопках.

**Возвращает**:
- `types.ReplyKeyboardMarkup`: Объект `ReplyKeyboardMarkup`, представляющий созданную клавиатуру.

**Примеры**:

```python
# Пример создания reply-клавиатуры
keyboard = keyboards()._reply_keyboard(name=['Один', 'Два', 'Три'])
```

### `PromptsCompressor`

**Описание**: Класс для сжатия и форматирования текстовых запросов с использованием предопределенных шаблонов.

**Методы**:
- `__init__`: Инициализирует объект `PromptsCompressor`, загружая размеры команд.
- `get_prompt`: Получает и форматирует текстовый запрос на основе предоставленной информации и индекса.
- `html_tags_insert`: Вставляет HTML-теги в текстовый ответ для форматирования.

#### `__init__`

```python
def __init__(self):
    """
    """
```

**Описание**: Инициализирует объект `PromptsCompressor` и определяет размеры команд.

**Примеры**:

```python
# Пример инициализации объекта PromptsCompressor
compressor = PromptsCompressor()
```

#### `get_prompt`

```python
def get_prompt(self, info: list[str], ind: int) -> str:
    """
    Args:
        info (list[str]): Список информации для вставки в шаблон запроса.
        ind (int): Индекс шаблона запроса.

    Returns:
        str: Сформированный текстовый запрос.
    """
```

**Описание**: Получает и форматирует текстовый запрос на основе предоставленной информации и индекса шаблона.

**Параметры**:
- `info` (list[str]): Список информации для вставки в шаблон запроса.
- `ind` (int): Индекс шаблона запроса, используемого для форматирования.

**Возвращает**:
- `str`: Сформированный текстовый запрос.

**Примеры**:

```python
# Пример получения и форматирования текстового запроса
compressor = PromptsCompressor()
prompt = compressor.get_prompt(info=['topic', 'TA', 'tone', 'struct', 'length', 'extra'], ind=0)
```

#### `html_tags_insert`

```python
@staticmethod
def html_tags_insert(response: str) -> str:
    """
    Args:
        response (str): Текст ответа для вставки HTML-тегов.

    Returns:
        str: Отформатированный текст с HTML-тегами.
    """
```

**Описание**: Вставляет HTML-теги в текстовый ответ для форматирования.

**Параметры**:
- `response` (str): Текст ответа, в который необходимо вставить HTML-теги.

**Возвращает**:
- `str`: Отформатированный текст с HTML-тегами.

**Примеры**:

```python
# Пример вставки HTML-тегов в текст ответа
formatted_text = PromptsCompressor.html_tags_insert(response='#### Заголовок\nТекст')
```