# Анализ кода модуля `hockey.py`

**Качество кода: 7/10**

*   **Плюсы**
    *   Код содержит подробное описание игры и её правил в виде многострочного комментария.
    *   Алгоритм игры хорошо структурирован и понятен.
    *   Имеется блок-схема игры в формате mermaid.
    *   Используются комментарии для пояснения основных частей кода.
    *   Есть обработка исключений при вводе данных.
*   **Минусы**
    *   Отсутствуют docstring у модуля и функций в формате reStructuredText.
    *   Используется стандартный `print` для вывода, вместо `logger`.
    *   Используется `try-except` для обработки ошибок, хотя можно использовать `logger.error`.
    *   Нет проверки корректности ввода углов и силы броска, что может привести к нежелательному поведению.
    *   Нет импорта модуля `src.logger.logger`.

**Рекомендации по улучшению**

1.  Добавить docstring в формате reStructuredText для модуля и функций, включая описание параметров и возвращаемых значений.
2.  Использовать `from src.logger.logger import logger` для логирования вместо `print`.
3.  Заменить `try-except` на `logger.error` для обработки ошибок.
4.  Добавить проверку на валидность введенных значений угла и силы броска (например, чтобы угол был от 0 до 90, а сила от 1 до 10).
5.  Удалить излишние комментарии, которые поясняют очевидные вещи.
6.  Использовать форматирование строк f-strings для повышения читаемости.

**Оптимизированный код**

```python
"""
Модуль для реализации игры в хоккей между двумя игроками.
=========================================================

Модуль содержит функции для управления игрой в хоккей между двумя игроками.
Игроки по очереди вводят угол и силу броска, пытаясь забить гол.
Игра длится 10 раундов, и в конце выводится победитель.

Пример использования
--------------------

.. code-block:: python

    from src.endpoints.ai_games.101_basic_computer_games.he.HOCKEY.hockey import play_hockey_game

    play_hockey_game()
"""
import random
#  Импортируем логер для записи ошибок и отладочной информации
from src.logger.logger import logger


def is_shot_successful(angle: int, strength: int) -> bool:
    """
    Определяет, был ли бросок успешным.

    :param angle: Угол броска (не используется напрямую в расчетах).
    :type angle: int
    :param strength: Сила броска (не используется напрямую в расчетах).
    :type strength: int
    :return: True, если бросок успешен, False в противном случае.
    :rtype: bool
    """
    #  Вероятность успеха броска определяется случайным образом для простоты
    return random.random() > 0.3


def play_hockey_game():
    """
    Запускает игру в хоккей между двумя игроками.
    
    Эта функция управляет ходом игры, включая ввод данных игроками,
    определение успешности бросков, подсчет очков и объявление победителя.
    """
    player1_score = 0 # Инициализация счета первого игрока
    player2_score = 0 # Инициализация счета второго игрока

    for turn in range(1, 11): #  Цикл, выполняющийся 10 раз (10 раундов игры)
        print(f"\nТур {turn}:")

        # Ход первого игрока
        try:
            #  Получаем ввод угла броска от первого игрока
            angle1 = int(input("Игрок 1, введите угол броска (0-90): "))
             #  Получаем ввод силы броска от первого игрока
            strength1 = int(input("Игрок 1, введите силу броска (1-10): "))
            #  Проверяем ввод на корректность (угол от 0 до 90, сила от 1 до 10)
            if not (0 <= angle1 <= 90 and 1 <= strength1 <= 10):
                logger.error(f"Некорректный ввод: угол = {angle1}, сила = {strength1}. Введите угол от 0 до 90, силу от 1 до 10.")
                print("Некорректный ввод, попробуйте еще раз")
                continue
        except ValueError as e:
            #  Логируем ошибку, если ввод не является целым числом
            logger.error("Некорректный ввод, пожалуйста, введите целые числа", exc_info=True)
            print("Некорректный ввод, пожалуйста, введите целые числа.")
            continue

        #  Проверяем, был ли бросок успешным
        if is_shot_successful(angle1, strength1):
             #  Увеличиваем счет первого игрока, если бросок был успешен
            player1_score += 1
            print("Игрок 1 забил гол!")
        else:
            print("Игрок 1 промахнулся.")

        # Ход второго игрока
        try:
             #  Получаем ввод угла броска от второго игрока
            angle2 = int(input("Игрок 2, введите угол броска (0-90): "))
             #  Получаем ввод силы броска от второго игрока
            strength2 = int(input("Игрок 2, введите силу броска (1-10): "))
            #  Проверяем ввод на корректность (угол от 0 до 90, сила от 1 до 10)
            if not (0 <= angle2 <= 90 and 1 <= strength2 <= 10):
                logger.error(f"Некорректный ввод: угол = {angle2}, сила = {strength2}. Введите угол от 0 до 90, силу от 1 до 10.")
                print("Некорректный ввод, попробуйте еще раз")
                continue
        except ValueError as e:
            #  Логируем ошибку, если ввод не является целым числом
            logger.error("Некорректный ввод, пожалуйста, введите целые числа", exc_info=True)
            print("Некорректный ввод, пожалуйста, введите целые числа.")
            continue

        #  Проверяем, был ли бросок успешным
        if is_shot_successful(angle2, strength2):
             #  Увеличиваем счет второго игрока, если бросок был успешен
            player2_score += 1
            print("Игрок 2 забил гол!")
        else:
            print("Игрок 2 промахнулся.")

        #  Выводим текущий счет
        print(f"Счет: Игрок 1 = {player1_score}, Игрок 2 = {player2_score}")

    # Объявление победителя
    print("\n--- Итоги игры ---")
    if player1_score > player2_score:
        print("Игрок 1 победил!")
    elif player2_score > player1_score:
        print("Игрок 2 победил!")
    else:
        print("Ничья!")


if __name__ == "__main__":
    play_hockey_game()
```