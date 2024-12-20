# Документация модуля `test_experimentation.py`

## Обзор

Этот модуль содержит unit-тесты для класса `ABRandomizer`, который используется для A/B-тестирования. Тесты проверяют правильность рандомизации, дерандомизации и дерандомизации имен.

## Оглавление

- [Функции](#функции)
  - [`test_randomize`](#test_randomize)
  - [`test_derandomize`](#test_derandomize)
  - [`test_derandomize_name`](#test_derandomize_name)
  - [`test_passtrough_name`](#test_passtrough_name)
  - [`test_intervention_1`](#test_intervention_1)

## Функции

### `test_randomize`

**Описание**: Тестирует метод `randomize` класса `ABRandomizer`. Проверяет, что метод возвращает корректные варианты в зависимости от случайно сгенерированного порядка.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения.

**Вызывает исключения**:
- `Exception`: Если не найдена рандомизация для элемента `i`.

### `test_derandomize`

**Описание**: Тестирует метод `derandomize` класса `ABRandomizer`. Проверяет, что метод возвращает исходные варианты после рандомизации.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения.

**Вызывает исключения**:
- Нет исключений.

### `test_derandomize_name`

**Описание**: Тестирует метод `derandomize_name` класса `ABRandomizer`. Проверяет, что метод возвращает корректное имя группы ("control" или "treatment") в зависимости от порядка рандомизации.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения.

**Вызывает исключения**:
- `Exception`: Если не найдена рандомизация для элемента `i`.

### `test_passtrough_name`

**Описание**: Тестирует метод `derandomize_name` класса `ABRandomizer` с параметром `passtrough_name`. Проверяет, что метод возвращает исходное имя, если оно находится в списке `passtrough_name`.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения.

**Вызывает исключения**:
- Нет исключений.

### `test_intervention_1`

**Описание**: Заглушка для теста `test_intervention_1`. Требуется доработка.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения.

**Вызывает исключения**:
- Нет исключений.