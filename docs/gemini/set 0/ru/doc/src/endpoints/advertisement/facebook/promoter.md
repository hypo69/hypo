# Модуль hypotez/src/endpoints/advertisement/facebook/promoter.py

## Обзор

Модуль `promoter.py` отвечает за продвижение сообщений и событий в группах Facebook. Он обрабатывает рекламные кампании и события, публикуя их в группах Facebook, избегая дублирования.

## Функции

### `get_event_url`

**Описание**: Возвращает измененный URL для создания события на Facebook, заменяя `group_id` значением из входящего URL.

**Параметры**:
- `group_url` (str): URL группы Facebook, содержащий `group_id`.
- `event_id` (str): Идентификатор события.

**Возвращает**:
- `str`: Измененный URL для создания события.


### `FacebookPromoter`

**Описание**: Класс для продвижения продуктов AliExpress и событий в группах Facebook.

**Методы**:

- `__init__`: Инициализирует продвижение для групп Facebook.
    **Параметры**:
        - `d` (Driver): Экземпляр WebDriver для автоматизации браузера.
        - `group_file_paths` (list[str | Path] | str | Path, optional): Список путей к файлам с данными групп. По умолчанию берется из папки `gs.path.google_drive / 'facebook' / 'groups'`.
        - `no_video` (bool, optional): Флаг для отключения видео в постах. По умолчанию False.
    
- `promote`: Продвигает категорию или событие в группе Facebook.
    **Параметры**:
        - `group` (SimpleNamespace): Данные о группе.
        - `item` (SimpleNamespace): Данные о категории или событии.
        - `is_event` (bool, optional): Признак, является ли элемент событием. По умолчанию False.
        - `language` (str, optional): Язык для фильтрации.
        - `currency` (str, optional): Валюта для фильтрации.
    **Возвращает**:
        - `bool`: True, если продвижение прошло успешно, иначе False.


- `log_promotion_error`: Записывает ошибку продвижения категории или события в лог.
    **Параметры**:
        - `is_event` (bool): Признак, является ли элемент событием.
        - `item_name` (str): Название категории или события.

- `update_group_promotion_data`: Обновляет данные о продвижении группы с новыми сведениями.
    **Параметры**:
        - `group` (SimpleNamespace): Данные о группе.
        - `item_name` (str): Название категории или события.
        - `is_event` (bool, optional): Признак, является ли элемент событием. По умолчанию False.

- `process_groups`: Обрабатывает все группы для текущей рекламной кампании или продвижения события.
    **Параметры**:
        - `campaign_name` (str, optional): Название рекламной кампании.
        - `events` (list[SimpleNamespace], optional): Список событий.
        - `is_event` (bool, optional): Признак, является ли продвижение событием. По умолчанию False.
        - `group_file_paths` (list[str], optional): Список путей к файлам с данными о группах.
        - `group_categories_to_adv` (list[str], optional): Список категорий, которые нужно продвигать. По умолчанию ['sales'].
        - `language` (str, optional): Язык для фильтрации.
        - `currency` (str, optional): Валюта для фильтрации.
    **Возвращает**:
       - `bool`: True если запуск успешно завершился, иначе False


- `get_category_item`: Возвращает категорию для продвижения, основываясь на кампании и источнике.
    **Параметры**:
        - `campaign_name` (str): Название кампании.
        - `group` (SimpleNamespace): Данные о группе.
        - `language` (str, optional): Язык для фильтрации.
        - `currency` (str, optional): Валюта для фильтрации.
    **Возвращает**:
        - `SimpleNamespace`: Объект с данными о категории.

- `check_interval`: Проверяет, прошло ли необходимое время для следующего продвижения.
    **Параметры**:
        - `group` (SimpleNamespace): Данные о группе.
    **Возвращает**:
        - `bool`: True, если интервал прошёл, иначе False.
    **Вызывает исключения**:
        - `ValueError`: Если формат интервала неверный.

- `parse_interval`: Преобразует строковый интервал в объект timedelta.
    **Параметры**:
        - `interval` (str): Интервал в строковом формате (например, '1H', '6M').
    **Возвращает**:
        - `timedelta`: Соответствующий объект timedelta.
    **Вызывает исключения**:
        - `ValueError`: Если формат интервала неверный.

- `run_campaigns`: Запускает цикл продвижения кампаний для всех групп и категорий последовательно.
    **Параметры**:
        - `campaigns` (list[str]): Список имён кампаний.
        - `group_file_paths` (list[str]): Список путей к файлам с данными групп.
        - `group_categories_to_adv` (list[str], optional): Список категорий, которые нужно продвигать.
        - `language` (str, optional): Язык для фильтрации.
        - `currency` (str, optional): Валюта для фильтрации.
        - `no_video` (bool, optional): Флаг для отключения видео в постах.


- `run_events`: Запускает продвижение событий во всех группах последовательно.
    **Параметры**:
        - `events_names` (list[str]): Список имён событий.
        - `group_file_paths` (list[str]): Список путей к файлам с данными групп.

- `stop`: Останавливает процесс продвижения, завершая экземпляр WebDriver.


## Примеры использования

```python
#Пример использования run_campaigns
group_files = ["ru_usd.json", "usa.json", "ger_en_eur.json", "he_il.json", "ru_il.json"]
promoter = FacebookPromoter(d=Driver(Chrome), group_file_paths=group_files, no_video=True)
promoter.run_campaigns(campaigns=["campaign1", "campaign2"], group_file_paths=group_files)
```

```python
#Пример использования run_events
promoter.run_events(events_names=["event1", "event2"], group_file_paths=group_files)
```

```python
# Пример использования check_interval
group = SimpleNamespace(interval="1H", last_promo_sended="01/01/23 10:00")
result = promoter.check_interval(group)
print(result)
```

```
```
```
```
```
```
```

```