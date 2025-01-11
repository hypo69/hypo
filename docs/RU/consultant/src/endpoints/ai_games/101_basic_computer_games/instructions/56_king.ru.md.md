# Анализ кода модуля KING

**Качество кода**
9
 -  Плюсы
    -   Представлено четкое и подробное описание игры, включая правила, цели и игровой процесс.
    -   Инструкции по реализации игры структурированы и понятны, что облегчает понимание логики и требований.
    -   Приведены примеры работы программы, которые демонстрируют последовательность действий и ожидаемые результаты.
    -   Описаны возможные ограничения и рекомендации по реализации, что помогает при разработке.
 -  Минусы
    -  Отсутствует код для реализации игры, только текстовое описание.
    -  Не хватает подробных инструкций по созданию функций, классов и обработке данных.
    -  Не предусмотрены логирование ошибок и форматирование кода в соответствии с PEP 8.
    -   Нет указаний по использованию reStructuredText (RST) в комментариях и docstring.

**Рекомендации по улучшению**
1.  **Реализация кода:** Необходимо создать фактический код на Python, используя предоставленные инструкции.
2.  **Формат документации:** Все комментарии и docstring должны быть написаны в формате reStructuredText (RST).
3.  **Использование j_loads/j_loads_ns:** В коде, который будет реализован, необходимо использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов.
4.  **Логирование:** При реализации кода необходимо использовать `from src.logger.logger import logger` для логирования ошибок.
5.  **Обработка ошибок:** Избегать избыточного использования стандартных блоков `try-except`, предпочитая обработку ошибок с помощью `logger.error`.
6.  **Структура кода:** Разделить код на функции и классы для лучшей читаемости и переиспользования.
7.  **Документация:** Добавить подробную документацию к каждой функции и классу в формате reStructuredText.
8. **Примеры кода:** Необходимо добавить примеры кода и возможные улучшения в формате `TODO`.

