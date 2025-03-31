# Модуль для отправки рекламных объявлений в группы Facebook

## Обзор

Модуль `src.endpoints.advertisement.facebook.start_posting_my_groups` предназначен для автоматической публикации рекламных объявлений в группах Facebook. Он использует веб-драйвер для управления браузером и взаимодействует с Facebook через класс `FacebookPromoter`. Модуль поддерживает запуск рекламных кампаний из списка, используя данные о группах из JSON-файлов.

## Подробней

Этот модуль является частью системы автоматизации рекламы в проекте `hypotez`. Он позволяет запускать рекламные кампании в Facebook, используя список групп, полученных из JSON-файлов. Модуль использует `FacebookPromoter` для управления процессом публикации и `Driver` для управления веб-браузером.

## Классы

### `FacebookPromoter`

**Описание**: Класс `FacebookPromoter` отвечает за автоматическую публикацию рекламных объявлений в группах Facebook.

**Как работает класс**:
Класс инициализируется драйвером веб-браузера, списком путей к файлам с информацией о группах и флагом, указывающим на необходимость публикации видео. Он предоставляет методы для запуска рекламных кампаний и обработки процесса публикации.

**Методы**:

- `run_campaigns`: Запускает рекламные кампании в Facebook.

## Функции

### Отсутствуют функции, определенные вне классов.

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

        
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

**Описание кода**:

1.  **Импорты**:
    *   `header`: Импорт модуля `header`.
    *   `copy`: Импорт модуля `copy` для создания копий объектов.
    *   `Driver`, `Chrome` из `src.webdriver.driver`: Импорт классов `Driver` и `Chrome` для управления веб-браузером.
    *   `FacebookPromoter` из `src.endpoints.advertisement.facebook.promoter`: Импорт класса `FacebookPromoter` для управления рекламными кампаниями.
    *   `logger` из `src.logger.logger`: Импорт модуля `logger` для логирования.

2.  **Инициализация драйвера**:

    *   `d = Driver(Chrome)`: Создание инстанса драйвера Chrome.
    *   `d.get_url(r"https://facebook.com")`: Открытие Facebook в браузере.

3.  **Настройка кампаний**:

    *   `filenames:list = ['my_managed_groups.json',]`: Список файлов, содержащих информацию о группах.
    *   `campaigns:list = ['brands', 'mom_and_baby', 'pain', 'sport_and_activity', 'house', 'bags_backpacks_suitcases', 'man']`: Список рекламных кампаний.

4.  **Инициализация промоутера**:

    *   `promoter = FacebookPromoter(d, group_file_paths=filenames, no_video=True)`: Создание инстанса `FacebookPromoter` с драйвером, списком файлов групп и флагом `no_video`.

5.  **Запуск кампаний**:

    *   `try`: Блок try-except для обработки исключений.
    *   `while True`: Бесконечный цикл для непрерывного запуска кампаний.
    *   `promoter.run_campaigns(campaigns=copy.copy(campaigns), group_file_paths=filenames)`: Запуск рекламных кампаний с копией списка кампаний и списком файлов групп.
    *   `...`: Индикатор продолжения кода (оставлен без изменений).

6.  **Обработка прерывания**:

    *   `except KeyboardInterrupt`: Обработка прерывания с клавиатуры (Ctrl+C).
    *   `logger.info("Campaign promotion interrupted.")`: Логирование сообщения о прерывании кампании.