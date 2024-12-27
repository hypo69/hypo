# Анализ кода модуля `38_even.ru.md`

**Качество кода**

- **Соответствие требованиям по оформлению кода:** 3/10
-  **Плюсы**
    - Текст хорошо структурирован, логично разделен на разделы и подразделы.
    - Описание игры и пошаговая инструкция понятны.
- **Минусы**
    - Файл представляет собой описание игры в формате markdown, а не код на Python.
    - Отсутствуют docstring и комментарии, соответствующие формату RST, так как это не код.
    - Не используются импорты, так как это не код.
    - Присутствует избыточное использование стандартных блоков `try-except` и отсутствует логирование ошибок, так как это не код.

**Рекомендации по улучшению**

1.  **Преобразование в исполняемый код:** Необходимо преобразовать текстовое описание игры в работающий код на Python.
2.  **Документирование кода:** Добавить docstring и комментарии в формате RST для всех функций, классов и переменных.
3.  **Логирование:** Использовать `from src.logger.logger import logger` для логирования ошибок и отладки.
4.  **Обработка ошибок:**  Обрабатывать ошибки с помощью `logger.error` вместо стандартных блоков `try-except` там, где это уместно.
5.  **Рефакторинг:** Улучшить структуру кода, разбив его на функции для лучшей читаемости и поддерживаемости.
6.  **Добавление функциональности:**  Реализовать возможность выбора уровня сложности, добавления счетчика раундов и сохранения результатов.

**Оптимизированный код**

```python
"""
Модуль для реализации игры EVEN (Игра на парность).
=========================================================================================

В этом модуле реализована логическая игра, в которой игрок и компьютер по очереди берут предметы из общей кучи.
Цель игры — оставить противнику чётное количество предметов после своего хода.

Пример использования
--------------------

.. code-block:: python

    game = EvenGame()
    game.start_game()
"""
import random
from src.logger.logger import logger  # Подключаем логер
from typing import List, Tuple


class EvenGame:
    """
    Класс для управления игрой EVEN.
    """

    def __init__(self, items_range: Tuple[int, int] = (10, 30)):
        """
        Инициализирует игру.

        :param items_range: Диапазон для генерации начального количества предметов.
        """
        self.items_range = items_range
        self.items_count = 0  # Количество предметов в куче
        self.player_wins = 0
        self.computer_wins = 0

    def _generate_items(self) -> None:
        """Генерирует случайное количество предметов в куче."""
        self.items_count = random.randint(*self.items_range)

    def _player_turn(self) -> bool:
        """
        Выполняет ход игрока.

        :return: True, если игрок победил, False в противном случае.
        """
        while True:
            try:
                player_choice = int(input(f"Введите количество предметов, которые вы хотите взять (1-3): "))
                if not 1 <= player_choice <= 3:
                    print("Некорректный ввод. Пожалуйста, введите число от 1 до 3.")
                    continue
                if player_choice > self.items_count:
                    print(
                        f"Некорректный ввод. Вы не можете взять {player_choice} предмета. В куче {self.items_count}."
                    )
                    continue
                break
            except ValueError:
                logger.error("Некорректный ввод. Введите целое число.")
                print("Некорректный ввод. Пожалуйста, введите целое число.")
                continue

        self.items_count -= player_choice
        print(f"Вы взяли {player_choice} предмета. Осталось {self.items_count} предметов.")

        if self.items_count % 2 != 0:
            print("Вы оставили компьютеру нечётное количество предметов!")
            self.computer_wins += 1
            return True
        return False

    def _computer_turn(self) -> bool:
        """
        Выполняет ход компьютера.

        :return: True, если компьютер победил, False в противном случае.
        """
        if self.items_count <= 0:
            print("Компьютер не может сделать ход, так как предметов не осталось.")
            return False
        if self.items_count % 2 == 0:
            computer_choice = random.randint(1, min(3, self.items_count)) # случайный ход
        else:
           computer_choice = 1 if self.items_count > 1 else 1 # компьютер забирает 1 предмет
        self.items_count -= computer_choice
        print(f"Компьютер взял {computer_choice} предмета. Осталось {self.items_count} предметов.")

        if self.items_count % 2 != 0:
            print("Компьютер оставил вам нечётное количество предметов!")
            self.player_wins += 1
            return True
        return False

    def _play_round(self) -> None:
        """Выполняет один раунд игры."""
        self._generate_items()
        print(f"В куче {self.items_count} предметов.")
        first_move = input("Хотите ходить первым? (да/нет): ").lower()

        game_over = False
        if first_move == "да":
            while not game_over:
                game_over = self._player_turn()
                if game_over:
                    print("Вы проиграли.")
                    break
                game_over = self._computer_turn()
                if game_over:
                    print("Вы победили.")
                    break
        elif first_move == "нет":
            while not game_over:
                game_over = self._computer_turn()
                if game_over:
                    print("Вы победили.")
                    break
                game_over = self._player_turn()
                if game_over:
                    print("Вы проиграли.")
                    break
        else:
            print("Некорректный ввод. Игра будет завершена.")

    def start_game(self) -> None:
        """Начинает новую игру."""
        print("Добро пожаловать в игру EVEN!")

        while True:
            self._play_round()
            print(f"Счёт: Игрок {self.player_wins} - Компьютер {self.computer_wins}")
            play_again = input("Хотите сыграть ещё раз? (да/нет): ").lower()
            if play_again != "да":
                print("Спасибо за игру!")
                break

if __name__ == "__main__":
    game = EvenGame()
    game.start_game()
```