# Модуль `hypotez/src/endpoints/advertisement/facebook/start_posting_katia.py`

## Обзор

Модуль `start_posting_katia.py` отвечает за запуск рекламных кампаний в группах Facebook. Он использует класс `FacebookPromoter` для автоматизированной отправки объявлений.  Модуль использует веб-драйвер для взаимодействия с сайтом Facebook.

## Параметры

- `MODE` (str): Режим работы (например, 'dev', 'prod').  По умолчанию 'dev'.
- `filenames` (list): Список путей к файлам с данными о целевых группах.
- `campaigns` (list): Список названий рекламных кампаний.


## Импорты

- `header`:  Модуль с дополнительными настройками (не описан в примере).
- `Driver`, `Chrome`: Классы для работы с веб-драйвером (из модуля `src.webdriver`).
- `FacebookPromoter`: Класс для работы с рекламными кампаниями в Facebook (из модуля `src.endpoints.advertisement.facebook.promoter`).
- `logger`: Модуль для логирования (из модуля `src.logger`).


## Функции

### `run_campaigns`

**Описание**: Запускает рекламные кампании в заданных группах.

**Параметры**:
- `campaigns` (list): Список названий рекламных кампаний.

**Возвращает**:
- Не имеет возвращаемого значения.

**Вызывает исключения**:
- `KeyboardInterrupt`:  Если пользователь прервал выполнение программы с помощью сочетания клавиш Ctrl+C.


## Классы

### `FacebookPromoter`

**Описание**: Класс для работы с рекламными кампаниями в Facebook.


**Методы**:
- `run_campaigns`: Запускает рекламные кампании.  (Описание приведено выше)



## Пример использования

```python
# ... (Импорты) ...
d = Driver(Chrome)
d.get_url(r"https://facebook.com")

filenames: list = ['katia_homepage.json',]
campaigns: list = [
    'sport_and_activity',
    'bags_backpacks_suitcases',
    'pain',
    'brands',
    'mom_and_baby',
    'house',
]

promoter = FacebookPromoter(d, group_file_paths=filenames, no_video=False)

try:
    promoter.run_campaigns(campaigns)
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

**Примечание**: Данный код демонстрирует общий способ использования. Подробности работы класса `FacebookPromoter` и его методов должны быть описаны в соответствующих модулях (`src.endpoints.advertisement.facebook.promoter`).  Также ожидается, что модули `header`, `logger` и `src.webdriver` содержат определения и документацию для своих компонентов.