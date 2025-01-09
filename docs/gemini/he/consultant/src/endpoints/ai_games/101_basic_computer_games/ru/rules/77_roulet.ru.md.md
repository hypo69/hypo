# Анализ кода модуля `77_roulet.ru.md`

**Качество кода**

- **Соответствие требованиям к формату кода (1-10):**
    - **Преимущества:**
        - Документ содержит подробное описание игры, включая правила, пошаговую инструкцию, примеры и возможные ограничения.
        - Описаны основные блоки программы и логика игры.
        - Присутствуют примеры работы программы, что облегчает понимание процесса.
    - **Недостатки:**
        - Код не представлен в виде исполняемой программы, а только в виде описания логики.
        - Отсутствуют элементы reStructuredText (RST).
        - Не используются импорты, обработка исключений и логирование.

**Рекомендации по улучшению**

1.  **Преобразование в исполняемый код:** Необходимо реализовать код на Python, используя описанную логику.
2.  **Документирование кода:** Добавить docstring в формате RST к функциям, методам и классам.
3.  **Обработка ошибок:** Использовать `try-except` блоки для обработки ошибок и `logger.error` для логирования.
4.  **Импорты:** Добавить необходимые импорты, такие как `random`, `logger` и другие, в зависимости от реализации кода.
5.  **Улучшение структуры:** Разделить код на функции для лучшей читаемости и повторного использования.
6.  **Использование `j_loads`:** Если в будущей реализации будет необходимость загружать данные из JSON, следует использовать `j_loads` или `j_loads_ns`.

**Улучшенный код**
```python
"""
Модуль для игры в рулетку
=========================================================================================

Модуль содержит реализацию игры в рулетку с базовыми правилами и возможностями.

Пример использования
--------------------

Пример запуска игры:

.. code-block:: python

    game = RouletGame()
    game.start_game()
"""
import random
from src.logger.logger import logger #  Импорт логгера для записи ошибок


class RouletGame:
    """
    Класс, представляющий игру в рулетку.
    """
    def __init__(self, initial_points: int = 100):
        """
        Инициализирует игру с заданным начальным количеством очков.

        :param initial_points: Начальное количество очков у игрока.
        """
        self.points = initial_points
        self.roulette_wheel = list(range(37)) # Колесо рулетки от 0 до 36

    def start_game(self):
        """
        Начинает игру, выводя приветствие и объяснение правил.
        """
        print("Добро пожаловать в ROULET!")
        print("Ваша задача — делать ставки на числа, цвета или группы чисел и выигрывать очки.")
        print("Игра продолжается до тех пор, пока у вас есть очки для ставок.")
        print("Удачи!")
        self.play_round()

    def play_round(self):
        """
        Запускает игровой раунд, позволяя игроку делать ставки, крутить колесо и подсчитывать результаты.
        """
        while self.points > 0:
            print(f"У вас {self.points} очков.")
            bet_type, bet_value, bet_amount = self.get_bet()
            if bet_amount > self.points:
                print("У вас недостаточно очков для этой ставки. Попробуйте снова.")
                continue
            self.spin_wheel()
            self.check_result(bet_type, bet_value, bet_amount)
            if self.points <= 0:
                print("Игра окончена! У вас 0 очков.")
                break
            if not self.ask_play_again():
                print("Спасибо за игру!")
                break

    def get_bet(self):
        """
        Запрашивает у игрока тип ставки, значение ставки и сумму ставки.

        :return: Кортеж (тип ставки, значение ставки, сумма ставки).
        :rtype: tuple
        """
        while True:
            try:
                bet_input = input("Выберите тип ставки (число, цвет, группа чисел) и укажите сумму ставки (пример: число 15, 10): ")
                parts = bet_input.split(",")
                if len(parts) != 2:
                   logger.error(f"Неверный формат ставки {bet_input=}") # Запись ошибки в лог
                   print("Неверный формат ставки. Попробуйте снова.")
                   continue
                bet_type_value, bet_amount_str = parts
                bet_type_value = bet_type_value.strip() # удаляем лишние пробелы
                bet_type, *bet_value_parts = bet_type_value.split(" ") # разделение типа ставки и значения ставки
                bet_value = " ".join(bet_value_parts).strip()
                bet_amount = int(bet_amount_str.strip()) # преобразование суммы ставки в целое число
                return bet_type, bet_value, bet_amount
            except ValueError as ex:
                logger.error(f"Ошибка ввода суммы ставки: {ex}") # Запись ошибки в лог
                print("Неверный формат суммы ставки. Попробуйте снова.")


    def spin_wheel(self):
        """
        Крутит колесо рулетки и выбирает случайное число.
        """
        print("Крутим колесо рулетки...")
        self.result = random.choice(self.roulette_wheel)
        self.result_color = self.get_color(self.result) # Получение цвета числа
        print(f"Выпало число {self.result} ({self.result_color}).")

    def get_color(self, number):
        """
        Определяет цвет числа на рулетке.
        
        :param number: Число на рулетке.
        :type number: int
        :return: Цвет числа ("красное", "черное", "зеленое").
        :rtype: str
        """
        if number == 0:
            return "зеленое"
        if number % 2 == 0:
            return "черное"
        return "красное"

    def check_result(self, bet_type, bet_value, bet_amount):
        """
        Проверяет, выиграл ли игрок, и обновляет количество очков.

        :param bet_type: Тип ставки.
        :type bet_type: str
        :param bet_value: Значение ставки.
        :type bet_value: str
        :param bet_amount: Сумма ставки.
        :type bet_amount: int
        """
        win = False
        if bet_type == "число" and str(self.result) == bet_value:
            self.points += bet_amount * 36 #  Начисление выигрыша за угаданное число
            win = True
        elif bet_type == "цвет" and bet_value == self.result_color:
            self.points += bet_amount * 2 #  Начисление выигрыша за угаданный цвет
            win = True
        elif bet_type == "группа" and self.check_group_win(bet_value):
                self.points += bet_amount * 2 #  Начисление выигрыша за угаданную группу
                win = True
        else:
            self.points -= bet_amount  #  Списание ставки за проигрыш

        if win:
            print(f"Вы выиграли {bet_amount * 36 if bet_type == 'число' else bet_amount * 2} очков!")
        else:
            print(f"Вы проиграли {bet_amount} очков.")

        print(f"У вас теперь {self.points} очков.")
    
    def check_group_win(self, group_name):
        """
        Проверяет, выиграла ли ставка на группу чисел.

        :param group_name: Название группы чисел.
        :type group_name: str
        :return: True, если игрок выиграл, False - в противном случае.
        :rtype: bool
        """
        if group_name == "малые" and 1 <= self.result <= 18:
            return True
        if group_name == "большие" and 19 <= self.result <= 36:
            return True
        if group_name == "четные" and self.result % 2 == 0 and self.result != 0:
            return True
        if group_name == "нечетные" and self.result % 2 != 0:
           return True
        return False


    def ask_play_again(self):
        """
        Предлагает игроку сыграть снова.

        :return: True, если игрок хочет сыграть снова, False - в противном случае.
        :rtype: bool
        """
        while True:
            answer = input("Хотите сыграть снова? (да/нет): ").lower()
            if answer in ["да", "нет"]:
                return answer == "да"
            print("Неверный ввод. Пожалуйста, введите 'да' или 'нет'.")


if __name__ == "__main__":
    game = RouletGame() # Создание экземпляра игры
    game.start_game()  # Запуск игры
```