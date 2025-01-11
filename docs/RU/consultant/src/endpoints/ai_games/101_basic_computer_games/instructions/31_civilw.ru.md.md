# Анализ кода модуля `31_civilw.ru.md`

**Качество кода**
7
- Плюсы
    - Описание игры и пошаговая инструкция четко структурированы, что облегчает понимание логики игры.
    - Приведен пример работы программы, который помогает понять игровой процесс.
    - Указаны возможные ограничения, что полезно для понимания рамок игры.
- Минусы
    - Отсутствует код, только описание и инструкция.
    - Не соблюдены требования к оформлению: нет RST, не описаны функции, не добавлены комментарии в стиле reStructuredText, нет импортов и т.д.
    - Не указана обработка ошибок.

**Рекомендации по улучшению**

1.  **Добавить код игры:** Необходимо реализовать игру на Python, опираясь на предоставленные инструкции.
2.  **Применить reStructuredText (RST):** Оформить все комментарии и документацию в формате RST.
3.  **Использовать `j_loads` или `j_loads_ns`:** При чтении данных из файлов использовать функции `j_loads` или `j_loads_ns` из `src.utils.jjson`.
4.  **Добавить импорты:** Добавить все необходимые импорты для работы программы, такие как `random` и `json`.
5.  **Логирование ошибок:**  Использовать `from src.logger.logger import logger` для логирования ошибок, избегая избыточных try-except блоков.
6.  **Документирование функций:** Добавить docstrings в формате RST для каждой функции, объясняющие назначение, параметры и возвращаемые значения.
7.  **Обработка ввода:** Добавить обработку ввода пользователя для предотвращения ошибок.
8.  **Структура игры:** Создать классы и функции для логической организации игры, такие как `Game`, `Battle`, `Player`, `Computer`, `Strategy`.
9.  **Улучшить описание:** Улучшить описание и инструкцию, добавив более точные описания стратегий и их влияния на игровой процесс.
10. **Расширить возможности:** Ввести более сложные стратегии, добавить разнообразие вариантов для игрока, а также добавить исторические справки по каждой битве.

**Оптимизированный код**

