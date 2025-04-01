# src.endpoints.advertisement.facebook.start_posting.py

## Обзор

Модуль предназначен для отправки рекламных объявлений в группы Facebook. Он использует веб-драйвер для автоматизации процесса публикации рекламы.

## Подробней

Этот модуль является частью системы автоматизации маркетинга и позволяет автоматически публиковать рекламные объявления в различных группах Facebook.  Он использует класс `FacebookPromoter` для управления кампаниями и веб-драйвер `Driver` для взаимодействия с Facebook через браузер Chrome. Модуль поддерживает запуск кампаний с использованием различных наборов групп, определенных в JSON-файлах. Кроме того, он обрабатывает исключения, позволяя процессу работать непрерывно, если возникают ошибки. Расположение файла в структуре проекта указывает на его роль в управлении рекламными кампаниями в Facebook.

## Классы

### `FacebookPromoter`

**Описание**: Класс для управления рекламными кампаниями Facebook.

**Методы**:
- `run_campaigns`: Запускает рекламные кампании.

**Параметры**:
- `d`: Объект веб-драйвера.
- `group_file_paths` (list[str]): Список путей к файлам JSON, содержащим информацию о группах.
- `no_video` (bool): Флаг, указывающий на отсутствие видео в объявлениях.

## Функции

### `Driver`

```python
def Driver(Chrome):
    """
    Args:
        Chrome: Драйвер для браузера Chrome.

    Returns:
        None

    Raises:
        None

    Example:
        Пример использования:
        >>> from src.webdriver.driver import Driver, Chrome
        >>> d = Driver(Chrome)
    """
```

**Описание**: Инициализирует веб-драйвер для управления браузером Chrome.

**Параметры**:
- `Chrome`: Класс, представляющий драйвер Chrome.

### `FacebookPromoter`

```python
def FacebookPromoter(d, group_file_paths: list[str], no_video: bool = True):
    """
    Args:
        d: Объект веб-драйвера.
        group_file_paths (list[str]): Список путей к файлам JSON, содержащим информацию о группах.
        no_video (bool): Флаг, указывающий на отсутствие видео в объявлениях. По умолчанию True.

    Returns:
        None

    Raises:
        None

    Example:
        Пример использования:
        >>> from src.endpoints.advertisement.facebook import FacebookPromoter
        >>> promoter = FacebookPromoter(d, group_file_paths=filenames, no_video = True)
    """
```

**Описание**: Инициализирует объект `FacebookPromoter` для управления рекламными кампаниями в Facebook.

**Параметры**:
- `d`: Объект веб-драйвера.
- `group_file_paths` (list[str]): Список путей к файлам JSON, содержащим информацию о группах.
- `no_video` (bool): Флаг, указывающий на отсутствие видео в объявлениях. По умолчанию `True`.

### `run_campaigns`

```python
def promoter.run_campaigns(campaigns: list, group_file_paths: list[str]):
    """
    Args:
        campaigns (list): Список кампаний для запуска.
        group_file_paths (list[str]): Список путей к файлам JSON, содержащим информацию о группах.

    Returns:
        None

    Raises:
        None

    Example:
        Пример использования:
        >>> promoter.run_campaigns(campaigns = copy.copy(campaigns), group_file_paths = filenames)
    """
```

**Описание**: Запускает рекламные кампании в Facebook.

**Параметры**:
- `campaigns` (list): Список кампаний для запуска.
- `group_file_paths` (list[str]): Список путей к файлам JSON, содержащим информацию о группах.