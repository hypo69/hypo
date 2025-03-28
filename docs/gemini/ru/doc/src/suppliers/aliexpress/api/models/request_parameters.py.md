# `request_parameters.py`

## Обзор

Модуль `request_parameters.py` содержит определения классов, представляющих параметры запросов к API AliExpress. Эти классы используются для задания различных типов продуктов, способов сортировки и типов ссылок при выполнении запросов.

## Подробней

Этот модуль предоставляет перечисления (классы с константами) для облегчения и стандартизации процесса формирования запросов к API AliExpress. Он определяет возможные значения для фильтрации и сортировки результатов поиска, а также для указания типа ссылки.

## Классы

### `ProductType`

**Описание**:
Класс, определяющий типы продуктов, которые могут быть запрошены через API AliExpress.

**Методы**:
- `ALL`: Все типы продуктов.
- `PLAZA`: Продукты, доступные на площадке Plaza.
- `TMALL`: Продукты, доступные на площадке Tmall.

**Примеры**
```python
product_type = ProductType()
print(product_type.ALL)
print(product_type.PLAZA)
```

### `SortBy`

**Описание**:
Класс, определяющий способы сортировки результатов поиска продуктов.

**Методы**:
- `SALE_PRICE_ASC`: Сортировка по возрастанию цены.
- `SALE_PRICE_DESC`: Сортировка по убыванию цены.
- `LAST_VOLUME_ASC`: Сортировка по возрастанию объема продаж.
- `LAST_VOLUME_DESC`: Сортировка по убыванию объема продаж.

**Примеры**
```python
sort_by = SortBy()
print(sort_by.SALE_PRICE_ASC)
print(sort_by.LAST_VOLUME_DESC)
```

### `LinkType`

**Описание**:
Класс, определяющий типы ссылок, которые могут быть использованы.

**Методы**:
- `NORMAL`: Обычная ссылка.
- `HOTLINK`: Горячая ссылка.

**Примеры**
```python
link_type = LinkType()
print(link_type.NORMAL)
print(link_type.HOTLINK)
```