# Модуль affiliate_links_shortener_scenario

## Обзор

Модуль `affiliate_links_shortener_scenario` предназначен для генерации сокращенных партнерских ссылок AliExpress через веб-браузер. Он использует Selenium WebDriver для автоматизации действий на странице сокращения ссылок и получения короткой ссылки.

## Подробней

Этот модуль предоставляет функцию `get_short_affiliate_link`, которая принимает полную URL и возвращает сокращенную версию, пригодную для использования в партнерских программах. Модуль включает обработку ошибок, логирование и проверку корректности сгенерированной ссылки. Он также обеспечивает открытие и закрытие вкладок браузера для проверки короткой ссылки.

## Функции

### `get_short_affiliate_link`

```python
def get_short_affiliate_link(d:Driver, url: str) -> str:
    """ Script for generating a shortened affiliate link
    @param url `str`: Full URL
    @returns `str`: Shortened URL
    """
```

**Описание**: Генерирует сокращенную партнерскую ссылку на основе переданного URL.

**Параметры**:
- `d` (Driver): Экземпляр WebDriver, используемый для управления браузером.
- `url` (str): Полный URL, который необходимо сократить.

**Возвращает**:
- `str`: Сокращенный URL.

**Вызывает исключения**:
- Отсутствуют явные исключения, но в коде закомментированы `ValueError`, которые могут быть активированы при необходимости.

**Примеры**:

```python
from src.webdriver.driver import Driver
from selenium import webdriver

# Пример использования функции
# Предположим, что у вас уже есть настроенный драйвер
# d = Driver(webdriver.Chrome())
# url = "https://aliexpress.com/some_product_url"
# short_url = get_short_affiliate_link(d, url)
# print(short_url)