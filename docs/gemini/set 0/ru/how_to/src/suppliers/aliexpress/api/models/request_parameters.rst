Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет три класса: `ProductType`, `SortBy`, и `LinkType`.  Эти классы содержат константы, представляющие типы данных для параметров запроса к API AliExpress.

Шаги выполнения
-------------------------
1. **`ProductType`:** Определяет возможные типы продуктов, которые можно запросить: `ALL`, `PLAZA`, `TMALL`.
2. **`SortBy`:** Определяет возможные параметры сортировки результатов: `SALE_PRICE_ASC` (по возрастанию цены), `SALE_PRICE_DESC` (по убыванию цены), `LAST_VOLUME_ASC` (по возрастанию объёма продаж), `LAST_VOLUME_DESC` (по убыванию объёма продаж).
3. **`LinkType`:** Определяет типы ссылок: `NORMAL` (обычная ссылка) и `HOTLINK` (горячая ссылка).

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.models.request_parameters import ProductType, SortBy, LinkType

    # Выбор типа продукта
    product_type = ProductType.PLAZA

    # Выбор параметра сортировки
    sort_by = SortBy.SALE_PRICE_DESC

    # Выбор типа ссылки
    link_type = LinkType.NORMAL

    # Пример использования в запросе (предполагается, что есть функция для создания запроса)
    request_data = create_aliexpress_request(product_type=product_type, sort_by=sort_by, link_type=link_type)

    # Примерная функция для создания запроса (заглушка)
    def create_aliexpress_request(product_type, sort_by, link_type):
        return {
            'product_type': product_type,
            'sort_by': sort_by,
            'link_type': link_type
        }

    print(request_data)