# apps.hendlers

## Обзор

Модуль `apps.hendlers` содержит обработчики для различных команд и запросов, связанных с поиском фильмов и сериалов через Telegram-бота. Включает в себя обработку команды `/start`, выбор типа фильма (фильм или сериал) и обработку ввода названия фильма для последующего поиска.

## Подробней

Этот модуль является частью Telegram-бота для поиска фильмов. Он обрабатывает взаимодействие с пользователем, определяя, какой тип контента (фильм или сериал) интересует пользователя, и принимает название для поиска. После получения необходимой информации, модуль использует функцию `search_query` для выполнения поиска и предоставляет результаты пользователю. Взаимодействие осуществляется через `aiogram`, который обеспечивает функциональность Telegram-бота.

## Классы

### `Params(StatesGroup)`

**Описание**:
Класс `Params` используется для определения состояний в FSM (Finite State Machine) для обработки параметров поиска фильма.

**Методы**:
- `type_movie`: Состояние для ожидания ввода типа фильма (фильм или сериал).
- `name`: Состояние для ожидания ввода названия фильма.

## Функции

### `command_start_handler(message: Message) -> None`

```python
async def command_start_handler(message: Message) -> None:
    """
    Args:
        message (Message): Объект сообщения от Telegram.

    Returns:
        None

    """
```

**Описание**:
Обработчик команды `/start`. Отправляет приветственное сообщение пользователю и предлагает начать поиск фильма.

**Параметры**:
- `message` (Message): Объект сообщения от Telegram.

**Возвращает**:
- `None`

**Примеры**:
```python
# Пример вызова (в контексте aiogram):
# async def some_handler(message: types.Message):
#     await command_start_handler(message)
```

### `movie_handler(callback: CallbackQuery, state: FSMContext) -> None`

```python
async def movie_handler(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Args:
        callback (CallbackQuery): Объект обратного вызова от Telegram.
        state (FSMContext): Объект состояния FSM.

    Returns:
        None

    """
```

**Описание**:
Обработчик нажатия кнопки `new_movies`. Устанавливает состояние ожидания выбора типа фильма (фильм или сериал).

**Параметры**:
- `callback` (CallbackQuery): Объект обратного вызова от Telegram.
- `state` (FSMContext): Объект состояния FSM.

**Возвращает**:
- `None`

**Примеры**:
```python
# Пример вызова (в контексте aiogram):
# async def some_handler(callback: types.CallbackQuery, state: FSMContext):
#     await movie_handler(callback, state)
```

### `series_handler(callback: CallbackQuery, state: FSMContext) -> None`

```python
async def series_handler(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Args:
        callback (CallbackQuery): Объект обратного вызова от Telegram.
        state (FSMContext): Объект состояния FSM.

    Returns:
        None

    """
```

**Описание**:
Обработчик нажатия кнопки `series`. Удаляет предыдущее сообщение, обновляет состояние FSM, указывая, что пользователь ищет сериал, и запрашивает название сериала.

**Параметры**:
- `callback` (CallbackQuery): Объект обратного вызова от Telegram.
- `state` (FSMContext): Объект состояния FSM.

**Возвращает**:
- `None`

**Примеры**:
```python
# Пример вызова (в контексте aiogram):
# async def some_handler(callback: types.CallbackQuery, state: FSMContext):
#     await series_handler(callback, state)
```

### `film_handler(callback: CallbackQuery, state: FSMContext) -> None`

```python
async def film_handler(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Args:
        callback (CallbackQuery): Объект обратного вызова от Telegram.
        state (FSMContext): Объект состояния FSM.

    Returns:
        None

    """
```

**Описание**:
Обработчик нажатия кнопки `film`. Удаляет предыдущее сообщение, обновляет состояние FSM, указывая, что пользователь ищет фильм, и запрашивает название фильма.

**Параметры**:
- `callback` (CallbackQuery): Объект обратного вызова от Telegram.
- `state` (FSMContext): Объект состояния FSM.

**Возвращает**:
- `None`

**Примеры**:
```python
# Пример вызова (в контексте aiogram):
# async def some_handler(callback: types.CallbackQuery, state: FSMContext):
#     await film_handler(callback, state)
```

### `name_handler(message: Message, state: FSMContext) -> None`

```python
async def name_handler(message: Message, state: FSMContext) -> None:
    """
    Args:
        message (Message): Объект сообщения от Telegram.
        state (FSMContext): Объект состояния FSM.

    Returns:
        None

    """
```

**Описание**:
Обработчик ввода названия фильма. Обновляет состояние FSM, сохраняя название фильма, выполняет поиск фильма с использованием функции `search_query` и предоставляет результаты пользователю.

**Параметры**:
- `message` (Message): Объект сообщения от Telegram.
- `state` (FSMContext): Объект состояния FSM.

**Возвращает**:
- `None`

**Примеры**:
```python
# Пример вызова (в контексте aiogram):
# async def some_handler(message: types.Message, state: FSMContext):
#     await name_handler(message, state)