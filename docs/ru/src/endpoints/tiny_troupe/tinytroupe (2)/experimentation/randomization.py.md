# Модуль для рандомизации A/B тестов
=================================================

Модуль содержит класс `ABRandomizer`, который используется для проведения A/B-тестирования, рандомизации выбора между двумя опциями и последующей дерандомизации.

## Обзор

Модуль `randomization.py` предоставляет класс `ABRandomizer`, который позволяет проводить A/B-тестирование с возможностью рандомизации и дерандомизации выбора между двумя вариантами. Он предназначен для использования в экспериментах, где необходимо представить пользователям варианты в случайном порядке, а затем анализировать их выбор, учитывая эту рандомизацию.

## Подробней

Класс `ABRandomizer` инициализируется с указанием реальных имен вариантов, их "слепых" имен (представленных пользователю) и списка имен, которые не должны быть рандомизированы. Он предоставляет методы для рандомизации вариантов, их дерандомизации и декодирования выбора пользователя с учетом проведенной рандомизации.

## Классы

### `ABRandomizer`

**Описание**: Класс для проведения A/B-тестирования с возможностью рандомизации и дерандомизации вариантов.

**Принцип работы**:
1.  При инициализации класса задаются реальные имена двух вариантов (`real_name_1`, `real_name_2`), их "слепые" имена (`blind_name_a`, `blind_name_b`), список имен, которые не должны быть рандомизированы (`passtrough_name`), и зерно для генератора случайных чисел (`random_seed`).
2.  Метод `randomize` случайным образом меняет местами два варианта и сохраняет информацию о том, была ли произведена замена.
3.  Метод `derandomize` возвращает варианты в исходном порядке на основе сохраненной информации.
4.  Метод `derandomize_name` декодирует выбор пользователя, учитывая, была ли произведена рандомизация.

**Аттрибуты**:

*   `choices (dict)`: Словарь, хранящий информацию о том, какие варианты были переключены для каждого элемента. Ключом является индекс элемента, значением - кортеж (0, 1) или (1, 0), указывающий на порядок вариантов после рандомизации.
*   `real_name_1 (str)`: Реальное имя первого варианта.
*   `real_name_2 (str)`: Реальное имя второго варианта.
*   `blind_name_a (str)`: "Слепое" имя первого варианта (отображаемое пользователю).
*   `blind_name_b (str)`: "Слепое" имя второго варианта (отображаемое пользователю).
*   `passtrough_name (list)`: Список имен, которые не должны быть рандомизированы.
*   `random_seed (int)`: Зерно для генератора случайных чисел, обеспечивающее воспроизводимость рандомизации.

**Методы**:

*   `__init__(self, real_name_1="control", real_name_2="treatment", blind_name_a="A", blind_name_b="B", passtrough_name=[], random_seed=42)`: Инициализирует экземпляр класса `ABRandomizer`.
*   `randomize(self, i, a, b)`: Случайным образом меняет местами варианты `a` и `b` и возвращает их.
*   `derandomize(self, i, a, b)`: Возвращает варианты `a` и `b` в исходном порядке, учитывая рандомизацию.
*   `derandomize_name(self, i, blind_name)`: Декодирует выбор пользователя (`blind_name`) и возвращает реальное имя выбранного варианта.

### `__init__`

```python
def __init__(self, real_name_1="control", real_name_2="treatment",
                       blind_name_a="A", blind_name_b="B",
                       passtrough_name=[],
                       random_seed=42):
    """
    An utility class to randomize between two options, and de-randomize later.
    The choices are stored in a dictionary, with the index of the item as the key.
    The real names are the names of the options as they are in the data, and the blind names
    are the names of the options as they are presented to the user. Finally, the passtrough names
    are names that are not randomized, but are always returned as-is.

    Args:
        real_name_1 (str): the name of the first option
        real_name_2 (str): the name of the second option
        blind_name_a (str): the name of the first option as seen by the user
        blind_name_b (str): the name of the second option as seen by the user
        passtrough_name (list): a list of names that should not be randomized and are always
                                returned as-is.
        random_seed (int): the random seed to use
    """
    ...
```

**Назначение**: Инициализация экземпляра класса `ABRandomizer`.

**Параметры**:

