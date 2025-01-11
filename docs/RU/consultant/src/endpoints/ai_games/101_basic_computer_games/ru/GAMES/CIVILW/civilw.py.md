# Анализ кода модуля `civilw.py`

**Качество кода**
7
-  Плюсы
    - Код достаточно хорошо структурирован и понятен.
    - Присутствуют комментарии, объясняющие основные этапы игры.
    - Реализована логика игры в соответствии с описанием.
    - Есть проверка ввода данных на корректность (целые числа).
    - Использованы циклы для обеспечения повторного ввода данных при неверном вводе.

-  Минусы
    -  Отсутствует документация в формате reStructuredText (RST) для модуля, функций и переменных.
    -  Используется `print` для вывода сообщений, вместо логирования.
    -  Использованы стандартные блоки `try-except` вместо обработки ошибок с помощью `logger.error`.
    -  Нет обработки ошибок, связанных с некорректным вводом данных (например, ввод букв).
    -  Нет явных функций для разделения логики игры.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Добавить docstring в формате reStructuredText (RST) в начало файла для описания модуля.
    -   Добавить docstring в формате reStructuredText (RST) для каждой переменной и цикла.
2.  **Логирование**:
    -   Использовать `from src.logger.logger import logger` для логирования ошибок вместо `print`.
    -   Заменить все `print` на `logger.info` для информационных сообщений.
3.  **Обработка ошибок**:
    -   Использовать `logger.error` для обработки ошибок ввода данных, вместо `print`.
    -   Убрать избыточные блоки `try-except`, где это возможно, и использовать `logger.error` в случае ошибок.
4.  **Рефакторинг**:
    -   Разделить код на функции для лучшей читаемости и повторного использования. Например, функции для ввода данных, расчета потерь, обновления численности армий и проверки условий победы.
5.  **Улучшение читаемости**:
    -   Использовать более описательные имена переменных.
    -   Добавить комментарии, объясняющие каждый шаг в игровом процессе.

**Оптимизированный код**

```python
"""
Модуль CIVILW: Симуляция Гражданской войны
=========================================================================================

Этот модуль представляет собой симуляцию сражения между двумя армиями: Конфедерацией и Союзом.
Игрок управляет Конфедерацией и принимает решения о численности своих войск и типе атак.

:py:data:`union_force`: Начальная численность армии Союза.
:py:data:`confederate_force`: Начальная численность армии Конфедерации.

Правила игры:
1.  Игрок управляет армией Конфедерации и должен победить армию Союза.
2.  Игрок вводит количество солдат для атаки.
3.  Игрок выбирает тип атаки: прямая (1) или обходная (2).
4.  В зависимости от выбора игрока и случайных факторов, производится расчет потерь для обеих сторон.
5.  После каждого сражения, игра выводит текущую численность войск обеих сторон.
6.  Игра завершается победой одной из сторон, когда численность войск противника становится равна или меньше 0.

Пример использования:
--------------------

.. code-block:: python

    python civilw.py

"""
import random
from src.logger.logger import logger # Добавлен импорт logger

# Начальная численность армий
union_force = 1000  # Армия Союза
confederate_force = 800  # Армия Конфедерации


def get_attack_force(confederate_force: int) -> int:
    """
    Запрашивает у игрока количество солдат для атаки.

    :param confederate_force: Текущая численность армии Конфедерации.
    :return: Количество солдат для атаки.
    """
    while True:
        try:
            attack_force = int(input("Введите количество солдат для атаки (Конфедерация): "))
            if attack_force > confederate_force:
                logger.info("Недостаточно сил! Попробуйте еще раз.")
            else:
                return attack_force
        except ValueError:
            logger.error("Пожалуйста, введите целое число.")
            # logger.error используется вместо print, для вывода ошибки


def get_attack_type() -> int:
    """
    Запрашивает у игрока тип атаки.

    :return: Тип атаки (1 - прямая, 2 - обходная).
    """
    while True:
        try:
            attack_type = int(input("Выберите тип атаки (1 - прямая, 2 - обходная): "))
            if attack_type in [1, 2]:
                return attack_type
            else:
                logger.info("Неверный тип атаки, попробуйте еще раз")
        except ValueError:
            logger.error("Пожалуйста, введите целое число 1 или 2.")
            # logger.error используется вместо print, для вывода ошибки


def calculate_confederate_losses(attack_force: int, attack_type: int) -> int:
    """
    Рассчитывает потери Конфедерации в зависимости от типа атаки.

    :param attack_force: Количество атакующих солдат.
    :param attack_type: Тип атаки (1 - прямая, 2 - обходная).
    :return: Потери Конфедерации.
    """
    if attack_type == 1:  # Прямая атака
        confederate_losses = int(attack_force * random.random() * 0.4)
    else:  # Обходной маневр
        confederate_losses = int(attack_force * random.random() * 0.2)

    if confederate_losses > attack_force:
        confederate_losses = attack_force
    return confederate_losses


def calculate_union_losses(attack_force: int, attack_type: int) -> int:
    """
    Рассчитывает потери Союза в зависимости от типа атаки.

    :param attack_force: Количество атакующих солдат.
    :param attack_type: Тип атаки (1 - прямая, 2 - обходная).
    :return: Потери Союза.
    """
    union_losses = int(attack_force * random.random() * 0.3)
    if attack_type == 2:
        union_losses += random.randint(0, 100)
    return union_losses


def update_forces(confederate_force: int, union_force: int, confederate_losses: int, union_losses: int) -> tuple[int, int]:
    """
    Обновляет численность армий после сражения.

    :param confederate_force: Текущая численность армии Конфедерации.
    :param union_force: Текущая численность армии Союза.
    :param confederate_losses: Потери Конфедерации.
    :param union_losses: Потери Союза.
    :return: Новая численность армии Конфедерации и Союза.
    """
    confederate_force -= confederate_losses
    union_force -= union_losses
    return confederate_force, union_force


def check_victory(confederate_force: int, union_force: int) -> bool:
    """
    Проверяет условия победы одной из сторон.

    :param confederate_force: Текущая численность армии Конфедерации.
    :param union_force: Текущая численность армии Союза.
    :return: True, если игра окончена, False в противном случае.
    """
    if union_force <= 0:
        logger.info("Конфедерация победила!")
        return True
    elif confederate_force <= 0:
        logger.info("Союз победил!")
        return True
    return False


# Основной игровой цикл
while union_force > 0 and confederate_force > 0:
    # Запрос количества солдат для атаки
    attack_force = get_attack_force(confederate_force)
    # Запрос типа атаки
    attack_type = get_attack_type()

    # Расчет потерь Конфедерации
    confederate_losses = calculate_confederate_losses(attack_force, attack_type)
    # Расчет потерь Союза
    union_losses = calculate_union_losses(attack_force, attack_type)

    # Обновление численности армий
    confederate_force, union_force = update_forces(confederate_force, union_force, confederate_losses, union_losses)
    # Вывод текущей численности армий
    logger.info(f"Конфедерация: {confederate_force} солдат") # изменено на logger.info
    logger.info(f"Союз: {union_force} солдат") # изменено на logger.info

    # Проверка условий победы
    if check_victory(confederate_force, union_force):
        break
```