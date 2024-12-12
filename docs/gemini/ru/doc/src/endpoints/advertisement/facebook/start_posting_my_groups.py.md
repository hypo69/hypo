# Модуль `start_posting_my_groups.py`

## Обзор

Модуль предназначен для автоматической отправки рекламных объявлений в группы Facebook (предположительно, в свои группы). Он использует WebDriver для управления браузером и FacebookPromoter для выполнения продвижения.

## Содержание

- [Обзор](#обзор)
- [Константы](#константы)
- [Импорты](#импорты)
- [Переменные](#переменные)
- [Классы](#классы)
- [Функции](#функции)
- [Основной блок](#основной-блок)

## Константы

- `MODE`: Режим работы скрипта, по умолчанию установлен в `dev`.

## Импорты

```python
import header
import copy
from src.webdriver.driver import Driver, Chrome
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.logger.logger import logger
```

## Переменные

- `d`: Экземпляр класса `Driver` с драйвером Chrome.
- `filenames`: Список строк, содержащих имена файлов со списками групп.
- `campaigns`: Список строк, содержащих имена кампаний.
- `promoter`: Экземпляр класса `FacebookPromoter` для продвижения объявлений.

## Классы

### `Driver`

**Описание**: Класс для управления веб-драйвером.

**Методы**:
- `get_url`: Переходит по указанному URL.

### `Chrome`

**Описание**: Класс для создания экземпляра браузера Chrome.

### `FacebookPromoter`

**Описание**: Класс для управления процессом продвижения в Facebook.

**Методы**:
- `run_campaigns`: Запускает продвижение для заданных кампаний.

## Функции

В данном файле нет пользовательских функций, только встроенные методы классов.

## Основной блок

```python
d = Driver(Chrome)
d.get_url(r"https://facebook.com")

filenames: list = ['my_managed_groups.json', ]

campaigns: list = ['brands',
                  'mom_and_baby',
                  'pain',
                  'sport_and_activity',
                  'house',
                  'bags_backpacks_suitcases',
                  'man']

promoter = FacebookPromoter(d, group_file_paths=filenames, no_video=True)

try:
    while True:
        promoter.run_campaigns(campaigns=copy.copy(campaigns), group_file_paths=filenames)
        ...

except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

**Описание**:

1.  Инициализирует драйвер Chrome и открывает Facebook.
2.  Определяет список файлов со списком групп и список кампаний для продвижения.
3.  Создаёт экземпляр `FacebookPromoter`.
4.  Запускает бесконечный цикл, в котором:
    *   Запускаются кампании.
    *   Многоточие (заполнитель для дальнейшей логики).
5.  Обрабатывает прерывание с клавиатуры, чтобы корректно завершить работу скрипта.

**Параметры**:
    -   `d` (Driver): Экземпляр класса `Driver`.
    -   `filenames` (list): Список строк, содержащих имена файлов со списками групп.
    -   `campaigns` (list): Список строк, содержащих имена кампаний.
    -   `promoter` (FacebookPromoter): Экземпляр класса `FacebookPromoter` для продвижения объявлений.

**Вызывает исключения**:
- `KeyboardInterrupt`: Прерывание выполнения скрипта пользователем с клавиатуры.