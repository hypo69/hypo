# Модуль `chat_gpt.py`

## Обзор

Модуль `chat_gpt.py` предназначен для работы с файлами бесед ChatGpt, включая их обработку и извлечение данных.

## Оглавление

1. [Константы](#константы)
2. [Классы](#классы)
    - [`ChatGpt`](#ChatGpt)
        - [`yeld_conversations_htmls`](#yeld_conversations_htmls)

## Константы

### `MODE`

**Описание**: Режим работы, по умолчанию установлен в `dev`.

## Классы

### `ChatGpt`

**Описание**: Класс для работы с файлами бесед ChatGpt.

**Методы**:

- [`yeld_conversations_htmls`](#yeld_conversations_htmls)

#### `yeld_conversations_htmls`

**Описание**: Метод для обработки HTML файлов бесед.

**Параметры**:
- Нет.

**Возвращает**:
    - `str`: Возвращает `str`.
```python
    def yeld_conversations_htmls(self) -> str:
        """"""
        ...
        conversation_directory = Path(gs.path.data / 'chat_gpt' / 'conversations')
        html_files = conversation_directory.glob("*.html")
```