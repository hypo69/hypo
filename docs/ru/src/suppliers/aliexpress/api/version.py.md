# Модуль `version`

## Обзор

Модуль `version` содержит информацию о версии текущего модуля или пакета, а также другие метаданные.

## Содержание

1. [Переменные модуля](#переменные-модуля)
    - [`__name__`](#__name__)
    - [`__version__`](#__version__)
    - [`__doc__`](#__doc__)
    - [`__details__`](#__details__)
    - [`__annotations__`](#__annotations__)
    - [`__author__`](#__author__)

## Переменные модуля

### `__name__`

**Описание**: Содержит имя текущего модуля. Если скрипт запущен напрямую, то значение будет `"__main__"`.

**Тип**: `str`

### `__version__`

**Описание**: Содержит версию текущего модуля или пакета.

**Тип**: `str`

**Значение**: `"3.12.0.0.0.4"`

### `__doc__`

**Описание**: Содержит строку документации модуля.

**Тип**: `str`

### `__details__`

**Описание**: Содержит дополнительные сведения о версии модуля или класса.

**Тип**: `str`

**Значение**: `"Details about version for module or class"`

### `__annotations__`

**Описание**: Содержит аннотации типов для переменных и функций в модуле.

**Тип**: `dict`

### `__author__`

**Описание**: Содержит имя(имена) автора(ов) модуля.

**Тип**: `str`

**Значение**: `"hypotez"`