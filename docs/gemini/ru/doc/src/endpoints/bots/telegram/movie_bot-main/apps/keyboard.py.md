# Модуль keyboard.py

## Обзор

Модуль `keyboard.py` содержит определения встроенных клавиатур для Telegram-ботов, используемых в приложении для работы с фильмами. В частности, он определяет две клавиатуры: `find_movie` для поиска новых фильмов и `choice` для выбора между сериалом и фильмом.

## Подробней

Этот модуль предоставляет удобные интерфейсные элементы для взаимодействия с пользователем через Telegram-бота. Клавиатуры позволяют пользователям быстро выбирать опции, не вводя текст вручную.

## Классы

В данном модуле нет классов.

## Функции

В данном модуле нет функций.

## InlineKeyboardMarkup

### `find_movie`

**Описание**: Клавиатура для поиска новых фильмов. Содержит кнопку "Найти", которая вызывает callback_data 'new_movies'.

**Как работает клавиатура**:

1.  Клавиатура `find_movie` создается с использованием `InlineKeyboardMarkup`.
2.  Она содержит одну кнопку "Найти", которая при нажатии отправляет `callback_data` 'new_movies'.
3.  `callback_data` используется ботом для обработки запроса пользователя и выполнения соответствующих действий.

**Пример**:

```python
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

find_movie = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Найти', callback_data='new_movies')]
])
```

### `choice`

**Описание**: Клавиатура для выбора между сериалом и фильмом. Содержит две кнопки: "Сериал" и "Фильм", вызывающие соответствующие callback_data 'series' и 'film'.

**Как работает клавиатура**:

1.  Клавиатура `choice` создается с использованием `InlineKeyboardMarkup`.
2.  Она содержит две кнопки: "Сериал" и "Фильм", которые при нажатии отправляют `callback_data` 'series' и 'film' соответственно.
3.  `callback_data` используется ботом для обработки выбора пользователя и выполнения соответствующих действий.

**Пример**:

```python
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

choice = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сериал', callback_data='series'),
     InlineKeyboardButton(text='Фильм', callback_data='film')]
])
```