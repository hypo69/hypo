# Модуль для проведения экспериментов A/B-тестирования и анализа TinyTroupe
## Обзор

Модуль `experimentation.py` предоставляет классы для проведения A/B-тестирования, рандомизации и дерандомизации выбора пользователей, а также для управления вмешательствами (interventions) в среде TinyTroupe.

## Подробнее

Модуль содержит классы `ABRandomizer` и `Intervention`.
Класс `ABRandomizer` используется для проведения A/B-тестирования, обеспечивая случайное распределение пользователей по группам и последующую возможность дерандомизации для анализа результатов.

Класс `Intervention` предназначен для моделирования вмешательств в среде TinyTroupe, позволяя изменять поведение агентов или окружающей среды на основе заданных условий.

## Классы

### `ABRandomizer`

**Описание**: Утилитарный класс для рандомизации между двумя опциями и последующей дерандомизации.

**Принцип работы**: Класс `ABRandomizer` принимает имена двух опций (control и treatment), их "слепые" имена (A и B), используемые для представления пользователю, список имен, которые не нужно рандомизировать, и зерно случайности. Он предоставляет методы для случайного переключения между опциями, сохранения информации о переключении и последующей дерандомизации для анализа.

**Аттрибуты**:

- `choices` (dict): Словарь, хранящий информацию о том, были ли переключены опции для каждого элемента.
- `real_name_1` (str): Название первой опции (control).
- `real_name_2` (str): Название второй опции (treatment).
- `blind_name_a` (str): Название первой опции, видимое пользователю (A).
- `blind_name_b` (str): Название второй опции, видимое пользователю (B).
- `passtrough_name` (list): Список имен, которые не нужно рандомизировать.
- `random_seed` (int): Зерно случайности для обеспечения воспроизводимости.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `ABRandomizer`.
- `randomize`: Случайно переключает местами две опции и сохраняет информацию о переключении.
- `derandomize`: Возвращает опции в исходном порядке на основе сохраненной информации о переключении.
- `derandomize_name`: Декодирует выбор пользователя и возвращает соответствующее реальное имя опции.

#### `__init__`

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

**Назначение**: Инициализирует объект класса `ABRandomizer` с заданными параметрами.

**Параметры**:

- `real_name_1` (str): Название первой опции (по умолчанию "control").
- `real_name_2` (str): Название второй опции (по умолчанию "treatment").
- `blind_name_a` (str): Название первой опции, видимое пользователю (по умолчанию "A").
- `blind_name_b` (str): Название второй опции, видимое пользователю (по умолчанию "B").
- `passtrough_name` (list): Список имен, которые не нужно рандомизировать (по умолчанию `[]`).
- `random_seed` (int): Зерно случайности для обеспечения воспроизводимости (по умолчанию 42).

**Как работает функция**:

1.  Инициализируется словарь `self.choices` для хранения информации о рандомизации.
2.  Сохраняются переданные параметры в атрибуты объекта.

```
Инициализация параметров
│
│ Сохранение параметров в атрибуты объекта
↓
Конец
```

**Примеры**:

```python
from tinytroupe.experimentation import ABRandomizer

# Создание экземпляра ABRandomizer с параметрами по умолчанию
randomizer = ABRandomizer()

# Создание экземпляра ABRandomizer с пользовательскими параметрами
randomizer = ABRandomizer(real_name_1="group_a", real_name_2="group_b", blind_name_a="X", blind_name_b="Y", passtrough_name=["id"], random_seed=123)
```

#### `randomize`

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

**Назначение**: Случайно переключает местами две опции и возвращает их.

**Параметры**:

- `i` (int): Индекс элемента.
- `a` (str): Первая опция.
- `b` (str): Вторая опция.

**Возвращает**:

- `tuple`: Кортеж из двух элементов, представляющих опции после возможного переключения.

**Как работает функция**:

1.  Используется `random.Random(self.random_seed).random()` для генерации случайного числа от 0 до 1 с использованием заданного зерна случайности.
2.  Если случайное число меньше 0.5, опции `a` и `b` возвращаются в исходном порядке, и в `self.choices` сохраняется значение `(0, 1)`, указывающее, что переключения не было.
3.  В противном случае опции `a` и `b` переключаются местами, и в `self.choices` сохраняется значение `(1, 0)`, указывающее, что переключение произошло.

