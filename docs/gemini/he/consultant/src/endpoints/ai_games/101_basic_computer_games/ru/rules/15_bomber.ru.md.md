# Анализ кода модуля `15_bomber.ru.md`

**Качество кода**

*   **Соответствие требованиям к формату кода (1-10):** 1
    *   **Преимущества:**
        *   Документ содержит описание игры, пошаговую инструкцию и пример работы программы.
    *   **Недостатки:**
        *   Код не является исполняемым.
        *   Нет разделения на модули и функции.
        *   Не используются docstring.
        *   Формат файла не соответствует reStructuredText (RST).
        *   Нет обработки ошибок, импортов и т.д.
        *   Это не код на Python, а текстовое описание игры.

**Рекомендации по улучшению**

1.  **Преобразовать текстовое описание в исполняемый код Python.** Необходимо реализовать логику игры, включая выбор стороны, самолёта, цели, управление самолётом, бомбардировку и обработку победы/поражения.
2.  **Добавить docstring и аннотации типов.** Каждая функция, метод и класс должны иметь подробное описание в формате RST.
3.  **Использовать `src.utils.jjson` для загрузки данных.** Если необходима загрузка данных из файлов, следует использовать `j_loads` или `j_loads_ns`.
4.  **Добавить обработку ошибок.** Использовать `logger.error` для регистрации ошибок вместо стандартных блоков `try-except`.
5.  **Разделить код на модули и функции.** Это улучшит читаемость и поддерживаемость кода.
6.  **Реализовать класс для игры.** Это позволит удобно управлять состоянием игры и взаимодействиями между её компонентами.

**Улучшенный код**

```python
"""
Модуль для реализации игры "Бомбардировщик"
===========================================

Этот модуль содержит класс :class:`BomberGame` для управления игрой,
включая выбор стороны, самолета, миссии, а также обработку событий игры,
таких как бомбардировка и столкновения с врагом.

Пример использования:
---------------------

.. code-block:: python

    game = BomberGame()
    game.start_game()
"""

from typing import List, Dict, Any
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_loads_ns  # Импорт функций j_loads и j_loads_ns из src.utils.jjson #
import random # Импорт модуля random

class BomberGame:
    """
    Класс для управления игрой "Бомбардировщик".

    :ivar sides: Список доступных сторон для выбора.
    :vartype sides: List[str]
    :ivar aircrafts: Словарь доступных самолётов и их характеристик.
    :vartype aircrafts: Dict[str, Dict[str, Any]]
    :ivar mission_targets: Список возможных целей миссий.
    :vartype mission_targets: List[str]
    :ivar player_side: Сторона, выбранная игроком.
    :vartype player_side: str
    :ivar player_aircraft: Самолёт, выбранный игроком.
    :vartype player_aircraft: str
    :ivar current_target: Текущая цель миссии.
    :vartype current_target: str
    :ivar bombs: Количество бомб у игрока.
    :vartype bombs: int
    :ivar is_game_over: Флаг, определяющий завершена ли игра.
    :vartype is_game_over: bool
    """

    def __init__(self) -> None:
        """
        Инициализация игры. Устанавливает начальные параметры и значения переменных.
        """
        self.sides: List[str] = ["Италия", "Союзники", "Япония", "Германия"]
        self.aircrafts: Dict[str, Dict[str, Any]] = {
            "B-29": {"bombs": 10, "speed": 8},
            "Lancaster": {"bombs": 8, "speed": 7},
            "B-17": {"bombs": 9, "speed": 6},
        }
        self.mission_targets: List[str] = ["Плоешти", "Берлин", "Токио"]
        self.player_side: str = ""
        self.player_aircraft: str = ""
        self.current_target: str = ""
        self.bombs: int = 0
        self.is_game_over: bool = False

    def _display_menu(self, options: List[str], prompt: str) -> int:
        """
        Отображает меню с заданными вариантами выбора.
    
        :param options: Список вариантов выбора.
        :type options: List[str]
        :param prompt: Текст приглашения к вводу.
        :type prompt: str
        :return: Выбранный индекс варианта.
        :rtype: int
        """
        print(prompt)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        while True:
            try:
                choice = int(input("> "))
                if 1 <= choice <= len(options):
                    return choice
                else:
                    print("Неверный ввод. Попробуйте еще раз.")
            except ValueError:
                print("Неверный ввод. Введите число.")

    def _select_side(self) -> None:
        """
        Позволяет игроку выбрать сторону.
        """
        choice = self._display_menu(self.sides, "Выберите свою сторону:")
        self.player_side = self.sides[choice - 1]
        print(f"Вы выбрали {self.player_side}.")

    def _select_aircraft(self) -> None:
        """
        Позволяет игроку выбрать самолет.
        """
        aircraft_names = list(self.aircrafts.keys())
        choice = self._display_menu(aircraft_names, "Выберите тип самолета:")
        self.player_aircraft = aircraft_names[choice - 1]
        print(f"Вы выбрали {self.player_aircraft}.")
        self.bombs = self.aircrafts[self.player_aircraft]["bombs"]

    def _select_target(self) -> None:
        """
        Позволяет игроку выбрать цель миссии.
        """
        self.current_target = random.choice(self.mission_targets)
        print(f"Вашей целью будет бомбардировка {self.current_target}.")

    def _simulate_flight(self) -> bool:
        """
        Моделирует полет, включая возможные столкновения и бомбардировку.
    
        :return: True, если миссия успешна, False в противном случае.
        :rtype: bool
        """
        print("Вы преодолели вражеские зенитные огни. Цель достигнута!")
        print("Подготовьтесь к сбросу бомб!")
        if random.random() > 0.2: # Шанс успеха 80% #
            print("Вы успешно разрушили цель.")
            return True
        else:
            print("Ваш самолет был поврежден вражеским огнем!")
            return False

    def _handle_mission_result(self, success: bool) -> None:
        """
        Обрабатывает результат миссии и выводит соответствующее сообщение.
    
        :param success: True, если миссия успешна, False в противном случае.
        :type success: bool
        """
        if success:
            print("Вы успешно завершили миссию! Ваш самолет возвращается на базу.")
        else:
            print("Вы были сбиты вражескими силами.")
            print("Пожалуйста, попробуйте снова.")
            self.is_game_over = True # Игра завершается, если миссия не удалась

    def _play_again(self) -> bool:
        """
        Предлагает игроку сыграть снова.
    
        :return: True, если игрок хочет сыграть снова, False в противном случае.
        :rtype: bool
        """
        while True:
            play_again = input("Хотите сыграть снова? (да/нет)\n> ").lower()
            if play_again in ["да", "нет"]:
                return play_again == "да"
            else:
                print("Неверный ввод. Пожалуйста, введите 'да' или 'нет'.")

    def start_game(self) -> None:
        """
        Начинает игру "Бомбардировщик".
        """
        print("Добро пожаловать в BOMBER!")
        while not self.is_game_over:
            self._select_side()
            self._select_aircraft()
            self._select_target()
            mission_success = self._simulate_flight()
            self._handle_mission_result(mission_success)

            if self.is_game_over: # Если игрок проиграл, игра завершается
                break # выходим из цикла, не предлагая играть еще раз
            
            if not self._play_again(): # Если игрок не хочет играть снова, игра завершается
                print("До свидания!")
                self.is_game_over = True # Устанавливаем флаг завершения игры

if __name__ == "__main__":
    game = BomberGame()
    game.start_game()
```