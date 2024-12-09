# Модуль `src.webdriver.driver`

## Обзор

Данный модуль предоставляет базовый класс для управления веб-драйверами (например, Chrome, Firefox, Edge) и содержит методы для взаимодействия с веб-страницей. Он основан на Selenium и предоставляет абстракцию для упрощения работы с разными типами драйверов.

## Оглавление

* [Модуль `src.webdriver.driver`](#модуль-srcwebdriverdriver)
* [Класс `DriverBase`](#класс-driverbase)
* [Класс `Driver`](#класс-driver)
* [Класс `DriverMeta`](#класс-drivermeta)

## Класс `DriverBase`

**Описание**: Базовый класс для взаимодействия с веб-драйвером.  Обеспечивает общие методы для работы с различными типами драйверов.

**Атрибуты**:

* `previous_url` (str): Предыдущий URL страницы.
* `referrer` (str): URL предыдущей страницы.
* `page_lang` (str): Язык страницы.
* `ready_state`: Состояние готовности страницы.
* `get_page_lang()`: Возвращает язык страницы.
* `unhide_DOM_element()`: Показывает элемент DOM.
* `get_referrer()`: Возвращает URL предыдущей страницы.
* `window_focus()`: Фокусирует окно браузера.
* `execute_locator()`: Выполняет локатор.
* `click()`: Нажимает на элемент.
* `get_webelement_as_screenshot()`: Возвращает скриншот элемента.
* `get_attribute_by_locator()`: Возвращает значение атрибута элемента по локатору.
* `send_message()`: Отправляет сообщение.
* `send_key_to_webelement()`: Вводит текст в элемент.


**Методы**:

* `driver_payload(self)`: Возвращает данные драйвера. 
* `scroll(self, scrolls: int, frame_size: int, direction: str, delay: float) -> None | bool`: Прокручивает страницу.
    * `scrolls` (int): Количество прокруток.
    * `frame_size` (int): Размер кадра.
    * `direction` (str): Направление прокрутки (например, "up", "down").
    * `delay` (float): Задержка между прокрутками.
* `locale(self) -> None | str`: Возвращает локаль браузера.
* `get_url(self, url: str) -> bool`: Загружает URL.
    * `url` (str): URL для загрузки.
* `extract_domain(self, url: str) -> str`: Извлекает домен из URL.
    * `url` (str): URL.
* `_save_cookies_localy(self, to_file: str | Path) -> bool`: Сохраняет куки в файл.
    * `to_file` (str | Path): Путь к файлу.
* `page_refresh(self) -> bool`: Обновляет страницу.
* `wait(self, interval: float)`: Ожидание.
    * `interval` (float): Интервал ожидания.
* `delete_driver_logs(self) -> bool`: Удаляет логи драйвера.



## Класс `Driver`

**Описание**:  Класс, реализующий интерфейс для работы с разными драйверами.  Он использует метакласс `DriverMeta` для создания конкретных драйверов (Chrome, Firefox, Edge).

**Использование примера**:
```python
from src.webdriver.driver import Driver, Chrome
d = Driver(Chrome)
```

## Класс `DriverMeta`

**Описание**:  Метакласс для создания конкретных драйверов.  Он принимает класс веб-драйвера (например, `Chrome`, `Firefox`) и инициализирует экземпляр, используя его как базовый класс.

**Методы**:

* `__call__(cls, webdriver_cls, *args, **kwargs)`: Создает экземпляр веб-драйвера.
    * `webdriver_cls`: Класс веб-драйвера (например, `Chrome`).
    * `*args`, `**kwargs`: Аргументы и ключевые аргументы для инициализации веб-драйвера.