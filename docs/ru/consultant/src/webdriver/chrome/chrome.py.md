### Анализ кода модуля `src.webdriver.chrome`

**Качество кода**:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код хорошо структурирован и разбит на логические блоки.
    - Используются `pathlib` для работы с путями, что делает код более кроссплатформенным.
    - Присутствует базовая обработка ошибок.
    - Логирование выполняется с помощью кастомного логгера.
- **Минусы**:
    - Использование `hasattr` для проверки наличия атрибутов в объекте настроек может быть заменено на более явные проверки.
    - Некоторые комментарии могут быть более информативными.
    - Не все функции имеют docstring в формате RST.
    - Отсутствует обработка конкретных исключений при работе с прокси.
    - В `_payload` методе есть дублирование, `self.send_message = self.send_key_to_webelement`, можно упростить код.

**Рекомендации по улучшению**:
1. **Улучшение документации**:
   - Добавить **RST** документацию для всех методов и класса.
   - Улучшить комментарии, сделать их более точными и информативными.

2. **Обработка ошибок**:
    - Обрабатывать конкретные исключения при работе с прокси, например, `requests.exceptions.RequestException`.
    - Использовать `logger.error` для логирования ошибок вместо прямого вывода.

3. **Рефакторинг кода**:
    - Заменить `hasattr` на более явные проверки (например, `if settings.get('options')`).
    - В `_payload` методе убрать дублирование, оставить `self.send_message =  execute_locator.send_message`, а в `execute_locator` переименовать `send_message` на `send_key_to_webelement`.
    - Использовать f-строки для форматирования строк, где это применимо.
    - Вынести повторяющуюся логику в отдельные методы.
    - Избегать множественного использования  `try-except` блоков, использовать `logger.error` с передачей ошибок.

4. **Конфигурация**:
    - Перенести логику обработки настроек в отдельный метод, чтобы уменьшить длину конструктора класса.
    - Сделать проверку существования файла с настройками.

5. **Форматирование**:
    - Привести код в соответствие со стандартом PEP8, выровнять объявления переменных, импорты.

