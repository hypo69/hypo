# Модуль code_checker_ru

## Обзор

Этот модуль предоставляет функции для проверки кода на соответствие определённым правилам.  Он предназначен для анализа Python-кода и выдачи отчётов об обнаруженных нарушениях.

## Функции

### `check_code_style`

**Описание**: Проверяет стиль кода на соответствие заданным стандартам.

**Параметры**:
- `code_snippet` (str): фрагмент кода для проверки.
- `style_guide` (str, optional): название стиля кода (например, PEP 8). По умолчанию используется PEP 8.

**Возвращает**:
- dict | None: словарь с результатами проверки.  Возвращает `None`, если код корректен. Словарь содержит ключи `errors` (список сообщений об ошибках) и `warnings` (список сообщений о предупреждениях).

**Возможные исключения**:
- `ValueError`: если входные данные не соответствуют ожидаемому формату.


### `check_variable_names`

**Описание**: Проверяет имена переменных на соответствие стандартам.

**Параметры**:
- `code_snippet` (str): фрагмент кода для проверки.

**Возвращает**:
- dict | None: словарь с результатами проверки.  Возвращает `None`, если код корректен. Словарь содержит ключи `errors` (список сообщений об ошибках) и `warnings` (список сообщений о предупреждениях).

**Возможные исключения**:
- `ValueError`: если входные данные не соответствуют ожидаемому формату.


### `check_function_complexity`

**Описание**: Анализирует сложность функций в коде.

**Параметры**:
- `code_snippet` (str): фрагмент кода для проверки.

**Возвращает**:
- dict | None: словарь с результатами проверки.  Возвращает `None`, если код корректен. Словарь содержит ключи `errors` (список сообщений об ошибках) и `warnings` (список сообщений о предупреждениях).  Внутри каждого ключа находятся данные о функции и её сложности.

**Возможные исключения**:
- `ValueError`: если входные данные не соответствуют ожидаемому формату.


## Классы


<!-- TODO: Добавить описание классов, если они есть. -->


## Примеры использования

```python
# Пример использования функции check_code_style
code_snippet = """
def my_function(param1, param2):
  return param1 + param2
"""
result = check_code_style(code_snippet)

if result:
  for error in result['errors']:
    print(f"Ошибка: {error}")
```


```python
# Пример использования функции check_variable_names
code_snippet = """
def my_function(param1, param2):
  result = param1 + param2
  return result
"""
result = check_variable_names(code_snippet)

if result:
  for error in result['errors']:
    print(f"Ошибка: {error}")
```


```python
# Пример использования функции check_function_complexity
code_snippet = """
def my_complex_function(param1, param2, param3):
    result = 0
    for i in range(10000):
        result += i * param1
    return result
"""
result = check_function_complexity(code_snippet)

if result:
    for function_data in result['errors']:
      print(f"Функция {function_data['function_name']} имеет высокую сложность: {function_data['complexity']}")
```


```
<!-- TODO: Добавить примеры использования других функций и классов, если есть. -->
```
```