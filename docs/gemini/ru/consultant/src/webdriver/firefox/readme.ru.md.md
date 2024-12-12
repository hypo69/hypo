# Анализ кода модуля `src.webdriver.firefox`

**Качество кода**

- Соответствие требованиям по оформлению кода: 6/10
  -  Плюсы
    -   Наличие подробной документации к модулю.
    -   Описаны основные классы, методы и их параметры.
    -   Присутствуют примеры использования.
  -  Минусы
    -   Отсутствует документация в формате reStructuredText (RST).
    -   Комментарии в коде отсутствуют.
    -   Не используются `j_loads` и `j_loads_ns` для чтения файлов.
    -   Не используется `from src.logger.logger import logger` для логирования ошибок.
    -   Не все комментарии соответствуют стандарту оформления docstring.

**Рекомендации по улучшению**

1.  Переписать все комментарии в формате reStructuredText (RST).
2.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов (если применимо).
3.  Добавить импорты `from src.logger.logger import logger` и `from src.utils.jjson import j_loads`.
4.  Реализовать логирование ошибок с помощью `logger.error` вместо стандартных `try-except`.
5.  Добавить docstring к каждому методу и классу в формате RST.
6.  Уточнить комментарии, избегая формулировок типа "получаем" и "делаем", использовать конкретные действия, например, "выполняет", "записывает" и т.д.
7.  Добавить проверки на корректность входных данных.

**Оптимизированный код**

```python
"""
Модуль для работы с WebDriver Firefox
=========================================================================================

Этот модуль содержит класс :class:`Firefox`, который расширяет функциональность стандартного WebDriver для Firefox.
Он позволяет настраивать пользовательский профиль, запускать WebDriver в киоске и устанавливать настройки прокси-сервера.

Пример использования
--------------------

Пример использования класса `Firefox`:

.. code-block:: python

    from src.webdriver.firefox import Firefox

    if __name__ == "__main__":
        profile_name = "custom_profile"
        geckodriver_version = "v0.29.0"
        firefox_version = "78.0"
        proxy_file_path = "path/to/proxies.txt"

        # Инициализация и запуск браузера
        browser = Firefox(
            profile_name=profile_name,
            geckodriver_version=geckodriver_version,
            firefox_version=firefox_version,
            proxy_file_path=proxy_file_path
        )
        browser.get("https://www.example.com")
        browser.quit()
"""
from typing import Optional, Any
# from selenium import webdriver # исправлено для импорта только нужных типов
from selenium.webdriver.firefox.options import Options # исправлено для импорта только нужных типов
from selenium.webdriver import Firefox as FirefoxWebDriver # исправлено для импорта только нужных типов
from selenium.webdriver.firefox.service import Service # исправлено для импорта только нужных типов
import random
from fake_useragent import UserAgent

from src.logger.logger import logger
from src.utils.jjson import j_loads # импорт j_loads


class Firefox(FirefoxWebDriver):
    """
    Расширяет стандартный WebDriver для Firefox, добавляя функции:
      - Установка пользовательского профиля
      - Прокси-настройки
      - Установка пользовательского агента
      - Интеграция с JavaScript и исполнение локаторов
    """
    def __init__(self, profile_name: Optional[str] = None,
                 geckodriver_version: Optional[str] = None,
                 firefox_version: Optional[str] = None,
                 user_agent: Optional[str] = None,
                 proxy_file_path: Optional[str] = None,
                 *args, **kwargs) -> None:
        """
        Инициализирует класс Firefox.

        :param profile_name: Имя пользовательского профиля Firefox.
        :param geckodriver_version: Версия geckodriver.
        :param firefox_version: Версия Firefox.
        :param user_agent: Пользовательский агент.
        :param proxy_file_path: Путь к файлу с прокси.
        """
        self.profile_name = profile_name
        self.geckodriver_version = geckodriver_version
        self.firefox_version = firefox_version
        self.user_agent = user_agent
        self.proxy_file_path = proxy_file_path
        self.options = Options()

        if self.user_agent:
            self.options.set_preference("general.useragent.override", self.user_agent)
        else:
            self.options.set_preference("general.useragent.override", UserAgent().random)

        self.options.set_preference("dom.webdriver.enabled", False)
        self.options.set_preference('useAutomationExtension', False)
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.set_proxy(self.options)

        try:
            service = Service(executable_path=f'/opt/geckodriver/{self.geckodriver_version}/geckodriver')
            super().__init__(service=service, options=self.options, *args, **kwargs) # вызывает конструктор родительского класса
        except Exception as ex:
            logger.error(f"Ошибка при инициализации WebDriver: {ex}")
            raise

        self._payload()

    def set_proxy(self, options: Options) -> None:
        """
        Настраивает прокси для Firefox, выбирая случайный рабочий прокси из предоставленного файла.

        :param options: Экземпляр Options для настройки WebDriver.
        """
        if not self.proxy_file_path:
            return

        try:
            # использует j_loads для чтения файла
            with open(self.proxy_file_path, 'r', encoding='utf-8') as f:
                 proxies = j_loads(f) # загружает прокси из файла
        except Exception as e:
            logger.error(f"Ошибка при загрузке прокси из файла: {e}")
            return
        
        if not proxies:
            logger.warning("Список прокси пуст.")
            return

        try:
            proxy = random.choice(proxies) # Выбирает случайный прокси
            options.set_preference('network.proxy.type', 1)
            options.set_preference('network.proxy.http', proxy['host'])
            options.set_preference('network.proxy.http_port', int(proxy['port']))
            options.set_preference('network.proxy.ssl', proxy['host'])
            options.set_preference('network.proxy.ssl_port', int(proxy['port']))
        except Exception as e:
            logger.error(f"Ошибка при установке прокси: {e}")

    def _payload(self) -> None:
        """
        Загружает необходимые исполнительные файлы для локаторов и JavaScript.
        """
        try:
            with open('./src/webdriver/payload.js', 'r', encoding='utf-8') as f:
                self.payload = f.read() # читает содержимое payload.js
            with open('./src/webdriver/execute_locator.js', 'r', encoding='utf-8') as f:
                self.execute_locator_js = f.read()# читает содержимое execute_locator.js
        except Exception as e:
            logger.error(f"Ошибка при загрузке payload: {e}")

    def execute_locator(self, locator: str, *args, **kwargs) -> Any:
        """
        Выполняет JavaScript код для поиска элементов на странице.

        :param locator: Строка с JavaScript кодом локатора.
        :return: Результат выполнения JavaScript-кода.
        """
        try:
            #  выполняет JavaScript код и возвращает результат
            return self.execute_script(self.execute_locator_js.replace('{{locator}}', locator), *args, **kwargs)
        except Exception as ex:
            logger.error(f'Ошибка выполнения execute_locator: {ex}')
            return None
```