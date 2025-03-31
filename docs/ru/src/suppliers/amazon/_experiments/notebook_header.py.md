# Модуль `notebook_header.py`

## Обзор

Модуль содержит набор импортов и определение переменной `dir_root`, используемой для добавления корневой директории проекта в `sys.path`. Также содержит функцию `start_supplier`, предназначенную для запуска поставщика с заданными параметрами.

## Подробней

Этот модуль, вероятно, используется для настройки окружения и импорта необходимых модулей для экспериментов, связанных с поставщиком Amazon. Он подготавливает пути и выполняет импорты, необходимые для работы с драйверами веб-браузеров, поставщиками, продуктами и категориями.

## Переменные

### `dir_root`

**Описание**: Переменная `dir_root` определяет корневую директорию проекта `hypotez`.

**Как работает переменная**:
1.  Получает текущую рабочую директорию с помощью `os.getcwd()`.
2.  Определяет индекс последнего вхождения строки `'hypotez'` в текущей рабочей директории.
3.  Извлекает подстроку текущей рабочей директории до конца слова `'hypotez'`, включая его (добавляет 7 символов, чтобы включить `'hypotez'`).
4.  Создает объект `Path` из полученной подстроки.

```python
dir_root : Path = Path (os.getcwd()[:os.getcwd().rfind('hypotez')+7])
```

## Функции

### `start_supplier`

```python
def start_supplier(supplier_prefix, locale):
    """ Старт поставщика """
    if not supplier_prefix and not locale: return "Не задан сценарий и язык"
    
    params: dict = \
    {
        'supplier_prefix': supplier_prefix,
        'locale': locale
    }
    
    return Supplier(**params)
```

**Описание**: Функция `start_supplier` создает экземпляр класса `Supplier` с заданными параметрами `supplier_prefix` и `locale`.

**Как работает функция**:

1.  Проверяет, заданы ли параметры `supplier_prefix` и `locale`. Если хотя бы один из них не задан, функция возвращает сообщение об ошибке "Не задан сценарий и язык".
2.  Создает словарь `params`, содержащий параметры `supplier_prefix` и `locale`.
3.  Создает и возвращает экземпляр класса `Supplier`, передавая словарь `params` в качестве аргументов конструктора.

**Параметры**:

*   `supplier_prefix` (str): Префикс поставщика.
*   `locale` (str): Локаль.

**Возвращает**:

*   `Supplier`: Экземпляр класса `Supplier` с заданными параметрами.
*   `str`: Строка "Не задан сценарий и язык", если параметры `supplier_prefix` и `locale` не заданы.

**Примеры**:

```python
from src.suppliers import Supplier # Это надо импортировать чтобы пример заработал
supplier = start_supplier(supplier_prefix='amazon', locale='us')
print(supplier) #  <src.suppliers.supplier.Supplier object at 0x...>
```
```python
supplier = start_supplier(supplier_prefix='', locale='')
print(supplier) # Не задан сценарий и язык
```
```python
supplier = start_supplier(supplier_prefix='amazon', locale='')
print(supplier) # <src.suppliers.supplier.Supplier object at 0x...>
```
```python
supplier = start_supplier(supplier_prefix='', locale='ru')
print(supplier) # <src.suppliers.supplier.Supplier object at 0x...>
```
```