**Оптимизированный код**:
```python
"""
rst
.. module:: src.webdriver.chrome
    :synopsys: Модуль для работы с WebDriver Chrome
"""
import os
import random
from pathlib import Path
from typing import Optional, List

from selenium.common.exceptions import WebDriverException
from selenium.webdriver import Chrome as WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent

from src import gs
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns
from src.webdriver.executor import ExecuteLocator
from src.webdriver.js import JavaScript
from src.webdriver.proxy import check_proxy, get_proxies_dict


class Chrome(WebDriver):
    """
    Расширение для `webdriver.Chrome` с дополнительной функциональностью.

    :param profile_name: Имя пользовательского профиля Chrome.
    :type profile_name: Optional[str]
    :param chromedriver_version: Версия chromedriver.
    :type chromedriver_version: Optional[str]
    :param user_agent: Пользовательский агент в формате строки.
    :type user_agent: Optional[str]
    :param proxy_file_path: Путь к файлу с прокси.
    :type proxy_file_path: Optional[str]
    :param options: Список опций для Chrome.
    :type options: Optional[List[str]]
    :param window_mode: Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.)
    :type window_mode: Optional[str]
    """
    driver_name: str = 'chrome'

    def __init__(
        self,
        profile_name: Optional[str] = None,
        chromedriver_version: Optional[str] = None,
        user_agent: Optional[str] = None,
        proxy_file_path: Optional[str] = None,
        options: Optional[List[str]] = None,
        window_mode: Optional[str] = None,
        *args,
        **kwargs,
    ) -> None:
        """
        Инициализирует драйвер Chrome с заданными параметрами.

        :param profile_name: Имя профиля пользователя Chrome.
        :type profile_name: Optional[str]
        :param chromedriver_version: Версия ChromeDriver.
        :type chromedriver_version: Optional[str]
        :param user_agent: User-Agent для браузера.
        :type user_agent: Optional[str]
        :param proxy_file_path: Путь к файлу с прокси.
        :type proxy_file_path: Optional[str]
        :param options: Список дополнительных опций для Chrome.
        :type options: Optional[List[str]]
        :param window_mode: Режим окна браузера ('kiosk', 'windowless', 'full_window').
        :type window_mode: Optional[str]
        """
        service = None
        options_obj = None

        settings = self._load_settings()  # Загрузка настроек из файла
        if not settings:
            return  # Если файл настроек не загружен, выходим.
        chromedriver_path: str = str(Path(gs.path.root, settings.get('executable_path', {}).get('chromedriver')))
        service = Service(chromedriver_path) # Инициализация сервиса

        options_obj = Options()  # Инициализация опций Chrome

        self._apply_options_from_settings(options_obj, settings)  # Применение опций из файла настроек
        self._apply_window_mode(options_obj, settings, window_mode) # Применение режима окна
        self._apply_additional_options(options_obj, options) # Применение дополнительных опций
        self._set_user_agent(options_obj, user_agent) # Установка user-agent
        self._set_proxy_if_enabled(options_obj, settings)  # Установка прокси если включено

        profile_directory = self._get_profile_directory(settings, profile_name) # Получение директории профиля
        options_obj.add_argument(f"--user-data-dir={profile_directory}") # Добавление директории профиля

        try:
            logger.info('Запуск Chrome WebDriver')
            super().__init__(service=service, options=options_obj) # Инициализация WebDriver
            self._payload() # Загрузка payload для WebDriver
        except WebDriverException as ex:
            logger.critical(
                """
                    ---------------------------------
                        Ошибка запуска WebDriver
                        Возможные причины:
                        - Обновление Chrome
                        - Отсутствие Chrome на ОС
                    ----------------------------------""",
                ex,
            )
            return  # Явный возврат при ошибке
        except Exception as ex:
            logger.critical('Ошибка работы Chrome WebDriver:', ex)
            return  # Явный возврат при ошибке

    def _load_settings(self) -> Optional[dict]:
        """
        Загружает настройки из JSON файла.

        :return: Словарь с настройками или None в случае ошибки.
        :rtype: Optional[dict]
        """
        settings_path = Path(gs.path.src / 'webdriver' / 'chrome' / 'chrome.json')
        try:
            if not settings_path.exists():
                logger.error(f"Файл настроек не найден: {settings_path}")
                return None
            settings = j_loads_ns(settings_path)
            return settings
        except Exception as ex:
            logger.error(f"Ошибка при загрузке настроек: {ex}")
            return None

    def _apply_options_from_settings(self, options_obj: Options, settings: dict) -> None:
        """
        Применяет опции из файла настроек к объекту Options.

        :param options_obj: Объект Options для применения опций.
        :type options_obj: Options
        :param settings: Словарь с настройками.
        :type settings: dict
        """
        if settings.get('options'):
            for option in settings.get('options'):
                options_obj.add_argument(option)


    def _apply_window_mode(self, options_obj: Options, settings: dict, window_mode: Optional[str]) -> None:
        """
        Устанавливает режим окна браузера.

        :param options_obj: Объект Options для установки режима окна.
        :type options_obj: Options
        :param settings: Словарь с настройками.
        :type settings: dict
        :param window_mode: Режим окна браузера.
        :type window_mode: Optional[str]
        """
        window_mode = window_mode or settings.get('window_mode')
        if window_mode:
            if window_mode == 'kiosk':
                options_obj.add_argument("--kiosk")
            elif window_mode == 'windowless':
                options_obj.add_argument("--headless")
            elif window_mode == 'full_window':
                options_obj.add_argument("--start-maximized")

    def _apply_additional_options(self, options_obj: Options, options: Optional[List[str]]) -> None:
       """
       Добавляет дополнительные опции к объекту Options.

       :param options_obj: Объект Options для добавления опций.
       :type options_obj: Options
       :param options: Список дополнительных опций.
       :type options: Optional[List[str]]
       """
       if options:
            for option in options:
                options_obj.add_argument(option)

    def _set_user_agent(self, options_obj: Options, user_agent: Optional[str]) -> None:
        """
        Устанавливает User-Agent для браузера.

        :param options_obj: Объект Options для установки User-Agent.
        :type options_obj: Options
        :param user_agent: User-Agent для браузера.
        :type user_agent: Optional[str]
        """
        user_agent = user_agent or UserAgent().random
        options_obj.add_argument(f'--user-agent={user_agent}')

    def _set_proxy_if_enabled(self, options_obj: Options, settings: dict) -> None:
        """
        Устанавливает прокси, если он включен в настройках.

        :param options_obj: Объект Options для установки прокси.
        :type options_obj: Options
        :param settings: Словарь с настройками.
        :type settings: dict
        """
        if settings.get('proxy_enabled'):
            self._set_proxy(options_obj)

    def _get_profile_directory(self, settings: dict, profile_name: Optional[str]) -> str:
        """
        Формирует путь к директории профиля.

        :param settings: Словарь с настройками.
        :type settings: dict
        :param profile_name: Имя профиля пользователя.
        :type profile_name: Optional[str]
        :return: Путь к директории профиля.
        :rtype: str
        """
        profile_directory = (
            settings.get('profile_directory', {}).get('os')
            if settings.get('profile_directory', {}).get('default') == 'os'
            else str(Path(gs.path.src, settings.get('profile_directory', {}).get('internal')))
        )

        if profile_name:
            profile_directory = str(Path(profile_directory).parent / profile_name)
        if '%LOCALAPPDATA%' in profile_directory:
            profile_directory = Path(
                profile_directory.replace('%LOCALAPPDATA%', os.environ.get('LOCALAPPDATA'))
            )
        return profile_directory

    def _set_proxy(self, options: Options) -> None:
        """
        Настраивает прокси из словаря, возвращаемого get_proxies_dict.

        :param options: Опции Chrome, в которые добавляются настройки прокси.
        :type options: Options
        """
        proxies_dict = get_proxies_dict() # Получаем словарь прокси
        all_proxies = proxies_dict.get('socks4', []) + proxies_dict.get('socks5', []) # Получаем все прокси

        working_proxy = None
        for proxy in random.sample(all_proxies, len(all_proxies)): # Перебираем все прокси
            if check_proxy(proxy): # Проверка прокси
                working_proxy = proxy
                break
        if working_proxy: # Устанавливаем прокси
            proxy = working_proxy
            protocol = proxy.get('protocol')
            if protocol == 'http':
                options.add_argument(f'--proxy-server=http://{proxy["host"]}:{proxy["port"]}')
                logger.info(f"Настройка HTTP Proxy: http://{proxy['host']}:{proxy['port']}")

            elif protocol == 'socks4':
                options.add_argument(f'--proxy-server=socks4://{proxy["host"]}:{proxy["port"]}')
                logger.info(f"Настройка SOCKS4 Proxy: {proxy['host']}:{proxy['port']}")

            elif protocol == 'socks5':
                options.add_argument(f'--proxy-server=socks5://{proxy["host"]}:{proxy["port"]}')
                logger.info(f"Настройка SOCKS5 Proxy: {proxy['host']}:{proxy['port']}")
            else:
                logger.warning(f"Неизвестный тип прокси: {protocol}")
        else:
            logger.warning('Нет доступных прокси в предоставленном файле.')


    def _payload(self) -> None:
        """
        Загружает исполнителей для локаторов и JavaScript сценариев.
        """
        j = JavaScript(self)
        self.get_page_lang = j.get_page_lang
        self.ready_state = j.ready_state
        self.get_referrer = j.ready_state
        self.unhide_DOM_element = j.unhide_DOM_element
        self.window_focus = j.window_focus

        execute_locator = ExecuteLocator(self)
        self.execute_locator = execute_locator.execute_locator
        self.get_webelement_as_screenshot = execute_locator.get_webelement_as_screenshot
        self.get_webelement_by_locator = execute_locator.get_webelement_by_locator
        self.get_attribute_by_locator = execute_locator.get_attribute_by_locator
        self.send_message = execute_locator.send_key_to_webelement # Убираем дублирование

if __name__ == "__main__":
    driver = Chrome(window_mode='full_window')
    driver.get(r"https://google.com")