```
Генерация случайного числа
│
├── Случайное число < 0.5?
│   ├── Да: Сохранение (0, 1) в self.choices и возврат (a, b)
│   └── Нет: Сохранение (1, 0) в self.choices и возврат (b, a)
│
Конец
```

**Примеры**:

```python
from tinytroupe.experimentation import ABRandomizer

randomizer = ABRandomizer()

# Случайное переключение опций "apple" и "banana" для элемента с индексом 1
option1, option2 = randomizer.randomize(1, "apple", "banana")
print(f"Рандомизированные опции: {option1}, {option2}")

# Случайное переключение опций "red" и "blue" для элемента с индексом 2
option3, option4 = randomizer.randomize(2, "red", "blue")
print(f"Рандомизированные опции: {option3}, {option4}")
```

#### `derandomize`

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

**Назначение**: Возвращает опции в исходном порядке на основе сохраненной информации о переключении.

**Параметры**:

- `i` (int): Индекс элемента.
- `a` (str): Первая опция.
- `b` (str): Вторая опция.

**Возвращает**:

- `tuple`: Кортеж из двух элементов, представляющих опции в исходном порядке.

**Вызывает исключения**:

- `Exception`: Если для элемента `i` не найдена информация о рандомизации.

**Как работает функция**:

1.  Проверяется значение `self.choices[i]`.
2.  Если `self.choices[i]` равно `(0, 1)`, опции `a` и `b` возвращаются в исходном порядке.
3.  Если `self.choices[i]` равно `(1, 0)`, опции `b` и `a` возвращаются в исходном порядке.
4.  Если для элемента `i` не найдена информация о рандомизации, выбрасывается исключение `Exception`.

```
Проверка self.choices[i]
│
├── self.choices[i] == (0, 1)?
│   ├── Да: Возврат (a, b)
│   └── Нет: Проверка self.choices[i] == (1, 0)?
│       ├── Да: Возврат (b, a)
│       └── Нет: Выброс исключения Exception
│
Конец
```

**Примеры**:

```python
from tinytroupe.experimentation import ABRandomizer

randomizer = ABRandomizer()

# Случайное переключение опций "apple" и "banana" для элемента с индексом 1
option1, option2 = randomizer.randomize(1, "apple", "banana")
print(f"Рандомизированные опции: {option1}, {option2}")

# Возврат опций в исходный порядок для элемента с индексом 1
original_option1, original_option2 = randomizer.derandomize(1, "apple", "banana")
print(f"Оригинальные опции: {original_option1}, {original_option2}")
```

#### `derandomize_name`

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

**Назначение**: Декодирует выбор, сделанный пользователем, и возвращает соответствующее реальное имя опции.

**Параметры**:

- `i` (int): Индекс элемента.
- `blind_name` (str): Выбор, сделанный пользователем (слепое имя опции).

**Возвращает**:

- `str`: Реальное имя опции, соответствующее выбору пользователя.

**Вызывает исключения**:

- `Exception`: Если для элемента `i` не найдена информация о рандомизации.
- `Exception`: Если выбор пользователя не распознан.

**Как работает функция**:

1.  Проверяется значение `self.choices[i]`.
2.  Если `self.choices[i]` равно `(0, 1)`, проверяется значение `blind_name`.
    - Если `blind_name` равно `self.blind_name_a`, возвращается `self.real_name_1`.
    - Если `blind_name` равно `self.blind_name_b`, возвращается `self.real_name_2`.
    - Если `blind_name` содержится в `self.passtrough_name`, возвращается `blind_name`.
    - В противном случае выбрасывается исключение `Exception`.
3.  Если `self.choices[i]` равно `(1, 0)`, проверяется значение `blind_name`.
    - Если `blind_name` равно `self.blind_name_a`, возвращается `self.real_name_2`.
    - Если `blind_name` равно `self.blind_name_b`, возвращается `self.real_name_1`.
    - Если `blind_name` содержится в `self.passtrough_name`, возвращается `blind_name`.
    - В противном случае выбрасывается исключение `Exception`.
