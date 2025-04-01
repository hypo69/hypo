# Модуль тестирования экспериментов `test_experimentation.py`

## Обзор

Модуль содержит набор модульных тестов для проверки функциональности экспериментирования, включая A/B-тестирование и проверку утверждений (proposition) с использованием объектов `TinyPerson` и `TinyWorld`.

## Подробнее

Модуль предназначен для тестирования различных аспектов экспериментирования, таких как рандомизация, дерандомизация, проверка утверждений на основе поведения объектов в смоделированной среде. В частности, проверяется корректность работы A/B-тестов, а также возможность формулирования и проверки гипотез относительно поведения виртуальных персонажей и их взаимодействия в виртуальном мире.

## Классы

### `ABRandomizer`

**Описание**: Класс для проведения A/B-тестирования. Позволяет рандомизировать и дерандомизировать варианты, а также определять имена групп.

**Методы**:
- `randomize(i: int, option1: str, option2: str) -> tuple[str, str]`:
    Рандомизирует два варианта (`option1` и `option2`) на основе индекса `i`.
    Возвращает кортеж с рандомизированными вариантами.

- `derandomize(i: int, a: str, b: str) -> tuple[str, str]`:
    Дерандомизирует два варианта (`a` и `b`) на основе индекса `i`.
    Возвращает исходные варианты в правильном порядке.

- `derandomize_name(i: int, name: str) -> str`:
    Определяет имя группы (control или treatment) на основе индекса `i` и выбранного варианта `name`.
    Возвращает имя группы.

### `Proposition`

**Описание**: Класс для представления утверждения, которое можно проверить на основе состояния целевого объекта.

**Атрибуты**:
- `target`: Целевой объект, на котором проверяется утверждение.
- `claim`: Текст утверждения.
- `last_n`: Количество последних действий, которые учитываются при проверке утверждения.

**Методы**:
- `check() -> bool`: Проверяет, истинно ли утверждение для целевого объекта.
    Возвращает `True`, если утверждение истинно, и `False` в противном случае.

## Функции

### `test_randomize`

```python
def test_randomize():
    """
    Тестирует функцию рандомизации A/B-теста.

    Выполняет несколько итераций рандомизации для проверки корректности выбора вариантов.

    Raises:
        Exception: Если не найдена рандомизация для элемента.
    """
    ...
```

**Как работает функция**:

1.  **Инициализация**: Создается экземпляр класса `ABRandomizer`.
2.  **Цикл рандомизации**:
    *   Цикл выполняется 20 раз.
    *   В каждой итерации вызывается метод `randomize` с параметрами `i`, `"option1"`, `"option2"`.
    *   Результат рандомизации сохраняется в переменные `a` и `b`.
    *   Проверяется значение `randomizer.choices[i]`:
        *   Если `randomizer.choices[i] == (0, 1)`, то утверждается, что `(a, b) == ("option1", "option2")`.
        *   Если `randomizer.choices[i] == (1, 0)`, то утверждается, что `(a, b) == ("option2", "option1")`.
        *   В противном случае вызывается исключение `Exception`.

```
Инициализация ABRandomizer
│
for i in range(20):
│   
├── Вызов ABRandomizer.randomize(i, "option1", "option2") → (a, b)
│   
├── Проверка randomizer.choices[i] == (0, 1)
│   │
│   └── Утверждение (a, b) == ("option1", "option2")
│   
├── Проверка randomizer.choices[i] == (1, 0)
│   │
│   └── Утверждение (a, b) == ("option2", "option1")
│   
└── Исключение Exception("No randomization found for item {i}") при отсутствии рандомизации
```

### `test_derandomize`

```python
def test_derandomize():
    """
    Тестирует функцию дерандомизации A/B-теста.

    Выполняет несколько итераций рандомизации и дерандомизации для проверки корректности восстановления исходных вариантов.
    """
    ...
```

**Как работает функция**:

1.  **Инициализация**: Создается экземпляр класса `ABRandomizer`.
2.  **Цикл рандомизации и дерандомизации**:
    *   Цикл выполняется 20 раз.
    *   В каждой итерации вызывается метод `randomize` с параметрами `i`, `"option1"`, `"option2"`.
    *   Результат рандомизации сохраняется в переменные `a` и `b`.
    *   Вызывается метод `derandomize` с параметрами `i`, `a`, `b`.
    *   Результат дерандомизации сохраняется в переменные `c` и `d`.
    *   Утверждается, что `(c, d) == ("option1", "option2")`.

