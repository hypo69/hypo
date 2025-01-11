# ACEDU

## Обзор

Этот модуль реализует игру ACEDU, в которой игрок должен угадать последовательность из 4 цифр (от 1 до 6). Игра предоставляет подсказки в виде количества цифр, находящихся на правильном месте ("Aced"), и количества цифр, которые присутствуют в последовательности, но не на своем месте ("Dueces").

## Содержание

- [Функции](#Функции)
    - [`play_acedu`](#play_acedu)

## Функции

### `play_acedu`

**Описание**: 
Функция реализует игру ACEDU, в которой игрок пытается угадать последовательность из 4 цифр, выбранных компьютером.

**Параметры**:
- Нет параметров.

**Возвращает**:
- None: Функция не возвращает значения, а управляет ходом игры и печатает результаты в консоль.

**Вызывает исключения**:
- `ValueError`: Возникает, если пользователь вводит некорректные данные (не цифры или неправильное количество цифр).
```python
def play_acedu():
    """
    Args:
        
    Returns:
        None: Функция не возвращает значения, а управляет ходом игры и печатает результаты в консоль.

    Raises:
        ValueError: Возникает, если пользователь вводит некорректные данные (не цифры или неправильное количество цифр).
    """
    continue_game = True
    target_sequence = [random.randint(1, 6) for _ in range(4)]

    while continue_game:
        while True:
            try:
                user_input = input("הזן ניחוש של 4 ספרות (1-6): ")
                user_sequence = [int(digit) for digit in user_input]
                if len(user_sequence) == 4 and all(1 <= digit <= 6 for digit in user_sequence):
                    break
                else:
                   print("קלט לא תקין. אנא הזן רצף של 4 ספרות בין 1 ל-6.")
            except ValueError as ex:
                print("קלט לא תקין. אנא הזן רק ספרות.")
        aced = 0
        dueces = 0

        for i in range(4):
           if user_sequence[i] == target_sequence[i]:
              aced += 1

        temp_target = target_sequence[:]
        temp_user = user_sequence[:]
         
        for digit in temp_user:
          if digit in temp_target:
            dueces += 1
            temp_target.remove(digit)

        dueces -= aced

        print(f"Aced: {aced}, Dueces: {dueces}")

        if aced == 4:
            print("You got it!")
            continue_game = False
```