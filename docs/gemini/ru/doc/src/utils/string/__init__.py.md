# Модуль `src.utils.string`

## Обзор

Модуль `src.utils.string` предоставляет набор утилит для работы со строками, включая валидацию и нормализацию данных. Модуль предназначен для использования в различных операционных системах, таких как Windows и Unix.

## Содержание

- [Обзор](#обзор)
- [Классы](#классы)
    - [`ProductFieldsValidator`](#productfieldsvalidator)
- [Функции](#функции)
    - [`normalize_string`](#normalize_string)
    - [`normalize_int`](#normalize_int)
    - [`normalize_float`](#normalize_float)
    - [`normalize_boolean`](#normalize_boolean)
    - [`normalize_sql_date`](#normalize_sql_date)

## Классы

### `ProductFieldsValidator`

**Описание**: Класс `ProductFieldsValidator` предназначен для валидации полей продукта. Подробности реализации доступны в модуле `validator`.

## Функции

### `normalize_string`

**Описание**: Функция `normalize_string` предназначена для нормализации строковых данных. Подробности реализации доступны в модуле `normalizer`.

### `normalize_int`

**Описание**: Функция `normalize_int` предназначена для нормализации целочисленных данных. Подробности реализации доступны в модуле `normalizer`.

### `normalize_float`

**Описание**: Функция `normalize_float` предназначена для нормализации данных с плавающей точкой. Подробности реализации доступны в модуле `normalizer`.

### `normalize_boolean`

**Описание**: Функция `normalize_boolean` предназначена для нормализации булевых данных. Подробности реализации доступны в модуле `normalizer`.

### `normalize_sql_date`

**Описание**: Функция `normalize_sql_date` предназначена для нормализации данных в формате SQL-даты. Подробности реализации доступны в модуле `normalizer`.