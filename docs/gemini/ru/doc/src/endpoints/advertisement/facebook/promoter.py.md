# Модуль `promoter.py`

## Обзор

Модуль `promoter.py` предназначен для автоматизации процесса продвижения контента (сообщений, событий, рекламы) в группах Facebook. Он содержит класс `FacebookPromoter`, который позволяет публиковать рекламные материалы в группах Facebook, избегая повторных публикаций и учитывая различные параметры, такие как язык и валюта.

## Подробней

Этот модуль является частью системы автоматизированного маркетинга в Facebook. Он использует WebDriver для взаимодействия с Facebook через браузер, что позволяет имитировать действия пользователя и автоматизировать публикацию контента. Основная цель модуля - упростить и автоматизировать процесс продвижения товаров и мероприятий в Facebook группах, сокращая время и усилия, затрачиваемые на ручное управление рекламными кампаниями.

## Классы

### `FacebookPromoter`

**Описание**: Класс `FacebookPromoter` предназначен для продвижения товаров AliExpress и событий в группах Facebook.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `FacebookPromoter`.
- `promote`: Продвигает категорию или событие в группе Facebook.
- `log_promotion_error`: Регистрирует ошибку продвижения для категории или события.
- `update_group_promotion_data`: Обновляет данные о продвижении группы с новой информацией.
- `process_groups`: Обрабатывает все группы для текущей рекламной кампании или продвижения события.
- `get_category_item`: Получает элемент категории для продвижения на основе кампании и промоутера.
- `check_interval`: Проверяет, достаточно ли времени прошло для продвижения этой группы.
- `validate_group`: Проверяет корректность данных группы.

**Параметры**:
- `d` (Driver): Экземпляр WebDriver для автоматизации браузера.
- `promoter` (str): Имя промоутера (например, 'aliexpress').
- `group_file_paths` (Optional[list[str | Path] | str | Path], optional): Список путей к файлам, содержащим данные групп. По умолчанию `None`.
- `no_video` (bool, optional): Флаг для отключения видео в постах. По умолчанию `False`.

**Примеры**
```python
from src.webdriver.driver import Driver
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from pathlib import Path

# Пример инициализации класса FacebookPromoter
driver = Driver()
promoter = FacebookPromoter(d=driver, promoter='aliexpress', group_file_paths=[Path('path/to/group_file.json')])
```

## Функции

### `get_event_url`

```python
def get_event_url(group_url: str) -> str:
    """
    Args:
        group_url (str): Facebook group URL containing `group_id`.

    Returns:
        str: Modified URL for creating the event.
    """
```

**Описание**: Возвращает измененный URL для создания события на Facebook, заменяя `group_id` значением из входного URL.

**Параметры**:
- `group_url` (str): URL группы Facebook, содержащий `group_id`.

**Возвращает**:
- `str`: Измененный URL для создания события.

**Примеры**:
```python
group_url = "https://www.facebook.com/groups/1234567890"
event_url = get_event_url(group_url)
print(event_url)
# Output: https://www.facebook.com/events/create/?acontext=%7B%22event_action_history%22%3A%5B%7B%22surface%22%3A%22group%22%7D%2C%7B%22mechanism%22%3A%22upcoming_events_for_group%22%2C%22surface%22%3A%22group%22%7D%5D%2C%22ref_notif_type%22%3Anull%7D&dialog_entry_point=group_events_tab&group_id=1234567890
```
```python
group_url = "https://www.facebook.com/groups/0987654321/"
event_url = get_event_url(group_url)
print(event_url)
# Output: https://www.facebook.com/events/create/?acontext=%7B%22event_action_history%22%3A%5B%7B%22surface%22%3A%22group%22%7D%2C%7B%22mechanism%22%3A%22upcoming_events_for_group%22%2C%22surface%22%3A%22group%22%7D%5D%2C%22ref_notif_type%22%3Anull%7D&dialog_entry_point=group_events_tab&group_id=0987654321
```
```python
group_url = "https://www.facebook.com/groups/qwertyuiop"
event_url = get_event_url(group_url)
print(event_url)
# Output: https://www.facebook.com/events/create/?acontext=%7B%22event_action_history%22%3A%5B%7B%22surface%22%3A%22group%22%7D%2C%7B%22mechanism%22%3A%22upcoming_events_for_group%22%2C%22surface%22%3A%22group%22%7D%5D%2C%22ref_notif_type%22%3Anull%7D&dialog_entry_point=group_events_tab&group_id=qwertyuiop
```
```python
group_url = "https://www.facebook.com/groups/azsxdfcvgh"
event_url = get_event_url(group_url)
print(event_url)
# Output: https://www.facebook.com/events/create/?acontext=%7B%22event_action_history%22%3A%5B%7B%22surface%22%3A%22group%22%7D%2C%7B%22mechanism%22%3A%22upcoming_events_for_group%22%2C%22surface%22%3A%22group%22%7D%5D%2C%22ref_notif_type%22%3Anull%7D&dialog_entry_point=group_events_tab&group_id=azsxdfcvgh
```
```python
group_url = "https://www.facebook.com/groups/plmoknijbuh"
event_url = get_event_url(group_url)
print(event_url)
# Output: https://www.facebook.com/events/create/?acontext=%7B%22event_action_history%22%3A%5B%7B%22surface%22%3A%22group%22%7D%2C%7B%22mechanism%22%3A%22upcoming_events_for_group%22%2C%22surface%22%3A%22group%22%7D%5D%2C%22ref_notif_type%22%3Anull%7D&dialog_entry_point=group_events_tab&group_id=plmoknijbuh