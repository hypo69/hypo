# Документация модуля `webdriver`

## Обзор

Модуль `webdriver` предоставляет инструменты для автоматизированного управления веб-браузерами. Включает в себя классы для управления драйверами браузеров (`Driver`, `Chrome`) и выполнения действий на веб-страницах (`ExecuteLocator`).

## Подробней

Этот модуль содержит классы и функции для упрощения взаимодействия с веб-браузерами через Selenium WebDriver. Он предоставляет абстракции для управления браузером, навигации по страницам, выполнения JavaScript-кода и взаимодействия с элементами на странице. Модуль предназначен для использования в задачах автоматизации тестирования, сбора данных и других сценариях, требующих управления браузером из Python-кода.

## Оглавление

- [Классы](#Классы)
    - [`Driver`](#Driver)
- [Примеры использования](#Примеры-использования)

## Классы

### `Driver`

**Описание**:
Класс `Driver` предоставляет расширенную реализацию WebDriver, объединяющую основные функциональности WebDriver с дополнительными методами для взаимодействия с веб-страницами, обработки JavaScript и управления cookie. Он использует возможности Selenium WebDriver и пользовательские расширения для поддержки различных задач автоматизации веб-приложений.

**Как работает класс**:
Класс `Driver` динамически создается на основе переданного класса WebDriver (например, `Chrome`, `Firefox`, `Edge`) и класса `DriverBase`, который содержит основные методы для взаимодействия с веб-страницами. При инициализации класса создаются методы JavaScript и настраивается функциональность для выполнения локаторов.

**Методы**:
- `__init__(self, webdriver_cls, user_agent: dict = None)`: Инициализирует экземпляр класса `Driver`.
- `scroll(self, scrolls: int = 1, direction: str = 'forward', frame_size: int = 1000, delay: float = 0) -> bool`: Прокручивает веб-страницу в указанном направлении.
- `get_url(self, url: str) -> bool`: Открывает указанный URL в браузере.
- `extract_domain(self, url: str) -> str`: Извлекает доменное имя из URL.
- `_save_cookies_localy(self) -> bool`: Сохраняет cookies в локальный файл.
- `page_refresh(self) -> bool`: Обновляет текущую страницу.
- `window_focus(self) -> None`: Фокусирует окно браузера.
- `find_element(self, by, value)`: Находит элемент на странице.
- `locale` (property): Определяет язык страницы.
- `current_url` (property): Возвращает текущий URL страницы.

**Параметры**:
- `webdriver_cls`: Класс WebDriver, который будет использоваться (например, `Chrome`, `Firefox`).
- `user_agent` (dict, optional): Пользовательский User-Agent для браузера. По умолчанию `None`.
- `scrolls` (int, optional): Количество прокруток. По умолчанию `1`.
- `direction` (str, optional): Направление прокрутки (`'forward'`, `'backward'`, `'both'`). По умолчанию `'forward'`.
- `frame_size` (int, optional): Размер фрейма прокрутки. По умолчанию `1000`.
- `delay` (float, optional): Задержка между прокрутками в секундах. По умолчанию `0`.
- `url` (str): URL для открытия.
- `by`: Метод поиска элемента (например, `By.CSS_SELECTOR`).
- `value`: Значение для поиска элемента.

**Примеры**:

```python
from src.webdriver.driver import Driver, Chrome

# Создание экземпляра Chrome драйвера
chrome_driver = Driver(Chrome)

# Открытие URL
if chrome_driver.get_url("https://www.example.com"):
    print("Successfully navigated to the URL")

# Прокрутка страницы вниз
if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
    print("Successfully scrolled the page down")
```

## Примеры использования

- **Создание экземпляра Chrome драйвера и навигация по URL:**

  ```python
  from src.webdriver.driver import Driver, Chrome
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
  from selenium.webdriver.common.by import By
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