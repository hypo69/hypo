# Анализ кода модуля LITQZ

**Качество кода**
  -  Соответствие требованиям к формату кода с 1 по 10:
    -  Преимущества:
       -  Текст представляет собой подробное описание игры, которое может быть использовано для дальнейшей реализации.
       -  Инструкции разделены на логические блоки и хорошо структурированы.
    -  Недостатки:
       -   Код не является Python кодом. Он представлен в формате Markdown с описанием алгоритма игры.
       -   Отсутствуют docstrings и комментарии в стиле RST.
       -   Не используется `j_loads` или `j_loads_ns`.
       -   Нет обработки ошибок и логирования.
       -   Отсутствуют импорты.
       -   Невозможно применить рефакторинг или улучшение как к Python коду.

**Рекомендации по улучшению**
  - Преобразовать описание игры в Python код с соблюдением всех требований.
  - Добавить docstring для модуля, функций и классов в формате reStructuredText (RST).
  - Использовать `j_loads` или `j_loads_ns` для работы с файлами.
  - Внедрить систему логирования с помощью `from src.logger.logger import logger`.
  - Обеспечить обработку ошибок с помощью `logger.error` вместо `try-except`.
  - Реализовать все этапы игры в коде, описанные в документе.
  - Придерживаться стандартов оформления кода Python (PEP 8).

