# Анализ кода модуля `readme.ru.md`

**Качество кода**
8
-  Плюсы
    - Документ содержит подробное описание функциональности модулей `driver.py`, `chrome.py`, и `executor.py`.
    - Приведены примеры использования классов и методов.
    - Описаны основные функции, принципы работы и зависимости.
-  Минусы
    -  Используется Markdown вместо reStructuredText (RST).
    -  Не хватает документации в формате docstring для кода.
    -  В примерах кода отсутствуют комментарии в стиле RST.
    -  Некоторые описания можно сделать более структурированными и подробными.

**Рекомендации по улучшению**

1.  Переписать весь текст документа в формате **reStructuredText (RST)**.
2.  Добавить подробные docstring к каждому методу и классу, а также к модулям, как показано в инструкции.
3.  Использовать более формализованное описание для методов и функций, включая параметры, возвращаемые значения и исключения.
4.  Переписать примеры кода с использованием docstring и более подробными пояснениями в стиле RST.
5.  Привести в соответствие имена переменных и функций в соответствии с другими модулями.
6.  Избегать общих формулировок, таких как "осуществляет проверку" или "выполняет действие", а давать конкретное описание.
7.  Внести изменения во все блоки кода, указанные в инструкции, прокомментировав каждую строку.
8.  Убрать излишнее дублирование информации, содержащейся в файлах `executor.ru.md` и `locator.ru.md`.

