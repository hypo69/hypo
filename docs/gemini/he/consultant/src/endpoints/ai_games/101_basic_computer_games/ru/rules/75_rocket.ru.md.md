# Анализ кода модуля `75_rocket.ru.md`

**Качество кода**

- **Соответствие требованиям к формату кода (1-10):**
    -   **Преимущества:**
        -   Документ хорошо структурирован, использует Markdown для разделения разделов и подзаголовков.
        -   Представлены чёткие инструкции по реализации игры.
        -   Содержатся примеры работы программы и возможные ограничения.
        -   Предложены рекомендации по улучшениям.
    -   **Недостатки:**
        -   Это Markdown-документ, а не код Python, поэтому большая часть требований не применима.
        -   Не хватает кода реализации игры на Python.
        -   Нет обработки ошибок или логирования.

**Рекомендации по улучшению**

1.  **Реализовать игру на Python:** Необходимо создать код на Python, реализующий описанные в документе правила игры.
2.  **Добавить функции:** Разбить код на функции для инициализации игры, обработки ходов игроков, проверки победы и т. д.
3.  **Обработка ошибок:** Добавить обработку ошибок, например, при неверном вводе пользователя.
4.  **Логирование:** Использовать `src.logger.logger` для записи ошибок и отладочной информации.
5.  **Документация:**  Добавить reStructuredText (RST) docstrings для всех функций и классов, если будут таковые.
6.  **Учесть требования** по использованию `j_loads` или `j_loads_ns`, хотя в данном случае это не требуется.
7. **Использовать константы:** Заменить "магические" числа (размер сетки, количество ходов) на именованные константы.
8. **Соблюдение стиля:** Код должен соответствовать PEP 8.

**Улучшенный код**