4.  Если для элемента `i` не найдена информация о рандомизации, выбрасывается исключение `Exception`.

```
Проверка self.choices[i]
│
├── self.choices[i] == (0, 1)?
│   ├── Да: Проверка blind_name
│   │   ├── blind_name == self.blind_name_a?
│   │   │   ├── Да: Возврат self.real_name_1
│   │   │   └── Нет: Проверка blind_name == self.blind_name_b?
│   │   │       ├── Да: Возврат self.real_name_2
│   │   │       └── Нет: Проверка blind_name in self.passtrough_name?
│   │   │           ├── Да: Возврат blind_name
│   │   │           └── Нет: Выброс исключения Exception
│   │   └── ...
│   └── Нет: Проверка self.choices[i] == (1, 0)?
│       ├── Да: Проверка blind_name
│       │   ├── blind_name == self.blind_name_a?
│       │   │   ├── Да: Возврат self.real_name_2
│       │   │   └── Нет: Проверка blind_name == self.blind_name_b?
│       │   │       ├── Да: Возврат self.real_name_1
│       │   │       └── Нет: Проверка blind_name in self.passtrough_name?
│       │   │           ├── Да: Возврат blind_name
│       │   │           └── Нет: Выброс исключения Exception
│       │   └── ...
│       └── Нет: Выброс исключения Exception
│
Конец
```

**Примеры**:

```python
from tinytroupe.experimentation import ABRandomizer

randomizer = ABRandomizer(real_name_1="group_a", real_name_2="group_b", blind_name_a="X", blind_name_b="Y")

# Случайное переключение опций для элемента с индексом 1
randomizer.randomize(1, "group_a", "group_b")

# Определение реального имени опции, выбранной пользователем (X) для элемента с индексом 1
real_name = randomizer.derandomize_name(1, "X")
print(f"Реальное имя опции: {real_name}")

# Определение реального имени опции, выбранной пользователем (Y) для элемента с индексом 1
real_name = randomizer.derandomize_name(1, "Y")
print(f"Реальное имя опции: {real_name}")
```

### `Intervention`

**Описание**: Класс для представления и применения вмешательств (interventions) в среде TinyTroupe.

**Принцип работы**: Класс `Intervention` принимает агентов и/или окружения, на которые будет оказано воздействие. Он позволяет задавать предусловия в виде текста или функций, а также функцию, определяющую эффект вмешательства. Методы класса позволяют проверить предусловия и применить эффект вмешательства.

**Атрибуты**:

- `agents` (list): Список агентов, на которых оказывается воздействие.
- `environments` (list): Список окружений, на которые оказывается воздействие.
- `text_precondition` (str): Текстовое описание предусловия.
- `precondition_func` (function): Функция, определяющая предусловие.
- `effect_func` (function): Функция, определяющая эффект вмешательства.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `Intervention`.
- `check_precondition`: Проверяет, выполнено ли предусловие для вмешательства.
- `apply`: Применяет эффект вмешательства.
- `set_textual_precondition`: Устанавливает предусловие в виде текста.
- `set_functional_precondition`: Устанавливает предусловие в виде функции.
- `set_effect`: Устанавливает эффект вмешательства.

#### `__init__`

```python
def __init__(self, agent=None, agents:list=None, environment=None, environments:list=None):
    """
    Initialize the intervention.

    Args:
        agent (TinyPerson): the agent to intervene on
        environment (TinyWorld): the environment to intervene on
    """
    ...
```

**Назначение**: Инициализирует объект класса `Intervention` с заданными агентами и/или окружениями.

**Параметры**:

- `agent` (TinyPerson, optional): Агент, на которого оказывается воздействие.
- `agents` (list, optional): Список агентов, на которых оказывается воздействие.
- `environment` (TinyWorld, optional): Окружение, на которое оказывается воздействие.
- `environments` (list, optional): Список окружений, на которые оказывается воздействие.

**Вызывает исключения**:

