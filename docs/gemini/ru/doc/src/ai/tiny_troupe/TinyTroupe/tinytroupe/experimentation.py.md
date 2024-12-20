# Документация модуля `experimentation.py`

## Обзор

Модуль `experimentation.py` содержит классы для проведения экспериментов, включая рандомизацию вариантов и реализацию вмешательств.

## Оглавление

- [Классы](#классы)
  - [`ABRandomizer`](#abrandomizer)
  - [`Intervention`](#intervention)
- [Использование](#использование)

## Классы

### `ABRandomizer`

**Описание**: Класс `ABRandomizer` предназначен для рандомизации двух вариантов (`real_name_1` и `real_name_2`) и их последующей дерандомизации. Он также позволяет представлять варианты пользователю под другими именами (`blind_name_a` и `blind_name_b`).

**Методы**:

#### `__init__`

**Описание**: Инициализирует объект `ABRandomizer`.

**Параметры**:
- `real_name_1` (str): Название первого варианта (по умолчанию "control").
- `real_name_2` (str): Название второго варианта (по умолчанию "treatment").
- `blind_name_a` (str): Название первого варианта для пользователя (по умолчанию "A").
- `blind_name_b` (str): Название второго варианта для пользователя (по умолчанию "B").
- `passtrough_name` (list): Список названий, которые не должны рандомизироваться (по умолчанию `[]`).
- `random_seed` (int): Зерно для генератора случайных чисел (по умолчанию 42).

#### `randomize`

**Описание**: Рандомизирует порядок вариантов `a` и `b` для элемента с индексом `i`.

**Параметры**:
- `i` (int): Индекс элемента.
- `a` (str): Первый вариант.
- `b` (str): Второй вариант.

**Возвращает**:
- `tuple[str, str]`: Рандомизированные варианты.

#### `derandomize`

**Описание**: Дерандомизирует порядок вариантов `a` и `b` для элемента с индексом `i`.

**Параметры**:
- `i` (int): Индекс элемента.
- `a` (str): Первый вариант.
- `b` (str): Второй вариант.

**Возвращает**:
- `tuple[str, str]`: Дерандомизированные варианты.

**Вызывает исключения**:
- `Exception`: Если для элемента `i` не найдено информации о рандомизации.

#### `derandomize_name`

**Описание**: Декодирует выбор пользователя и возвращает соответствующий вариант.

**Параметры**:
- `i` (int): Индекс элемента.
- `blind_name` (str): Выбор пользователя.

**Возвращает**:
- `str`: Дерандомизированное имя варианта.

**Вызывает исключения**:
- `Exception`: Если для элемента `i` не найдено информации о рандомизации, либо выбор пользователя не распознан.

### `Intervention`

**Описание**: Класс `Intervention` представляет собой вмешательство, которое можно применить к агентам или средам.

**Методы**:

#### `__init__`

**Описание**: Инициализирует объект `Intervention`.

**Параметры**:
- `agent` (TinyPerson, optional): Один агент, к которому применяется вмешательство.
- `agents` (list, optional): Список агентов, к которым применяется вмешательство.
- `environment` (TinyWorld, optional): Одна среда, к которой применяется вмешательство.
- `environments` (list, optional): Список сред, к которым применяется вмешательство.

**Вызывает исключения**:
- `Exception`: Если передано одновременно `agent` и `agents`, `environment` и `environments`, или не передан ни один из параметров.

#### `check_precondition`

**Описание**: Проверяет, выполняются ли предварительные условия для вмешательства.

**Вызывает исключения**:
- `NotImplementedError`: Всегда, так как метод требует реализации.

#### `apply`

**Описание**: Применяет вмешательство, вызывая функцию эффекта.

#### `set_textual_precondition`

**Описание**: Устанавливает текстовое описание предварительного условия.

**Параметры**:
- `text` (str): Текст предварительного условия.

#### `set_functional_precondition`

**Описание**: Устанавливает функциональное предварительное условие.

**Параметры**:
- `func` (function): Функция предварительного условия, принимающая аргументы: `agent`, `agents`, `environment`, `environments`.

#### `set_effect`

**Описание**: Устанавливает функцию эффекта вмешательства.

**Параметры**:
- `effect_func` (function): Функция эффекта вмешательства.

## Использование

Пример использования `ABRandomizer`:
```python
randomizer = ABRandomizer(real_name_1="control", real_name_2="treatment", blind_name_a="A", blind_name_b="B")
a, b = randomizer.randomize(0, "option1", "option2")
print(f"Рандомизированные варианты: {a}, {b}")
a, b = randomizer.derandomize(0, "option1", "option2")
print(f"Дерандомизированные варианты: {a}, {b}")
real_name = randomizer.derandomize_name(0, "A")
print(f"Дерандомизированное имя: {real_name}")
```

Пример использования `Intervention`:
```python
def effect_func(agents, environments):
    print("Вмешательство применено")

intervention = Intervention()
intervention.set_effect(effect_func)
intervention.apply()
```