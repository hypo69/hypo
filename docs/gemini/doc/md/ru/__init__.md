# hypotez/src/__init__.py

## Обзор

Этот модуль является началом пакета `hypotez/src`. Он содержит константу `MODE`, определяющую режим работы, и импортирует функцию `gs` из файла `credentials.py`.

## Оглавление

* [Обзор](#обзор)
* [Константы](#константы)
    * [`MODE`](#mode)
* [Импорты](#импорты)
    * [`gs`](#gs)


## Константы

### `MODE`

**Описание**: Строковая константа, определяющая режим работы приложения (`development` в данном случае).


## Импорты

### `gs`

**Описание**: Импортирует функцию `gs` из файла `hypotez/src/credentials.py`.


```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'development'

from .credentials import gs
```
