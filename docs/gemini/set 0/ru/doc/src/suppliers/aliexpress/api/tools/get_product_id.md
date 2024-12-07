# Модуль `hypotez/src/suppliers/aliexpress/api/tools/get_product_id.py`

## Обзор

Данный модуль содержит функцию `get_product_id`, предназначенную для извлечения идентификатора продукта из предоставленного текста.  Функция использует вспомогательную функцию `extract_prod_ids` для поиска идентификатора.

## Функции

### `get_product_id`

**Описание**: Возвращает идентификатор продукта, извлеченный из входного текста.  Если идентификатор не найден, генерирует исключение `ProductIdNotFoundException`.

**Параметры**:

- `raw_product_id` (str): Входной текст, содержащий идентификатор продукта.


**Возвращает**:

- str:  Идентификатор продукта, извлеченный из входного текста.

**Вызывает исключения**:

- `ProductIdNotFoundException`: Возникает, если идентификатор продукта не может быть найден в переданном `raw_product_id`.


## Модуль `src.suppliers.aliexpress.utils.extract_product_id`

**Описание**: Этот модуль не документирован в данном файле.  Предполагается, что функция `extract_prod_ids` определена в этом модуле и выполняет извлечение идентификатора продукта из различных типов входов (например, URL, текстовые строки).


## Модуль `hypotez/src/suppliers/aliexpress/errors`

**Описание**: Этот модуль содержит определение класса `ProductIdNotFoundException`,  используемое в `get_product_id` для обработки случаев, когда идентификатор продукта не найден.