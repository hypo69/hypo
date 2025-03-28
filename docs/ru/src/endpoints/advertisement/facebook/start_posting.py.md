# Модуль `start_posting`

## Обзор

Модуль предназначен для отправки рекламных объявлений в группы Facebook. Он использует WebDriver для автоматизации действий в браузере и загружает информацию о группах из JSON файлов.

## Оглавление

1. [Обзор](#обзор)
2. [Импорты](#импорты)
3. [Переменные](#переменные)
4. [Класс `FacebookPromoter`](#класс-facebookpromoter)
5. [Основной цикл](#основной-цикл)

## Импорты

В данном модуле используются следующие импорты:

- `math.log`:  Используется для математических операций (хотя в коде не используется напрямую).
- `header`: Неизвестный модуль, предполагается, что он используется для добавления заголовков (скорее всего для запросов к сети).
- `time`: Для работы со временем, используется для задержек и отслеживания времени.
- `copy`:  Используется для создания копий объектов, например, списков.
- `src.webdriver.driver.Driver`, `src.webdriver.driver.Chrome`: Классы для управления браузером.
- `src.endpoints.advertisement.facebook.FacebookPromoter`: Класс для отправки рекламных объявлений в Facebook.
- `src.logger.logger.logger`: Объект логгера для записи сообщений.

## Переменные

В модуле определены следующие переменные:

- `d`: Экземпляр класса `Driver` с использованием `Chrome` в качестве браузера. Открывает страницу `https://facebook.com`.
- `filenames`: Список строк, представляющих имена файлов JSON, содержащих информацию о группах.
- `excluded_filenames`: Список строк, содержащих имена файлов, которые не нужно использовать.
- `campaigns`: Список строк, представляющих названия рекламных кампаний.
- `promoter`: Экземпляр класса `FacebookPromoter`, используемый для запуска рекламных кампаний.

## Класс `FacebookPromoter`

### `FacebookPromoter`

**Описание**:

Экземпляр класса `FacebookPromoter` создается с передачей объекта `Driver` и списка файлов с данными о группах. Параметр `no_video` установлен в `True`.

**Параметры**:
- `d` (Driver): Объект драйвера браузера.
- `group_file_paths` (list[str]): Список путей к файлам JSON с данными о группах.
- `no_video` (bool): Указывает, публиковать ли объявления без видео (по умолчанию `True`).

**Методы**:
  - `run_campaigns`: Метод для запуска рекламных кампаний.

## Основной цикл

### `try...except`

**Описание**:

Основной цикл `while True:` обеспечивает бесконечную работу программы. 
Внутри цикла вызывается метод `run_campaigns` объекта `promoter`, передавая копию списка кампаний и список файлов с данными о группах. После этого программа приостанавливается на 180 секунд. Обработка исключения `KeyboardInterrupt` позволяет завершить программу, выводя соответствующее сообщение в лог.

**Код**:
```python
try:
    while True:
        
        promoter.run_campaigns(campaigns = copy.copy(campaigns), group_file_paths = filenames)
        print(f"Going sleep {time.localtime}")
        time.sleep(180)
        ...
        
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

**Исключения**:
- `KeyboardInterrupt`: Возникает при нажатии пользователем `Ctrl+C`. Программа завершает работу.