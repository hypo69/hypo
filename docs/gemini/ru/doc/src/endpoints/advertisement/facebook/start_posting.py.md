# src.endpoints.advertisement.facebook.start_posting.py

## Обзор

Модуль предназначен для автоматической отправки рекламных объявлений в группы Facebook. Он использует веб-драйвер для взаимодействия с Facebook и выполняет циклический запуск рекламных кампаний, выбирая группы из указанных файлов.

## Подорбней

Этот скрипт автоматизирует процесс публикации рекламных объявлений в группах Facebook. Он инициализирует веб-драйвер, выполняет вход на сайт Facebook и затем циклически запускает рекламные кампании. Кампании настраиваются через список файлов, содержащих информацию о группах, и список категорий кампаний. Скрипт предназначен для работы в долгосрочном режиме, автоматически повторяя запуск кампаний через заданный интервал времени.

## Классы

### `FacebookPromoter`

**Описание**: Класс, отвечающий за продвижение контента в Facebook.

**Методы**:
- `run_campaigns`: Запускает рекламные кампании.

**Параметры**:
- `d` (Driver): Экземпляр веб-драйвера.
- `group_file_paths` (list[str]): Список путей к файлам, содержащим информацию о группах.
- `no_video` (bool): Флаг, указывающий на отсутствие видео в рекламных материалах.

**Примеры**
```python
from src.webdriver.driver import Driver, Chrome
from src.endpoints.advertisement.facebook import FacebookPromoter

d = Driver(Chrome)
d.get_url(r"https://facebook.com")

filenames:list[str] = [
                        "usa.json",
                        "he_ils.json",
                        "ru_ils.json",
                        "katia_homepage.json",
                        "my_managed_groups.json",
          
                        ]
promoter:FacebookPromoter = FacebookPromoter(d, group_file_paths=filenames, no_video = True)
```

## Функции

### `time.sleep`

```python
time.sleep(180)
```

**Описание**: Приостанавливает выполнение программы на указанное количество секунд.

**Параметры**:
- Количество секунд для приостановки выполнения.

**Примеры**:
```python
import time
time.sleep(180) # Приостанавливает выполнение программы на 180 секунд.
```

### `logger.info`

```python
logger.info("Campaign promotion interrupted.")
```

**Описание**: Регистрирует информационное сообщение в лог.

**Параметры**:
- Сообщение для записи в лог.

**Примеры**:
```python
from src.logger.logger import logger
logger.info("Campaign promotion interrupted.") # Записывает информационное сообщение о прерывании кампании.
```