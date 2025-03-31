# Модуль _experiments

## Обзор

Модуль `_experiments` предназначен для экспериментов в рамках поставщика `visualdg`. В коде задаются пути к директориям, добавляются пути к системным переменным, импортируются необходимые модули и классы, а также определена функция `start_supplier` для запуска поставщика.

## Подробней

Этот модуль, по-видимому, является частью более крупной системы, в которой поставщики (`Supplier`) управляют данными о продуктах и категориях. Функция `start_supplier` позволяет инициализировать и запустить конкретного поставщика с заданными параметрами, такими как префикс поставщика и локаль. Импортируемые классы и модули, такие как `Driver`, `Product`, `Category`, `StringFormatter`, `StringNormalizer`, `PrestaShop.Product`, указывают на взаимодействие с веб-драйвером, обработку продуктов и категорий, форматирование строк и взаимодействие с PrestaShop.

## Функции

### `start_supplier`

```python
def start_supplier(supplier_prefix: str = 'aliexpress', locale: str = 'en'):
    """ Старт поставщика """
    params: dict = \
    {
        'supplier_prefix': supplier_prefix,
        'locale': locale
    }
    
    return Supplier(**params)
```

**Как работает функция**:

Функция `start_supplier` создает и возвращает экземпляр класса `Supplier` с заданными параметрами. Она принимает два аргумента: `supplier_prefix` и `locale`, которые используются для конфигурации поставщика. Функция создает словарь `params`, содержащий эти параметры, и затем передает этот словарь в конструктор класса `Supplier` с помощью оператора `**`, который распаковывает словарь в именованные аргументы.

**Параметры**:

- `supplier_prefix` (str, optional): Префикс поставщика. По умолчанию `'aliexpress'`.
- `locale` (str, optional): Локаль. По умолчанию `'en'`.

**Возвращает**:

- `Supplier`: Экземпляр класса `Supplier`, сконфигурированный с заданными параметрами.

**Примеры**:

```python
supplier = start_supplier(supplier_prefix='aliexpress', locale='en')
```

```python
supplier = start_supplier(supplier_prefix='amazon', locale='de')
```
```python
params: dict = \
    {
        'supplier_prefix': supplier_prefix,
        'locale': locale
    }
```
```python
return Supplier(**params))