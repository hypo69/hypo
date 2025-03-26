# Модуль `header.py`

## Обзор

Модуль содержит примеры кода и импорты, демонстрирующие структуру и использование различных компонентов проекта, таких как работа с путями, JSON, регулярными выражениями, а также импорт пользовательских модулей и классов.

## Оглавление

1. [Импорты](#Импорты)
2. [Переменные](#Переменные)
3. [Примеры использования](#Примеры-использования)
4. [Импорты из модулей проекта](#Импорты-из-модулей-проекта)

## Импорты

В этом разделе описаны основные импортируемые модули.

### Стандартные библиотеки Python

-   `sys`: Используется для работы с системными параметрами и функциями, в частности, для изменения пути поиска модулей.
-   `os`: Предоставляет функции для взаимодействия с операционной системой, например, для работы с файловой системой.
-   `pathlib.Path`: Класс для представления путей к файлам и директориям в объектно-ориентированном стиле.
-   `json`: Модуль для работы с данными в формате JSON.
-   `re`: Модуль для работы с регулярными выражениями.

### Переменные

-   `dir_root`:  Представляет собой путь к корневой директории проекта.
-   `dir_src`: Представляет собой путь к директории `src` внутри корневой директории проекта.

## Примеры использования

В этом разделе показаны примеры использования импортированных модулей и классов.

-   Пример добавления пути к корневой директории проекта в `sys.path` для возможности импорта модулей проекта.

```python
import sys
import os
from pathlib import Path

dir_root : Path = Path (os.getcwd()[:os.getcwd().rfind('hypotez')+11])
sys.path.append (str (dir_root) )  # Добавляю корневую папку в sys.path
dir_src = Path (dir_root, 'src')
sys.path.append (str (dir_root) )
...

print(dir_root)
```

## Импорты из модулей проекта

-   `from src import gs`: Импортирует модуль `gs` из директории `src`.
-   `from src.suppliers import Supplier`: Импортирует класс `Supplier` из модуля `suppliers` внутри директории `src`.
-   `from src.product import Product, ProductFields, ProductFieldsLocators`: Импортирует классы `Product`, `ProductFields`, `ProductFieldsLocators` из модуля `product` внутри директории `src`.
-   `from src.category import Category`: Импортирует класс `Category` из модуля `category` внутри директории `src`.
-   `from src.utils.jjson import j_dumps, j_loads, pprint, save_text_file`: Импортирует функции `j_dumps`, `j_loads`, `pprint`, `save_text_file` из модуля `jjson` внутри директории `src/utils`.
-   `from src.logger.logger import logger, StringNormalizer, ProductFieldsValidator`: Импортирует  `logger`, `StringNormalizer`, `ProductFieldsValidator` из модуля `logger` внутри директории `src/logger`.