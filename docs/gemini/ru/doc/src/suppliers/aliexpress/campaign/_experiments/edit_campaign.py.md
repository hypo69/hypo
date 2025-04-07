# Модуль `edit_campaign.py`

## Обзор

Модуль предназначен для редактирования рекламных кампаний на платформе AliExpress. Включает функциональность для обработки и изменения параметров кампаний, категорий и общей конфигурации.

## Подробней

Модуль `edit_campaign.py` является частью проекта `hypotez` и отвечает за редактирование рекламных кампаний на AliExpress. Он включает в себя инструменты для настройки параметров кампаний, обработки категорий и общей конфигурации рекламных активностей. Модуль использует классы и функции из других модулей проекта, таких как `AliCampaignEditor`, `process_campaign`, `process_campaign_category` и `process_all_campaigns`. Расположение файла в структуре проекта указывает на его роль в экспериментальных настройках кампаний.

## Импортированные модули

В данном модуле используются следующие импортированные модули:

- `header`
- `pathlib.Path`
- `src.gs`
- `src.suppliers.aliexpress.campaign.AliCampaignEditor`
- `src.suppliers.aliexpress.campaign.process_campaign`
- `src.suppliers.aliexpress.campaign.process_campaign_category`
- `src.suppliers.aliexpress.campaign.process_all_campaigns`
- `src.utils.get_filenames`
- `src.utils.get_directory_names`
- `src.utils.printer.pprint`

## Переменные

### `locales`

```python
locales = {'EN': 'USD', 'HE': 'ILS', 'RU': 'ILS'}
```

- **Описание**: Словарь, содержащий соответствия между языковыми кодами (`EN`, `HE`, `RU`) и валютами (`USD`, `ILS`).

### `campaign_name`

```python
campaign_name = "building_bricks"
```

- **Описание**: Имя рекламной кампании (`building_bricks`).

### `category_name`

```python
category_name = "building_bricks"
```

- **Описание**: Имя категории рекламной кампании (`building_bricks`).

### `a`

```python
a = AliCampaignEditor(campaign_name,'EN','USD')
```

- **Описание**: Экземпляр класса `AliCampaignEditor`, созданный для редактирования кампании с указанным именем, языком и валютой.

## Классы

В предоставленном коде нет определения новых классов. Используется класс `AliCampaignEditor` из модуля `src.suppliers.aliexpress.campaign`.

## Функции

В предоставленном коде нет определения новых функций. Используются функции `process_campaign`, `process_campaign_category`, `process_all_campaigns` из модуля `src.suppliers.aliexpress.campaign`.

```python
...