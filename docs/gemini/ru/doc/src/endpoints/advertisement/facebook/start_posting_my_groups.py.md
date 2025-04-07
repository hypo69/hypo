# Модуль для отправки рекламных объявлений в группы Facebook

## Обзор

Модуль `start_posting_my_groups.py` предназначен для автоматической отправки рекламных объявлений в группы Facebook. Он использует веб-драйвер для взаимодействия с Facebook и модуль `FacebookPromoter` для управления кампаниями.

## Подробнее

Модуль инициализирует веб-драйвер Chrome, заходит на сайт Facebook и запускает рекламные кампании, используя списки групп и кампаний, определенные в коде.

## Классы

### `FacebookPromoter`

**Описание**: Класс `FacebookPromoter` отвечает за управление рекламными кампаниями в Facebook. Он использует веб-драйвер для взаимодействия с Facebook и выполняет задачи, связанные с отправкой рекламных объявлений в группы.

**Методы**:

- `run_campaigns(campaigns: list, group_file_paths: list)`: Запускает рекламные кампании.

## Функции

В данном коде отсутствуют отдельные функции, но есть основной блок `try-except`, который выполняет запуск рекламных кампаний.

### Основной блок `try-except`

**Назначение**: Основной блок `try-except` предназначен для запуска и управления рекламными кампаниями до тех пор, пока не будет прерван пользователем.

**Как работает**:

1.  **Инициализация**:
    *   Создается инстанс драйвера `d` на основе браузера Chrome.
    *   Драйвер переходит по ссылке `https://facebook.com`.
    *   Определяются списки `filenames` (файлы с группами) и `campaigns` (названия кампаний).
    *   Создается инстанс `promoter` класса `FacebookPromoter`.
2.  **Цикл `while True`**:
    *   Внутри цикла вызывается метод `promoter.run_campaigns` с копиями списков `campaigns` и `filenames`.
    *   Цикл продолжается до тех пор, пока не произойдет прерывание с клавиатуры (`KeyboardInterrupt`).
3.  **Обработка исключений**:
    *   При возникновении исключения `KeyboardInterrupt` (например, при нажатии Ctrl+C) программа переходит в блок `except`.
    *   В блоке `except` фиксируется информация о прерывании кампании с использованием `logger.info`.

```
A
│
│ Создание инстанса драйвера и переход на Facebook
│
B
│
│ Инициализация списков групп и кампаний
│
C
│
│ Создание инстанса FacebookPromoter
│
D
│
│ Цикл: Запуск кампаний
│
E
│
│ Запуск promoter.run_campaigns
│
F
│
│ Прерывание KeyboardInterrupt
│
G
│
│ Логирование прерывания кампании
│
H
```

**Примеры**:

Пример запуска рекламной кампании:

```python
from src.webdriver.driver import Driver, Chrome
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.logger.logger import logger
import copy

d = Driver(Chrome)
d.get_url("https://facebook.com")

filenames:list = ['my_managed_groups.json']

campaigns:list = ['brands',
                  'mom_and_baby',
                  'pain',
                  'sport_and_activity',
                  'house',
                  'bags_backpacks_suitcases',
                  'man']

promoter = FacebookPromoter(d, group_file_paths = filenames, no_video = True)

try:
    promoter.run_campaigns(campaigns = copy.copy(campaigns), group_file_paths = filenames)
except KeyboardInterrupt as ex:
    logger.info("Campaign promotion interrupted.", ex, exc_info=True)