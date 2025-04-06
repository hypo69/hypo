# Модуль отправки рекламных объявлений в Facebook (Katia?)

## Обзор

Модуль предназначен для автоматической отправки рекламных объявлений в группы Facebook. Он использует веб-драйвер для взаимодействия с сайтом Facebook и выполняет заданные рекламные кампании.

## Подробнее

Этот модуль является частью системы автоматизации рекламных кампаний в Facebook. Он использует класс `FacebookPromoter` для выполнения основных операций по размещению рекламы в группах. Файл конфигурации содержит пути к файлам с описаниями групп Facebook и список кампаний, которые необходимо выполнить. Модуль обеспечивает возможность прерывания выполнения кампании с помощью `KeyboardInterrupt`.

## Классы

### `FacebookPromoter`

**Описание**: Класс, отвечающий за размещение рекламных объявлений в группах Facebook.

**Методы**:
- `run_campaigns(campaigns: list)`: Запускает указанные рекламные кампании.

## Функции

В данном коде нет явно определенных функций, но используется класс `FacebookPromoter` с методом `run_campaigns`.

### `run_campaigns`

```python
def run_campaigns(campaigns: list):
    """Запускает указанные рекламные кампании.

    Args:
        campaigns (list): Список названий кампаний для запуска.

    Raises:
        Exception: Если возникает ошибка во время выполнения кампании.

    """
    ...
```

**Назначение**: Запускает рекламные кампании, определенные в списке `campaigns`.

**Параметры**:
- `campaigns` (list): Список строк, представляющих названия кампаний, которые необходимо запустить.

**Как работает функция**:

1.  Функция `run_campaigns` принимает список названий кампаний (`campaigns`).
2.  Перебирает кампании в списке и выполняет необходимые действия для каждой кампании (подробности реализации находятся в классе `FacebookPromoter`).

**Примеры**:

```python
promoter.run_campaigns(['sport_and_activity', 'bags_backpacks_suitcases'])
```

## Код

```python
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

**Описание кода**:

1.  **Импорт необходимых модулей**:
    *   `header`: Импорт модуля `header`.
    *   `src.webdriver.driver.Driver` и `src.webdriver.driver.Chrome`: Импорт классов для управления веб-драйвером Chrome.
    *   `src.endpoints.advertisement.facebook.promoter.FacebookPromoter`: Импорт класса для управления рекламными кампаниями в Facebook.
    *   `src.logger.logger.logger`: Импорт модуля для логирования событий.

2.  **Инициализация веб-драйвера**:
    *   `d = Driver(Chrome)`: Создается экземпляр веб-драйвера Chrome.
    *   `d.get_url(r"https://facebook.com")`: Открывается сайт Facebook в браузере.

3.  **Определение параметров кампании**:
    *   `filenames:list = ['katia_homepage.json',]`: Список файлов конфигурации, содержащих информацию о группах Facebook.
    *   `campaigns:list = [...]`: Список названий рекламных кампаний для запуска.

4.  **Создание экземпляра `FacebookPromoter`**:
    *   `promoter = FacebookPromoter(d, group_file_paths=filenames, no_video=False)`: Создается экземпляр класса `FacebookPromoter` с передачей веб-драйвера, списка файлов конфигурации и флага `no_video`.

5.  **Запуск рекламных кампаний**:
    *   `try...except KeyboardInterrupt`: Блок try-except для обработки прерывания выполнения кампании с клавиатуры.
    *   `promoter.run_campaigns(campaigns)`: Запускаются рекламные кампании.
    *   `logger.info("Campaign promotion interrupted.")`: В случае прерывания кампании выводится сообщение в лог.

**ASCII Flowchart**:

```
    Инициализация веб-драйвера (Chrome)
    |
    Открытие Facebook в браузере
    |
    Определение файлов конфигурации и списка кампаний
    |
    Создание экземпляра FacebookPromoter
    |
    Запуск рекламных кампаний (try)
    |
    Обработка прерывания (except KeyboardInterrupt)
    |
    Вывод сообщения о прерывании в лог