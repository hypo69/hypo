# Модуль для отправки мероприятий в группы Facebook

## Обзор

Модуль `start_event.py` предназначен для автоматической отправки мероприятий в группы Facebook. Он использует веб-драйвер для взаимодействия с Facebook и выполняет итеративный процесс отправки мероприятий с заданными параметрами.

## Подробнее

Этот модуль является частью системы автоматизации маркетинга `hypotez`. Он отвечает за продвижение мероприятий в Facebook группах. Модуль конфигурируется через JSON-файлы, которые содержат информацию о группах и параметрах событий. Процесс включает в себя инициализацию веб-драйвера, загрузку конфигураций и запуск цикла отправки мероприятий с заданными интервалами. Расположение файла `hypotez/src/endpoints/advertisement/facebook/start_event.py` указывает, что он является частью подсистемы для управления рекламой в Facebook.

## Переменные

### `d`

**Описание**: Экземпляр класса `Driver` для управления браузером Chrome.

### `filenames`

**Описание**: Список имен файлов, содержащих пути к группам.
- `my_managed_groups.json`
- `usa.json`
- `he_il.json`
- `ru_il.json`
- `katia_homepage.json`
- `ru_usd.json`
- `ger_en_eur.json`

### `excluded_filenames`

**Описание**: Список имен файлов, исключенных из обработки.

### `events_names`

**Описание**: Список имен событий для запуска.
- `choice_day_01_10`

### `promoter`

**Описание**: Экземпляр класса `FacebookPromoter` для управления продвижением в Facebook.

## Функции

### `FacebookPromoter.run_events`

```python
    def run_events(events_names: list[str], group_file_paths: list[str]) -> None:
        """
        Args:
            events_names (list[str]): Список имен событий для запуска.
            group_file_paths (list[str]): Список путей к файлам групп.

        Returns:
            None

        Raises:
            Exception: Если возникает ошибка при выполнении событий.
        """
```

**Описание**: Запускает события в группах Facebook.

**Параметры**:
- `events_names` (list[str]): Список имен событий для запуска.
- `group_file_paths` (list[str]): Список путей к файлам групп.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при выполнении событий.

**Примеры**:
   ```python
   promoter.run_events(events_names=['event1', 'event2'], group_file_paths=['groups1.json', 'groups2.json'])
   ```
## Обработка исключений

Обработка исключений включает в себя перехват `KeyboardInterrupt` для корректного завершения работы программы при прерывании с клавиатуры.

```python
try:
    while True:
        logger.debug(f"waikig up {time.strftime('%H:%M:%S')}",None,False)
        promoter.run_events(events_names = events_names, group_file_paths = filenames)
        logger.debug(f"going to sleep at {time.strftime('%H:%M:%S')}",None,False)
        time.sleep(7200)
        
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```