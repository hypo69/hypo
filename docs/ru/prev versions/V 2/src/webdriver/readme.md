# Документация модуля `webdriver`

## Оглавление

- [Обзор модуля](#обзор-модуля)
- [Классы](#классы)
    - [`DriverBase`](#driverbase)
    - [`DriverMeta`](#drivermeta)
    - [`Driver`](#driver)
    - [`ExecuteLocator`](#executelocator)
- [Примеры использования классов и методов](#примеры-использования-классов-и-методов)
- [Примеры локаторов](#примеры-локаторов)
- [Зависимости](#зависимости)

## Обзор модуля

Модуль `webdriver` предоставляет инструменты для автоматизации взаимодействия с веб-страницами с использованием WebDriver. Он включает классы для управления браузером (`Driver`), выполнения действий на элементах веб-страницы (`ExecuteLocator`) и описания способов поиска элементов (`locator`).

## Классы

### `DriverBase`

**Описание**:
Базовый класс для `Driver`, предоставляющий общие методы для взаимодействия с веб-страницами, такие как прокрутка, получение URL, управление cookies, обновление страницы и управление окном.

**Атрибуты**:
- `previous_url`: (str) Предыдущий URL.
- `referrer`: (str) Реферер URL.
- `page_lang`: (str) Язык страницы.

**Методы**:

#### `scroll`

**Описание**: Прокручивает веб-страницу в указанном направлении.

**Параметры**:
- `scrolls` (int): Количество прокруток.
- `direction` (str): Направление прокрутки (`'forward'`, `'backward'` или `'both'`). По умолчанию `'forward'`.
- `frame_size` (int): Размер кадра прокрутки в пикселях. По умолчанию `1000`.
- `delay` (int): Задержка между прокрутками в секундах. По умолчанию `1`.

**Возвращает**:
- `bool`: `True`, если прокрутка выполнена успешно, `False` в противном случае.

#### `locale`

**Описание**: Пытается определить язык страницы путем проверки мета-тегов или с использованием JavaScript.

**Возвращает**:
- `str`: Язык страницы или `None`, если язык не удалось определить.

#### `get_url`

**Описание**: Загружает указанный URL.

**Параметры**:
- `url` (str): URL для загрузки.

**Возвращает**:
- `bool`: `True`, если URL загружен успешно, `False` в противном случае.

#### `extract_domain`

**Описание**: Извлекает домен из URL.

**Параметры**:
- `url` (str): URL, из которого нужно извлечь домен.

**Возвращает**:
- `str`: Домен или `None`, если домен не удалось извлечь.

#### `_save_cookies_localy`

**Описание**: Сохраняет cookies в локальный файл.

**Возвращает**:
- `bool`: `True`, если cookies сохранены успешно, `False` в противном случае.

#### `page_refresh`

**Описание**: Обновляет текущую страницу.

**Возвращает**:
- `bool`: `True`, если страница обновлена успешно, `False` в противном случае.

#### `window_focus`

**Описание**: Фокусирует окно браузера, используя JavaScript.

**Возвращает**:
- `bool`: `True`, если фокус передан успешно, `False` в противном случае.

#### `wait`

**Описание**: Ожидает указанный интервал времени.

**Параметры**:
- `interval` (int): Интервал ожидания в секундах.

**Возвращает**:
- `None`

### `DriverMeta`

**Описание**:
Метакласс для `Driver`, создающий новый класс `Driver` путем объединения `DriverBase` и указанного класса WebDriver (например, Chrome, Firefox, Edge).

**Методы**:

#### `__call__`

**Описание**: Создает новый класс `Driver`, который сочетает `DriverBase` и указанный класс WebDriver.

**Параметры**:
- `cls` (type): Класс WebDriver (например, Chrome).
- `*args`: Позиционные аргументы для инициализации класса WebDriver.
- `**kwargs`: Именованные аргументы для инициализации класса WebDriver.

**Возвращает**:
- `type`: Новый класс `Driver`.

### `Driver`

**Описание**:
Динамически создаваемый класс WebDriver, наследуемый от `DriverBase` и указанного класса WebDriver.

**Пример использования**:

```python
from src.webdriver.driver import Driver, Chrome, Firefox, Edge
d = Driver(Chrome)
```
### `ExecuteLocator`

**Описание**:
Класс для выполнения действий с веб-элементами на основе данных локатора.

**Атрибуты**:
- `driver`: (webdriver.Chrome | webdriver.Firefox | webdriver.Edge) Экземпляр WebDriver.
- `actions`: (ActionChains) Экземпляр ActionChains для сложных действий.
- `by_mapping`: (dict) Словарь соответствия строковых представлений локаторов объектам `By`.

**Методы**:

#### `__init__`

**Описание**: Инициализирует экземпляр класса `ExecuteLocator`.

**Параметры**:
- `driver` (webdriver.Chrome | webdriver.Firefox | webdriver.Edge): Экземпляр WebDriver.
- `*args`: Дополнительные позиционные аргументы.
- `**kwargs`: Дополнительные именованные аргументы.

**Возвращает**:
- `None`

#### `execute_locator`

**Описание**: Выполняет действие на основе переданного словаря локатора.

**Параметры**:
- `locator` (dict): Словарь с данными локатора.
- `message` (str, optional): Сообщение для отправки (если требуется). По умолчанию `None`.
- `typing_speed` (float, optional): Скорость ввода текста (если требуется). По умолчанию `0`.
- `continue_on_error` (bool, optional): Продолжать выполнение при ошибке (если требуется). По умолчанию `True`.

**Возвращает**:
- `str | list | dict | WebElement | bool`: Результат выполнения локатора.

#### `get_webelement_by_locator`

**Описание**: Возвращает веб-элемент(ы) по данным локатора.

**Параметры**:
- `locator` (dict | SimpleNamespace): Словарь или SimpleNamespace с данными локатора.
- `message` (str, optional): Сообщение для логирования. По умолчанию `None`.

**Возвращает**:
- `WebElement | List[WebElement] | bool`: Веб-элемент, список веб-элементов или `False`, если элемент не найден.

#### `get_attribute_by_locator`

**Описание**: Возвращает атрибут(ы) элемента(ов) по данным локатора.

**Параметры**:
- `locator` (dict | SimpleNamespace): Словарь или SimpleNamespace с данными локатора.
- `message` (str, optional): Сообщение для логирования. По умолчанию `None`.

**Возвращает**:
- `str | list | dict | bool`: Значение атрибута, список значений атрибутов или `False`, если атрибут не найден.

#### `_get_element_attribute`

**Описание**: Возвращает атрибут веб-элемента.

**Параметры**:
- `element` (WebElement): Веб-элемент.
- `attribute` (str): Название атрибута.

**Возвращает**:
- `str | None`: Значение атрибута или `None`, если атрибут не найден.

#### `send_message`

**Описание**: Отправляет сообщение в веб-элемент.

**Параметры**:
- `locator` (dict | SimpleNamespace): Словарь или SimpleNamespace с данными локатора.
- `message` (str): Сообщение для отправки.
- `typing_speed` (float): Скорость ввода текста.
- `continue_on_error` (bool): Продолжать выполнение при ошибке.

**Возвращает**:
- `bool`: `True`, если сообщение отправлено успешно, `False` в противном случае.

#### `evaluate_locator`

**Описание**: Вычисляет значение атрибута локатора.

**Параметры**:
- `attribute` (str | list | dict): Атрибут для вычисления.

**Возвращает**:
- `str`: Вычисленное значение атрибута.

#### `_evaluate`

**Описание**: Вспомогательный метод для вычисления значения атрибута.

**Параметры**:
- `attribute` (str): Атрибут для вычисления.

**Возвращает**:
- `str | None`: Вычисленное значение атрибута или `None`, если значение не найдено.

#### `get_locator_keys`

**Описание**: Возвращает список доступных ключей локатора.

**Возвращает**:
- `list`: Список доступных ключей локатора.

## Примеры использования классов и методов

- **Создание экземпляра Chrome драйвера и навигация по URL:**

  ```python
  chrome_driver = Driver(Chrome)
  if chrome_driver.get_url("https://www.example.com"):
      print("Successfully navigated to the URL")
  ```

- **Извлечение домена из URL:**

  ```python
  domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
  print(f"Extracted domain: {domain}")
  ```

- **Сохранение cookies в локальный файл:**

  ```python
  success = chrome_driver._save_cookies_localy()
  if success:
      print("Cookies were saved successfully")
  ```

- **Обновление текущей страницы:**

  ```python
  if chrome_driver.page_refresh():
      print("Page was refreshed successfully")
  ```

- **Прокрутка страницы вниз:**

  ```python
  if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
      print("Successfully scrolled the page down")
  ```

- **Получение языка текущей страницы:**

  ```python
  page_language = chrome_driver.locale
  print(f"Page language: {page_language}")
  ```

- **Установка кастомного User-Agent для Chrome драйвера:**

  ```python
  user_agent = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
  }
  custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
  if custom_chrome_driver.get_url("https://www.example.com"):
      print("Successfully navigated to the URL with custom user agent")
  ```

- **Поиск элемента по CSS селектору:**

  ```python
  element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
  if element:
      print(f"Found element with text: {element.text}")
  ```

- **Получение текущего URL:**

  ```python
  current_url = chrome_driver.current_url
  print(f"Current URL: {current_url}")
  ```

- **Фокусировка окна, чтобы убрать фокус с элемента:**

  ```python
  chrome_driver.window_focus()
  print("Focused the window")
  ```

## Примеры локаторов

```json
{
  "product_links": {
    "attribute": "href",
    "by": "xpath",
    "selector": "//div[contains(@id,'node-galery')]//li[contains(@class,'item')]//a",
    "selector 2": "//span[@data-component-type='s-product-image']//a",
    "if_list":"first",
    "use_mouse": false,
    "mandatory": true,
    "timeout":0,
    "timeout_for_event":"presence_of_element_located",
    "event": null
  },
  "pagination": {
    "ul": {
      "attribute": null,
      "by": "xpath",
      "selector": "//ul[@class='pagination']",
      "timeout":0,
      "timeout_for_event":"presence_of_element_located",
      "event": "click()"
    },
    "->": {
      "attribute": null,
      "by": "xpath",
      "selector": "//*[@class = 'ui-pagination-navi util-left']/a[@class='ui-pagination-next']",
      "timeout":0,
      "timeout_for_event":"presence_of_element_located",
      "event": "click()",
      "if_list":"first",
      "use_mouse": false
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
    "timeout":0,
    "timeout_for_event":"presence_of_element_located",
    "event": [
      "click()",
      null
    ],
    "if_list":"first",
    "use_mouse": [
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

## Зависимости

- `selenium`: Для работы с WebDriver.
- `src`: Внутренние модули проекта, включая `gs`, `utils`, `printer`, `logger` и `exceptions`.