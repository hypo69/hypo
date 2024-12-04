# Модуль `hypotez/src/endpoints/advertisement/facebook/start_posting_my_groups.py`

## Оглавление

* [Отправка рекламных объявлений в группы Facebook](#отправка-рекламных-объявлений-в-группы-facebook)
* [Константы](#константы)
* [Импорты](#импорты)
* [Переменные](#переменные)
* [Главная логика](#главная-логика)


## Отправка рекламных объявлений в группы Facebook

Этот модуль отвечает за запуск рекламных кампаний в группах Facebook. Он использует драйвер для управления браузером и класс `FacebookPromoter` для взаимодействия с платформой Facebook. Модуль циклически запускает рекламные кампании, используя список кампаний и пути к файлам с данными о группах.

## Константы

```python
MODE = 'dev'
```

`MODE`: Строковая константа, хранящая режим работы (например, 'dev', 'prod').


## Импорты

```python
import header
import copy
from src.webdriver import Driver, Chrome
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.logger import logger
```

- `header`:  Вероятно, файл с дополнительными импортами.
- `copy`: Модуль для работы с копиями объектов.
- `Driver`, `Chrome`: Классы из модуля `src.webdriver` для работы с браузером (вероятно, с использованием Selenium).
- `FacebookPromoter`: Класс из модуля `src.endpoints.advertisement.facebook` для работы с рекламными кампаниями Facebook.
- `logger`: Модуль для ведения логов.


## Переменные

```python
filenames: list = ['my_managed_groups.json',]
campaigns: list = ['brands', 'mom_and_baby', 'pain', 'sport_and_activity', 'house', 'bags_backpacks_suitcases', 'man']
```

- `filenames`: Список путей к JSON-файлам с данными о группах Facebook.
- `campaigns`: Список названий рекламных кампаний.


## Главная логика

```python
d = Driver(Chrome)
d.get_url(r"https://facebook.com")

promoter = FacebookPromoter(d, group_file_paths=filenames, no_video=True)

try:
    while True:
        promoter.run_campaigns(campaigns=copy.copy(campaigns), group_file_paths=filenames)
        ...
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

1. Инициализация драйвера браузера и переход на страницу Facebook.
2. Создание экземпляра `FacebookPromoter` с необходимыми параметрами.
3. Цикл `while True`:
    - Вызов метода `run_campaigns` для запуска рекламных кампаний.
    - `...`:  Этот блок предполагает наличие дополнительного кода внутри цикла. Вероятно, обработка результатов кампаний, задержка между запусками или другие операции.
4. Обработка исключения `KeyboardInterrupt`:
    - Вывод сообщения об прерывании кампаний в лог.

**Примечание:**  Блок `...`  в коде требует дополнительной информации для полного понимания логики работы программы.  Необходимы детали о том, как происходит обработка результатов запуска рекламных кампаний, а также, какие действия выполняются внутри цикла `while`.