Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `AffiliateLink`, представляющий данные об аффилиатной ссылке.  Класс содержит два атрибута: `promotion_link` (строка, представляющая промо-ссылку) и `source_value` (строка, содержащая исходные данные).

Шаги выполнения
-------------------------
1. Определяется класс `AffiliateLink`.
2. В классе определяются два атрибута:
    - `promotion_link`:  будет хранить строковое значение промо-ссылки.
    - `source_value`: будет хранить строковое значение исходных данных.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.models.affiliate_link import AffiliateLink

    # Создание экземпляра класса AffiliateLink
    affiliate_link = AffiliateLink()

    # Установка значений атрибутов
    affiliate_link.promotion_link = "https://example.com/promotion"
    affiliate_link.source_value = "aliexpress_product_123"


    # Вывод значений атрибутов
    print(affiliate_link.promotion_link)  # Выведет: https://example.com/promotion
    print(affiliate_link.source_value)  # Выведет: aliexpress_product_123