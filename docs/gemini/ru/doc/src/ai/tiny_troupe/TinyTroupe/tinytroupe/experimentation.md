# Модуль experimentation

## Обзор

Этот модуль содержит классы для рандомизации выборов и реализации интервенций.  `ABRandomizer` предназначен для рандомизации выбора между двумя вариантами (например, A и B), а затем для обратного преобразования этого выбора.  `Intervention` предоставляет базовый класс для реализации интервенций, задавая условия (прекондиции) и эффекты.

## Классы

### `ABRandomizer`

**Описание**: Класс для рандомизации и де-рандомизации выборов между двумя вариантами.

**Методы**:

#### `__init__`

**Описание**: Инициализирует экземпляр класса `ABRandomizer`.

**Параметры**:
- `real_name_1` (str): Имя первого варианта в исходных данных.
- `real_name_2` (str): Имя второго варианта в исходных данных.
- `blind_name_a` (str): Имя первого варианта для пользователя.
- `blind_name_b` (str): Имя второго варианта для пользователя.
- `passtrough_name` (list): Список имен, которые не подлежат рандомизации и всегда возвращаются как есть.
- `random_seed` (int): Семено для генератора случайных чисел.

#### `randomize`

**Описание**: Рандомизирует выбор между двумя вариантами для данного индекса.

**Параметры**:
- `i` (int): Индекс элемента.
- `a` (str): Первый вариант.
- `b` (str): Второй вариант.

**Возвращает**:
- tuple(str, str): Пара (a, b) после рандомизации.

**Примечание**: Хранит результаты рандомизации в `self.choices`.


#### `derandomize`

**Описание**: Де-рандомизирует выбор для данного индекса.

**Параметры**:
- `i` (int): Индекс элемента.
- `a` (str): Первый вариант.
- `b` (str): Второй вариант.

**Возвращает**:
- tuple(str, str): Пара (a, b) после де-рандомизации.

**Возможные исключения**:
- `Exception`: Если рандомизация для элемента не найдена.


#### `derandomize_name`

**Описание**:  Декодирует выбранное пользователем имя и возвращает соответствующее истинное имя.

**Параметры**:
- `i` (int): Индекс элемента.
- `blind_name` (str): Выбранное пользователем имя.

**Возвращает**:
- str: Истинное имя варианта.

**Возможные исключения**:
- `Exception`: Если выбранное пользователем имя не распознано.


### `Intervention`

**Описание**: Базовый класс для реализации интервенций.

**Методы**:

#### `__init__`

**Описание**: Инициализирует экземпляр класса `Intervention`.

**Параметры**:
- `agent` (TinyPerson): Агент для интервенции (может быть только один).
- `agents` (list): Список агентов для интервенции.
- `environment` (TinyWorld): Среда для интервенции (может быть только одна).
- `environments` (list): Список сред для интервенции.

**Возможные исключения**:
- `Exception`: Если предоставлены и `agent`, и `agents`, или `environment` и `environments`.
- `Exception`: Если ни один из параметров не предоставлен.

#### `check_precondition`

**Описание**: Проверяет выполнение условия для интервенции.

**Возможные исключения**:
- `NotImplementedError`:  Метод не реализован.


#### `apply`

**Описание**: Применяет интервенцию.

**Возможные исключения**:
- `NotImplementedError`: Метод не реализован.


#### `set_textual_precondition`

**Описание**: Устанавливает текстовое условие для интервенции.

**Параметры**:
- `text` (str): Текстовое условие.


#### `set_functional_precondition`

**Описание**: Устанавливает функциональное условие для интервенции.

**Параметры**:
- `func` (function): Функция условия.


#### `set_effect`

**Описание**: Устанавливает эффект интервенции.

**Параметры**:
- `effect_func` (function): Функция эффекта.