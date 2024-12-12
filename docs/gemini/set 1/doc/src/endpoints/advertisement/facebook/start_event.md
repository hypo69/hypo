# Модуль `hypotez/src/endpoints/advertisement/facebook/start_event.py`

## Обзор

Модуль `start_event.py` отвечает за запуск автоматизированной рекламной кампании на Facebook, отправляя мероприятия в заданные группы. Он использует драйвер для взаимодействия с веб-сайтом Facebook и класс `FacebookPromoter` для управления процессом продвижения.

## Переменные

### `MODE`

**Тип**: `str`

**Описание**:  Устанавливает режим работы модуля (например, 'dev', 'prod').

### `filenames`

**Тип**: `list[str]`

**Описание**: Список путей к файлам с информацией о группах Facebook, в которые нужно отправлять мероприятия.

### `excluded_filenames`

**Тип**: `list[str]`

**Описание**: Список файлов, которые должны быть исключены из процесса отправки.

### `events_names`

**Тип**: `list`

**Описание**: Список имен мероприятий, которые нужно отправлять.

## Классы

### `FacebookPromoter`

**Описание**: Класс для управления процессом отправки мероприятий в группы Facebook.  Подробности реализации смотрите в соответствующем модуле.

## Функции

### `run_events`

```python
def run_events(events_names: list, group_file_paths: list) -> None:
    """
    Args:
        events_names (list): Список имен мероприятий.
        group_file_paths (list): Список путей к файлам с данными о группах.

    Returns:
        None: Функция не возвращает значение.

    Raises:
        Exception:  В случае возникновения каких-либо ошибок во время работы с группами Facebook или файлами.
    """
```

## Обработка исключений

```python
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

**Описание**: Обрабатывает исключение `KeyboardInterrupt`, выдаваемое при прерывании программы пользователем. Выводит сообщение в лог о прерывании кампании.


## Основной блок

```python
d = Driver(Chrome)
d.get_url(r"https://facebook.com")

promoter:FacebookPromoter = FacebookPromoter(d, group_file_paths=filenames, no_video = True)

try:
    while True:
        logger.debug(f"waikig up {time.strftime(\'%H:%M:%S\')}",None,False)
        promoter.run_events(events_names = events_names, group_file_paths = filenames)
        logger.debug(f"going to sleep at {time.strftime(\'%H:%M:%S\')}",None,False)
        time.sleep(7200)
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

**Описание**: Основной цикл программы.  Инициализирует драйвер, создаёт экземпляр класса `FacebookPromoter`, и запускает функцию `run_events` в бесконечном цикле с периодом 7200 секунд.  Обрабатывает исключение `KeyboardInterrupt`.


**Примечание**:  Этот код предполагает наличие импортированных модулей (`header`, `time`, `jjson`, `Driver`, `Chrome`, `FacebookPromoter`, `logger`).  Для полной документации необходимо добавить документацию к этим импортированным модулям и классу `FacebookPromoter`.  Также, следует добавить информацию о формате файлов, используемых для `filenames`.