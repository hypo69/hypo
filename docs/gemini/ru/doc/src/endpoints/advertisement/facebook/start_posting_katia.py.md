# Модуль `start_posting_katia.py`

## Обзор

Модуль предназначен для автоматической отправки рекламных объявлений в группы Facebook, используя заданные конфигурации. Модуль использует `FacebookPromoter` для управления процессом продвижения и `Driver` для управления браузером.

## Оглавление

1. [Обзор](#обзор)
2. [Импорты](#импорты)
3. [Переменные](#переменные)
4. [Инициализация](#инициализация)
5. [Обработка исключений](#обработка-исключений)

## Импорты

В данном разделе перечислены все импортированные модули и классы, используемые в коде.

```python
import header
from src.webdriver.driver import Driver, Chrome
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.logger.logger import logger
```

## Переменные

В данном разделе перечислены основные переменные, используемые в модуле.

- `MODE` (str): Режим работы, по умолчанию установлен в `'dev'`.
- `filenames` (list): Список файлов конфигурации для групп.
- `campaigns` (list): Список кампаний, которые нужно запустить.
- `d` (Driver): Экземпляр драйвера браузера `Chrome`.
- `promoter` (FacebookPromoter): Экземпляр класса `FacebookPromoter`, используемый для управления процессом публикации.

## Инициализация

В данном разделе описывается инициализация основных компонентов, таких как драйвер браузера и промоутер.

```python
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
```
Здесь:
- Инициализируется драйвер браузера Chrome и переходит на страницу Facebook.
- Создается список файлов конфигурации для групп `filenames` и список кампаний `campaigns`.
- Создается экземпляр класса `FacebookPromoter` с настроенным драйвером и параметрами кампании.

## Обработка исключений

В данном разделе описывается блок обработки исключений.

```python
try:
    promoter.run_campaigns(campaigns)
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

- Пытается запустить кампании с помощью `promoter.run_campaigns(campaigns)`.
- Если возникает исключение `KeyboardInterrupt` (например, при нажатии Ctrl+C), то регистрируется сообщение об прерывании продвижения кампании.