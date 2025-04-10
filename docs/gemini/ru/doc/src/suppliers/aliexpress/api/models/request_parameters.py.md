# Модуль: src.suppliers.aliexpress.api.models.request_parameters

## Обзор

Модуль содержит классы, определяющие возможные значения параметров запросов к API AliExpress. Эти классы используются для типизации и валидации параметров при формировании запросов к API, таких как тип продукта, способ сортировки и тип ссылки.

## Подробнее

Данный код предоставляет перечисления (классы) для определения типов продуктов, способов сортировки и типов ссылок, используемых при взаимодействии с API AliExpress. Использование этих классов позволяет унифицировать и облегчить процесс формирования запросов, а также избежать ошибок, связанных с неправильными значениями параметров.

## Классы

### `ProductType`

**Описание**: Класс, определяющий возможные типы продуктов для запроса к API AliExpress.

**Принцип работы**:
Класс `ProductType` содержит константы, представляющие различные типы продуктов. Это позволяет использовать строго определенные значения при формировании запросов.

**Атрибуты**:
- `ALL` (str): Представляет все типы продуктов.
- `PLAZA` (str): Представляет продукты, доступные на площадке Plaza.
- `TMALL` (str): Представляет продукты, доступные на площадке Tmall.

**Методы**:
- Нет методов.

**Примеры**
```python
product_type = ProductType.ALL
print(product_type)  # Вывод: ALL
```

### `SortBy`

**Описание**: Класс, определяющий возможные способы сортировки результатов запроса к API AliExpress.

**Принцип работы**:
Класс `SortBy` содержит константы, представляющие различные способы сортировки продуктов. Это позволяет использовать строго определенные значения при формировании запросов.

**Атрибуты**:
- `SALE_PRICE_ASC` (str): Сортировка по возрастанию цены.
- `SALE_PRICE_DESC` (str): Сортировка по убыванию цены.
- `LAST_VOLUME_ASC` (str): Сортировка по возрастанию объема продаж.
- `LAST_VOLUME_DESC` (str): Сортировка по убыванию объема продаж.

**Методы**:
- Нет методов.

**Примеры**
```python
sort_order = SortBy.SALE_PRICE_ASC
print(sort_order)  # Вывод: SALE_PRICE_ASC
```

### `LinkType`

**Описание**: Класс, определяющий возможные типы ссылок для запроса к API AliExpress.

**Принцип работы**:
Класс `LinkType` содержит константы, представляющие различные типы ссылок. Это позволяет использовать строго определенные значения при формировании запросов.

**Атрибуты**:
- `NORMAL` (int): Представляет обычную ссылку.
- `HOTLINK` (int): Представляет партнерскую ссылку.

**Методы**:
- Нет методов.

**Примеры**
```python
link_type = LinkType.HOTLINK
print(link_type)  # Вывод: 2