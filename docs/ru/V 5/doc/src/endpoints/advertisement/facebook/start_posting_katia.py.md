# Модуль `start_posting_katia.py`

## Обзор

Модуль `start_posting_katia.py` предназначен для отправки рекламных объявлений в группы Facebook. В нём используется веб-драйвер для автоматизации процесса публикации. Модуль является частью подсистемы `advertisement` и отвечает за запуск рекламных кампаний в Facebook.

## Подробней

Модуль использует классы `Driver` и `Chrome` для управления браузером, а также класс `FacebookPromoter` для выполнения фактической публикации объявлений. Он считывает конфигурацию кампаний из JSON-файлов и выполняет их в указанном порядке.

## Классы

### `FacebookPromoter`

**Описание**: Класс `FacebookPromoter` отвечает за продвижение рекламных кампаний в Facebook.

**Как работает класс**:
Класс инициализируется с веб-драйвером, списком файлов с описаниями групп и флагом, указывающим на наличие видео. Он предоставляет метод `run_campaigns` для запуска рекламных кампаний.

**Методы**:
- `run_campaigns`: Запускает рекламные кампании.

**Параметры**:
- `d`: Экземпляр веб-драйвера.
- `group_file_paths` (list): Список путей к файлам с описаниями групп.
- `no_video` (bool): Флаг, указывающий на отсутствие видео.

**Примеры**:
```python
from src.webdriver.driver import Driver, Chrome
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter

d = Driver(Chrome)
d.get_url(r"https://facebook.com")

filenames: list = ['katia_homepage.json']
campaigns: list = ['sport_and_activity']

promoter = FacebookPromoter(d, group_file_paths=filenames, no_video=False)
promoter.run_campaigns(campaigns)
```

## Функции

В данном коде функции отсутствуют.

## Переменные

- `d`: Экземпляр класса `Driver`, используемый для управления браузером Chrome.
- `filenames` (list): Список имен JSON-файлов, содержащих информацию о группах для публикации.
- `campaigns` (list): Список кампаний для запуска. Каждая кампания соответствует определенной тематике.
- `promoter`: Экземпляр класса `FacebookPromoter`, который отвечает за запуск и управление рекламными кампаниями в Facebook.

## Обработка исключений

В коде используется блок `try...except` для обработки прерывания с клавиатуры.
```python
try:
    promoter.run_campaigns(campaigns)
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```
Если пользователь прерывает выполнение программы нажатием Ctrl+C, будет зарегистрировано сообщение об этом.