# Модуль для отправки рекламных объявлений в группы Facebook

## Обзор

Модуль `start_posting_my_groups.py` предназначен для автоматической отправки рекламных объявлений в группы Facebook. Он использует веб-драйвер для управления браузером и выполняет задачи по размещению рекламы, определенные в других модулях проекта.

## Подробней

Этот модуль является частью системы автоматизации маркетинга в Facebook. Он запускает рекламные кампании, используя список групп и рекламные материалы, определенные в файлах конфигурации. Модуль предназначен для работы в цикле, автоматически повторяя запуск кампаний до тех пор, пока не будет прерван вручную.

## Классы

### `FacebookPromoter`

**Описание**: Класс `FacebookPromoter` управляет процессом размещения рекламы в группах Facebook.

**Принцип работы**:
Класс инициализируется драйвером веб-браузера, списком файлов с информацией о группах и флагом, указывающим на необходимость исключения видео из рекламных материалов. Основной метод `run_campaigns` выполняет итерацию по списку кампаний и файлов групп, отправляя рекламные объявления в соответствующие группы.

**Методы**:

- `run_campaigns(campaigns: list, group_file_paths: list)`: Запускает рекламные кампании в указанных группах.

## Функции

### Отсутствуют

В данном файле функции отсутствуют, вся основная логика реализована в классе `FacebookPromoter`.

## Как работает код:

1.  **Инициализация**:
    *   Импортируются необходимые модули, такие как `header`, `copy`, `Driver`, `Chrome`, `FacebookPromoter` и `logger`.
    *   Создается экземпляр драйвера `Chrome` для управления браузером.
    *   Драйвер переходит на сайт `facebook.com`.
    *   Определяются списки файлов (`filenames`) и кампаний (`campaigns`), которые будут использоваться для продвижения.
    *   Создается экземпляр класса `FacebookPromoter` с передачей ему драйвера, списка файлов с группами и флага `no_video`.

2.  **Запуск рекламных кампаний**:
    *   Код входит в бесконечный цикл `while True`.
    *   Внутри цикла вызывается метод `run_campaigns` объекта `promoter` с передачей копии списка кампаний и списка файлов с группами.
    *   Цикл продолжается до тех пор, пока не будет прерван пользователем (например, нажатием `Ctrl+C`).

3.  **Обработка прерывания**:
    *   Если пользователь прерывает выполнение программы (нажатием `Ctrl+C`), возникает исключение `KeyboardInterrupt`.
    *   Блок `except` перехватывает это исключение и записывает сообщение "Campaign promotion interrupted." в лог.

```
Начало работы
     |
     | Инициализация драйвера, списков файлов и кампаний, FacebookPromoter
     |
     V
Запуск цикла рекламных кампаний (while True)
     |
     | Вызов promoter.run_campaigns(copy.copy(campaigns), filenames)
     |
     V
Завершение при KeyboardInterrupt
     |
     | Запись сообщения в лог
     |
Конец
```

## Примеры

Пример запуска модуля:

```python
import header
import copy
from src.webdriver.driver import Driver, Chrome
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.logger.logger import logger

d = Driver(Chrome)
d.get_url(r"https://facebook.com")

filenames: list = ['my_managed_groups.json']

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
        # <инструкция для модели gemini:Ожидание или условия для прерывания цикла>
except KeyboardInterrupt as ex:
    logger.info("Campaign promotion interrupted.", ex, exc_info=True)