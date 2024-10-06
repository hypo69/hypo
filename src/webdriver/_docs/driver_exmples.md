
```python
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" Examples for using `Driver` and `Chrome` classes """

from src.webdriver import Driver, Chrome
from selenium.webdriver.common.by import By

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

if __name__ == "__main__":
    main()
```

### Примеры использования классов и методов

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