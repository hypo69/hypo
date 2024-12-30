# Анализ кода модуля 65_nim.ru.md

**Качество кода**

- Соответствие требованиям к формату кода (1-10):
    -   **Преимущества**:
        -   Документ содержит подробное описание игры NIM, включая правила, пошаговую инструкцию, пример работы программы, возможные ограничения, рекомендации по реализации и рекомендуемые улучшения.
        -   Структура документа хорошо организована и легко читается, что облегчает понимание логики игры и процесса ее разработки.
    -   **Недостатки**:
        -   В документе отсутствует программный код на Python, что затрудняет проверку соответствия принципам написания кода.
        -   Использование только Markdown затрудняет автоматическую проверку документа на соответствие стандартам reStructuredText (RST) для комментариев и docstring.

**Рекомендации по улучшению**

1.  **Добавление программного кода**: Реализовать игру NIM на Python, следуя инструкциям, описанным в документе. Это позволит оценить соответствие кода стандартам и предложить улучшения.
2.  **Использование reStructuredText**: Заменить Markdown на reStructuredText для комментариев и docstring в коде Python.
3.  **Улучшение структуры кода**: Разделить код на функции и классы для улучшения читаемости и повторного использования кода.
4.  **Добавление обработки ошибок**: Включить обработку ошибок при вводе данных пользователем (например, некорректные номера куч или количества камней).
5.  **Добавление логирования**: Использовать `src.logger.logger` для логирования ошибок и других важных событий.

**Улучшенный код**

```python
"""
Модуль для реализации игры NIM.
=========================================================================================

Этот модуль содержит реализацию классической стратегической игры NIM для двух игроков.
Игроки по очереди забирают камни из куч, и цель игры - заставить противника взять последний камень.

Пример использования
--------------------

Пример запуска игры:

.. code-block:: python

    if __name__ == '__main__':
        nim_game = NimGame()
        nim_game.start_game()
"""
from typing import List, Tuple
import random
from src.utils.jjson import j_loads, j_loads_ns  # импортируем j_loads
from src.logger.logger import logger # импортируем logger

class NimGame:
    """
    Реализует игру NIM.

    :ivar player1_name: Имя первого игрока.
    :vartype player1_name: str
    :ivar player2_name: Имя второго игрока.
    :vartype player2_name: str
    :ivar heaps: Состояние куч с камнями.
    :vartype heaps: list[int]
    :ivar current_player: Имя текущего игрока.
    :vartype current_player: str
    """
    def __init__(self):
        """
        Инициализирует игру, устанавливает начальные параметры.
        """
        self.player1_name: str = ''
        self.player2_name: str = ''
        self.heaps: List[int] = []
        self.current_player: str = ''

    def _get_player_names(self) -> Tuple[str, str]:
        """
        Получает имена игроков через ввод пользователя.

        :return: Кортеж с именами игроков.
        :rtype: tuple[str, str]
        """
        player1_name = input("Введите имя Игрока 1: ")
        player2_name = input("Введите имя Игрока 2: ")
        return player1_name, player2_name

    def _initialize_heaps(self) -> None:
        """
        Инициализирует кучи с камнями случайным образом.
        """
        num_heaps = random.randint(3, 5)
        self.heaps = [random.randint(5, 15) for _ in range(num_heaps)]

    def _display_heaps(self) -> None:
        """
        Выводит текущее состояние куч.
        """
        print("Текущее состояние куч:")
        for i, stones in enumerate(self.heaps):
            print(f"Куча {i + 1}: {stones} камней")

    def _get_player_move(self) -> Tuple[int, int]:
        """
        Получает ход игрока (номер кучи и количество камней).

        :return: Кортеж с номером кучи и количеством камней.
        :rtype: tuple[int, int]
        """
        while True:
            try:
                heap_num = int(input(f"{self.current_player}, введите номер кучи: ")) - 1
                stones_to_take = int(input(f"Введите количество камней: "))
                if 0 <= heap_num < len(self.heaps) and stones_to_take > 0 and stones_to_take <= self.heaps[heap_num]:
                    return heap_num, stones_to_take
                else:
                    logger.error("Некорректный ввод. Пожалуйста, попробуйте еще раз.")
                    print("Ошибка! Некорректный ввод. Попробуйте снова.")
            except ValueError:
                    logger.error("Некорректный ввод. Пожалуйста, введите число.")
                    print("Ошибка! Пожалуйста, введите число.")


    def _update_heaps(self, heap_num: int, stones_to_take: int) -> None:
         """
        Обновляет состояние куч после хода игрока.

         :param heap_num: Номер кучи, из которой берутся камни.
         :type heap_num: int
         :param stones_to_take: Количество камней, которое нужно взять.
         :type stones_to_take: int
         """
         self.heaps[heap_num] -= stones_to_take

    def _check_game_over(self) -> bool:
         """
        Проверяет, окончена ли игра (нет камней).

         :return: True, если игра окончена, False в противном случае.
         :rtype: bool
         """
         return all(stones == 0 for stones in self.heaps)

    def _switch_player(self) -> None:
        """
        Переключает текущего игрока.
        """
        self.current_player = self.player2_name if self.current_player == self.player1_name else self.player1_name

    def start_game(self) -> None:
        """
        Запускает игру NIM.
        """
        print("Добро пожаловать в NIM!")
        self.player1_name, self.player2_name = self._get_player_names()
        self._initialize_heaps()
        self.current_player = self.player1_name
        print("Игра начинается!")
        while True:
            self._display_heaps()
            heap_num, stones_to_take = self._get_player_move()
            self._update_heaps(heap_num, stones_to_take)
            if self._check_game_over():
                print(f"Игрок {self.current_player} взял последний камень.")
                self._switch_player() # Переключаемся на другого игрока, который не брал последний камень.
                print(f"Победитель: {self.current_player}! Поздравляем!")
                break
            self._switch_player()

if __name__ == '__main__':
    nim_game = NimGame() # создаем экземпляр класса NimGame
    nim_game.start_game() # запускаем игру