# Модуль для публикации событий в Facebook

## Обзор

Модуль `post_event.py` предназначен для автоматической публикации информации о мероприятиях в Facebook. Он получает данные о мероприятиях из JSON-файлов, расположенных в Google Drive, и отправляет их в указанные группы Facebook. Модуль использует веб-драйвер для взаимодействия с Facebook и библиотеку `jjson` для обработки JSON-файлов.

## Подробней

Модуль автоматизирует процесс публикации информации о мероприятиях в группах Facebook. Он выполняет следующие шаги:

1.  Получает список директорий с данными о мероприятиях из Google Drive.
2.  Загружает данные о каждом мероприятии из JSON-файла.
3.  Определяет группы Facebook, в которые необходимо опубликовать информацию о мероприятии.
4.  Использует веб-драйвер для входа в Facebook и публикации информации в выбранных группах.

## Функции

### `post_events`

```python
def post_events():
    """Обрабатывает и отправляет мероприятия на Facebook.

    Функция получает данные о мероприятиях из указанной директории, загружает детали мероприятий из JSON-файлов
    и отправляет их на Facebook. Мероприятия хранятся в структуре директорий под папкой `facebook/events`.

    Raises:
        FileNotFoundError: Если JSON-файл с информацией о мероприятии отсутствует.
    """
```

**Назначение**: Обрабатывает и публикует мероприятия на Facebook.

**Как работает функция**:

1.  Инициализирует веб-драйвер Chrome.
2.  Получает список директорий с данными о мероприятиях из Google Drive (события AliExpress).
3.  Получает список файлов с информацией о группах Facebook, в которые нужно публиковать мероприятия.
4.  Создает экземпляр класса `FacebookPromoter` для управления публикацией мероприятий.
5.  Для каждого файла с данными о мероприятии:
    *   Загружает данные о мероприятии из JSON-файла.
    *   Использует метод `process_groups` класса `FacebookPromoter` для публикации информации о мероприятии в выбранных группах.

**ASCII flowchart**:

```
Начало
  ↓
Инициализация веб-драйвера (Chrome)
  ↓
Получение списка директорий событий из Google Drive
  ↓
Получение списка файлов групп Facebook из Google Drive
  ↓
Создание экземпляра FacebookPromoter
  ↓
Для каждой директории события:
  │
  ├── Загрузка данных события из JSON
  │
  └── Публикация события в группах Facebook через FacebookPromoter
  ↓
Конец
```

**Примеры**:

```python
post_events()
```

### `post_to_my_group`

```python
def post_to_my_group(event):
    """"""
```

**Назначение**: Публикует мероприятие в указанных группах Facebook.

**Как работает функция**:

1.  Загружает данные о группах из JSON-файла `my_managed_groups.json`.
2.  Инициализирует веб-драйвер Chrome.
3.  Для каждой группы Facebook:
    *   Извлекает URL группы из данных JSON.
    *   Переходит по URL группы с помощью веб-драйвера.
    *   Вызывает функцию `post_event` для публикации информации о мероприятии в группе.

**ASCII flowchart**:

```
Начало
  ↓
Загрузка данных о группах из JSON
  ↓
Инициализация веб-драйвера (Chrome)
  ↓
Для каждой группы:
  │
  ├── Извлечение URL группы
  │
  ├── Переход по URL группы
  │
  └── Публикация события в группе через post_event
  ↓
Конец
```

**Примеры**:

```python
event = j_loads_ns(gs.path.google_drive / 'aliexpress' / 'events'  / 'sep_11_2024_over60_pricedown' / 'sep_11_2024_over60_pricedown.json')
post_to_my_group(event)
```

```markdown
def get_event_url(group_url: str = "https://www.facebook.com/groups/474876993824344") -> str:
    """Генерирует URL для публикации события в группе Facebook.

    Args:
        group_url (str, optional): URL группы Facebook.
            Defaults to "https://www.facebook.com/groups/474876993824344".

    Returns:
        str: URL для публикации события в группе.

    Example:
        >>> get_event_url()
        'https://m.facebook.com/groups/474876993824344'
    """
    ...

def post_event(driver: Driver, event: dict) -> None:
    """Публикует событие в группе Facebook.

    Args:
        driver (Driver): Экземпляр веб-драйвера для управления браузером.
        event (dict): Словарь с данными о событии.

    Returns:
        None

    Raises:
        Exception: Если возникает ошибка при выполнении локатора.

    Example:
        >>> post_event(driver, event_data)
    """
    ...

class FacebookPromoter:
    def __init__(self, d: Driver, group_file_paths: list):
        """Инициализирует объект FacebookPromoter.

        Args:
            d (Driver): Экземпляр веб-драйвера для управления браузером.
            group_file_paths (list): Список путей к файлам с данными о группах Facebook.
        """
        ...

    def process_groups(self, events: list, is_event: bool, group_file_paths: list) -> None:
        """Обрабатывает группы Facebook и публикует события.

        Args:
            events (list): Список событий для публикации.
            is_event (bool): Флаг, указывающий, является ли публикуемый объект событием.
            group_file_paths (list): Список путей к файлам с данными о группах Facebook.

        Returns:
            None
        """
        ...