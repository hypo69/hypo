# Модуль `hypotez/src/endpoints/advertisement/facebook/start_posting_my_groups.py`

## Обзор

Этот модуль отвечает за запуск рекламных кампаний в группах Facebook (My Groups). Он использует драйвер браузера Chrome для взаимодействия с сайтом Facebook и класс `FacebookPromoter` для управления рекламными кампаниями.  Модуль загружает список групп из файла `my_managed_groups.json` и запускает цикл, поочередно выполняя кампании.

## Оглавление

* [Обзор](#обзор)
* [Переменные](#переменные)
* [Импорты](#импорты)
* [Функции](#функции)
* [Обработка исключений](#обработка-исключений)

## Переменные

### `MODE`

**Описание**: Строковая переменная, определяющая режим работы (например, 'dev' для разработки).

### `filenames`

**Описание**: Список путей к файлам, содержащим информацию о группах Facebook.

### `campaigns`

**Описание**: Список названий рекламных кампаний.

## Импорты

* `header`:  Модуль, предположительно содержащий общие настройки и функции.
* `copy`: Модуль для работы с копиями объектов.
* `Driver`, `Chrome`: Классы для работы с браузером (вероятно, из `src.webdriver`).
* `FacebookPromoter`: Класс для управления рекламными кампаниями в Facebook (из `src.endpoints.advertisement.facebook.promoter`).
* `logger`: Модуль для логирования (из `src.logger`).

## Классы

(Список классов отсутствует в коде, поэтому данный раздел пуст.)

## Функции

(Список функций отсутствует в коде, поэтому данный раздел пуст.)

## Обработка исключений

### `KeyboardInterrupt`

**Описание**: Обрабатывает прерывание пользователя (Ctrl+C). Выводит сообщение о прерывании кампании.

## Использование

Модуль `start_posting_my_groups.py` запускает цикл рекламных кампаний. Он использует `FacebookPromoter` для инициализации и выполнения кампаний. Важно, чтобы были доступны необходимые данные и настройки в `my_managed_groups.json` для корректной работы.


```python
d = Driver(Chrome)
d.get_url(r"https://facebook.com")

filenames: list = ['my_managed_groups.json',]
campaigns: list = ['brands', 'mom_and_baby', 'pain', 'sport_and_activity', 'house', 'bags_backpacks_suitcases', 'man']

promoter = FacebookPromoter(d, group_file_paths=filenames, no_video=True)

try:
    while True:
        promoter.run_campaigns(campaigns=copy.copy(campaigns), group_file_paths=filenames)
        # ... (Дополнительные действия в цикле)
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

**Примечание**: Код содержит комментарии `...`, что указывает на необходимость добавления дополнительных действий внутри цикла `while`.  Также, отсутствует реализация метода `run_campaigns` в `FacebookPromoter`, что требует дополнительной информации для полноценного описания.