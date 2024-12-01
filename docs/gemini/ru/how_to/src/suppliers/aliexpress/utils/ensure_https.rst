Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код проверяет, содержит ли строка(и) URL префикс `https://`. Если в строке присутствует только идентификатор продукта, то код создаёт полную URL-строку, добавляя префикс `https://`.  Функция `ensure_https` обрабатывает как одиночные URL-строки, так и списки таких строк.  Она вызывает вспомогательную функцию `ensure_https_single` для обработки каждой строки индивидуально. Функция `extract_prod_ids` (вероятно, из другого модуля) используется для извлечения идентификатора продукта из URL. В случае ошибки, например, если не удаётся извлечь идентификатор, логгируется сообщение об ошибке.

Шаги выполнения
-------------------------
1. Функция `ensure_https` принимает на вход строку или список строк (`prod_ids`).
2. Если вход – список, функция применяет `ensure_https_single` к каждой строке в списке и возвращает новый список обработанных строк.
3. Если вход – строка, функция вызывает `ensure_https_single` для обработки этой строки.
4. Функция `ensure_https_single` извлекает идентификатор продукта (`_prod_id`) из входной строки.
5. Если идентификатор продукта найден, функция строит полную URL-строку вида `https://www.aliexpress.com/item/{_prod_id}.html` и возвращает её.
6. В противном случае, если идентификатор продукта не найден, функция регистрирует ошибку с помощью `logger.error` и возвращает исходную строку без изменений.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.utils.ensure_https import ensure_https

    # Пример с одной строкой:
    url = "example_product_id"
    url_with_https = ensure_https(url)
    print(url_with_https)  # Output: https://www.aliexpress.com/item/example_product_id.html


    # Пример со списком строк:
    urls = ["example_product_id1", "https://www.aliexpress.com/item/example_product_id2.html"]
    urls_with_https = ensure_https(urls)
    print(urls_with_https)  # Output: ['https://www.aliexpress.com/item/example_product_id1.html', 'https://www.aliexpress.com/item/example_product_id2.html']


    # Пример с уже существующим https:
    url_with_https = "https://www.example.com/item/example_product_id"
    url_with_https = ensure_https(url_with_https)
    print(url_with_https)  # Output: https://www.example.com/item/example_product_id