*   `real_name_1 (str)`: Реальное имя первого варианта. По умолчанию "control".
*   `real_name_2 (str)`: Реальное имя второго варианта. По умолчанию "treatment".
*   `blind_name_a (str)`: "Слепое" имя первого варианта (отображаемое пользователю). По умолчанию "A".
*   `blind_name_b (str)`: "Слепое" имя второго варианта (отображаемое пользователю). По умолчанию "B".
*   `passtrough_name (list)`: Список имен, которые не должны быть рандомизированы. По умолчанию пустой список `[]`.
*   `random_seed (int)`: Зерно для генератора случайных чисел, обеспечивающее воспроизводимость рандомизации. По умолчанию `42`.

**Как работает функция**:

1.  Инициализирует словарь `self.choices` для хранения информации о рандомизации.
2.  Сохраняет переданные параметры в атрибуты экземпляра класса.

### `randomize`

```python
def randomize(self, i, a, b):
    """
    Randomly switch between a and b, and return the choices.
    Store whether the a and b were switched or not for item i, to be able to
    de-randomize later.

    Args:
        i (int): index of the item
        a (str): first choice
        b (str): second choice
    """
    ...
```

**Назначение**: Случайным образом меняет местами два варианта (`a` и `b`) и возвращает их.

**Параметры**:

*   `i (int)`: Индекс элемента.
*   `a (str)`: Первый вариант.
*   `b (str)`: Второй вариант.

**Возвращает**:

*   Кортеж из двух строк: `(a, b)` или `(b, a)` в случайном порядке.

**Как работает функция**:

1.  Инициализирует генератор случайных чисел с зерном `self.random_seed`.
2.  Если случайное число меньше 0.5, то сохраняет в `self.choices[i]` кортеж `(0, 1)` и возвращает `(a, b)`.
3.  Иначе сохраняет в `self.choices[i]` кортеж `(1, 0)` и возвращает `(b, a)`.

```
Начало
|
-- Генерация случайного числа < 0.5?
|   да
|   |
|   -- self.choices[i] = (0, 1)
|   |
|   -- Возврат (a, b)
|   |
|   Конец
|
нет
|
-- self.choices[i] = (1, 0)
|
-- Возврат (b, a)
|
Конец
```

**Примеры**:

```python
randomizer = ABRandomizer()
a, b = randomizer.randomize(1, "вариант_A", "вариант_B")
print(f"После рандомизации: a = {a}, b = {b}")
```

### `derandomize`

```python
def derandomize(self, i, a, b):
    """
    De-randomize the choices for item i, and return the choices.

    Args:
        i (int): index of the item
        a (str): first choice
        b (str): second choice
    """
    ...
```

**Назначение**: Возвращает варианты `a` и `b` в исходном порядке, учитывая рандомизацию.

**Параметры**:

*   `i (int)`: Индекс элемента.
*   `a (str)`: Первый вариант.
*   `b (str)`: Второй вариант.

**Возвращает**:

*   Кортеж из двух строк: `(a, b)` или `(b, a)` в исходном порядке.

**Вызывает исключения**:

*   `Exception`: Если для элемента `i` не найдена информация о рандомизации.

**Как работает функция**:

1.  Проверяет значение `self.choices[i]`.
2.  Если `self.choices[i]` равно `(0, 1)`, возвращает `(a, b)`.
3.  Если `self.choices[i]` равно `(1, 0)`, возвращает `(b, a)`.
4.  Иначе вызывает исключение `Exception` с сообщением "No randomization found for item {i}".

```
Начало
|
-- Проверка self.choices[i]
|
-- self.choices[i] == (0, 1)?
|   да
|   |
|   -- Возврат (a, b)
|   |
|   Конец
|
нет
|
-- self.choices[i] == (1, 0)?
|   да
|   |
|   -- Возврат (b, a)
|   |
|   Конец
|
нет
|
-- Вызов исключения Exception("No randomization found for item {i}")
|
Конец
```

**Примеры**:

```python
randomizer = ABRandomizer()
a, b = randomizer.randomize(1, "вариант_A", "вариант_B")
a, b = randomizer.derandomize(1, "вариант_A", "вариант_B")
print(f"После дерандомизации: a = {a}, b = {b}")
```

### `derandomize_name`

```python
def derandomize_name(self, i, blind_name):
    """
    Decode the choice made by the user, and return the choice. 

    Args:
        i (int): index of the item
        choice_name (str): the choice made by the user
    """
    ...
```

