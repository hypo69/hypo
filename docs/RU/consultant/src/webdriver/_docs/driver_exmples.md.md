# Анализ кода модуля `driver_exmples.md`

**Качество кода**
9
 -  Плюсы
    - Код хорошо структурирован и содержит примеры использования основных методов `Driver` и `Chrome`.
    - Примеры наглядно демонстрируют функциональность каждого метода.
    - Код содержит комментарии и пояснения.
    - Наличие примеров кода для каждого метода делает документацию понятной.
 -  Минусы
    - Отсутствует reStructuredText (RST) в docstring.
    - Используются стандартные комментарии вместо reStructuredText (RST).
    - Отсутствует обработка ошибок в примерах, что делает их неполными.
    - Код содержит не все необходимые импорты, такие как `from src.logger.logger import logger`.
    - Используется прямой вызов `_save_cookies_localy`, что может подразумевать необходимость пересмотра приватности этого метода.
    - Нет docstring для модуля и функции `main`.

**Рекомендации по улучшению**
1.  Переписать docstring и комментарии к функциям, методам и модулю в формате reStructuredText (RST).
2.  Добавить импорт `from src.logger.logger import logger` для логирования ошибок.
3.  Использовать `logger.error` для обработки ошибок в методах `Driver`.
4.  Избегать прямого вызова `_save_cookies_localy` и пересмотреть необходимость его публичного использования.
5.  Добавить docstring для модуля и функции `main`.
6.  Добавить обработку ошибок в примерах кода, чтобы они были более надежными.
7.  Использовать одинарные кавычки `'` вместо двойных `"` в Python коде.

**Оптимизированный код**

```python
"""
Модуль с примерами использования классов `Driver` и `Chrome`.
=====================================================================

Этот модуль содержит примеры использования классов `Driver` и `Chrome`
из пакета `src.webdriver` для демонстрации основных возможностей управления браузером.

Примеры использования
---------------------
    Примеры включают навигацию по URL, извлечение домена, сохранение кук,
    обновление страницы, прокрутку, получение языка страницы, установку user-agent,
    поиск элементов, получение текущего URL и фокусировку окна.

    .. code-block:: python

        from src.webdriver.driver import Driver, Chrome
        from selenium.webdriver.common.by import By

        def main():
            # Пример 1: Создание экземпляра драйвера Chrome и навигация по URL
            chrome_driver = Driver(Chrome)
            if chrome_driver.get_url('https://www.example.com'):
                print('Successfully navigated to the URL')

            # Пример 2: Извлечение домена из URL
            domain = chrome_driver.extract_domain('https://www.example.com/path/to/page')
            print(f'Extracted domain: {domain}')

            # Пример 3: Сохранение cookies в локальный файл
            success = chrome_driver._save_cookies_localy()
            if success:
                print('Cookies were saved successfully')

            # Пример 4: Обновление текущей страницы
            if chrome_driver.page_refresh():
                print('Page was refreshed successfully')

            # Пример 5: Прокрутка страницы вниз
            if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
                print('Successfully scrolled the page down')

            # Пример 6: Получение языка текущей страницы
            page_language = chrome_driver.locale
            print(f'Page language: {page_language}')

            # Пример 7: Установка кастомного user agent для Chrome драйвера
            user_agent = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
            }
            custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
            if custom_chrome_driver.get_url('https://www.example.com'):
                print('Successfully navigated to the URL with custom user agent')

            # Пример 8: Поиск элемента по CSS селектору
            element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
            if element:
                print(f'Found element with text: {element.text}')

            # Пример 9: Получение текущего URL
            current_url = chrome_driver.current_url
            print(f'Current URL: {current_url}')

            # Пример 10: Фокусировка окна
            chrome_driver.window_focus()
            print('Focused the window')

        if __name__ == '__main__':
            main()
"""
from src.webdriver.driver import Driver, Chrome
from selenium.webdriver.common.by import By
# импорт logger для логирования ошибок
from src.logger.logger import logger


def main():
    """
    Основная функция для демонстрации примеров использования классов `Driver` и `Chrome`.

    Функция демонстрирует различные способы использования драйвера для
    управления браузером, включая навигацию по URL, извлечение домена,
    сохранение кук, обновление страницы, прокрутку, получение языка страницы,
    установку user-agent, поиск элементов, получение текущего URL и
    фокусировку окна.
    """
    # Пример 1: Создание экземпляра драйвера Chrome и навигация по URL
    # создаем экземпляр драйвера Chrome
    chrome_driver = Driver(Chrome)
    # проверяем успешность навигации по URL
    if chrome_driver.get_url('https://www.example.com'):
        print('Successfully navigated to the URL')

    # Пример 2: Извлечение домена из URL
    # извлекаем домен из URL
    domain = chrome_driver.extract_domain('https://www.example.com/path/to/page')
    print(f'Extracted domain: {domain}')

    # Пример 3: Сохранение cookies в локальный файл
    # сохраняем cookies в локальный файл
    success = chrome_driver._save_cookies_localy()
    # проверяем успешность сохранения
    if success:
        print('Cookies were saved successfully')

    # Пример 4: Обновление текущей страницы
    # обновляем текущую страницу
    if chrome_driver.page_refresh():
        print('Page was refreshed successfully')

    # Пример 5: Прокрутка страницы вниз
    # прокручиваем страницу вниз
    if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
        print('Successfully scrolled the page down')

    # Пример 6: Получение языка текущей страницы
    # получаем язык текущей страницы
    page_language = chrome_driver.locale
    print(f'Page language: {page_language}')

    # Пример 7: Установка кастомного user agent для Chrome драйвера
    # создаем словарь с кастомным user agent
    user_agent = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    # создаем экземпляр драйвера с кастомным user agent
    custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
    # проверяем успешность навигации по URL с кастомным user agent
    if custom_chrome_driver.get_url('https://www.example.com'):
        print('Successfully navigated to the URL with custom user agent')

    # Пример 8: Поиск элемента по CSS селектору
    # ищем элемент по CSS селектору
    element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
    # проверяем наличие элемента и выводим его текст
    if element:
        print(f'Found element with text: {element.text}')

    # Пример 9: Получение текущего URL
    # получаем текущий URL
    current_url = chrome_driver.current_url
    print(f'Current URL: {current_url}')

    # Пример 10: Фокусировка окна
    # фокусируем окно
    chrome_driver.window_focus()
    print('Focused the window')


if __name__ == '__main__':
    main()
```

