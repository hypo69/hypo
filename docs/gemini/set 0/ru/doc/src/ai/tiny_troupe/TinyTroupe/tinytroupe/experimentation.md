# Модуль `experimentation`

## Обзор

Этот модуль предоставляет классы для рандомизации выборок и реализации вмешательств.  `ABRandomizer` позволяет рандомизировать выборки между двумя вариантами, а `Intervention` предоставляет базовый класс для определения и применения вмешательств.

## Оглавление

- [Модуль `experimentation`](#модуль-experimentation)
- [Класс `ABRandomizer`](#класс-abrandomizer)
    - [`__init__`](#__init__)
    - [`randomize`](#randomize)
    - [`derandomize`](#derandomize)
    - [`derandomize_name`](#derandomize_name)
- [Класс `Intervention`](#класс-intervention)
    - [`__init__`](#__init___1)
    - [`check_precondition`](#check_precondition)
    - [`apply`](#apply)
    - [`set_textual_precondition`](#set_textual_precondition)
    - [`set_functional_precondition`](#set_functional_precondition)
    - [`set_effect`](#set_effect)


## Классы

### `ABRandomizer`

**Описание**: Класс для рандомизации выборок между двумя вариантами (A и B), а также последующего возврата к исходному состоянию. Сохраняет информацию о рандомизации для каждого элемента.

#### `__init__`

```python
def __init__(self, real_name_1="control", real_name_2="treatment",
                   blind_name_a="A", blind_name_b="B",
                   passtrough_name=[],
                   random_seed=42):
    """
    Инициализирует объект ABRandomizer.

    Args:
        real_name_1 (str): Название первого варианта.
        real_name_2 (str): Название второго варианта.
        blind_name_a (str): Название первого варианта для пользователя.
        blind_name_b (str): Название второго варианта для пользователя.
        passtrough_name (list): Список имён, которые не рандомизируются.
        random_seed (int): Зерно для генератора случайных чисел.
    """
```

#### `randomize`

```python
def randomize(self, i, a, b):
    """
    Рандомизирует выборки для элемента i.

    Args:
        i (int): Индекс элемента.
        a (str): Первый вариант.
        b (str): Второй вариант.

    Returns:
        tuple: Кортеж из рандомизированных вариантов (a, b).
    """
```

#### `derandomize`

```python
def derandomize(self, i, a, b):
    """
    Возвращает выборки для элемента i к исходному состоянию.

    Args:
        i (int): Индекс элемента.
        a (str): Первый вариант.
        b (str): Второй вариант.

    Returns:
        tuple: Кортеж из исходных вариантов (a, b).
    Raises:
        Exception: Если рандомизация для элемента i не найдена.
    """
```

#### `derandomize_name`

```python
def derandomize_name(self, i, blind_name):
    """
    Возвращает реальное имя варианта для выбранного пользователем варианта.

    Args:
        i (int): Индекс элемента.
        blind_name (str): Выбранное пользователем имя варианта.

    Returns:
        str: Реальное имя варианта.
    Raises:
        Exception: Если выбранное имя варианта не распознано.
    """
```


### `Intervention`

**Описание**: Базовый класс для определения и применения вмешательств.

#### `__init__`

```python
def __init__(self, agent=None, agents:list=None, environment=None, environments:list=None):
    """
    Инициализирует объект Intervention.

    Args:
        agent (TinyPerson): Агент.
        agents (list): Список агентов.
        environment (TinyWorld): Среда.
        environments (list): Список сред.

    Raises:
        Exception: Если предоставлены как `agent`, так и `agents`, или как `environment`, так и `environments`, или если не указан ни один из параметров.
    """
```


#### `check_precondition`

```python
def check_precondition(self):
    """
    Проверяет выполнение условия для вмешательства.
    Возвращает результат проверки условия.
    Raises:
        NotImplementedError: Если метод не реализован.
    """
```


#### `apply`

```python
def apply(self):
    """
    Применяет вмешательство.
    """
```


#### `set_textual_precondition`

```python
def set_textual_precondition(self, text):
    """
    Устанавливает текстовое условие для вмешательства.

    Args:
        text (str): Текст условия.
    """
```


#### `set_functional_precondition`

```python
def set_functional_precondition(self, func):
    """
    Устанавливает функциональное условие для вмешательства.

    Args:
        func (function): Функция условия.
    """
```


#### `set_effect`

```python
def set_effect(self, effect_func):
    """
    Устанавливает эффект вмешательства.

    Args:
        effect_func (function): Функция эффекта.
    """
```