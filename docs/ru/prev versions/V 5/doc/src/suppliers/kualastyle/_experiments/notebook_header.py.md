# src.suppliers.kualastyle._experiments.notebook_header

## Обзор

Этот модуль содержит код, который, вероятно, использовался для экспериментов или прототипирования в рамках работы с поставщиком Kualastyle. Он включает импорты различных модулей и классов, используемых в проекте hypotez, а также функцию `start_supplier`, предназначенную для инициализации поставщика.

## Подробней

Этот файл, судя по названию `notebook_header.py`, мог быть частью Jupyter Notebook или подобной среды, где проводились эксперименты. Код включает импорт стандартных библиотек, таких как `sys`, `os`, `pathlib`, `json`, `re`, а также модулей из проекта `hypotez`, таких как `gs`, `Supplier`, `Product`, `Category` и другие утилиты. Функция `start_supplier` предназначена для инициализации объекта поставщика с заданным префиксом.

## Функции

### `start_supplier`

```python
def start_supplier(supplier_prefix: str = 'kualastyle') -> Supplier:
    """ Старт поставщика (kualastyle)"""
```

**Описание**: Инициализирует и возвращает объект поставщика (`Supplier`).

**Как работает функция**:
1.  Принимает префикс поставщика `supplier_prefix` (по умолчанию `'kualastyle'`) в качестве аргумента.
2.  Создает словарь `params`, содержащий `supplier_prefix`.
3.  Инициализирует объект `Supplier` с параметрами из словаря `params`.
4.  Возвращает созданный объект `Supplier`.

**Параметры**:

*   `supplier_prefix` (str, optional): Префикс поставщика. По умолчанию `'kualastyle'`.

**Возвращает**:

*   `Supplier`: Объект поставщика, инициализированный с заданными параметрами.

**Примеры**:

```python
supplier = start_supplier()
print(type(supplier))
#  <class 'src.suppliers.Supplier'>
```

```python
supplier = start_supplier(supplier_prefix='another_supplier')
print(supplier.prefix)
#  another_supplier