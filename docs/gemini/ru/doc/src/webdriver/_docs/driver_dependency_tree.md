# Модуль `src.webdriver.driver`

## Обзор

Данный модуль предоставляет базовый класс для работы с веб-драйверами (Selenium), а также классы для конкретных типов драйверов (Chrome, Firefox, Edge). Он обеспечивает абстракцию над Selenium, позволяя работать с веб-драйверами, используя единый интерфейс.  Модуль включает в себя методы для взаимодействия с элементами веб-страницы, навигации по страницам, работы с cookie и др.

## Оглавление

* [Модуль `src.webdriver.driver`](#модуль-srcwebdriverdriver)
    * [Импорты](#импорты)
    * [Класс `DriverBase`](#класс-driverbase)
        * [Атрибуты](#атрибуты)
        * [Методы](#методы)
    * [Метакласс `DriverMeta`](#метакласс-drivermeta)
        * [Методы](#методы-1)
    * [Класс `Driver`](#класс-driver)
        * [Использование](#использование)

## Импорты

Модуль использует следующие импорты:

* `sys`
* `pickle`
* `time`
* `copy`
* `pathlib.Path`
* `typing`
* `urllib.parse`
* `selenium.webdriver.common.action_chains.ActionChains`
* `selenium.webdriver.common.keys.Keys`
* `selenium.webdriver.common.by.By`
* `selenium.webdriver.support.expected_conditions as EC`
* `selenium.webdriver.support.ui.WebDriverWait`
* `selenium.webdriver.remote.webelement.WebElement`
* `selenium.common.exceptions`
    * `InvalidArgumentException`
    * `ElementClickInterceptedException`
    * `ElementNotInteractableException`
    * `ElementNotVisibleException`
* `src.settings.gs`
* `src.webdriver.executor.ExecuteLocator`
* `src.webdriver.javascript.js.JavaScript`
* `src.utils.pprint`
* `src.logger.logger`
* `src.exceptions.WebDriverException`


## Класс `DriverBase`

**Описание**: Базовый класс для работы с веб-драйверами.

### Атрибуты

* `previous_url: str`: Предыдущий URL-адрес.
* `referrer: str`: Ссылка-источник.
* `page_lang: str`: Язык страницы.
* `ready_state`:  Состояние готовности страницы.
* `get_page_lang()`: Метод для получения языка страницы.
* `unhide_DOM_element()`: Метод для отображения элемента DOM.
* `get_referrer()`: Метод для получения ссылки-источника.
* `window_focus()`: Метод для перефокусировки окна.
* `execute_locator()`: Метод для выполнения локализации.
* `click()`: Метод для клика по элементу.
* `get_webelement_as_screenshot()`: Метод для получения скриншота элемента.
* `get_attribute_by_locator()`: Метод для получения атрибута элемента по локатору.
* `send_message()`: Метод для отправки сообщения.
* `send_key_to_webelement()`: Метод для ввода текста в элемент.


### Методы

* `driver_payload(self)`: Возвращает информацию о драйвере.  Включает в себя методы класса `JavaScript` и `ExecuteLocator`.

* `scroll(self, scrolls: int, frame_size: int, direction: str, delay: float) -> None | bool`: Прокручивает страницу.
    * `scrolls` (int): Количество прокруток.
    * `frame_size` (int): Размер кадра.
    * `direction` (str): Направление прокрутки.
    * `delay` (float): Задержка между прокрутками.


* `carousel(direction: str, scrolls: int, frame_size: int, delay: float) -> bool`:  Прокручивает страницу по типу карусели.
    * `direction` (str): Направление прокрутки.
    * `scrolls` (int): Количество прокруток.
    * `frame_size` (int): Размер кадра.
    * `delay` (float): Задержка между прокрутками.


* `locale(self) -> None | str`: Возвращает локаль браузера.

* `get_url(self, url: str) -> bool`: Переход на URL.
    * `url` (str): Новый URL.

* `extract_domain(self, url: str) -> str`: Извлекает домен из URL.
    * `url` (str): URL для извлечения домена.

* `_save_cookies_localy(self, to_file: str | Path) -> bool`: Сохраняет куки в файл.
    * `to_file` (str | Path): Путь к файлу для сохранения кук.

* `page_refresh(self) -> bool`: Обновляет страницу.

* `wait(self, interval: float)`: Ожидание готовности страницы.
    * `interval` (float): Интервал ожидания.


* `delete_driver_logs(self) -> bool`: Удаляет логи драйвера.



## Метакласс `DriverMeta`

**Описание**: Метакласс для создания классов веб-драйверов.


### Методы

* `__call__(cls, webdriver_cls, *args, **kwargs)`: Создает экземпляр веб-драйвера.
    * `webdriver_cls`: Класс веб-драйвера (Chrome, Firefox, etc.).
    * `*args`: Дополнительные аргументы.
    * `**kwargs`: Дополнительные ключевые аргументы.


## Класс `Driver`

**Описание**: Класс для работы с веб-драйверами.

### Использование

Пример использования:

```python
from src.webdriver.driver import Driver, Chrome, Firefox, Edge

d = Driver(Chrome)
```
```