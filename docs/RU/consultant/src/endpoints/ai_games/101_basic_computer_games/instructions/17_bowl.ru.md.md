# Анализ кода модуля `17_bowl.ru.md`

**Качество кода**
9
 - Плюсы
    - Документ подробно описывает правила игры в боулинг, шаги реализации, пример работы программы, ограничения и реализацию.
    - Описаны все важные аспекты игры: инициализация, основной цикл, типы бросков, подсчет победителя и завершение игры.
    - Приведены примеры ввода-вывода, что помогает понять, как должна работать программа.
- Минусы
    - Отсутствует код, есть только описание.
    - Нет документации в формате reStructuredText (RST).
    - Нет логирования ошибок.
    - Нет обработки ввода пользователя.
    - Нет импортов.

**Рекомендации по улучшению**

1.  **Добавить reStructuredText (RST) документацию:** Переписать все комментарии в формате RST, включая описание модуля, функций, методов и переменных, используя docstring.
2.  **Реализовать код:** На основе описания реализовать код игры в боулинг.
3.  **Добавить логирование:** Использовать `from src.logger.logger import logger` для логирования ошибок и других важных событий.
4.  **Обработка ошибок:** Избегать `try-except` блоков без крайней необходимости, использовать `logger.error` для обработки ошибок.
5.  **Обработка пользовательского ввода:** Добавить проверку ввода пользователя и обработку некорректных данных.
6.  **Добавить импорты:** Импортировать необходимые модули (например, `random` для имитации бросков, `src.utils.jjson` для загрузки данных).
7.  **Функции и классы:** Разбиение кода на функции и классы для более структурированной разработки.

**Оптимизированный код**

```markdown
# Анализ игры BOWL

## Основные требования:

## Output Language: RU (Русский)

1. **Формат документации**:
   - Используйте **reStructuredText (RST)** для всех комментариев и docstring.
   - Всегда используйте одинарные кавычки (`'`) в Python коде.

2. **Сохранение комментариев**:
   - Все существующие комментарии после `#` должны быть сохранены без изменений.
   - Блоки кода, которые необходимо изменить, должны быть прокомментированы построчно с использованием символа `#`.

3. **Обработка данных**:
   - Используйте `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.load` для чтения файлов.
   - Оставляйте любые `...` в коде без изменений как точки остановки.

4. **Анализ структуры**:
   - Проверьте и добавьте отсутствующие импорты в код.
   - Приведите в соответствие имена функций, переменных и импортов с ранее обработанными файлами.

5. **Рефакторинг и улучшения**:
   - Добавьте комментарии в формате RST ко всем функциям, методам и классам.
   - Используйте `from src.logger.logger import logger` для логирования ошибок.
   - Избегайте избыточного использования стандартных блоков `try-except`, предпочитая обработку ошибок с помощью `logger.error`.
   - В комментариях избегайте слов 'получаем', 'делаем' и подобных. Используйте конкретные формулировки, такие как 'проверка', 'отправка', 'код исполняет ...'.

6. **Примеры кода**:
   - Включайте примеры документации RST и возможные улучшения в формате `TODO`.
    - Документация должна соответствовать стандартам оформления docstring в Python (например, для Sphinx).

7. **Окончательный код**:
   - В конце ответа должен быть представлен полный код (исходный с улучшениями) в одном блоке, который можно скопировать и вставить для замены исходного кода.
   - Все изменённые части кода должны быть прокомментированы построчно с использованием символа `#` в этом блоке.

8.  **Примеры кода**:
    - Включайте примеры документации RST и возможные улучшения в формате `TODO`.

9. **Дополнительная инструкция**:
   - Все комментарии к модулям, функциям, методам и переменным должны быть переписаны в формате reStructuredText (RST). Это включает:
        - Описание модуля в начале файла.
        - Документацию для каждой функции, метода и переменной.
        - Соблюдение стандартов оформления docstring в Python (например, для Sphinx).
        - В комментариях после `#` строки должны содержать подробное объяснение следующего за ними блока кода.

