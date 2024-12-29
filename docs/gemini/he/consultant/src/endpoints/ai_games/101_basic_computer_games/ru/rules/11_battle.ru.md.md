# Анализ кода модуля `11_battle.ru.md`

**Качество кода**

- **Соответствие требованиям к формату кода (1-10):**
    -   **Преимущества:**
        -   Документ хорошо структурирован, с четкими заголовками и разделами.
        -   Представлено подробное пошаговое руководство по реализации игры.
        -   Присутствуют примеры работы программы, которые помогают понять игровую механику.
        -   Описаны возможные ограничения, что показывает внимание к деталям.
    -   **Недостатки:**
        -   Файл представляет собой описание игры в формате Markdown, а не код на Python, поэтому многие требования не применимы напрямую.
        -   Отсутствует описание кода в reStructuredText, как того требуют инструкции.
        -   Нет использования `j_loads` или `j_loads_ns`, так как нет кода Python.
        -   Нет кода, требующего проверки и исправления импортов.
        -   Нет кода, требующего добавления комментариев в формате RST или использования логгера.
        -   Нет кода, требующего обработки ошибок через `logger.error`.
        -   Нет кода, требующего добавления примеров и `TODO`.
        -   Файл не содержит кода, поэтому не может быть непосредственно улучшен с помощью инструкций.

**Рекомендации по улучшению**

1.  **Преобразование в исполняемый код:** Преобразовать текстовое описание игры в Python код, следуя пошаговым инструкциям.
2.  **Реализация структур данных:** Создать структуры данных для представления игрового поля и кораблей.
3.  **Реализация игровой логики:** Разработать функции для обработки ввода игрока, проверки попаданий, и обновления состояния игры.
4.  **Добавление пользовательского интерфейса:** Создать простой интерфейс для взаимодействия с игроком (например, через ввод с клавиатуры).
5.  **Включение логирования:** Использовать логгер для отслеживания ошибок и событий в игре.
6.  **Оформление кода:** Написать docstrings в reStructuredText для документирования функций и классов.
7.  **Обработка ошибок:** Добавить обработку исключений с помощью `try-except` и `logger.error`.
8.  **Документация:** Добавить примеры использования и комментарии `TODO` для будущих улучшений.

**Улучшенный код**

