# Модуль `hypotez/src/endpoints/advertisement/facebook/start_posting.py`

## Обзор

Модуль `start_posting.py` отвечает за запуск рекламных кампаний в группах Facebook. Он использует класс `FacebookPromoter` для автоматической публикации объявлений, загружая данные из JSON-файлов.

## Переменные

### `MODE`

Тип: `str`

Значение: `'dev'`

Описание: Переменная, определяющая режим работы (в данном случае 'dev').

### `filenames`

Тип: `list[str]`

Описание: Список путей к JSON-файлам с данными о целевых группах Facebook.

### `excluded_filenames`

Тип: `list[str]`

Описание: Список имен JSON-файлов, которые не должны обрабатываться.

### `campaigns`

Тип: `list`

Описание: Список названий рекламных кампаний.

## Классы

### `Driver`

Описание: Класс для работы с веб-драйвером.  (Описание класса Driver и его методов должно быть взято из файла `src/webdriver/driver.py` и сюда вставлено).

### `Chrome`

Описание:  (Описание класса Chrome должно быть взято из файла `src/webdriver/driver.py` и сюда вставлено).

### `FacebookPromoter`

Описание:  (Описание класса FacebookPromoter должно быть взято из файла `src/endpoints/advertisement/facebook/facebook_promoter.py` и сюда вставлено).

## Функции

### `run_campaigns`

**Описание**: Запускает рекламные кампании для заданных групп.

**Параметры**:
- `campaigns` (`list`): Список названий рекламных кампаний.
- `group_file_paths` (`list[str]`): Список путей к JSON-файлам с данными о группах.

**Возвращает**:
-  `None`.


## Инициализация

```python
d = Driver(Chrome)
d.get_url(r"https://facebook.com")

promoter:FacebookPromoter = FacebookPromoter(d, group_file_paths=filenames, no_video = True)
```

Описание: Инициализирует веб-драйвер и объект `FacebookPromoter`, загружая данные о группах из файлов.

## Цикл обработки

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

Описание: Бесконечный цикл, запускающий рекламные кампании.  После каждой итерации цикл ждет 180 секунд. Обработка `KeyboardInterrupt` позволяет корректно завершить программу при прерывании пользователя.

**Обрабатывает исключения**:
- `KeyboardInterrupt`:  Прерывание выполнения пользователем. В этом случае выводится сообщение в логгер.


**Замечания:**

* Для полной документации необходимо добавить документацию к классам `Driver`, `Chrome`, `FacebookPromoter`, а также описать работу с JSON-файлами и логикой запуска рекламных кампаний.
* Присутствует неполная реализация. Код `...` предполагает наличие дополнительных действий внутри цикла.
* Приведенный код предполагает, что классы `Driver`, `Chrome`, и `FacebookPromoter` содержат адекватную реализацию.
* Необходима документация к модулю `header`, `time`, `copy` и `src.logger`.