### Примеры использования классов и методов

- **Создание экземпляра Chrome драйвера и навигация по URL:**

  ```python
  chrome_driver = Driver(Chrome)
  if chrome_driver.get_url('https://www.example.com'):
      print('Successfully navigated to the URL')
  ```

- **Извлечение домена из URL:**

  ```python
  domain = chrome_driver.extract_domain('https://www.example.com/path/to/page')
  print(f'Extracted domain: {domain}')
  ```

- **Сохранение cookies в локальный файл:**

  ```python
  success = chrome_driver._save_cookies_localy()
  if success:
      print('Cookies were saved successfully')
  ```

- **Обновление текущей страницы:**

  ```python
  if chrome_driver.page_refresh():
      print('Page was refreshed successfully')
  ```

- **Прокрутка страницы вниз:**

  ```python
  if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
      print('Successfully scrolled the page down')
  ```

- **Получение языка текущей страницы:**

  ```python
  page_language = chrome_driver.locale
  print(f'Page language: {page_language}')
  ```

- **Установка кастомного User-Agent для Chrome драйвера:**

  ```python
  user_agent = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
  }
  custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
  if custom_chrome_driver.get_url('https://www.example.com'):
      print('Successfully navigated to the URL with custom user agent')
  ```

- **Поиск элемента по CSS селектору:**

  ```python
  element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
  if element:
      print(f'Found element with text: {element.text}')
  ```

- **Получение текущего URL:**

  ```python
  current_url = chrome_driver.current_url
  print(f'Current URL: {current_url}')
  ```

- **Фокусировка окна, чтобы убрать фокус с элемента:**

  ```python
  chrome_driver.window_focus()
  print('Focused the window')
  ```

### Примечания

- Убедитесь, что у вас установлены все зависимости, например `selenium`, `fake_useragent`, и `src` модули, указанные в импортах.
- Путь к файлу настроек и другим ресурсам должен быть настроен в `gs` (global settings).

Этот файл примеров демонстрирует, как использовать различные методы и функции из `driver.py` и `chrome.py`. Вы можете запускать эти примеры для тестирования работы вашего драйвера и других утилит.