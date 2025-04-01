# Модуль: src.suppliers.ebay._experiments

## Обзор

Модуль `src.suppliers.ebay._experiments` содержит экспериментальный код, связанный с поставщиком eBay. Включает в себя импорты необходимых библиотек, определение корневой директории проекта, добавление путей к системным переменным, а также функцию для запуска поставщика.

## Подробней

Модуль предоставляет базовую структуру для экспериментов с поставщиком eBay. Он настраивает окружение, добавляет необходимые пути в `sys.path`, импортирует классы и функции, используемые в дальнейшей работе с поставщиком, и предоставляет функцию `start_supplier` для инициализации поставщика с заданными параметрами. Этот код служит отправной точкой для разработки и тестирования новых функций и улучшений, связанных с eBay.

## Функции

### `start_supplier`

```python
def start_supplier(supplier_prefix: str = 'aliexpress', locale: str = 'en') -> Supplier:
    """Старт поставщика

    Args:
        supplier_prefix (str, optional): Префикс поставщика. По умолчанию 'aliexpress'.
        locale (str, optional): Локаль поставщика. По умолчанию 'en'.

    Returns:
        Supplier: Объект поставщика Supplier.

    Raises:
        Нет исключений.

    Example:
        >>> supplier = start_supplier(supplier_prefix='ebay', locale='ru')
        >>> print(supplier)
        <src.suppliers.Supplier object at ...>
    """
    ...
```

**Назначение**: Функция `start_supplier` создает и возвращает объект поставщика `Supplier` с заданными параметрами.

**Параметры**:
- `supplier_prefix` (str, optional): Префикс поставщика. Используется для определения типа поставщика (например, 'aliexpress', 'ebay'). По умолчанию 'aliexpress'.
- `locale` (str, optional): Локаль поставщика. Указывает язык и регион, которые будут использоваться при работе с поставщиком. По умолчанию 'en'.

**Возвращает**:
- `Supplier`: Объект класса `Supplier`, инициализированный с переданными параметрами.

**Как работает функция**:
1. Определяется словарь `params`, содержащий переданные аргументы `supplier_prefix` и `locale`.
2. Создается и возвращается экземпляр класса `Supplier` с использованием словаря `params` в качестве аргументов.

**Примеры**:

```python
from src.suppliers import Supplier  # Предполагается, что класс Supplier находится в модуле src.suppliers

# Пример вызова функции start_supplier с параметрами по умолчанию
supplier_default = start_supplier()
print(supplier_default)  # Вывод: <src.suppliers.Supplier object at ...>

# Пример вызова функции start_supplier с указанием префикса и локали поставщика
supplier_ebay_ru = start_supplier(supplier_prefix='ebay', locale='ru')
print(supplier_ebay_ru)  # Вывод: <src.suppliers.Supplier object at ...>