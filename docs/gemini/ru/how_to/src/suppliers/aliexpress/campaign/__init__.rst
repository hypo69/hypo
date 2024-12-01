Как использовать модуль src.suppliers.aliexpress.campaign
========================================================================================

Описание
-------------------------
Модуль `src.suppliers.aliexpress.campaign` предоставляет инструменты для управления рекламными кампаниями на Aliexpress. Он содержит классы и функции для работы с редактированием, обработкой и генерацией данных кампаний. В модуле определены константы, импортированы классы и функции из других модулей этого пакета, которые отвечают за конкретные задачи.

Шаги выполнения
-------------------------
1. Импортируйте необходимые классы и функции:
   - `AliCampaignEditor`: класс для редактирования кампаний.
   - `process_campaign`, `process_campaign_category`, `process_all_campaigns`: функции для обработки кампаний.
   - `CategoryHTMLGenerator`, `ProductHTMLGenerator`: классы для генерации HTML-представлений категорий и продуктов.


2. Используйте функции `process_campaign`, `process_campaign_category`, или `process_all_campaigns` для обработки данных кампаний.
   - `process_campaign(campaign_data)` обрабатывает данные одной кампании.
   - `process_campaign_category(category_data)` обрабатывает данные категории кампании.
   - `process_all_campaigns(campaign_data_list)` обрабатывает список данных всех кампаний.


3. Используйте класс `AliCampaignEditor` для редактирования данных кампаний.

4. Используйте классы `CategoryHTMLGenerator` и `ProductHTMLGenerator` для генерации HTML-отчётов о категориях и продуктах кампаний.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.campaign import AliCampaignEditor, process_campaign, process_all_campaigns

    # Пример данных кампании
    campaign_data = {
        "campaign_id": 123,
        "name": "Summer Sale",
        "budget": 1000,
        # ... другие данные кампании
    }


    # Обработка одной кампании
    campaign_result = process_campaign(campaign_data)
    print(campaign_result)



    # Пример обработки всех кампаний
    all_campaign_data = [campaign_data, { ... }, { ... }]  # Список данных всех кампаний
    results = process_all_campaigns(all_campaign_data)
    print(results)



    # Пример использования AliCampaignEditor
    editor = AliCampaignEditor(campaign_data)
    editor.update_budget(2000)
    updated_campaign = editor.get_updated_campaign()
    print(updated_campaign)