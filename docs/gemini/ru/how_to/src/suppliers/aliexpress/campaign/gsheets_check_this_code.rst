Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код представляет класс `AliCampaignGoogleSheet`, предназначенный для работы с Google Таблицами в контексте управления рекламными кампаниями AliExpress. Он наследует класс `SpreadSheet` и предоставляет методы для:

- Управления листами Google Таблиц (создание, удаление).
- Записи данных о кампаниях, категориях и продуктах.
- Форматирования листов (установка ширины столбцов, высоты строк, форматирование заголовков).
- Очистки данных на листах.


Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек:** Код импортирует нужные модули, включая `time`, `SimpleNamespace`, `Driver`, `Chrome`, `Worksheet`, `SpreadSheet`, `AliCampaignEditor`, `j_dumps`, `pprint`, `logger`, и другие библиотеки для работы с Google Таблицами и веб-драйвером.

2. **Инициализация класса `AliCampaignGoogleSheet`:**
    - Создание экземпляра класса `AliCampaignGoogleSheet` с параметрами кампании (название, язык, валюта).
    - Инициализация родительского класса `SpreadSheet` с ID Google Таблицы.
    - Создание экземпляра `AliCampaignEditor` для работы с данными кампании.
    - Очистка листов таблицы (`self.clear()`).
    - Установка листов для кампании и категорий (`self.set_campaign_worksheet`, `self.set_categories_worksheet`).
    - Откройте Google таблицу в браузере, используя драйвер веб-драйвера (`self.driver.get_url(...)`).

3. **Очистка листов (`self.clear()`):** Удаляет все листы в Google Таблицах, кроме `'categories'` и `'product_template'`.

4. **Установка данных кампании на лист `'campaign'` (`self.set_campaign_worksheet`):**
    - Получает лист `'campaign'`.
    - Записывает данные кампании (имя, заголовок, язык, валюта, описание) в вертикальном формате в ячейки.

5. **Установка данных категорий на лист `'categories'` (`self.set_categories_worksheet`):**
    - Очищает лист `'categories'`.
    - Получает данные категорий из объекта `SimpleNamespace`.
    - Записывает данные категорий (имя, заголовок, описание, теги, количество продуктов) в ячейки.
    - Форматирует лист категорий (`self._format_categories_worksheet`).

6. **Установка данных продуктов на лист `<category_name>` (`self.set_products_worksheet`):**
    -  Если категория указана (`category_name`), получает список продуктов из этой категории.
    - Копирует шаблон листа `'product'` в новый лист с именем, соответствующим имени категории.
    - Записывает данные продуктов из объекта `SimpleNamespace` в ячейки.
    - Форматирует лист продуктов (`self._format_category_products_worksheet`).


7. **Форматирование листов (`_format_categories_worksheet`, `_format_category_products_worksheet`):** Настраивает ширину столбцов и высоту строк, а также форматирует заголовки для лучшей читаемости.

8. **Получение данных категорий (`self.get_categories`):** Возвращает данные категорий из таблицы в виде списка словарей.

9. **Запись данных о продуктах в новую таблицу (`self.set_category_products`):** Записывает данные продуктов в новую таблицу, используя уже имеющиеся заголовки.



Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.campaign.gsheets_check_this_code import AliCampaignGoogleSheet
    from types import SimpleNamespace

    # Пример данных кампании
    campaign_data = SimpleNamespace(
        name="Campaign Name",
        title="Campaign Title",
        language="ru",
        currency="USD",
        description="Campaign description"
    )
    
    # Инициализируем класс
    gsheets = AliCampaignGoogleSheet(campaign_name="MyCampaign")

    # Записываем данные кампании
    gsheets.set_campaign_worksheet(campaign_data)

    # ... (заполнение данных о категориях и продуктах аналогично)