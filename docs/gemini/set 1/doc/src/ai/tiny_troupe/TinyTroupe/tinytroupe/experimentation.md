# Модуль experimentation

## Обзор

Этот модуль содержит классы для рандомизации и обработки данных, а также для реализации вмешательства.  `ABRandomizer` предназначен для рандомизации выбора между двумя вариантами (например, A/B тестирование). `Intervention` абстрагирует процесс вмешательства в систему, позволяя задавать условия и эффекты.

## Классы

### `ABRandomizer`

**Описание**: Утилитарный класс для рандомизации между двумя вариантами и последующего дерандомизирования. Хранит результаты рандомизации для каждого элемента.

**Методы**

- `__init__`: Инициализирует класс.
- `randomize`: Рандомизирует выбор между двумя вариантами для заданного индекса.
- `derandomize`: Дерандомизирует выбор для заданного индекса.
- `derandomize_name`: Декодирует выбор пользователя, возвращая исходное значение.

**Параметры**

- `real_name_1` (str): Имя первого варианта в исходных данных.
- `real_name_2` (str): Имя второго варианта в исходных данных.
- `blind_name_a` (str): Имя первого варианта, отображаемое пользователю.
- `blind_name_b` (str): Имя второго варианта, отображаемое пользователю.
- `passtrough_name` (list): Список имен, которые не должны быть рандомизированы и возвращаются как есть.
- `random_seed` (int): Семен для генератора случайных чисел.

**Возвращает**

- `randomize`: Кортеж (a, b) - рандомизированные значения.
- `derandomize`: Кортеж (a, b) - дерандомизированные значения.
- `derandomize_name`: Исходное значение варианта.

**Вызывает исключения**

- `Exception`: Выбрасывается, если не найдена информация о рандомизации элемента или если выбор пользователя не распознан.


### `Intervention`

**Описание**: Абстрактный класс для реализации вмешательства в систему.

**Методы**

- `__init__`: Инициализирует класс.
- `check_precondition`: Проверяет выполнение условия для вмешательства.
- `apply`: Применяет вмешательство.
- `set_textual_precondition`: Устанавливает текстовое условие для вмешательства.
- `set_functional_precondition`: Устанавливает условие вмешательства как функцию.
- `set_effect`: Устанавливает эффект вмешательства.


**Параметры**

- `agent` (TinyPerson): Агент, на котором выполняется вмешательство.
- `agents` (list): Список агентов, на которых выполняется вмешательство.
- `environment` (TinyWorld): Среда, на которой выполняется вмешательство.
- `environments` (list): Список сред, на которых выполняется вмешательство.
- `text` (str): Текст условия для вмешательства.
- `func` (function): Функция, представляющая условие для вмешательства.
- `effect` (str): Функция, описывающая эффект вмешательства.


**Возвращает**

- `check_precondition`: Булево значение, указывающее на выполнение условия.
- `apply`: Результат применения вмешательства.
-  (Все остальные методы не возвращают значений)

**Вызывает исключения**

- `Exception`: Выбрасывается в случае несоответствия входных параметров.
- `NotImplementedError`: Выбрасывается, если метод `check_precondition` не реализован.


## Функции

(Нет функций в этом модуле)