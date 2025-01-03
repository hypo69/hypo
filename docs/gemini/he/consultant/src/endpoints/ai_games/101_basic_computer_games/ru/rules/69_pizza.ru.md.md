# Анализ кода модуля `69_pizza.ru.md`

**Качество кода**

- **Соблюдение требований к формату кода (1-10):**
    -   **Преимущества:**
        -   Документ в формате Markdown, что соответствует требованиям.
        -   Присутствует подробное описание игры, пошаговая инструкция, пример работы, ограничения и рекомендации по реализации, что хорошо для понимания.
    -   **Недостатки:**
        -   Отсутствует программный код, что делает невозможным анализ его соответствия.
        -   Нет использования reStructuredText (RST) для аннотаций, как того требуют условия.
        -   Не соблюдены требования по использованию `j_loads` и `j_loads_ns` для загрузки данных.
        -   Нет логирования с использованием `from src.logger.logger import logger`.
        -   Отсутствуют docstring для функций и классов, так как нет кода.

**Рекомендации по улучшению**

1.  **Создание программного кода:**
    -   Реализовать игру на Python, как указано в разделе "Реализация".
    -   Использовать массивы (списки) для хранения состояния пиццы и игроков.
    -   Использовать функции для обработки ходов игроков и проверок.

2.  **Документация в reStructuredText (RST):**
    -   Добавить reStructuredText docstring для функций, методов и классов.
    -   Включить описание модуля в начале файла.
    -   Добавить примеры кода с использованием RST.

3.  **Использование `j_loads` и `j_loads_ns`:**
    -   Если предполагается загрузка данных из файла, использовать `j_loads` или `j_loads_ns` из `src.utils.jjson`.

4.  **Логирование:**
    -   Использовать `from src.logger.logger import logger` для записи ошибок и предупреждений.
    -   Избегать чрезмерного использования `try-except` и предпочитать логирование ошибок.

5.  **Обработка ввода:**
    -   Реализовать проверку ввода пользователя на корректность.
    -   Предусмотреть обработку некорректного ввода (не числа, числа вне диапазона).

6.  **Дополнительные функции:**
    -   Реализовать рекомендованные улучшения, такие как "атака" на кусочки соперника, режим игры с компьютером и графический интерфейс.

7.  **Подробные комментарии:**
    -   Добавить комментарии к коду, объясняющие логику каждой строки.
    -   Использовать комментарии в стиле RST.

**Улучшенный код**

