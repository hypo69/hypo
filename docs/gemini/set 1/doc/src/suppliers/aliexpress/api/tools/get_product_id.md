# Модуль `hypotez/src/suppliers/aliexpress/api/tools/get_product_id.py`

## Обзор

Модуль `get_product_id` предоставляет функцию для извлечения идентификатора продукта из входного текста.

## Функции

### `get_product_id`

**Описание**: Возвращает идентификатор продукта, извлечённый из заданного текста.  Если идентификатор не найден, выбрасывает исключение `ProductIdNotFoundException`.

**Параметры**:

- `raw_product_id` (str): Строка, содержащая потенциальный идентификатор продукта.

**Возвращает**:

- str: Идентификатор продукта в виде строки. Возвращает результат из функции `extract_prod_ids`.


**Вызывает исключения**:

- `ProductIdNotFoundException`: Если идентификатор продукта не найден в предоставленном тексте.  (Исключение обрабатывается в функции `extract_prod_ids`).


## Модули

### `src.suppliers.aliexpress.utils.extract_product_id`

**Описание**: Модуль содержит функцию `extract_prod_ids`, которая, по всей видимости, отвечает за извлечение идентификатора продукта.  Полная функциональность и реализация этого модуля не показаны в представленном фрагменте кода.