```python
"""
Модуль для реализации игры "Морской бой"
=========================================================================================

Модуль содержит классы и функции для создания и управления игрой "Морской бой".
Включает логику размещения кораблей, обработки выстрелов и определения победителя.

Пример использования
--------------------

Пример запуска игры:

.. code-block:: python

    game = BattleGame()
    game.play()

"""
import random
from src.logger.logger import logger # Импорт логгера

class Ship:
    """
    Класс для представления корабля.

    :ivar int size: Размер корабля (количество клеток).
    :ivar list<tuple<int, int>> positions: Список координат, занимаемых кораблем.
    :ivar int hits: Количество попаданий по кораблю.
    :ivar bool sunk: Флаг, указывающий, потоплен ли корабль.
    """
    def __init__(self, size):
        """
        Инициализирует корабль заданного размера.

        :param int size: Размер корабля.
        """
        self.size = size
        self.positions = []
        self.hits = 0
        self.sunk = False

    def is_hit(self, coord):
        """
        Проверяет, является ли заданная координата попаданием по кораблю.

        :param tuple<int, int> coord: Координата для проверки.
        :return: True, если попадание, иначе False.
        :rtype: bool
        """
        return coord in self.positions

    def register_hit(self):
        """
        Регистрирует попадание по кораблю.
        
        Обновляет количество попаданий и флаг потопления.
        """
        self.hits += 1
        if self.hits == self.size:
            self.sunk = True

class BattleGame:
    """
    Класс для управления игрой "Морской бой".

    :ivar int board_size: Размер игрового поля.
    :ivar list<Ship> ships: Список кораблей на поле.
    :ivar list<tuple<int, int>> shots: Список всех выстрелов, сделанных игроком.
    :ivar int hits: Количество попаданий.
    :ivar int splash: Количество промахов.
    """
    def __init__(self, board_size=6):
        """
        Инициализирует игру с заданным размером поля и размещением кораблей.

        :param int board_size: Размер игрового поля.
        """
        self.board_size = board_size
        self.ships = self.create_ships()
        self.shots = []
        self.hits = 0
        self.splash = 0

    def create_ships(self):
        """
        Создает и размещает корабли на игровом поле.

        :return: Список кораблей.
        :rtype: list<Ship>
        """
        ships = []
        ship_sizes = [2, 2, 3, 3, 4, 4] # Размеры кораблей
        for size in ship_sizes:
            ship = Ship(size)
            placed = False
            while not placed:
                orientation = random.choice(['horizontal', 'vertical'])
                if orientation == 'horizontal':
                    row = random.randint(0, self.board_size - 1)
                    col = random.randint(0, self.board_size - size)
                    positions = [(row, col + i) for i in range(size)]
                else:
                    row = random.randint(0, self.board_size - size)
                    col = random.randint(0, self.board_size - 1)
                    positions = [(row + i, col) for i in range(size)]

                if not self.check_overlap(positions, ships):
                    ship.positions = positions
                    ships.append(ship)
                    placed = True
        return ships

    def check_overlap(self, positions, ships):
        """
        Проверяет, перекрываются ли заданные позиции с другими кораблями.

        :param list<tuple<int, int>> positions: Список позиций для проверки.
        :param list<Ship> ships: Список существующих кораблей.
        :return: True, если есть пересечение, иначе False.
        :rtype: bool
        """
        for ship in ships:
            for pos in positions:
                if pos in ship.positions:
                    return True
        return False

    def process_shot(self, coord):
        """
        Обрабатывает выстрел игрока и обновляет состояние игры.

        :param tuple<int, int> coord: Координаты выстрела.
        :return: Статус выстрела ("Splash", "Hit" или "Sunk"), или None если выстрел недопустим.
        :rtype: str or None
        """
        if not self.is_valid_coord(coord):
            logger.error(f'Недопустимые координаты: {coord}')  # Логирование ошибки
            return None

        self.shots.append(coord) # Записывает выстрел
        for ship in self.ships:
            if ship.is_hit(coord): # Проверяет попадание
                ship.register_hit()
                self.hits += 1
                if ship.sunk: # Проверяет потопление
                    return "Sunk"
                return "Hit"
        self.splash += 1 # Записывает промах
        return "Splash"

    def is_valid_coord(self, coord):
        """
        Проверяет, являются ли координаты корректными.

        :param tuple<int, int> coord: Координаты для проверки.
        :return: True, если координаты в пределах поля, иначе False.
        :rtype: bool
        """
        row, col = coord
        return 0 <= row < self.board_size and 0 <= col < self.board_size

    def is_game_over(self):
        """
        Проверяет, закончилась ли игра (все корабли потоплены).

        :return: True, если все корабли потоплены, иначе False.
        :rtype: bool
        """
        return all(ship.sunk for ship in self.ships)

    def display_results(self):
        """
        Выводит итоговые результаты игры.
        
        :return: None.
        """
        print("\nИгра завершена!")
        print("Вы потопили все корабли противника!")
        print(f"Итоговый счёт:\nHits: {self.hits}\nSplash: {self.splash}")
        if self.splash != 0:
            print(f"Соотношение Splash/Hit: {self.splash}/{self.hits} ({self.splash/self.hits:.1f})")
        else:
             print("Соотношение Splash/Hit: 0")

    def play(self):
        """
        Запускает основной игровой цикл.
        
        :return: None.
        """
        while not self.is_game_over():
            try:
                coord_str = input("Введите координаты для уничтожения вражеского корабля (формат: row,col): ")
                row, col = map(int, coord_str.split(','))
                coord = (row, col)
                result = self.process_shot(coord)

                if result is None: # Обработка невалидных координат
                    print("Недопустимые координаты. Попробуйте снова.")
                    continue
                print(f"Компьютер: {result}!")
            except ValueError as e:
                 logger.error(f'Ошибка ввода координат: {e}')
                 print("Неправильный формат ввода. Введите координаты через запятую (row,col).")
            except Exception as e:
                logger.error(f'Неизвестная ошибка: {e}')
                print("Произошла ошибка. Пожалуйста, попробуйте еще раз.")
        self.display_results()

if __name__ == "__main__":
    game = BattleGame() # Создает экземпляр игры
    game.play() # Начинает игру
```