# Анализ кода модуля FOOTBL

**Качество кода**
8
- Плюсы
    - Чёткое и подробное описание правил игры, пошаговой инструкции и примера работы.
    - Хорошая структура документа, разделение на логические блоки.
    - Наличие примеров работы программы, что помогает понять механику игры.
- Минусы
    - Отсутствует программный код, что делает невозможным анализ его структуры и стиля.
    - Нет информации о формате данных и импортах.
    - Отсутствуют комментарии в формате reStructuredText (RST).

**Рекомендации по улучшению**

1. **Добавить программный код:**
   - Необходимо предоставить программный код на Python, который будет реализовать описанную логику игры.

2. **Реализация функций:**
   - Разбить код на функции для инициализации игры, игрового процесса, расчёта результатов и т.д.

3. **Использование `random`:**
   - Использовать `random` для случайного определения исходов действий (бег, пас, пробитие).

4. **Структуры данных:**
   - Использовать списки или словари для хранения состояния игры (позиция на поле, счёт, таймы).

5. **Обработка пользовательского ввода:**
   - Добавить обработку пользовательского ввода для выбора действий и подтверждения продолжения игры.

6. **Логирование:**
   - Использовать `from src.logger.logger import logger` для логирования ошибок и важных событий.

7. **Документация RST:**
   - Добавить документацию в формате RST для всех функций, методов и классов.

8. **Структурирование кода:**
   - Разделить код на блоки для лучшей читаемости.

**Оптимизированный код**

