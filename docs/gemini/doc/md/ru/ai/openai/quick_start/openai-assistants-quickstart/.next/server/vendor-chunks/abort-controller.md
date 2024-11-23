```markdown
# Модуль abort-controller

## Обзор

Данный модуль содержит определения классов `AbortSignal` и `AbortController`,  обеспечивающие механизм отмены асинхронных операций в JavaScript.


## Классы

### `AbortSignal`

**Описание**: Класс `AbortSignal` представляет собой объект, который сигнализирует о необходимости прервать асинхронную операцию.

**Методы**:

- `get aborted()`: Возвращает `true`, если операция прервана, и `false` в противном случае.

### `AbortController`

**Описание**: Класс `AbortController` отвечает за создание и управление `AbortSignal` объектами.

**Методы**:

- `constructor()`: Инициализирует новый `AbortController`.
- `get signal()`: Возвращает связанный с данным `AbortController` объект `AbortSignal`.
- `abort()`: Отменяет асинхронную операцию, связанную с `AbortSignal`.


## Функции


### `createAbortSignal()`

**Описание**: Функция создает новый объект `AbortSignal`.

**Возвращает**:
- `AbortSignal`: Созданный объект `AbortSignal`.


### `abortSignal(signal)`

**Описание**: Функция отменяет асинхронную операцию, связанную с предоставленным `AbortSignal`.

**Параметры**:
- `signal (AbortSignal)`: Объект `AbortSignal` для отмены.


### `getSignal(controller)`

**Описание**: Функция возвращает `AbortSignal` объект, связанный с данным `AbortController`.

**Параметры**:
- `controller (AbortController)`: Объект `AbortController`.

**Возвращает**:
- `AbortSignal`: Объект `AbortSignal`, связанный с данным `AbortController`.

**Возможные исключения**:
- `TypeError`: Если переданный объект не является `AbortController` или `null`/`undefined`.



```
