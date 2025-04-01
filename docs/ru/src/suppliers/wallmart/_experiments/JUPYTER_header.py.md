# Модуль `src.suppliers.wallmart._experiments.JUPYTER_header`

## Обзор

Модуль предназначен для экспериментов и отладки, связанных с поставщиком Walmart. 
Он содержит набор импортов и функций, необходимых для работы с веб-драйвером, поставщиками, продуктами, категориями, утилитами и API PrestaShop.
Предположительно, модуль использовался в Jupyter Notebook для интерактивной разработки и тестирования.

## Подробнее

Этот модуль является частью проекта `hypotez` и предназначен для работы с данными поставщика Walmart. 
Он содержит функции для запуска поставщика, а также импортирует необходимые классы и функции из других модулей проекта.

## Функции

### `start_supplier`

```python
def start_supplier(supplier_prefix: str = 'aliexpress', locale: str = 'en') -> Supplier:
    """ Старт поставщика 
    Args:
        supplier_prefix (str, optional): Префикс поставщика. По умолчанию 'aliexpress'.
        locale (str, optional): Локаль поставщика. По умолчанию 'en'.

    Returns:
        Supplier: Возвращает объект Supplier, инициализированный с указанными параметрами.

    Как работает функция:
    1. Функция создает словарь `params`, содержащий префикс и локаль поставщика.
    2. Затем функция возвращает экземпляр класса `Supplier`, инициализированный с использованием словаря `params`.

    Внутри функции происхоят следующие действия и преобразования:
     Инициализация параметров поставщика
     |
     Создание экземпляра класса `Supplier` с заданными параметрами

    Примеры:
        >>> supplier = start_supplier(supplier_prefix='wallmart', locale='ru')
        >>> print(supplier.prefix)
        wallmart
        >>> print(supplier.locale)
        ru
    """
    params: dict = \
    {
        'supplier_prefix': supplier_prefix,
        'locale': locale
    }
    
    return Supplier(**params)