# Модуль для рандомизации A/B-тестов
## Обзор

Модуль предоставляет класс `ABRandomizer`, который используется для проведения A/B-тестов, позволяя рандомизировать выбор между двумя опциями и восстанавливать исходный выбор позже. Он особенно полезен в задачах, где необходимо скрыть реальные имена опций от пользователя.

## Подробнее

Этот модуль предназначен для упрощения процесса A/B-тестирования, обеспечивая возможность как случайного выбора между двумя вариантами, так и восстановления исходного варианта выбора. Это полезно, когда нужно скрыть реальные названия вариантов от пользователя во время эксперимента. Класс `ABRandomizer` позволяет инициализировать различные параметры, такие как имена вариантов, имена для отображения пользователю и зерно случайности, что обеспечивает воспроизводимость результатов.

## Классы

### `ABRandomizer`

**Описание**: Класс для рандомизации и дерандомизации вариантов в A/B-тестах.

**Принцип работы**:

1.  Инициализация класса `ABRandomizer` с указанием реальных имен вариантов, имен для отображения пользователю и списка вариантов, которые не нужно рандомизировать.
2.  Метод `randomize` случайным образом выбирает один из двух вариантов и сохраняет информацию о выборе для последующей дерандомизации.
3.  Метод `derandomize` восстанавливает исходный порядок вариантов на основе сохраненной информации.
4.  Метод `derandomize_name` декодирует выбор пользователя, возвращая реальное имя выбранного варианта.

**Атрибуты**:

*   `choices` (dict): Словарь, хранящий информацию о том, какие варианты были переключены для каждого элемента.
*   `real_name_1` (str): Реальное имя первого варианта.
*   `real_name_2` (str): Реальное имя второго варианта.
*   `blind_name_a` (str): Имя первого варианта, отображаемое пользователю.
*   `blind_name_b` (str): Имя второго варианта, отображаемое пользователю.
*   `passtrough_name` (list): Список имен, которые не должны быть рандомизированы.
*   `random_seed` (int): Зерно случайности для воспроизводимости результатов.

**Методы**:

*   `__init__(self, real_name_1="control", real_name_2="treatment", blind_name_a="A", blind_name_b="B", passtrough_name=[], random_seed=42)`: Инициализирует класс `ABRandomizer`.
*   `randomize(self, i, a, b)`: Рандомизирует порядок двух вариантов.
*   `derandomize(self, i, a, b)`: Восстанавливает исходный порядок вариантов.
*   `derandomize_name(self, i, blind_name)`: Декодирует выбор пользователя и возвращает реальное имя варианта.

