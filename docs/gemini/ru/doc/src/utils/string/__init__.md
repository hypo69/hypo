# Модуль hypotez/src/utils/string/__init__.py

## Обзор

Этот модуль предоставляет инструменты для работы со строками, включая валидацию и нормализацию различных типов данных.  Модуль содержит классы и функции для проверки соответствия полей продукта и нормализации строк, целых чисел, чисел с плавающей точкой, булевых значений и дат в формате SQL.

## Содержание

* [Валидация](#валидация)
* [Нормализация](#нормализация)


## Валидация

### `ProductFieldsValidator`

**Описание**: Класс для валидации полей продукта. Подробности реализации и функциональности требуют дополнительной документации.

**Методы**:  (Подробности реализации требуют кода самого класса.)

* Подробные описания методов должны быть добавлены с использованием кода `"""` в методах самого класса


## Нормализация

### `normalize_string`

**Описание**: Функция для нормализации строк.

**Параметры**:

* `string` (str): Строка для нормализации.

**Возвращает**:

* `str`: Нормализованная строка. (Подробности о нормализации требуют дополнительной документации.)

### `normalize_int`

**Описание**: Функция для нормализации целых чисел.

**Параметры**:

* `number` (str): Строковое представление целого числа.

**Возвращает**:

* `int`: Нормализованное целое число. (Возвращает `None`, если входное значение не может быть преобразовано в целое число.)


### `normalize_float`

**Описание**: Функция для нормализации чисел с плавающей точкой.

**Параметры**:

* `number` (str): Строковое представление числа с плавающей точкой.

**Возвращает**:

* `float`: Нормализованное число с плавающей точкой. (Возвращает `None`, если входное значение не может быть преобразовано в число с плавающей точкой.)


### `normalize_boolean`

**Описание**: Функция для нормализации булевых значений.

**Параметры**:

* `boolean` (str): Строковое представление булева значения (например, 'true', 'false').

**Возвращает**:

* `bool`: Нормализованное булевое значение. (Возвращает `None`, если входное значение не может быть преобразовано в булевое значение.)


### `normalize_sql_date`

**Описание**: Функция для нормализации дат в формате SQL.

**Параметры**:

* `date` (str): Строковое представление даты в формате SQL.

**Возвращает**:

* `date`: Нормализованная дата. (Возвращает `None`, если входное значение не может быть преобразовано в дату.)