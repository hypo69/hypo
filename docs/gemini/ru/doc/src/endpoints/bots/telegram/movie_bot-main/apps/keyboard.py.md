# Модуль для создания клавиатур для Telegram Movie Bot

## Обзор

Модуль `keyboard.py` содержит определения встроенных клавиатур (InlineKeyboardMarkup) для Telegram-бота, предназначенного для поиска фильмов. Эти клавиатуры предоставляют пользователю интерфейс для выбора действий, таких как поиск новых фильмов или выбор типа контента (фильм или сериал).

## Подробнее

Этот модуль предоставляет готовые объекты `InlineKeyboardMarkup`, которые могут быть использованы при отправке сообщений пользователям через Telegram API. Каждая клавиатура содержит кнопки с определенным текстом и callback-data, которая используется для обработки нажатий на эти кнопки. Расположение файла `hypotez/src/endpoints/bots/telegram/movie_bot-main/apps/keyboard.py` указывает на то, что данный модуль является частью Telegram-бота для поиска фильмов.

## Переменные

### `find_movie`

```python
find_movie = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Найти', callback_data='new_movies')]
])
```

**Описание**: Встроенная клавиатура, содержащая одну кнопку "Найти".

**Параметры**:
- `inline_keyboard` (list[list[InlineKeyboardButton]]): Список списков кнопок. В данном случае содержит одну кнопку с текстом "Найти" и callback_data "new_movies".

**Примеры**:

```python
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

find_movie = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Найти', callback_data='new_movies')]
])

# Пример использования при отправке сообщения:
# await bot.send_message(chat_id=user_id, text='Нажмите кнопку, чтобы найти новые фильмы:', reply_markup=find_movie)
```

### `choice`

```python
choice = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сериал', callback_data='series'),
     InlineKeyboardButton(text='Фильм', callback_data='film')]
])
```

**Описание**: Встроенная клавиатура, предлагающая пользователю выбор между "Сериалом" и "Фильмом".

**Параметры**:
- `inline_keyboard` (list[list[InlineKeyboardButton]]): Список списков кнопок. В данном случае содержит две кнопки: "Сериал" с callback_data "series" и "Фильм" с callback_data "film".

**Примеры**:

```python
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

choice = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сериал', callback_data='series'),
     InlineKeyboardButton(text='Фильм', callback_data='film')]
])

# Пример использования при отправке сообщения:
# await bot.send_message(chat_id=user_id, text='Выберите тип контента:', reply_markup=choice)
```