**Оптимизированный код**
```markdown
# Анализ модуля `src.webdriver`

## Обзор модуля: `src.webdriver`
   Модуль предоставляет инструменты для автоматизации взаимодействия с веб-страницами через WebDriver. Он включает классы и методы для управления браузером, обработки элементов и выполнения различных действий на веб-страницах.
   =========================================================================================

   Основные компоненты:

   -   **driver.py**: Содержит классы для управления WebDriver, включая настройку и базовые действия.
   -   **chrome.py**: Класс для настройки и запуска Chrome WebDriver.
   -  **executor.py**: Класс для выполнения действий с веб-элементами на основе заданных локаторов.

   **Пример использования**

   ```python
   from src.webdriver.driver import Driver, Chrome
   driver = Driver(Chrome)
   driver.get_url("https://example.com")
   ```
   
## Обзор `driver.py`

   Модуль `driver.py` предоставляет динамическую реализацию WebDriver, которая объединяет стандартные функции WebDriver с дополнительными методами для взаимодействия с веб-страницами, обработки JavaScript и управления cookies.

### Основные характеристики:
* Наследует от указанного класса WebDriver (например, Chrome, Firefox, Edge) и добавляет дополнительную функциональность.
* Включает методы для прокрутки, обработки cookies, взаимодействия с веб-элементами и выполнения JavaScript.
* Предоставляет утилиты для управления окнами браузера и взаимодействием со страницами.

### Компоненты:

1.  **Класс `DriverBase`**
    *  **Атрибуты:**
       - `previous_url` - Сохраняет предыдущий URL.
       - `referrer` - Сохраняет URL реферера.
       - `page_lang` - Сохраняет язык страницы.
       - Различные атрибуты для взаимодействия с веб-элементами и выполнения JavaScript.
    *  **Методы:**
        -  `scroll(scrolls: int, direction: str, frame_size: int, delay: int) -> bool`
            
            Прокручивает веб-страницу в указанном направлении. Поддерживает прокрутку вперед, назад или в обоих направлениях.

            :param scrolls: Количество прокруток.
            :param direction: Направление прокрутки ('forward', 'backward').
            :param frame_size: Размер фрейма прокрутки.
            :param delay: Задержка между прокрутками.
            :return: `True` в случае успешной прокрутки, `False` в противном случае.
        -  `locale -> str`
            
            Определяет язык страницы путем проверки мета-тегов или использования JavaScript.

            :return: Язык страницы в виде строки или `None`, если язык не определен.
        -  `get_url(url: str) -> bool`
           
            Загружает указанный URL.

            :param url: URL для загрузки.
            :return: `True`, если URL успешно загружен, `False` в противном случае.
        -  `extract_domain(url: str) -> str`
            
            Извлекает домен из URL.

            :param url: URL, из которого требуется извлечь домен.
            :return: Домен из URL в виде строки или `None`, если домен не может быть извлечен.
        -  `_save_cookies_localy() -> bool`
            
            Сохраняет cookies в локальный файл.

            :return: `True`, если cookies были сохранены успешно, `False` в противном случае.
        -  `page_refresh() -> bool`
            
            Обновляет текущую страницу.

            :return: `True`, если страница была успешно обновлена, `False` в противном случае.
        -  `window_focus() -> None`
            
             Фокусирует окно браузера с использованием JavaScript.
        -  `wait(sec: int) -> None`
            
            Ожидает указанное количество секунд.

            :param sec: Количество секунд для ожидания.

2.  **Класс `DriverMeta`**
    *  **Методы:**
       - `__call__(cls, webdriver_class: type, *args, **kwargs) -> type`
            Создает новый класс `Driver`, который объединяет указанный класс WebDriver (например, Chrome, Firefox, Edge) с `DriverBase`. Инициализирует JavaScript методы и функции выполнения локаторов.
            
            :param webdriver_class: Класс WebDriver для наследования.
            :return: Созданный класс `Driver`.

3.  **Класс `Driver`**
    *  **Описание:**
        Динамически созданный класс WebDriver, который наследует от `DriverBase` и указанного класса WebDriver.
    *  **Пример использования:**

    ```python
    from src.webdriver.driver import Driver, Chrome, Firefox, Edge
    d = Driver(Chrome)
    ```

### Использование:
*  **Инициализация:** Создайте экземпляр `Driver` с указанным классом WebDriver.
*  **Функциональность:** Используйте методы, такие как `scroll`, `get_url`, `extract_domain` и `page_refresh` для взаимодействия с веб-страницами. Класс также предоставляет методы для выполнения JavaScript и управления cookies.

### Зависимости:
*  **Selenium:** Используется для операций WebDriver, включая поиск элементов, прокрутку и взаимодействие с веб-страницами.
*  **Python Libraries:** Включает `sys`, `pickle`, `time`, `copy`, `pathlib`, `urllib.parse` и другие для различных функций.

## Обзор `executor.py`
   Модуль `executor.py` содержит класс `ExecuteLocator`, который предназначен для выполнения различных действий с элементами веб-страницы с помощью Selenium WebDriver.
   
###  Общая структура и назначение

*   **Основное назначение:** Класс `ExecuteLocator` предназначен для выполнения алгоритмов навигации и взаимодействия с веб-страницей на основе данных конфигурации, предоставленных в виде словарей локаторов.

*   **Основные компоненты:**

    1.  **Импорты и зависимости:**
    ```python
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.remote.webelement import WebElement
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.common.exceptions import NoSuchElementException, TimeoutException
    from src import gs
    from src.utils.printer import pprint, j_loads, j_loads_ns, j_dumps, save_png
    from src.logger.logger import logger
    from src.logger.exceptions import DefaultSettingsException, WebDriverException, ExecuteLocatorException
    ```
        Здесь импортируются необходимые библиотеки и модули, включая Selenium WebDriver для взаимодействия с веб-страницами, а также внутренние модули для настроек, логирования и обработки исключений.

    2.  **Класс `ExecuteLocator`:**
        Класс `ExecuteLocator` является основным компонентом этого файла и содержит методы для выполнения действий с веб-элементами и обработки локаторов. Рассмотрим его методы и атрибуты более подробно.

###  Атрибуты класса:
*  `driver` -  Ссылка на экземпляр WebDriver, используемый для взаимодействия с браузером.
*  `actions` - Экземпляр `ActionChains` для выполнения сложных действий с элементами веб-страницы.
*  `by_mapping` - Словарь, который сопоставляет строковые представления локаторов с объектами Selenium `By`.

### Методы класса:

1.  `__init__(self, driver: webdriver, *args, **kwargs) -> None`
    
    Конструктор класса инициализирует WebDriver и `ActionChains`.

        :param driver: Экземпляр WebDriver.
        :param args: Позиционные аргументы.
        :param kwargs: Именованные аргументы.
2.  `execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]`
   
    Основной метод для выполнения действий на основе локатора.

    :param locator: Словарь с параметрами для выполнения действий.
    :param message: Сообщение для отправки, если необходимо.
    :param typing_speed: Скорость набора текста для отправки сообщений.
    :param continue_on_error: Флаг, указывающий, следует ли продолжать выполнение, если возникает ошибка.
    :return: Результат выполнения локатора.
3.  `get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`
    
    Извлекает элементы, найденные на странице, на основе локатора.

    :param locator: Словарь или `SimpleNamespace` с параметрами локатора.
    :param message: Сообщение для логирования.
    :return: Веб-элемент, список веб-элементов или `False`, если элементы не найдены.
4.  `get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`
    
    Извлекает атрибут из элемента на основе локатора.
    
    :param locator: Словарь или `SimpleNamespace` с параметрами локатора.
    :param message: Сообщение для логирования.
    :return: Атрибут элемента, список атрибутов, словарь или `False`, если атрибут не найден.
5.  `_get_element_attribute(self, element: WebElement, attribute: str) -> str | None`
    
    Вспомогательный метод для извлечения атрибута из веб-элемента.

    :param element: Веб-элемент, атрибут которого необходимо извлечь.
    :param attribute: Имя атрибута.
    :return: Значение атрибута или `None`, если атрибут не найден.
6.  `send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool`
    
    Отправляет сообщение веб-элементу.
    
    :param locator: Словарь или `SimpleNamespace` с параметрами локатора.
    :param message: Сообщение для отправки.
    :param typing_speed: Скорость набора текста.
    :param continue_on_error: Флаг, указывающий, следует ли продолжать выполнение, если возникает ошибка.
    :return: `True`, если сообщение успешно отправлено, `False` в противном случае.
7.  `evaluate_locator(self, attribute: str | list | dict) -> str`
   
    Выполняет оценку атрибута локатора.
    
    :param attribute: Атрибут для оценки.
    :return: Оцененное значение атрибута.
8.  `_evaluate(self, attribute: str) -> str | None`
    
    Вспомогательный метод для оценки одиночного атрибута.

    :param attribute: Атрибут для оценки.
    :return: Оцененное значение атрибута или `None`, если оценка невозможна.
9.  `get_locator_keys() -> list`
    
     Возвращает список доступных ключей локаторов.

        :return: Список ключей локаторов.

### Примеры локаторов

Файл содержит примеры различных локаторов, которые могут использоваться для тестирования.
```json
{
  "product_links": {
    "attribute": "href",
    "by": "xpath",
    "selector": "//div[contains(@id,'node-galery')]//li[contains(@class,'item')]//a",
    "selector 2": "//span[@data-component-type='s-product-image']//a",
    "if_list":"first","use_mouse": false, 
    "mandatory": true,
    "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
  },
    "pagination": {
        "ul": {
            "attribute": null,
            "by": "xpath",
            "selector": "//ul[@class='pagination']",
            "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click()"
        },
        "->": {
            "attribute": null,
            "by": "xpath",
            "selector": "//*[@class = 'ui-pagination-navi util-left']/a[@class='ui-pagination-next']",
            "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click()",
            "if_list":"first","use_mouse": false
        }
    },
    "description": {
        "attribute": [
          null,
          null
        ],
        "by": [
          "xpath",
          "xpath"
        ],
        "selector": [
          "//a[contains(@href, '#tab-description')]",
          "//div[@id = 'tab-description']//p"
        ],
        "timeout":0,"timeout_for_event":"presence_of_element_located","event": [
          "click()",
          null
        ],
        "if_list":"first","use_mouse": [
          false,
          false
        ],
        "mandatory": [
          true,
          true
        ],
        "locator_description": [
          "Clicking on the tab to open the description field",
          "Reading data from div"
        ]
      }
}
```
   
### Примеры кодов клавиш:
   
   ```
    1. KEY.NULL: Представляет нулевой ключ.
    2. KEY.CANCEL: Представляет ключ отмены.
    3. KEY.HELP: Представляет ключ справки.
    4. KEY.BACKSPACE: Представляет клавишу backspace.
    5. KEY.TAB: Представляет клавишу tab.
    6. KEY.CLEAR: Представляет клавишу clear.
    7. KEY.RETURN: Представляет клавишу return.
    8. KEY.ENTER: Представляет клавишу enter.
    9. KEY.SHIFT: Представляет клавишу shift.
    10. KEY.CONTROL: Представляет клавишу control.
    11. KEY.ALT: Представляет клавишу alt.
    12. KEY.PAUSE: Представляет клавишу pause.
    13. KEY.ESCAPE: Представляет клавишу escape.
    14. KEY.SPACE: Представляет клавишу space.
    15. KEY.PAGE_UP: Представляет клавишу page up.
    16. KEY.PAGE_DOWN: Представляет клавишу page down.
    17. KEY.END: Представляет клавишу end.
    18. KEY.HOME: Представляет клавишу home.
    19. KEY.LEFT: Представляет клавишу стрелка влево.
    20. KEY.UP: Представляет клавишу стрелка вверх.
    21. KEY.RIGHT: Представляет клавишу стрелка вправо.
    22. KEY.DOWN: Представляет клавишу стрелка вниз.
    23. KEY.INSERT: Представляет клавишу insert.
    24. KEY.DELETE: Представляет клавишу delete.
    25. KEY.SEMICOLON: Представляет клавишу semicolon.
    26. KEY.EQUALS: Представляет клавишу equals.
    27. KEY.NUMPAD0 through KEY.NUMPAD9: Представляет клавиши numpad от 0 до 9.
    28. KEY.MULTIPLY: Представляет клавишу multiply.
    29. KEY.ADD: Представляет клавишу add.
    30. KEY.SEPARATOR: Представляет клавишу separator.
    31. KEY.SUBTRACT: Представляет клавишу subtract.
    32. KEY.DECIMAL: Представляет клавишу decimal.
    33. KEY.DIVIDE: Представляет клавишу divide.
    34. KEY.F1 through KEY.F12: Представляет функциональные клавиши от F1 до F12.
    35. KEY.META: Представляет клавишу meta.
    ```

## Обзор `chrome.py`

   Модуль `chrome.py` представляет класс для настройки и запуска Chrome WebDriver.

   **Основные характеристики:**

    -  Наследует от `selenium.webdriver.chrome.webdriver.WebDriver`.
    -  Предоставляет дополнительные настройки для запуска Chrome, включая опции, пользовательские агенты и управление расширениями.
    -   Реализует методы для управления процессом Chrome.

   **Компоненты:**

   1.  **Класс `Chrome`**
        *  **Методы:**
        - `__init__(self, *args, **kwargs)`
            
            Конструктор класса, который инициализирует параметры Chrome WebDriver, включая параметры запуска, пользовательский агент, профиль пользователя и настройки для управления окном браузера.

            :param args: Позиционные аргументы.
            :param kwargs: Именованные аргументы.
        -  `_get_chrome_options(self, user_agent: dict = None) -> webdriver.ChromeOptions`
           
            Возвращает параметры Chrome с настроенным пользовательским агентом, если он предоставлен.

            :param user_agent: Словарь с пользовательским агентом.
            :return: Объект `webdriver.ChromeOptions` с настроенными параметрами.

   **Использование:**

    *   **Инициализация:** Создайте экземпляр `Chrome` для запуска Chrome WebDriver с заданными параметрами.
    *   **Функциональность:** Используйте методы `Chrome` для настройки параметров запуска и пользовательского агента.

   **Зависимости:**
   
    *   **Selenium:** Используется для управления Chrome WebDriver.
    *  **`src.utils.jjson`**: Используется для чтения конфигурационных файлов.
    * **`src.logger.logger`**: Используется для логирования ошибок.

## Примеры использования классов и методов

```python
# -*- coding: utf-8 -*-
"""
Примеры использования классов `Driver` и `Chrome`.
====================================================
   
   Этот модуль содержит примеры использования классов `Driver` и `Chrome` для демонстрации основных функций
   и возможностей по взаимодействию с веб-страницами через WebDriver.
   
   
   Примеры использования
   --------------------
   
   Примеры демонстрируют как создать экземпляр драйвера, перейти по ссылке, прокрутить страницу
   и взаимодействовать с элементами на странице.
   
   
   .. code-block:: python
   
    # Пример 1: Создание экземпляра Chrome драйвера и навигация по URL
    chrome_driver = Driver(Chrome)
    if chrome_driver.get_url("https://www.example.com"):
        print("Successfully navigated to the URL")
   """
