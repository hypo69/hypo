# Модуль `AuxiliaryClasses`

## Обзор

Модуль `AuxiliaryClasses.py` содержит вспомогательные классы для работы с Telegram-ботом. Он включает в себя класс `keyboards` для создания клавиатур и класс `PromptsCompressor` для обработки и формирования текстовых подсказок.

## Содержание

- [Классы](#классы)
    - [`keyboards`](#keyboards)
    - [`PromptsCompressor`](#promptscompressor)

## Классы

### `keyboards`

**Описание**: Класс `keyboards` предназначен для создания различных типов клавиатур, используемых в Telegram-боте.

**Методы**:

- `_keyboard_two_blank(self, data: list[str], name: list[str]) -> types.InlineKeyboardMarkup`
- `_reply_keyboard(self, name: list[str]) -> types.ReplyKeyboardMarkup`

#### `_keyboard_two_blank`

**Описание**: Создает инлайн-клавиатуру с двумя кнопками в строке.

**Параметры**:
- `data` (list[str]): Список callback-данных для каждой кнопки.
- `name` (list[str]): Список названий для каждой кнопки.

**Возвращает**:
- `types.InlineKeyboardMarkup`: Объект инлайн-клавиатуры.

#### `_reply_keyboard`

**Описание**: Создает обычную клавиатуру (reply keyboard) с кнопками.

**Параметры**:
- `name` (list[str]): Список названий для каждой кнопки.

**Возвращает**:
- `types.ReplyKeyboardMarkup`: Объект reply-клавиатуры.

### `PromptsCompressor`

**Описание**: Класс `PromptsCompressor` предназначен для обработки и формирования текстовых подсказок.

**Методы**:

- `__init__(self)`
- `get_prompt(self, info: list[str], ind: int) -> str`
- `html_tags_insert(response: str) -> str`

#### `__init__`

**Описание**: Инициализирует экземпляр класса `PromptsCompressor`, задавая размеры команд для последующего формирования подсказок.

**Параметры**:
- `self`: Экземпляр класса.

**Возвращает**:
- `None`: Ничего не возвращает.

#### `get_prompt`

**Описание**: Получает и формирует текстовую подсказку на основе заданных параметров и индекса.

**Параметры**:
- `info` (list[str]): Список параметров для подстановки в шаблон подсказки.
- `ind` (int): Индекс шаблона подсказки.

**Возвращает**:
- `str`: Сформированная текстовая подсказка.

**Вызывает исключения**:
- `FileNotFoundError`: если файл `ToolBox/BaseSettings/prompts.json` не найден.

#### `html_tags_insert`

**Описание**: Вставляет HTML-теги в текст для форматирования.

**Параметры**:
- `response` (str): Текст, в который необходимо вставить HTML-теги.

**Возвращает**:
- `str`: Текст с вставленными HTML-тегами.