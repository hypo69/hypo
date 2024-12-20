# Модуль `test_experimentation.py`

## Обзор

Данный модуль содержит тесты для класса `ABRandomizer`, проверяющие правильность работы функций рандомизации и дерандомизации.

## Функции

### `test_randomize`

**Описание**: Тестирует функцию `randomize` класса `ABRandomizer`.  Проверяет, что функция возвращает корректные пары вариантов A/B, соответствующие рандомизации.  Тестирование выполняется 20 раз для повышения надежности результатов.

**Параметры**:
- `i` (int): Индекс элемента для рандомизации.
- `"option1"` (str): Первый вариант.
- `"option2"` (str): Второй вариант.


**Возвращает**:
- `None`: Данная функция не возвращает значения, а проверяет корректность возвращаемых значений.


**Вызывает исключения**:
- `Exception`: В случае, если для текущего элемента `i` не найдено корректное рандомизированное значение.


### `test_derandomize`

**Описание**: Тестирует функцию `derandomize` класса `ABRandomizer`. Проверяет, что функция корректно восстанавливает исходные варианты A/B.  Тестирование выполняется 20 раз для повышения надежности результатов.

**Параметры**:
- `i` (int): Индекс элемента для дерандомизации.
- `a` (str): Первый вариант после рандомизации.
- `b` (str): Второй вариант после рандомизации.

**Возвращает**:
- `None`: Данная функция не возвращает значения, а проверяет корректность возвращаемых значений.


**Вызывает исключения**:
- `None`: Данная функция не вызывает исключений.


### `test_derandomize_name`

**Описание**: Тестирует функцию `derandomize_name` класса `ABRandomizer`. Проверяет, что функция корректно восстанавливает имя варианта (control или treatment) в зависимости от результата рандомизации.  Тестирование выполняется 20 раз для повышения надежности результатов.

**Параметры**:
- `i` (int): Индекс элемента для дерандомизации.
- `a` (str): Первый вариант после рандомизации.

**Возвращает**:
- `None`: Данная функция не возвращает значения, а проверяет корректность возвращаемых значений.


**Вызывает исключения**:
- `Exception`: В случае, если для текущего элемента `i` не найдено корректное рандомизированное значение.


### `test_passtrough_name`

**Описание**: Тестирует функцию `derandomize_name` класса `ABRandomizer` с параметром `passtrough_name`. Проверяет, что для элементов, включенных в `passtrough_name`, функция возвращает соответствующее значение, а не рандомизированное.


**Параметры**:
- `"option3"` (list): Список вариантов, которые должны возвращаться без изменения.
- `i` (int): Индекс элемента для дерандомизации.
- `a` (str): Первый вариант после рандомизации.

**Возвращает**:
- `None`: Данная функция не возвращает значения, а проверяет корректность возвращаемого значения.


**Вызывает исключения**:
- `None`: Данная функция не вызывает исключений.


### `test_intervention_1`

**Описание**: Тест для функции, связанной с интервенциями.  (TODO: Не реализовано)

**Параметры**:
- `None`:  Функция пока не реализована, поэтому параметры не определены.

**Возвращает**:
- `None`:  Функция пока не реализована.

**Вызывает исключения**:
- `None`:  Функция пока не реализована.