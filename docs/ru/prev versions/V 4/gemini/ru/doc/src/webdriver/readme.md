# Документация модуля `webdriver`

## Оглавление

- [Обзор](#обзор)
- [Подробнее](#подробнее)
- [Классы](#классы)
  - [`Driver`](#driver)
- [Функции](#функции)
  - [`main`](#main)

## Обзор

Модуль `webdriver` предоставляет классы для управления веб-драйверами, такие как `Driver` и `Chrome`. Он содержит функции для навигации по веб-страницам, извлечения данных и выполнения различных действий с использованием Selenium WebDriver.

## Подробнее

Модуль включает класс `Driver`, который является базовым классом для управления веб-драйверами, и класс `Chrome`, который является производным классом для управления браузером Chrome. В модуле также реализованы функции для выполнения основных действий, таких как открытие URL, извлечение домена, сохранение cookies, обновление страницы и прокрутка.

Этот код используется для автоматизации действий в браузере, что полезно для тестирования веб-приложений, сбора данных и выполнения других задач, требующих взаимодействия с веб-страницами.

## Классы

### `Driver`

**Описание**: Базовый класс для управления веб-драйверами. Предоставляет методы для навигации, взаимодействия с элементами страницы, управления cookies и выполнения JavaScript.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Driver` с указанным типом драйвера (например, `Chrome`).
- `get_url`: Открывает указанный URL в браузере.
- `extract_domain`: Извлекает домен из URL.
- `_save_cookies_localy`: Сохраняет cookies в локальный файл.
- `page_refresh`: Обновляет текущую страницу.
- `scroll`: Прокручивает страницу вниз или вверх.
- `window_focus`: Фокусирует окно браузера.

**Параметры**:
- `driver_type` (Type[webdriver]): Тип веб-драйвера для использования (например, `Chrome`).
- `user_agent` (Optional[dict], optional): Пользовательский user-agent для установки. По умолчанию `None`.

**Примеры**:

```python
from src.webdriver.driver import Driver, Chrome

# Создание экземпляра Chrome драйвера
chrome_driver = Driver(Chrome)

# Открытие URL
if chrome_driver.get_url("https://www.example.com"):
    print("Successfully navigated to the URL")
```

## Функции

### `main`

```python
def main():
    """ Main function to demonstrate usage examples for Driver and Chrome """
    # Example 1: Create a Chrome driver instance and navigate to a URL
    chrome_driver = Driver(Chrome)
    if chrome_driver.get_url("https://www.example.com"):
        print("Successfully navigated to the URL")

    # Example 2: Extract the domain from a URL
    domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
    print(f"Extracted domain: {domain}")

    # Example 3: Save cookies to a local file
    success = chrome_driver._save_cookies_localy()
    if success:
        print("Cookies were saved successfully")

    # Example 4: Refresh the current page
    if chrome_driver.page_refresh():
        print("Page was refreshed successfully")

    # Example 5: Scroll the page down
    if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
        print("Successfully scrolled the page down")

    # Example 6: Get the language of the current page
    page_language = chrome_driver.locale
    print(f"Page language: {page_language}")

    # Example 7: Set a custom user agent for the Chrome driver
    user_agent = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
    if custom_chrome_driver.get_url("https://www.example.com"):
        print("Successfully navigated to the URL with custom user agent")

    # Example 8: Find an element by its CSS selector
    element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
    if element:
        print(f"Found element with text: {element.text}")

    # Example 9: Get the current URL
    current_url = chrome_driver.current_url
    print(f"Current URL: {current_url}")

    # Example 10: Focus the window to remove focus from the element
    chrome_driver.window_focus()
    print("Focused the window")
```

**Описание**: Функция `main` демонстрирует примеры использования классов `Driver` и `Chrome` для выполнения различных действий в браузере, таких как навигация по URL, извлечение домена, сохранение cookies, обновление страницы, прокрутка и фокусировка окна.

**Примеры**:

```python
# Запуск функции main
if __name__ == "__main__":
    main()