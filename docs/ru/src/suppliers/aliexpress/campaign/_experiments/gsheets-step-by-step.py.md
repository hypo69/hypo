# Документация для модуля `src.suppliers.aliexpress.campaign._experiments.gsheets-step-by-step`

## Обзор

Модуль `gsheets-step-by-step.py` представляет собой эксперимент по интеграции Google Sheets с процессом управления рекламными кампаниями на AliExpress. Он предназначен для упрощения и автоматизации работы с данными кампаний, такими как категории и продукты, путем использования Google Sheets в качестве интерфейса для редактирования и обновления информации.

## Подробней

Этот модуль предоставляет функциональность для работы с Google Sheets, позволяя получать и обновлять данные рекламных кампаний AliExpress. Он использует классы `AliCampaignGoogleSheet` и `AliCampaignEditor` для взаимодействия с Google Sheets и управления данными кампаний соответственно. Модуль позволяет устанавливать категории в Google Sheet, получать отредактированные категории и обновлять информацию о продуктах для каждой категории. Он также включает функциональность для преобразования данных между различными форматами, такими как `SimpleNamespace`, словари и списки, чтобы обеспечить совместимость с различными компонентами системы.

## Функции

### `__init__` (из класса `AliCampaignGoogleSheet`)

```python
    def __init__(self, spreadsheet_id: str) -> None:
        """Инициализирует экземпляр класса AliCampaignGoogleSheet.

        Args:
            spreadsheet_id (str): Идентификатор Google Spreadsheet.

        """
        ...
```

**Назначение**: Инициализирует экземпляр класса `AliCampaignGoogleSheet`, устанавливая соединение с указанной Google Spreadsheet.

**Параметры**:
- `spreadsheet_id` (str): Идентификатор Google Spreadsheet, который будет использоваться для чтения и записи данных кампании.

**Как работает функция**:
1. Сохраняет идентификатор Google Spreadsheet для последующего использования.
2. Подготавливает экземпляр класса для работы с Google Sheets.

### `set_categories` (из класса `AliCampaignGoogleSheet`)

```python
    def set_categories(self, categories: list) -> None:
        """Устанавливает категории в Google Sheet.

        Args:
            categories (list): Список категорий для установки.

        """
        ...
```

**Назначение**: Записывает список категорий в Google Sheet.

**Параметры**:
- `categories` (list): Список объектов `CategoryType`, содержащих информацию о категориях.

**Как работает функция**:
1. Получает список категорий для записи.
2. Преобразует данные категорий в формат, подходящий для записи в Google Sheet.
3. Записывает данные в указанный Google Sheet.

### `get_categories` (из класса `AliCampaignGoogleSheet`)

```python
    def get_categories(self) -> list[dict]:
        """Получает отредактированные категории из Google Sheet.

        Returns:
            list[dict]: Список словарей с отредактированными данными категорий.

        """
        ...
```

**Назначение**: Получает список отредактированных категорий из Google Sheet.

**Возвращает**:
- `list[dict]`: Список словарей, где каждый словарь содержит информацию об отредактированной категории.

**Как работает функция**:
1. Читает данные из Google Sheet.
2. Преобразует данные в список словарей, где каждый словарь представляет категорию.
3. Возвращает список отредактированных категорий.

### `set_category_products` (из класса `AliCampaignGoogleSheet`)

```python
    def set_category_products(self, category_name: str, products: list) -> None:
        """Устанавливает продукты для указанной категории в Google Sheet.

        Args:
            category_name (str): Название категории.
            products (list): Список продуктов для установки.

        """
        ...
```

**Назначение**: Записывает список продуктов для указанной категории в Google Sheet.

**Параметры**:
- `category_name` (str): Название категории, для которой необходимо установить продукты.
- `products` (list): Список объектов, содержащих информацию о продуктах.

**Как работает функция**:
1. Получает название категории и список продуктов для записи.
2. Преобразует данные продуктов в формат, подходящий для записи в Google Sheet.
3. Записывает данные в указанный Google Sheet для соответствующей категории.

### `__init__` (из класса `AliCampaignEditor`)

```python
    def __init__(self, campaign_name: str, language: str, currency: str) -> None:
        """Инициализирует экземпляр класса AliCampaignEditor.

        Args:
            campaign_name (str): Имя кампании.
            language (str): Язык кампании.
            currency (str): Валюта кампании.

        """
        ...
```

**Назначение**: Инициализирует экземпляр класса `AliCampaignEditor` с указанными параметрами кампании.

**Параметры**:
- `campaign_name` (str): Имя кампании.
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.

**Как работает функция**:
1. Сохраняет параметры кампании (имя, язык, валюту) для последующего использования.
2. Инициализирует и подготавливает экземпляр класса для редактирования данных кампании.

### `get_category_products` (из класса `AliCampaignEditor`)

```python
    def get_category_products(self, category_name: str) -> list:
        """Получает список продуктов для указанной категории.

        Args:
            category_name (str): Название категории.

        Returns:
            list: Список продуктов для указанной категории.

        """
        ...
```

**Назначение**: Получает список продуктов для указанной категории.

**Параметры**:
- `category_name` (str): Название категории, для которой требуется получить список продуктов.

