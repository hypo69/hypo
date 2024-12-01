Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код представляет класс `AliCampaignGoogleSheet`, предназначенный для работы с Google Таблицами в контексте управления рекламными кампаниями AliExpress.  Он предоставляет методы для записи данных о кампаниях, категориях и продуктах, а также для форматирования листов Google Таблиц.  Класс наследует функциональность из класса `SpreadSheet`, упрощая работу с Google Sheets.  Ключевая особенность - возможность создавать и заполнять листы с информацией о продуктах, кампаниях и категориях.  Также реализованы методы удаления ненужных листов и форматирования таблиц для улучшения читаемости.

Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек:** Код импортирует нужные библиотеки, такие как `time`, `SimpleNamespace`, типы данных `Optional, Any, List, Dict`,  `gspread` (для работы с Google Таблицами), `SpreadSheet` (внутренний класс для работы с Google Таблицами), `j_dumps`, `pprint` (для вывода данных) и `logger` (для логирования).

2. **Определение класса `AliCampaignGoogleSheet`:** Создается класс, наследующий от `SpreadSheet`. Он содержит атрибуты `spreadsheet_id` (идентификатор Google Таблицы) и `spreadsheet`, `worksheet`.  Это ключевая часть, позволяющая работать с конкретной таблицей.

3. **Инициализация класса `AliCampaignGoogleSheet`:** Метод `__init__` инициализирует класс с параметрами кампании (название, язык, валюта). Он настраивает соединение с Google Таблицами.

4. **Очистка таблицы:** Метод `clear()` удаляет все листы, кроме `categories` и `product_template`.

5. **Удаление листов продуктов:** Метод `delete_products_worksheets()` удаляет все листы, кроме указанных исключений.

6. **Запись данных кампании:** Метод `set_campaign_worksheet()` записывает информацию о кампании (название, заголовок, язык, валюта, описание) в лист `campaign` в Google Таблицах.  Данные записываются вертикально в столбец B, а заголовки в столбец A.

7. **Запись данных о продуктах:** Метод `set_products_worksheet()` записывает информацию о продуктах в лист Google Таблиц, соответствующий имени категории. Данные берутся из объекта `SimpleNamespace`, содержащего информацию о продуктах (идентификатор, цена, ссылка, изображение и т.д.).  Информация записывается в отдельный лист для каждой категории.

8. **Запись данных категорий:** Метод `set_categories_worksheet()` записывает данные о категориях (название, заголовок, описание, теги, количество продуктов) в лист `categories`. Данные записываются в определенных столбцах.

9. **Форматирование листов:** Методы `_format_categories_worksheet()` и `_format_category_products_worksheet()`  настраивают ширину столбцов и высоту строк, а также форматируют заголовки листов для лучшей читаемости. Это включает в себя настройку шрифта и цвета заголовков.

10. **Получение данных категорий:** Метод `get_categories()` считывает все записи из листа `categories` и возвращает их в виде списка словарей.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet
    from types import SimpleNamespace

    # Пример данных для кампании
    campaign_data = SimpleNamespace(
        campaign_name="Campaign Example",
        title="Example Campaign Title",
        language="ru",
        currency="USD",
        description="Description of the campaign"
    )

    # Пример данных для категории
    category_data = SimpleNamespace(name="Category 1", title="Example Category", description="Description", tags=["tag1", "tag2"], products_count=10)

    # Пример данных для продукта
    product_data = SimpleNamespace(product_id=123, product_title="Product Title", app_sale_price=10, original_price=20, sale_price=15, promotion_link="https://example.com")


    # Создание экземпляра класса
    gsheet = AliCampaignGoogleSheet('Example Campaign', language='ru', currency='USD')


    # Запись данных кампании
    gsheet.set_campaign_worksheet(campaign_data)

    # Запись данных категории
    gsheet.set_categories_worksheet(category_data)

    # Запись данных о продуктах
    gsheet.set_products_worksheet("Category 1")  # Укажите имя категории


    # Очистка таблицы
    gsheet.clear()