# `JUPYTER_header.py`

## Обзор

Файл содержит набор импортов и определение функции `start_supplier`. Это экспериментальный файл, используемый в Jupyter Notebook для разработки и тестирования.

## Подробней

Этот файл содержит определения, необходимые для запуска и тестирования поставщиков (suppliers) в контексте Jupyter Notebook. Файл содержит импорты модулей и определение функции `start_supplier()`, которая создает экземпляр класса `Supplier` с заданными параметрами.

## Функции

### `start_supplier`

```python
def start_supplier(supplier_prefix: str = 'aliexpress', locale: str = 'en'):
    """ Старт поставщика """
```

**Описание**: Функция для инициализации и запуска поставщика.

**Как работает функция**:
Функция принимает префикс поставщика и локаль в качестве параметров и создает словарь `params` с этими значениями. Затем она возвращает экземпляр класса `Supplier`, инициализированный с использованием переданных параметров.

**Параметры**:
- `supplier_prefix` (str, optional): Префикс поставщика. По умолчанию 'aliexpress'.
- `locale` (str, optional): Локаль. По умолчанию 'en'.

**Возвращает**:
- `Supplier`: Объект поставщика, созданный с использованием переданных параметров.

**Примеры**:

```python
supplier = start_supplier(supplier_prefix='aliexpress', locale='en')
print(supplier)
# <src.suppliers.Supplier object at 0x...>
```
```python
supplier = start_supplier()
print(supplier)
# <src.suppliers.Supplier object at 0x...>
```
```python
supplier = start_supplier(locale='ru')
print(supplier)
# <src.suppliers.Supplier object at 0x...>
```
```python
supplier = start_supplier(supplier_prefix='amazon', locale='de')
print(supplier)
# <src.suppliers.Supplier object at 0x...>