```python
"""
Модуль для реализации текстовой игры в футбол.
=========================================================================================

Этот модуль содержит функции для запуска и управления игрой в футбол, включая инициализацию игры,
обработку ходов игрока и компьютера, подсчет очков и завершение игры.

Пример использования
--------------------

Пример запуска игры:

.. code-block:: python

    from src.games.footbl import start_game
    start_game()
"""
import random
from src.logger.logger import logger # импортируем logger

def initialize_game():
    """
    Инициализирует игру, запрашивает имя команды у игрока, генерирует соперника и выводит начальное сообщение.
    
    :return: tuple, содержащий имя команды игрока, имя команды соперника, уровень сложности и текущее положение на поле.
    """
    print("Добро пожаловать в игру FOOTBL!")
    team_name = input("Введите название вашей команды: ")
    opponent_level = random.randint(1, 3)
    opponent_names = {1: "Орлы", 2: "Медведи", 3: "Волки"}
    opponent_name = opponent_names.get(opponent_level, "Соперник")
    print(f"Ваш соперник: {opponent_name} (уровень сложности: {opponent_level})")
    print("Матч начался!")
    return team_name, opponent_name, opponent_level, 0 # начальное положение на поле 0 ярдов

def player_action(team_name, team_position, opponent_level):
    """
    Позволяет игроку выбрать действие (бег, пас или пробитие) и обрабатывает его результат.
    
    :param team_name: str, имя команды игрока.
    :param team_position: int, текущая позиция команды на поле.
    :param opponent_level: int, уровень сложности соперника.
    :return: tuple, содержащий новую позицию команды и количество заработанных очков.
    """
    while True:
        action = input("Выберите действие: бег, пас, пробитие: ").lower()
        if action in ["бег", "пас", "пробитие"]:
            break
        else:
            print("Неверный выбор действия. Попробуйте снова.")
    
    #  код исполняет расчёт продвижения и очков
    if action == "бег":
        yards = random.randint(2, 8) # генерация случайного количества ярдов при беге
        team_position += yards
        print(f"Вы продвинулись на {yards} ярдов. Ваши текущие позиции: {team_position} ярдов до зачётной зоны.")
    elif action == "пас":
        success = random.random() > 0.3 + opponent_level * 0.1 #  шанс на успех паса в зависимости от уровня соперника
        if success:
            yards = random.randint(10, 30) # генерация случайного количества ярдов при успешном пасе
            team_position += yards
            print(f"Пас прошёл удачно! Вы продвинулись на {yards} ярдов. До зачётной зоны осталось {100 - team_position} ярдов.")
        else:
             print("Пас перехвачен!")
    elif action == "пробитие":
         if team_position >= 90:
             touchdown = random.random() > 0.2 # шанс на тачдаун
             if touchdown:
                 print("Тачдаун! Вы заработали 6 очков.")
                 extra_point = input("Хотите выполнить реализацию? (да/нет): ").lower()
                 points = 6
                 if extra_point == "да":
                     success = random.random() > 0.3 #  шанс на реализацию
                     if success:
                        print("Удар по воротам успешен! +1 очко")
                        points +=1
                     else:
                        print("Реализация не удалась")
                 return team_position, points
             else:
                print("Пробитие не удалось!")

    return team_position, 0 #  возвращает новую позицию и 0 очков по умолчанию

def opponent_action(team_position, opponent_level):
    """
    Моделирует действие команды соперника.
    
    :param team_position: int, текущая позиция команды игрока.
    :param opponent_level: int, уровень сложности соперника.
    :return: int, количество ярдов, на которое продвинулась команда соперника.
    """
    if random.random() > 0.4 + opponent_level * 0.1: #  определяет действие соперника
         opponent_yards = random.randint(1, 10) #  рассчитывает на сколько продвинулся соперник
         print(f"Соперник продвинулся на {opponent_yards} ярдов.")
         return opponent_yards
    else:
       print("Соперник не смог продвинуться")
       return 0
        
def game_cycle(team_name, opponent_name, opponent_level):
    """
    Основной игровой цикл, управляет ходами игрока и компьютера, а также подсчётом очков.
    
    :param team_name: str, имя команды игрока.
    :param opponent_name: str, имя команды соперника.
    :param opponent_level: int, уровень сложности соперника.
    """
    team_score = 0
    opponent_score = 0
    team_position = 0
    opponent_position = 0

    for quarter in range(1, 5):
        print(f"\nНачало {quarter}-го тайма")
        while True:
           team_position, points = player_action(team_name, team_position, opponent_level)
           team_score += points
           if team_position >= 100:
               print(f"Счёт: {team_name} — {team_score}, {opponent_name} — {opponent_score}.")
               team_position = 0
               break
           opponent_yards = opponent_action(team_position, opponent_level)
           opponent_position += opponent_yards
           if opponent_position >=100:
               opponent_score +=6
               print(f"Счёт: {team_name} — {team_score}, {opponent_name} — {opponent_score}.")
               opponent_position = 0
               break
           print(f"Счёт: {team_name} — {team_score}, {opponent_name} — {opponent_score}.")
           if team_score >= 18 or opponent_score >=18:
              break
        if team_score >= 18 or opponent_score >=18:
           break
           
    return team_score, opponent_score

def end_game(team_name, opponent_name, team_score, opponent_score):
    """
    Завершает игру, выводит итоговый счёт и определяет победителя.
    
    :param team_name: str, имя команды игрока.
    :param opponent_name: str, имя команды соперника.
    :param team_score: int, количество очков команды игрока.
    :param opponent_score: int, количество очков команды соперника.
    """
    print("\nФинальный счёт:")
    print(f"{team_name} — {team_score}, {opponent_name} — {opponent_score}")
    if team_score > opponent_score:
        print("Поздравляем, вы победили!")
    elif team_score < opponent_score:
        print("Вы проиграли.")
    else:
        print("Ничья!")

def play_again():
    """
    Спрашивает игрока, хочет ли он сыграть еще раз.
    
    :return: bool, True, если игрок хочет сыграть еще раз, иначе False.
    """
    while True:
        choice = input("Хотите сыграть ещё раз? (да/нет): ").lower()
        if choice in ["да", "нет"]:
            return choice == "да"
        else:
            print("Неверный ввод. Пожалуйста, введите 'да' или 'нет'.")

def start_game():
    """
    Запускает основной процесс игры, включая инициализацию, игровой цикл и завершение игры.
    """
    while True:
        team_name, opponent_name, opponent_level, _ = initialize_game() #  инициализируем игру и получаем начальные параметры
        team_score, opponent_score = game_cycle(team_name, opponent_name, opponent_level) # запускаем игровой цикл
        end_game(team_name, opponent_name, team_score, opponent_score) #  завершаем игру и выводим результаты
        if not play_again(): #  если игрок не хочет играть снова, выходим из цикла
            print("Спасибо за игру!")
            break

if __name__ == '__main__':
    start_game()
```
```python
"""
Модуль для реализации текстовой игры в футбол.
=========================================================================================

Этот модуль содержит функции для запуска и управления игрой в футбол, включая инициализацию игры,
обработку ходов игрока и компьютера, подсчет очков и завершение игры.

Пример использования
--------------------

Пример запуска игры:

.. code-block:: python

    from src.games.footbl import start_game
    start_game()
"""
# импортируем logger
import random
from src.logger.logger import logger

def initialize_game():
    """
    Инициализирует игру, запрашивает имя команды у игрока, генерирует соперника и выводит начальное сообщение.
    
    :return: tuple, содержащий имя команды игрока, имя команды соперника, уровень сложности и текущее положение на поле.
    """
    print("Добро пожаловать в игру FOOTBL!")
    # Запрашиваем у игрока название команды
    team_name = input("Введите название вашей команды: ")
    # Генерируем случайный уровень сложности для соперника
    opponent_level = random.randint(1, 3)
    # Определяем имя соперника на основе уровня сложности
    opponent_names = {1: "Орлы", 2: "Медведи", 3: "Волки"}
    opponent_name = opponent_names.get(opponent_level, "Соперник")
    print(f"Ваш соперник: {opponent_name} (уровень сложности: {opponent_level})")
    print("Матч начался!")
    # Возвращаем начальные параметры игры
    return team_name, opponent_name, opponent_level, 0 # начальное положение на поле 0 ярдов

def player_action(team_name, team_position, opponent_level):
    """
    Позволяет игроку выбрать действие (бег, пас или пробитие) и обрабатывает его результат.
    
    :param team_name: str, имя команды игрока.
    :param team_position: int, текущая позиция команды на поле.
    :param opponent_level: int, уровень сложности соперника.
    :return: tuple, содержащий новую позицию команды и количество заработанных очков.
    """
    while True:
        # Запрашиваем у игрока выбор действия
        action = input("Выберите действие: бег, пас, пробитие: ").lower()
        # Проверяем корректность выбора
        if action in ["бег", "пас", "пробитие"]:
            break
        else:
            print("Неверный выбор действия. Попробуйте снова.")
    
    # код исполняет расчёт продвижения и очков
    if action == "бег":
        # Генерируем случайное количество ярдов при беге
        yards = random.randint(2, 8)
        team_position += yards
        print(f"Вы продвинулись на {yards} ярдов. Ваши текущие позиции: {team_position} ярдов до зачётной зоны.")
    elif action == "пас":
        # Определяем шанс на успех паса в зависимости от уровня соперника
        success = random.random() > 0.3 + opponent_level * 0.1
        if success:
            # Генерируем случайное количество ярдов при успешном пасе
            yards = random.randint(10, 30)
            team_position += yards
            print(f"Пас прошёл удачно! Вы продвинулись на {yards} ярдов. До зачётной зоны осталось {100 - team_position} ярдов.")
        else:
             print("Пас перехвачен!")
    elif action == "пробитие":
        # Проверяем, находится ли команда достаточно близко к зачётной зоне для пробития
         if team_position >= 90:
             # Определяем шанс на тачдаун
             touchdown = random.random() > 0.2
             if touchdown:
                 print("Тачдаун! Вы заработали 6 очков.")
                 # Спрашиваем игрока, хочет ли он выполнить реализацию
                 extra_point = input("Хотите выполнить реализацию? (да/нет): ").lower()
                 points = 6
                 if extra_point == "да":
                     # Определяем шанс на реализацию
                     success = random.random() > 0.3
                     if success:
                        print("Удар по воротам успешен! +1 очко")
                        points +=1
                     else:
                        print("Реализация не удалась")
                 return team_position, points
             else:
                print("Пробитие не удалось!")
    # Возвращаем новую позицию и 0 очков по умолчанию
    return team_position, 0

def opponent_action(team_position, opponent_level):
    """
    Моделирует действие команды соперника.
    
    :param team_position: int, текущая позиция команды игрока.
    :param opponent_level: int, уровень сложности соперника.
    :return: int, количество ярдов, на которое продвинулась команда соперника.
    """
    #  определяет действие соперника
    if random.random() > 0.4 + opponent_level * 0.1:
        # рассчитывает на сколько продвинулся соперник
         opponent_yards = random.randint(1, 10)
         print(f"Соперник продвинулся на {opponent_yards} ярдов.")
         return opponent_yards
    else:
       print("Соперник не смог продвинуться")
       return 0
        
def game_cycle(team_name, opponent_name, opponent_level):
    """
    Основной игровой цикл, управляет ходами игрока и компьютера, а также подсчётом очков.
    
    :param team_name: str, имя команды игрока.
    :param opponent_name: str, имя команды соперника.
    :param opponent_level: int, уровень сложности соперника.
    """
    team_score = 0
    opponent_score = 0
    team_position = 0
    opponent_position = 0
    # Игровой цикл из 4 таймов
    for quarter in range(1, 5):
        print(f"\nНачало {quarter}-го тайма")
        while True:
           #  получаем результат хода игрока и обновляем счёт
           team_position, points = player_action(team_name, team_position, opponent_level)
           team_score += points
           #  проверяем, достиг ли игрок конца поля
           if team_position >= 100:
               print(f"Счёт: {team_name} — {team_score}, {opponent_name} — {opponent_score}.")
               team_position = 0
               break
           #  выполняем ход соперника
           opponent_yards = opponent_action(team_position, opponent_level)
           opponent_position += opponent_yards
           #  проверяем, достиг ли соперник конца поля
           if opponent_position >=100:
               opponent_score +=6
               print(f"Счёт: {team_name} — {team_score}, {opponent_name} — {opponent_score}.")
               opponent_position = 0
               break
           print(f"Счёт: {team_name} — {team_score}, {opponent_name} — {opponent_score}.")
           #  проверяем, не набрал ли кто-то 18 очков и заканчиваем игру досрочно
           if team_score >= 18 or opponent_score >=18:
              break
        if team_score >= 18 or opponent_score >=18:
           break
           
    return team_score, opponent_score

def end_game(team_name, opponent_name, team_score, opponent_score):
    """
    Завершает игру, выводит итоговый счёт и определяет победителя.
    
    :param team_name: str, имя команды игрока.
    :param opponent_name: str, имя команды соперника.
    :param team_score: int, количество очков команды игрока.
    :param opponent_score: int, количество очков команды соперника.
    """
    print("\nФинальный счёт:")
    print(f"{team_name} — {team_score}, {opponent_name} — {opponent_score}")
    if team_score > opponent_score:
        print("Поздравляем, вы победили!")
    elif team_score < opponent_score:
        print("Вы проиграли.")
    else:
        print("Ничья!")

def play_again():
    """
    Спрашивает игрока, хочет ли он сыграть еще раз.
    
    :return: bool, True, если игрок хочет сыграть еще раз, иначе False.
    """
    while True:
        # Запрашиваем у игрока, хочет ли он сыграть еще раз
        choice = input("Хотите сыграть ещё раз? (да/нет): ").lower()
        # Проверяем корректность ввода
        if choice in ["да", "нет"]:
            return choice == "да"
        else:
            print("Неверный ввод. Пожалуйста, введите 'да' или 'нет'.")

def start_game():
    """
    Запускает основной процесс игры, включая инициализацию, игровой цикл и завершение игры.
    """
    while True:
        #  инициализируем игру и получаем начальные параметры
        team_name, opponent_name, opponent_level, _ = initialize_game()
        # запускаем игровой цикл
        team_score, opponent_score = game_cycle(team_name, opponent_name, opponent_level)
        # завершаем игру и выводим результаты
        end_game(team_name, opponent_name, team_score, opponent_score)
        # если игрок не хочет играть снова, выходим из цикла
        if not play_again():
            print("Спасибо за игру!")
            break
# код исполняет запуск игры, если скрипт вызывается напрямую
if __name__ == '__main__':
    start_game()