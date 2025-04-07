# Модуль для создания клавиатур для Telegram-бота

## Обзор

Этот модуль содержит определения для создания inline-клавиатур, используемых в Telegram-боте для взаимодействия с пользователем. Он предоставляет две inline-клавиатуры: `find_movie` и `choice`.

## Подробнее

Модуль используется для создания интерактивных элементов в Telegram-боте, позволяющих пользователям выбирать опции или выполнять действия, такие как поиск новых фильмов или выбор типа контента (сериал или фильм). Клавиатуры создаются с использованием библиотеки `aiogram`.

## Классы

В этом модуле нет классов.

## Функции

В этом модуле нет функций.

## Переменные

### `find_movie`

```python
find_movie = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Найти', callback_data='new_movies')]
])
```

**Назначение**: Inline-клавиатура, содержащая кнопку "Найти" для поиска новых фильмов.

**Как работает**:

1.  Создается объект `InlineKeyboardMarkup`.
2.  В `inline_keyboard` передается список списков, представляющий собой структуру клавиатуры.
3.  Внутри списка создается кнопка `InlineKeyboardButton` с текстом "Найти" и `callback_data` "new_movies". `callback_data` используется для идентификации нажатой кнопки при обработке ответа от пользователя.

**Примеры**:

```python
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

find_movie = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Найти', callback_data='new_movies')]
])
```

### `choice`

```python
choice = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сериал', callback_data='series'),
     InlineKeyboardButton(text='Фильм', callback_data='film')]
])
```

**Назначение**: Inline-клавиатура, предлагающая пользователю выбор между сериалом и фильмом.

**Как работает**:

1.  Создается объект `InlineKeyboardMarkup`.
2.  В `inline_keyboard` передается список списков, представляющий структуру клавиатуры.
3.  Внутри списка создаются две кнопки `InlineKeyboardButton`:
    *   Первая кнопка с текстом "Сериал" и `callback_data` "series".
    *   Вторая кнопка с текстом "Фильм" и `callback_data` "film".

**Примеры**:

```python
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

choice = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сериал', callback_data='series'),
     InlineKeyboardButton(text='Фильм', callback_data='film')]
])