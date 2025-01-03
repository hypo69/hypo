# SALVO I

## Обзор

Этот модуль реализует игру "Салво", в которой игрок должен угадать расположение корабля на игровом поле 10x10. Корабль имеет длину 3 клетки и располагается либо горизонтально, либо вертикально. Игрок вводит координаты выстрелов, пока не попадет в корабль.

## Содержание

- [Функции](#функции)
- [Переменные](#переменные)
- [Логика игры](#логика-игры)

## Функции

В данном файле нет определенных функций, так как основная логика игры реализована в основном теле скрипта.

## Переменные

### `numberOfGuesses`
**Описание**: Счетчик попыток игрока.
**Тип**: `int`
**Начальное значение**: `0`

### `shipStartRow`
**Описание**: Случайная начальная строка для размещения корабля.
**Тип**: `int`
**Диапазон значений**: `0-7`

### `shipStartCol`
**Описание**: Случайный начальный столбец для размещения корабля.
**Тип**: `int`
**Диапазон значений**: `0-7`

### `direction`
**Описание**: Случайное направление размещения корабля (0 - горизонтально, 1 - вертикально).
**Тип**: `int`
**Возможные значения**: `0` или `1`

### `shipPositions`
**Описание**: Список, содержащий координаты клеток, занимаемых кораблем.
**Тип**: `list`
**Формат**: `list` из `tuple` типа `(int, int)`

## Логика игры

### Инициализация
В начале игры происходит инициализация необходимых переменных:
- Счетчик `numberOfGuesses` устанавливается в 0.
- Случайным образом генерируются начальные координаты `shipStartRow` и `shipStartCol` для корабля, чтобы он не выходил за границы игрового поля.
- Случайным образом выбирается направление `direction` для корабля (горизонтальное или вертикальное).
- На основе начальных координат и направления вычисляются координаты всех клеток, занимаемых кораблем, и сохраняются в списке `shipPositions`.

### Игровой цикл
Игра продолжается в бесконечном цикле `while True`:
- На каждой итерации цикла увеличивается счетчик попыток `numberOfGuesses`.
- Игроку предлагается ввести координаты выстрела: строку `row` и столбец `col`.
- Проверяется, попал ли игрок в корабль, сравнивая введенные координаты с координатами корабля `shipPositions`.
- Если игрок попал, выводится сообщение "פגיעה!", а также количество попыток, и игра завершается с помощью оператора `break`.
- Если игрок промахнулся, выводится сообщение "החטאה!".

### Обработка ошибок
При вводе координат предусмотрена обработка ошибок:
- Блок `try-except` обрабатывает ошибку `ValueError`, которая может возникнуть, если игрок вводит нецелочисленные значения. В этом случае выводится сообщение об ошибке и программа просит повторить ввод.

### Завершение игры
Игра завершается, когда игрок попадает в корабль. Выводится сообщение о победе и количестве попыток.