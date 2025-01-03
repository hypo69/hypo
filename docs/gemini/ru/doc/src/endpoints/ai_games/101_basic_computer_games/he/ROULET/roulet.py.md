# ROULET

## Обзор

Этот модуль представляет собой простую симуляцию игры в рулетку. Игрок вводит ставку на число от 0 до 36, а компьютер имитирует вращение рулетки и выводит результат. Если число, выбранное игроком, совпадает с результатом рулетки, игрок выигрывает.

## Содержание

- [Обзор](#обзор)
- [Алгоритм](#алгоритм)
- [Функции](#функции)
- [Пример использования](#пример-использования)

## Алгоритм

1.  Начать бесконечный цикл.
2.  Запросить у игрока ввод числа от 0 до 36 или нажать Enter для завершения.
3.  Если игрок нажал Enter, выйти из цикла.
4.  Если игрок ввел число, попытаться преобразовать его в целое число.
    *   Если преобразование не удалось, запросить ввод снова и перейти к следующей итерации цикла.
5.  Сгенерировать случайное число от 0 до 36.
6.  Если введенное игроком число равно сгенерированному, вывести "YOU WIN".
7.  Иначе, вывести сгенерированное число.
8.  Вернуться к шагу 2.

## Функции

### Основной игровой цикл

**Описание**: Основной цикл игры, который продолжается до тех пор, пока пользователь не решит выйти.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения.

**Вызывает исключения**:
- `ValueError`: Возникает, если ввод пользователя не может быть преобразован в целое число.

```python
import random

while True:
    user_input = input("הזן הימור (0-36) או הקש אנטר לסיום: ")

    if user_input == "":
        print("המשחק הסתיים")
        break

    try:
        user_bet = int(user_input)
    except ValueError as ex:
        print("קלט לא תקין. אנא הזן מספר שלם או הקש אנטר לסיום.")
        continue

    roulette_number = random.randint(0, 36)

    if user_bet == roulette_number:
        print("YOU WIN")
    else:
        print(roulette_number)
```

## Пример использования

При запуске скрипта пользователю будет предложено ввести ставку (число от 0 до 36) или нажать Enter для выхода. Игра будет продолжаться, пока пользователь не выберет выход.

```text
הזן הימור (0-36) או הקש אנטר לסיום: 10
25
הזן הימור (0-36) או הקש אנטר לסיום: 10
YOU WIN
הזן הימור (0-36) או הקש אנטר לסיום: abc
קלט לא תקין. אנא הזן מספר שלם או הקש אנטר לסיום.
הזן הימור (0-36) או הקש אנטר לסיום: 20
13
הזן הימור (0-36) או הקש אנטר לסיום: 
המשחק הסתיים
```