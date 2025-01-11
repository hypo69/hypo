# ROCKSP - משחק "אבן, נייר ומספריים"

## Обзор
Файл `rocksp.py` содержит реализацию классической игры "Камень, ножницы, бумага" на иврите. В этой игре пользователь играет против компьютера, выбирая один из трех вариантов: камень, бумагу или ножницы. Программа определяет победителя на основе стандартных правил игры и предлагает пользователю сыграть снова.

## Содержание

- [Функции](#функции)
  - [`play_rock_paper_scissors`](#play_rock_paper_scissors)

## Функции

### `play_rock_paper_scissors`

**Описание**:
Функция `play_rock_paper_scissors` реализует логику игры "Камень, ножницы, бумага". Она позволяет пользователю играть против компьютера. Функция выводит на экран варианты выбора, обрабатывает ввод пользователя, генерирует случайный выбор компьютера и определяет победителя.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения.

**Вызывает исключения**:
- `ValueError`: Возникает, если пользователь вводит некорректное значение (не целое число от 1 до 3).

```python
def play_rock_paper_scissors():
    """
    Args:
        None

    Returns:
        None

    Raises:
        ValueError: Вызывается при некорректном вводе пользователя.
    """
    while True:
        print("בחר: (1) אבן, (2) נייר, (3) מספריים")
        try:
            user_choice = int(input("הכנס את בחירתך (1-3): "))
            if user_choice < 1 or user_choice > 3:
                print("בחירה לא חוקית, אנא בחר בין 1 ל 3")
                continue
        except ValueError as ex:
            print("קלט לא חוקי, אנא הזן מספר שלם בין 1 ל 3")
            continue
        
        computer_choice = random.randint(1, 3)
        
        choices = {1: "אבן", 2: "נייר", 3: "מספריים"}
        user_choice_name = choices[user_choice]
        computer_choice_name = choices[computer_choice]

        print(f"אתה בחרת: {user_choice_name}")
        print(f"המחשב בחר: {computer_choice_name}")

        if user_choice == computer_choice:
            print("תיקו!")
        elif (user_choice == 1 and computer_choice == 3) or \
             (user_choice == 2 and computer_choice == 1) or \
             (user_choice == 3 and computer_choice == 2):
            print("ניצחת!")
        else:
            print("הפסדת!")

        play_again = input("רוצה לשחק שוב? (כן/לא): ").lower()
        if play_again != "כן":
            break
```