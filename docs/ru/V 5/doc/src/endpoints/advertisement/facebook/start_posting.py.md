# Модуль запуска постинга в Facebook

## Обзор

Модуль `start_posting.py` предназначен для автоматической публикации рекламных объявлений в группах Facebook. Он использует веб-драйвер для доступа к Facebook и класс `FacebookPromoter` для управления процессом публикации.

## Подробней

Этот модуль является частью системы автоматизации маркетинга `hypotez`. Он предназначен для увеличения охвата целевой аудитории через социальную сеть Facebook. Код выполняет следующие задачи:

- Инициализирует веб-драйвер для взаимодействия с Facebook.
- Загружает конфигурации групп и рекламных кампаний из файлов.
- Запускает рекламные кампании, публикуя объявления в выбранных группах.
- Обеспечивает непрерывную работу процесса публикации с заданными интервалами.

## Классы

### `FacebookPromoter`

**Описание**: Класс `FacebookPromoter` отвечает за управление процессом публикации рекламных объявлений в группах Facebook.

 **Как работает класс**:
   Этот класс использует веб-драйвер для навигации по сайту Facebook, поиска групп и публикации объявлений. Он также управляет файлами конфигурации групп и рекламных кампаний.

**Методы**:
- `run_campaigns`: Запускает рекламные кампании.

   **Параметры**:
   - `campaigns` (list): Список названий рекламных кампаний для запуска.
   - `group_file_paths` (list): Список путей к файлам, содержащим информацию о группах для публикации.

## Функции

### `Driver`

```python
d = Driver(Chrome)
```

 **Как работает функция**:
   Создает экземпляр веб-драйвера Chrome для автоматизации действий в браузере.

### `get_url`

```python
d.get_url(r"https://facebook.com")
```

 **Как работает функция**:
   Открывает указанный URL (в данном случае, главную страницу Facebook) в браузере, управляемом веб-драйвером.

### `FacebookPromoter`

```python
promoter:FacebookPromoter = FacebookPromoter(d, group_file_paths=filenames, no_video = True)
```

 **Как работает функция**:
   Создает экземпляр класса `FacebookPromoter`, передавая ему веб-драйвер, список файлов с группами и флаг, указывающий на отсутствие видео в объявлениях.

   **Параметры**:
   - `d`: Экземпляр веб-драйвера.
   - `group_file_paths`: Список путей к файлам, содержащим информацию о группах для публикации.
   - `no_video`: Флаг, указывающий на отсутствие видео в объявлениях.

### `run_campaigns`

```python
promoter.run_campaigns(campaigns = copy.copy(campaigns), group_file_paths = filenames)
```

 **Как работает функция**:
   Запускает рекламные кампании, используя переданные параметры.

   **Параметры**:
   - `campaigns`: Список названий рекламных кампаний для запуска.
   - `group_file_paths`: Список путей к файлам, содержащим информацию о группах для публикации.

### `time.sleep`

```python
time.sleep(180)
```

 **Как работает функция**:
   Приостанавливает выполнение программы на 180 секунд.

## Переменные

- `filenames` (list[str]): Список имен файлов, содержащих информацию о группах Facebook для публикации объявлений.
- `excluded_filenames` (list[str]): Список имен файлов, которые следует исключить из списка групп для публикации.
- `campaigns` (list): Список названий рекламных кампаний.
- `promoter` (FacebookPromoter): Экземпляр класса `FacebookPromoter`, используемый для управления процессом публикации.

## Обработка исключений

```python
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

**Описание**:
   Перехватывает исключение `KeyboardInterrupt`, которое возникает при прерывании программы пользователем (например, нажатием Ctrl+C). В случае прерывания выводит информационное сообщение в лог.

**Как работает функция**:
   При возникновении исключения `KeyboardInterrupt`, программа записывает сообщение "Campaign promotion interrupted." в лог с использованием модуля `logger`.

## Примеры

Пример запуска процесса публикации рекламных объявлений:

```python
from src.webdriver.driver import Driver, Chrome
from src.endpoints.advertisement.facebook import FacebookPromoter
import time
import copy
from src.logger.logger import logger

d = Driver(Chrome)
d.get_url("https://facebook.com")

filenames = ["usa.json", "he_ils.json", "ru_ils.json"]
campaigns = ['brands', 'mom_and_baby', 'pain']

promoter = FacebookPromoter(d, group_file_paths=filenames, no_video=True)

try:
    while True:
        promoter.run_campaigns(campaigns=copy.copy(campaigns), group_file_paths=filenames)
        print(f"Going sleep {time.localtime()}")
        time.sleep(180)
except KeyboardInterrupt as ex:
    logger.info("Campaign promotion interrupted.", ex, exc_info = True)