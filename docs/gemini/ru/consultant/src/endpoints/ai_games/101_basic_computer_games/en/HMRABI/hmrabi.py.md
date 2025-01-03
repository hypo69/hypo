# Анализ кода модуля hmrabi.py

**Качество кода**
7
-  Плюсы
    - Код содержит описание игры, правил, алгоритма и блок-схемы.
    - Код логически структурирован и соответствует алгоритму игры.
    - Код содержит комментарии, объясняющие основные шаги.
    - Присутствуют проверки на корректность ввода.
-  Минусы
    - Отсутствует документация в формате reStructuredText (RST).
    - Используется стандартный `input` для ввода, без обработки ошибок ввода (кроме `ValueError`).
    - Отсутствует логирование ошибок.
    - Код не использует `j_loads` или `j_loads_ns`.
    - Есть повторения кода при запросе ввода (блоки `while True: try...except ValueError`).
    - Комментарии после `#` не содержат подробное описание следующего за ними блока кода.

**Рекомендации по улучшению**

1.  **Документация**:
    - Добавить документацию в формате RST для модуля, функций и переменных.
2.  **Импорты**:
    - Добавить необходимые импорты, такие как `logger` из `src.logger.logger`.
3.  **Обработка ошибок**:
    - Использовать `logger.error` для логирования ошибок вместо стандартного `try-except`.
4.  **Ввод данных**:
    - Избегать повторяющегося кода при запросе ввода, вынести в отдельную функцию.
5.  **Комментарии**:
    - Добавить подробные комментарии к блокам кода, поясняющие их назначение.
6. **Использование `j_loads`**:
   - Хотя в данном коде не производится чтение файлов, необходимо добавить комментарии о необходимости использовать `j_loads` или `j_loads_ns` при работе с файлами.
7. **Улучшение обработки пользовательского ввода**:
    - Вынести логику запроса пользовательского ввода в отдельные функции для упрощения и предотвращения дублирования кода.
8. **Переменные**:
    - Использовать более информативные имена переменных.

**Оптимизированный код**

