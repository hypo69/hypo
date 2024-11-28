# Модуль `hypotez/src/endpoints/advertisement/facebook/start_posting.py`

## Обзор

Данный модуль отвечает за запуск рекламных кампаний в группах Facebook. Он использует драйвер веб-драйвера, инициализирует FacebookPromoter и запускает рекламные кампании, определённые в списке `campaigns`. Модуль реализует циклическую работу по запуску кампаний с определенным интервалом.


## Переменные

### `MODE`

**Тип:** `str`

**Описание:** Строковая переменная, определяющая режим работы. В текущей реализации значение равно `'dev'`.

### `filenames`

**Тип:** `list[str]`

**Описание:** Список путей к JSON-файлам с данными о группах Facebook, которые будут использоваться для рекламных кампаний.

### `excluded_filenames`

**Тип:** `list[str]`

**Описание:** Список путей к JSON-файлам, которые будут исключены из списка групп Facebook.

### `campaigns`

**Тип:** `list`

**Описание:** Список строк, представляющих названия рекламных кампаний.

## Классы

### `Driver`

**Описание**:  Класс для взаимодействия с веб-драйвером. В данной реализации используется Chrome.

### `Chrome`

**Описание**:  Реализация драйвера для Chrome.


### `FacebookPromoter`

**Описание**: Класс для запуска рекламных кампаний в Facebook. Требует инициализации драйвером веб-драйвера и списком путей к JSON-файлам.

## Функции

### `run_campaigns`

**Описание**: Функция запуска рекламных кампаний.

**Параметры:**

- `campaigns (list)`: Список рекламных кампаний для запуска.
- `group_file_paths (list[str])`: Список путей к JSON-файлам с группами Facebook.

**Возвращает:**

- `None`

**Вызывает исключения:**

- `None`


## Использование


1. Инициализировать драйвер веб-драйвера (`Driver`):
```python
d = Driver(Chrome)
d.get_url(r"https://facebook.com")
```

2. Создать экземпляр `FacebookPromoter`, передав инициализированный драйвер и список путей к файлам с группами:
```python
promoter:FacebookPromoter = FacebookPromoter(d, group_file_paths=filenames, no_video = True)
```

3. Запустить цикл для запуска рекламных кампаний:
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

**Обработка исключений**

Обработка исключений `KeyboardInterrupt` позволяет корректно завершать работу программы при прерывании пользователя.


**Примечания:**

Модуль использует `copy.copy(campaigns)` для предотвращения изменения исходного списка `campaigns` во время выполнения цикла. Важно добавить импорты необходимых библиотек (header, time, copy, src.webdriver, src.endpoints.advertisement.facebook, src.logger).

```