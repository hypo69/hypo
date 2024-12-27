# Анализ кода модуля `70_poetry.ru.md`

**Качество кода: 7/10**

- **Плюсы:**
    - Документ содержит подробное описание игры "POETRY" и пошаговую инструкцию её реализации.
    - Приведены примеры работы программы, которые наглядно демонстрируют игровой процесс.
    - Описаны возможные ограничения и рекомендации по улучшению, что способствует пониманию и развитию проекта.

- **Минусы:**
    - Отсутствует какой-либо код, что делает документ скорее спецификацией, чем готовым к исполнению кодом.
    - Документ не содержит reStructuredText (RST) форматирования для комментариев, как это требуется в инструкции.
    - Нет упоминания о логировании ошибок и использовании `j_loads` или `j_loads_ns`.
    - Нет примеров функций и классов, а также их документирования в формате RST.
    - Нет кода, который можно было бы рефакторить или улучшить, следуя инструкциям.

**Рекомендации по улучшению:**

1.  **Добавить код**: Необходимо добавить базовую реализацию игры на Python, которая будет соответствовать описанию.
2.  **Применить RST**: Все комментарии в коде должны быть переформатированы в reStructuredText (RST).
3.  **Использовать логирование**: Внедрить логирование ошибок с помощью `from src.logger.logger import logger`.
4.  **Использовать `j_loads`**:  Если потребуется загрузка данных из файла, использовать `j_loads` или `j_loads_ns`.
5.  **Структурировать код**: Использовать функции для разделения логики, например, для инициализации игры, хода игрока, проверки строки и подсчета голосов.
6.  **Документировать функции**: Добавить docstring в формате RST для всех функций и методов.
7.  **Обработка ошибок**: Использовать `logger.error` для обработки ошибок вместо стандартных `try-except`.

**Оптимизированный код:**

```python
"""
Модуль, описывающий правила и реализацию игры в поэзию.
=========================================================================================

Этот модуль содержит описание игры, ее правил и пример реализации на Python.
Игра позволяет пользователям по очереди добавлять строки к общему стихотворению.

Пример использования
--------------------

Пример запуска игры в поэзию:

.. code-block:: python

    poetry_game = PoetryGame()
    poetry_game.start_game()
"""
from typing import List
from src.logger.logger import logger # Добавлен импорт logger


class PoetryGame:
    """
    Класс, представляющий игру в поэзию.

    :ivar players: Список имен игроков.
    :vartype players: list
    :ivar poem: Список строк стихотворения.
    :vartype poem: list
    :ivar max_lines: Максимальное количество строк в стихотворении.
    :vartype max_lines: int
    """
    def __init__(self, max_lines: int = 4):
        """
        Инициализирует игру с заданным максимальным количеством строк.

        :param max_lines: Максимальное количество строк в стихотворении. По умолчанию 4.
        :type max_lines: int
        """
        self.players = []
        self.poem = []
        self.max_lines = max_lines

    def start_game(self):
        """
        Начинает игру, запрашивает имена игроков и запускает основной цикл игры.
        """
        print("Добро пожаловать в POETRY!")
        self._get_player_names()
        self._play_game()
        self._end_game()

    def _get_player_names(self):
        """
        Запрашивает имена игроков и сохраняет их в список.
        """
        while True: # Бесконечный цикл для запроса имен, пока не будет введено как минимум два имени
            try:
                num_players = int(input("Введите количество игроков (минимум 2): "))
                if num_players >= 2:
                   for i in range(num_players):
                       name = input(f"Игрок {i + 1}, введите ваше имя: ")
                       self.players.append(name)
                   break # Выход из цикла, если количество игроков корректно
                else:
                    print("Пожалуйста, введите число игроков не меньше 2.")
            except ValueError:
                print("Некорректный ввод. Введите целое число.")
                continue

    def _play_game(self):
        """
        Основной цикл игры, в котором игроки по очереди добавляют строки к стихотворению.
        """
        current_player_index = 0
        while len(self.poem) < self.max_lines:
            current_player = self.players[current_player_index]
            print(f"\n{current_player}, ваш ход.")
            line = input("Введите строку: ")
            if self._is_valid_line(line):
                self.poem.append(line)
                print("Строка добавлена.")
                self._display_poem()
                current_player_index = (current_player_index + 1) % len(self.players)
            else:
                print("Строка не соответствует правилам. Попробуйте снова.")

    def _is_valid_line(self, line: str) -> bool:
         """
         Проверяет, соответствует ли строка правилам (длина не более 50 символов).

         :param line: Строка для проверки.
         :type line: str
         :return: True, если строка соответствует правилам, False в противном случае.
         :rtype: bool
         """
         if len(line) > 50:
            logger.error(f"Длина строки превышает 50 символов: {line}") # Логирование ошибки, если строка слишком длинная
            return False
         return True

    def _display_poem(self):
        """
        Выводит текущее состояние стихотворения.
        """
        print("Текущее стихотворение:")
        for i, line in enumerate(self.poem):
            print(f"{i + 1}. {line}")

    def _end_game(self):
        """
        Завершает игру, объявляет стихотворение и предлагает игрокам проголосовать за лучшую строку.
        """
        print("\nСтихотворение завершено:")
        self._display_poem()
        self._vote_for_best_line()

        if self._play_again():
            self.__init__()
            self.start_game()
        else:
            print("Спасибо за игру!")

    def _vote_for_best_line(self):
         """
         Проводит голосование за лучшую строку и объявляет победителя.
         """
         votes = {}
         for player in self.players:
             while True:
                 try:
                     vote = int(input(f"{player}, проголосуйте за лучшую строку (введите номер): "))
                     if 1 <= vote <= len(self.poem):
                         votes[player] = vote
                         break
                     else:
                         print("Некорректный номер строки. Попробуйте снова.")
                 except ValueError:
                     print("Некорректный ввод. Введите целое число.")
         self._announce_winner(votes)


    def _announce_winner(self, votes: dict):
         """
         Подсчитывает голоса и объявляет победителя.

         :param votes: Словарь с голосами игроков, где ключ - имя игрока, а значение - номер выбранной строки.
         :type votes: dict
         """
         line_votes = {}
         for line_number in range(1, len(self.poem)+1):
            line_votes[line_number]=0
         for player, vote in votes.items():
            line_votes[vote] += 1
         winner_line = max(line_votes, key=line_votes.get)
         winner_count = line_votes[winner_line]
         winners = [player for player, vote in votes.items() if vote == winner_line]
         if len(winners) == 1:
            print(f"Победил {winners[0]} с строкой \"{self.poem[winner_line - 1]}\"")
         else:
            print(f"Победила строка \"{self.poem[winner_line - 1]}\" получив {winner_count} голоса ")


    def _play_again(self) -> bool:
        """
        Предлагает сыграть еще раз и возвращает True, если игрок хочет продолжить.

        :return: True, если игрок хочет сыграть снова, False в противном случае.
        :rtype: bool
        """
        while True:
            play_again = input("Хотите сыграть снова? (да/нет): ").lower()
            if play_again in ['да', 'нет']:
                return play_again == 'да'
            else:
                 print("Некорректный ввод. Введите 'да' или 'нет'.")


if __name__ == "__main__":
    poetry_game = PoetryGame()
    poetry_game.start_game()
```