# Модуль AuxiliaryClasses.py

## Обзор

Модуль `AuxiliaryClasses.py` содержит вспомогательные классы `keyboards` и `PromptsCompressor`, используемые для создания клавиатур и обработки текстовых запросов в Telegram-боте.
Класс `keyboards` предназначен для генерации различных типов клавиатур, а класс `PromptsCompressor` — для сжатия и форматирования текстовых подсказок.

## Подробней

В данном модуле реализованы классы для упрощения создания интерактивных элементов (клавиатур) и обработки текстовых запросов в Telegram-боте.
Класс `keyboards` предоставляет методы для создания различных типов клавиатур, таких как встроенные клавиатуры с двумя полями и клавиатуры ответов.
Класс `PromptsCompressor` используется для сжатия и форматирования текстовых подсказок, а также для вставки HTML-тегов в текстовые ответы.

## Классы

### `keyboards`

**Описание**: Класс `keyboards` предоставляет методы для создания различных типов клавиатур для Telegram-бота.

**Методы**:
- `_keyboard_two_blank`: Создает встроенную клавиатуру с двумя полями.
- `_reply_keyboard`: Создает клавиатуру ответов.

#### `_keyboard_two_blank`

```python
def _keyboard_two_blank(self, data: list[str], name: list[str]) -> types.InlineKeyboardMarkup:
    """
    Args:
        data (list[str]): Список данных для кнопок.
        name (list[str]): Список названий для кнопок.

    Returns:
        types.InlineKeyboardMarkup: Объект встроенной клавиатуры.

    Raises:
        None
    """
```

**Описание**: Создает встроенную клавиатуру с двумя полями.

**Параметры**:
- `data` (list[str]): Список данных, которые будут переданы при нажатии на кнопку.
- `name` (list[str]): Список названий кнопок, отображаемых пользователю.

**Возвращает**:
- `types.InlineKeyboardMarkup`: Объект встроенной клавиатуры, готовый для отправки в Telegram-сообщении.

**Примеры**:
```python
keyboard = keyboards()._keyboard_two_blank(data=['1', '2', '3'], name=['Один', 'Два', 'Три'])
```

#### `_reply_keyboard`

```python
def _reply_keyboard(self, name: list[str]):
    """
    Args:
        name (list[str]): Список названий для кнопок.

    Returns:
        types.ReplyKeyboardMarkup: Объект клавиатуры ответов.

    Raises:
        None
    """
```

**Описание**: Создает клавиатуру ответов (reply keyboard).

**Параметры**:
- `name` (list[str]): Список названий кнопок, отображаемых пользователю.

**Возвращает**:
- `types.ReplyKeyboardMarkup`: Объект клавиатуры ответов, готовый для отправки в Telegram-сообщении.

**Примеры**:
```python
keyboard = keyboards()._reply_keyboard(name=['Да', 'Нет', 'Отмена'])
```

### `PromptsCompressor`

**Описание**: Класс `PromptsCompressor` предназначен для сжатия и форматирования текстовых подсказок, а также для вставки HTML-тегов в текстовые ответы.

**Методы**:
- `__init__`: Инициализирует объект класса, задавая размеры команд.
- `get_prompt`: Получает сжатую подсказку на основе предоставленной информации.
- `html_tags_insert`: Вставляет HTML-теги в текстовый ответ.

#### `__init__`

```python
def __init__(self):
    """
    Args:
        None

    Returns:
        None

    Raises:
        None
    """
```

**Описание**: Инициализирует объект класса `PromptsCompressor`, задавая размеры команд.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Отсутствует.

**Примеры**:
```python
compressor = PromptsCompressor()
```

#### `get_prompt`

```python
def get_prompt(self, info: list[str], ind: int) -> str:
    """
    Args:
        info (list[str]): Список информации для вставки в подсказку.
        ind (int): Индекс команды в списке команд.

    Returns:
        str: Сформированная строка подсказки.

    Raises:
        FileNotFoundError: Если файл 'ToolBox/BaseSettings/prompts.json' не найден.
        KeyError: Если ключ 'commands' или `ind` не найден в JSON-файле.
    """
```

**Описание**: Получает сжатую подсказку на основе предоставленной информации.

**Параметры**:
- `info` (list[str]): Список информации для вставки в подсказку.
- `ind` (int): Индекс команды в списке команд.

**Возвращает**:
- `str`: Сформированная строка подсказки.

**Примеры**:
```python
compressor = PromptsCompressor()
prompt = compressor.get_prompt(info=['Тема', 'Целевая аудитория', 'Длина'], ind=0)
```

#### `html_tags_insert`

```python
@staticmethod
def html_tags_insert(response: str) -> str:
    """
    Args:
        response (str): Текст, в который нужно вставить HTML-теги.

    Returns:
        str: Текст с вставленными HTML-тегами.

    Raises:
        None
    """
```

**Описание**: Вставляет HTML-теги в текстовый ответ.

**Параметры**:
- `response` (str): Текст, в который нужно вставить HTML-теги.

**Возвращает**:
- `str`: Текст с вставленными HTML-тегами.

**Примеры**:
```python
formatted_text = PromptsCompressor.html_tags_insert(response='#### Заголовок \\nТекст **жирный** *наклонный*')
```