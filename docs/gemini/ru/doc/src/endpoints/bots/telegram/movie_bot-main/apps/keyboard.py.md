# Модуль keyboard.py

## Обзор

Модуль `keyboard.py` содержит определения inline-клавиатур для Telegram-бота. Он предоставляет готовые клавиатуры для различных действий, таких как поиск фильмов и выбор типа контента (фильм или сериал). Этот модуль упрощает взаимодействие пользователя с ботом через графический интерфейс.

## Подробней

Этот модуль предназначен для создания интерактивных элементов интерфейса в Telegram-боте. Он определяет inline-клавиатуры, которые позволяют пользователям быстро выполнять действия, выбирая соответствующие кнопки. В частности, модуль предоставляет клавиатуры для поиска новых фильмов и выбора между фильмами и сериалами.

## Классы

В данном модуле классы отсутствуют.

## Функции

В данном модуле функции отсутствуют.

## InlineKeyboardMarkup

### `find_movie`

```python
find_movie = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Найти', callback_data='new_movies')]
])
```

**Описание**: Клавиатура для поиска новых фильмов.

**Параметры**: 
- `inline_keyboard` (list[list[InlineKeyboardButton]]): Список списков кнопок. В данном случае, содержит одну кнопку с текстом "Найти" и callback_data "new_movies".

**Примеры**:
```python
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

find_movie = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Найти', callback_data='new_movies')]
])

# Использование клавиатуры в обработчике команды
# await bot.send_message(chat_id=chat_id, text="Нажмите кнопку, чтобы найти новые фильмы", reply_markup=find_movie)
```

### `choice`

```python
choice = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сериал', callback_data='series'),
     InlineKeyboardButton(text='Фильм', callback_data='film')]
])
```

**Описание**: Клавиатура для выбора типа контента: фильм или сериал.

**Параметры**:
- `inline_keyboard` (list[list[InlineKeyboardButton]]): Список списков кнопок. В данном случае, содержит две кнопки: "Сериал" с callback_data "series" и "Фильм" с callback_data "film".

**Примеры**:
```python
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

choice = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сериал', callback_data='series'),
     InlineKeyboardButton(text='Фильм', callback_data='film')]
])

# Использование клавиатуры в обработчике команды
# await bot.send_message(chat_id=chat_id, text="Выберите тип контента:", reply_markup=choice)