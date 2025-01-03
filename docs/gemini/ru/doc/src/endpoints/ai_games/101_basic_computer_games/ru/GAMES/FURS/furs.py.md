# Игра "Меха"

## Обзор

Игра "Меха" - это текстовая игра, в которой компьютер генерирует случайный текст, состоящий из случайных слов и цифр. Игрок пытается угадать, какие случайные слова и цифры были сгенерированы. Игра продолжается до тех пор, пока игрок не угадает все сгенерированные слова и цифры.

## Оглавление

- [Обзор](#обзор)
- [Игровой процесс](#игровой-процесс)
- [Переменные](#переменные)
- [Игровой цикл](#игровой-цикл)
- [Проверка соответствия](#проверка-соответствия)
- [Проверка победы и завершение игры](#проверка-победы-и-завершение-игры)

## Игровой процесс

1.  Компьютер выбирает случайные 4 слова из списка (в данном случае это заранее заданный список).
2.  Компьютер выбирает случайные 4 цифры из диапазона от 0 до 9.
3.  Игрок должен ввести слова и цифры, которые, по его мнению, были выбраны компьютером.
4.  Если игрок угадывает одно или несколько слов или цифр, компьютер выводит в какой позиции он угадал.
5.  Игра продолжается до тех пор, пока игрок не угадает все слова и цифры.

## Переменные

### `words`

**Описание**: Список возможных слов для выбора.

### `chosenWords`

**Описание**: Пустой список для хранения выбранных слов.

### `chosenDigits`

**Описание**: Пустой список для хранения выбранных цифр.

## Игровой цикл

### `while True:`

**Описание**: Основной игровой цикл, который продолжается до тех пор, пока игрок не угадает все слова и цифры.

**Действия**:

1. Запрашивает ввод от пользователя 4-х слов (A-J) и 4-х цифр (0-9) через пробел.
2. Разбивает ввод на список слов и список цифр.

## Проверка соответствия

### Проверка слов

**Описание**: Проверяет соответствие слов, введенных пользователем, с загаданными словами.

**Действия**:

-   Итерирует по списку введенных слов и сравнивает их с загаданными словами на соответствующих позициях.
-   Если слово угадано, выводит сообщение об этом.
-   Если хотя бы одно слово не угадано, флаг `all_correct` устанавливается в `False`.

### Проверка цифр

**Описание**: Проверяет соответствие цифр, введенных пользователем, с загаданными цифрами.

**Действия**:

-   Итерирует по списку введенных цифр и сравнивает их с загаданными цифрами на соответствующих позициях.
-   Обрабатывает исключение `ValueError`, если пользователь ввел не цифру.
-   Если цифра угадана, выводит сообщение об этом.
-   Если хотя бы одна цифра не угадана или произошла ошибка ввода, флаг `all_correct` устанавливается в `False`.

## Проверка победы и завершение игры

**Описание**: Проверяет, угадал ли игрок все слова и цифры, и завершает игру при победе.

**Действия**:

1.  Проверяет значение флага `all_correct`.
2.  Если `all_correct` равен `True`, игра считается выигранной.
3.  Выводится сообщение "YOU GOT IT!".
4.  Цикл завершается с помощью `break`, завершая игру.