# Анализ кода модуля LITQZ

**Качество кода**

-   **Соответствие требованиям к формату кода (1-10)**:
    -   В основном соответствует требованиям, но не является исполняемым кодом Python.
    -   Требуется реализация на Python.
-   **Преимущества:**
    -   Описание игры четкое и подробное.
    -   Представлено пошаговое руководство по реализации игры.
    -   Примеры работы программы демонстрируют игровой процесс.
    -   Описаны возможные ограничения и рекомендации по улучшению.
-   **Недостатки:**
    -   Код представлен в виде текстового описания, а не в виде исполняемого кода.
    -   Отсутствует docstring для модуля и функций.
    -   Не используются `j_loads` или `j_loads_ns`.
    -   Отсутствует обработка ошибок через `logger.error`.
    -   Не используются импорты из `src.logger.logger import logger`.

**Рекомендации по улучшению**

1.  **Реализация на Python:** Преобразовать текстовое описание игры в исполняемый код на Python.
2.  **Добавить docstrings:** Добавить docstrings для модуля и функций в формате RST для документации.
3.  **Использовать `j_loads` или `j_loads_ns`:** Если для чтения данных из файлов используются функции `json.load`, необходимо заменить их на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
4.  **Обработка ошибок:** Использовать `try-except` блоки с `logger.error` для обработки ошибок.
5.  **Импорт логгера:** Импортировать `logger` из `src.logger.logger import logger`.
6.  **Добавить тесты:** Написать юнит тесты для проверки правильности работы кода.
7.  **Управление сложностью:** Реализовать систему уровней сложности.
8.  **Таймер:** Добавить таймер для ограничения времени на ответ.
9.  **База данных:** Добавить поддержку базы данных для хранения результатов игроков.