**Возвращает**:
- `list`: Список продуктов, связанных с указанной категорией.

**Как работает функция**:
1. Получает название категории.
2. Извлекает список продуктов, связанных с указанной категорией, из данных кампании.
3. Возвращает список продуктов.

### `update_campaign` (из класса `AliCampaignEditor`)

```python
    def update_campaign(self, campaign: SimpleNamespace) -> None:
        """Обновляет данные кампании.

        Args:
            campaign (SimpleNamespace): Объект SimpleNamespace с обновленными данными кампании.

        """
        ...
```

**Назначение**: Обновляет данные текущей кампании.

**Параметры**:
- `campaign` (SimpleNamespace): Объект `SimpleNamespace`, содержащий обновленные данные кампании.

**Как работает функция**:
1. Получает объект `SimpleNamespace` с обновленными данными кампании.
2. Обновляет текущие данные кампании на основе предоставленных данных.

## Переменные

- `gs`: Инстанс класса `AliCampaignGoogleSheet`, используемый для взаимодействия с Google Sheets. Инициализируется с идентификатором таблицы `'1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0'`.
- `campaign_name`: Имя кампании, установлено как `"lighting"`.
- `language`: Язык кампании, установлен как `'EN'`.
- `currency`: Валюта кампании, установлена как `'USD'`.
- `campaign_editor`: Инстанс класса `AliCampaignEditor`, используемый для редактирования данных кампании. Инициализируется с именем кампании, языком и валютой.
- `campaign_data`: Данные кампании, полученные из `campaign_editor.campaign`.
- `_categories`: Категории кампании, полученные из `campaign_data.category`.
- `categories_dict`: Словарь, содержащий категории кампании, преобразованные из `_categories`.
- `categories_list`: Список категорий кампании, полученный из значений `categories_dict`.
- `edited_categories`: Отредактированные категории, полученные из Google Sheet с помощью `gs.get_categories()`.
- `_cat`: Итератор по списку `edited_categories`, представляющий отдельную категорию.
- `_cat_ns`: Объект `SimpleNamespace`, созданный из данных категории `_cat`.
- `_updated_categories`: Объект `SimpleNamespace`, содержащий обновленные данные категорий.
- `campaign_dict`: Словарь, содержащий данные кампании, включая имя, заголовок, язык, валюту и категории.
- `edited_campaign`: Объект `SimpleNamespace`, созданный из `campaign_dict`, представляющий отредактированную кампанию.

## Логические блоки

1. **Инициализация объектов**:
   - Создаются инстансы классов `AliCampaignGoogleSheet` и `AliCampaignEditor` для работы с Google Sheets и данными кампании.
2. **Преобразование и установка категорий**:
   - Категории преобразуются из `SimpleNamespace` в словарь, а затем в список для установки в Google Sheets.
   - `_categories: SimpleNamespace` -> `categories_dict: dict[str, CategoryType]` -> `categories_list: list[CategoryType]`
3. **Получение и обновление категорий**:
   - Отредактированные категории получаются из Google Sheets и используются для обновления данных кампании.
   - `edited_categories: list[dict]` -> `_cat_ns: SimpleNamespace` -> `categories_dict[_cat_ns.name] = _cat_ns`
4. **Обновление продуктов категорий**:
   - Для каждой категории извлекаются и устанавливаются соответствующие продукты.
   - `category_name: str` -> `products: list` -> `gs.set_category_products(category_name, products)`
5. **Преобразование и обновление данных кампании**:
   - Обновленные данные категорий преобразуются обратно в `SimpleNamespace` и используются для создания словаря кампании.
   - `categories_dict: dict` -> `_updated_categories: SimpleNamespace` -> `campaign_dict: dict`
6. **Создание и обновление отредактированной кампании**:
   - Словарь кампании преобразуется в `SimpleNamespace` для представления отредактированной кампании.
   - `campaign_dict: dict` -> `edited_campaign: SimpleNamespace`

## Примеры

### Пример 1: Установка и получение категорий

```python
gs = AliCampaignGoogleSheet('1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0')
campaign_name = "lighting"
language = 'EN'
currency = 'USD'

campaign_editor = AliCampaignEditor(campaign_name, language, currency)
campaign_data = campaign_editor.campaign
_categories: SimpleNamespace = campaign_data.category

categories_dict: dict[str, CategoryType] = {category_name: getattr(_categories, category_name) for category_name in vars(_categories)}
categories_list: list[CategoryType] = list(categories_dict.values())

gs.set_categories(categories_list)
edited_categories: list[dict] = gs.get_categories()
```

Этот пример показывает, как установить категории в Google Sheets и получить отредактированные категории обратно.

### Пример 2: Обновление данных кампании

```python
campaign_dict: dict = {
    'name': campaign_data.campaign_name,
    'title': campaign_data.title,
    'language': language,
    'currency': currency,
    'category': _updated_categories
}

edited_campaign: SimpleNamespace = SimpleNamespace(**campaign_dict)
campaign_editor.update_campaign(edited_campaign)
```

Этот пример демонстрирует, как обновить данные кампании с использованием отредактированных категорий.