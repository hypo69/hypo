# Модуль для экспериментов со сценариями

## Обзор

Этот модуль предназначен для экспериментов со сценариями, используемыми в проекте `hypotez`. Он содержит код для запуска и тестирования различных сценариев, связанных с поставщиками (например, `aliexpress`, `amazon`, `kualastyle`, `ebay`).

## Подробней

Модуль добавляет корневую папку проекта `hypotez` в `sys.path`, что позволяет импортировать другие модули проекта. Он использует классы `Scenario` и `Supplier` для моделирования и выполнения сценариев. Эксперименты могут включать в себя тестирование различных поставщиков и их интеграцию в систему.

## Функции

### `start_supplier`

```python
def start_supplier(supplier_prefix: str) -> Supplier:
    """
    Создает и возвращает экземпляр класса `Supplier` с заданным префиксом.

    Args:
        supplier_prefix (str): Префикс поставщика, например, 'aliexpress', 'amazon'.

    Returns:
        Supplier: Объект поставщика, созданный на основе предоставленного префикса.
    """
```

**Назначение**:
Функция `start_supplier` создает объект класса `Supplier` с заданным префиксом. Это позволяет инициализировать поставщика с определенными параметрами.

**Параметры**:
- `supplier_prefix` (str): Префикс поставщика (например, 'aliexpress').

**Возвращает**:
- `Supplier`: Объект класса `Supplier`.

**Как работает функция**:
1. Функция принимает префикс поставщика в качестве аргумента.
2. Создает словарь `params` с ключом `'supplier_prefix'` и значением, равным переданному префиксу.
3. Создает экземпляр класса `Supplier`, передавая словарь `params` в качестве аргументов.
4. Возвращает созданный экземпляр класса `Supplier`.

**Примеры**:

```python
supplier_aliexpress = start_supplier('aliexpress')
supplier_amazon = start_supplier('amazon')
```

## Переменные

### `s`

```python
s = start_supplier(supplier_prefix)
```

`s` - экземпляр класса `Supplier`, созданный на основе префикса поставщика.

**Описание**:
Переменная `s` содержит объект класса `Supplier`, который используется для работы с поставщиками.

### `scenario`

```python
scenario = Scenario(s)
```

`scenario` - экземпляр класса `Scenario`, который принимает объект `Supplier` `s` в качестве аргумента.

**Описание**:
Переменная `scenario` содержит объект класса `Scenario`, используемый для запуска сценариев.

## Код

```python
import sys
import os
path = os.getcwd()[:os.getcwd().rfind(r'hypotez')]
sys.path.append(path)  # Добавляю корневую папку в sys.path

from pathlib import Path
import json
import re

from hypotez import gs
from src.utils.printer import  pprint

from src.scenario import Scenario
from src.suppliers import Supplier

def start_supplier(supplier_prefix: str) -> Supplier:
    params: dict = \
    {
        'supplier_prefix': supplier_prefix
    }
    
    return Supplier(**params)


supplier_prefix = 'aliexpress'
#supplier_prefix = 'amazon'
#supplier_prefix = 'kualastyle'
#supplier_prefix = 'ebay'

s = start_supplier(supplier_prefix)
""" s - на протяжении всего кода означает класс `Supplier` """

print(" Можно продолжать ")

scenario = Scenario(s)

scenario.run_scenarios()