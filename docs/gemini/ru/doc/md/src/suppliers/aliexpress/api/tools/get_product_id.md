# Модуль `hypotez/src/suppliers/aliexpress/api/tools/get_product_id.py`

## Обзор

Модуль `get_product_id` предоставляет функцию для извлечения идентификатора продукта из входного текста.  Функция использует вспомогательную функцию `extract_prod_ids` для поиска и возвращения идентификатора продукта. Если идентификатор не найден, генерируется исключение `ProductIdNotFoundException`.

## Оглавление

* [Функции](#функции)


## Функции

### `get_product_id`

**Описание**: Извлекает идентификатор продукта из входного текста.

**Параметры**:
- `raw_product_id` (str): Исходный текст, содержащий идентификатор продукта.

**Возвращает**:
- `str`: Идентификатор продукта, если найден.

**Вызывает исключения**:
- `ProductIdNotFoundException`: Если идентификатор продукта не найден в входном тексте.


```python
def get_product_id(raw_product_id: str) -> str:
    """Returns the product ID from a given text. Raises ProductIdNotFoundException on fail."""
    return extract_prod_ids(raw_product_id)
    # if re.search(r'^[0-9]*$', text):
    #     return text
    #
    # # Extract product ID from URL
    # asin = re.search(r'(/)([0-9]*)(.)', text)
    # if asin:
    #     return asin.group(2)
    # else:
    #     raise ProductIdNotFoundException('Product id not found: ' + text)
```

**Примечание:** Текущая реализация использует функцию `extract_prod_ids`.  В коде присутствуют комментарии, которые демонстрируют прежнюю логику.  Рекомендуется пересмотреть и убрать старую, неэффективную реализацию, если функция `extract_prod_ids` надежно решает задачу.