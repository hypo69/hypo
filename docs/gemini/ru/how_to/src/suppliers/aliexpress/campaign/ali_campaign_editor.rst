Как использовать метод get_category_products
========================================================================================

Описание
-------------------------
Этот метод `get_category_products` читает данные о товарах из JSON-файлов для заданной категории. Он ищет JSON-файлы в подкаталоге, соответствующем категории, языку и валюте текущей кампании, и загружает данные из каждого найденного файла в список объектов `SimpleNamespace`.

Шаги выполнения
-------------------------
1. **Определение пути к категории:** Метод формирует путь к каталогу категории, учитывая `self.base_path`, `category_name`, `self.language`, и `self.currency`.

2. **Поиск JSON-файлов:** Используется функция `get_filenames` для поиска всех файлов с расширением `.json` в указанном каталоге.

3. **Обработка каждого найденного JSON-файла:**
   - Для каждого найденного `.json` файла данные загружаются функцией `j_loads_ns`.
   - Из загруженных данных создаётся объект `SimpleNamespace` с помощью `SimpleNamespace(**vars(product_data))`.
   - Данный объект добавляется в список `products`.

4. **Возврат списка продуктов:** Если файлы найдены и обработаны, метод возвращает список `products` содержащий объекты `SimpleNamespace`.

5. **Обработка отсутствия файлов:** Если JSON-файлов не найдено, выводится сообщение об ошибке с указанием пути, где должны быть файлы. Метод `process_category_products` вызывается для подготовки данных о категории (вероятно, выполнение действий, чтобы эти файлы были созданы или обновлены), после чего метод возвращает `None`.

Пример использования
-------------------------
.. code-block:: python

    from pathlib import Path
    from types import SimpleNamespace
    from hypotez.src.suppliers.aliexpress.campaign import ali_campaign_editor

    # Предположим, что campaign и base_path уже инициализированы
    campaign = ali_campaign_editor.AliCampaignEditor(campaign_name="Summer Sale", language="EN", currency="USD")
    campaign.base_path = Path("./campaign_data")  # Замените на действительный путь

    products = campaign.get_category_products("Electronics")

    if products:
        for product in products:
            print(product.product_id, product.title)  # Пример доступа к полям
    else:
        print("Продукты не найдены или не удалось получить данные.")