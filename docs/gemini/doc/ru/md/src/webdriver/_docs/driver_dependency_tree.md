# Модуль `src.webdriver.driver`

## Обзор

Данный модуль предоставляет базовый класс для работы с веб-драйверами Selenium, обеспечивая общие методы для управления браузером, взаимодействия с элементами и обработки различных ситуаций.

## Оглавление

* [src.webdriver.driver.DriverBase](#driverbase)
* [src.webdriver.driver.DriverMeta](#drivermeta)
* [src.webdriver.driver.Driver](#driver)

## Класс `DriverBase`

**Описание**: Базовый класс для работы с веб-драйверами.  Он содержит общие атрибуты и методы для взаимодействия с браузером, такие как управление URL, локалем, перехода по ссылкам, обработка исключений и т.д.

**Атрибуты**:

- `previous_url: str`: Предыдущий URL адрес.
- `referrer: str`: Ссылка, с которой был переходе на текущую страницу.
- `page_lang: str`: Язык страницы.
- `ready_state`: Статус готовности страницы.
- `get_page_lang()`: Возвращает язык страницы.
- `unhide_DOM_element()`: Метод для отображения элементов.
- `get_referrer()`: Метод для получения referer.
- `window_focus()`: Метод для фокусировки окна браузера.
- `execute_locator()`: Метод для выполнения локейтора.
- `click()`: Метод для клика по элементу.
- `get_webelement_as_screenshot()`: Метод для получения скриншота элемента.
- `get_attribute_by_locator()`: Метод для получения атрибута элемента.
- `send_message()`: Метод для отправки сообщения.
- `send_key_to_webelement()`: Метод для отправки нажатий клавиш на элемент.

**Методы**:

- `driver_payload(self)`: Возвращает данные драйвера.
- `scroll(self, scrolls: int, frame_size: int, direction: str, delay: float) -> None | bool`: Прокрутка страницы.
    - `scrolls`: Количество прокруток.
    - `frame_size`: Размер кадра прокрутки.
    - `direction`: Направление прокрутки (например, "up", "down").
    - `delay`: Задержка между прокрутками.
    - `Возвращает`: `None` или `bool` (успешность выполнения).
- `locale(self) -> None | str`: Возвращает локаль страницы.
- `get_url(self, url: str) -> bool`: Загрузка URL.
    - `url`: URL для загрузки.
    - `Возвращает`: `bool` (успешность выполнения).
- `extract_domain(self, url: str) -> str`: Извлечение домена из URL.
    - `url`: URL для извлечения домена.
    - `Возвращает`: Строка с доменом.
- `_save_cookies_localy(self, to_file: str | Path) -> bool`: Сохранение куки.
    - `to_file`: Путь к файлу для сохранения.
    - `Возвращает`: `bool` (успешность выполнения).
- `page_refresh(self) -> bool`: Обновление страницы.
    - `Возвращает`: `bool` (успешность выполнения).
- `wait(self, interval: float)`: Ожидание загрузки страницы.
    - `interval`: Задержка ожидания в секундах.
- `delete_driver_logs(self) -> bool`: Удаление логов драйвера.
    - `Возвращает`: `bool` (успешность выполнения).


## Класс `DriverMeta`

**Описание**: Метакласс для управления созданием экземпляров класса `Driver`.

**Методы**:

- `__call__(cls, webdriver_cls, *args, **kwargs)`:  Метод вызывается при создании экземпляра класса `Driver`.
    - `webdriver_cls`: Класс веб-драйвера (например, `Chrome`, `Firefox`).
    - `*args`, `**kwargs`: Дополнительные аргументы и ключевые аргументы, передаваемые при создании объекта веб-драйвера.
    - `Возвращает`: Объект `Driver`, инициализированный выбранным веб-драйвером.


## Класс `Driver`

**Описание**: Основной класс для работы с веб-драйверами, использующий метакласс `DriverMeta`.

**Использование**:

```python
from src.webdriver import Driver, Chrome
d = Driver(Chrome)
```