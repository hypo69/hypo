# Модуль для отправки рекламных объявлений в группы Facebook

## Обзор

Модуль `start_posting_my_groups.py` предназначен для автоматической отправки рекламных объявлений в группы Facebook. Он использует веб-драйвер для взаимодействия с Facebook и модуль `FacebookPromoter` для управления кампаниями и группами.

## Подробнее

Этот модуль является частью системы автоматизации рекламы в Facebook. Он запускает рекламные кампании, используя список групп и рекламных материалов, определенных в файлах конфигурации. Модуль предназначен для работы в режиме бесконечного цикла, пока не будет прерван пользователем.

## Классы

В данном модуле напрямую классы не определены, но используется класс `FacebookPromoter` из модуля `src.endpoints.advertisement.facebook.promoter`.

### `FacebookPromoter`

**Описание**: Класс `FacebookPromoter` управляет процессом продвижения рекламных кампаний в Facebook. Он инициализируется веб-драйвером, путями к файлам с группами и флагом, указывающим на отсутствие видео в рекламных материалах.

**Принцип работы**:

Класс `FacebookPromoter` выполняет следующие действия:

1.  Загружает данные о группах из файлов конфигурации.
2.  Авторизуется в Facebook с использованием веб-драйвера.
3.  Выбирает группы для публикации рекламных объявлений.
4.  Публикует рекламные объявления в выбранных группах.
5.  Повторяет процесс для каждой кампании и группы.

**Методы**:

-   `run_campaigns`: Запускает рекламные кампании.

## Функции

В данном модуле нет явно определенных функций, но используется класс `FacebookPromoter` с методом `run_campaigns`.

### `FacebookPromoter.run_campaigns`

```python
def run_campaigns(campaigns: list, group_file_paths: list):
    """ Запускает рекламные кампании в Facebook.

    Args:
        campaigns (list): Список названий кампаний для запуска.
        group_file_paths (list): Список путей к файлам с информацией о группах.

    Raises:
        Exception: Если возникает ошибка во время выполнения кампании.
    """
    ...
```

**Назначение**: Запускает рекламные кампании, перебирая список кампаний и пути к файлам групп.

**Параметры**:

*   `campaigns` (list): Список названий кампаний для запуска.
*   `group_file_paths` (list): Список путей к файлам с информацией о группах.

**Как работает функция**:

1.  Функция принимает список кампаний и список путей к файлам с группами.
2.  Внутри функции происходит перебор по всем кампаниям и группам, указанным в файлах конфигурации.
3.  Для каждой группы выполняется публикация рекламного объявления.

```
Запуск кампаний
│
├───Копирование списка кампаний
│
└───Запуск промоутера для каждой кампании и группы
```

**Примеры**:

```python
promoter.run_campaigns(campaigns=['brands', 'mom_and_baby'], group_file_paths=['my_managed_groups.json'])
```

## Переменные

*   `d`: Инстанс класса `Driver` для управления веб-драйвером (Chrome).
*   `filenames`: Список файлов, содержащих информацию о группах.
*   `campaigns`: Список кампаний для запуска.
*   `promoter`: Инстанс класса `FacebookPromoter` для управления рекламными кампаниями.

## Код

```python
import header 
import copy
from src.webdriver.driver import Driver, Chrome
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.logger.logger import logger

d = Driver(Chrome)
d.get_url(r"https://facebook.com")

filenames:list = ['my_managed_groups.json',]  

campaigns:list = ['brands',
                  'mom_and_baby',
                  'pain',
                  'sport_and_activity',
                  'house',
                  'bags_backpacks_suitcases',
                  'man']

promoter = FacebookPromoter(d, group_file_paths = filenames, no_video = True)

try:
    while True:
        
        promoter.run_campaigns(campaigns = copy.copy(campaigns), group_file_paths = filenames)
        ...

        
except KeyboardInterrupt as ex:
    logger.info("Campaign promotion interrupted.")
```

**Объяснение кода**:

1.  Импортируются необходимые модули и классы:
    *   `header` (назначение неизвестно, требуется дополнительный анализ).
    *   `copy` для создания копий списков.
    *   `Driver` и `Chrome` из `src.webdriver.driver` для управления веб-драйвером.
    *   `FacebookPromoter` из `src.endpoints.advertisement.facebook.promoter` для управления рекламными кампаниями.
    *   `logger` из `src.logger.logger` для логирования.
2.  Создается инстанс веб-драйвера `Driver` с использованием браузера Chrome.
3.  Выполняется переход по URL `https://facebook.com` с использованием веб-драйвера.
4.  Определяется список файлов `filenames`, содержащих информацию о группах.
5.  Определяется список кампаний `campaigns` для запуска.
6.  Создается инстанс класса `FacebookPromoter` с передачей веб-драйвера, списка файлов с группами и флага `no_video`.
7.  В бесконечном цикле `while True` запускаются рекламные кампании с использованием метода `run_campaigns` класса `FacebookPromoter`. Для каждой итерации цикла создается копия списка кампаний с помощью `copy.copy(campaigns)`.
8.  Обрабатывается исключение `KeyboardInterrupt`, которое возникает при прерывании работы программы пользователем (например, нажатием Ctrl+C). В случае возникновения исключения в лог выводится сообщение "Campaign promotion interrupted.".