**Оптимизированный код**
```python
"""
Модуль для реализации игры KING (Управляй своим островом).
=========================================================================================

Этот модуль содержит реализацию игры KING, в которой игрок управляет вымышленным островом,
принимая решения о бюджете, распределении ресурсов и экологии.

Пример использования
--------------------

Пример запуска игры:

.. code-block:: python

    game = KingGame()
    game.start_game()
"""

from src.logger.logger import logger # Импорт логгера для отслеживания ошибок

class KingGame:
    """
    Класс, реализующий игру KING.
    """
    def __init__(self):
        """
        Инициализирует начальные параметры игры.
        """
        self.rallods = 5000  # Начальный бюджет
        self.land_size = 30 * 70  # Размер острова в квадратных милях
        self.population = 1000  # Начальное количество людей на острове
        self.year = 0  # Текущий год игры
        self.game_over = False # Флаг для завершения игры
        self.price_per_land = 100 # Стоимость земли за квадратную милю

    def _display_welcome_message(self):
        """
        Выводит приветственное сообщение и правила игры.
        """
        print("Добро пожаловать в игру KING!")
        print("Вы — премьер острова Setats Detinu, небольшой коммунистический остров с размерами 30 на 70 миль.")
        print("Ваша задача — управлять бюджетом страны, распределять деньги среди граждан и принимать решения, влияющие на будущее острова.")
        print("Ваша страна получает доход от сельского хозяйства, туризма, а также от продажи земли для промышленности.")
        print("Ваша цель — завершить восьмилетний срок правления без крупных неудач.")

    def _check_player_experience(self):
        """
        Проверяет опыт игрока и выводит соответствующие сообщения.
        """
        try:
            experience = int(input("Введите количество раз, сколько вы уже играли: "))
            if experience == 0:
                self._display_welcome_message()
            elif experience == 500:
                print("Игра начинается без объяснения правил.")
            elif experience == 1000:
                print("Продолжение предыдущей игры.")
        except ValueError:
            logger.error("Некорректный ввод. Введите целое число.") # Логирование ошибки при некорректном вводе
            self._check_player_experience() # Повторный запрос на ввод
        except Exception as ex:
            logger.error("Произошла ошибка при проверке опыта игрока.", ex) # Логирование ошибок при исключениях

    def _get_land_sale_input(self):
        """
        Запрашивает у игрока количество земли для продажи и возвращает доход.
        
        :return: Доход от продажи земли.
        :rtype: int
        """
        while True:
            try:
                land_to_sell = int(input("Сколько квадратных миль земли вы хотите продать для промышленности? "))
                if land_to_sell < 0 or land_to_sell > self.land_size:
                    print(f"Некорректный ввод. Введите значение от 0 до {self.land_size}")
                    continue
                sale_income = land_to_sell * self.price_per_land
                self.rallods += sale_income
                self.land_size -= land_to_sell
                print(f"Цена за квадратный милль: {self.price_per_land} Rallods.")
                print(f"Вы получили {sale_income} Rallods от продажи земли.")
                return sale_income
            except ValueError:
                logger.error("Некорректный ввод. Введите целое число.") # Логирование ошибки при некорректном вводе
            except Exception as ex:
                logger.error("Произошла ошибка при получении ввода продажи земли.", ex) # Логирование ошибок при исключениях
                return 0

    def _get_rallods_distribution_input(self):
        """
        Запрашивает у игрока количество Rallods для распределения и возвращает потраченную сумму.
        
        :return: Потраченная сумма Rallods.
        :rtype: int
        """
        while True:
            try:
                rallods_to_distribute = int(input("Сколько Rallods вы хотите распределить среди граждан? "))
                if rallods_to_distribute < 0:
                    print("Некорректный ввод. Введите положительное число.")
                    continue
                self.rallods -= rallods_to_distribute
                if self.rallods < 0:
                    print("Недостаточно средств в казне")
                    self.rallods += rallods_to_distribute # Возврат потраченных средств
                    continue
                return rallods_to_distribute
            except ValueError:
                logger.error("Некорректный ввод. Введите целое число.") # Логирование ошибки при некорректном вводе
            except Exception as ex:
                logger.error("Произошла ошибка при получении ввода распределения Rallods.", ex) # Логирование ошибок при исключениях
                return 0

    def _get_environmental_spending_input(self):
        """
        Запрашивает у игрока количество Rallods для расходов на экологию и возвращает потраченную сумму.
        
        :return: Потраченная сумма Rallods.
        :rtype: int
        """
        while True:
            try:
                environmental_spending = int(input("Сколько Rallods вы хотите потратить на охрану экологии? "))
                if environmental_spending < 0:
                   print("Некорректный ввод. Введите положительное число.")
                   continue
                self.rallods -= environmental_spending
                if self.rallods < 0:
                    print("Недостаточно средств в казне")
                    self.rallods += environmental_spending
                    continue
                return environmental_spending
            except ValueError:
                 logger.error("Некорректный ввод. Введите целое число.") # Логирование ошибки при некорректном вводе
            except Exception as ex:
                logger.error("Произошла ошибка при получении ввода расходов на экологию.", ex) # Логирование ошибок при исключениях
                return 0

    def _calculate_results(self, rallods_distributed, environmental_spending):
        """
        Вычисляет результаты хода игры: количество погибших, уехавших и оставшиеся Rallods.

        :param rallods_distributed: Количество Rallods, распределенных среди граждан.
        :type rallods_distributed: int
        :param environmental_spending: Количество Rallods, потраченных на охрану окружающей среды.
        :type environmental_spending: int
        """
        rallods_per_person = 100
        people_starved = max(0, self.population - (rallods_distributed // rallods_per_person))
        people_left = max(0, people_starved // 2)
        self.population -= people_starved + people_left
        
        print(f"Вы потратили {rallods_distributed} Rallods на граждан и {environmental_spending} Rallods на охрану экологии.")
        print(f"{people_left} людей покинули остров из-за нехватки ресурсов.")
        print(f"{people_starved} людей погибли от голода.")
        print(f"{self.rallods} Rallods остаются в казне.")

    def _check_game_over(self):
        """
        Проверяет, не завершилась ли игра из-за неудачного управления.

        :return: True, если игра завершилась, False в противном случае.
        :rtype: bool
        """
        if self.population <= 0 :
            print("Ваша страна потерпела поражение из-за неудачного управления!")
            print("Вы были вынуждены уйти в отставку.")
            self.game_over = True
            return True
        if self.year >= 8:
            print("Поздравляем! Вы успешно завершили ваш срок правления!")
            self.game_over = True
            return True
        return False

    def start_game(self):
        """
        Запускает игровой процесс.
        """
        self._check_player_experience()
        while not self.game_over:
            self.year += 1
            print(f"\nГод {self.year}. Ваша страна имеет {self.rallods} Rallods в казне.")
            land_sale_income = self._get_land_sale_input()
            rallods_distributed = self._get_rallods_distribution_input()
            environmental_spending = self._get_environmental_spending_input()
            self._calculate_results(rallods_distributed, environmental_spending)
            if self._check_game_over():
                 break
            
        self._play_again()

    def _play_again(self):
        """
        Предлагает игроку сыграть еще раз.
        """
        while True:
            try:
                play_again = input("Хотите сыграть снова? (да/нет) ").lower()
                if play_again == "да":
                   self.__init__() # Переинициализация игры
                   self.start_game()
                   break
                elif play_again == "нет":
                    print("Спасибо за игру!")
                    break
                else:
                     print("Некорректный ввод. Введите 'да' или 'нет'.")
            except Exception as ex:
                logger.error("Произошла ошибка при запросе на повторную игру.", ex)
                break

# TODO: Добавить случайные события, такие как природные катастрофы, экономический кризис или рост туризма.
# TODO: Реализовать систему уровня сложности.
# TODO: Добавить учет дохода от сельского хозяйства и туризма.
if __name__ == "__main__":
    game = KingGame()
    game.start_game()