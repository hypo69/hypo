# Модуль `hypotez/src/endpoints/advertisement/facebook/start_posting.py`

## Обзор

Модуль `start_posting.py` отвечает за автоматическую публикацию рекламных объявлений в группы Facebook.  Он использует драйвер для взаимодействия с браузером, а также класс `FacebookPromoter` для управления рекламными кампаниями.  Модуль повторяет циклический запуск кампаний с заданным интервалом.


## Переменные

### `MODE`

**Описание**:  Строковая константа, указывающая режим работы (например, 'dev' или 'prod').

### `filenames`

**Описание**: Список путей к файлам с данными о целевых группах Facebook.

### `excluded_filenames`

**Описание**: Список исключаемых файлов из списка `filenames`.

### `campaigns`

**Описание**: Список названий рекламных кампаний.

### `promoter`

**Описание**: Экземпляр класса `FacebookPromoter`, используемый для запуска кампаний.


## Классы

Не определены.


## Функции

Не определены.


## Использование


```python
from src.webdriver.driver import Driver, Chrome
from src.endpoints.advertisement.facebook import FacebookPromoter
from src.logger.logger import logger
import time
import copy
import header


# ... (Инициализация драйвера и других необходимых переменных) ...

promoter: FacebookPromoter = FacebookPromoter(d, group_file_paths=filenames, no_video = True)

try:
    while True:
        promoter.run_campaigns(campaigns=copy.copy(campaigns), group_file_paths=filenames)
        print(f"Going sleep {time.localtime()}")
        time.sleep(180)
        # ... (Дополнительные действия в цикле) ...
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

**Описание использования:** Код демонстрирует инициализацию объекта `FacebookPromoter` и запуск циклического выполнения метода `run_campaigns`. Обработка `KeyboardInterrupt` позволяет корректно остановить программу при прерывании.

**Обратите внимание:** Не хватает импорта `math` , но он не используется. Также `d` объявляется но не используется.

**Важно:**  Для корректной работы модуля необходимы:

- Подключение к драйверу `Driver` и `Chrome`.
- Наличие класса `FacebookPromoter`.
- Функция `run_campaigns` в классе `FacebookPromoter`.
- Доступ к файлам с данными в `filenames`.
- Наличие логгера `logger`.

## Обрабатываемые исключения

### `KeyboardInterrupt`

**Описание**: Обработка прерывания выполнения программы через Ctrl+C. Выводит сообщение в логгер.
```
```