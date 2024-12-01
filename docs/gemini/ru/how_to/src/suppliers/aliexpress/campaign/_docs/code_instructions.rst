Как использовать этот блок кода для создания и редактирования рекламных кампаний
================================================================================
Описание
-------------------------
Этот блок кода предоставляет инструкции для программистов по созданию и редактированию рекламных кампаний на AliExpress. Он описывает шаги инициализации кампании, сбора данных, создания рекламных материалов, сохранения конфигурации и последующего редактирования.  Включает также примеры использования Python-кода и рекомендации по обработке ошибок и логированию.

Шаги выполнения
-------------------------
1. **Создание кампании:**
   - Определите имя кампании, язык и валюту.
   - Создайте директории для кампании и категорий продуктов.
   - Сохраните конфигурацию кампании в файле.
   - Соберите данные о продуктах (URL или ID).
   - Сохраните собранные данные о продуктах.
   - Создайте рекламные материалы на основе собранных данных.
   - Просмотрите и опубликуйте кампанию.

2. **Редактирование кампании:**
   - Загрузите конфигурацию существующей кампании.
   - Обновите параметры кампании (язык, валюта).
   - Обновите список категорий и соответствующие директории.
   - Соберите новые данные о продуктах.
   - Сохраните обновленные данные о продуктах.
   - Обновите рекламные материалы на основе новых данных.
   - Просмотрите и опубликуйте обновленную кампанию.

3. **Обработка ошибок и логирование:**
   - Используйте `try-except` блоки для обработки возможных ошибок во время выполнения кода.
   - Логируйте важные события и ошибки, чтобы отслеживать и исправлять проблемы.

Пример использования
-------------------------
.. code-block:: python

    import logging

    # ... (определение функций create_directories, save_config, collect_product_data, etc.) ...

    def create_campaign(campaign_name, language, currency, categories, product_urls):
        try:
            create_directories(campaign_name, categories)
            campaign_config = {'name': campaign_name, 'language': language, 'currency': currency}
            save_config(campaign_name, campaign_config)
            product_data = collect_product_data(product_urls)
            save_product_data(campaign_name, product_data)
            create_promotional_materials(campaign_name, product_data)
            review_campaign(campaign_name)
            publish_campaign(campaign_name)
            logging.info(f"Кампания '{campaign_name}' успешно создана.")
        except Exception as ex:
            logging.error(f"Ошибка при создании кампании '{campaign_name}': {ex}")

    # Пример использования функции create_campaign
    campaign_name = 'my_campaign'
    language = 'EN'
    currency = 'USD'
    categories = ['electronics', 'fashion']
    product_urls = ['https://example.com/item1', 'https://example.com/item2']

    # Инициализируем логгер
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    create_campaign(campaign_name, language, currency, categories, product_urls)

    # ... (код для редактирования кампании) ...