**Улучшенный код**
```python
"""
Модуль для реализации игры LITQZ (логическая викторина)
=========================================================================================

Этот модуль содержит логику и структуру игры LITQZ, в которой игроки отвечают на интеллектуальные вопросы.

Примеры использования
---------------------

Пример запуска игры:

.. code-block:: python

    game = LITQZGame()
    game.start_game()
"""
import random  # Импортируем модуль random для случайного выбора вопросов
from typing import List, Dict, Any  # Импортируем типы для аннотации

from src.logger.logger import logger # Импортируем logger для записи ошибок


class LITQZGame:
    """
    Класс для управления игрой LITQZ.
    """
    def __init__(self):
        """
        Инициализация игры, включая вопросы и ответы, а также начальные настройки.
        """
        self.questions = {
            "math": [
                {"question": "Сколько будет 5 + 7?", "answer": "12"},
                {"question": "Сколько будет 8 x 6?", "answer": "48"},
                {"question": "Что такое квадратный корень из 144?", "answer": "12"}, # Добавлен новый вопрос
            ],
            "logic": [
                {
                    "question": "Что тяжелее: 1 кг железа или 1 кг пуха?",
                    "answer": "одинаково",
                },
                {
                  "question": "Сколько углов у квадрата?",
                   "answer": "4",
                }, # Добавлен новый вопрос
            ],
            "general": [
                {
                    "question": "Какой город является столицей Франции?",
                    "answer": "париж",
                },
                 {
                    "question": "Что является столицей Японии?",
                    "answer": "токио",
                }, # Добавлен новый вопрос
            ],
        }
        self.players = {}
        self.current_player = None
        self.game_mode = None
        self.rounds_played = 0
        self.max_rounds = 10
        self.current_question = None # Добавлен атрибут для текущего вопроса
    def start_game(self):
        """
        Запускает игру, приветствует игрока, выбирает режим игры и начинает игру.
        """
        print("Добро пожаловать в LITQZ!")
        print(
            "Вам будут задаваться интеллектуальные вопросы.\nВаша задача — дать правильный ответ за наименьшее количество попыток."
        )
        print("Вы можете играть в одиночку или соревноваться с другим игроком. Удачи!")
        self.choose_game_mode()
        self.play_game()

    def choose_game_mode(self):
        """
        Позволяет игроку выбрать режим игры: одиночный или двухпользовательский.
        """
        while True:
            print("Выберите режим игры:")
            print("1. Одиночный режим")
            print("2. Двухпользовательский режим")
            choice = input("> ")
            if choice in ("1", "2"):
                self.game_mode = int(choice)
                break
            else:
                print("Неверный ввод. Пожалуйста, выберите 1 или 2.")
        if self.game_mode == 2: # Инициализация игроков
                self.players = {"Игрок 1": 0, "Игрок 2": 0}
                self.current_player = "Игрок 1"
    def play_game(self):
        """
        Осуществляет основной игровой процесс, включая генерацию вопросов, обработку ответов и подсчет очков.
        """
        if self.game_mode == 1:
            self.play_single_mode()
        elif self.game_mode == 2:
            self.play_multiplayer_mode()

    def play_single_mode(self):
        """
        Реализация одиночного режима игры.
        """
        score = 0
        for _ in range(self.max_rounds):
            question, answer = self.get_random_question()
            print(question)
            user_answer = input("> ").lower()
            if user_answer == answer:
                print("Правильно! Вы заработали 10 баллов.")
                score += 10
            else:
                print(f"Неправильно. Правильный ответ: {answer}")
        print(f"Игра окончена! Ваш результат: {score} баллов")
        self.play_again()
    def play_multiplayer_mode(self):
         """
         Реализация многопользовательского режима игры.
         """
         while self.rounds_played < self.max_rounds:
            question, answer = self.get_random_question()
            print(f"{self.current_player}, ваш вопрос:")
            print(question)
            user_answer = input("> ").lower()

            if user_answer == answer:
                 print("Правильно! Вы заработали 10 баллов.")
                 self.players[self.current_player] += 10
            else:
                 print(f"Неправильно. Правильный ответ: {answer}")
            self.rounds_played += 1
            self.switch_player()
            self.display_scores()
         self.end_game()
    def get_random_question(self) -> tuple[str, str]:
        """
        Случайно выбирает вопрос из доступных категорий и возвращает вопрос и ответ.

        :return: Кортеж, содержащий текст вопроса и правильный ответ.
        :rtype: tuple[str, str]
        """
        try:
             category = random.choice(list(self.questions.keys()))
             question_data = random.choice(self.questions[category])
             self.current_question = question_data
             return question_data["question"], question_data["answer"]
        except Exception as ex:
             logger.error(f"Ошибка при выборе случайного вопроса: {ex}")
             return "", ""  # Возвращаем пустую строку при ошибке
    def switch_player(self):
        """
        Переключает текущего игрока в многопользовательском режиме.
        """
        if self.current_player == "Игрок 1":
            self.current_player = "Игрок 2"
        else:
            self.current_player = "Игрок 1"
    def display_scores(self):
        """
        Выводит текущие очки игроков в многопользовательском режиме.
        """
        print("Результаты после раунда:")
        for player, score in self.players.items():
            print(f"{player}: {score} баллов")
    def end_game(self):
         """
         Завершает игру, объявляет результаты и предлагает сыграть снова.
         """
         print("Игра окончена! Ваши результаты:")
         winner = None
         max_score = -1
         for player, score in self.players.items():
              print(f"{player}: {score} баллов")
              if score > max_score:
                    max_score = score
                    winner = player
         print(f"Победитель: {winner}!")

         self.play_again()
    def play_again(self):
        """
        Спрашивает игрока, хочет ли он сыграть снова. Если да, начинает новую игру.
        """
        while True:
            play_again = input("Хотите сыграть снова? (да/нет): ").lower()
            if play_again in ("да", "нет"):
                break
            else:
                print("Неверный ввод. Пожалуйста, введите 'да' или 'нет'.")
        if play_again == "да":
            self.__init__()
            self.start_game()
        else:
            print("Спасибо за игру!")
if __name__ == "__main__":
    game = LITQZGame()
    game.start_game()
```