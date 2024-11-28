# Модуль `hypotez/src/endpoints/advertisement/facebook/promoter.py`

## Обзор

Данный модуль отвечает за продвижение сообщений и событий в группах Facebook. Он обрабатывает кампании и события, публикуя их в группах Facebook, избегая дублирования.

## Константы

### `MODE`

Строковая константа, определяющая режим работы (в данном случае 'dev').

## Функции

### `get_event_url(group_url: str) -> str`

**Описание**: Возвращает изменённый URL для создания события на Facebook, заменяя `group_id` значением из входного URL.

**Параметры**:

- `group_url` (str): URL группы Facebook, содержащий `group_id`.

**Возвращает**:

- `str`: Изменённый URL для создания события.

### `FacebookPromoter.__init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False)`

**Описание**: Инициализирует продвигатель для групп Facebook.

**Параметры**:

- `d` (Driver): Экземпляр WebDriver для автоматизации браузера.
- `promoter` (str): Идентификатор продвигателя.
- `group_file_paths` (Optional[list[str | Path] | str | Path], необязательно): Список путей к файлам с данными о группах. По умолчанию используется список файлов из папки `gs.path.google_drive / 'facebook' / 'groups'`.
- `no_video` (bool, необязательно): Флаг для отключения видео в постах. По умолчанию `False`.

### `FacebookPromoter.promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool`

**Описание**: Продвигает категорию или событие в группе Facebook.

**Параметры**:

- `group` (SimpleNamespace): Объект с данными о группе.
- `item` (SimpleNamespace): Объект с данными о категории/событии.
- `is_event` (bool, необязательно): Флаг, указывающий, является ли `item` событием. По умолчанию `False`.
- `language` (str, необязательно): Язык.
- `currency` (str, необязательно): Валюта.

**Возвращает**:

- `bool`: `True` в случае успешного продвижения, иначе `False`.

### `FacebookPromoter.log_promotion_error(self, is_event: bool, item_name: str)`

**Описание**: Записывает ошибку при продвижении категории или события.

**Параметры**:

- `is_event` (bool): Флаг, указывающий, является ли `item` событием.
- `item_name` (str): Название категории/события.

### `FacebookPromoter.update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False)`

**Описание**: Обновляет данные о продвижении группы с новой информацией.

**Параметры**:

- `group` (SimpleNamespace): Объект с данными о группе.
- `item_name` (str): Название категории/события.
- `is_event` (bool, необязательно): Флаг, указывающий, является ли `item` событием. По умолчанию `False`.

### `FacebookPromoter.process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None)`

**Описание**: Обрабатывает все группы для текущей кампании или продвижения события.

**Параметры**:

- `campaign_name` (str, необязательно): Название кампании.
- `events` (list[SimpleNamespace], необязательно): Список событий для продвижения.
- `is_event` (bool, необязательно): Флаг, указывающий, является ли текущая задача продвижением события.
- `group_file_paths` (list[str], необязательно): Список путей к файлам с данными о группах.
- `group_categories_to_adv` (list[str], необязательно): Список категорий для продвижения.
- `language` (str, необязательно): Язык.
- `currency` (str, необязательно): Валюта.


### `FacebookPromoter.get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace`

**Описание**: Получает элемент категории для продвижения на основе кампании и продвигателя.

**Параметры**:

- `campaign_name` (str): Название кампании.
- `group` (SimpleNamespace): Объект с данными о группе.
- `language` (str): Язык.
- `currency` (str): Валюта.

**Возвращает**:

- `SimpleNamespace`: Элемент категории.


### `FacebookPromoter.check_interval(self, group: SimpleNamespace) -> bool`

**Описание**: Проверяет, истек ли необходимый интервал для следующего продвижения.

**Параметры**:

- `group` (SimpleNamespace): Объект с данными о группе.

**Возвращает**:

- `bool`: `True`, если интервал истек, иначе `False`.

**Возможные исключения**:

- `ValueError`: Если формат интервала недействителен.


### `FacebookPromoter.parse_interval(self, interval: str) -> timedelta`

**Описание**: Преобразует строковый интервал в объект `timedelta`.

**Параметры**:

- `interval` (str): Интервал в строковом формате (например, '1H', '6M').

**Возвращает**:

- `timedelta`: Соответствующий объект `timedelta`.

**Возможные исключения**:

- `ValueError`: Если формат интервала недействителен.


### `FacebookPromoter.run_campaigns(self, campaigns: list[str], group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language:str = None, currency:str = None, no_video:bool = False)`

**Описание**: Запускает цикл продвижения кампании для всех групп и категорий последовательно.

**Параметры**:

- `campaigns` (list[str]): Список названий кампаний для продвижения.
- `group_file_paths` (list[str], необязательно): Список путей к файлам с данными о группах.
- `group_categories_to_adv` (list[str], необязательно): Список категорий для продвижения.
- `language` (str, необязательно): Язык.
- `currency` (str, необязательно): Валюта.
- `no_video` (bool, необязательно): Флаг для отключения видео в постах.

### `FacebookPromoter.run_events(self, events_names: list[str], group_file_paths: list[str])`

**Описание**: Запускает продвижение событий во всех группах последовательно.

**Параметры**:

- `events_names` (list[str]): Список названий событий.
- `group_file_paths` (list[str]): Список путей к файлам с данными о группах.


### `FacebookPromoter.stop(self)`

**Описание**: Останавливает процесс продвижения, закрывая экземпляр WebDriver.

## Пример использования (в блоке `if __name__ == "__main__":`)


```
```