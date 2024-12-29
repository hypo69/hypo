# Модуль `experimentation.py`

## Обзор

Модуль `experimentation.py` содержит классы для проведения экспериментов, включая рандомизацию и применение интервенций.

## Содержание

- [Класс `ABRandomizer`](#класс-abrandomizer)
    - [Метод `__init__`](#метод-__init__)
    - [Метод `randomize`](#метод-randomize)
    - [Метод `derandomize`](#метод-derandomize)
    - [Метод `derandomize_name`](#метод-derandomize_name)
- [Класс `Intervention`](#класс-intervention)
    - [Метод `__init__`](#метод-__init__-1)
    - [Метод `check_precondition`](#метод-check_precondition)
    - [Метод `apply`](#метод-apply)
    - [Метод `set_textual_precondition`](#метод-set_textual_precondition)
    - [Метод `set_functional_precondition`](#метод-set_functional_precondition)
    - [Метод `set_effect`](#метод-set_effect)

## Классы

### `ABRandomizer`

**Описание**: Утилитарный класс для рандомизации между двумя вариантами и последующей дерандомизации. Выбор хранится в словаре с индексом элемента в качестве ключа.

**Методы**:
- [`__init__`](#__init__): Инициализирует объект `ABRandomizer`.
- [`randomize`](#randomize): Рандомизирует выбор между `a` и `b`.
- [`derandomize`](#derandomize): Дерандомизирует выбор для элемента с индексом `i`.
- [`derandomize_name`](#derandomize_name): Декодирует выбор, сделанный пользователем, и возвращает реальное имя.

#### `__init__`

```python
def __init__(self, real_name_1="control", real_name_2="treatment",
                       blind_name_a="A", blind_name_b="B",
                       passtrough_name=[],
                       random_seed=42):
```
**Описание**: Инициализирует объект `ABRandomizer` с заданными параметрами.

**Параметры**:
- `real_name_1` (str, optional): Имя первого варианта. По умолчанию "control".
- `real_name_2` (str, optional): Имя второго варианта. По умолчанию "treatment".
- `blind_name_a` (str, optional): Имя первого варианта для отображения пользователю. По умолчанию "A".
- `blind_name_b` (str, optional): Имя второго варианта для отображения пользователю. По умолчанию "B".
- `passtrough_name` (list, optional): Список имен, которые не нужно рандомизировать. По умолчанию `[]`.
- `random_seed` (int, optional): Зерно для генератора случайных чисел. По умолчанию 42.

#### `randomize`

```python
def randomize(self, i, a, b):
```

**Описание**: Рандомно переключает местами `a` и `b` и возвращает выбор. Сохраняет информацию о том, были ли `a` и `b` переключены, чтобы можно было выполнить дерандомизацию.

**Параметры**:
- `i` (int): Индекс элемента.
- `a` (str): Первый вариант.
- `b` (str): Второй вариант.

**Возвращает**:
- `tuple`: Кортеж из `a` и `b` или `b` и `a` в зависимости от рандомизации.

#### `derandomize`

```python
def derandomize(self, i, a, b):
```
**Описание**: Дерандомизирует выбор для элемента с индексом `i` и возвращает исходный порядок.

**Параметры**:
- `i` (int): Индекс элемента.
- `a` (str): Первый вариант.
- `b` (str): Второй вариант.

**Возвращает**:
- `tuple`: Кортеж из `a` и `b` или `b` и `a` в зависимости от сохраненной информации о рандомизации.

**Вызывает исключения**:
- `Exception`: Если для элемента `i` не найдена рандомизация.

#### `derandomize_name`

```python
def derandomize_name(self, i, blind_name):
```

**Описание**: Декодирует выбор, сделанный пользователем, и возвращает реальное имя варианта.

**Параметры**:
- `i` (int): Индекс элемента.
- `blind_name` (str): Имя выбора, сделанного пользователем.

**Возвращает**:
- `str`: Реальное имя выбранного варианта.

**Вызывает исключения**:
- `Exception`: Если для элемента `i` не найдена рандомизация.
- `Exception`: Если имя `blind_name` не распознано.

### `Intervention`

**Описание**: Класс для представления интервенции в эксперименте.

**Методы**:
- [`__init__`](#__init__-1): Инициализирует объект `Intervention`.
- [`check_precondition`](#check_precondition): Проверяет, выполнено ли предусловие для интервенции.
- [`apply`](#apply): Применяет интервенцию.
- [`set_textual_precondition`](#set_textual_precondition): Устанавливает текстовое предусловие для интервенции.
- [`set_functional_precondition`](#set_functional_precondition): Устанавливает функциональное предусловие для интервенции.
- [`set_effect`](#set_effect): Устанавливает эффект интервенции.

#### `__init__`

```python
def __init__(self, agent=None, agents:list=None, environment=None, environments:list=None):
```

**Описание**: Инициализирует объект `Intervention` с заданными агентами и окружениями.

**Параметры**:
- `agent` (TinyPerson, optional): Агент, на которого оказывается воздействие.
- `agents` (list, optional): Список агентов, на которых оказывается воздействие.
- `environment` (TinyWorld, optional): Окружение, на которое оказывается воздействие.
- `environments` (list, optional): Список окружений, на которые оказывается воздействие.

**Вызывает исключения**:
- `Exception`: Если переданы и `agent`, и `agents`, или и `environment`, и `environments`.
- `Exception`: Если не передан ни один из параметров.

#### `check_precondition`

```python
def check_precondition(self):
```
**Описание**: Проверяет, выполнено ли предусловие для интервенции.

**Вызывает исключения**:
- `NotImplementedError`: Метод не реализован.

#### `apply`

```python
def apply(self):
```
**Описание**: Применяет интервенцию, вызывая функцию эффекта.

#### `set_textual_precondition`

```python
def set_textual_precondition(self, text):
```

**Описание**: Устанавливает предусловие в виде текста, который будет интерпретироваться языковой моделью.

**Параметры**:
- `text` (str): Текст предусловия.

#### `set_functional_precondition`

```python
def set_functional_precondition(self, func):
```

**Описание**: Устанавливает предусловие в виде функции, которая будет вычисляться в коде.

**Параметры**:
- `func` (function): Функция предусловия. Функция должна принимать аргументы: `agent`, `agents`, `environment`, `environments`.

#### `set_effect`

```python
def set_effect(self, effect_func):
```
**Описание**: Устанавливает функцию эффекта интервенции.

**Параметры**:
- `effect_func` (function): Функция, применяющая эффект.