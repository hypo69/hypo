# Модуль `src.suppliers.etzmaleh._experiments.JUPYTER_header`

## Обзор

Модуль предназначен для экспериментов и содержит код, связанный с поставщиками, веб-драйверами и обработкой данных для проекта `hypotez`. Включает в себя импорты различных модулей и определение функции для запуска поставщика.

## Подробней

Этот модуль, судя по его расположению, является частью экспериментального кода в рамках работы с поставщиком Etzmaleh. Он содержит импорты необходимых модулей, таких как `Driver` для управления веб-драйвером, `Supplier` для работы с поставщиками, `Product` и `Category` для представления данных о продуктах и категориях, а также утилиты для обработки строк. Также здесь определена функция `start_supplier`, предназначенная для запуска процесса работы с поставщиком.

## Функции

### `start_supplier`

```python
def start_supplier(supplier_prefix: str = 'aliexpress', locale: str = 'en'):
    """Старт поставщика
    
    Args:
        supplier_prefix (str, optional): Префикс поставщика. По умолчанию 'aliexpress'.
        locale (str, optional): Локаль поставщика. По умолчанию 'en'.
    
    Returns:
        Supplier: Объект поставщика, созданный с переданными параметрами.
        
    Example:
        >>> supplier = start_supplier(supplier_prefix='my_supplier', locale='fr')
        >>> print(supplier.prefix)
        my_supplier
    """
```

**Назначение**: Функция `start_supplier` создает и возвращает объект класса `Supplier` с заданными параметрами `supplier_prefix` и `locale`.

**Параметры**:
- `supplier_prefix` (str, optional): Префикс поставщика, используемый для определения конкретного поставщика. По умолчанию имеет значение `'aliexpress'`.
- `locale` (str, optional): Локаль поставщика, определяющая язык и региональные настройки. По умолчанию имеет значение `'en'`.

**Возвращает**:
- `Supplier`: Объект класса `Supplier`, инициализированный с переданными параметрами `supplier_prefix` и `locale`.

**Как работает функция**:

1. **Определение параметров**:
   - Функция принимает два параметра: `supplier_prefix` (префикс поставщика) и `locale` (локаль).

2. **Создание словаря параметров**:
   - Создается словарь `params`, содержащий переданные параметры `supplier_prefix` и `locale`.

3. **Создание и возврат объекта `Supplier`**:
   - Используя оператор `**params`, словарь параметров передается в конструктор класса `Supplier`.
   - Возвращается созданный объект `Supplier`.

**Примеры**:

```python
supplier = start_supplier(supplier_prefix='my_supplier', locale='fr')
print(supplier.prefix)
# Ожидаемый вывод: my_supplier
```
```python
supplier = start_supplier()
print(supplier.prefix)
# Ожидаемый вывод: aliexpress
```