- `Exception`: Если переданы одновременно `agent` и `agents` или `environment` и `environments`.
- `Exception`: Если не передан ни один из параметров (`agent`, `agents`, `environment`, `environments`).

**Как работает функция**:

1.  Проверяется, что переданы либо `agent`, либо `agents`, но не оба одновременно.
2.  Проверяется, что переданы либо `environment`, либо `environments`, но не оба одновременно.
3.  Проверяется, что передан хотя бы один из параметров.
4.  Инициализируются атрибуты `self.agents` и `self.environments` в зависимости от переданных параметров.
5.  Инициализируются атрибуты `self.text_precondition`, `self.precondition_func` и `self.effect_func` значением `None`.

```
Проверка параметров
│
├── agent и agents переданы вместе?
│   ├── Да: Выброс исключения Exception
│   └── Нет: Проверка environment и environments переданы вместе?
│       ├── Да: Выброс исключения Exception
│       └── Нет: Проверка, что хотя бы один параметр передан
│           ├── Нет: Выброс исключения Exception
│           └── Да: Инициализация атрибутов self.agents и self.environments
│               │
│               └── Инициализация атрибутов self.text_precondition, self.precondition_func и self.effect_func значением None
│
Конец
```

**Примеры**:

```python
from tinytroupe.experimentation import Intervention
from tinytroupe.agent import TinyPerson

# Создание экземпляра Intervention с агентом
agent = TinyPerson()
intervention = Intervention(agent=agent)

# Создание экземпляра Intervention со списком агентов
agents = [TinyPerson(), TinyPerson()]
intervention = Intervention(agents=agents)
```

#### `check_precondition`

```python
def check_precondition(self):
    """
    Check if the precondition for the intervention is met.
    """
    ...
```

**Назначение**: Проверяет, выполнено ли предусловие для вмешательства.

**Вызывает исключения**:

- `NotImplementedError`: Метод требует переопределения в подклассах.

**Как работает функция**:

1. Выбрасывает исключение `NotImplementedError`, указывающее, что метод должен быть переопределен в подклассах для реализации конкретной логики проверки предусловия.

#### `apply`

```python
def apply(self):
    """
    Apply the intervention.
    """
    ...
```

**Назначение**: Применяет эффект вмешательства.

**Как работает функция**:

1. Вызывает функцию `self.effect_func` с аргументами `self.agents` и `self.environments`.

```
Вызов self.effect_func(self.agents, self.environments)
│
Конец
```

#### `set_textual_precondition`

```python
def set_textual_precondition(self, text):
    """
    Set a precondition as text, to be interpreted by a language model.

    Args:
        text (str): the text of the precondition
    """
    ...
```

**Назначение**: Устанавливает предусловие в виде текста.

**Параметры**:

- `text` (str): Текст предусловия.

**Как работает функция**:

1. Сохраняет текст предусловия в атрибут `self.text_precondition`.

```
Сохранение текста в self.text_precondition
│
Конец
```

#### `set_functional_precondition`

```python
def set_functional_precondition(self, func):
    """
    Set a precondition as a function, to be evaluated by the code.

    Args:
        func (function): the function of the precondition. 
          Must have the arguments: agent, agents, environment, environments.
    """
    ...
```

**Назначение**: Устанавливает предусловие в виде функции.

**Параметры**:

- `func` (function): Функция предусловия. Функция должна принимать аргументы `agent`, `agents`, `environment`, `environments`.

**Как работает функция**:

1. Сохраняет функцию предусловия в атрибут `self.precondition_func`.

```
Сохранение функции в self.precondition_func
│
Конец
```

#### `set_effect`

```python
def set_effect(self, effect_func):
    """
    Set the effect of the intervention.

    Args:
        effect (str): the effect function of the intervention
    """
    ...
```

**Назначение**: Устанавливает эффект вмешательства.

**Параметры**:

- `effect_func` (function): Функция, определяющая эффект вмешательства.

**Как работает функция**:

1. Сохраняет функцию эффекта в атрибут `self.effect_func`.

```
Сохранение функции в self.effect_func
│
Конец