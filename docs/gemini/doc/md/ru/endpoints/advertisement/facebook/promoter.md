```markdown
# Модуль `hypotez/src/endpoints/advertisement/facebook/promoter.py`

## Обзор

Этот модуль отвечает за продвижение рекламных сообщений и событий в группах Facebook. Он обрабатывает кампании и события, публикуя их в группах Facebook, избегая дублирования.  Модуль использует WebDriver для автоматизации процесса.

## Классы

### `FacebookPromoter`

**Описание**: Класс для продвижения продуктов AliExpress и событий в группах Facebook.  Автоматизирует публикацию промоматериалов, учитывая категории, события и избегает дублирования.

**Методы**:

- `__init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False)`: Инициализирует продвижение для Facebook групп.
- `promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool`: Продвигает категорию или событие в группе Facebook.
- `log_promotion_error(self, is_event: bool, item_name: str)`: Логирует ошибку продвижения категории или события.
- `update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False)`: Обновляет данные о продвижении группы с учетом новых промоматериалов.
- `process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None)`: Обрабатывает все группы для текущей кампании или события продвижения.
- `get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace`:  Получает категорию товара для продвижения на основе кампании.
- `check_interval(self, group: SimpleNamespace) -> bool`: Проверяет, прошло ли необходимое время для следующего продвижения.
- `parse_interval(self, interval: str) -> timedelta`: Преобразует строку интервала в объект timedelta.
- `run_campaigns(self, campaigns: list[str], group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language:str = None, currency:str = None, no_video:bool = False)`: Запускает цикл продвижения кампании для всех групп и категорий.
- `run_events(self, events_names: list[str], group_file_paths: list[str])`: Запускает продвижение событий во всех группах.
- `stop(self)`: Останавливает процесс продвижения, закрывая экземпляр WebDriver.


## Функции

### `get_event_url(group_url: str) -> str`

**Описание**: Возвращает изменённый URL для создания события в Facebook, заменяя `group_id` значением из входного URL.

**Параметры**:
- `group_url` (str): URL группы Facebook, содержащий `group_id`.
- `event_id` (str): Идентификатор события (не используется в реализации).

**Возвращает**:
- `str`: Изменённый URL для создания события.


##  Примечания

Модуль использует `SimpleNamespace` для структурирования данных о группах и товарах, а также `gs` (предположительно, глобальный объект) и `logger` для работы с файлами, логированием и другими вспомогательными функциями.


## Пример использования

```python
group_files = ["ru_usd.json", "usa.json", ...]
promoter = FacebookPromoter(d=Driver(Chrome), group_file_paths=group_files, no_video=True)
promoter.run_campaigns(campaigns=["campaign1", "campaign2"], group_file_paths=group_files)
```

**Обратите внимание:** Приведенный пример предполагает наличие необходимых объектов и модулей, таких как `Driver`, `Chrome`, `SimpleNamespace`, `gs`, и `logger`.
```
