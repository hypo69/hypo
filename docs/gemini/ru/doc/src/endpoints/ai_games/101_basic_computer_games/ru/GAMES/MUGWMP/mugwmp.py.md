# MUGWMP

## Обзор

Игра "MUGWMP" - это текстовая игра, в которой игрок угадывает четырехзначное число, сгенерированное компьютером. После каждой попытки игрок получает подсказки в виде количества правильно угаданных цифр на своих местах (MUG) и количества правильно угаданных цифр не на своих местах (WMP). Цель - угадать число за минимальное количество попыток.

## Оглавление

1. [Функции](#функции)
    - [`generate_secret_number`](#generate_secret_number)
    - [`count_mug_wmp`](#count_mug_wmp)

## Функции

### `generate_secret_number`

**Описание**: Генерирует случайное четырехзначное число с уникальными цифрами.

**Параметры**:

- Нет параметров

**Возвращает**:
- `str`: Строка, представляющая четырехзначное число с уникальными цифрами.

### `count_mug_wmp`

**Описание**: Считает количество MUG (совпадений на своих местах) и WMP (совпадений не на своих местах).

**Параметры**:
- `secret` (str): Секретное число.
- `guess` (str): Предположение игрока.

**Возвращает**:
- `tuple`: Кортеж, содержащий количество MUG и WMP.

## Основной игровой процесс

1. **Генерация секретного числа**:
   - С помощью функции `generate_secret_number` генерируется четырехзначное число с уникальными цифрами.

2. **Инициализация попыток**:
   - Счетчик попыток `number_of_guesses` инициализируется нулем.

3. **Игровой цикл**:
   - Игра продолжается в цикле `while True`, пока игрок не угадает число.
   - Счетчик попыток увеличивается на единицу в начале каждой итерации цикла.

4. **Ввод пользовательского числа**:
   - Пользователю предлагается ввести четырехзначное число с уникальными цифрами.
   - Ввод проверяется на корректность (длина, наличие только цифр, уникальность цифр). Если ввод некорректен, пользователю предлагается ввести число повторно.

5. **Проверка выигрыша**:
   - Сравнивается введенное пользователем число с секретным числом.
   - Если числа совпадают, выводится сообщение о победе с количеством затраченных попыток и цикл завершается.

6. **Подсчет MUG и WMP**:
   - Если число не угадано, вызывается функция `count_mug_wmp`, которая считает количество совпадений на своих местах (MUG) и совпадений не на своих местах (WMP).

7. **Вывод подсказок**:
   - Выводится подсказка в формате "MUG = X, WMP = Y", где X - количество MUG, а Y - количество WMP.

8. **Повторение цикла**:
   - Цикл повторяется до тех пор, пока игрок не угадает число.