## Функции

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
        are names that are not randomized, but are always returned as-is.\n
        Args:\n
            real_name_1 (str): the name of the first option\n
            real_name_2 (str): the name of the second option\n
            blind_name_a (str): the name of the first option as seen by the user\n
            blind_name_b (str): the name of the second option as seen by the user\n
            passtrough_name (list): a list of names that should not be randomized and are always\n
                                    returned as-is.\n
            random_seed (int): the random seed to use\n
        """
```

**Назначение**: Инициализирует объект класса `ABRandomizer` с заданными параметрами.

**Параметры**:

*   `real_name_1` (str): Реальное имя первого варианта (по умолчанию "control").
*   `real_name_2` (str): Реальное имя второго варианта (по умолчанию "treatment").
*   `blind_name_a` (str): Имя первого варианта, отображаемое пользователю (по умолчанию "A").
*   `blind_name_b` (str): Имя второго варианта, отображаемое пользователю (по умолчанию "B").
*   `passtrough_name` (list): Список имен, которые не должны быть рандомизированы и всегда возвращаются как есть (по умолчанию `[]`).
*   `random_seed` (int): Зерно случайности для воспроизводимости результатов (по умолчанию 42).

**Как работает функция**:

1.  Инициализирует словарь `self.choices` для хранения информации о переключениях вариантов.
2.  Устанавливает значения атрибутов `self.real_name_1`, `self.real_name_2`, `self.blind_name_a`, `self.blind_name_b`, `self.passtrough_name` и `self.random_seed` на основе переданных аргументов.

```
Инициализация --> Установка атрибутов
```

**Примеры**:

```python
randomizer = ABRandomizer()
randomizer = ABRandomizer(real_name_1="Контроль", real_name_2="Тест", blind_name_a="Вариант A", blind_name_b="Вариант B", passtrough_name=["Не менять"], random_seed=123)
```

### `randomize`

```python
    def randomize(self, i, a, b):
        """
        Randomly switch between a and b, and return the choices.\n
        Store whether the a and b were switched or not for item i, to be able to
        de-randomize later.\n
        Args:\n
            i (int): index of the item\n
            a (str): first choice\n
            b (str): second choice\n
        """
```

**Назначение**: Случайным образом меняет местами два варианта (`a` и `b`) и возвращает их. Сохраняет информацию о том, были ли переставлены варианты, чтобы можно было выполнить дерандомизацию позже.

**Параметры**:

*   `i` (int): Индекс элемента.
*   `a` (str): Первый вариант.
*   `b` (str): Второй вариант.

**Возвращает**:

*   Кортеж из двух элементов: (`a`, `b`) или (`b`, `a`) в зависимости от случайного выбора.

**Как работает функция**:

1.  Использует `random.Random(self.random_seed).random()` для генерации случайного числа в диапазоне от 0 до 1.
2.  Если случайное число меньше 0.5, сохраняет в `self.choices[i]` кортеж `(0, 1)` и возвращает варианты в исходном порядке (`a`, `b`).
3.  Если случайное число больше или равно 0.5, сохраняет в `self.choices[i]` кортеж `(1, 0)` и возвращает варианты в переставленном порядке (`b`, `a`).

```
Генерация случайного числа --> Проверка случайного числа (< 0.5?) --> Сохранение выбора в self.choices и возврат вариантов
```

**Примеры**:

```python
randomizer = ABRandomizer()
a, b = randomizer.randomize(1, "вариант1", "вариант2")
```

### `derandomize`

```python
    def derandomize(self, i, a, b):
        """
        De-randomize the choices for item i, and return the choices.\n
        Args:\n
            i (int): index of the item\n
            a (str): first choice\n
            b (str): second choice\n
        """
```

**Назначение**: Восстанавливает исходный порядок вариантов для элемента с индексом `i` и возвращает их.

**Параметры**:

*   `i` (int): Индекс элемента.
*   `a` (str): Первый вариант.
*   `b` (str): Второй вариант.

**Возвращает**:

*   Кортеж из двух элементов: (`a`, `b`) или (`b`, `a`) в зависимости от того, как они были переставлены при рандомизации.

**Вызывает исключения**:

*   `Exception`: Если для элемента `i` не найдена информация о рандомизации.

**Как работает функция**:

1.  Проверяет значение `self.choices[i]`.
2.  Если `self.choices[i]` равно `(0, 1)`, возвращает варианты в исходном порядке (`a`, `b`).
3.  Если `self.choices[i]` равно `(1, 0)`, возвращает варианты в переставленном порядке (`b`, `a`).
4.  Если для элемента `i` не найдена информация о рандомизации (т.е. `self.choices[i]` не существует), вызывает исключение с сообщением "No randomization found for item {i}".

```
Проверка self.choices[i] --> Возврат вариантов в исходном или переставленном порядке (или вызов исключения)
```

**Примеры**:

```python
randomizer = ABRandomizer()
a, b = randomizer.randomize(1, "вариант1", "вариант2")
a, b = randomizer.derandomize(1, "вариант1", "вариант2")
```

### `derandomize_name`

```python
    def derandomize_name(self, i, blind_name):
        """
        Decode the choice made by the user, and return the choice. \n
        Args:\n
            i (int): index of the item\n
            choice_name (str): the choice made by the user\n
        """
```

**Назначение**: Декодирует выбор, сделанный пользователем, и возвращает соответствующее реальное имя варианта.

**Параметры**:

*   `i` (int): Индекс элемента.
*   `blind_name` (str): Выбор, сделанный пользователем (имя варианта, отображаемое пользователю).

**Возвращает**:

*   Реальное имя выбранного варианта (`self.real_name_1` или `self.real_name_2`) или `blind_name`, если он находится в списке `self.passtrough_name`.

**Вызывает исключения**:

*   `Exception`: Если для элемента `i` не найдена информация о рандомизации или если `blind_name` не распознано.

**Как работает функция**:

1.  Проверяет значение `self.choices[i]`.
2.  Если `self.choices[i]` равно `(0, 1)`:
    *   Если `blind_name` равно `self.blind_name_a`, возвращает `self.real_name_1`.
    *   Если `blind_name` равно `self.blind_name_b`, возвращает `self.real_name_2`.
    *   Если `blind_name` находится в `self.passtrough_name`, возвращает `blind_name`.
    *   В противном случае вызывает исключение с сообщением "Choice '{blind_name}' not recognized".
3.  Если `self.choices[i]` равно `(1, 0)`:
    *   Если `blind_name` равно `self.blind_name_a`, возвращает `self.real_name_2`.
    *   Если `blind_name` равно `self.blind_name_b`, возвращает `self.real_name_1`.
    *   Если `blind_name` находится в `self.passtrough_name`, возвращает `blind_name`.
    *   В противном случае вызывает исключение с сообщением "Choice '{blind_name}' not recognized".
4.  Если для элемента `i` не найдена информация о рандомизации, вызывает исключение с сообщением "No randomization found for item {i}".

```
Проверка self.choices[i] --> Проверка blind_name --> Возврат реального имени варианта (или вызов исключения)
```

**Примеры**:

```python
randomizer = ABRandomizer(real_name_1="вариант1", real_name_2="вариант2", blind_name_a="A", blind_name_b="B", passtrough_name=["не менять"])
randomizer.randomize(1, "A", "B")
real_name = randomizer.derandomize_name(1, "A")