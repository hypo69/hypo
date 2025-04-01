# apps.hendlers

## Обзор

Модуль `apps.hendlers` предназначен для обработки различных взаимодействий с пользователем в Telegram-боте. Он содержит обработчики команд и запросов, связанных с поиском фильмов и сериалов. Модуль использует библиотеку `aiogram` для работы с Telegram API и включает в себя определение состояний для управления диалогом с пользователем.

## Подробней

Модуль `apps.hendlers` обрабатывает команды `/start`, запросы на поиск фильмов/сериалов, а также сохраняет и передает параметры поиска (тип и название) между состояниями. Он использует клавиатуру (`apps.keyboard`) для предоставления пользователю выбора и вызывает функцию `search_query` (`apps.search`) для выполнения поиска.

## Классы

### `Params`

**Описание**:
Класс `Params` представляет собой группу состояний (StatesGroup) для хранения параметров поиска фильма или сериала.

**Методы**:
- `type_movie`: Состояние для хранения типа фильма/сериала.
- `name`: Состояние для хранения названия фильма/сериала.

## Функции

### `command_start_handler`

```python
async def command_start_handler(message: Message) -> None:
    """
    Args:
        message (Message): Объект сообщения от пользователя.

    Returns:
        None

    Raises:
        No exceptions
    """
```

**Описание**:
Обработчик команды `/start`. Отправляет приветственное сообщение пользователю и предлагает начать поиск фильма.

**Параметры**:
- `message` (Message): Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Возвращает**:
- `None`

**Примеры**:
```python
# Пример вызова (непосредственно не вызывается, вызывается aiogram при получении команды /start)
# await command_start_handler(message)
```

### `movie_handler`

```python
async def movie_handler(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Args:
        callback (CallbackQuery): Объект callback query от пользователя.
        state (FSMContext): Объект FSM context для управления состоянием пользователя.

    Returns:
        None

    Raises:
        No exceptions
    """
```

**Описание**:
Обработчик callback-запроса `new_movies`. Устанавливает состояние `Params.type_movie` и предлагает пользователю указать, что он ищет: фильм или сериал.

**Параметры**:
- `callback` (CallbackQuery): Объект callback-запроса, содержащий информацию о нажатой кнопке.
- `state` (FSMContext): Объект FSM context, используемый для управления состоянием пользователя.

**Возвращает**:
- `None`

**Примеры**:
```python
# Пример вызова (непосредственно не вызывается, вызывается aiogram при получении callback-запроса с data == 'new_movies')
# await movie_handler(callback, state)
```

### `series_handler`

```python
async def series_handler(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Args:
        callback (CallbackQuery): Объект callback query от пользователя.
        state (FSMContext): Объект FSM context для управления состоянием пользователя.

    Returns:
        None

    Raises:
        No exceptions
    """
```

**Описание**:
Обработчик callback-запроса `series`. Удаляет предыдущее сообщение, обновляет данные состояния, устанавливает состояние `Params.name` и запрашивает название сериала.

**Параметры**:
- `callback` (CallbackQuery): Объект callback-запроса, содержащий информацию о нажатой кнопке.
- `state` (FSMContext): Объект FSM context, используемый для управления состоянием пользователя.

**Возвращает**:
- `None`

**Примеры**:
```python
# Пример вызова (непосредственно не вызывается, вызывается aiogram при получении callback-запроса с data == 'series')
# await series_handler(callback, state)
```

### `film_handler`

```python
async def film_handler(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Args:
        callback (CallbackQuery): Объект callback query от пользователя.
        state (FSMContext): Объект FSM context для управления состоянием пользователя.

    Returns:
        None

    Raises:
        No exceptions
    """
```

**Описание**:
Обработчик callback-запроса `film`. Удаляет предыдущее сообщение, обновляет данные состояния, устанавливает состояние `Params.name` и запрашивает название фильма.

**Параметры**:
- `callback` (CallbackQuery): Объект callback-запроса, содержащий информацию о нажатой кнопке.
- `state` (FSMContext): Объект FSM context, используемый для управления состоянием пользователя.

**Возвращает**:
- `None`

**Примеры**:
```python
# Пример вызова (непосредственно не вызывается, вызывается aiogram при получении callback-запроса с data == 'film')
# await film_handler(callback, state)
```

### `name_handler`

```python
async def name_handler(message: Message, state: FSMContext) -> None:
    """
    Args:
        message (Message): Объект сообщения от пользователя.
        state (FSMContext): Объект FSM context для управления состоянием пользователя.

    Returns:
        None

    Raises:
        No exceptions
    """
```

**Описание**:
Обработчик сообщений в состоянии `Params.name`. Обновляет данные состояния названием фильма/сериала, выполняет поиск с использованием `search_query` и отправляет результат пользователю. После этого предлагает начать новый поиск и очищает состояние.

**Параметры**:
- `message` (Message): Объект сообщения, содержащий название фильма/сериала.
- `state` (FSMContext): Объект FSM context, используемый для управления состоянием пользователя.

**Возвращает**:
- `None`

**Примеры**:
```python
# Пример вызова (непосредственно не вызывается, вызывается aiogram при получении сообщения в состоянии Params.name)
# await name_handler(message, state)