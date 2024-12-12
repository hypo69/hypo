# Анализ кода модуля `readme.md`

**Качество кода**
9
-  Плюсы
    -  Документ содержит подробное описание модуля WebDriver и его компонентов.
    -  Включает примеры использования.
    -  Содержит описание основных классов и методов.
    -  Присутствует информация об обработке ошибок.
-  Минусы
    -  Формат документации не соответствует `reStructuredText` (RST).
    -  Отсутствует описание параметров функций в примерах кода.
    -  Некоторые примеры кода могут быть более детализированы.
    -  Некоторые части документации дублируют друг друга.

**Рекомендации по улучшению**
1. **Форматирование:** Перевести всю документацию в формат `reStructuredText` (RST), чтобы обеспечить её совместимость с инструментами генерации документации, такими как Sphinx.
2. **Уточнение примеров кода:** Добавить более подробные комментарии в примерах кода, включая пояснения к параметрам и возвращаемым значениям.
3. **Устранение дублирования:** Избегать дублирования информации, представленной в разных разделах документа.
4. **Логирование ошибок:**  Привести все примеры в соответствии с единым стандартом логирования.
5. **Улучшение описания методов:** Добавить более подробные описания для всех методов, особенно тех, которые выполняют сложные действия.
6. **Оптимизация структуры:** Разбить текст на более мелкие, логически связанные блоки с чёткими заголовками и подзаголовками.
7. **Введение ссылок на другие файлы:** Заменить прямые ссылки на файлы на ссылки на соответствующие страницы документации.

**Оптимизированный код**
```markdown
# Анализ модуля WebDriver

## Обзор
Модуль WebDriver предоставляет фреймворк для навигации и взаимодействия с веб-страницами. Он обрабатывает скрипты и локаторы для выполнения автоматизированных действий над веб-элементами.

## Основные возможности
- **Обработка локаторов**
    - **Инициализация:** Класс `ExecuteLocator` инициализируется экземпляром WebDriver и списком дополнительных аргументов и именованных аргументов. Он настраивает WebDriver и цепочки действий для взаимодействия с веб-элементами.
    - **Выполнение локаторов:** Метод `execute_locator` обрабатывает словарь локаторов, который содержит информацию о том, как находить веб-элементы и взаимодействовать с ними. Он обрабатывает различные типы локаторов и действий на основе предоставленной конфигурации.
    - **Получение элемента:** Метод `get_webelement_by_locator` получает веб-элементы на основе информации о локаторе, такой как XPATH, ID или CSS-селекторы. Он ожидает появления элементов и может вернуть один элемент, список элементов или `False`, если ничего не найдено.
    - **Получение атрибута:** Метод `get_attribute_by_locator` получает атрибуты из элементов, найденных с помощью локатора. Он поддерживает как одиночные, так и множественные элементы.
    - **Отправка сообщения:** Метод `send_message` отправляет текстовый ввод в веб-элементы. Он поддерживает имитацию печати с настраиваемой скоростью ввода и дополнительным взаимодействием мыши.
- **Скриншоты**
    - **Скриншот элемента:** Метод `get_webelement_as_screenshot` делает скриншот веб-элемента и возвращает его в формате PNG. Он поддерживает захват скриншотов нескольких элементов и обрабатывает ошибки, если элементы больше не присутствуют в DOM.
- **Действие клика**
    - **Клик элемента:** Метод `click` выполняет действие клика на веб-элементе, идентифицированном по локатору. Он обрабатывает случаи, когда клик приводит к переходу на новую страницу или открытию нового окна, и регистрирует ошибки, если клик не удался.
- **Оценка локатора**
    - **Оценка атрибута:** Метод `evaluate_locator` оценивает атрибуты локатора, включая обработку особых случаев, когда атрибуты представлены в виде плейсхолдеров (например, `%EXTERNAL_MESSAGE%`).

## Обработка ошибок
Модуль использует блоки `try-except` для перехвата и регистрации ошибок во время различных операций, таких как поиск элементов, отправка сообщений и создание скриншотов. Конкретные исключения, такие как `NoSuchElementException` и `TimeoutException`, перехватываются для обработки случаев, когда элементы не найдены или время ожидания истекло.

## Использование

### Инициализация
Создайте экземпляр `ExecuteLocator` с экземпляром WebDriver.

### Выполнение локатора
Вызовите метод `execute_locator` со словарем локаторов для выполнения действий или получения данных из веб-элементов.

### Обработка результатов
Используйте методы, такие как `get_webelement_by_locator`, `send_message` и `get_webelement_as_screenshot`, для взаимодействия с веб-элементами и обработки результатов.

## Зависимости
Модуль опирается на Selenium для операций WebDriver, включая поиск элементов, отправку клавиш и взаимодействие с веб-страницами. Он также использует встроенные библиотеки Python для обработки исключений и управления временем.

## Пример использования

```python
from src.webdriver.driver import Driver, Chrome
from selenium.webdriver.common.by import By

