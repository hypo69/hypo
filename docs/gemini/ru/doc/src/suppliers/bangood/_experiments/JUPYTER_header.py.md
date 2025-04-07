# Модуль _experiments

## Обзор

Модуль `_experiments` является частью пакета `src.suppliers.bangood` и предназначен для экспериментальных разработок. В данном модуле содержатся импорты библиотек, необходимые для работы с поставщиками, продуктами, категориями и веб-драйвером. Также в модуле определена функция `start_supplier` для запуска поставщика с заданными параметрами.

## Подробней

Этот модуль используется для экспериментов с кодом, связанным с поставщиком Banggood. Он содержит импорты, настройки путей и функцию для запуска поставщика. В дальнейшем здесь могут разрабатываться новые функции и классы для работы с данными от Banggood, которые потом могут быть перенесены в основные модули проекта.

## Функции

### `start_supplier`

```python
def start_supplier(supplier_prefix: str = 'aliexpress', locale: str = 'en') -> Supplier:
    """ Старт поставщика 
    Args:
        supplier_prefix (str, optional): Префикс поставщика. По умолчанию 'aliexpress'.
        locale (str, optional): Языковая настройка. По умолчанию 'en'.

    Returns:
        Supplier: Возвращает объект поставщика `Supplier`.

    """
    params: dict = {
        'supplier_prefix': supplier_prefix,
        'locale': locale
    }
    
    return Supplier(**params)
```

**Назначение**: Запускает поставщика с указанным префиксом и языковой настройкой.

**Параметры**:
- `supplier_prefix` (str, optional): Префикс поставщика. По умолчанию `'aliexpress'`.
- `locale` (str, optional): Языковая настройка. По умолчанию `'en'`.

**Возвращает**:
- `Supplier`: Объект поставщика `Supplier`, созданный с переданными параметрами.

**Как работает функция**:
1. Функция принимает префикс поставщика и языковую настройку.
2. Создает словарь `params` с переданными параметрами.
3. Инициализирует и возвращает объект `Supplier` с использованием словаря `params` в качестве аргументов.

```
start_supplier
   │
   └── Создание словаря параметров `params`
   │
   └── Инициализация объекта `Supplier` с параметрами из `params`
   │
   └── Возврат объекта `Supplier`
```

**Примеры**:

```python
from src.suppliers import Supplier  # Предполагается, что Supplier импортируется именно так

# Запуск поставщика с префиксом 'aliexpress' и локалью 'en'
supplier1 = start_supplier()
print(type(supplier1))  # Вывод: <class 'src.suppliers.Supplier'>

# Запуск поставщика с префиксом 'banggood' и локалью 'ru'
supplier2 = start_supplier(supplier_prefix='banggood', locale='ru')
print(type(supplier2))  # Вывод: <class 'src.suppliers.Supplier'>