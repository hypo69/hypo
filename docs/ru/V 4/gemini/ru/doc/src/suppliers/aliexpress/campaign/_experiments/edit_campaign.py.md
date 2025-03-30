# Модуль `edit_campaign.py`

## Обзор

Модуль `edit_campaign.py` предназначен для редактирования рекламных кампаний AliExpress. Он включает функциональность для обработки кампаний, категорий кампаний и всех кампаний в целом. Модуль использует классы и функции из других модулей проекта, таких как `AliCampaignEditor`, `process_campaign`, `process_campaign_category` и `process_all_campaigns`.

## Подробней

Модуль предоставляет инструменты для автоматизации процесса редактирования рекламных кампаний на AliExpress. Он использует библиотеку `AliCampaignEditor` для внесения изменений в кампании и функции `process_campaign`, `process_campaign_category` и `process_all_campaigns` для обработки кампаний различных типов. Расположение файла `/src/suppliers/aliexpress/campaign/_experiments/edit_campaign.py` указывает на то, что модуль находится в экспериментальной стадии разработки.

## Импортированные модули

- `header`
- `pathlib.Path`: Для работы с путями к файлам и директориям.
- `src`: Главный модуль проекта.
- `src.gs`: Модуль, вероятно, содержащий глобальные настройки или утилиты.
- `src.suppliers.aliexpress.campaign.AliCampaignEditor`: Класс для редактирования кампаний AliExpress.
- `src.suppliers.aliexpress.campaign.process_campaign`: Функция для обработки кампании.
- `src.suppliers.aliexpress.campaign.process_campaign_category`: Функция для обработки категории кампании.
- `src.suppliers.aliexpress.campaign.process_all_campaigns`: Функция для обработки всех кампаний.
- `src.utils.get_filenames`: Функция для получения списка имен файлов.
- `src.utils.get_directory_names`: Функция для получения списка имен директорий.
- `src.utils.printer.pprint`: Функция для красивого вывода данных.

## Переменные

- `locales`: Словарь, содержащий соответствия между языковыми кодами (`EN`, `HE`, `RU`) и валютами (`USD`, `ILS`).

## Пример использования

```python
campaign_name = "building_bricks"
category_name = "building_bricks"
a = AliCampaignEditor(campaign_name,'EN','USD')
...
```
```