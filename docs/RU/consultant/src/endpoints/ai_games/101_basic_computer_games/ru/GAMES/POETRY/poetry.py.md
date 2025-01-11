# Анализ кода модуля poetry.py

**Качество кода**
7
-  Плюсы
    - Код достаточно хорошо структурирован и понятен.
    -  Присутствует базовая обработка ошибок ввода.
    -  Используются информативные переменные.
-  Минусы
    -  Отсутствует reStructuredText документация для модуля и функции.
    -  Используется стандартный `print` для вывода, что затрудняет интеграцию с системой логирования.
    -  Избыточное использование `try-except` блоков.
    -  Нет импорта модуля `logger` из `src.logger.logger`.
    -  Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -  Дублирование кода при проверке ввода пользователя.

**Рекомендации по улучшению**

1.  Добавить reStructuredText документацию для модуля и функции `change_list`.
2.  Использовать `from src.logger.logger import logger` для логирования ошибок и заменить `print` на `logger.info`, `logger.debug` и `logger.error`.
3.  Избегать избыточного использования `try-except`, обрабатывая ошибки с помощью `logger.error`.
4.  Устранить дублирование кода проверки ввода пользователя, вынеся его в отдельную функцию.
5.  Заменить множественные блоки `if/elif` на `match/case`.
6.  Необходимо добавить импорт `Any` из `typing` для аннотации типов.

**Оптимизированный код**