```python
"""
Модуль реализует игру "Ракета".
=========================================================================================

Игра, где два игрока управляют ракетами, цель - первым достичь орбиты планеты.

Пример использования
--------------------
.. code-block:: python

    game = RocketGame()
    game.start()
"""
import random # Добавлен импорт random
from typing import Tuple # Добавлен импорт Tuple
from src.logger.logger import logger  # Добавлен импорт logger

GRID_SIZE = 10 # Размер игровой сетки
MAX_TURNS = 20 # Максимальное количество ходов
ASTEROIDS_COUNT = 15 # Количество астероидов

class RocketGame:
    """
    Класс для управления игровой логикой ракетной игры.
    """

    def __init__(self):
        """
        Инициализирует игровое поле, начальные позиции ракет и препятствия.
        """
        self.grid = [['[ ]' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.player1_pos = (0, 0)  # Начальная позиция игрока 1
        self.player2_pos = (GRID_SIZE - 1, GRID_SIZE - 1)  # Начальная позиция игрока 2
        self.grid[self.player1_pos[0]][self.player1_pos[1]] = '[R1]' # Установка ракеты 1 на поле
        self.grid[self.player2_pos[0]][self.player2_pos[1]] = '[R2]' # Установка ракеты 2 на поле
        self.asteroids = self._generate_asteroids() # Генерация астероидов
        self.current_player = 1 # Текущий игрок
        self.turns_count = 0 # Количество ходов

    def _generate_asteroids(self) -> list[tuple[int, int]]:
         """
         Генерирует случайные позиции астероидов на игровом поле.

         :return: Список кортежей с координатами астероидов.
         """
         asteroids = []
         while len(asteroids) < ASTEROIDS_COUNT:
            x = random.randint(0, GRID_SIZE - 1)
            y = random.randint(0, GRID_SIZE - 1)
            if (x, y) not in [self.player1_pos, self.player2_pos] and (x, y) not in asteroids:
                asteroids.append((x, y))
                self.grid[x][y] = '[A]' # Установка астероида на поле
         return asteroids

    def print_grid(self) -> None:
        """
        Выводит текущее состояние игрового поля в консоль.
        """
        print("  " + " ".join(chr(ord('A') + i) for i in range(GRID_SIZE))) # Вывод заголовка
        for i, row in enumerate(self.grid): # Итерация по строкам поля
            print(f'{i+1:2} {" ".join(row)}') # Вывод строк поля

    def _is_valid_move(self, new_pos: tuple[int, int]) -> bool:
        """
         Проверяет, является ли ход допустимым.

         :param new_pos: Кортеж с координатами новой позиции ракеты.
         :return: True, если ход допустим, False иначе.
         """
        x, y = new_pos # Распаковка координат
        if not (0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE): # Проверка выхода за границы поля
            return False
        if self.grid[x][y] == '[A]': # Проверка на наличие астероида в целевой клетке
           return False
        if self.current_player == 1 and (x, y) == self.player2_pos: # Проверка на наличие другой ракеты
            return False
        if self.current_player == 2 and (x, y) == self.player1_pos: # Проверка на наличие другой ракеты
            return False

        return True

    def _get_move(self) -> tuple[str, int]:
        """
         Получает от игрока направление и количество клеток для перемещения ракеты.
         В случае неправильного ввода предлагает повторить.

         :return: Кортеж с направлением и количеством клеток.
        """
        while True:
            try: # Попытка преобразовать пользовательский ввод
                move_str = input(f'Игрок {self.current_player}, введите направление и количество клеток (например, вверх 2): ')
                direction, steps = move_str.split() # Разделение ввода на направление и количество шагов
                steps = int(steps) # Преобразование количества шагов в целое число
                if direction in ['вверх', 'вниз', 'влево', 'вправо'] and steps > 0:
                    return direction, steps # Возвращение направления и количества шагов
                else:
                    print("Неверный ввод. Попробуйте снова.") # Сообщение об ошибке
            except ValueError:
                print("Неверный ввод. Попробуйте снова.")  # Сообщение об ошибке

    def _move_rocket(self, direction: str, steps: int) -> bool:
        """
         Перемещает ракету игрока в соответствии с заданными направлением и количеством клеток.

         :param direction: Направление перемещения.
         :param steps: Количество клеток для перемещения.
         :return: True, если перемещение выполнено, False если перемещение не удалось.
        """
        current_pos = self.player1_pos if self.current_player == 1 else self.player2_pos # Определение текущей позиции ракеты
        new_x, new_y = current_pos # Распаковка координат
        if direction == 'вверх':
                new_x -= steps
        elif direction == 'вниз':
            new_x += steps
        elif direction == 'влево':
            new_y -= steps
        elif direction == 'вправо':
            new_y += steps

        new_pos = (new_x, new_y) # Формирование новой позиции

        if self._is_valid_move(new_pos): # Проверка допустимости перемещения
            self.grid[current_pos[0]][current_pos[1]] = '[ ]' # Очистка предыдущей позиции
            if self.current_player == 1:
                self.player1_pos = new_pos # Обновление позиции игрока 1
                self.grid[new_pos[0]][new_pos[1]] = '[R1]' # Установка ракеты 1 на новой позиции
            else:
                self.player2_pos = new_pos # Обновление позиции игрока 2
                self.grid[new_pos[0]][new_pos[1]] = '[R2]' # Установка ракеты 2 на новой позиции
            return True
        else:
            print("Недопустимый ход. Попробуйте снова.")  # Сообщение об ошибке
            return False

    def _check_winner(self) -> int:
         """
         Проверяет, достиг ли игрок орбиты планеты (противоположный край поля).

         :return: Номер победившего игрока (1 или 2) или 0, если никто не победил.
         """
         if self.current_player == 1 and self.player1_pos[0] == GRID_SIZE - 1: # Проверка победы игрока 1
              return 1
         if self.current_player == 2 and self.player2_pos[0] == 0: # Проверка победы игрока 2
              return 2
         return 0

    def start(self) -> None:
        """
         Запускает игровой процесс.
         """
        print("Добро пожаловать в ROCKET!") # Вывод приветствия
        print("Ваша задача — первым достичь орбиты планеты, перемещая свою ракету по сетке.") # Инструкция
        print("Игра продолжается до тех пор, пока один из игроков не достигнет орбиты или пока не будет достигнуто максимальное количество ходов.") # Инструкция
        print("Удачи!")  # Мотивация

        while self.turns_count < MAX_TURNS:
            self.print_grid() # Вывод игрового поля
            move = self._get_move() # Получение хода от игрока
            if self._move_rocket(move[0], move[1]): # Перемещение ракеты
                winner = self._check_winner() # Проверка на победителя
                if winner: # Объявление победителя
                    self.print_grid() # Вывод игрового поля
                    print(f"Игра окончена! Победил Игрок {winner}.") # Вывод сообщения о победе
                    break

                self.current_player = 3 - self.current_player # Смена игрока
                self.turns_count += 1 # Увеличение количества ходов

        if not winner:
            print("Игра окончена! Ничья.") # Сообщение о ничье

        play_again = input("Хотите сыграть снова? (да/нет): ").lower() # Предложение начать новую игру
        if play_again == "да":
            self.__init__() # Инициализация новой игры
            self.start() # Запуск новой игры
        else:
            print("Спасибо за игру!") # Благодарность за игру

if __name__ == "__main__": # Проверка, запущен ли скрипт напрямую
    try:
        game = RocketGame() # Создание экземпляра игры
        game.start() # Запуск игры
    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True) # Логирование ошибки
```