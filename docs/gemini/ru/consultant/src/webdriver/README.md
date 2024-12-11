# Received Code

```python
# -*- coding: utf-8 -*-\n\n""" Examples for using `Driver` and `Chrome` classes """\n\nfrom src.webdriver.driver import Driver, Chrome\nfrom selenium.webdriver.common.by import By\n\ndef main():\n    """ Main function to demonStarte usage examples for Driver and Chrome """\n\n    # Example 1: Create a Chrome driver instance and navigate to a URL\n    chrome_driver = Driver(Chrome)\n    if chrome_driver.get_url("https://www.example.com"):\n        print("Successfully navigated to the URL")\n\n    # Example 2: Extract the domain from a URL\n    domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")\n    print(f"Extracted domain: {domain}")\n\n    # Example 3: Save cookies to a local file\n    success = chrome_driver._save_cookies_localy()\n    if success:\n        print("Cookies were saved successfully")\n\n    # Example 4: Refresh the current page\n    if chrome_driver.page_refresh():\n        print("Page was refreshed successfully")\n\n    # Example 5: Scroll the page down\n    if chrome_driver.scroll(scrolls=3, direction=\'forward\', frame_size=1000, delay=1):\n        print("Successfully scrolled the page down")\n\n    # Example 6: Get the language of the current page\n    page_language = chrome_driver.locale\n    print(f"Page language: {page_language}")\n\n    # Example 7: Set a custom user agent for the Chrome driver\n    user_agent = {\n        \'user-agent\': \'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36\'\n    }\n    custom_chrome_driver = Driver(Chrome, user_agent=user_agent)\n    if custom_chrome_driver.get_url("https://www.example.com"):\n        print("Successfully navigated to the URL with custom user agent")\n\n    # Example 8: Find an element by its CSS selector\n    element = chrome_driver.find_element(By.CSS_SELECTOR, \'h1\')\n    if element:\n        print(f"Found element with text: {element.text}")\n\n    # Example 9: Get the current URL\n    current_url = chrome_driver.current_url\n    print(f"Current URL: {current_url}")\n\n    # Example 10: Focus the window to remove focus from the element\n    chrome_driver.window_focus()\n    print("Focused the window")\n\nif __name__ == "__main__":\n    main()\n```

# Improved Code

```python
# -*- coding: utf-8 -*-

"""
Модуль для работы с драйвером WebDriver.
=========================================================================================

Этот модуль содержит примеры использования класса `Driver` для взаимодействия с веб-страницами.
Он предоставляет методы для навигации, взаимодействия с элементами и обработки ошибок.
"""

from src.webdriver.driver import Driver, Chrome
from selenium.webdriver.common.by import By
from src.logger.logger import logger


def main():
    """
    Основная функция для демонстрации использования класса `Driver`.

    Проверяет работу методов драйвера на примерах.
    """

    try:
        # Создание экземпляра драйвера Chrome
        chrome_driver = Driver(Chrome)

        # Проверка навигации по URL
        if chrome_driver.get_url("https://www.example.com"):
            logger.info("Успешно перешли на URL")
        else:
            logger.error("Ошибка перехода на URL")


        # Извлечение домена
        domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
        logger.info(f"Извлеченный домен: {domain}")

        # Сохранение куки
        success = chrome_driver._save_cookies_localy()
        if success:
            logger.info("Куки были сохранены успешно")
        else:
            logger.error("Ошибка сохранения куки")


        # Обновление страницы
        if chrome_driver.page_refresh():
            logger.info("Страница обновлена успешно")
        else:
            logger.error("Ошибка обновления страницы")

        # Прокрутка страницы
        if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
            logger.info("Страница прокручена успешно")
        else:
            logger.error("Ошибка прокрутки страницы")
        
        # Получение языка страницы
        page_language = chrome_driver.locale
        logger.info(f"Язык страницы: {page_language}")

        # Настройка пользовательского User-Agent
        user_agent = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }
        custom_chrome_driver = Driver(Chrome, user_agent=user_agent)

        # Навигация с пользовательским User-Agent
        if custom_chrome_driver.get_url("https://www.example.com"):
            logger.info("Успешно перешли на URL с пользовательским User-Agent")
        else:
            logger.error("Ошибка перехода на URL с пользовательским User-Agent")

        # Поиск элемента
        element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
        if element:
            logger.info(f"Найден элемент с текстом: {element.text}")
        else:
            logger.error("Ошибка поиска элемента")


        # Получение текущего URL
        current_url = chrome_driver.current_url
        logger.info(f"Текущий URL: {current_url}")

        # Фокусировка окна
        chrome_driver.window_focus()
        logger.info("Окно сфокусировано")
        
    except Exception as e:
        logger.exception(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
```

# Changes Made

*   Добавлены импорты `logger` из `src.logger.logger`.
*   Внесены изменения в функцию `main()`:
    *   Код внутри `main()` теперь заключен в блок `try...except`. Это позволит ловить и обрабатывать возможные исключения.
    *   Вместо стандартных блоков `if` , теперь используется `logger.info` и `logger.error` для логирования результатов и ошибок.
    *   Добавлен `logger.exception` для логирования исключений.


# FULL Code

```python
# -*- coding: utf-8 -*-

"""
Модуль для работы с драйвером WebDriver.
=========================================================================================

Этот модуль содержит примеры использования класса `Driver` для взаимодействия с веб-страницами.
Он предоставляет методы для навигации, взаимодействия с элементами и обработки ошибок.
"""

from src.webdriver.driver import Driver, Chrome
from selenium.webdriver.common.by import By
from src.logger.logger import logger


def main():
    """
    Основная функция для демонстрации использования класса `Driver`.

    Проверяет работу методов драйвера на примерах.
    """

    try:
        # Создание экземпляра драйвера Chrome
        chrome_driver = Driver(Chrome)

        # Проверка навигации по URL
        if chrome_driver.get_url("https://www.example.com"):
            logger.info("Успешно перешли на URL")
        else:
            logger.error("Ошибка перехода на URL")


        # Извлечение домена
        domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
        logger.info(f"Извлеченный домен: {domain}")

        # Сохранение куки
        success = chrome_driver._save_cookies_localy()
        if success:
            logger.info("Куки были сохранены успешно")
        else:
            logger.error("Ошибка сохранения куки")


        # Обновление страницы
        if chrome_driver.page_refresh():
            logger.info("Страница обновлена успешно")
        else:
            logger.error("Ошибка обновления страницы")

        # Прокрутка страницы
        if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
            logger.info("Страница прокручена успешно")
        else:
            logger.error("Ошибка прокрутки страницы")
        
        # Получение языка страницы
        page_language = chrome_driver.locale
        logger.info(f"Язык страницы: {page_language}")

        # Настройка пользовательского User-Agent
        user_agent = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }
        custom_chrome_driver = Driver(Chrome, user_agent=user_agent)

        # Навигация с пользовательским User-Agent
        if custom_chrome_driver.get_url("https://www.example.com"):
            logger.info("Успешно перешли на URL с пользовательским User-Agent")
        else:
            logger.error("Ошибка перехода на URL с пользовательским User-Agent")

        # Поиск элемента
        element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
        if element:
            logger.info(f"Найден элемент с текстом: {element.text}")
        else:
            logger.error("Ошибка поиска элемента")


        # Получение текущего URL
        current_url = chrome_driver.current_url
        logger.info(f"Текущий URL: {current_url}")

        # Фокусировка окна
        chrome_driver.window_focus()
        logger.info("Окно сфокусировано")
        
    except Exception as e:
        logger.exception(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
```