Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код представляет класс `AliCampaignGoogleSheet`, предназначенный для работы с Google Таблицами в контексте управления рекламными кампаниями AliExpress.  Он наследует класс `SpreadSheet` и предоставляет методы для:

- Управления рабочими листами (удаление, копирование).
- Записи данных о кампании (название, описание, язык, валюта).
- Записи данных о категориях (имена, заголовки, описания, количество продуктов).
- Записи данных о продуктах (идентификатор, цена, ссылка и т.д.) в отдельные листы для каждой категории.
- Форматирования листов (установка ширины столбцов, высоты строк, стилей ячеек для заголовков).
- Очистки данных на листах.


Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек**:  Код импортирует нужные модули, такие как `time`, `SimpleNamespace`, `Driver`, `SpreadSheet`, `AliCampaignEditor`,  `logger` и другие для работы с Google Таблицами, веб-драйверами и другими функциональными возможностями.

2. **Создание класса `AliCampaignGoogleSheet`**: Создается класс, наследующий от `SpreadSheet`.  Этот класс предоставляет методы для работы с Google Таблицами, связанными с кампаниями AliExpress.

3. **Установка параметров**: Конструктор класса (`__init__`) принимает имя кампании, язык и валюту, необходимую для создания кампании в Google Таблицах.

4. **Очистка листов**: Метод `clear()` удаляет все листы в Google Таблицах, за исключением листов `categories` и `product_template`.  Это позволяет избежать дублирования данных.

5. **Удаление листов**: Метод `delete_products_worksheets()` удаляет все листы, кроме 'categories' и 'product_template',  обеспечивая, что данные сохраняются в ожидаемом формате.

6. **Запись данных кампании**: Метод `set_campaign_worksheet()` записывает данные о кампании в лист 'campaign'. Данные берутся из объекта `campaign` (типа `SimpleNamespace`).

7. **Запись данных категорий**: Метод `set_categories_worksheet()` записывает данные о категориях в лист 'categories'. Данные берутся из объекта `categories` (типа `SimpleNamespace`).

8. **Запись данных продуктов**: Метод `set_products_worksheet()` записывает данные о продуктах в отдельный лист для каждой категории.  Данные берутся из объекта `products` (типа `SimpleNamespace`).

9. **Форматирование листов**: Методы `_format_categories_worksheet()` и `_format_category_products_worksheet()` форматируют листы, устанавливая ширину столбцов и форматируя заголовки для лучшего восприятия данных.

10. **Получение данных**: Метод `get_categories()` возвращает данные из листа 'categories' в формате списка словарей.

11. **Запись данных о продуктах в определенную категорию**: Метод `set_category_products()` записывает данные о продуктах в определенную категорию.


Пример использования
-------------------------
```python
from hypotez.src.suppliers.aliexpress.campaign.gsheets_check_this_code import AliCampaignGoogleSheet
from types import SimpleNamespace

# Пример данных кампании
campaign_data = SimpleNamespace(
    name="Campaign Name Example",
    title="Campaign Title Example",
    language="ru",
    currency="USD",
    description="Campaign Description",
)

# Пример данных категорий
category_data = SimpleNamespace(
    category1=SimpleNamespace(name='Category 1', title='Category Title 1', description='Description', tags=['tag1', 'tag2'], products_count=10, products=[]),
)

# Создание экземпляра класса AliCampaignGoogleSheet
gsheets_campaign = AliCampaignGoogleSheet("My Campaign", language="ru", currency="USD")


# Заполнение данных для кампании
gsheets_campaign.set_campaign_worksheet(campaign_data)

# Заполнение данных для категорий
gsheets_campaign.set_categories_worksheet(category_data.category1)

# Заполнение данных для продуктов (внутри категории)
# (Необходимо заполнить products внутри category_data.category1)

gsheets_campaign.set_products_worksheet("category1")

# Получение данных
categories_data = gsheets_campaign.get_categories()
print(categories_data)
```
```
```
**Примечание:** Пример использования предполагает, что у вас есть  `campaign_data` и `category_data`  объекты с соответствующими атрибутами. В реальном использовании вам нужно будет заполнить эти данные из ваших источников.  Также, важно учесть, что `products` внутри `category_data`  должны быть заполнены списком объектов SimpleNamespace с данными продуктов.