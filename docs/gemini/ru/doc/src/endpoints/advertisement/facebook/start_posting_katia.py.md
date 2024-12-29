# Модуль `start_posting_katia.py`

## Обзор

Модуль предназначен для запуска процесса публикации рекламных объявлений в группы Facebook с использованием настроек, специфичных для пользователя Katia. Он использует веб-драйвер для автоматизации взаимодействия с Facebook и загружает конфигурации из JSON-файлов.

## Оглавление

1. [Обзор](#обзор)
2. [Импорты](#импорты)
3. [Переменные](#переменные)
4. [Инициализация `FacebookPromoter`](#инициализация-facebookpromoter)
5. [Запуск кампаний](#запуск-кампаний)
6. [Обработка прерывания](#обработка-прерывания)

## Импорты

Модуль импортирует следующие компоненты:

- `header`: Неизвестный модуль, предположительно содержащий общие заголовки или настройки.
- `Driver`, `Chrome` из `src.webdriver.driver`: Классы для управления веб-драйвером Chrome.
- `FacebookPromoter` из `src.endpoints.advertisement.facebook.promoter`: Класс для управления рекламными кампаниями в Facebook.
- `logger` из `src.logger.logger`: Модуль для ведения журнала событий.

## Переменные

- `d`: Экземпляр класса `Driver` с настроенным драйвером Chrome для взаимодействия с веб-страницами.
- `filenames`: Список строк, содержащий имена файлов JSON с настройками групп для публикации.
- `campaigns`: Список строк, содержащий названия кампаний для запуска.
- `promoter`: Экземпляр класса `FacebookPromoter`, настроенный для запуска рекламных кампаний.

## Инициализация `FacebookPromoter`

Создается экземпляр класса `FacebookPromoter` со следующими параметрами:

- `d` (экземпляр `Driver`): Веб-драйвер.
- `group_file_paths`: Список файлов с настройками групп.
- `no_video`: Отключение публикации видео.

## Запуск кампаний

Метод `run_campaigns` экземпляра `promoter` запускается со списком кампаний `campaigns` в качестве аргумента. Это запускает процесс публикации объявлений в соответствующих группах Facebook.

## Обработка прерывания

В случае прерывания процесса (например, нажатием `Ctrl+C`), будет поймано исключение `KeyboardInterrupt`, и в журнал будет записано сообщение "Campaign promotion interrupted.".

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.endpoints.advertisement.facebook
	:platform: Windows, Unix
	:synopsis: Отправка рекламных объявлений в группы фейсбук (Katia?)
"""
import header 
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
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```