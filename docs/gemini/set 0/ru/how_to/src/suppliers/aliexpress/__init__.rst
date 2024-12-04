Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код импортирует классы и модули из пакета `aliexpress`, предназначенные для работы с AliExpress. Он определяет константу `MODE`, которая вероятно используется для выбора режима работы (например, 'dev' для разработки, 'prod' для производства).  Импортируются классы для работы с API, запросами, кампаниями и генерацией HTML.

Шаги выполнения
-------------------------
1. Определяется константа `MODE` со значением 'dev'.
2. Импортируются классы `Aliexpress`, `AliApi`, `AliRequests`, `AliCampaignEditor` из соответствующих подмодулей.
3. Импортируются классы `ProductHTMLGenerator`, `CategoryHTMLGenerator` и `CampaignHTMLGenerator` для генерации HTML-представлений продуктов, категорий и кампаний соответственно.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress import Aliexpress, AliApi, AliCampaignEditor

    # Пример использования (неполный):
    # Инициализация объекта Aliexpress
    aliexpress_instance = Aliexpress()

    # Получение данных с API
    api_instance = AliApi()

    # Изменение кампании
    campaign_editor = AliCampaignEditor()
    campaign_editor.update_campaign(campaign_id=123, new_title="Новое название")