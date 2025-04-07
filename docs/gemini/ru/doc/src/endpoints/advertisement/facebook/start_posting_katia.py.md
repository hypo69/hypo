# Модуль для запуска рекламной кампании в Facebook (Katia)

## Обзор

Модуль предназначен для автоматической отправки рекламных объявлений в группы Facebook с использованием веб-драйвера. Он использует класс `FacebookPromoter` для управления процессом продвижения рекламных кампаний.

## Подробнее

Модуль `start_posting_katia.py` является точкой входа для запуска рекламных кампаний в Facebook. Он инициализирует веб-драйвер, определяет список рекламных кампаний и использует класс `FacebookPromoter` для выполнения продвижения. В случае прерывания процесса пользователем, регистрируется соответствующее сообщение.

## Классы

### `FacebookPromoter`

**Описание**: Класс `FacebookPromoter` отвечает за продвижение рекламных кампаний в Facebook.

**Принцип работы**:
Класс использует веб-драйвер для взаимодействия с Facebook, загружает параметры групп из файлов конфигурации и выполняет шаги, необходимые для размещения рекламных объявлений в группах.

**Методы**:
- `run_campaigns`: Запускает процесс продвижения для указанных рекламных кампаний.

## Функции

В данном модуле нет отдельных функций, кроме методов класса `FacebookPromoter`. Основная логика выполняется внутри класса `FacebookPromoter`.

### `FacebookPromoter.run_campaigns`

**Назначение**: Запускает процесс продвижения рекламных кампаний, определенных в списке `campaigns`.

```python
def run_campaigns(campaigns:list):
    """
    Запускает процесс продвижения рекламных кампаний, определенных в списке `campaigns`.

    Args:
        campaigns (list): Список названий рекламных кампаний для запуска.

    Raises:
        Exception: Если во время выполнения кампании возникают ошибки.
    """
    ...
```

**Параметры**:
- `campaigns` (list): Список названий рекламных кампаний, которые необходимо запустить.

**Возвращает**:
- Ничего. Функция выполняет действия и не возвращает значения явно.

**Вызывает исключения**:
- `Exception`: Если во время выполнения кампании возникают какие-либо ошибки.

**Как работает функция**:

1. **Инициализация:**
   - Функция `run_campaigns` принимает список названий рекламных кампаний `campaigns`.

2. **Выполнение кампаний:**
   - Выполняются действия, необходимые для продвижения каждой кампании в Facebook.

3. **Обработка исключений:**
   - Если происходит прерывание с клавиатуры (`KeyboardInterrupt`), регистрируется сообщение об этом.

**Примеры**:
```python
promoter.run_campaigns(['sport_and_activity', 'bags_backpacks_suitcases'])
```

```ascii
    Начало
     ↓
  run_campaigns(campaigns)
     ↓
  Продвижение кампаний
     ↓
Завершение
```

## Пример использования модуля

```python
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