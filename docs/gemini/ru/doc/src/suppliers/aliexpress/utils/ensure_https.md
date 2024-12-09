# Модуль `ensure_https`

## Обзор

Модуль `ensure_https` предназначен для обеспечения того, что предоставленная строка(и) URL содержит префикс `https://`. Если на вход подается идентификатор продукта, модуль создает полный URL с префиксом `https://`.

## Функции

### `ensure_https`

**Описание**: Функция проверяет, содержит ли входная строка(или список строк) URL префикс `https://`. Если нет, добавляет его. Если на вход подается идентификатор продукта, функция строит полный URL с префиксом `https://`.

**Параметры**:
- `prod_ids` (str | list[str]): Строка URL или список строк URL, которые необходимо проверить и изменить при необходимости.


**Возвращает**:
- str | list[str]: Строка URL или список строк URL с префиксом `https://`.


**Вызывает исключения**:
- `ValueError`: Если `prod_ids` является экземпляром `WindowsPath`.

### `ensure_https_single`

**Описание**: Функция проверяет, содержит ли входная строка URL префикс `https://`. Если нет, добавляет его. Если на вход подается идентификатор продукта, функция строит полный URL с префиксом `https://`.

**Параметры**:
- `prod_id` (str): Строка URL или идентификатор продукта.


**Возвращает**:
- str: Строка URL с префиксом `https://`.


**Вызывает исключения**:
- `ValueError`: Если `prod_id` является экземпляром `WindowsPath`.


## Примеры использования

```python
# Пример использования для одиночной строки
url = "example_product_id"
url_with_https = ensure_https(url)
print(url_with_https)  # Вывод: https://www.aliexpress.com/item/example_product_id.html

# Пример использования для списка строк
urls = ["example_product_id1", "https://www.aliexpress.com/item/example_product_id2.html"]
urls_with_https = ensure_https(urls)
print(urls_with_https)  # Вывод: ['https://www.aliexpress.com/item/example_product_id1.html', 'https://www.aliexpress.com/item/example_product_id2.html']

# Пример использования для уже существующего https URL
url_https = "https://www.example.com/item/example_product_id"
url_with_https = ensure_https(url_https)
print(url_with_https)  # Вывод: https://www.example.com/item/example_product_id
```

## Зависимости

- Модуль `src.logger`
- Модуль `src.suppliers.aliexpress.utils.extract_product_id`

```
```