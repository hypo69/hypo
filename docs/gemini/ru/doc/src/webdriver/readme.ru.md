# Модуль `webdriver`

## Обзор

Модуль предоставляет функциональность для управления и взаимодействия с веб-страницами через WebDriver. Он включает в себя классы для создания драйверов браузера, выполнения действий с элементами и управления общим поведением веб-драйвера.

## Содержание

- [Классы](#классы)
  - [`Driver`](#класс-driver)
  - [`Chrome`](#класс-chrome)
- [Примеры использования](#примеры-использования)
- [Дополнительные ресурсы](#дополнительные-ресурсы)

## Классы

### `Driver`

**Описание**:
Класс `Driver` предоставляет динамическую реализацию WebDriver, интегрируя основные функции WebDriver с дополнительными методами для взаимодействия с веб-страницами, обработки JavaScript и управления cookies. Он использует возможности Selenium WebDriver и пользовательские расширения для поддержки различных задач веб-автоматизации.

**Атрибуты:**
- `previous_url`: Сохраняет предыдущий URL.
- `referrer`: Сохраняет URL реферера.
- `page_lang`: Сохраняет язык страницы.
- Различные атрибуты, связанные с взаимодействием с веб-элементами и выполнением JavaScript.

**Методы:**

- `__init__(self, driver_class, *args, **kwargs)`
    
    **Описание**: Инициализирует экземпляр класса `Driver`.
        
    **Параметры**:
        - `driver_class`: Класс WebDriver, который будет использоваться (например, `Chrome`, `Firefox`, `Edge`).
        - `*args`: Позиционные аргументы, передаваемые в конструктор WebDriver.
        - `**kwargs`: Именованные аргументы, передаваемые в конструктор WebDriver.
    
- `scroll(self, scrolls: int = 1, direction: str = 'forward', frame_size: int = 1000, delay: float = 0.5) -> bool`
    
    **Описание**: Прокручивает веб-страницу в указанном направлении.
        
    **Параметры**:
        - `scrolls` (int, optional): Количество прокруток. По умолчанию `1`.
        - `direction` (str, optional): Направление прокрутки (`forward` или `backward`). По умолчанию `forward`.
        - `frame_size` (int, optional): Размер кадра прокрутки в пикселях. По умолчанию `1000`.
        - `delay` (float, optional): Задержка между прокрутками в секундах. По умолчанию `0.5`.
        
    **Возвращает**:
        - bool: `True`, если прокрутка выполнена успешно, иначе `False`.
        
    **Вызывает исключения**:
       - `WebDriverException`: Если произошла ошибка во время выполнения прокрутки.

- `locale(self) -> str | None`
    
    **Описание**: Определяет язык страницы, проверяя метатеги или используя JavaScript.
        
    **Параметры**:
        - Нет параметров.
        
    **Возвращает**:
        - str | None: Язык страницы (например, `ru`, `en`), или `None`, если язык не удалось определить.
        
- `get_url(self, url: str, is_js_load: bool = False, continue_on_error: bool = False) -> bool`
    
    **Описание**: Загружает указанный URL.
        
    **Параметры**:
        - `url` (str): URL для загрузки.
        - `is_js_load` (bool, optional): Если `True`, использует JavaScript для загрузки. По умолчанию `False`.
        - `continue_on_error` (bool, optional): Если `True`, продолжает выполнение при ошибке. По умолчанию `False`.
        
    **Возвращает**:
        - bool: `True`, если URL загружен успешно, иначе `False`.

- `extract_domain(self, url: str) -> str | None`
    
    **Описание**: Извлекает домен из URL.
        
    **Параметры**:
        - `url` (str): URL, из которого нужно извлечь домен.
        
    **Возвращает**:
        - str | None: Домен из URL, или `None`, если не удалось извлечь.

- `_save_cookies_localy(self) -> bool`
    
    **Описание**: Сохраняет cookies в локальный файл.
        
    **Параметры**:
        - Нет параметров.
        
    **Возвращает**:
        - bool: `True`, если cookies сохранены успешно, иначе `False`.
        
    **Вызывает исключения**:
       - `WebDriverException`: Если произошла ошибка во время сохранения cookies.

- `page_refresh(self) -> bool`
    
    **Описание**: Обновляет текущую страницу.
        
    **Параметры**:
        - Нет параметров.
        
    **Возвращает**:
        - bool: `True`, если страница обновлена успешно, иначе `False`.

- `window_focus(self) -> bool`
    
    **Описание**: Фокусирует окно браузера, используя JavaScript.
        
    **Параметры**:
        - Нет параметров.
        
    **Возвращает**:
        - bool: `True`, если окно сфокусировано успешно, иначе `False`.
        
    **Вызывает исключения**:
       - `WebDriverException`: Если произошла ошибка во время фокусировки окна.

- `wait(self, interval: float = 0.5) -> bool`
   
    **Описание**: Выполняет ожидание в течение заданного интервала.
        
    **Параметры**:
        - `interval` (float, optional): Интервал ожидания в секундах. По умолчанию `0.5`.
        
    **Возвращает**:
         - bool: Всегда `True`, если ожидание прошло успешно.

- `find_element(self, by: str, selector: str) -> WebElement | None`

   **Описание**: Ищет один элемент на странице.
   
   **Параметры**:
        - `by` (str): Метод поиска элемента (`By.CSS_SELECTOR`, `By.XPATH`, и т.д.).
        - `selector` (str): Строка селектора для поиска.
        
   **Возвращает**:
        - WebElement | None: Найденный элемент или `None`, если не найден.
        
   **Вызывает исключения**:
       - `WebDriverException`: Если произошла ошибка во время поиска элемента.

- `current_url(self) -> str | None`

   **Описание**: Возвращает текущий URL страницы.
    
   **Параметры**:
       - Нет параметров.

   **Возвращает**:
       - str | None: Текущий URL или `None`, если не удается получить.

### `Chrome`

**Описание**:
Класс `Chrome` предоставляет конфигурацию и функциональность для работы с браузером Chrome через WebDriver.

**Методы:**
- `__init__(self, *args, **kwargs)`
    
    **Описание**: Инициализирует экземпляр класса `Chrome`.
        
    **Параметры**:
        - `*args`: Позиционные аргументы, передаваемые в конструктор Chrome WebDriver.
        - `**kwargs`: Именованные аргументы, передаваемые в конструктор Chrome WebDriver.

## Примеры использования

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
## Дополнительные ресурсы

- [Объяснение Driver](https://github.com/hypo69/hypo/tree/master/src/webdriver/executor.ru.md)
- [Объяснение Executor](https://github.com/hypo69/hypo/tree/master/src/webdriver/executor.ru.md)
- [Объяснение локатора](https://github.com/hypo69/hypo/tree/master/src/webdriver/locator.ru.md)