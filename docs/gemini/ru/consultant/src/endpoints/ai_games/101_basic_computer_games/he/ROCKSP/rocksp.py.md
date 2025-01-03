# Анализ кода модуля rocksp.py

**Качество кода**
8
-  Плюсы
    - Код игры "Камень, ножницы, бумага" реализован корректно и логично.
    - Присутствует обработка некорректного ввода пользователя.
    - Код хорошо задокументирован, присутствуют комментарии на иврите, поясняющие работу алгоритма.
    - Структура кода понятна и легко читаема.
-  Минусы
    - Комментарии не соответствуют формату reStructuredText (RST).
    - Отсутствует использование логирования.
    - Используется стандартный `print` для вывода сообщений, лучше использовать `logger` для вывода и для ошибок.

**Рекомендации по улучшению**

1.  **Переформатировать комментарии в reStructuredText (RST):** Все комментарии, включая docstring модуля и функции, должны быть переписаны в формате RST. Это включает описание модуля, функций и переменных.

2.  **Использовать логирование:**  Заменить `print` на `logger.info` для вывода информационных сообщений и `logger.error` для ошибок, это позволит более эффективно управлять процессом логирования.

3. **Упростить проверку ввода пользователя:** Можно упростить проверку ввода пользователя, используя `in`.

4.  **Улучшить читаемость кода:** Разделить логику игры на более мелкие функции для повышения читаемости и переиспользования кода.

**Оптимизированный код**

