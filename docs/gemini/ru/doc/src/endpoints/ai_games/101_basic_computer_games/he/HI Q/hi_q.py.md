# HI Q

## Обзор

Этот модуль реализует игру HI Q, в которой игрок должен перемещать фишки по доске, перепрыгивая через другие фишки, чтобы убрать их с доски. Цель игры - оставить только одну фишку, желательно в центре доски.

## Оглавление
1.  [Функции](#функции)
    *   [`print_board`](#print_board)
    *   [`is_valid_move`](#is_valid_move)
    *   [`make_move`](#make_move)
    *   [`check_win`](#check_win)
    *   [`play_hi_q`](#play_hi_q)

## Функции

### `print_board`

**Описание**:
Выводит текущее состояние игрового поля в консоль.

**Параметры**:
- `board` (list): Список, представляющий игровое поле.

**Возвращает**:
- `None`

### `is_valid_move`

**Описание**:
Проверяет, является ли ход с заданными начальной позицией и направлением допустимым.

**Параметры**:
- `board` (list): Список, представляющий игровое поле.
- `start` (int): Индекс начальной позиции хода.
- `direction` (str): Направление хода ('u', 'd', 'l', 'r').

**Возвращает**:
- `bool`: `True`, если ход допустим, `False` в противном случае.

### `make_move`

**Описание**:
Выполняет ход на игровом поле, обновляя его состояние.

**Параметры**:
- `board` (list): Список, представляющий игровое поле.
- `start` (int): Индекс начальной позиции хода.
- `direction` (str): Направление хода ('u', 'd', 'l', 'r').

**Возвращает**:
- `None`

### `check_win`

**Описание**:
Проверяет, выиграл ли игрок, то есть осталась ли на доске только одна фишка в центре.

**Параметры**:
- `board` (list): Список, представляющий игровое поле.

**Возвращает**:
- `bool`: `True`, если игрок выиграл, `False` в противном случае.

### `play_hi_q`

**Описание**:
Реализует основную логику игры HI Q.

**Параметры**:
- `None`

**Возвращает**:
- `None`

**Детали реализации**
- Инициализирует игровое поле и выводит его в консоль.
- Запускает игровой цикл, пока на доске не останется одна фишка.
- Запрашивает у пользователя ввод позиции фишки и направления хода.
- Проверяет корректность ввода и допустимость хода.
- Выполняет ход и обновляет игровое поле.
- Выводит результат игры (победа или поражение).