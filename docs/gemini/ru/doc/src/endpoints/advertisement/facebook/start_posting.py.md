# Модуль `start_posting.py`

## Обзор

Модуль `start_posting.py` предназначен для автоматической публикации рекламных объявлений в группы Facebook. Он использует веб-драйвер для управления браузером, загружает данные о группах из JSON-файлов и выполняет рекламные кампании.

## Содержание

1. [Обзор](#обзор)
2. [Импорты](#импорты)
3. [Переменные](#переменные)
4. [Инициализация](#инициализация)
5. [Основной цикл](#основной-цикл)

## Импорты

```python
from math import log
import header
import time
import copy
from src.webdriver.driver import Driver, Chrome
from src.endpoints.advertisement.facebook import FacebookPromoter
from src.logger.logger import logger
```

- `math.log`: Используется для математических операций (хотя в коде не используется напрямую).
- `header`: Импортирует модуль `header` (его содержимое не показано в предоставленном коде).
- `time`: Используется для работы со временем, например, для задержек.
- `copy`: Используется для создания копий объектов, например, списков.
- `src.webdriver.driver.Driver`, `src.webdriver.driver.Chrome`: Классы для управления веб-драйвером.
- `src.endpoints.advertisement.facebook.FacebookPromoter`: Класс для управления рекламными кампаниями в Facebook.
- `src.logger.logger.logger`: Объект логгера для записи информации о работе скрипта.

## Переменные

### `MODE`
```python

```
- **Описание**: Указывает режим работы скрипта (в данном случае, "dev").
- **Тип**: `str`.

### `filenames`
```python
filenames: list[str] = [
    "usa.json",
    "he_ils.json",
    "ru_ils.json",
    "katia_homepage.json",
    "my_managed_groups.json",
]
```
- **Описание**: Список имен файлов, содержащих информацию о группах для размещения рекламы.
- **Тип**: `list[str]`.

### `excluded_filenames`
```python
excluded_filenames: list[str] = [
    "my_managed_groups.json",
    "ru_usd.json",
    "ger_en_eur.json",
]
```
- **Описание**: Список файлов, которые следует исключить из процесса размещения рекламы.
- **Тип**: `list[str]`.

### `campaigns`
```python
campaigns: list = [
    'brands',
    'mom_and_baby',
    'pain',
    'sport_and_activity',
    'house',
    'bags_backpacks_suitcases',
    'man'
]
```
- **Описание**: Список имен рекламных кампаний.
- **Тип**: `list`.

### `d`
```python
d = Driver(Chrome)
```
- **Описание**: Экземпляр класса `Driver`, управляющий веб-драйвером Chrome.
- **Тип**: `Driver`.

### `promoter`
```python
promoter: FacebookPromoter = FacebookPromoter(d, group_file_paths=filenames, no_video=True)
```
- **Описание**: Экземпляр класса `FacebookPromoter`, управляющий процессом размещения рекламы в Facebook.
- **Тип**: `FacebookPromoter`.

## Инициализация

```python
d.get_url(r"https://facebook.com")
```

- **Описание**: Открывает страницу Facebook в браузере, управляемом веб-драйвером.

## Основной цикл

```python
try:
    while True:
        promoter.run_campaigns(campaigns=copy.copy(campaigns), group_file_paths=filenames)
        print(f"Going sleep {time.localtime}")
        time.sleep(180)
        ...

except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

- **Описание**: Бесконечный цикл, который запускает рекламные кампании, делает паузу и повторяет этот процесс.
- **Параметры**:
    - `campaigns` (list): Список кампаний, которые нужно запустить.
    - `group_file_paths` (list[str]): Список файлов с данными о группах.
- **Исключения**:
    - `KeyboardInterrupt`: Обрабатывается прерывание с клавиатуры (Ctrl+C), при котором скрипт останавливается и в лог записывается сообщение.
- **Внутренние действия**:
   - `promoter.run_campaigns`: Запускает рекламные кампании.
   - `time.sleep(180)`: Приостанавливает выполнение скрипта на 180 секунд.
   - `print(f"Going sleep {time.localtime}")`: Выводит в консоль сообщение о том, что скрипт уходит в спящий режим.