```
Инициализация ABRandomizer
│
for i in range(20):
│   
├── Вызов ABRandomizer.randomize(i, "option1", "option2") → (a, b)
│   
├── Вызов ABRandomizer.derandomize(i, a, b) → (c, d)
│   
└── Утверждение (c, d) == ("option1", "option2")
```

### `test_derandomize_name`

```python
def test_derandomize_name():
    """
    Тестирует функцию дерандомизации имени группы A/B-теста.

    Выполняет несколько итераций рандомизации и дерандомизации имени для проверки корректности определения группы (control или treatment).

    Raises:
        Exception: Если не найдена рандомизация для элемента.
    """
    ...
```

**Как работает функция**:

1.  **Инициализация**: Создается экземпляр класса `ABRandomizer`.
2.  **Цикл рандомизации и дерандомизации имени**:
    *   Цикл выполняется 20 раз.
    *   В каждой итерации вызывается метод `randomize` с параметрами `i`, `"cats"`, `"dogs"`.
    *   Результат рандомизации сохраняется в переменные `a` и `b`.
    *   Вызывается метод `derandomize_name` с параметрами `i`, `"A"`.
    *   Результат дерандомизации имени сохраняется в переменную `real_name`.
    *   Проверяется значение `randomizer.choices[i]`:
        *   Если `randomizer.choices[i] == (0, 1)`, то утверждается, что `real_name == "control"`.
        *   Если `randomizer.choices[i] == (1, 0)`, то утверждается, что `real_name == "treatment"`.
        *   В противном случае вызывается исключение `Exception`.

```
Инициализация ABRandomizer
│
for i in range(20):
│   
├── Вызов ABRandomizer.randomize(i, "cats", "dogs") → (a, b)
│   
├── Вызов ABRandomizer.derandomize_name(i, "A") → real_name
│   
├── Проверка randomizer.choices[i] == (0, 1)
│   │
│   └── Утверждение real_name == "control"
│   
├── Проверка randomizer.choices[i] == (1, 0)
│   │
│   └── Утверждение real_name == "treatment"
│   
└── Исключение Exception("No randomization found for item {i}") при отсутствии рандомизации
```

### `test_passtrough_name`

```python
def test_passtrough_name():
    """
    Тестирует сквозное имя в A/B-тесте.

    Проверяет, что при использовании сквозного имени функция `derandomize_name` возвращает исходное имя без изменений.
    """
    ...
```

**Как работает функция**:

1.  **Инициализация**: Создается экземпляр класса `ABRandomizer` с параметром `passtrough_name=["option3"]`.
2.  **Рандомизация**: Вызывается метод `randomize` с параметрами `0`, `"option1"`, `"option2"`.
3.  **Дерандомизация имени**: Вызывается метод `derandomize_name` с параметрами `0`, `"option3"`.
4.  **Утверждение**: Утверждается, что `real_name == "option3"`.

```
Инициализация ABRandomizer с passtrough_name=["option3"]
│
├── Вызов ABRandomizer.randomize(0, "option1", "option2") → (a, b)
│   
├── Вызов ABRandomizer.derandomize_name(0, "option3") → real_name
│   
└── Утверждение real_name == "option3"
```

### `test_proposition_with_tinyperson`

```python
def test_proposition_with_tinyperson(setup):
    """
    Тестирует утверждения с использованием объекта TinyPerson.

    Проверяет, что утверждения о поведении TinyPerson оцениваются правильно.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
    """
    ...
```

**Как работает функция**:

1.  **Создание объекта `TinyPerson`**: Создается экземпляр класса `TinyPerson` с помощью функции `create_oscar_the_architect()`.
2.  **Действие `TinyPerson`**: `TinyPerson` выполняет действие `listen_and_act` с аргументом `"Tell me a bit about your travel preferences."`.
3.  **Создание истинного утверждения**: Создается экземпляр класса `Proposition` с параметрами `target=oscar`, `claim="Oscar mentions his travel preferences."`.
4.  **Проверка истинного утверждения**: Вызывается метод `check()` для проверки истинности утверждения. Утверждается, что результат равен `True`.
5.  **Создание ложного утверждения**: Создается экземпляр класса `Proposition` с параметрами `target=oscar`, `claim="Oscar writes a novel about how cats are better than dogs."`.
6.  **Проверка ложного утверждения**: Вызывается метод `check()` для проверки истинности утверждения. Утверждается, что результат равен `False`.