def main():
    """
    Главная функция для демонстрации примеров использования классов Driver и Chrome.
    """

    # Пример 1: Создание экземпляра драйвера Chrome и переход по URL
    chrome_driver = Driver(Chrome)
    if chrome_driver.get_url("https://www.example.com"):
        print("Успешно выполнен переход по URL")

    # Пример 2: Извлечение домена из URL
    domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
    print(f"Извлеченный домен: {domain}")

    # Пример 3: Сохранение куки в локальный файл
    success = chrome_driver._save_cookies_localy()
    if success:
        print("Куки успешно сохранены")

    # Пример 4: Обновление текущей страницы
    if chrome_driver.page_refresh():
        print("Страница успешно обновлена")

    # Пример 5: Прокрутка страницы вниз
    if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
        print("Страница успешно прокручена вниз")

    # Пример 6: Получение языка текущей страницы
    page_language = chrome_driver.locale
    print(f"Язык страницы: {page_language}")

    # Пример 7: Установка кастомного User-Agent для драйвера Chrome
    user_agent = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
    if custom_chrome_driver.get_url("https://www.example.com"):
        print("Успешно выполнен переход по URL с кастомным user agent")

    # Пример 8: Поиск элемента по CSS-селектору
    element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
    if element:
        print(f"Найден элемент с текстом: {element.text}")

    # Пример 9: Получение текущего URL
    current_url = chrome_driver.current_url
    print(f"Текущий URL: {current_url}")

    # Пример 10: Фокусировка окна, чтобы убрать фокус с элемента
    chrome_driver.window_focus()
    print("Окно сфокусировано")

if __name__ == "__main__":
    main()
