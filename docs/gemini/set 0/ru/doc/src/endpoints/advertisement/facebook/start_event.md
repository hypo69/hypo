# Модуль hypotez/src/endpoints/advertisement/facebook/start_event.py

## Обзор

Модуль `start_event.py` отвечает за отправку рекламных мероприятий в группы Facebook. Он использует драйвер Chrome для авторизации на Facebook и API для взаимодействия с группами.  Модуль настроен для работы с JSON-файлами, содержащими информацию о группах и мероприятиях. Программа циклически запускает мероприятия и засыпает на 2 часа.

## Конфигурация

* **MODE:** Строковая переменная, определяющая режим работы. В текущей реализации имеет значение 'dev'.
* **filenames:** Список путей к JSON-файлам, содержащим информацию о целевых группах Facebook.
* **excluded_filenames:** Список путей к JSON-файлам, которые необходимо исключить из обработки.
* **events_names:** Список названий мероприятий, которые необходимо запустить.

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

## Классы

### `FacebookPromoter`

* **Описание**:  Представлен в модуле `FacebookPromoter`.  Обеспечивает функциональность для запуска рекламных мероприятий в группах Facebook.

## Функции

### `run_events`

```python
def run_events(self, events_names: list, group_file_paths: list) -> None:
    """
    Args:
        events_names (list): Список названий мероприятий для запуска.
        group_file_paths (list): Список путей к JSON-файлам с данными о группах.

    Returns:
        None: Функция не возвращает значения.
    """
```

* **Описание**: Функция запускает выбранные рекламные мероприятия в указанных группах.  Детали реализации находятся в классе FacebookPromoter.

### Основной код

```python
d = Driver(Chrome)
d.get_url(r"https://facebook.com")

filenames:list[str] = [...]
excluded_filenames:list[str] = [...]
events_names:list = [...]


promoter:FacebookPromoter = FacebookPromoter(d, group_file_paths=filenames, no_video = True)

try:
    while True:
        logger.debug(f"Запуск в {time.strftime('%H:%M:%S')}",None,False)
        promoter.run_events(events_names = events_names, group_file_paths = filenames)
        logger.debug(f"Ожидание {time.strftime('%H:%M:%S')}",None,False)
        time.sleep(7200)
except KeyboardInterrupt:
    logger.info("Запуск рекламной кампании прерван.")
```

* **Описание**:  Основной цикл программы. Он запускает функцию `run_events`  для запуска рекламных мероприятий и ожидает 2 часа (`time.sleep(7200)`). Цикл продолжается до тех пор, пока не будет получен сигнал `KeyboardInterrupt`.


## Обработка исключений

Обработка `KeyboardInterrupt` позволяет корректно завершить работу программы при прерывании пользователя.

## Замечания

- Модуль предполагает наличие классов `Driver`, `Chrome`, `FacebookPromoter` и модулей `jjson` и `logger` в других частях проекта.
- Подробности реализации функциональности `FacebookPromoter` не раскрыты в этом файле, но предполагается, что он взаимодействует с API Facebook для выполнения заданных действий.
- JSON-файлы, используемые в этом коде, должны содержать информацию в соответствующем формате.
- Важно проверить корректность работы с веб-драйвером, особенно с учетом потенциальных задержек.