```
Создание TinyPerson (Oscar)
│
├── Oscar.listen_and_act("Tell me a bit about your travel preferences.")
│   
├── Создание Proposition(target=Oscar, claim="Oscar mentions his travel preferences.")
│   │
│   └── Утверждение Proposition.check() == True
│   
└── Создание Proposition(target=Oscar, claim="Oscar writes a novel about how cats are better than dogs.")
    │
    └── Утверждение Proposition.check() == False
```

### `test_proposition_with_tinyperson_at_multiple_points`

```python
def test_proposition_with_tinyperson_at_multiple_points(setup):
    """
    Тестирует утверждения с использованием объекта TinyPerson в нескольких точках времени.

    Проверяет, что утверждения о поведении TinyPerson оцениваются правильно с учетом последних действий.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
    """
    ...
```

**Как работает функция**:

1.  **Создание объекта `TinyPerson`**: Создается экземпляр класса `TinyPerson` с помощью функции `create_oscar_the_architect()`.
2.  **Действие `TinyPerson`**: `TinyPerson` выполняет действие `listen_and_act` с аргументом `"Tell me a bit about your travel preferences."`.
3.  **Создание истинного утверждения**: Создается экземпляр класса `Proposition` с параметрами `target=oscar`, `claim="Oscar talks about his travel preferences", last_n=3`.
4.  **Проверка истинного утверждения**: Вызывается метод `check()` для проверки истинности утверждения. Утверждается, что результат равен `True`.
5.  **Вывод обоснования и уверенности**: Выводится обоснование и уверенность утверждения.
6.  **Проверка длины обоснования и значения уверенности**: Утверждается, что длина обоснования больше 0 и значение уверенности больше или равно 0.0.
7.  **Действие `TinyPerson`**: `TinyPerson` выполняет действие `listen_and_act` с аргументом `"Now let's change subjects. What do you work with?"`.
8.  **Проверка ложного утверждения**: Вызывается метод `check()` для проверки истинности утверждения. Утверждается, что результат равен `False`.

```
Создание TinyPerson (Oscar)
│
├── Oscar.listen_and_act("Tell me a bit about your travel preferences.")
│   
├── Создание Proposition(target=Oscar, claim="Oscar talks about his travel preferences", last_n=3)
│   │
│   └── Утверждение Proposition.check() == True
│   
├── Вывод Proposition.justification и Proposition.confidence
│   
├── Утверждение len(Proposition.justification) > 0 и Proposition.confidence >= 0.0
│   
├── Oscar.listen_and_act("Now let's change subjects. What do you work with?")
│   
└── Утверждение Proposition.check() == False
```

### `test_proposition_with_tinyworld`

```python
def test_proposition_with_tinyworld(setup, focus_group_world):
    """
    Тестирует утверждения с использованием объекта TinyWorld.

    Проверяет, что утверждения о событиях в TinyWorld оцениваются правильно.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
        focus_group_world: Фикстура pytest, представляющая объект TinyWorld.
    """
    ...
```

**Как работает функция**:

1.  **Получение объекта `TinyWorld`**: Получается экземпляр класса `TinyWorld` из фикстуры `focus_group_world`.
2.  **Действие `TinyWorld`**: `TinyWorld` выполняет действие `broadcast` с аргументом `"Discuss the comparative advantages of dogs and cats."`.
3.  **Запуск `TinyWorld`**: `TinyWorld` запускается на 2 итерации.
4.  **Создание истинного утверждения**: Создается экземпляр класса `Proposition` с параметрами `target=world`, `claim="There's a discussion about dogs and cats."`.
5.  **Проверка истинного утверждения**: Вызывается метод `check()` для проверки истинности утверждения. Утверждается, что результат равен `True`.
6.  **Создание ложного утверждения**: Создается экземпляр класса `Proposition` с параметрами `target=world`, `claim="There's a discussion about whether porto wine vs french wine."`.
7.  **Проверка ложного утверждения**: Вызывается метод `check()` для проверки истинности утверждения. Утверждается, что результат равен `False`.

