# Модуль для создания клавиатур для Telegram бота
## Обзор

Модуль `keyboard.py` предназначен для создания и хранения различных встроенных клавиатур (InlineKeyboardMarkup) для Telegram-бота, используемого в проекте `hypotez`. Он содержит определения клавиатур для поиска фильмов и выбора типа контента (фильм или сериал).

## Подробней

Этот модуль предоставляет готовые объекты `InlineKeyboardMarkup`, которые могут быть использованы при отправке сообщений пользователям Telegram. Клавиатуры создаются с помощью библиотеки `aiogram`.

## Классы

В данном модуле классы отсутствуют.

## Функции

В данном модуле функции отсутствуют.

## InlineKeyboardMarkup

### `find_movie`

**Описание**: Клавиатура для поиска новых фильмов.

**Принцип работы**:
Клавиатура содержит одну кнопку с текстом "Найти", при нажатии на которую отправляется callback-data 'new_movies'.

**Структура**:

```
InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Найти', callback_data='new_movies')]])
```

**Элементы**:
- `inline_keyboard`: Список списков, содержащих объекты `InlineKeyboardButton`.

**InlineKeyboardButton**:
- `text`: Текст, отображаемый на кнопке ("Найти").
- `callback_data`: Данные, отправляемые боту при нажатии на кнопку ('new_movies').

**Пример**:

```python
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

find_movie = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Найти', callback_data='new_movies')]
])
```

### `choice`

**Описание**: Клавиатура для выбора типа контента (фильм или сериал).

**Принцип работы**:
Клавиатура содержит две кнопки: "Сериал" и "Фильм". При нажатии на кнопку "Сериал" отправляется callback-data 'series', а при нажатии на кнопку "Фильм" - callback-data 'film'.

**Структура**:

```
InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сериал', callback_data='series'),
     InlineKeyboardButton(text='Фильм', callback_data='film')]
])
```

**Элементы**:
- `inline_keyboard`: Список списков, содержащих объекты `InlineKeyboardButton`.

**InlineKeyboardButton**:
- `text`: Текст, отображаемый на кнопке ("Сериал" или "Фильм").
- `callback_data`: Данные, отправляемые боту при нажатии на кнопку ('series' или 'film').

**Пример**:

```python
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

choice = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сериал', callback_data='series'),
     InlineKeyboardButton(text='Фильм', callback_data='film')]
])