```python
"""
Модуль для игры в "Камень, ножницы, бумага"
=========================================

Этот модуль реализует классическую игру "Камень, ножницы, бумага" против компьютера.

Описание игры
-------------

В игре участвуют два игрока: человек и компьютер. Каждый игрок выбирает один из трех вариантов: камень, ножницы или бумага.
Победитель определяется следующим образом:
- Камень побеждает ножницы.
- Ножницы побеждают бумагу.
- Бумага побеждает камень.
Если оба игрока выбирают одинаковый вариант, объявляется ничья.

Алгоритм игры
-------------

1.  Вывод на экран вариантов выбора: камень, ножницы, бумага.
2.  Получение выбора от пользователя.
3.  Генерация случайного выбора для компьютера.
4.  Сравнение выборов пользователя и компьютера и определение победителя.
5.  Вывод результата игры на экран.
6.  Предложение сыграть снова.

Пример использования
--------------------

.. code-block:: python

    if __name__ == "__main__":
        play_rock_paper_scissors()
"""
import random
from src.logger.logger import logger

def get_user_choice() -> int:
    """
    Запрашивает выбор пользователя и проверяет его корректность.

    :return: Выбор пользователя (1 - камень, 2 - ножницы, 3 - бумага).
    :rtype: int
    """
    while True:
        print("בחר: (1) אבן, (2) נייר, (3) מספריים") # Вывод пользователю вариантов выбора
        try:
            user_choice = int(input("הכנס את בחירתך (1-3): ")) # Получение выбора пользователя
            if user_choice not in [1, 2, 3]: # Проверка корректности ввода
                logger.error("בחירה לא חוקית, אנא בחר בין 1 ל 3") # Логирование ошибки ввода
                continue
            return user_choice # Возврат выбора пользователя
        except ValueError:
            logger.error("קלט לא חוקי, אנא הזן מספר שלם בין 1 ל 3") # Логирование ошибки ввода
            continue

def get_computer_choice() -> int:
    """
    Генерирует случайный выбор для компьютера.

    :return: Случайный выбор компьютера (1 - камень, 2 - ножницы, 3 - бумага).
    :rtype: int
    """
    return random.randint(1, 3) # Генерация случайного выбора для компьютера

def determine_winner(user_choice: int, computer_choice: int) -> str:
    """
    Определяет победителя игры.

    :param user_choice: Выбор пользователя (1 - камень, 2 - ножницы, 3 - бумага).
    :type user_choice: int
    :param computer_choice: Выбор компьютера (1 - камень, 2 - ножницы, 3 - бумага).
    :type computer_choice: int
    :return: Результат игры ("תיקו!", "ניצחת!", "הפסדת!").
    :rtype: str
    """
    choices = {1: "אבן", 2: "נייר", 3: "מספריים"} # Словарь для преобразования числовых выборов в текстовые
    user_choice_name = choices[user_choice] # Получение текстового представления выбора пользователя
    computer_choice_name = choices[computer_choice] # Получение текстового представления выбора компьютера
    logger.info(f"אתה בחרת: {user_choice_name}") # Логирование выбора пользователя
    logger.info(f"המחשב בחר: {computer_choice_name}") # Логирование выбора компьютера

    if user_choice == computer_choice: # Проверка на ничью
        return "תיקו!" # Возврат результата - ничья
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2): # Проверка условий победы пользователя
        return "ניצחת!" # Возврат результата - победа пользователя
    else:
        return "הפסדת!" # Возврат результата - поражение пользователя

def play_again() -> bool:
    """
    Спрашивает пользователя, хочет ли он сыграть еще раз.

    :return: True, если пользователь хочет играть еще раз, False в противном случае.
    :rtype: bool
    """
    play_again_input = input("רוצה לשחק שוב? (כן/לא): ").lower() # Получение ответа пользователя
    return play_again_input == "כן" # Возврат результата - хочет играть или нет

def play_rock_paper_scissors():
    """
    Основная функция для запуска игры "Камень, ножницы, бумага".
    """
    while True:
        user_choice = get_user_choice() # Получение выбора пользователя
        computer_choice = get_computer_choice() # Получение выбора компьютера
        result = determine_winner(user_choice, computer_choice) # Определение результата игры
        logger.info(result) # Логирование результата игры

        if not play_again(): # Проверка - хочет ли пользователь играть снова
            break # Завершение игры, если пользователь не хочет играть снова

if __name__ == "__main__":
    play_rock_paper_scissors() # Запуск игры, если файл запущен напрямую

"""
הסבר הקוד:
1.  **ייבוא המודול `random`**::
    - `import random`: ייבוא המודול `random` המשמש ליצירת בחירה אקראית של המחשב.
2. **ייבוא `logger`**::
     -  `from src.logger.logger import logger`: импортируем логгер для логирования сообщений и ошибок
3.  **הגדרת הפונקציה `get_user_choice()`**::
    -  `def get_user_choice() -> int:`:  функция запрашивает выбор пользователя и проверяет его корректность
4.  **הגדרת הפונקציה `get_computer_choice()`**::
   - `def get_computer_choice() -> int:`: функция генерирует случайный выбор для компьютера
5. **הגדרת הפונקציה `determine_winner`**::
    - `def determine_winner(user_choice: int, computer_choice: int) -> str:`: функция определяет победителя игры
6. **הגדרת הפונקציה `play_again`**::
     -  `def play_again() -> bool:`: функция запрашивает пользователя, хочет ли он играть еще раз
7.  **הגדרת הפונקציה `play_rock_paper_scissors()`**::
    - `def play_rock_paper_scissors():`: основная функция для запуска игры
8.  **לולאת המשחק הראשית `while True:`**::
     -  `while True:`:  цикл, позволяющий играть до тех пор, пока пользователь не выберет не играть снова
9.  **קבלת קלט מהמשתמש**::
    -  `user_choice = get_user_choice()`: функция вызывает функцию `get_user_choice` для получения корректного ввода от пользователя
10. **יצירת בחירה אקראית למחשב**::
     - `computer_choice = get_computer_choice()`: функция вызывает функцию `get_computer_choice` для получения выбора компьютера
11. **השוואת הבחירות וקביעת המנצח**::
     - `result = determine_winner(user_choice, computer_choice)`: функция вызывает функцию `determine_winner` для определения результата игры
12. **שאלה האם לשחק שוב**::
      -  `if not play_again(): break`: если пользователь не хочет играть, цикл прерывается.
13. **הפעלת המשחק**::
      -  `if __name__ == "__main__":`:  условие запуска игры при прямом вызове файла
      -  `play_rock_paper_scissors()`: вызов основной функции игры
"""
```