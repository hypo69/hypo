# Документация для `user_router.py`

## Обзор

Модуль `user_router.py` определяет обработчики для различных пользовательских взаимодействий в Telegram-боте, включая обработку команды `/start`, переходы по страницам "Главная", "О магазине", "Мой профиль" и "Мои покупки". Он использует библиотеку `aiogram` для обработки входящих сообщений и callback-запросов от пользователей. Модуль также взаимодействует с базой данных через `UserDAO` для получения и обновления информации о пользователях и их покупках.

## Подробней

Этот файл является частью Telegram-бота `hypotez`, который предоставляет пользователям возможность взаимодействовать с магазином через Telegram. Здесь реализованы основные обработчики команд и callback-запросов, связанных с пользовательским интерфейсом бота.

- Обработчик команды `/start` регистрирует новых пользователей и приветствует существующих.
- Обработчики callback-запросов позволяют пользователям переходить по различным страницам бота, таким как "Главная", "О магазине", "Мой профиль" и "Мои покупки".
- Информация о пользователях и их покупках получается из базы данных с использованием `UserDAO`.
- Ответы бота формируются с использованием клавиатур (`main_user_kb`, `purchases_kb`) для удобной навигации.

## Классы

### `user_router`

**Описание**: Роутер для обработки пользовательских взаимодействий.

**Методы**:
- `message`: Регистрирует обработчики для входящих сообщений.
- `callback_query`: Регистрирует обработчики для callback-запросов.

**Параметры**:
- Нет параметров.

**Примеры**
```python
from aiogram import Router

user_router = Router()
```

## Функции

### `cmd_start`

```python
async def cmd_start(message: Message, session_with_commit: AsyncSession):
    """
    Args:
        message (Message): Объект сообщения от Telegram.
        session_with_commit (AsyncSession): Асинхровая сессия SQLAlchemy для работы с базой данных.

    Returns:
        await message.answer: Возвращает приветственное сообщение с клавиатурой для зарегистрированных пользователей.
        await message.answer: Возвращает сообщение об успешной регистрации с клавиатурой для новых пользователей.

    """
```

**Описание**: Обрабатывает команду `/start`. Регистрирует нового пользователя, если его нет в базе данных, или приветствует существующего пользователя.

**Параметры**:
- `message` (Message): Объект сообщения от Telegram.
- `session_with_commit` (AsyncSession): Асинхровая сессия SQLAlchemy для работы с базой данных.

**Возвращает**:
- `await message.answer`: Возвращает приветственное сообщение с клавиатурой для зарегистрированных пользователей.
- `await message.answer`: Возвращает сообщение об успешной регистрации с клавиатурой для новых пользователей.

**Примеры**:
```python
# Пример вызова функции cmd_start
# Допустим, у нас есть объекты message и session_with_commit
# await cmd_start(message, session_with_commit)
```

### `page_home`

```python
async def page_home(call: CallbackQuery):
    """
    Args:
        call (CallbackQuery): Объект callback-запроса от Telegram.

    Returns:
        await call.message.answer: Возвращает приветственное сообщение с клавиатурой для пользователя.
    """
```

**Описание**: Обрабатывает callback-запрос для перехода на главную страницу.

**Параметры**:
- `call` (CallbackQuery): Объект callback-запроса от Telegram.

**Возвращает**:
- `await call.message.answer`: Возвращает приветственное сообщение с клавиатурой для пользователя.

**Примеры**:
```python
# Пример вызова функции page_home
# Допустим, у нас есть объект call
# await page_home(call)
```

### `page_about`

```python
async def page_about(call: CallbackQuery):
    """
    Args:
        call (CallbackQuery): Объект callback-запроса от Telegram.

    Returns:
        await call.message.answer: Возвращает сообщение с информацией о магазине.
    """
```

**Описание**: Обрабатывает callback-запрос для перехода на страницу "О магазине".

**Параметры**:
- `call` (CallbackQuery): Объект callback-запроса от Telegram.

**Возвращает**:
- `await call.message.answer`: Возвращает сообщение с информацией о магазине.

**Примеры**:
```python
# Пример вызова функции page_about
# Допустим, у нас есть объект call
# await page_about(call)
```

### `page_about`

```python
async def page_about(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Args:
        call (CallbackQuery): Объект callback-запроса от Telegram.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для работы с базой данных (без коммита).

    Returns:
        await call.message.answer: Возвращает сообщение с информацией о профиле пользователя.
    """
```

**Описание**: Обрабатывает callback-запрос для перехода на страницу "Мой профиль".

**Параметры**:
- `call` (CallbackQuery): Объект callback-запроса от Telegram.
- `session_without_commit` (AsyncSession): Асинхровая сессия SQLAlchemy для работы с базой данных (без коммита).

**Возвращает**:
- `await call.message.answer`: Возвращает сообщение с информацией о профиле пользователя.

**Примеры**:
```python
# Пример вызова функции page_about
# Допустим, у нас есть объекты call и session_without_commit
# await page_about(call, session_without_commit)
```

### `page_user_purchases`

```python
async def page_user_purchases(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Args:
        call (CallbackQuery): Объект callback-запроса от Telegram.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для работы с базой данных (без коммита).

    Returns:
        await call.message.answer: Возвращает список покупок пользователя или сообщение об их отсутствии.
    """
```

**Описание**: Обрабатывает callback-запрос для перехода на страницу "Мои покупки".

**Параметры**:
- `call` (CallbackQuery): Объект callback-запроса от Telegram.
- `session_without_commit` (AsyncSession): Асинхровая сессия SQLAlchemy для работы с базой данных (без коммита).

**Возвращает**:
- `await call.message.answer`: Возвращает список покупок пользователя или сообщение об их отсутствии.

**Примеры**:
```python
# Пример вызова функции page_user_purchases
# Допустим, у нас есть объекты call и session_without_commit
# await page_user_purchases(call, session_without_commit)
```