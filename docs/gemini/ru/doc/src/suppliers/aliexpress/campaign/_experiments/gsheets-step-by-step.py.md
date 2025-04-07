# Модуль для экспериментов с Google Sheets в кампаниях AliExpress

## Обзор

Модуль предназначен для экспериментов по интеграции Google Sheets в процесс управления кампаниями на AliExpress. Он позволяет считывать и записывать данные о кампаниях, категориях и продуктах, используя Google Sheets в качестве источника данных и инструмента для редактирования.

## Подорбней

Этот модуль является экспериментальной частью проекта `hypotez` и предназначен для автоматизации работы с кампаниями AliExpress через Google Sheets. Он включает в себя функциональность для:

- Чтения и записи данных категорий кампании в Google Sheets.
- Редактирования категорий кампании непосредственно в Google Sheets.
- Обновления данных кампании на основе изменений, внесенных в Google Sheets.

Использование Google Sheets позволяет упростить процесс редактирования и управления данными кампании, делая его более наглядным и доступным для нетехнических специалистов.

## Функции

### `None`

```python
gs = AliCampaignGoogleSheet(\'1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0\')
...
campaign_name = "lighting"
language = \'EN\'
currency = \'USD\'

campaign_editor = AliCampaignEditor(campaign_name, language, currency)
campaign_data = campaign_editor.campaign
_categories: SimpleNamespace = campaign_data.category

# Преобразование _categories в словарь
categories_dict: dict[str, CategoryType] = {category_name: getattr(_categories, category_name) for category_name in vars(_categories)}

# Преобразование категорий в список для Google Sheets
categories_list: list[CategoryType] = list(categories_dict.values())

# Установка категорий в Google Sheet
gs.set_categories(categories_list)

# Получение отредактированных категорий из Google Sheet
edited_categories: list[dict] = gs.get_categories()

# Обновление словаря categories_dict с отредактированными данными
for _cat in edited_categories:
    _cat_ns: SimpleNamespace = SimpleNamespace(**{
        \'name\':_cat[\'name\'],
        \'title\':_cat[\'title\'],
        \'description\':_cat[\'description\'],
        \'tags\':_cat[\'tags\'],
        \'products_count\':_cat[\'products_count\']
    }
    )
    # Логирование для отладки
    logger.info(f"Updating category: {_cat_ns.name}")
    categories_dict[_cat_ns.name] = _cat_ns
    products = campaign_editor.get_category_products(_cat_ns.name)
    gs.set_category_products(_cat_ns.name,products)

# Преобразование categories_dict обратно в SimpleNamespace вручную
_updated_categories = SimpleNamespace(**categories_dict)

# Вывод данных для отладки
pprint(_updated_categories)

# Создание словаря для кампании
campaign_dict: dict = {
    \'name\': campaign_data.campaign_name,
    \'title\': campaign_data.title,
    \'language\': language,
    \'currency\': currency,
    \'category\': _updated_categories
}

edited_campaign: SimpleNamespace = SimpleNamespace(**campaign_dict)



# Пример использования pprint для вывода данных
pprint(edited_campaign)
campaign_editor.update_campaign(edited_campaign)
...
```

**Как работает функция**:

1.  **Инициализация**:
    *   Создается экземпляр класса `AliCampaignGoogleSheet` с указанием идентификатора Google Sheet.
    *   Определяются основные параметры кампании: `campaign_name`, `language` и `currency`.
    *   Создается экземпляр класса `AliCampaignEditor` для управления данными кампании.

2.  **Преобразование категорий в словарь**:
    *   Извлекаются категории из данных кампании (`campaign_data.category`).
    *   Преобразуются категории из объекта `SimpleNamespace` в словарь `categories_dict`, где ключами являются имена категорий, а значениями - объекты `CategoryType`.

3.  **Подготовка данных для Google Sheets**:
    *   Значения категорий (объекты `CategoryType`) преобразуются в список `categories_list` для последующей записи в Google Sheets.

4.  **Запись категорий в Google Sheets**:
    *   Метод `gs.set_categories(categories_list)` записывает список категорий в Google Sheets.

5.  **Чтение отредактированных категорий из Google Sheets**:
    *   Метод `gs.get_categories()` считывает отредактированные данные категорий из Google Sheets в виде списка словарей `edited_categories`.

6.  **Обновление данных категорий**:
    *   Итерируясь по списку `edited_categories`, каждый словарь преобразуется в объект `SimpleNamespace` (`_cat_ns`).
    *   Логируется информация об обновляемой категории с использованием `logger.info`.
    *   Обновляются данные в словаре `categories_dict` с использованием данных из `_cat_ns`.
    *   Извлекаются продукты для каждой категории с использованием `campaign_editor.get_category_products(_cat_ns.name)`.
    *   Данные о продуктах записываются в Google Sheets с использованием `gs.set_category_products(_cat_ns.name, products)`.

7.  **Преобразование категорий обратно в SimpleNamespace**:
    *   Словарь `categories_dict` преобразуется обратно в объект `SimpleNamespace` `_updated_categories`.

8.  **Создание словаря кампании**:
    *   Создается словарь `campaign_dict`, содержащий основные данные кампании, включая обновленные категории.

9.  **Обновление данных кампании**:
    *   Словарь `campaign_dict` преобразуется в объект `SimpleNamespace` `edited_campaign`.
    *   Данные кампании обновляются с использованием метода `campaign_editor.update_campaign(edited_campaign)`.

10. **Отладка**:
    *   Используется `pprint` для вывода данных `_updated_categories` и `edited_campaign` в целях отладки.

```
Инициализация GS и CampaignEditor --> Преобразование категорий в словарь --> Подготовка списка категорий --> Запись категорий в GS --> Чтение категорий из GS --> 
Обновление данных категорий: Итерация по категориям -> Преобразование в SimpleNamespace -> Логирование -> Обновление словаря -> Получение продуктов -> Запись продуктов в GS -->
Преобразование категорий обратно в SimpleNamespace --> Создание словаря кампании --> Обновление данных кампании --> Отладка: Вывод данных
```

**Примеры**:

```python
# Пример инициализации и базовой настройки
gs = AliCampaignGoogleSheet('1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0')
campaign_name = "lighting"
language = 'EN'
currency = 'USD'
campaign_editor = AliCampaignEditor(campaign_name, language, currency)

# Пример получения и вывода обновленных категорий
edited_categories: list[dict] = gs.get_categories()
pprint(edited_categories)

# Пример обновления кампании
campaign_dict: dict = {
    'name': campaign_editor.campaign.campaign_name,
    'title': campaign_editor.campaign.title,
    'language': language,
    'currency': currency,
    'category': campaign_editor.campaign.category
}
edited_campaign: SimpleNamespace = SimpleNamespace(**campaign_dict)
campaign_editor.update_campaign(edited_campaign)