```python
"""
Модуль реализует игру "Хаммурапи" - текстовую экономическую игру, в которой игрок управляет древним городом.

===========================================================================================================

В игре игрок принимает решения о покупке и продаже земли, распределении урожая, посеве и следит за уровнем голода и численностью населения.

Игра заканчивается, если население города умирает от голода или по истечении 10 игровых лет.

Пример использования
--------------------

.. code-block:: python

    python hmrabi.py

"""
import random
from src.logger.logger import logger  #  Импортируем logger для логирования ошибок

def get_int_input(prompt: str) -> int:
    """
    Запрашивает у пользователя ввод целого числа.

    :param prompt: Сообщение, отображаемое пользователю.
    :return: Введенное целое число.
    :raises ValueError: Если введенное значение не является целым числом.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            logger.error("Ошибка ввода: Пожалуйста, введите целое число.")  # Используем logger.error для логирования ошибки

# Инициализация переменных
year = 0  # текущий год
population = 100  # начальное население
grain = 2800  # начальное количество зерна
land = 1000  # начальная площадь земли

print("Добро пожаловать в игру Хаммурапи!")

# Основной игровой цикл
while year < 10 and population > 0:
    print(f"\nГод {year + 1}")
    print(f"Население: {population}")
    print(f"Зерно: {grain} бушелей")
    print(f"Земля: {land} акров")

    # Вычисляем случайную цену земли
    land_price = random.randint(15, 25)
    print(f"Цена земли: {land_price} бушелей за акр")

    # Запрашиваем у игрока сколько земли купить или продать
    land_trade = get_int_input("Сколько земли купить (+) или продать (-)? ")

    # Проверяем достаточно ли зерна для покупки или земли для продажи
    while True:
        if land_trade > 0 and grain < land_trade * land_price:
            print("Недостаточно зерна для покупки земли.")
            land_trade = get_int_input("Сколько земли купить (+) или продать (-)? ")
            continue
        if land_trade < 0 and land < abs(land_trade):
            print("Недостаточно земли для продажи.")
            land_trade = get_int_input("Сколько земли купить (+) или продать (-)? ")
            continue
        break

    # Обновляем количество земли и зерна
    land += land_trade
    grain -= land_trade * land_price

    # Запрашиваем сколько зерна посеять
    grain_to_plant = get_int_input("Сколько зерна использовать для посева? ")

    # Проверяем, достаточно ли зерна для посева.
    while True:
         if grain < grain_to_plant:
            print("Недостаточно зерна для посева.")
            grain_to_plant = get_int_input("Сколько зерна использовать для посева? ")
            continue
         break

    # Вычисляем случайный урожай
    yield_per_acre = random.randint(1, 8)
    harvest = grain_to_plant * yield_per_acre
    grain += harvest

    # Вычисляем количество зерна съеденное крысами
    rats_damage = int(random.random() * 0.1 * grain)
    grain -= rats_damage
    print(f"Крысы съели {rats_damage} бушелей зерна.")

    # Запрашиваем, сколько зерна отдать на пропитание.
    grain_to_feed = get_int_input("Сколько зерна отдать на пропитание? ")

    # Проверяем, хватит ли зерна на пропитание.
    if grain_to_feed >= population:
        population = min(1000, int(population * 1.1))
        grain -= grain_to_feed
        print("Все сыты, население растёт!")
    else:
        starved = int(population * (1 - grain_to_feed / population))
        population -= starved
        grain -= grain_to_feed
        print(f"{starved} человек умерло от голода.")
        if population <= 0:
            print("Вы проиграли, все население вымерло от голода!")

    year += 1

if year == 10:
    print("Игра окончена. Прошло 10 лет.")

"""
Объяснение кода:

1. **Импорт модуля `random`**::
    - `import random`: Импортирует модуль для генерации случайных чисел.
    - `from src.logger.logger import logger`: Импортирует логгер для записи ошибок.

2. **Функция `get_int_input(prompt: str) -> int`**:
   -  :param prompt: Сообщение, отображаемое пользователю.
   -  :return: Введенное целое число.
   -  :raises ValueError: Если введенное значение не является целым числом.
   - `while True:`: Цикл для запроса ввода целого числа, пока ввод не будет корректным.
   - `try...except ValueError`:  Блок try-except для перехвата ошибки, если ввод не является целым числом.
   - `logger.error("Ошибка ввода: Пожалуйста, введите целое число.")`: Логирует ошибку ввода с использованием logger.
   - `return value`: Возвращает введенное пользователем целое число.

3. **Инициализация переменных**:
    - `year = 0`: Инициализирует переменную `year` для отслеживания текущего года (начинается с 0).
    - `population = 100`: Инициализирует переменную `population` для отслеживания количества населения (начинается со 100).
    - `grain = 2800`: Инициализирует переменную `grain` для отслеживания количества зерна (начинается с 2800).
    - `land = 1000`: Инициализирует переменную `land` для отслеживания количества земли (начинается с 1000).
    - `print("Добро пожаловать в игру Хаммурапи!")`: Выводит приветственное сообщение для игрока.

4. **Основной игровой цикл `while year < 10 and population > 0:`**:
    - Цикл продолжается, пока не пройдет 10 лет или население не станет меньше или равно 0.
    - `print(f"\\nГод {year + 1}")`: Выводит текущий год.
    - `print(f"Население: {population}")`: Выводит текущее количество населения.
    - `print(f"Зерно: {grain} бушелей")`: Выводит текущее количество зерна.
    - `print(f"Земля: {land} акров")`: Выводит текущее количество земли.

5. **Определение цены земли**:
    - `land_price = random.randint(15, 25)`: Генерирует случайную цену за акр земли в диапазоне от 15 до 25 бушелей.
    - `print(f"Цена земли: {land_price} бушелей за акр")`: Выводит текущую цену земли.

6.  **Ввод количества земли для торговли**:
    - `land_trade = get_int_input("Сколько земли купить (+) или продать (-)? ")`: Запрашивает у пользователя количество земли для покупки или продажи, используя функцию `get_int_input`.

7. **Проверка достаточности ресурсов для торговли**:
    - `while True:`: Цикл для проверки хватает ли зерна для покупки земли или земли для продажи.
    - `if land_trade > 0 and grain < land_trade * land_price:`: Проверяет, достаточно ли зерна для покупки. Если нет, выводит сообщение об ошибке и запрашивает ввод снова.
    - `if land_trade < 0 and land < abs(land_trade):`: Проверяет, достаточно ли земли для продажи. Если нет, выводит сообщение об ошибке и запрашивает ввод снова.
    - `break`: Если ввод корректен, цикл завершается.

8. **Обновление количества земли и зерна**:
   - `land += land_trade`: Обновляет количество земли.
   - `grain -= land_trade * land_price`: Обновляет количество зерна.

9.  **Ввод количества зерна для посева**:
    - `grain_to_plant = get_int_input("Сколько зерна использовать для посева? ")`: Запрашивает у пользователя количество зерна для посева, используя функцию `get_int_input`.

10.  **Проверка достаточности зерна для посева**:
    - `while True:`: Цикл для проверки хватает ли зерна для посева.
    - `if grain < grain_to_plant:`: Проверяет достаточно ли зерна для посева, если нет, выводит сообщение об ошибке и запрашивает новый ввод.
    - `break`: Если ввод корректен, цикл завершается.

11. **Вычисление урожая**:
    - `yield_per_acre = random.randint(1, 8)`: Генерирует случайное количество урожая от 1 до 8 бушелей на акр.
    - `harvest = grain_to_plant * yield_per_acre`: Вычисляет общий урожай.
    - `grain += harvest`: Добавляет урожай к общему запасу зерна.

12. **Расчет ущерба от крыс**:
    - `rats_damage = int(random.random() * 0.1 * grain)`: Вычисляет случайный ущерб от крыс (от 0 до 10% запасов зерна).
    - `grain -= rats_damage`: Уменьшает количество зерна на величину ущерба от крыс.
    - `print(f"Крысы съели {rats_damage} бушелей зерна.")`: Выводит сообщение о количестве зерна, съеденном крысами.

13. **Ввод количества зерна для пропитания**:
   -  `grain_to_feed = get_int_input("Сколько зерна отдать на пропитание? ")`: Запрашивает у пользователя количество зерна для пропитания, используя функцию `get_int_input`.

14. **Проверка достаточности зерна для пропитания**:
    - `if grain_to_feed >= population:`: Проверяет достаточно ли зерна для пропитания всего населения
    - `population = min(1000, int(population * 1.1))`: Если зерна достаточно, увеличивает население на 10%, но не более 1000.
    - `grain -= grain_to_feed`: Уменьшает запасы зерна на количество, отданное для пропитания.
    - `else:`: Если зерна не хватает.
    - `starved = int(population * (1 - grain_to_feed / population))`: Вычисляет количество умерших от голода.
    - `population -= starved`: Уменьшает население на количество умерших.
    - `print(f"{starved} человек умерло от голода.")`: Выводит сообщение о количестве умерших от голода.
    - `if population <= 0:`: Если население умерло, выводится сообщение о проигрыше.

15. **Увеличение года**:
   -  `year += 1`: Увеличивает текущий год на 1.

16. **Завершение игры**:
   - `if year == 10:`: Если прошло 10 лет, выводится сообщение об окончании игры.
"""
```