```
Получение TinyWorld (world) из фикстуры
│
├── world.broadcast("Discuss the comparative advantages of dogs and cats.")
│   
├── world.run(2)
│   
├── Создание Proposition(target=world, claim="There's a discussion about dogs and cats.")
│   │
│   └── Утверждение Proposition.check() == True
│   
└── Создание Proposition(target=world, claim="There's a discussion about whether porto wine vs french wine.")
    │
    └── Утверждение Proposition.check() == False
```

### `test_proposition_with_multiple_targets`

```python
def test_proposition_with_multiple_targets(setup):
    """
    Тестирует утверждения с использованием нескольких целевых объектов.

    Проверяет, что утверждения, охватывающие несколько объектов TinyPerson, оцениваются правильно.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
    """
    ...
```

**Как работает функция**:

1.  **Создание объектов `TinyPerson`**: Создаются экземпляры класса `TinyPerson` с помощью функций `create_oscar_the_architect()` и `create_lisa_the_data_scientist()`.
2.  **Действия `TinyPerson`**: Каждый `TinyPerson` выполняет действие `listen_and_act` с разными аргументами.
3.  **Определение целей**: Создается список `targets`, содержащий объекты `oscar` и `lisa`.
4.  **Создание истинного утверждения**: Создается экземпляр класса `Proposition` с параметрами `target=targets`, `claim="Oscar mentions his travel preferences and Lisa discusses data science projects."`.
5.  **Проверка истинного утверждения**: Вызывается метод `check()` для проверки истинности утверждения. Утверждается, что результат равен `True`.
6.  **Создание ложного утверждения**: Создается экземпляр класса `Proposition` с параметрами `target=targets`, `claim="Oscar writes a novel about how cats are better than dogs."`.
7.  **Проверка ложного утверждения**: Вызывается метод `check()` для проверки истинности утверждения. Утверждается, что результат равен `False`.

```
Создание TinyPerson (Oscar)
│
├── Создание TinyPerson (Lisa)
│   
├── Oscar.listen_and_act("Tell me a bit about your travel preferences.")
│   
├── Lisa.listen_and_act("Tell me about your data science projects.")
│   
├── targets = [Oscar, Lisa]
│   
├── Создание Proposition(target=targets, claim="Oscar mentions his travel preferences and Lisa discusses data science projects.")
│   │
│   └── Утверждение Proposition.check() == True
│   
└── Создание Proposition(target=targets, claim="Oscar writes a novel about how cats are better than dogs.")
    │
    └── Утверждение Proposition.check() == False
```

### `test_proposition_class_method`

```python
def test_proposition_class_method(setup):
    """
    Тестирует метод класса для проверки утверждений.

    Проверяет, что утверждения можно проверить с использованием метода класса `check_proposition`.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
    """
    ...
```

**Как работает функция**:

1.  **Создание объекта `TinyPerson`**: Создается экземпляр класса `TinyPerson` с помощью функции `create_oscar_the_architect()`.
2.  **Действие `TinyPerson`**: `TinyPerson` выполняет действие `listen_and_act` с аргументом `"Tell me a bit about your travel preferences."`.
3.  **Проверка истинного утверждения**: Вызывается функция `check_proposition` с параметрами `target=oscar`, `claim="Oscar mentions his travel preferences."`. Утверждается, что результат равен `True`.
4.  **Проверка истинного утверждения (альтернативный синтаксис)**: Вызывается функция `check_proposition` с параметрами `oscar`, `"Oscar mentions his travel preferences."`. Утверждается, что результат равен `True`.
5.  **Проверка ложного утверждения**: Вызывается функция `check_proposition` с параметрами `target=oscar`, `claim="Oscar writes a novel about how cats are better than dogs."`. Утверждается, что результат равен `False`.
6.  **Проверка ложного утверждения (альтернативный синтаксис)**: Вызывается функция `check_proposition` с параметрами `oscar`, `"Oscar writes a novel about how cats are better than dogs."`. Утверждается, что результат равен `False`.

```
Создание TinyPerson (Oscar)
│
├── Oscar.listen_and_act("Tell me a bit about your travel preferences.")
│   
├── Утверждение check_proposition(target=Oscar, claim="Oscar mentions his travel preferences.") == True
│   
├── Утверждение check_proposition(Oscar, "Oscar mentions his travel preferences.") == True
│   
├── Утверждение check_proposition(target=Oscar, claim="Oscar writes a novel about how cats are better than dogs.") == False
│   
└── Утверждение check_proposition(Oscar, "Oscar writes a novel about how cats are better than dogs.") == False