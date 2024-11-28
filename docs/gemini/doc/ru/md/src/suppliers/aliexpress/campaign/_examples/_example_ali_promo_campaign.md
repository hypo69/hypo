# Модуль hypotez/src/suppliers/aliexpress/campaign/_examples/_example_ali_promo_campaign.py

## Обзор

Этот модуль содержит примеры создания рекламных кампаний на AliExpress. Он демонстрирует использование классов `AliPromoCampaign` и `AliAffiliatedProducts`, а также вспомогательных функций из модуля `src.utils` для работы с данными и файлами.

## Переменные

### `MODE`

**Описание**: Переменная, хранящая режим работы (например, 'dev' для разработки).

**Значение**:  `'dev'`


## Импорты

Этот раздел содержит список импортированных модулей и классов:

- `header`
- `pathlib.Path`
- `types.SimpleNamespace`
- `src.gs`
- `src.suppliers.aliexpress.AliPromoCampaign`
- `src.suppliers.aliexpress.AliAffiliatedProducts`
- `src.utils.get_filenames`
- `src.utils.get_directory_names`
- `src.utils.read_text_file`
- `src.utils.csv2dict`
- `src.utils.j_loads_ns`
- `src.utils.pprint`
- `src.logger.logger`


## Функции

В данном модуле нет явно определенных функций.


## Классы

В данном файле нет объявлений классов.


## Примеры использования

### Создание экземпляра класса `AliPromoCampaign`

```python
campaign_name = '280624_cleararanse'
category_name = 'gaming_comuter_accessories'
language = 'EN'
currency = 'USD'

a: SimpleNamespace = AliPromoCampaign(campaign_name=campaign_name,
                     category_name=category_name,
                     language=language,
                     currency=currency)
```

Этот пример демонстрирует создание экземпляра класса `AliPromoCampaign` с заданными параметрами. Обратите внимание на использование аннотаций типов для параметров.


### Использование методов класса `AliPromoCampaign`

```python
campaign = a.campaign
category = a.category
products = a.category.products
```

Этот пример демонстрирует доступ к атрибутам созданного объекта `AliPromoCampaign`, которые представляют собой объекты, содержащие данные о кампании и категории.


### Создание экземпляра класса `AliPromoCampaign` с dict

```python
a = AliPromoCampaign(campaign_name, category_name, {'EN': 'USD'})
```

Пример демонстрирует создание экземпляра класса `AliPromoCampaign` используя словарь для языков и валют.


### Создание экземпляра класса `AliPromoCampaign` с string

```python
a = AliPromoCampaign(campaign_name, category_name, 'EN', 'USD')
```

Пример демонстрирует создание экземпляра класса `AliPromoCampaign` используя строки для языка и валюты.


## Пути

### `campaigns_directory`

**Описание**: Путь к директории с рекламными кампаниями.

**Значение**: `Path(gs.path.google_drive, 'aliexpress', 'campaigns')`


### `campaign_names`

**Описание**: Список имен директорий в директории `campaigns_directory`.

**Значение**: `get_directory_names(campaigns_directory)`


## Заметки

- Модуль предоставляет примеры инициализации и доступа к атрибутам класса `AliPromoCampaign`.
- Файл импортирует нужные классы и функции из других модулей для работы с данными и файлами.
- Модуль использует `SimpleNamespace` для хранения данных.
- В коде присутствуют неполные или неиспользуемые секции, которые могли быть временными или являющимися частью реализации других функций.
- Подробные описания классов `AliPromoCampaign` и `AliAffiliatedProducts`, а также других используемых классов и функций, ожидаются в других модулях.