from src.webdriver.driver import Driver, Chrome
from selenium.webdriver.common.by import By

def main():
    """
    Основная функция для демонстрации примеров использования классов `Driver` и `Chrome`.
    """
    # Пример 1: Создание экземпляра Chrome драйвера и навигация по URL
    chrome_driver = Driver(Chrome)
    if chrome_driver.get_url("https://www.example.com"):
        print("Successfully navigated to the URL")

    # Пример 2: Извлечение домена из URL
    domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
    print(f"Extracted domain: {domain}")

    # Пример 3: Сохранение cookies в локальный файл
    success = chrome_driver._save_cookies_localy()
    if success:
        print("Cookies were saved successfully")

    # Пример 4: Обновление текущей страницы
    if chrome_driver.page_refresh():
        print("Page was refreshed successfully")

    # Пример 5: Прокрутка страницы вниз
    if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
        print("Successfully scrolled the page down")

    # Пример 6: Получение языка текущей страницы
    page_language = chrome_driver.locale
    print(f"Page language: {page_language}")

    # Пример 7: Установка кастомного User-Agent для Chrome драйвера
    user_agent = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
    if custom_chrome_driver.get_url("https://www.example.com"):
        print("Successfully navigated to the URL with custom user agent")

    # Пример 8: Поиск элемента по CSS селектору
    element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
    if element:
        print(f"Found element with text: {element.text}")

    # Пример 9: Получение текущего URL
    current_url = chrome_driver.current_url
    print(f"Current URL: {current_url}")

    # Пример 10: Фокусировка окна, чтобы убрать фокус с элемента
    chrome_driver.window_focus()
    print("Focused the window")

if __name__ == "__main__":
    main()
```

### Примечания

-   Убедитесь, что у вас установлены все зависимости, например `selenium`, `fake_useragent`, и `src` модули, указанные в импортах.
-   Путь к файлу настроек и другим ресурсам должен быть настроен в `gs` (global settings).

Этот файл примеров демонстрирует, как использовать различные методы и функции из `driver.py` и `chrome.py`. Вы можете запускать эти примеры для тестирования работы вашего драйвера и других утилит.

[Объяснение Driver](https://github.com/hypo69/hypo/tree/master/src/webdriver/executor.ru.md)
[Объяснение Executor](https://github.com/hypo69/hypo/tree/master/src/webdriver/executor.ru.md)
[Объяснение локатора](https://github.com/hypo69/hypo/tree/master/src/webdriver/locator.ru.md)
```