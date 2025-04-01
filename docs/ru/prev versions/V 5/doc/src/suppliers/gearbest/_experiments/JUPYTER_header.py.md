# Модуль src.suppliers.gearbest._experiments

## Обзор

Модуль содержит экспериментальный код, связанный с поставщиком Gearbest. Он включает в себя различные импорты и определения, необходимые для работы с данными о товарах, категориях и поставщиках. Модуль предназначен для использования в проекте `hypotez`.

## Подробней

Этот модуль, расположенный в каталоге `src/suppliers/gearbest/_experiments`, содержит экспериментальный код, который, вероятно, находится в стадии разработки или тестирования. Он импортирует множество модулей и классов, необходимых для работы с данными о товарах, категориях и поставщиках, а также для взаимодействия с PrestaShop.

## Функции

### `start_supplier`

```python
def start_supplier(supplier_prefix: str = 'aliexpress', locale: str = 'en'):
    """ Старт поставщика """
```

**Описание**: Функция для запуска поставщика.

**Как работает функция**:
1. Определяет параметры для запуска поставщика, включая префикс поставщика и локаль.
2. Создает экземпляр класса `Supplier` с переданными параметрами.
3. Возвращает созданный экземпляр поставщика.

**Параметры**:
- `supplier_prefix` (str, optional): Префикс поставщика. По умолчанию `'aliexpress'`.
- `locale` (str, optional): Локаль поставщика. По умолчанию `'en'`.

**Возвращает**:
- `Supplier`: Экземпляр класса `Supplier`.

**Примеры**:

```python
supplier = start_supplier(supplier_prefix='gearbest', locale='ru')
```
```python
supplier = start_supplier()
```
```python
supplier = start_supplier(locale='de')
```
```python
supplier = start_supplier(supplier_prefix='banggood', locale='en')
```
```python
supplier = start_supplier(supplier_prefix='alibaba', locale='zh')