```markdown
# Модуль `start_event`

## Обзор

Данный модуль отвечает за отправку рекламных мероприятий (events) в группы Facebook.  Он использует предопределенные файлы JSON с данными о группах и мероприятиях.  Модуль использует класс `FacebookPromoter` для управления процессом.  Запуск осуществляется в цикле, с периодическим повтором.

## Оглавление

- [Модуль `start_event`](#модуль-start-event)
- [Переменные](#переменные)
- [Импорты](#импорты)
- [Инициализация](#инициализация)
- [Переменные файлов](#переменные-файлов)
- [Переменные имен мероприятий](#переменные-имен-мероприятий)
- [Создание экземпляра FacebookPromoter](#создание-экземпляра-facebookpromoter)
- [Цикл](#цикл)
- [Обработка исключений](#обработка-исключений)


## Переменные

```python
MODE = 'development'
```

`MODE`: Строковая переменная, содержащая режим работы (`development`).

## Импорты

```python
from math import log
import header
import time
from src.utils.jjson import j_loads
from src.webdriver import Driver, Chrome
from src.endpoints.advertisement.facebook import FacebookPromoter
from src.logger import logger
```

Импортируются необходимые модули: `math`, `time`, `jjson`, `Driver`, `Chrome`, `FacebookPromoter`, `logger`.


## Инициализация

```python
d = Driver(Chrome)
d.get_url(r"https://facebook.com")
```

Создается экземпляр драйвера `Driver` с использованием браузера Chrome и устанавливается URL-адрес Facebook.


## Переменные файлов

```python
filenames:list[str] = [ "my_managed_groups.json",
                        "usa.json",
                        "he_il.json",
                        "ru_il.json",
                        "katia_homepage.json",
                        
                        "ru_usd.json",
                        "ger_en_eur.json",            
                        ]
excluded_filenames:list[str] = ["my_managed_groups.json",]
```

`filenames`: Список путей к файлам с данными о группах Facebook.
`excluded_filenames`: Список путей к файлам, которые будут исключены из процесса.


## Переменные имен мероприятий

```python
events_names:list = ["choice_day_01_10"]
```

`events_names`: Список имен мероприятий, которые будут отправлены.


## Создание экземпляра FacebookPromoter

```python
promoter:FacebookPromoter = FacebookPromoter(d, group_file_paths=filenames, no_video = True)
```

Создается экземпляр класса `FacebookPromoter` с предоставленными данными о файлах групп и параметром `no_video`.


## Цикл

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

Цикл `while True` выполняет следующие действия:
- Запись в лог текущего времени.
- Вызов метода `run_events` для отправки мероприятий.
- Запись в лог времени ожидания.
- Ожидание 7200 секунд (2 часа).
- Обработка исключения `KeyboardInterrupt` при прерывании.



## Обработка исключений

```python
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

В случае прерывания выполнения программы (например, нажатием Ctrl+C), записывается сообщение в лог.
```
