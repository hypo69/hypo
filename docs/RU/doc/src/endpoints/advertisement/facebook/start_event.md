# Модуль hypotez/src/endpoints/advertisement/facebook/start_event.py

## Обзор

Модуль `start_event.py` отвечает за отправку рекламных мероприятий в группы Facebook. Он использует веб-драйвер для взаимодействия с Facebook и загружает данные о группах из JSON-файлов.  Модуль организует циклическую отправку мероприятий, используя `FacebookPromoter` и списки имен событий и путей к файлам.

## Импорты

```python
from math import log
import header
import time
from src.utils.jjson import j_loads
from src.webdriver.driver import Driver, Chrome
from src.endpoints.advertisement.facebook import FacebookPromoter
from src.logger import logger
```

## Переменные

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
events_names:list = ["choice_day_01_10"]
```

## Инициализация

```python
d = Driver(Chrome)
d.get_url(r"https://facebook.com")
promoter:FacebookPromoter = FacebookPromoter(d, group_file_paths=filenames, no_video = True)
```

## Функция `run` (неявная)

Хотя явных функций нет, модуль запускает цикл:

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


**Описание цикла:**

- Бесконечный цикл `while True`.
- `logger.debug()` записывает сообщения в лог.
- `promoter.run_events()` выполняет отправку мероприятий.
- `time.sleep(7200)` приостанавливает выполнение на 2 часа.
- Обработка `KeyboardInterrupt` для безопасного выхода из программы.


## Возможные ошибки

- `KeyboardInterrupt`:  Произойдет, если пользователь прервет выполнение программы с помощью комбинации клавиш.

## Зависимости

Этот модуль использует следующие зависимости:

- `header` (документация отсутствует)
- `j_loads` (из модуля `src.utils.jjson`)
- `Driver`, `Chrome` (из модуля `src.webdriver.driver`)
- `FacebookPromoter` (из модуля `src.endpoints.advertisement.facebook`)
- `logger` (из модуля `src.logger`)

## Дополнительные замечания

- Необходимо обеспечить наличие файлов JSON, указанных в `filenames`, в соответствующем каталоге.
- Необходимо иметь реализацию класса `FacebookPromoter`, отвечающего за отправку рекламных мероприятий в группы Facebook.
- Логирование (`logger`) должно быть настроено для записи сообщений.
-  Инициализация веб-драйвера (`Driver(Chrome)`) требует корректной установки драйвера Chrome.