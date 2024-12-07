# Модуль `hypotez/src/endpoints/advertisement/facebook/promoter.py`

## Обзор

Модуль `promoter.py` отвечает за продвижение сообщений и событий в группах Facebook. Он обрабатывает кампании и события, публикуя их в группах Facebook, избегая при этом дублирования продвижений. Модуль использует WebDriver для автоматизации процесса.

## Определения

### Переменная `MODE`

```python
MODE = 'dev'
```

**Описание**: Строковая переменная, определяющая режим работы модуля.  В данном случае значение `'dev'`.


### Функция `get_event_url`

```python
def get_event_url(group_url: str) -> str:
    """
    Возвращает изменённый URL для создания события в Facebook, заменяя `group_id` значением из входного URL.

    Args:
        group_url (str): URL группы Facebook, содержащий `group_id`.

    Returns:
        str: Изменённый URL для создания события.
    """
    group_id = group_url.rstrip('/').split('/')[-1]
    base_url = "https://www.facebook.com/events/create/"
    params = {
        "acontext": '{"event_action_history":[{"surface":"group"},{"mechanism":"upcoming_events_for_group","surface":"group"}],"ref_notif_type":null}',
        "dialog_entry_point": "group_events_tab",
        "group_id": group_id
    }

    query_string = urlencode(params)
    return f"{base_url}?{query_string}"
```


### Класс `FacebookPromoter`

```python
class FacebookPromoter:
    """ Класс для продвижения товаров AliExpress и событий в группах Facebook.

    Этот класс автоматизирует публикацию промоакций в группах Facebook с помощью экземпляра WebDriver,
    обеспечивая продвижение категорий и событий, избегая дублирования.
    """
    d: Driver = None
    group_file_paths: str | Path = None
    no_video: bool = False
    promoter: str

    def __init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False):
        """ Инициализирует промоутера для групп Facebook.

        Args:
            d (Driver): Экземпляр WebDriver для автоматизации браузера.
            group_file_paths (list[str | Path] | str | Path, optional): Список путей к файлам с данными групп.
            no_video (bool, optional): Флаг для отключения видео в постах. По умолчанию False.
        """
        self.promoter = promoter
        self.d = d
        self.group_file_paths = group_file_paths if group_file_paths else get_filenames(gs.path.google_drive / 'facebook' / 'groups')
        self.no_video = no_video
        self.spinner = spinning_cursor()
```


## Функции


### `promote`

```python
    def promote(self, group: SimpleNamespace, item: SimpleNamespace, is_event: bool = False, language: str = None, currency: str = None) -> bool:
        """Продвигает категорию или событие в группе Facebook."""
        ...
```


### `log_promotion_error`

```python
    def log_promotion_error(self, is_event: bool, item_name: str):
        """Регистрирует ошибку продвижения для категории или события."""
        logger.debug(f"Ошибка при публикации {\'события\' if is_event else \'категории\'} {item_name}", None, False)
```


### `update_group_promotion_data`

```python
    def update_group_promotion_data(self, group: SimpleNamespace, item_name: str, is_event: bool = False):
        """Обновляет данные продвижения группы с новой промоакцией."""
        ...
```


### `process_groups`

```python
    def process_groups(self, campaign_name: str = None, events: list[SimpleNamespace] = None, is_event: bool = False, group_file_paths: list[str] = None, group_categories_to_adv: list[str] = ['sales'], language: str = None, currency: str = None):
        """Обрабатывает все группы для текущей кампании или продвижения события."""
        ...
```


### `get_category_item`

```python
    def get_category_item(self, campaign_name: str, group: SimpleNamespace, language: str, currency: str) -> SimpleNamespace:
        """Получает категорию для продвижения на основе кампании и промоутера."""
        ...
```


### `check_interval`

```python
    def check_interval(self, group: SimpleNamespace) -> bool:
        """Проверяет, достаточно ли времени прошло для продвижения этой группы."""
        ...
        return True
```


### `validate_group`

```python
    def validate_group(self, group: SimpleNamespace) -> bool:
        """Проверяет, что данные группы корректны."""
        return group and hasattr(group, 'group_url') and hasattr(group, 'group_categories')
```

**Примечания:**

* Документация к функциям `promote`, `process_groups`, `get_category_item` и `check_interval` требует дополнения. В текущем виде эти функции не описаны полностью.