Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `AffiliateLink`, который представляет собой модель для ссылки на партнерскую программу AliExpress.  Модель имеет два атрибута: `promotion_link` (ссылка на промоакцию) и `source_value` (значение источника).

Шаги выполнения
-------------------------
1. Создается класс `AffiliateLink`.
2. Определяются два атрибута класса:
    - `promotion_link`:  хранит строку, представляющую собой ссылку на партнерскую программу.
    - `source_value`: хранит строку, содержащую значение источника.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.models.affiliate_link import AffiliateLink

    # Создание объекта AffiliateLink
    affiliate_link = AffiliateLink()

    # Присвоение значений атрибутам
    affiliate_link.promotion_link = "https://www.aliexpress.com/somepromotionlink"
    affiliate_link.source_value = "SomeSourceValue"

    # Вывод значений атрибутов (или использование в дальнейшем в коде)
    print(affiliate_link.promotion_link)
    print(affiliate_link.source_value)