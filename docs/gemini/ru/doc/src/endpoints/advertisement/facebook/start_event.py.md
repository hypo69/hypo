# Модуль `src.endpoints.advertisement.facebook.start_event`

## Обзор

Модуль предназначен для отправки рекламных мероприятий в группы Facebook. Он использует WebDriver для взаимодействия с Facebook и загружает настройки групп из JSON файлов.

## Оглавление

- [Обзор](#обзор)
- [Константы](#константы)
- [Импорты](#импорты)
- [Переменные](#переменные)
- [Классы](#классы)
- [Функции](#функции)

## Константы

### `MODE`

**Описание**: Режим работы модуля. В данном случае установлен в 'dev'.

## Импорты

### `from math import log`

Импортируется функция `log` из модуля `math`.

### `import header`

Импортируется модуль `header`.

### `import time`

Импортируется модуль `time`.

### `from src.utils.jjson import j_loads`

Импортируется функция `j_loads` из модуля `src.utils.jjson`.

### `from src.webdriver.driver import Driver, Chrome`

Импортируются классы `Driver` и `Chrome` из модуля `src.webdriver.driver`.

### `from src.endpoints.advertisement.facebook import FacebookPromoter`

Импортируется класс `FacebookPromoter` из модуля `src.endpoints.advertisement.facebook`.

### `from src.logger.logger import logger`

Импортируется объект `logger` из модуля `src.logger.logger`.

## Переменные

### `d`

**Описание**: Экземпляр класса `Driver` с использованием `Chrome` в качестве браузера. Открывает URL `https://facebook.com`.

### `filenames`

**Описание**: Список путей к JSON файлам, содержащим настройки групп Facebook.

### `excluded_filenames`

**Описание**: Список файлов, которые будут исключены из обработки.

### `events_names`

**Описание**: Список названий рекламных мероприятий.

### `promoter`

**Описание**: Экземпляр класса `FacebookPromoter` для выполнения рекламных мероприятий.

## Классы

В данном файле классы не определены.

## Функции

В данном файле функции не определены.

## Основной блок

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

**Описание**: Основной блок кода, который выполняет следующие действия:

1.  Запускает бесконечный цикл `while True`:
    -   Выводит сообщение о начале работы в лог.
    -   Вызывает метод `run_events` объекта `promoter` для запуска рекламных мероприятий.
    -   Выводит сообщение о переходе в режим ожидания в лог.
    -   Приостанавливает выполнение на 7200 секунд (2 часа).

2.  Обрабатывает исключение `KeyboardInterrupt` (прерывание с клавиатуры):
    -   Выводит сообщение об остановке рекламной кампании в лог.