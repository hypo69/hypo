# Модуль `hypotez/src/suppliers/aliexpress/api/helpers/products.py`

## Обзор

Этот модуль содержит функции для обработки данных о продуктах, полученных с API AliExpress.  Функции `parse_product` и `parse_products` предназначены для преобразования и подготовки данных для дальнейшего использования.

## Функции

### `parse_product`

**Описание**: Функция преобразует объект `product`, изменяя атрибут `product_small_image_urls` на строковое представление.

**Параметры**:
- `product`: Объект, содержащий данные о продукте.  Предполагается, что у него есть атрибут `product_small_image_urls`, который является итерируемым объектом, и метод `string` для получения строки из итерируемого объекта.

**Возвращает**:
- `product`: Объект `product` с измененным атрибутом `product_small_image_urls`.

**Вызывает исключения**:
- `AttributeError`: Возникает, если у объекта `product` нет атрибута `product_small_image_urls` или метод `string` для него недоступен.
- `TypeError`: Возникает, если атрибут `product_small_image_urls` не является итерируемым объектом.


### `parse_products`

**Описание**: Функция обрабатывает список объектов `products`, применяя функцию `parse_product` к каждому элементу.

**Параметры**:
- `products`: Список объектов `product`.

**Возвращает**:
- `new_products`: Новый список объектов `product`, обработанных функцией `parse_product`.

**Вызывает исключения**:
- `TypeError`: Возникает, если `products` не является списком.
- `TypeError`: Возникает, если элементы списка `products` не являются объектами, к которым можно применить функцию `parse_product`.