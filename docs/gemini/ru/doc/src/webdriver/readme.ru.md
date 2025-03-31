# Модуль `webdriver`

## Обзор

Модуль `webdriver` предоставляет инструменты для автоматизации взаимодействия с веб-страницами с использованием WebDriver. Он включает классы для управления драйверами браузеров (например, Chrome) и выполнения действий на веб-страницах, таких как навигация, ввод текста, клики и получение скриншотов. Модуль также обеспечивает обработку ошибок и ведение журнала для облегчения отладки и поддержки.

## Подробней

Этот модуль предназначен для автоматизации тестирования веб-приложений, сбора данных и выполнения других задач, требующих взаимодействия с веб-страницами. Он предоставляет абстракции для работы с WebDriver, упрощая выполнение распространенных операций и обеспечивая гибкость для реализации сложных сценариев.

## Содержание

- [Классы](#классы)
  - [`Driver`](#driver)
  - [`Chrome`](#chrome)
- [Примеры использования классов и методов](#примеры-использования-классов-и-методов)

## Классы

### `Driver`

**Описание**:
Класс `Driver` предоставляет динамическую реализацию WebDriver, которая объединяет общие функциональные возможности WebDriver с дополнительными методами для взаимодействия с веб-страницами, обработки JavaScript и управления файлами cookie. Он использует возможности Selenium WebDriver и пользовательские расширения для поддержки различных задач автоматизации веб-интерфейса.

**Как работает класс**:
Класс `Driver` использует метакласс `DriverMeta` для динамического создания класса WebDriver, который наследуется от указанного класса WebDriver (например, Chrome, Firefox, Edge) и `DriverBase`. Он инициализирует методы JavaScript и функциональные возможности выполнения локатора.

**Методы**:
- `__init__(self, web_driver_cls, user_agent: Optional[dict] = None)`: Инициализирует экземпляр класса `Driver`.
- `scroll(self, scrolls: int = 1, direction: str = 'forward', frame_size: int = 600, delay: float = 0.5) -> bool`: Прокручивает веб-страницу в указанном направлении.
- `locale(self) -> str | None`: Пытается определить язык страницы, проверяя метатеги или используя JavaScript.
- `get_url(self, url: str, sleep: int = 0) -> bool`: Загружает указанный URL.
- `extract_domain(self, url: str) -> str`: Извлекает домен из URL.
- `_save_cookies_localy(self) -> bool`: Сохраняет cookies в локальный файл.
- `page_refresh(self) -> bool`: Обновляет текущую страницу.
- `window_focus(self) -> None`: Фокусирует окно браузера с помощью JavaScript.
- `wait(self, interval: float = 0.5) -> None`: Ждет указанный интервал.
- `find_element(self, by, selector: str) -> WebElement | None`: Находит элемент на странице по указанному селектору.
- `current_url(self) -> str`: Возвращает текущий URL страницы.

**Параметры**:
- `web_driver_cls`: Класс WebDriver, который будет использоваться (например, Chrome, Firefox).
- `user_agent` (Optional[dict], optional): Пользовательский user-agent для драйвера Chrome. По умолчанию `None`.
- `scrolls` (int, optional): Количество прокруток страницы. По умолчанию `1`.
- `direction` (str, optional): Направление прокрутки (`'forward'`, `'backward'` или `'both'`). По умолчанию `'forward'`.
- `frame_size` (int, optional): Размер кадра прокрутки в пикселях. По умолчанию `600`.
- `delay` (float, optional): Задержка между прокрутками в секундах. По умолчанию `0.5`.
- `url` (str): URL для загрузки.
- `sleep` (int, optional): Время ожидания после загрузки страницы в секундах. По умолчанию `0`.
- `by`: Метод поиска элемента (например, `By.CSS_SELECTOR`, `By.XPATH`).
- `selector` (str): Селектор для поиска элемента.
- `interval` (float, optional): Интервал ожидания в секундах. По умолчанию `0.5`.

**Возвращает**:
- `scroll` (bool): `True`, если прокрутка выполнена успешно, `False` в противном случае.
- `locale` (str | None): Язык страницы или `None`, если язык не удалось определить.
- `get_url` (bool): `True`, если URL загружен успешно, `False` в противном случае.
- `extract_domain` (str): Домен из URL.
- `_save_cookies_localy` (bool): `True`, если cookies сохранены успешно, `False` в противном случае.
- `page_refresh` (bool): `True`, если страница обновлена успешно, `False` в противном случае.
- `find_element` (WebElement | None): Найденный элемент или `None`, если элемент не найден.
- `current_url` (str): Текущий URL страницы.
- `None`: `window_focus`, `wait`.

**Вызывает исключения**:
- Не вызывает исключений напрямую, но методы WebDriver могут вызывать исключения, такие как `TimeoutException` или `NoSuchElementException`.

**Примеры**:
```python
from src.webdriver.driver import Driver, Chrome

# Создание экземпляра Chrome драйвера и навигация по URL
chrome_driver = Driver(Chrome)
if chrome_driver.get_url("https://www.example.com"):
    print("Successfully navigated to the URL")

# Извлечение домена из URL
domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
print(f"Extracted domain: {domain}")

# Прокрутка страницы вниз
if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
    print("Successfully scrolled the page down")

# Получение языка текущей страницы
page_language = chrome_driver.locale
print(f"Page language: {page_language}")
```

### `Chrome`

**Описание**:
Класс `Chrome` - это просто псевдоним для класса `selenium.webdriver.chrome.webdriver.WebDriver`.

**Как работает класс**:
Он используется для создания экземпляров драйвера Chrome, которые можно использовать для управления браузером Chrome.

**Методы**:
- Нет явно определенных методов, поскольку это псевдоним для класса `WebDriver` из Selenium.

**Параметры**:
- Параметры, которые можно передать в конструктор `selenium.webdriver.chrome.webdriver.WebDriver`.

**Возвращает**:
- Экземпляр класса `selenium.webdriver.chrome.webdriver.WebDriver`.

**Вызывает исключения**:
- Могут быть вызваны исключения, связанные с инициализацией драйвера Chrome, например, если драйвер Chrome не установлен или несовместим.

**Примеры**:
```python
from src.webdriver.driver import Driver, Chrome

# Создание экземпляра Chrome драйвера
chrome_driver = Driver(Chrome)
```

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