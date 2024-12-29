# POETRY

## Обзор

Игра "Поэзия" - это игра, в которой компьютер генерирует случайные предложения, выбирая случайные слова из заранее заданных списков. Игрок может влиять на генерацию, вводя различные коды, которые меняют источник слов. Цель игры - увидеть и оценить случайные и иногда абсурдные результаты генерации фраз.

## Оглавление
1. [Функции](#Функции)
    - [`change_list`](#change_list)
2. [Основной код](#Основной-код)
    - [Инициализация списков](#Инициализация-списков)
    - [Приветствие и инструкции](#Приветствие-и-инструкции)
    - [Основной цикл игры](#Основной-цикл-игры)
    - [Завершение игры](#Завершение-игры)

## Функции

### `change_list`

**Описание**: Функция для изменения списка слов.

**Параметры**:
- `list_name` (str): Имя списка, который нужно изменить.

**Возвращает**:
- `list`: Новый список слов, введенных пользователем.

### Основной код

#### Инициализация списков

```python
nouns = ["BIRDS", "CATS", "DOGS", "FISH", "TREES", "FLOWERS", "RIVERS", "MOUNTAINS", "CLOUDS", "STARS"]
verbs = ["FLY", "RUN", "SWIM", "JUMP", "GROW", "BLOOM", "FLOW", "CLIMB", "FLOAT", "SHINE"]
adjectives = ["RED", "BLUE", "GREEN", "YELLOW", "TALL", "SHORT", "BIG", "SMALL", "BRIGHT", "DARK"]
prepositions = ["OVER", "UNDER", "IN", "ON", "BY", "NEAR", "THROUGH", "AROUND", "ACROSS", "ALONG"]
```
-   Инициализирует списки существительных (`nouns`), глаголов (`verbs`), прилагательных (`adjectives`) и предлогов (`prepositions`) начальными значениями.

#### Приветствие и инструкции
```python
print("Добро пожаловать в игру POETRY!")
print("Нажмите:")
print("1 чтобы поменять существительные")
print("2 чтобы поменять глаголы")
print("3 чтобы поменять прилагательные")
print("4 чтобы поменять предлоги")
print("0 чтобы выйти")
```
- Выводит на экран приветствие и инструкции для пользователя.

#### Основной цикл игры
```python
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
          except ValueError:
            print ("Неверный ввод, введите 0, 1, 2, 3 или 4")
            continue

    else:
       user_code = input("Введите код (0 для выхода): ")
       if user_code == "0":
            break
       else:
          try:
            user_code = int(user_code)
          except ValueError:
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
```
-   Бесконечный цикл, который продолжается, пока пользователь не введет `0`.
-   Генерирует случайное число от 1 до 4.
-   Если случайное число равно 1, генерирует случайную фразу, используя текущие значения списков.
-   Запрашивает у пользователя ввод кода для изменения списка слов.
-   Обрабатывает ввод пользователя, изменяя соответствующие списки, если ввод не `0`.
-   Обрабатывает исключение `ValueError` в случае некорректного ввода.

#### Завершение игры
```python
print("BYE")
```
-   Выводит сообщение "BYE" после завершения цикла (когда пользователь ввел 0).