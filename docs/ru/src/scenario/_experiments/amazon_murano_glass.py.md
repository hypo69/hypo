# Модуль `amazon_murano_glass`

## Обзор

Модуль `amazon_murano_glass.py` предназначен для запуска сценария парсинга товаров "Муранское стекло" с сайта Amazon. Он использует класс `Supplier` для управления процессом парсинга и запускает определенный сценарий из `dict_scenarios.py`.

## Подробней

Модуль выполняет следующие шаги:

1.  Импортирует необходимые модули и функции из `header.py`.
2.  Инициализирует класс `Supplier` с именем 'amazon', используя функцию `start_supplier`.
3.  Запускает сценарий 'Murano Glass' из словаря `scenario`, используя метод `run_scenario` класса `Supplier`.
4.  Извлекает первый ключ из словаря `default_category` внутри `presta_categories` из текущего сценария.

## Функции

### `start_supplier`

```python
def start_supplier(supplier_name: str) -> Supplier:
    """
    Создает и инициализирует объект Supplier для указанного поставщика.

    Args:
        supplier_name (str): Название поставщика.

    Returns:
        Supplier: Объект класса Supplier.
    """
    ...
```

**Назначение**: Функция `start_supplier` создает и инициализирует объект `Supplier` с указанным именем поставщика.

**Параметры**:

*   `supplier_name` (str): Название поставщика, для которого создается объект `Supplier`.

**Возвращает**:

*   `Supplier`: Объект класса `Supplier`, инициализированный с указанным именем поставщика.

**Как работает функция**:

1.  Принимает название поставщика (`supplier_name`) в качестве аргумента.
2.  Создает экземпляр класса `Supplier` с переданным именем.
3.  Возвращает созданный объект `Supplier`.

```
    Начало
    ↓
    Создание экземпляра Supplier
    ↓
    Конец
```

**Примеры**:

```python
s = start_supplier('amazon')
```

## Переменные

-   `s`: Объект класса `Supplier`, представляющий поставщика 'amazon'.
-   `k`: Первый ключ из словаря `default_category` внутри `presta_categories` из текущего сценария.

## Использование

```python
import header
from header import start_supplier

s = start_supplier('amazon')

from dict_scenarios import scenario
s.run_scenario(scenario['Murano Glass'])

k = list(s.current_scenario['presta_categories']['default_category'].keys())[0]
```

В данном коде происходит следующее:

1.  Импортируются необходимые модули и функции из `header.py`.
2.  Создается объект `Supplier` с именем 'amazon'.
3.  Запускается сценарий 'Murano Glass' из словаря `scenario`.
4.  Извлекается первый ключ из словаря `default_category`.