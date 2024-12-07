# Модуль hypotez/src/utils/string/normalizer.py

## Обзор

Модуль `normalizer.py` предназначен для нормализации данных, в основном текстовых строк и чисел, из различных источников.  Он предоставляет функции для приведения данных к стандартному формату, удаления нежелательных элементов (тегов HTML, переносов строк, специальных символов) и обработки различных типов данных (строки, логические значения, целые и вещественные числа). Если нормализация не выполняется успешно, функция возвращает исходные данные.

## Функции

### `normalize_boolean`

**Описание**: Нормализует входные данные в булево значение.

**Параметры**:
- `input_data` (Any): Данные, которые могут представлять булево значение (например, bool, строка, целое число).

**Возвращает**:
- `bool`: Булево представление входных данных.

**Примеры**:
- `normalize_boolean('yes')` возвращает `True`
- `normalize_boolean(1)` возвращает `True`
- `normalize_boolean('0')` возвращает `False`


**Обрабатывает исключения**:
- `Exception`:  Если возникает ошибка при преобразовании входных данных в строку или проверке булевого значения, логгирует ошибку и возвращает исходные данные.


### `normalize_string`

**Описание**: Нормализует строку или список строк.

**Параметры**:
- `input_data` (str | List[str]): Входные данные, которые могут быть строкой или списком строк.

**Возвращает**:
- `str`: Очищенная и нормализованная строка в формате UTF-8.

**Примеры**:
- `normalize_string(['Hello', '  World!  '])` возвращает `'Hello World!'`

**Обрабатывает исключения**:
- `Exception`: Если возникает ошибка при нормализации строки, логгирует ошибку и возвращает исходные данные в формате UTF-8.


### `normalize_int`

**Описание**: Нормализует данные в целое число.

**Параметры**:
- `input_data` (str | int | float | Decimal): Входные данные, которые могут быть числом или его строковым представлением.

**Возвращает**:
- `int`: Целочисленное представление входных данных.

**Примеры**:
- `normalize_int('42')` возвращает `42`

**Обрабатывает исключения**:
- `ValueError`, `TypeError`, `InvalidOperation`: Если возникает ошибка при преобразовании входных данных в целое число, логгирует ошибку и возвращает исходные данные.


### `normalize_float`

**Описание**:  Безопасно преобразует входные значения в число с плавающей точкой или список чисел с плавающей точкой.

**Параметры**:
- `value` (Any): Входное значение, которое может быть числом или строкой, представляющей число, или итерируемым объектом (список/кортеж).

**Возвращает**:
- `float | List[float] | None`: Значение с плавающей точкой, список чисел с плавающей точкой или `None`, если преобразование не удалось.

**Примеры**:
- `normalize_float("3.14")` возвращает `3.14`
- `normalize_float([1, '2.5', 3])` возвращает `[1.0, 2.5, 3.0]`
- `normalize_float("abc")` возвращает `None` с сообщением об ошибке.


**Обрабатывает исключения**:
- `ValueError`, `TypeError`:  Логирует предупреждение, если преобразование в число с плавающей точкой не удалось, и возвращает исходное значение.