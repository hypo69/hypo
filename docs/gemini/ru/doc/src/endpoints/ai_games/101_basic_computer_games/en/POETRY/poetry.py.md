# Модуль POETRY

## Обзор

Модуль `POETRY` представляет собой игру, в которой компьютер генерирует случайные предложения, выбирая слова из предопределенных списков. Пользователь может изменять эти списки, вводя соответствующие коды.

## Содержание

- [Функции](#Функции)
  - [`change_list`](#change_list)
- [Основной код](#Основной-код)

## Функции

### `change_list`

**Описание**: Функция для изменения списка слов. Запрашивает у пользователя новые слова и возвращает новый список.

**Параметры**:

- `list_name` (str): Имя списка, который нужно изменить.

**Возвращает**:

- `list`: Новый список слов, введенный пользователем.

## Основной код

1. **Инициализация списков слов**:
    - `nouns`: Список существительных.
    - `verbs`: Список глаголов.
    - `adjectives`: Список прилагательных.
    - `prepositions`: Список предлогов.

2. **Приветствие и инструкции**:
   - Выводит на экран приветствие и инструкции для пользователя.

3. **Основной цикл игры**:
    - Генерирует случайное число от 1 до 4.
    - Если число равно 1, генерируется случайная фраза и выводится на экран.
    - В любом случае запрашивается у пользователя код для изменения списков или выхода.
    - В зависимости от введенного кода, вызывается функция `change_list` для изменения соответствующего списка.
    - Игра завершается, когда пользователь вводит код `0`.

4. **Завершение игры**:
    - Выводит сообщение "BYE".

**Пример использования**
```python
import random

# Начальные списки слов
nouns = ["BIRDS", "CATS", "DOGS", "FISH", "TREES", "FLOWERS", "RIVERS", "MOUNTAINS", "CLOUDS", "STARS"]
verbs = ["FLY", "RUN", "SWIM", "JUMP", "GROW", "BLOOM", "FLOW", "CLIMB", "FLOAT", "SHINE"]
adjectives = ["RED", "BLUE", "GREEN", "YELLOW", "TALL", "SHORT", "BIG", "SMALL", "BRIGHT", "DARK"]
prepositions = ["OVER", "UNDER", "IN", "ON", "BY", "NEAR", "THROUGH", "AROUND", "ACROSS", "ALONG"]

def change_list(list_name):
    """
    Args:
        list_name (str): Имя списка, который нужно изменить.

    Returns:
        list: Новый список слов, введенный пользователем.
    """
    new_list = input(f"Введите новые слова для списка {list_name} через запятую: ").upper().split(",")
    return new_list

print("Добро пожаловать в игру POETRY!")
print("Нажмите:")
print("1 чтобы поменять существительные")
print("2 чтобы поменять глаголы")
print("3 чтобы поменять прилагательные")
print("4 чтобы поменять предлоги")
print("0 чтобы выйти")

while True:
    # Генерируем случайное число от 1 до 4
    randomNumber = random.randint(1, 4)
    
    if randomNumber == 1:
       # Генерируем предложение
       random_noun = random.choice(nouns)
       random_verb = random.choice(verbs)
       random_adjective = random.choice(adjectives)
       random_preposition = random.choice(prepositions)

       phrase = f"THE {random_adjective} {random_noun} {random_verb} {random_preposition} THE FOREST"
       print(f"Случайная фраза: {phrase}")
       user_code = input("Введите код (0 для выхода): ")
       if user_code == "0":
            break
       else:
          try:
            user_code = int(user_code)
          except ValueError as ex:
            print ("Неверный ввод, введите 0, 1, 2, 3 или 4")
            continue

    else:
       user_code = input("Введите код (0 для выхода): ")
       if user_code == "0":
            break
       else:
          try:
            user_code = int(user_code)
          except ValueError as ex:
            print ("Неверный ввод, введите 0, 1, 2, 3 или 4")
            continue
          
    if user_code == 1:
            nouns = change_list("существительных")
    elif user_code == 2:
            verbs = change_list("глаголов")
    elif user_code == 3:
            adjectives = change_list("прилагательных")
    elif user_code == 4:
            prepositions = change_list("предлогов")
print("BYE")