**Назначение**: Декодирует выбор пользователя (`blind_name`) и возвращает реальное имя выбранного варианта.

**Параметры**:

*   `i (int)`: Индекс элемента.
*   `blind_name (str)`: "Слепое" имя варианта, выбранного пользователем.

**Возвращает**:

*   Строка: Реальное имя выбранного варианта.

**Вызывает исключения**:

*   `Exception`: Если для элемента `i` не найдена информация о рандомизации или если `blind_name` не распознано.

**Как работает функция**:

1.  Проверяет значение `self.choices[i]`.
2.  Если `self.choices[i]` равно `(0, 1)`:
    *   Если `blind_name` равно `self.blind_name_a`, возвращает `self.real_name_1`.
    *   Если `blind_name` равно `self.blind_name_b`, возвращает `self.real_name_2`.
    *   Если `blind_name` находится в `self.passtrough_name`, возвращает `blind_name`.
    *   Иначе вызывает исключение `Exception` с сообщением "Choice '{blind_name}' not recognized".
3.  Если `self.choices[i]` равно `(1, 0)`:
    *   Если `blind_name` равно `self.blind_name_a`, возвращает `self.real_name_2`.
    *   Если `blind_name` равно `self.blind_name_b`, возвращает `self.real_name_1`.
    *   Если `blind_name` находится в `self.passtrough_name`, возвращает `blind_name`.
    *   Иначе вызывает исключение `Exception` с сообщением "Choice '{blind_name}' not recognized".
4.  Иначе вызывает исключение `Exception` с сообщением "No randomization found for item {i}".

```
Начало
|
-- Проверка self.choices[i]
|
-- self.choices[i] == (0, 1)?
|   да
|   |
|   -- Проверка blind_name
|   |
|   -- blind_name == self.blind_name_a?
|   |   да
|   |   |
|   |   -- Возврат self.real_name_1
|   |   |
|   |   Конец
|   |
|   нет
|   |
|   -- blind_name == self.blind_name_b?
|   |   да
|   |   |
|   |   -- Возврат self.real_name_2
|   |   |
|   |   Конец
|   |
|   нет
|   |
|   -- blind_name in self.passtrough_name?
|   |   да
|   |   |
|   |   -- Возврат blind_name
|   |   |
|   |   Конец
|   |
|   нет
|   |
|   -- Вызов исключения Exception("Choice '{blind_name}' not recognized")
|   |
|   Конец
|
нет
|
-- self.choices[i] == (1, 0)?
|   да
|   |
|   -- Проверка blind_name
|   |
|   -- blind_name == self.blind_name_a?
|   |   да
|   |   |
|   |   -- Возврат self.real_name_2
|   |   |
|   |   Конец
|   |
|   нет
|   |
|   -- blind_name == self.blind_name_b?
|   |   да
|   |   |
|   |   -- Возврат self.real_name_1
|   |   |
|   |   Конец
|   |
|   нет
|   |
|   -- blind_name in self.passtrough_name?
|   |   да
|   |   |
|   |   -- Возврат blind_name
|   |   |
|   |   Конец
|   |
|   нет
|   |
|   -- Вызов исключения Exception("Choice '{blind_name}' not recognized")
|   |
|   Конец
|
нет
|
-- Вызов исключения Exception("No randomization found for item {i}")
|
Конец
```

**Примеры**:

```python
randomizer = ABRandomizer(real_name_1="control_group", real_name_2="treatment_group", blind_name_a="A", blind_name_b="B")
randomizer.randomize(1, "A", "B")
choice = randomizer.derandomize_name(1, "A")
print(f"Выбор пользователя: {choice}")
```
```python
randomizer = ABRandomizer(real_name_1="control_group", real_name_2="treatment_group", blind_name_a="A", blind_name_b="B", passtrough_name=["C"])
randomizer.randomize(1, "A", "B")
choice = randomizer.derandomize_name(1, "C")
print(f"Выбор пользователя: {choice}")
```
```python
randomizer = ABRandomizer(real_name_1="control_group", real_name_2="treatment_group", blind_name_a="A", blind_name_b="B")
randomizer.randomize(1, "A", "B")
try:
    choice = randomizer.derandomize_name(1, "C")
except Exception as ex:
    print(f"Возникло исключение: {ex}")
```
## Функции

В данном модуле нет отдельных функций, только класс `ABRandomizer` с его методами.