```python
"""
Модуль для игры в поэзию.
==========================

Этот модуль реализует игру, в которой компьютер генерирует случайные
предложения, выбирая слова из заданных списков. Игрок может влиять на
генерацию, изменяя списки слов.

Основные функции:
- Генерация случайных предложений.
- Изменение списков слов по запросу пользователя.

Пример использования:
---------------------

.. code-block:: python

    python poetry.py
"""
import random
from typing import List, Any
from src.logger.logger import logger

# Начальные списки слов
nouns: List[str] = ["BIRDS", "CATS", "DOGS", "FISH", "TREES", "FLOWERS", "RIVERS", "MOUNTAINS", "CLOUDS", "STARS"]
verbs: List[str] = ["FLY", "RUN", "SWIM", "JUMP", "GROW", "BLOOM", "FLOW", "CLIMB", "FLOAT", "SHINE"]
adjectives: List[str] = ["RED", "BLUE", "GREEN", "YELLOW", "TALL", "SHORT", "BIG", "SMALL", "BRIGHT", "DARK"]
prepositions: List[str] = ["OVER", "UNDER", "IN", "ON", "BY", "NEAR", "THROUGH", "AROUND", "ACROSS", "ALONG"]


def change_list(list_name: str) -> List[str]:
    """
    Изменяет список слов, запрашивая ввод у пользователя.

    :param list_name: Название списка для изменения.
    :type list_name: str
    :return: Новый список слов.
    :rtype: List[str]
    """
    new_list_str = input(f"Введите новые слова для списка {list_name} через запятую: ").upper()
    return new_list_str.split(",")


def get_user_code() -> int | None:
    """
    Запрашивает у пользователя ввод кода и проверяет его на валидность.

    :return: Код, введенный пользователем, или None в случае неверного ввода.
    :rtype: int | None
    """
    user_code_str = input("Введите код (0 для выхода): ")
    if user_code_str == "0":
        return 0
    try:
        return int(user_code_str)
    except ValueError:
        logger.error("Неверный ввод, введите 0, 1, 2, 3 или 4")
        return None


logger.info("Добро пожаловать в игру POETRY!")
logger.info("Нажмите:")
logger.info("1 чтобы поменять существительные")
logger.info("2 чтобы поменять глаголы")
logger.info("3 чтобы поменять прилагательные")
logger.info("4 чтобы поменять предлоги")
logger.info("0 чтобы выйти")

while True:
    # Генерируем случайное число от 1 до 4
    random_number = random.randint(1, 4)

    if random_number == 1:
        # Генерируем предложение
        random_noun = random.choice(nouns)
        random_verb = random.choice(verbs)
        random_adjective = random.choice(adjectives)
        random_preposition = random.choice(prepositions)

        phrase = f"THE {random_adjective} {random_noun} {random_verb} {random_preposition} THE FOREST"
        logger.info(f"Случайная фраза: {phrase}")

        user_code = get_user_code()
        if user_code == 0:
            break
        if user_code is None:
            continue
    else:
        user_code = get_user_code()
        if user_code == 0:
            break
        if user_code is None:
            continue

    match user_code:
        case 1:
            nouns = change_list("существительных")
        case 2:
            verbs = change_list("глаголов")
        case 3:
            adjectives = change_list("прилагательных")
        case 4:
            prepositions = change_list("предлогов")
        case _:
            continue

logger.info("BYE")
"""
Объяснение кода:
1.  **Импорт модулей**:
    - `import random`: Импортирует модуль `random` для генерации случайных чисел и выбора случайных элементов из списка.
    - `from typing import List, Any`: Импортирует `List` и `Any` для аннотации типов.
    - `from src.logger.logger import logger`: Импортирует logger для логирования.

2.  **Инициализация списков слов**:
    - `nouns: List[str] = [...]`: Инициализирует список существительных с аннотацией типа.
    - `verbs: List[str] = [...]`: Инициализирует список глаголов с аннотацией типа.
    - `adjectives: List[str] = [...]`: Инициализирует список прилагательных с аннотацией типа.
    - `prepositions: List[str] = [...]`: Инициализирует список предлогов с аннотацией типа.

3.  **Функция `change_list(list_name: str) -> List[str]`**:
    - Определяет функцию `change_list`, которая позволяет пользователю изменить список слов.
    - `:param list_name: str`: Название списка для изменения.
    - `:return: List[str]`: Новый список слов.
    - `new_list_str = input(...)`: Запрашивает у пользователя ввод новых слов через запятую и преобразует ввод в верхний регистр.
    - `return new_list_str.split(",")`: Возвращает новый список слов.

4. **Функция `get_user_code() -> int | None`**:
    -  Запрашивает ввод кода от пользователя.
    - `:return: int | None`: Возвращает код пользователя в виде целого числа, если ввод корректен. В противном случае возвращает None.
    -  `if user_code_str == "0":`: Проверяет, ввел ли пользователь "0".
    -  `try/except`: обрабатывает неверный ввод.
    -  `logger.error("Неверный ввод, введите 0, 1, 2, 3 или 4")`: Выводит сообщение об ошибке через logger.

5.  **Приветствие и инструкции**:
    - `logger.info("Добро пожаловать в игру POETRY!")`: Выводит приветствие через logger.
    -   Выводит на экран инструкции для пользователя через logger.

6.  **Основной цикл `while True`**:
    - Бесконечный цикл, который продолжается до тех пор, пока пользователь не введет `0`.
    - `random_number = random.randint(1, 4)`: Генерирует случайное число от 1 до 4.

    - **Условие генерации фразы**:
      - `if random_number == 1:`: Проверяет, равно ли случайное число 1.
      - `random_noun = random.choice(nouns)`: Случайно выбирает существительное из списка.
      - `random_verb = random.choice(verbs)`: Случайно выбирает глагол из списка.
      - `random_adjective = random.choice(adjectives)`: Случайно выбирает прилагательное из списка.
      - `random_preposition = random.choice(prepositions)`: Случайно выбирает предлог из списка.
      - `phrase = f"THE {random_adjective} {random_noun} {random_verb} {random_preposition} THE FOREST"`: Формирует случайную фразу.
      - `logger.info(f"Случайная фраза: {phrase}")`: Выводит сгенерированную фразу через logger.
      - `user_code = get_user_code()`: Запрашивает ввод кода пользователя через функцию get_user_code.
       -   `if user_code == 0: break`: Если пользователь вводит `0`, то завершаем цикл.
       - `if user_code is None: continue`: Если ввод не корректный, пропускаем итерацию.

    - **Условие изменения списков**:
      - `else`: Если случайное число не равно 1, то запрашиваем код для изменения списков.
       -   `user_code = get_user_code()`: Запрашивает ввод кода пользователя через функцию get_user_code.
      -   `if user_code == 0: break`: Если пользователь вводит `0`, то завершаем цикл.
      -  `if user_code is None: continue`: Если ввод не корректный, пропускаем итерацию.
    - `match user_code:`: Использует `match/case` для обработки введенного кода.
      - `case 1:`: Если пользователь вводит `1`, то вызываем функцию `change_list` для изменения списка существительных.
      - `case 2:`: Если пользователь вводит `2`, то вызываем функцию `change_list` для изменения списка глаголов.
      - `case 3:`: Если пользователь вводит `3`, то вызываем функцию `change_list` для изменения списка прилагательных.
      - `case 4:`: Если пользователь вводит `4`, то вызываем функцию `change_list` для изменения списка предлогов.
      -  `case _: continue`: Если пользователь вводит некорректный код, то пропускаем итерацию цикла.

7.  **Завершение игры**:
    - `logger.info("BYE")`: Выводит сообщение "BYE" через logger после завершения цикла.
"""
```