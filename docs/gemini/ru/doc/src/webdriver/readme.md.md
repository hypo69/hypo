# Документация модуля `webdriver`

## Оглавление

- [Обзор](#обзор)
- [Классы](#классы)
    - [`ExecuteLocator`](#execute-locator)
    - [`Driver`](#driver)
- [Примеры использования](#примеры-использования)
- [Зависимости](#зависимости)
- [Примеры локаторов](#примеры-локаторов)
- [Клавиши Selenium](#клавиши-selenium)
- [Дополнительные ссылки](#дополнительные-ссылки)

## Обзор

Модуль `webdriver` предоставляет функциональность для автоматизации взаимодействия с веб-страницами через WebDriver. Он включает в себя классы для управления браузером (`Driver`), выполнения действий над элементами страницы (`ExecuteLocator`), и определения локаторов для поиска элементов.

## Классы

### `ExecuteLocator`

#### Описание

Класс `ExecuteLocator` предназначен для выполнения действий над веб-элементами на основе переданных локаторов. Он использует Selenium WebDriver для взаимодействия со страницей и выполняет такие действия, как отправка сообщений, клики, получение атрибутов и создание скриншотов.

#### Методы

* `__init__(self, driver, *args, **kwargs)`
    **Описание:** Конструктор класса. Инициализирует экземпляр `ExecuteLocator` с драйвером WebDriver.

    **Параметры:**
    - `driver`: Экземпляр WebDriver.
    - `*args`: Произвольные позиционные аргументы.
    - `**kwargs`: Произвольные именованные аргументы.
    
    **Возвращает:**
    - `None`

* `execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> str | list | dict | WebElement | bool`

    **Описание:** Выполняет действия над веб-элементом(ами) на основе предоставленного локатора.

    **Параметры:**
    - `locator` (dict): Словарь с параметрами локатора.
    - `message` (str, optional): Сообщение для отправки в элемент. По умолчанию `None`.
    - `typing_speed` (float, optional): Скорость печати сообщения. По умолчанию `0`.
    - `continue_on_error` (bool, optional): Флаг, определяющий, продолжать ли выполнение при ошибке. По умолчанию `True`.

    **Возвращает:**
    - `str | list | dict | WebElement | bool`: Результат выполнения действия.

    **Вызывает исключения:**
    - `ExecuteLocatorException`: Если возникает ошибка во время выполнения локатора.

* `get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`

    **Описание:** Возвращает веб-элемент(ы), найденный по локатору.

    **Параметры:**
    - `locator` (dict | SimpleNamespace): Локатор в виде словаря или `SimpleNamespace`.
    - `message` (str, optional): Дополнительное сообщение для логирования. По умолчанию `None`.

    **Возвращает:**
    - `WebElement | List[WebElement] | bool`: Найденный элемент(ы) или `False`, если элемент не найден.

    **Вызывает исключения:**
    - `NoSuchElementException`: Если элемент не найден в DOM.
    - `TimeoutException`: Если истекло время ожидания элемента.

* `get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`
    **Описание:** Возвращает атрибут элемента, найденного по локатору.
    
    **Параметры:**
    - `locator` (dict | SimpleNamespace): Локатор элемента.
    - `message` (str, optional): Сообщение для логирования. По умолчанию `None`.

    **Возвращает:**
    - `str | list | dict | bool`: Значение атрибута элемента.

    **Вызывает исключения:**
    - `NoSuchElementException`: Если элемент не найден в DOM.
    - `TimeoutException`: Если истекло время ожидания элемента.

* `_get_element_attribute(self, element: WebElement, attribute: str) -> str | None`
    **Описание:** Получает значение атрибута веб-элемента.
    
    **Параметры:**
    - `element` (WebElement): Веб-элемент.
    - `attribute` (str): Название атрибута.

    **Возвращает:**
    - `str | None`: Значение атрибута или `None`, если атрибут не найден.

* `send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool`

    **Описание:** Отправляет сообщение в веб-элемент.

    **Параметры:**
    - `locator` (dict | SimpleNamespace): Локатор элемента.
    - `message` (str): Сообщение для отправки.
    - `typing_speed` (float): Скорость печати сообщения.
    - `continue_on_error` (bool): Флаг для продолжения работы при ошибке.

    **Возвращает:**
    - `bool`: `True` в случае успешной отправки сообщения, иначе `False`.

    **Вызывает исключения:**
    - `NoSuchElementException`: Если элемент не найден в DOM.
    - `TimeoutException`: Если истекло время ожидания элемента.

* `evaluate_locator(self, attribute: str | list | dict) -> str`

    **Описание:** Вычисляет атрибут локатора.

    **Параметры:**
    - `attribute` (str | list | dict): Атрибут для вычисления.

    **Возвращает:**
    - `str`: Вычисленное значение атрибута.

* `_evaluate(self, attribute: str) -> str | None`
    **Описание:** Вычисляет одиночный атрибут локатора.

    **Параметры:**
    - `attribute` (str): Атрибут для вычисления.
    
    **Возвращает:**
    - `str | None`: Вычисленное значение атрибута или `None`, если не удалось вычислить.

* `@staticmethod get_locator_keys() -> list`
    **Описание:** Возвращает список доступных ключей локаторов.
    
    **Возвращает:**
    - `list`: Список ключей.

### `Driver`

#### Описание

Класс `Driver` предоставляет расширенную функциональность для управления браузером, наследуясь от указанного драйвера (например, Chrome). Он включает методы для скроллинга, работы с cookies, выполнения JavaScript и т.д.

#### Методы
-   `__init__(self, driver_class, *args, **kwargs)`
    
    **Описание:** Конструктор класса. Инициализирует экземпляр `Driver` с указанным классом WebDriver и передает ему дополнительные аргументы.

    **Параметры:**
    - `driver_class` (class): Класс драйвера (например, `Chrome`, `Firefox`, `Edge`).
    - `*args`: Позиционные аргументы, передаваемые в конструктор `driver_class`.
    - `**kwargs`: Именованные аргументы, передаваемые в конструктор `driver_class`.

    **Возвращает:**
        - None
   
-   `scroll(self, scrolls: int = 3, direction: str = 'forward', frame_size: int = 1000, delay: float = 1) -> bool`
    
    **Описание:** Прокручивает страницу в указанном направлении.
    
    **Параметры:**
    - `scrolls` (int, optional): Количество прокруток. По умолчанию `3`.
    - `direction` (str, optional): Направление прокрутки (`forward` или `backward`). По умолчанию `forward`.
    - `frame_size` (int, optional): Размер прокрутки в пикселях. По умолчанию `1000`.
    - `delay` (float, optional): Задержка между прокрутками в секундах. По умолчанию `1`.
        
    **Возвращает:**
        - `bool`: `True` если прокрутка выполнена успешно, `False` в противном случае.
        
-   `locale`

    **Описание:** Свойство, возвращающее язык текущей страницы.
    
    **Возвращает:**
    - `str | None`: Язык страницы или `None`, если не удалось определить.

-   `get_url(self, url: str, wait_page_load:bool=True, wait_time:int=10) -> bool`
    
    **Описание:** Открывает указанный URL.
    
    **Параметры:**
    - `url` (str): URL для загрузки.
    - `wait_page_load` (bool, optional): Нужно ли дождаться загрузки страницы. По умолчанию `True`.
    - `wait_time` (int, optional): Время ожидания загрузки страницы. По умолчанию `10`.

    **Возвращает:**
        - `bool`: `True` если URL загружен успешно, `False` в противном случае.

-   `extract_domain(self, url: str) -> str | None`
    
    **Описание:** Извлекает домен из URL.
    
    **Параметры:**
    - `url` (str): URL для извлечения домена.
        
    **Возвращает:**
    - `str | None`: Доменное имя или `None` если не удалось извлечь.

-   `_save_cookies_localy(self) -> bool`

    **Описание:** Сохраняет cookies в локальный файл.

    **Возвращает:**
    - `bool`: `True` если сохранение выполнено успешно, `False` в противном случае.

-   `page_refresh(self) -> bool`

    **Описание:** Обновляет текущую страницу.

    **Возвращает:**
        - `bool`: `True` если обновление выполнено успешно, `False` в противном случае.

-  `window_focus(self) -> None`
 
    **Описание:** Фокусирует окно браузера, используя JavaScript.
    
    **Возвращает:**
        - `None`.

-   `wait(self, interval: int = 1) -> None`
    
    **Описание:** Ожидает указанное время.
    
    **Параметры:**
        - `interval` (int, optional): Время ожидания в секундах. По умолчанию `1`.
    
    **Возвращает:**
        - `None`

## Примеры использования

```python
from src.webdriver.driver import Driver, Chrome
from selenium.webdriver.common.by import By

def main():
    # Создание экземпляра Chrome драйвера и навигация по URL
    chrome_driver = Driver(Chrome)
    if chrome_driver.get_url("https://www.example.com"):
        print("Successfully navigated to the URL")

    # Извлечение домена из URL
    domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
    print(f"Extracted domain: {domain}")

    # Сохранение cookies в локальный файл
    success = chrome_driver._save_cookies_localy()
    if success:
        print("Cookies were saved successfully")

    # Обновление текущей страницы
    if chrome_driver.page_refresh():
        print("Page was refreshed successfully")

    # Прокрутка страницы вниз
    if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
        print("Successfully scrolled the page down")

    # Получение языка текущей страницы
    page_language = chrome_driver.locale
    print(f"Page language: {page_language}")

    # Установка кастомного User-Agent для Chrome драйвера
    user_agent = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
    if custom_chrome_driver.get_url("https://www.example.com"):
        print("Successfully navigated to the URL with custom user agent")

    # Поиск элемента по CSS селектору
    element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
    if element:
        print(f"Found element with text: {element.text}")

    # Получение текущего URL
    current_url = chrome_driver.current_url
    print(f"Current URL: {current_url}")

    # Фокусировка окна, чтобы убрать фокус с элемента
    chrome_driver.window_focus()
    print("Focused the window")

if __name__ == "__main__":
    main()
```

## Зависимости

- **Selenium**: Используется для управления браузером, поиска элементов и взаимодействия со страницей.
- **Python**: Стандартные библиотеки Python, такие как `sys`, `pickle`, `time`, `copy`, `pathlib`, `urllib.parse`.
- **Внутренние модули**: `src.gs`, `src.utils.printer`, `src.logger.logger`, `src.logger.exceptions`.

## Примеры локаторов

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

## Клавиши Selenium

```
KEY.NULL
KEY.CANCEL
KEY.HELP
KEY.BACKSPACE
KEY.TAB
KEY.CLEAR
KEY.RETURN
KEY.ENTER
KEY.SHIFT
KEY.CONTROL
KEY.ALT
KEY.PAUSE
KEY.ESCAPE
KEY.SPACE
KEY.PAGE_UP
KEY.PAGE_DOWN
KEY.END
KEY.HOME
KEY.LEFT
KEY.UP
KEY.RIGHT
KEY.DOWN
KEY.INSERT
KEY.DELETE
KEY.SEMICOLON
KEY.EQUALS
KEY.NUMPAD0
KEY.NUMPAD1
KEY.NUMPAD2
KEY.NUMPAD3
KEY.NUMPAD4
KEY.NUMPAD5
KEY.NUMPAD6
KEY.NUMPAD7
KEY.NUMPAD8
KEY.NUMPAD9
KEY.MULTIPLY
KEY.ADD
KEY.SEPARATOR
KEY.SUBTRACT
KEY.DECIMAL
KEY.DIVIDE
KEY.F1
KEY.F2
KEY.F3
KEY.F4
KEY.F5
KEY.F6
KEY.F7
KEY.F8
KEY.F9
KEY.F10
KEY.F11
KEY.F12
KEY.META
```

## Дополнительные ссылки

- [Driver explanantion](https://github.com/hypo69/hypo/tree/master/src/webdriver/executor.md)
- [Executor explanantion](https://github.com/hypo69/hypo/tree/master/src/webdriver/executor.md)
- [Locator explanantion](https://github.com/hypo69/hypo/tree/master/src/webdriver/locator.md)