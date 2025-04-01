# Модуль для запуска поставщика Kualastyle

## Обзор

Модуль предназначен для запуска поставщика Kualastyle. Он определяет функцию `start_supplier`, которая создает и возвращает экземпляр класса `Supplier` с заданными параметрами.

## Подробней

Этот модуль используется для инициализации и запуска процесса сбора и обработки данных о товарах от поставщика Kualastyle. Он импортирует необходимые классы и модули из других частей проекта `hypotez`, такие как `Supplier`, `Product`, `Category`, а также утилиты для работы со строками и нормализации данных.

## Функции

### `start_supplier`

```python
def start_supplier(supplier_prefix: str = 'kualastyle'):
    """
    Запускает поставщика Kualastyle.

    Args:
        supplier_prefix (str, optional): Префикс поставщика. По умолчанию 'kualastyle'.

    Returns:
        Supplier: Экземпляр класса Supplier с заданными параметрами.
    """
```

**Назначение**: Функция `start_supplier` создает и возвращает экземпляр класса `Supplier` с заданным префиксом.

**Параметры**:

- `supplier_prefix` (str, optional): Префикс поставщика. Используется для определения параметров конфигурации поставщика. По умолчанию имеет значение `'kualastyle'`.

**Возвращает**:

- `Supplier`: Экземпляр класса `Supplier`, созданный с параметром `supplier_prefix`.

**Как работает функция**:

1. **Определение параметров**: Функция создает словарь `params`, содержащий параметр `supplier_prefix`.
2. **Создание экземпляра `Supplier`**: Создается экземпляр класса `Supplier` с использованием словаря `params` в качестве аргументов.
3. **Возврат экземпляра**: Функция возвращает созданный экземпляр класса `Supplier`.

**Примеры**:

```python
from src.suppliers import Supplier
from src.suppliers.kualastyle._experiments.notebook_header import start_supplier

# Запуск поставщика с префиксом по умолчанию
supplier = start_supplier()
print(type(supplier))
# <class 'src.suppliers.supplier.Supplier'>

# Запуск поставщика с указанием префикса
supplier = start_supplier(supplier_prefix='test_supplier')
print(type(supplier))
# <class 'src.suppliers.supplier.Supplier'>
```