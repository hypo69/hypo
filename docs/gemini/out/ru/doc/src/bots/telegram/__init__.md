# Модуль `hypotez/src/bots/telegram/__init__.py`

## Обзор

Данный модуль (`hypotez/src/bots/telegram/__init__.py`) содержит инициализацию для бота Telegram. Он импортирует класс `TelegramBot` из подмодуля `.bot`.  Также определяет константу `MODE`, которая, судя по имени, вероятно, используется для выбора режима работы (например, `dev`, `prod`).

## Переменные

### `MODE`

**Описание**: Переменная, хранящая режим работы. Значение по умолчанию `'dev'`.

## Импорты

### `from .bot import TelegramBot`

**Описание**: Импортирует класс `TelegramBot` из модуля `.bot`.

## Содержимое

```python
MODE = 'dev'

from .bot import TelegramBot
```