```
## Обзор модуля `Driver`

**Описание:**
Модуль `Driver` предоставляет динамическую реализацию WebDriver, которая интегрирует общие функциональные возможности WebDriver с дополнительными методами для взаимодействия с веб-страницами, обработки JavaScript и управления куки. Он использует возможности Selenium WebDriver и пользовательские расширения для поддержки различных задач автоматизации веб-приложений.

**Основные возможности:**
- Наследует от указанного класса WebDriver (например, Chrome, Firefox, Edge) и добавляет дополнительную функциональность.
- Включает методы для прокрутки, обработки куки, взаимодействия с веб-элементами и выполнения JavaScript.
- Предоставляет утилиты для управления окнами браузера и взаимодействия со страницами.

**Компоненты:**

1. **Класс `DriverBase`**
   - **Атрибуты:**
     - `previous_url`: Хранит предыдущий URL.
     - `referrer`: Хранит URL реферера.
     - `page_lang`: Хранит язык страницы.
     - Различные атрибуты, связанные с взаимодействием с веб-элементами и выполнением JavaScript.
   - **Методы:**
     - `scroll`: Прокручивает веб-страницу в указанном направлении. Поддерживает прокрутку вперед, назад или в обоих направлениях.
     - `locale`: Пытается определить язык страницы, проверяя метатеги или используя JavaScript.
     - `get_url`: Загружает указанный URL.
     - `extract_domain`: Извлекает домен из URL.
     - `_save_cookies_localy`: Сохраняет куки в локальный файл.
     - `page_refresh`: Обновляет текущую страницу.
     - `window_focus`: Фокусирует окно браузера с помощью JavaScript.
     - `wait`: Ожидает указанный интервал.

2. **Класс `DriverMeta`**
   - **Методы:**
     - `__call__`: Создает новый класс `Driver`, который объединяет указанный класс WebDriver (например, Chrome, Firefox, Edge) с `DriverBase`. Инициализирует методы JavaScript и функциональность выполнения локаторов.

3. **Класс `Driver`**
   - **Описание:**
     - Динамически созданный класс WebDriver, который наследует от `DriverBase` и указанного класса WebDriver.
   - **Пример использования:**
     ```python
     from src.webdriver.driver import Driver, Chrome, Firefox, Edge
     d = Driver(Chrome)
     ```

**Использование:**
- **Инициализация:** Создайте экземпляр `Driver` с конкретным классом WebDriver.
- **Функциональность:** Используйте такие методы, как `scroll`, `get_url`, `extract_domain` и `page_refresh` для взаимодействия с веб-страницами. Класс также предоставляет методы для выполнения JavaScript и управления куки.

**Зависимости:**
- **Selenium:** Используется для операций WebDriver, включая поиск элементов, прокрутку и взаимодействие с веб-страницами.
- **Библиотеки Python:** Включает `sys`, `pickle`, `time`, `copy`, `pathlib`, `urllib.parse` и другие для различных функций.

## Примеры использования классов и методов

- **Создание экземпляра драйвера Chrome и навигация по URL:**
  ```python
  chrome_driver = Driver(Chrome)
  if chrome_driver.get_url("https://www.example.com"):
      print("Успешно выполнен переход по URL")
  ```

- **Извлечение домена из URL:**
  ```python
  domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
  print(f"Извлеченный домен: {domain}")
  ```

- **Сохранение cookies в локальный файл:**
  ```python
  success = chrome_driver._save_cookies_localy()
  if success:
      print("Cookies успешно сохранены")
  ```

- **Обновление текущей страницы:**
  ```python
  if chrome_driver.page_refresh():
      print("Страница успешно обновлена")
  ```

- **Прокрутка страницы вниз:**
  ```python
  if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
      print("Страница успешно прокручена вниз")
  ```

- **Получение языка текущей страницы:**
  ```python
  page_language = chrome_driver.locale
  print(f"Язык страницы: {page_language}")
  ```

- **Установка кастомного User-Agent для драйвера Chrome:**
  ```python
  user_agent = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
  }
  custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
  if custom_chrome_driver.get_url("https://www.example.com"):
      print("Успешно выполнен переход по URL с кастомным user agent")
  ```

- **Поиск элемента по CSS-селектору:**
  ```python
  element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
  if element:
      print(f"Найден элемент с текстом: {element.text}")
  ```

- **Получение текущего URL:**
  ```python
  current_url = chrome_driver.current_url
  print(f"Текущий URL: {current_url}")
  ```

- **Фокусировка окна, чтобы убрать фокус с элемента:**
  ```python
  chrome_driver.window_focus()
  print("Окно сфокусировано")
  ```

### Примечания
- Убедитесь, что у вас установлены все зависимости, например, `selenium`, `fake_useragent`, и модули `src`, указанные в импортах.
- Путь к файлу настроек и другим ресурсам должен быть настроен в `gs` (global settings).

Этот файл примеров демонстрирует, как использовать различные методы и функции из `driver.py` и `chrome.py`. Вы можете запускать эти примеры для тестирования работы вашего драйвера и других утилит.

## Обзор файла `executor.py`
Файл `executor.py` в модуле `src.webdriver` содержит класс `ExecuteLocator`, предназначенный для выполнения различных действий с веб-элементами на веб-странице с использованием Selenium WebDriver.

### Основное назначение
Класс `ExecuteLocator` предназначен для выполнения навигационных алгоритмов и взаимодействия с веб-страницей на основе конфигурационных данных, представленных в виде словарей локаторов.

### Основные компоненты
1.  **Импорты и зависимости**
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

2.  **Класс `ExecuteLocator`**
    Класс `ExecuteLocator` является основным компонентом этого файла и содержит методы для выполнения действий над веб-элементами и обработки локаторов.

    #### Атрибуты класса
    -   `driver`: Ссылка на экземпляр WebDriver, используемый для взаимодействия с браузером.
    -   `actions`: Экземпляр `ActionChains` для выполнения сложных действий над элементами веб-страницы.
    -   `by_mapping`: Словарь, который отображает строковые представления локаторов на объекты Selenium `By`.

    #### Методы класса
    1.  **`__init__(self, driver, *args, **kwargs)`**
        Конструктор класса инициализирует WebDriver и `ActionChains`:
        ```python
        def __init__(self, driver, *args, **kwargs):
            self.driver = driver
            self.actions = ActionChains(driver)
        ```

    2.  **`execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True)`**
        Основной метод для выполнения действий на основе локатора:
        ```python
        def execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]:
            ...
        ```
        -   `locator`: Словарь с параметрами для выполнения действий.
        -   `message`: Сообщение для отправки, если необходимо.
        -   `typing_speed`: Скорость печати при отправке сообщений.
        -   `continue_on_error`: Флаг, указывающий, следует ли продолжать выполнение при возникновении ошибки.
        Этот метод выбирает, какие действия выполнять, на основе конфигурации локатора.

    3.  **`get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`**
        Получает элементы, найденные на странице, на основе локатора:
        ```python
        def get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool:
            ...
        ```

    4.  **`get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`**
        Получает атрибут из элемента на основе локатора:
        ```python
        def get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool:
            ...
        ```

    5.  **`_get_element_attribute(self, element: WebElement, attribute: str) -> str | None`**
        Вспомогательный метод для получения атрибута из веб-элемента:
        ```python
        def _get_element_attribute(self, element: WebElement, attribute: str) -> str | None:
            ...
        ```

    6.  **`send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error: bool) -> bool`**
        Отправляет сообщение веб-элементу:
        ```python
        def send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error: bool) -> bool:
            ...
        ```

    7.  **`evaluate_locator(self, attribute: str | list | dict) -> str`**
        Оценивает атрибут локатора:
        ```python
        def evaluate_locator(self, attribute: str | list | dict) -> str:
            ...
        ```

    8.  **`_evaluate(self, attribute: str) -> str | None`**
        Вспомогательный метод для оценки одного атрибута:
        ```python
        def _evaluate(self, attribute: str) -> str | None:
            ...
        ```

    9.  **`get_locator_keys() -> list`**
        Возвращает список доступных ключей локатора:
        ```python
        @staticmethod
        def get_locator_keys() -> list:
            ...
        ```

### Примеры локаторов
Файл также содержит примеры различных локаторов, которые могут быть использованы для тестирования:
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
  ...
}
```
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

