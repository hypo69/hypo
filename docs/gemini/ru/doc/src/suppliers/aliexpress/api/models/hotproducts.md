# Модуль hypotez/src/suppliers/aliexpress/api/models/hotproducts.py

## Обзор

Данный модуль содержит определение класса `HotProductsResponse`, который представляет собой ответ API для получения списка популярных продуктов (hot products).  Класс содержит информацию о текущей странице, количестве записей на текущей странице и общем количестве записей, а также список объектов `Product`.

## Оглавление

- [Модуль `HotProductsResponse`](#модуль-hotproductsresponse)


## Классы

### `HotProductsResponse`

**Описание**: Класс `HotProductsResponse` представляет ответ API для получения списка популярных продуктов. Он содержит информацию о текущей странице, количестве записей на текущей странице и общем количестве записей, а также список объектов `Product`.

**Атрибуты**:

- `current_page_no` (int): Номер текущей страницы.
- `current_record_count` (int): Количество записей на текущей странице.
- `total_record_count` (int): Общее количество записей.
- `products` (List[Product]): Список объектов `Product`.

```python
class HotProductsResponse:
    current_page_no: int
    current_record_count: int
    total_record_count: int
    products: List[Product]
```

**Примечание**:  В данном модуле используется класс `Product`, предполагается, что он определен в другом месте (например, в файле `product.py`).  Рекомендуется добавить импорт `Product` вместе с другими импортами в начале модуля.
```