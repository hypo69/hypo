Как использовать метод `get_category_products`
========================================================================================

Описание
-------------------------
Метод `get_category_products` извлекает данные о товарах из JSON-файлов для заданной категории.  Он ищет JSON-файлы в подкаталоге категории, соответствующей языку и валюте текущей кампании.  Если JSON-файлы найдены, метод загружает данные из них, создаёт объекты `SimpleNamespace` для каждого товара и возвращает список этих объектов. Если JSON-файлы не найдены, метод записывает сообщение об ошибке в лог и вызывает вспомогательный метод `process_category_products`, чтобы подготовить данные о товарах.

Шаги выполнения
-------------------------
1. **Определение пути к категории:** Метод формирует путь к каталогу категории, используя `self.base_path`, `category_name`, `self.language`, и `self.currency`.
2. **Поиск JSON-файлов:** Ищет JSON-файлы в сформированном пути к категории.
3. **Обработка найденных файлов:** Для каждого найденного JSON-файла:
    a. Загружает данные из файла с помощью `j_loads_ns`.
    b. Создаёт объект `SimpleNamespace` на основе загруженных данных.
    c. Добавляет созданный объект `SimpleNamespace` в список `products`.
4. **Возврат результата:** Если в каталоге были найдены JSON-файлы, возвращает список `products`.
5. **Обработка отсутствия файлов:** Если JSON-файлы не найдены:
    a. Записывает сообщение об ошибке в лог.
    b. Вызывает метод `process_category_products` для текущей категории, чтобы подготовить данные о товарах.
    c. Возвращает `None`.


Пример использования
-------------------------
.. code-block:: python

    from pathlib import Path
    from hypotez.src.suppliers.aliexpress.campaign.ali_campaign_editor import AliCampaignEditor
    from typing import List

    # Предполагается, что у вас есть экземпляр AliCampaignEditor с нужными настройками
    campaign = AliCampaignEditor(campaign_name="Summer Sale", language="EN", currency="USD")
    campaign.base_path = Path("./campaigns/Summer Sale")  # Замените на реальный путь
    
    products = campaign.get_category_products("Electronics")

    if products:
        for product in products:
            print(product.product_id, product.title)
    else:
        print("Данные о товарах не найдены.")