### Перечисление клавиш
В модуле также определены перечисления клавиш:
1.  `KEY.NULL`: Представляет null-клавишу.
2.  `KEY.CANCEL`: Представляет клавишу отмены.
3.  `KEY.HELP`: Представляет клавишу помощи.
4.  `KEY.BACKSPACE`: Представляет клавишу backspace.
5.  `KEY.TAB`: Представляет клавишу tab.
6.  `KEY.CLEAR`: Представляет клавишу clear.
7.  `KEY.RETURN`: Представляет клавишу return.
8.  `KEY.ENTER`: Представляет клавишу enter.
9.  `KEY.SHIFT`: Представляет клавишу shift.
10. `KEY.CONTROL`: Представляет клавишу control.
11. `KEY.ALT`: Представляет клавишу alt.
12. `KEY.PAUSE`: Представляет клавишу pause.
13. `KEY.ESCAPE`: Представляет клавишу escape.
14. `KEY.SPACE`: Представляет клавишу space.
15. `KEY.PAGE_UP`: Представляет клавишу page up.
16. `KEY.PAGE_DOWN`: Представляет клавишу page down.
17. `KEY.END`: Представляет клавишу end.
18. `KEY.HOME`: Представляет клавишу home.
19. `KEY.LEFT`: Представляет клавишу левой стрелки.
20. `KEY.UP`: Представляет клавишу верхней стрелки.
21. `KEY.RIGHT`: Представляет клавишу правой стрелки.
22. `KEY.DOWN`: Представляет клавишу нижней стрелки.
23. `KEY.INSERT`: Представляет клавишу insert.
24. `KEY.DELETE`: Представляет клавишу delete.
25. `KEY.SEMICOLON`: Представляет клавишу semicolon.
26. `KEY.EQUALS`: Представляет клавишу equals.
27. `KEY.NUMPAD0` через `KEY.NUMPAD9`: Представляют клавиши цифровой панели от 0 до 9.
28. `KEY.MULTIPLY`: Представляет клавишу multiply.
29. `KEY.ADD`: Представляет клавишу add.
30. `KEY.SEPARATOR`: Представляет клавишу separator.
31. `KEY.SUBTRACT`: Представляет клавишу subtract.
32. `KEY.DECIMAL`: Представляет клавишу decimal.
33. `KEY.DIVIDE`: Представляет клавишу divide.
34. `KEY.F1` через `KEY.F12`: Представляют функциональные клавиши от F1 до F12.
35. `KEY.META`: Представляет клавишу meta.

[Driver explanantion](https://github.com/hypo69/hypo/tree/master/src/webdriver/executor.md)
[Executor explanantion](https://github.com/hypo69/hypo/tree/master/src/webdriver/executor.md)
[Locator explanantion](https://github.com/hypo69/hypo/tree/master/src/webdriver/locator.md)
```