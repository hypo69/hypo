# Модуль `JUPYTER_header.py`

## Обзор

Модуль предназначен для экспериментов с поставщиком eBay. Он содержит необходимые импорты и базовые функции для запуска поставщика.

## Подробней

Этот модуль используется для инициализации и запуска поставщика, а также для работы с продуктами и категориями. Он включает в себя импорты из различных модулей проекта `hypotez`, таких как `webdriver`, `suppliers`, `product`, `category` и `utils`. Также, в модуле определена функция `start_supplier`, предназначенная для запуска поставщика с указанными параметрами.

## Классы

В данном модуле нет классов.

## Функции

### `start_supplier`

```python
def start_supplier(supplier_prefix: str = 'aliexpress', locale: str = 'en') -> Supplier:
    """ Старт поставщика """
    params: dict = \
    {
        'supplier_prefix': supplier_prefix,
        'locale': locale
    }
    
    return Supplier(**params)
```

**Назначение**: Запускает поставщика с указанными параметрами.

**Параметры**:
- `supplier_prefix` (str, optional): Префикс поставщика. По умолчанию `'aliexpress'`.
- `locale` (str, optional): Локаль поставщика. По умолчанию `'en'`.

**Возвращает**:
- `Supplier`: Объект поставщика.

**Как работает функция**:
1. **Определение параметров**: Функция принимает два параметра: `supplier_prefix` и `locale`, которые определяют префикс и локаль поставщика соответственно.
2. **Создание словаря параметров**: Создается словарь `params`, содержащий переданные параметры `supplier_prefix` и `locale`.
3. **Инициализация и возврат поставщика**: Создается и возвращается объект `Supplier` с использованием распакованного словаря `params` в качестве аргументов.

**Примеры**:

```python
from src.suppliers import Supplier  # Предполагается, что класс Supplier находится в модуле src.suppliers

# Пример запуска поставщика с параметрами по умолчанию
supplier = start_supplier()
print(supplier)  # Вывод: <src.suppliers.Supplier object at ...>

# Пример запуска поставщика с указанием префикса и локали
supplier = start_supplier(supplier_prefix='ebay', locale='de')
print(supplier)  # Вывод: <src.suppliers.Supplier object at ...>
```
```
A → B → C
```

- **A**: Принимает `supplier_prefix` и `locale`.
- **B**: Формирует словарь `params`.
- **C**: Создает и возвращает объект `Supplier`.