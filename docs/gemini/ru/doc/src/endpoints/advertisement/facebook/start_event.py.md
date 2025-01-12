# Модуль `src.endpoints.advertisement.facebook.start_event`

## Обзор

Модуль предназначен для отправки событий в группы Facebook. Он использует Selenium для автоматизации действий в браузере и взаимодействует с API Facebook через класс `FacebookPromoter`. Модуль запускает бесконечный цикл, который периодически публикует события в выбранные группы.

## Оглавление
1. [Импорты](#Импорты)
2. [Глобальные переменные](#Глобальные-переменные)
3. [Функции](#Функции)

## Импорты
В данном разделе описаны все импортируемые модули и их назначение.

```python
from math import log
import header
import time
from src.utils.jjson import j_loads
from src.webdriver.driver import Driver, Chrome
from src.endpoints.advertisement.facebook import FacebookPromoter
from src.logger.logger import logger
```
- `math.log`: Используется для математических операций (не используется в текущем коде).
- `header`: Импортируется модуль `header` (содержание не известно).
- `time`: Используется для управления временем, например, для задержки выполнения программы.
- `src.utils.jjson.j_loads`: Используется для загрузки JSON данных.
- `src.webdriver.driver.Driver`, `src.webdriver.driver.Chrome`: Используются для управления браузером.
- `src.endpoints.advertisement.facebook.FacebookPromoter`: Используется для взаимодействия с API Facebook и публикации событий.
- `src.logger.logger.logger`: Используется для логирования событий.

## Глобальные переменные

В этом разделе описаны глобальные переменные и их использование в скрипте.

### `d`
   - **Описание**: Экземпляр класса `Driver` с выбранным браузером Chrome.
   - **Тип**: `Driver`.
    ```python
    d = Driver(Chrome)
    d.get_url(r"https://facebook.com")
    ```
### `filenames`
   - **Описание**: Список строк, представляющих имена JSON файлов, содержащих информацию о группах Facebook.
   - **Тип**: `list[str]`.
    ```python
     filenames:list[str] = [ "my_managed_groups.json",
                            "usa.json",
                            "he_il.json",
                            "ru_il.json",
                            "katia_homepage.json",
                            
                            "ru_usd.json",
                            "ger_en_eur.json",            
                            ]
    ```

### `excluded_filenames`
   - **Описание**: Список строк, представляющих имена JSON файлов, которые нужно исключить из обработки.
   - **Тип**: `list[str]`.
   ```python
     excluded_filenames:list[str] = ["my_managed_groups.json",]
   ```

### `events_names`
   - **Описание**: Список строк, представляющих названия событий.
   - **Тип**: `list`.
   ```python
   events_names:list = ["choice_day_01_10"]
   ```

### `promoter`
   - **Описание**: Экземпляр класса `FacebookPromoter`, который управляет публикацией событий в Facebook.
   - **Тип**: `FacebookPromoter`.
   ```python
   promoter:FacebookPromoter = FacebookPromoter(d, group_file_paths=filenames, no_video = True)
   ```
## Функции
В данном модуле не определено ни одной функции. Основная логика выполняется в глобальном контексте.

### Основной цикл
  - **Описание**: Бесконечный цикл, который периодически запускает публикацию событий в группах Facebook.
    ```python
    try:
        while True:
            logger.debug(f"waikig up {time.strftime(\'%H:%M:%S\')}",None,False)
            promoter.run_events(events_names = events_names, group_file_paths = filenames)
            logger.debug(f"going to sleep at {time.strftime(\'%H:%M:%S\')}",None,False)
            time.sleep(7200)
            
    except KeyboardInterrupt:
        logger.info("Campaign promotion interrupted.")
    ```

  - **Параметры**:
    - `events_names` (`list`): Список событий для публикации.
    - `group_file_paths` (`list`): Список файлов с данными о группах.
  - **Возвращает**:
     - `None`
  - **Вызывает исключения**:
      - `KeyboardInterrupt`: Возникает при прерывании выполнения программы пользователем.