```python
"""
Модуль для симуляции игры в боулинг.
=====================================================

Этот модуль реализует игру в боулинг для одного или нескольких игроков.
Используются стандартные правила боулинга, где каждый игрок
выполняет 10 фреймов, и его задача — сбить все 10 кеглей за два броска.

Пример использования
--------------------

Пример запуска игры:

.. code-block:: python

   game = BowlingGame()
   game.start_game()

"""
import random
from src.logger.logger import logger
from typing import List, Dict
# from src.utils.jjson import j_loads_ns # TODO: При необходимости использовать этот импорт


class BowlingGame:
    """
    Класс для управления игрой в боулинг.

    :ivar players_count: Количество игроков в игре.
    :vartype players_count: int
    :ivar players_scores: Словарь, содержащий счет каждого игрока.
    :vartype players_scores: dict[int, list[int]]
    :ivar current_player: Номер текущего игрока.
    :vartype current_player: int
    :ivar frame: Текущий фрейм игры.
    :vartype frame: int
    """

    def __init__(self):
        """
        Инициализирует игру в боулинг.
        """
        self.players_count = 0
        self.players_scores = {}
        self.current_player = 1
        self.frame = 1
        self.pins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] # 1 - кегля стоит, 0 - кегля сбита.

    def _display_pins(self) -> str:
        """
        Формирует строку для отображения оставшихся кеглей.

        :return: Строка с представлением кеглей.
        :rtype: str
        """
        return ' '.join(['+' if pin else '0' for pin in self.pins])
        # Код формирует строку из оставшихся кеглей, заменяя 1 на '+' и 0 на '0'

    def _roll(self) -> int:
        """
        Имитирует бросок мяча, сбивая случайное количество кеглей.

        :return: Количество сбитых кеглей.
        :rtype: int
        """
        # Генерирует случайное количество сбитых кеглей
        pins_down = random.randint(0, sum(self.pins))
        knocked_pins_indices = random.sample([i for i, pin in enumerate(self.pins) if pin], pins_down)
        for index in knocked_pins_indices:
            self.pins[index] = 0
        return pins_down
        # Код генерирует случайное количество сбитых кеглей, и изменяет состояние кеглей

    def _reset_pins(self) -> None:
        """
        Сбрасывает все кегли в начальное положение.
        """
        self.pins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        # Код сбрасывает все кегли в начальное положение (все стоят)

    def _check_result(self, pins_down: int, second_roll: bool = False) -> str:
        """
        Анализирует результат броска и возвращает его тип.

        :param pins_down: Количество сбитых кеглей.
        :type pins_down: int
        :param second_roll: Флаг, указывающий, что это второй бросок в фрейме.
        :type second_roll: bool
        :return: Тип результата броска ('GUTTER', 'STRIKE', 'SPARE', 'ERROR').
        :rtype: str
        """
        if pins_down == 0:
            return 'GUTTER'
        elif sum(self.pins) == 0 and not second_roll:
            return 'STRIKE'
        elif sum(self.pins) == 0 and second_roll:
            return 'SPARE'
        else:
            return 'ERROR'
        # Код проверяет и возвращает результат броска (GUTTER, STRIKE, SPARE, ERROR)

    def _switch_player(self) -> None:
        """
        Переключает ход на следующего игрока.
        """
        self.current_player += 1
        if self.current_player > self.players_count:
            self.current_player = 1
            self.frame += 1
        # Код переключает ход на следующего игрока или на следующий фрейм

    def _add_score(self, score: int) -> None:
         """
         Добавляет очки игроку за текущий фрейм.

         :param score: Количество набранных очков.
         :type score: int
        """
         self.players_scores[self.current_player].append(score)
        # Код добавляет очки текущему игроку в его список очков

    def _get_final_scores(self) -> dict[int, int]:
      """
      Вычисляет итоговый счет для каждого игрока.

      :return: Словарь с итоговым счетом каждого игрока.
      :rtype: dict[int, int]
      """
      final_scores = {}
      for player, scores in self.players_scores.items():
            final_scores[player] = sum(scores)
      return final_scores
      # Код вычисляет и возвращает итоговый счет для каждого игрока

    def _get_winner(self, final_scores: dict[int, int]) -> int:
        """
        Определяет победителя игры.

        :param final_scores: Словарь с итоговыми очками каждого игрока.
        :type final_scores: dict[int, int]
        :return: Номер игрока-победителя.
        :rtype: int
        """
        return max(final_scores, key=final_scores.get)
        # Код определяет и возвращает номер игрока-победителя

    def start_game(self) -> None:
        """
        Запускает игру в боулинг.
        """
        print("Добро пожаловать в боулинг!")
        while True:
            try:
                self.players_count = int(input("Сколько игроков участвуют? (1-4)\n> "))
                if 1 <= self.players_count <= 4:
                    break
                else:
                    logger.error(f'Некорректное количество игроков {self.players_count}')
                    print("Пожалуйста, введите число от 1 до 4.")
            except ValueError:
                logger.error('Введено некорректное значение для количества игроков')
                print("Пожалуйста, введите число.")
            # Код запрашивает ввод количества игроков и проверяет его корректность

        self.players_scores = {i: [] for i in range(1, self.players_count + 1)}
        # Код инициализирует список очков для каждого игрока
        while self.frame <= 10:
            print(f"Игрок {self.current_player}, ваш ход.")
            self._reset_pins()
            first_roll_pins = self._roll()
            print(f"Оставшиеся кегли: {self._display_pins()}")
            first_roll_result = self._check_result(first_roll_pins)
            print(f"Результат: {first_roll_result}!")
            self._add_score(first_roll_pins)
            if first_roll_result != 'STRIKE':
                second_roll_pins = self._roll()
                print(f"Оставшиеся кегли: {self._display_pins()}")
                second_roll_result = self._check_result(second_roll_pins, True)
                print(f"Результат: {second_roll_result}!")
                self._add_score(second_roll_pins)

            self._switch_player()
            # Код реализует один фрейм игры

        final_scores = self._get_final_scores()
        for player, score in final_scores.items():
            print(f"Итоговый счёт игрока {player}: {score}")
        winner = self._get_winner(final_scores)
        print(f"Победил игрок {winner}!")
        # Код выводит итоговые результаты и объявляет победителя

        while True:
          play_again = input("Хотите сыграть снова? (да/нет)\n> ").lower()
          if play_again in ['да', 'нет']:
            break
          else:
              logger.error(f'Некорректный ввод ответа на повтор игры: {play_again}')
              print('Пожалуйста, введите "да" или "нет".')
              # Код запрашивает у игрока повторить игру или нет

        if play_again == 'да':
            self.__init__()
            self.start_game()
            # Код запускает новую игру, если игрок ответил 'да'
        else:
            print("До свидания!")
            # Код завершает игру, если игрок ответил 'нет'

if __name__ == '__main__':
    game = BowlingGame()
    game.start_game()
    # Код запускает игру при запуске скрипта

```