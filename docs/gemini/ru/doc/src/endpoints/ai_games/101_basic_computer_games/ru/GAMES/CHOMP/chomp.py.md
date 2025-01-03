# CHOMP

## Обзор

Данный модуль реализует игру "CHOMP", в которой два игрока по очереди откусывают куски от шоколадной плитки. Цель игры - заставить противника съесть отравленную дольку, находящуюся в верхнем левом углу плитки.

## Оглавление
1. [Функции](#Функции)
   - [`initialize_board`](#initialize_board)
   - [`display_board`](#display_board)
   - [`make_move`](#make_move)
   - [`is_game_over`](#is_game_over)
   - [`play_chomp`](#play_chomp)

## Функции

### `initialize_board`

**Описание**:
Инициализирует игровое поле (шоколадную плитку).

**Параметры**:
- `rows` (int): Количество строк на доске.
- `cols` (int): Количество столбцов на доске.

**Возвращает**:
- `list of lists`: Список списков, представляющий игровую доску, где 'X' - шоколад, ' ' - пустое место.

### `display_board`

**Описание**:
Выводит текущее состояние доски на экран.

**Параметры**:
- `board` (list of lists): Игровая доска.

### `make_move`

**Описание**:
Обновляет состояние доски после хода игрока. Все клетки справа и выше выбранной позиции удаляются.

**Параметры**:
- `board` (list of lists): Игровая доска.
- `row_move` (int): Строка, на которую игрок сделал ход.
- `col_move` (int): Столбец, на который игрок сделал ход.

**Возвращает**:
- `list of lists`: Обновленная игровая доска.

### `is_game_over`

**Описание**:
Проверяет, закончилась ли игра. Игра заканчивается, если ядовитая долька (верхний левый угол) съедена.

**Параметры**:
- `board` (list of lists): Игровая доска.

**Возвращает**:
- `bool`: True, если игра окончена, иначе False.

### `play_chomp`

**Описание**:
Основная функция игры "CHOMP". Реализует игровой процесс, включая ввод размеров доски, отображение доски и обработку ходов игроков.

**Возвращает**:
- `None`: Функция ничего не возвращает.