# Received Code

```python
# Локаторы полей на `HTML`-странице

### Пример локатора:
```json
"close_banner": {
    "attribute": null, 
    "by": "XPATH",
    "selector": "//button[@id = 'closeXButton']",
    "if_list": "first",
    "use_mouse": false,
    "mandatory": false,
    "event": "click()",
    "locator_description": "Закрываю pop-up окно. Если оно не появилось — не страшно (`mandatory`: `false`)."\
  },
  "additional_images_urls": {
    "attribute": "src",
    "by": "XPATH",
    "selector": "//ol[contains(@class, 'flex-control-thumbs')]//img",
    "if_list": "all",
    "use_mouse": false,
    "mandatory": false,
    "event": null,
    "locator_description": "Получает список `url` дополнительных изображений."\
  },
  "id_supplier": {
    "attribute": "innerText",
    "by": "XPATH",
    "selector": "//span[@class = 'ltr sku-copy']",
    "if_list": "first",
    "use_mouse": false,
    "mandatory": true,
    "event": null,
    "locator_description": "SKU Morlevi."\
  },
  "default_image_url": {
    "attribute": null,
    "by": "XPATH",
    "selector": "//a[@id = 'mainpic']//img",
    "if_list": "first",
    "use_mouse": false,
    "event": "screenshot()",
    "mandatory": true,
    "locator_description": "Внимание! В Morlevi картинка получается через screenshot и возвращается как PNG (`bytes`)."\
  }
```

### Детали:
Имя словаря соответствует имени поля класса `ProductFields` ([подробнее о `ProductFields`](../product/product_fields)).

- **`attribute`**: Атрибут, который нужно получить от веб-элемента. Например: `innerText`, `src`, `id`, `href` и т.д.  
  Если установить значение `attribute` в `none/false`, то WebDriver вернёт весь веб-элемент (`WebElement`).

- **`by`**: Стратегия для поиска элемента:  
  - `ID` соответствует `By.ID`  
  - `NAME` соответствует `By.NAME`  
  - `CLASS_NAME` соответствует `By.CLASS_NAME`  
  - `TAG_NAME` соответствует `By.TAG_NAME`  
  - `LINK_TEXT` соответствует `By.LINK_TEXT`  
  - `PARTIAL_LINK_TEXT` соответствует `By.PARTIAL_LINK_TEXT`  
  - `CSS_SELECTOR` соответствует `By.CSS_SELECTOR`  
  - `XPATH` соответствует `By.XPATH`

- **`selector`**: Селектор, определяющий способ нахождения веб-элемента. Примеры:  
  `(//li[@class = 'slide selected previous'])[1]//img`,  
  `//a[@id = 'mainpic']//img`,  
  `//span[@class = 'ltr sku-copy']`.

- **`if_list`**: Определяет, что делать со списком найденных веб-элементов (`web_element`). Возможные значения:  
  - `first`: выбрать первый элемент из списка.  
  - `all`: выбрать все элементы.  
  - `last`: выбрать последний элемент.  
  - `even`, `odd`: выбрать чётные/нечётные элементы.  
  - Указание конкретных номеров, например, `1,2,...` или `[1,3,5]`: выбрать элементы с указанными номерами.  
  Альтернативный способ — указать номер элемента прямо в селекторе, например:  
  `(//div[contains(@class, 'description')])[2]//p`

- **`use_mouse`**: `true` | `false`  
  Используется для выполнения действий с помощью мыши.

- **`event`**: WebDriver может выполнить действие с веб-элементом, например, `click()`, `screenshot()`, `scroll()` и т.д.  
  **Важно**: Если указан `event`, он будет выполнен **до** получения значения из `attribute`.  

- **`mandatory`**: Является ли локатор обязательным.  
  Если `{mandatory: true}` и взаимодействие с веб-элементом невозможно, код выбросит ошибку. Если `mandatory: false`, элемент будет пропущен.

- **`locator_description`**: Описание локатора.

---

### Сложные локаторы:
В ключи локатора можно передавать списки, кортежи или словари.

```python
```
```

# Improved Code

```python
"""
Модуль для определения локаторов веб-элементов.
================================================
Этот модуль содержит конфигурацию локаторов для различных веб-элементов.
Локаторы используются для нахождения и взаимодействия с веб-элементами.
"""
from typing import Any, Dict
from src.utils.jjson import j_loads
from src.logger import logger

LOCATORS_FILE = 'hypotez/src/suppliers/locator.ru.md'  # Путь к файлу локаторов

def load_locators() -> Dict[str, Dict[str, Any]]:
    """
    Загружает локаторы из файла.

    :return: Словарь локаторов.
    :raises FileNotFoundError: Если файл не найден.
    :raises ValueError: Если не удалось загрузить данные из файла.
    """
    try:
        with open(LOCATORS_FILE, 'r') as f:
            locators_data = j_loads(f.read())
            return locators_data
    except FileNotFoundError as e:
        logger.error('Ошибка загрузки локаторов:', e)
        raise
    except ValueError as e:
        logger.error('Ошибка парсинга данных локаторов:', e)
        raise

# Пример использования
# locators = load_locators()
```

# Changes Made

- Создан модуль `locator.py`.
- Функция `load_locators()` загружает локаторы из файла.
- Функция `load_locators()` использует `j_loads` для загрузки данных, а не `json.load()`.
- Добавлен обработчик ошибок для `FileNotFoundError` и `ValueError` с использованием `logger.error`.
- Добавлены комментарии RST для описания модуля и функции `load_locators()`.
- Переменная `LOCATORS_FILE` определена для явного указания пути к файлу.
- Удалены неиспользуемые части кода.
- Улучшен стиль кода.

# FULL Code

```python
"""
Модуль для определения локаторов веб-элементов.
================================================
Этот модуль содержит конфигурацию локаторов для различных веб-элементов.
Локаторы используются для нахождения и взаимодействия с веб-элементами.
"""
from typing import Any, Dict
from src.utils.jjson import j_loads
from src.logger import logger

LOCATORS_FILE = 'hypotez/src/suppliers/locator.ru.md'  # Путь к файлу локаторов

def load_locators() -> Dict[str, Dict[str, Any]]:
    """
    Загружает локаторы из файла.

    :return: Словарь локаторов.
    :raises FileNotFoundError: Если файл не найден.
    :raises ValueError: Если не удалось загрузить данные из файла.
    """
    try:
        with open(LOCATORS_FILE, 'r') as f:
            locators_data = j_loads(f.read())
            return locators_data
    except FileNotFoundError as e:
        logger.error('Ошибка загрузки локаторов:', e)
        raise
    except ValueError as e:
        logger.error('Ошибка парсинга данных локаторов:', e)
        raise

# Пример использования
# locators = load_locators()
```
```