```python
"""
Модуль для реализации игры "Пицца"
=========================================================================================

Этот модуль реализует игру "Пицца", в которой игроки по очереди захватывают кусочки пиццы.
Цель игры - собрать наибольшее количество кусочков.

Пример использования
--------------------

Пример запуска игры:

.. code-block:: python

    game = PizzaGame()
    game.start_game()
"""
import random  # импортируем модуль random для случайного выбора хода
from src.logger.logger import logger # импортируем logger для логгирования ошибок
from typing import List, Dict # импортируем типы для аннотаций

class PizzaGame:
    """
    Класс, представляющий игру "Пицца".

    :ivar pizza_slices: Состояние пиццы (список, где None означает свободный кусочек, а int - номер игрока, захватившего кусок).
    :vartype pizza_slices: List[int or None]
    :ivar players_scores: Словарь с очками игроков (ключ - номер игрока, значение - количество захваченных кусков).
    :vartype players_scores: Dict[int, int]
    :ivar current_player: Номер текущего игрока.
    :vartype current_player: int
    :ivar is_game_over: Флаг, указывающий на завершение игры.
    :vartype is_game_over: bool
    """
    def __init__(self):
        """
        Инициализирует игру, создает пиццу из 8 кусочков, устанавливает счет игроков в 0 и устанавливает текущего игрока 1.
        """
        self.pizza_slices: List[int or None] = [None] * 8  # Состояние пиццы: None - свободный, int - номер игрока
        self.players_scores: Dict[int, int] = {1: 0, 2: 0} # Очки игроков
        self.current_player: int = 1 # Текущий игрок
        self.is_game_over: bool = False # Флаг конца игры
        logger.debug('Игра "Пицца" инициализирована') # Логирование инициализации игры

    def _print_welcome_message(self) -> None:
        """
        Выводит приветственное сообщение и правила игры.
        """
        print("Добро пожаловать в PIZZA!") # Приветственное сообщение
        print("Ваша задача — собрать как можно больше кусочков пиццы.") # Объяснение цели игры
        print("Пицца разбита на 8 кусочков. Каждый игрок по очереди выбирает кусочек.") # Описание количества кусочков
        print("Если вы выбираете кусочек, который граничит с уже выбранными кусочками, вы забираете их себе.") # Описание правила захвата
        print("Удачи!") # Пожелание удачи

    def _display_pizza(self) -> None:
        """
        Выводит текущее состояние пиццы.
        """
        print("Текущее состояние пиццы:")  # Вывод сообщения о текущем состоянии
        for i, owner in enumerate(self.pizza_slices): # Цикл для прохода по всем кусочкам пиццы
            if owner is None: # Проверка, свободен ли кусочек
                print(f"Кусочек {i + 1}: Свободен") # Если свободен, выводится сообщение, что он свободен
            else:
                print(f"Кусочек {i + 1}: Игрок {owner}") # Если занят, выводится сообщение, каким игроком занят

    def _switch_player(self) -> None:
        """
        Переключает текущего игрока.
        """
        self.current_player = 3 - self.current_player  # Переключаем текущего игрока

    def _is_valid_move(self, slice_number: int) -> bool:
        """
        Проверяет, является ли ход допустимым.

        :param slice_number: Номер выбранного кусочка пиццы (от 1 до 8).
        :type slice_number: int
        :return: True, если ход допустим, False в противном случае.
        :rtype: bool
        """
        if not 1 <= slice_number <= 8: # Проверка диапазона
            logger.error(f'Недопустимый номер куска: {slice_number}') # Логирование ошибки
            print("Неверный ввод. Попробуйте снова.") # Вывод сообщения об ошибке
            return False # Если номер куска вне диапазона возвращаем False

        if self.pizza_slices[slice_number - 1] is not None: # Проверка, занят ли кусок
           logger.debug(f'Кусок {slice_number} уже занят') # Логирование, если кусок уже занят
           print("Кусочек уже захвачен. Попробуйте снова.") # Вывод сообщения, что кусок занят
           return False # Возвращаем False
        return True # Возвращаем True, если ход допустимый

    def _capture_slices(self, slice_number: int) -> None:
        """
        Захватывает выбранный кусок и прилегающие куски, если они принадлежат игроку.

        :param slice_number: Номер выбранного кусочка (от 1 до 8).
        :type slice_number: int
        """
        slice_index = slice_number - 1 # Получаем индекс куска
        self.pizza_slices[slice_index] = self.current_player # Захватываем выбранный кусок
        self.players_scores[self.current_player] += 1 # Увеличиваем счет игрока

        # Проверяем соседние куски
        neighbors = self._get_neighbors(slice_index) # Получаем соседние куски
        for neighbor_index in neighbors: # Цикл для обхода соседних кусочков
            if self.pizza_slices[neighbor_index] is not None and self.pizza_slices[neighbor_index] != self.current_player: # Проверка, есть ли сосед и не занят ли он текущим игроком
                  # Здесь можно добавить логику для "атаки" на куски противника, но пока ограничимся просто захватом соседних
                self.pizza_slices[neighbor_index] = self.current_player # Захватываем соседний кусок
                self.players_scores[self.current_player] += 1 # Увеличиваем счет игрока
                logger.debug(f'Игрок {self.current_player} захватил кусок {neighbor_index + 1}') # Логируем захват куска

        logger.debug(f'Игрок {self.current_player} захватил кусок {slice_number}')  # Логируем захват куска

    def _get_neighbors(self, slice_index: int) -> List[int]:
        """
        Возвращает индексы соседних кусочков.

        :param slice_index: Индекс кусочка (от 0 до 7).
        :type slice_index: int
        :return: Список индексов соседних кусочков.
        :rtype: List[int]
        """
        neighbors = [] # Инициализируем список соседних кусочков
        if slice_index > 0: # Проверяем, не первый ли это кусок
            neighbors.append(slice_index - 1) # Добавляем левый соседний кусок
        if slice_index < 7: # Проверяем, не последний ли это кусок
            neighbors.append(slice_index + 1) # Добавляем правый соседний кусок

        if slice_index == 0 and 7 in neighbors:
            neighbors.remove(7)
            neighbors.append(7)

        if slice_index == 7 and 0 in neighbors:
            neighbors.remove(0)
            neighbors.append(0)

        return neighbors # Возвращаем список соседних кусков

    def _is_game_finished(self) -> bool:
        """
        Проверяет, закончена ли игра (все кусочки захвачены).

        :return: True, если игра закончена, False в противном случае.
        :rtype: bool
        """
        self.is_game_over = all(slice_owner is not None for slice_owner in self.pizza_slices) # Проверяем, все ли куски захвачены
        return self.is_game_over # Возвращаем результат

    def _print_scores(self) -> None:
        """
        Выводит текущий счет игроков.
        """
        print("Текущий счет:") # Вывод сообщения о текущем счете
        for player, score in self.players_scores.items():  # Цикл для вывода счета каждого игрока
             print(f"Игрок {player}: {score} кусочка") # Вывод счета игрока

    def _print_winner(self) -> None:
        """
        Выводит победителя игры.
        """
        winner = max(self.players_scores, key=self.players_scores.get) # Определяем победителя по максимальному количеству кусочков
        print(f"Игра окончена! Победил Игрок {winner} с {self.players_scores[winner]} захваченными кусочками.") # Выводим сообщение о победителе

    def start_game(self) -> None:
        """
        Запускает игру.
        """
        self._print_welcome_message() # Выводим приветственное сообщение
        while not self.is_game_over: # Пока игра не закончена
            self._display_pizza() # Выводим текущее состояние пиццы
            print(f"Игрок {self.current_player}, ваш ход.") # Сообщаем, какой игрок ходит
            while True: # Бесконечный цикл для запроса ввода пользователя
                try: # Обработка исключений
                    slice_number = int(input("Введите номер кусочка, который хотите захватить (от 1 до 8): ")) # Получаем номер куска от пользователя
                    if self._is_valid_move(slice_number): # Проверяем, является ли ход допустимым
                        break # Если ход допустимый, выходим из цикла
                except ValueError: # Обработка ошибки ValueError
                    logger.error('Неверный ввод, ожидается число') # Логируем ошибку
                    print("Неверный ввод. Попробуйте снова.") # Выводим сообщение об ошибке
            self._capture_slices(slice_number) # Захватываем кусочки
            self._print_scores() # Выводим счет
            if self._is_game_finished(): # Проверяем, закончена ли игра
                break # Если игра окончена, выходим из цикла
            self._switch_player() # Переключаем игрока
        self._print_winner() # Выводим победителя
        if self._play_again():
             self.__init__()
             self.start_game()
        else:
           print("Спасибо за игру!") # Выводим сообщение о завершении игры

    def _play_again(self) -> bool:
        """
        Предлагает пользователю сыграть ещё раз.

        :return: True, если пользователь хочет сыграть ещё раз, False в противном случае.
        :rtype: bool
        """
        while True:
           answer = input("Хотите сыграть снова? (да/нет): ").lower() # Получаем ответ пользователя
           if answer in ("да", "нет"):  # Проверяем, является ли ввод пользователя "да" или "нет"
               return answer == "да" # Возвращаем true или false
           else: # Обработка неверного ввода
               logger.error("Неверный ввод, ожидается 'да' или 'нет'") # Логирование неверного ввода
               print("Неверный ввод. Пожалуйста, введите 'да' или 'нет'.") # Сообщение для пользователя

if __name__ == "__main__":
    """
    Основная точка входа в программу.
    """
    game = PizzaGame() # Создаем экземпляр игры
    game.start_game() # Запускаем игру
```