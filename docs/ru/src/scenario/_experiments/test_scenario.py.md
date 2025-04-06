# Модуль test_scenario.py

## Обзор

Модуль `test_scenario.py` представляет собой экспериментальный сценарий для тестирования и запуска сценариев, связанных с различными поставщиками (например, AliExpress, Amazon, Kualastyle, eBay). Он использует классы `Scenario` и `Supplier` из проекта `hypotez` для моделирования и выполнения сценариев взаимодействия с поставщиками.

## Подробнее

Модуль предназначен для запуска сценариев, связанных с различными поставщиками. Он инициализирует поставщика с заданным префиксом (например, 'aliexpress') и затем использует класс `Scenario` для запуска сценариев, связанных с этим поставщиком.

## Классы

В данном модуле классы не определены. Используются классы `Scenario` и `Supplier` из других модулей.

## Функции

### `start_supplier`

```python
def start_supplier(supplier_prefix: str) -> Supplier:
    """
    Создает и возвращает экземпляр класса `Supplier` с заданным префиксом.

    Args:
        supplier_prefix (str): Префикс поставщика (например, 'aliexpress', 'amazon').

    Returns:
        Supplier: Экземпляр класса `Supplier`.

    Example:
        >>> supplier = start_supplier('aliexpress')
        >>> print(type(supplier))
        <class 'src.suppliers.Supplier'>
    """
```

**Назначение**: Функция создает и возвращает экземпляр класса `Supplier` с заданным префиксом.

**Параметры**:
- `supplier_prefix` (str): Префикс поставщика, используемый для инициализации объекта `Supplier`.

**Возвращает**:
- `Supplier`: Объект класса `Supplier`, созданный с использованием переданного префикса.

**Как работает функция**:
1. Функция принимает префикс поставщика `supplier_prefix` в качестве аргумента.
2. Создается словарь `params`, содержащий префикс поставщика.
3. Создается экземпляр класса `Supplier` с использованием параметров из словаря `params`.
4. Возвращается созданный экземпляр класса `Supplier`.

```
    A[Принимает supplier_prefix]
    |
    B[Создает словарь params с supplier_prefix]
    |
    C[Создает экземпляр класса Supplier с params]
    |
    D[Возвращает экземпляр Supplier]
```

**Примеры**:

```python
supplier = start_supplier('aliexpress')
print(type(supplier))
```

## Переменные

### `supplier_prefix`

```python
supplier_prefix = 'aliexpress'
#supplier_prefix = 'amazon'
#supplier_prefix = 'kualastyle'
#supplier_prefix = 'ebay'
```

`supplier_prefix` (str): Определяет префикс поставщика, который будет использоваться для создания экземпляра класса `Supplier`. В коде закомментированы другие варианты значений: `amazon`, `kualastyle` и `ebay`.

### `s`

```python
s = start_supplier(supplier_prefix)
""" s - на протяжении всего кода означает класс `Supplier` """
```

`s` (Supplier): Экземпляр класса `Supplier`, созданный с использованием функции `start_supplier` и префикса `supplier_prefix`.

### `scenario`

```python
scenario = Scenario(s)
```

`scenario` (Scenario): Экземпляр класса `Scenario`, созданный с использованием экземпляра класса `Supplier` (`s`).

## Запуск сценария

```python
scenario.run_scenarios()
```

Метод `run_scenarios()` запускает сценарии, связанные с текущим поставщиком.