# Модуль `test_scenario.py`

## Обзор

Модуль `test_scenario.py` предназначен для экспериментов и тестирования сценариев работы с поставщиками в проекте `hypotez`. Он включает в себя запуск сценариев для различных поставщиков, таких как AliExpress, Amazon, KuaLasta и eBay. Модуль использует классы `Scenario` и `Supplier` для моделирования и управления этими сценариями.

## Подробней

Этот файл служит для проверки и отладки логики взаимодействия с различными поставщиками. Он создает экземпляры класса `Supplier` с разными префиксами поставщиков и запускает сценарии, определенные в классе `Scenario`. Это позволяет проверить, как система обрабатывает разные источники данных и адаптируется к их особенностям.

## Функции

### `start_supplier`

```python
def start_supplier(supplier_prefix: str) -> Supplier:
    """
    Args:
        supplier_prefix (str): Префикс поставщика (например, 'aliexpress', 'amazon').

    Returns:
        Supplier: Экземпляр класса `Supplier`, инициализированный с указанным префиксом.

    Example:
        >>> supplier = start_supplier('aliexpress')
        >>> print(supplier.supplier_prefix)
        aliexpress
    """
```

**Описание**: Функция `start_supplier` создает и возвращает экземпляр класса `Supplier` с заданным префиксом поставщика.

**Параметры**:
- `supplier_prefix` (str): Префикс поставщика, используемый для инициализации экземпляра `Supplier`.

**Возвращает**:
- `Supplier`: Экземпляр класса `Supplier`, настроенный для работы с указанным поставщиком.

**Примеры**:
```python
supplier = start_supplier('aliexpress')
print(supplier.supplier_prefix)
```

## Переменные

- `supplier_prefix` (str): Определяет, с каким поставщиком будет работать сценарий. Может принимать значения 'aliexpress', 'amazon', 'kualastyle' или 'ebay'.
- `s` (Supplier): Экземпляр класса `Supplier`, созданный с использованием функции `start_supplier`.
- `scenario` (Scenario): Экземпляр класса `Scenario`, использующий экземпляр `Supplier` для выполнения сценариев.

## Пример использования

```python
from src.scenario import Scenario
from src.suppliers import Supplier

def start_supplier(supplier_prefix: str) -> Supplier:
    params: dict = {
        'supplier_prefix': supplier_prefix
    }
    return Supplier(**params)

supplier_prefix = 'aliexpress'
s = start_supplier(supplier_prefix)
scenario = Scenario(s)
scenario.run_scenarios()
```