# Модуль для отправки рекламных объявлений в Facebook (Katia?)

## Обзор

Модуль `start_posting_katia.py` предназначен для автоматической отправки рекламных объявлений в группы Facebook с использованием веб-драйвера. В частности, используется класс `FacebookPromoter` для запуска рекламных кампаний на основе заданных файлов конфигурации и списка кампаний.

## Подробнее

Этот модуль является частью системы автоматизации размещения рекламы в Facebook. Он использует `FacebookPromoter` для управления процессом размещения объявлений в группах. Модуль настраивает веб-драйвер Chrome, получает URL Facebook и запускает рекламные кампании, определенные в списке `campaigns`.

## Классы

### `FacebookPromoter`

**Описание**: Класс `FacebookPromoter` предназначен для автоматизации процесса размещения рекламных объявлений в группах Facebook.

**Принцип работы**:

Класс инициализируется драйвером веб-браузера, списком путей к файлам с данными групп и флагом, указывающим на необходимость размещения видео. Он предоставляет метод `run_campaigns` для запуска рекламных кампаний на основе списка кампаний.

**Методы**:

- `run_campaigns(campaigns: list)`: Запускает рекламные кампании для каждой кампании в списке.

## Функции

### Отсутствуют

В данном коде функции отсутствуют. Код содержит только импорт модулей, инициализацию драйвера и запуск рекламных кампаний через класс `FacebookPromoter`.

## Пример использования

```python
from src.webdriver.driver import Driver, Chrome
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.logger.logger import logger

d = Driver(Chrome)
d.get_url(r"https://facebook.com")

filenames: list = ['katia_homepage.json', ]
campaigns: list = [
    'sport_and_activity',
    'bags_backpacks_suitcases',
    'pain',
    'brands',
    'mom_and_baby',
    'house',
]
promoter = FacebookPromoter(d, group_file_paths=filenames, no_video=False)

try:
    promoter.run_campaigns(campaigns)
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

В этом примере создается экземпляр драйвера Chrome, открывается Facebook, инициализируется `FacebookPromoter` с указанием файлов групп и списка кампаний, а затем запускаются кампании. Если процесс прерывается пользователем, регистрируется соответствующее сообщение.