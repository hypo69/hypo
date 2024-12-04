Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код проверяет, содержит ли строка(и) URL префикс "https://". Если входные данные представляют собой идентификатор продукта, то функция строит полный URL с префиксом "https://".  Функция `ensure_https` обрабатывает как одиночные строки, так и списки строк.  Внутренняя функция `ensure_https_single` обрабатывает одну строку, проверяя содержит ли она префикс, и при необходимости добавляя его. Если в строке находится идентификатор продукта, она формирует URL.

Шаги выполнения
-------------------------
1. Функция `ensure_https` принимает на вход строку или список строк (`prod_ids`).
2. Если на вход подан список строк, то для каждой строки вызывается внутренняя функция `ensure_https_single`.
3. Если на вход подана строка, то вызывается внутренняя функция `ensure_https_single`.
4. Внутренняя функция `ensure_https_single` извлекает идентификатор продукта из входной строки с помощью функции `extract_prod_ids`.
5. Если идентификатор продукта извлечен, функция формирует URL вида "https://www.aliexpress.com/item/{id}.html", где {id} - извлеченный идентификатор продукта.
6. Если идентификатор продукта не найден, функция логирует ошибку и возвращает исходную строку без изменений.
7. Функция возвращает модифицированную строку или список строк.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.utils.ensure_https import ensure_https

    # Пример с одиночной строкой (идентификатор продукта)
    url = "example_product_id"
    url_with_https = ensure_https(url)
    print(url_with_https)  # Output: https://www.aliexpress.com/item/example_product_id.html

    # Пример со списком строк
    urls = ["example_product_id1", "https://www.aliexpress.com/item/example_product_id2.html"]
    urls_with_https = ensure_https(urls)
    print(urls_with_https)  # Output: ['https://www.aliexpress.com/item/example_product_id1.html', 'https://www.aliexpress.com/item/example_product_id2.html']

    # Пример, когда на вход подаётся корректный URL
    valid_url = "https://www.example.com/item/example_product_id"
    valid_url_result = ensure_https(valid_url)
    print(valid_url_result)  # Output: https://www.example.com/item/example_product_id