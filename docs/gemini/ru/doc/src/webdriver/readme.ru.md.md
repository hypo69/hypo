# Модуль `webdriver`

## Обзор

Модуль `webdriver` предоставляет функциональность для управления веб-браузером с помощью Selenium WebDriver. Включает в себя классы и функции для создания драйверов, взаимодействия с веб-страницами и выполнения различных действий на веб-элементах.

## Содержание

- [Класс `Driver`](#класс-driver)
    - [Описание](#описание)
    - [Методы](#методы)
- [Класс `Chrome`](#класс-chrome)
    - [Описание](#описание-1)
    - [Методы](#методы-1)
- [Примеры использования классов и методов](#примеры-использования-классов-и-методов)

## Класс `Driver`

### Описание
Класс `Driver` предоставляет динамическую реализацию WebDriver, интегрируя основные функции WebDriver с дополнительными методами для взаимодействия с веб-страницами, обработки JavaScript и управления cookies. Он использует возможности Selenium WebDriver и пользовательские расширения для поддержки различных задач веб-автоматизации.

### Методы

#### `__init__(self, webdriver_class, *args, user_agent: Optional[dict] = None, **kwargs)`

**Описание**: Конструктор класса `Driver`, инициализирует WebDriver и устанавливает пользовательский User-Agent, если он предоставлен.

**Параметры**:

- `webdriver_class` (Type[webdriver.Chrome | webdriver.Firefox | webdriver.Edge]): Класс WebDriver, который будет использоваться.
- `*args` (list): Позиционные аргументы, передаваемые в класс WebDriver.
- `user_agent` (Optional[dict], optional): Словарь с пользовательским User-Agent. По умолчанию `None`.
- `**kwargs` (dict): Именованные аргументы, передаваемые в класс WebDriver.

**Возвращает**:
- `None`: Метод не возвращает значения.

#### `scroll(self, scrolls: int = 1, direction: str = 'forward', frame_size: int = 1000, delay: float = 1) -> bool`
**Описание**: Прокручивает веб-страницу в заданном направлении.

**Параметры**:
- `scrolls` (int, optional): Количество прокруток. По умолчанию `1`.
- `direction` (str, optional): Направление прокрутки ('forward', 'backward', 'both'). По умолчанию `forward`.
- `frame_size` (int, optional): Размер кадра прокрутки. По умолчанию `1000`.
- `delay` (float, optional): Задержка между прокрутками в секундах. По умолчанию `1`.

**Возвращает**:
- `bool`: Возвращает `True` если прокрутка прошла успешно, иначе `False`.

#### `locale() -> str | None`
**Описание**: Определяет язык текущей страницы, используя метатеги или JavaScript.

**Параметры**:
    - Нет

**Возвращает**:
    - `str | None`: Язык страницы или `None`, если язык не удалось определить.

#### `get_url(self, url: str) -> bool`
**Описание**: Загружает указанный URL.

**Параметры**:
- `url` (str): URL, который нужно загрузить.

**Возвращает**:
- `bool`: Возвращает `True` если страница была загружена успешно, иначе `False`.

#### `extract_domain(self, url: str) -> str`

**Описание**: Извлекает домен из URL.

**Параметры**:
- `url` (str): URL, из которого нужно извлечь домен.

**Возвращает**:
- `str`: Извлеченный домен.

#### `_save_cookies_localy(self) -> bool`

**Описание**: Сохраняет cookies в локальный файл.

**Параметры**:
    - Нет

**Возвращает**:
- `bool`: Возвращает `True` если cookies были сохранены успешно, иначе `False`.

#### `page_refresh(self) -> bool`

**Описание**: Обновляет текущую страницу.

**Параметры**:
    - Нет

**Возвращает**:
- `bool`: Возвращает `True` если страница была обновлена успешно, иначе `False`.

#### `window_focus(self) -> bool`

**Описание**: Фокусирует окно браузера с помощью JavaScript.

**Параметры**:
    - Нет

**Возвращает**:
- `bool`: Возвращает `True` если фокус был установлен успешно, иначе `False`.

#### `wait(self, seconds: int) -> None`

**Описание**: Ожидает указанное количество секунд.

**Параметры**:
- `seconds` (int): Количество секунд для ожидания.

**Возвращает**:
- `None`: Метод не возвращает значения.

## Класс `Chrome`

### Описание

Класс `Chrome` представляет собой класс для управления браузером Chrome. Он наследуется от `selenium.webdriver.chrome.webdriver.WebDriver`, предоставляя стандартный функционал для работы с Chrome через Selenium.

### Методы

#### `__init__(self, *args, user_agent: Optional[dict] = None, **kwargs)`

**Описание**: Конструктор класса `Chrome`, инициализирует Chrome WebDriver с возможностью установки пользовательского User-Agent.

**Параметры**:
- `*args` (list): Позиционные аргументы, передаваемые в класс `webdriver.Chrome`.
- `user_agent` (Optional[dict], optional): Словарь с пользовательским User-Agent. По умолчанию `None`.
- `**kwargs` (dict): Именованные аргументы, передаваемые в класс `webdriver.Chrome`.

**Возвращает**:
- `None`: Метод не возвращает значения.

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

### Примечания

- Убедитесь, что у вас установлены все зависимости, например `selenium`, `fake_useragent`, и `src` модули, указанные в импортах.
- Путь к файлу настроек и другим ресурсам должен быть настроен в `gs` (global settings).

Этот файл примеров демонстрирует, как использовать различные методы и функции из `driver.py` и `chrome.py`. Вы можете запускать эти примеры для тестирования работы вашего драйвера и других утилит.