# Модуль `hypotez/src/suppliers/aliexpress/utils/ensure_https.py`

## Обзор

Модуль `ensure_https` предназначен для обеспечения того, что предоставленная строка(и) URL содержит префикс `https://`. Если на вход подается идентификатор продукта, модуль создает полный URL с префиксом `https://`.

## Функции

### `ensure_https`

**Описание**: Функция проверяет, содержит ли входная строка (или список строк) URL префикс `https://`. Если нет, добавляет его.  Если на вход подается идентификатор продукта, строка преобразуется в URL.

**Параметры**:

- `prod_ids` (str | list[str]): Строка URL или список строк URL, которые необходимо проверить и изменить при необходимости.

**Возвращает**:

- str | list[str]: Строка URL или список строк URL с префиксом `https://`.

**Возможные исключения**:

- `ValueError`: Если `prod_ids` является экземпляром `WindowsPath`.


### `ensure_https_single`

**Описание**: Функция проверяет, содержит ли одна строка URL префикс `https://`. Если нет, добавляет его.  Если на вход подается идентификатор продукта, строка преобразуется в URL.

**Параметры**:

- `prod_id` (str): Строка URL или идентификатора продукта.

**Возвращает**:

- str: Строка URL с префиксом `https://`.

**Возможные исключения**:

- `ValueError`: Если `prod_id` является экземпляром `WindowsPath`.


## Примеры использования

```python
# Пример 1: с одиночной строкой
url = "example_product_id"
url_with_https = ensure_https(url)
print(url_with_https)  # Вывод: https://www.aliexpress.com/item/example_product_id.html

# Пример 2: со списком строк
urls = ["example_product_id1", "https://www.aliexpress.com/item/example_product_id2.html"]
urls_with_https = ensure_https(urls)
print(urls_with_https)  # Вывод: ['https://www.aliexpress.com/item/example_product_id1.html', 'https://www.aliexpress.com/item/example_product_id2.html']

# Пример 3: уже существующий https
url = "https://www.example.com/item/example_product_id"
url_with_https = ensure_https(url)
print(url_with_https)  # Вывод: https://www.example.com/item/example_product_id
```

##  Зависимости

- `src.logger.logger`:  Модуль для логирования.
- `src.suppliers.aliexpress.utils.extract_product_id`: Функция для извлечения идентификаторов продуктов.


```