**Улучшенный код**
```python
"""
Модуль для реализации игры LITQZ (Игра на логику и интеллект)
===========================================================

Этот модуль содержит реализацию игры-викторины LITQZ, в которой игрокам предлагается решать
интеллектуальные задачи.

Пример использования
--------------------

Пример запуска игры в одиночном режиме:

.. code-block:: python

    game = LITQZGame()
    game.start_game()

"""
import random  # импорт для рандомизации вопросов
from typing import List, Dict, Any  # импорт для аннотации типов
from src.utils.jjson import j_loads  # импорт для загрузки json
from src.logger.logger import logger # импорт для логирования
QUESTIONS_FILE = 'questions.json' # путь к файлу с вопросами


class LITQZGame:
    """
    Класс, представляющий игру LITQZ.

    :ivar questions: Список вопросов и ответов.
    :vartype questions: List[Dict[str, Any]]
    :ivar current_player: Текущий игрок.
    :vartype current_player: int
    :ivar scores: Словарь, хранящий очки игроков.
    :vartype scores: Dict[int, int]
    :ivar mode: Режим игры (одиночный или многопользовательский).
    :vartype mode: int
    :ivar number_of_questions: Количество вопросов в игре
    :vartype number_of_questions: int
    """

    def __init__(self, number_of_questions = 10):
        """
        Инициализирует игру LITQZ.
        Загружает вопросы из файла и устанавливает начальные значения.
        """
        self.questions = self._load_questions()  # загружает вопросы из файла
        self.current_player = 1  # игрок 1 начинает игру
        self.scores = {1: 0, 2: 0}  # начальные очки игроков
        self.mode = 0  # режим игры не выбран
        self.number_of_questions = number_of_questions # количество вопросов


    def _load_questions(self) -> List[Dict[str, Any]]:
         """
         Загружает вопросы из JSON файла.

         :return: Список вопросов.
         :rtype: List[Dict[str, Any]]
         """
         try:
             # используем j_loads для загрузки данных из файла
             with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
                  questions = j_loads(f)
                  if not isinstance(questions, list): # проверка что загрузился список
                      logger.error(f'Неверный формат данных в файле {QUESTIONS_FILE}')
                      return []
                  return questions
         except FileNotFoundError:
             logger.error(f'Файл {QUESTIONS_FILE} не найден') # логирование ошибки
             return []
         except Exception as ex:
             logger.error(f'Ошибка при загрузке данных из файла {QUESTIONS_FILE}: {ex}')
             return []

    def _display_welcome_message(self):
        """
         Выводит приветственное сообщение и правила игры.
        """
        print("Добро пожаловать в LITQZ!")
        print("Вам будут задаваться интеллектуальные вопросы.")
        print("Ваша задача — дать правильный ответ за наименьшее количество попыток.")
        print("Вы можете играть в одиночку или соревноваться с другим игроком. Удачи!\n")


    def _select_game_mode(self) -> int:
        """
         Позволяет игроку выбрать режим игры.

         :return: Выбранный режим игры (1 - одиночный, 2 - многопользовательский).
         :rtype: int
        """
        while True: # бесконечный цикл, пока не будет введён правильный вариант
            try:
                mode = int(input("Выберите режим игры:\n1. Одиночный\n2. Двухпользовательский\n> ")) # получаем ввод пользователя
                if mode in [1, 2]:  # проверка на корректный ввод
                    return mode # возвращаем выбранный режим
                else:
                     print("Неверный ввод. Пожалуйста, введите 1 или 2.") # сообщение об ошибке
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите число.") # сообщение об ошибке

    def _generate_question(self) -> Dict[str, Any]:
        """
        Случайно выбирает вопрос из списка.

        :return: Словарь, содержащий вопрос и ответ.
        :rtype: Dict[str, Any]
        """
        if not self.questions:
            logger.error("Нет доступных вопросов для игры")
            return {}
        return random.choice(self.questions)


    def _get_player_answer(self) -> str:
        """
        Получает ответ от игрока.

        :return: Ответ игрока.
        :rtype: str
        """
        return input("> ").strip()


    def _check_answer(self, question: Dict[str, Any], answer: str) -> bool:
        """
        Проверяет ответ игрока.

         :param question: Словарь с вопросом и ответом.
         :type question: Dict[str, Any]
         :param answer: Ответ игрока.
         :type answer: str
         :return: True, если ответ верный, False в противном случае.
         :rtype: bool
        """
        if not question or 'answer' not in question: # проверка на наличие вопроса и ответа
            logger.error("Неверный формат вопроса или ответа")
            return False
        return answer.lower() == question['answer'].lower()


    def _handle_single_player_game(self):
        """
        Обрабатывает одиночный режим игры.
        Игрок проходит серию вопросов и подсчитывает очки.
        """
        print("Начало одиночной игры\n")
        for i in range(self.number_of_questions): # цикл вопросов
            question = self._generate_question() # генерируем вопрос
            if not question: # проверяем что вопрос получен
                continue
            print(f"Вопрос {i + 1}: {question['question']}") # выводим вопрос
            attempts = 0 # попытки
            while attempts < 3: # даем 3 попытки
                answer = self._get_player_answer()  # получаем ответ
                if self._check_answer(question, answer): # проверка ответа
                   self.scores[1] += 10 - attempts * 3  # начисление очков
                   print("Правильно! Вы заработали баллы.\n")
                   break
                else:
                    attempts += 1  # увеличиваем количество попыток
                    print(f"Неверно. Попробуйте еще раз. Осталось попыток: {3 - attempts}\n")
            else:
                print(f"Правильный ответ: {question['answer']}\n") # если игрок не ответил, выводим ответ
        print(f"Игра окончена! Ваши результаты: {self.scores[1]} баллов\n")

    def _handle_multiplayer_game(self):
        """
        Обрабатывает многопользовательский режим игры.
        Игроки по очереди отвечают на вопросы.
        """
        print("Начало многопользовательской игры\n")
        for i in range(self.number_of_questions): # цикл вопросов
             question = self._generate_question()  # генерируем вопрос
             if not question:
                 continue
             print(f"Игрок {self.current_player}, ваш вопрос: {question['question']}")
             attempts = 0
             while attempts < 3:
                answer = self._get_player_answer() # получаем ответ
                if self._check_answer(question, answer): # проверка ответа
                    self.scores[self.current_player] += 10 - attempts * 3
                    print("Правильно! Вы заработали баллы.\n")
                    break
                else:
                    attempts += 1
                    print(f"Неверно. Попробуйте еще раз. Осталось попыток: {3 - attempts}\n")
             else:
                 print(f"Правильный ответ: {question['answer']}\n")
             self._switch_player()  # переключаем игрока
             print(f"Результаты после {i + 1} раунда: Игрок 1: {self.scores[1]} баллов, Игрок 2: {self.scores[2]} баллов\n") # выводим результат

        self._display_results()


    def _switch_player(self):
        """
        Переключает текущего игрока.
        """
        self.current_player = 3 - self.current_player  # переключает текущего игрока


    def _display_results(self):
        """
         Выводит результаты игры и определяет победителя.
        """
        print("Игра окончена! Ваши результаты:")
        print(f"Игрок 1: {self.scores[1]} баллов") # выводим результаты
        print(f"Игрок 2: {self.scores[2]} баллов") # выводим результаты
        if self.scores[1] > self.scores[2]:
            print("Победитель: Игрок 1!\n") # определяем победителя
        elif self.scores[2] > self.scores[1]:
             print("Победитель: Игрок 2!\n") # определяем победителя
        else:
             print("Ничья!\n")  # определяем ничью


    def start_game(self):
        """
         Запускает игру LITQZ.
        """
        self._display_welcome_message()  # выводим приветствие
        self.mode = self._select_game_mode() # выбираем режим игры
        if self.mode == 1:
            self._handle_single_player_game()  # обрабатываем одиночный режим
        elif self.mode == 2:
             self._handle_multiplayer_game() # обрабатываем многопользовательский режим
        else:
             logger.error("Неверный режим игры")
        self._play_again() # играем ещё раз

    def _play_again(self):
        """
        Предлагает игроку сыграть еще раз.
        """
        while True:
            play_again = input("Хотите сыграть снова? (да/нет): ").lower()
            if play_again == 'да':
                self.__init__() # переинициализация игры
                self.start_game() # запускаем игру снова
                break
            elif play_again == 'нет':
                print("Спасибо за игру!")
                break
            else:
                print("Неверный ввод. Пожалуйста, введите 'да' или 'нет'.") # сообщение об ошибке



if __name__ == "__main__":
    game = LITQZGame()  # создаем объект игры
    game.start_game() # запускаем игру
```