# Модуль hypotez/src/endpoints/advertisement/facebook/start_event.py

## Обзор

Модуль `start_event.py` отвечает за запуск рекламной кампании в группах Facebook. Он загружает данные о группах из JSON-файлов, подключается к Facebook и отправляет заданные события в указанные группы.  Модуль использует класс `FacebookPromoter` для взаимодействия с Facebook API. Процесс повторяется циклически с заданным интервалом времени.


## Конфигурация

* `MODE`: Устанавливает режим работы (например, 'dev').  Значение по умолчанию: 'dev'.

* `filenames`: Список путей к JSON-файлам, содержащим данные о группах Facebook.

* `excluded_filenames`: Список путей к JSON-файлам, которые следует исключить из обработки.

* `events_names`: Список имен событий, которые нужно отправить.


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

## Классы и Функции

### `FacebookPromoter`

**Описание**: Класс `FacebookPromoter` реализует логику взаимодействия с Facebook для отправки событий.

**Параметры**:

* `d`: Экземпляр класса `Driver`, используемый для взаимодействия с браузером.
* `group_file_paths`: Список путей к JSON-файлам, содержащим данные о группах.
* `no_video`:  Флаг, определяющий нужно ли запускать видео в группах Facebook.


**Методы**:

* `run_events(events_names, group_file_paths)`: Метод для запуска рекламных событий в указанных группах.  Подробности реализованы в классе FacebookPromoter.

### `Driver` (используется, но не документирован в этом модуле)

**Описание**: Класс `Driver` управляет браузерным сессией и взаимодействием с веб-сайтом.


### `Chrome` (используется, но не документирован в этом модуле)

**Описание**:  По-видимому, представляет конфигурацию драйвера браузера Chrome.


## Функции

### `start_event`


**Описание**: Точка входа для запуска рекламной кампании.


**Параметры**:

*  Не принимает никаких параметров.



**Вызывает исключения**:

* `KeyboardInterrupt`: Прерывание программы пользователем.



##  Обработка ошибок

```python
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

## Пример использования

```python
promoter = FacebookPromoter(d, group_file_paths=filenames, no_video = True)

try:
    while True:
        logger.debug(f"waikig up {time.strftime(\'%H:%M:%S\')}",None,False)
        promoter.run_events(events_names = events_names, group_file_paths = filenames)
        logger.debug(f"going to sleep at {time.strftime(\'%H:%M:%S\')}",None,False)
        time.sleep(7200)
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

**Описание примера:**  Код показывает использование `FacebookPromoter` в бесконечном цикле, показывающем запуск и остановку.


```