```python
"""
Модуль, реализующий игру "Гражданская война" (CIVILW).
=======================================================

Этот модуль предоставляет симуляцию сражений Гражданской войны США.

Игра основана на 14 реальных сражениях, используя исторические факты и цифры.

Пример использования
--------------------

.. code-block:: python

   from src.games.civil_war import CivilWarGame

   game = CivilWarGame()
   game.start_game()
"""

import random
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger
# from typing import List, Dict, Any
# TODO: import enum


class Strategy:
    """
    Класс, представляющий стратегию в игре.

    :param name: Название стратегии.
    :param description: Описание стратегии.
    :param impact: Воздействие стратегии на результат битвы.
    """
    def __init__(self, name: str, description: str, impact: float):
        self.name = name
        self.description = description
        self.impact = impact

    def __repr__(self):
        return f"{self.name}"

class Battle:
    """
    Класс, представляющий битву в игре.

    :param name: Название битвы.
    :param confederate_losses: Реальные потери конфедератов в битве.
    :param union_losses: Реальные потери союза в битве.
    :param strategies: Словарь доступных стратегий.
    """
    def __init__(self, name: str, confederate_losses: int, union_losses: int, strategies: dict):
        self.name = name
        self.confederate_losses = confederate_losses
        self.union_losses = union_losses
        self.strategies = strategies

    def __repr__(self):
        return f"{self.name}"

class Player:
    """
    Класс, представляющий игрока.

    :param name: Имя игрока.
    :param losses: Количество потерь игрока.
    """
    def __init__(self, name: str):
        self.name = name
        self.losses = 0

    def choose_strategy(self, battle: Battle) -> Strategy:
        """
        Позволяет игроку выбрать стратегию.

        :param battle: Текущая битва.
        :return: Выбранная игроком стратегия.
        """
        print('Выберите стратегию:')
        for i, strategy in enumerate(battle.strategies):
            print(f'{i + 1}. {strategy}')
        while True:
            try:
                choice = int(input("> "))
                if 1 <= choice <= len(battle.strategies):
                    return list(battle.strategies.values())[choice - 1]
                else:
                     print('Неверный выбор. Попробуйте еще раз.')
            except ValueError:
                 print('Неверный ввод. Введите число.')

    def report_losses(self, losses: int):
        """
        Обновляет и сообщает потери игрока.

        :param losses: Количество потерь в текущей битве.
        """
        self.losses += losses
        print(f'Ваши потери в этой битве: {losses} человек.')
        print(f'Общие потери: {self.losses}')

class Computer:
    """
    Класс, представляющий компьютерного противника.

    :param name: Имя компьютера.
    :param losses: Количество потерь компьютера.
    """
    def __init__(self, name: str):
        self.name = name
        self.losses = 0

    def choose_strategy(self, battle: Battle) -> Strategy:
        """
         Выбирает стратегию компьютера случайным образом.

        :param battle: Текущая битва.
        :return: Выбранная компьютером стратегия.
        """
        return random.choice(list(battle.strategies.values()))

    def report_losses(self, losses: int):
        """
        Обновляет и сообщает потери компьютера.

        :param losses: Количество потерь в текущей битве.
        """
        self.losses += losses
        print(f'Потери противника: {losses} человек.')
        print(f'Общие потери противника: {self.losses}')

class CivilWarGame:
    """
    Класс, управляющий ходом игры "Гражданская война".

    Содержит логику для выбора битвы, определения победителя, и перезапуска игры.
    """
    def __init__(self):
        """
        Инициализирует игру, загружает данные из файла и создает экземпляры Player и Computer.
        """
        try:
            # Загрузка данных из файла battle_data.json.
            self.battle_data = j_loads_ns('hypotez/src/endpoints/ai_games/101_basic_computer_games/instructions/battle_data.json')
        except Exception as e:
            logger.error(f"Ошибка при загрузке данных битвы: {e}")
            self.battle_data = {}
        self.player = Player(name="Конфедерация")
        self.computer = Computer(name="Союз")
        self.battles = self._prepare_battles()

    def _prepare_battles(self) -> list:
        """
        Подготавливает список объектов Battle на основе загруженных данных.

        :return: Список подготовленных битв.
        """
        battles = []
        for battle_data in self.battle_data.get("battles", []):
           strategies = {
               strategy['name']: Strategy(strategy['name'], strategy['description'], strategy['impact'])
               for strategy in battle_data.get('strategies',[])
           }
           battle = Battle(
               name = battle_data['name'],
               confederate_losses = battle_data['confederate_losses'],
               union_losses = battle_data['union_losses'],
               strategies = strategies
           )
           battles.append(battle)
        return battles

    def start_game(self):
        """
        Запускает основной игровой цикл.

        Включает выбор битвы, выбор стратегий игроком и компьютером, подсчет потерь и определение победителя.
        """
        print("Добро пожаловать в игру CIVILW!")
        while True:
             for battle in self.battles:
                print(f"\nБитва начинается: {battle.name}")
                player_strategy = self.player.choose_strategy(battle)
                computer_strategy = self.computer.choose_strategy(battle)
                print(f"Вы выбрали стратегию: {player_strategy}")
                print(f"Противник выбрал стратегию: {computer_strategy}")
                self._simulate_battle(battle, player_strategy, computer_strategy)

                if self.player.losses > self.computer.losses:
                     print("Вы проиграли эту битву!")
                else:
                    print("Вы выиграли эту битву!")

             if not self.play_again():
                 break
        print("Спасибо за игру!")

    def _simulate_battle(self, battle: Battle, player_strategy: Strategy, computer_strategy: Strategy):
        """
        Моделирует битву, рассчитывая потери на основе выбранных стратегий.

        :param battle: Текущая битва.
        :param player_strategy: Стратегия, выбранная игроком.
        :param computer_strategy: Стратегия, выбранная компьютером.
        """
        # Код исполняет расчет потерь с учетом выбранных стратегий.
        player_losses = int(battle.confederate_losses * player_strategy.impact)
        computer_losses = int(battle.union_losses * computer_strategy.impact)
        self.player.report_losses(player_losses)
        self.computer.report_losses(computer_losses)

    def play_again(self) -> bool:
        """
        Предлагает игроку сыграть еще раз.

        :return: True, если игрок хочет сыграть еще раз, иначе False.
        """
        while True:
            play_again = input("Хотите сыграть снова? (да/нет) ").lower()
            if play_again in ["да", "нет"]:
                return play_again == "да"
            else:
                print("Неверный ввод. Пожалуйста, введите 'да' или 'нет'.")

if __name__ == "__main__":
    """
    Точка входа в программу.

    Создает экземпляр игры CivilWarGame и запускает её.
    """
    game = CivilWarGame()
    game.start_game()
```
```json
{
  "battles": [
    {
      "name": "Битва при Булл-Ран",
      "confederate_losses": 1982,
      "union_losses": 2896,
       "strategies": [
         {
           "name": "Артиллерийская атака",
           "description": "Атака артиллерией",
            "impact": 0.8
          },
          {
           "name": "Укрепления против фронтальной атаки",
            "description": "Укрепления против фронтальной атаки",
            "impact": 0.6
          },
          {
           "name": "Укрепления против фланговых маневров",
            "description": "Укрепления против фланговых маневров",
             "impact": 0.7
          },
          {
            "name": "Отступление",
            "description": "Отступление",
             "impact": 0.3
          }
       ]
    },
    {
      "name": "Битва при Шайло",
      "confederate_losses": 10699,
      "union_losses": 13047,
         "strategies": [
         {
           "name": "Артиллерийская атака",
           "description": "Атака артиллерией",
            "impact": 0.9
          },
          {
           "name": "Прямой удар",
            "description": "Прямой удар",
             "impact": 1
          },
          {
           "name": "Маневры по флангу",
             "description": "Маневры по флангу",
              "impact": 0.8
          },
          {
            "name": "Окружение",
            "description": "Окружение",
             "impact": 1.2
          }
       ]
    }
  ]
}
```