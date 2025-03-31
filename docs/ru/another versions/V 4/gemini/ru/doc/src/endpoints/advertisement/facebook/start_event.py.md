# Модуль отправки мероприятий в Facebook

## Обзор

Модуль `src.endpoints.advertisement.facebook.start_event` предназначен для автоматической отправки мероприятий в группы Facebook. Он использует веб-драйвер для взаимодействия с Facebook и загружает данные о группах и мероприятиях из JSON-файлов.

## Подробней

Этот модуль является частью системы автоматизации маркетинга в Facebook. Он позволяет автоматически публиковать информацию о мероприятиях в различных группах, используя данные из конфигурационных файлов. Модуль инициализирует веб-драйвер, настраивает промоутера Facebook и запускает цикл, который периодически публикует мероприятия.

## Переменные

### `d`

**Описание**: Экземпляр веб-драйвера Chrome для управления браузером.

### `filenames`

**Описание**: Список имен файлов JSON, содержащих информацию о группах для публикации мероприятий.

### `excluded_filenames`

**Описание**: Список имен файлов, которые исключаются из процесса публикации мероприятий.

### `events_names`

**Описание**: Список названий мероприятий для публикации.

### `promoter`

**Описание**: Экземпляр класса `FacebookPromoter`, который управляет процессом публикации мероприятий в Facebook.

## Классы

### `FacebookPromoter`

**Описание**: Класс, отвечающий за публикацию мероприятий в группах Facebook.

**Методы**:
- `run_events`: Запускает процесс публикации мероприятий.

**Параметры**:
- `d` (Driver): Экземпляр веб-драйвера.
- `group_file_paths` (list[str]): Список путей к файлам с информацией о группах.
- `no_video` (bool): Флаг, указывающий на отсутствие видео в мероприятиях.

**Примеры**:
```python
promoter:FacebookPromoter = FacebookPromoter(d, group_file_paths=filenames, no_video = True)
```

## Функции

### `time.sleep`

```python
time.sleep(7200)
```

**Описание**: Приостанавливает выполнение программы на заданное количество секунд.

**Параметры**:
- Время сна в секундах

**Примеры**:
```python
time.sleep(7200)
```

### `logger.debug`

```python
logger.debug(f"waikig up {time.strftime('%H:%M:%S')}",None,False)
logger.debug(f"going to sleep at {time.strftime('%H:%M:%S')}",None,False)
```

**Описание**: Используется для отладочного логирования.

**Параметры**:
- `Сообщение` (str): Строка сообщения для отладки.
- `*args`: Переменное число аргументов.
- `exc_info`: Дополнительная информация об исключении.

**Примеры**:
```python
logger.debug(f"waikig up {time.strftime('%H:%M:%S')}",None,False)
```

### `promoter.run_events`

```python
promoter.run_events(events_names = events_names, group_file_paths = filenames)
```

**Описание**: Запускает процесс публикации мероприятий в группах Facebook.

**Параметры**:
- `events_names` (list[str]): Список названий мероприятий для публикации.
- `group_file_paths` (list[str]): Список путей к файлам с информацией о группах.

**Примеры**:
```python
promoter.run_events(events_names = events_names, group_file_paths = filenames)
```

### `logger.info`

```python
logger.info("Campaign promotion interrupted.")
```

**Описание**: Используется для информационного логирования.

**Параметры**:
- `Сообщение` (str): Строка сообщения.
- `*args`: Переменное число аргументов.

**Примеры**:
```python
logger.info("Campaign promotion interrupted.")
```

## Обработка исключений

### `KeyboardInterrupt`

```python
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

**Описание**: Обрабатывает прерывание с клавиатуры (Ctrl+C), завершая выполнение программы.