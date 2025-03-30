# src.endpoints.advertisement.facebook.start_posting_katia.py

## Обзор

Модуль предназначен для отправки рекламных объявлений в группы Facebook. Он использует веб-драйвер для автоматизации действий в браузере и класс `FacebookPromoter` для управления процессом продвижения.

## Подробней

Этот скрипт автоматизирует процесс публикации рекламных объявлений в группах Facebook. Он инициализирует веб-драйвер Chrome, переходит на сайт Facebook, определяет список кампаний и файлов с группами, а затем запускает продвижение. Скрипт обрабатывает прерывание с клавиатуры для завершения процесса.

## Классы

### `FacebookPromoter`

**Описание**: Класс для управления процессом продвижения в Facebook.

**Методы**:
- `run_campaigns`: Запускает кампании продвижения.

**Параметры**:
- `d`: Объект веб-драйвера.
- `group_file_paths`: Список путей к файлам с информацией о группах.
- `no_video`: Флаг, указывающий на необходимость исключения видео из продвижения.

**Примеры**

```python
# Пример использования класса FacebookPromoter
from src.webdriver.driver import Driver, Chrome
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.logger.logger import logger

d = Driver(Chrome)
d.get_url(r"https://facebook.com")

filenames:list = ['katia_homepage.json',]
campaigns:list = [ 'sport_and_activity',
                  'bags_backpacks_suitcases',
                    'pain',
                    'brands',
                    'mom_and_baby',
                    'house',
                ]
promoter = FacebookPromoter(d, group_file_paths = filenames, no_video = False)

try:
    promoter.run_campaigns(campaigns)
except KeyboardInterrupt as ex:
    logger.info("Campaign promotion interrupted.", ex, exc_info = True)
```

## Функции

### `Driver`

```python
from src.webdriver.driver import Driver, Chrome
d = Driver(Chrome)
d.get_url(r"https://facebook.com")
```

**Описание**: Инициализирует веб-драйвер Chrome и открывает сайт Facebook.

**Параметры**:
- Отсутствуют явные параметры. Использует `Chrome` из `src.webdriver.driver`.

**Возвращает**:
- Отсутствует явное возвращаемое значение.

**Вызывает исключения**:
- Возможные исключения при инициализации и управлении веб-драйвером.

**Примеры**:

```python
from src.webdriver.driver import Driver, Chrome
d = Driver(Chrome)
d.get_url(r"https://facebook.com")
```

### `FacebookPromoter.run_campaigns`

```python
promoter = FacebookPromoter(d, group_file_paths = filenames, no_video = False)
try:
    promoter.run_campaigns(campaigns)
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

**Описание**: Запускает кампании продвижения в Facebook.

**Параметры**:
- `campaigns` (list): Список кампаний для запуска.

**Возвращает**:
- Отсутствует явное возвращаемое значение.

**Вызывает исключения**:
- `KeyboardInterrupt`: Возникает при прерывании с клавиатуры.
- Другие исключения, возникающие в процессе выполнения кампаний.

**Примеры**:

```python
promoter = FacebookPromoter(d, group_file_paths = filenames, no_video = False)
try:
    promoter.run_campaigns(campaigns)
except KeyboardInterrupt as ex:
    logger.info("Campaign promotion interrupted.", ex, exc_info = True)
```