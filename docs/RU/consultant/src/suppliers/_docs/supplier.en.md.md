# Анализ кода модуля `Supplier`

**Качество кода**
8
-  Плюсы
    -  Хорошая структура класса, разделение на методы, что облегчает чтение и поддержку кода.
    -  Присутствует подробное описание класса на английском языке, что помогает понять его назначение и функциональность.
    -  Использование `supplier_prefix` для загрузки настроек и локаторов.
    -  Предусмотрены методы для логина и запуска сценариев.
-  Минусы
    -  Отсутствует документация в формате reStructuredText (RST) для класса и методов.
    -  Не используются `j_loads` или `j_loads_ns` для загрузки JSON-файлов.
    -  Не хватает обработки ошибок с использованием `logger.error`.
    -  Не все импорты могут быть явными.
    -  Присутствует `...` (многоточие) как заглушка в коде.
    -  Не везде есть использование `logger` для отладки и логирования.

**Рекомендации по улучшению**
1. **Документация**:
   - Добавить документацию в формате RST для класса `Supplier` и его методов.
   - Описать назначение каждого параметра в методах.
   - Указать возвращаемые значения и возможные исключения.
2. **Загрузка JSON**:
   - Заменить стандартный `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
3. **Обработка ошибок**:
   - Заменить общие блоки `try-except` на логирование ошибок с использованием `logger.error`.
   - Добавить обработку возможных исключений при загрузке данных и выполнении сценариев.
4. **Импорты**:
   - Убедиться, что все необходимые импорты присутствуют и корректны.
5. **Логирование**:
    - Использовать `logger` для отладки и логирования важных событий и ошибок.
6. **Заглушки**:
    - Убрать `...` заглушки или заменить их на конкретную логику.
7. **Рефакторинг**:
    - Разделить метод `_payload` на более мелкие функции для улучшения читаемости и поддерживаемости.
    - Пересмотреть структуру методов `login`, `run_scenario_files` и `run_scenarios` для большей гибкости и расширяемости.
    - Использовать более конкретные типы для аргументов и возвращаемых значений.
8. **Комментарии**:
    - Добавить пояснения к каждой строке кода.

**Оптимизированный код**
```python
"""
Модуль для управления поставщиками данных.
=========================================================================================

Этот модуль определяет базовый класс :class:`Supplier`, который предоставляет
основу для управления поставщиками данных, такими как Amazon, AliExpress,
Walmart и другие. Класс обрабатывает инициализацию настроек поставщика,
управляет сценариями сбора данных и предоставляет методы для входа в систему
и выполнения сценариев.
"""
import os
from typing import List, Dict, Any
from src.utils.jjson import j_loads
from src.logger.logger import logger
from src.webdriver.driver import Driver

class Supplier:
    """
    Базовый класс для управления поставщиками данных.

    :ivar supplier_id: Уникальный идентификатор поставщика.
    :vartype supplier_id: str
    :ivar supplier_prefix: Префикс поставщика, например, 'aliexpress' или 'amazon'.
    :vartype supplier_prefix: str
    :ivar supplier_settings: Настройки поставщика, загруженные из файла конфигурации.
    :vartype supplier_settings: dict
    :ivar locale: Код локализации, например, 'en' для английского или 'ru' для русского.
    :vartype locale: str
    :ivar price_rule: Правило расчета цен, например, добавление НДС или применение скидок.
    :vartype price_rule: dict
    :ivar related_modules: Модуль, содержащий специфические функции поставщика.
    :vartype related_modules: module
    :ivar scenario_files: Список файлов сценариев для выполнения.
    :vartype scenario_files: list
    :ivar current_scenario: Текущий выполняемый сценарий.
    :vartype current_scenario: dict
    :ivar login_data: Учетные данные для входа на сайт поставщика (если требуется).
    :vartype login_data: dict
    :ivar locators: Локаторы веб-элементов на сайте поставщика.
    :vartype locators: dict
    :ivar driver: Веб-драйвер для взаимодействия с сайтом поставщика.
    :vartype driver: Driver
    :ivar parsing_method: Метод парсинга данных, например, 'webdriver', 'api', 'xls', 'csv'.
    :vartype parsing_method: str
    """

    supplier_id: str = None
    supplier_prefix: str = None
    supplier_settings: dict = None
    locale: str = None
    price_rule: dict = None
    related_modules: Any = None
    scenario_files: List[str] = None
    current_scenario: dict = None
    login_data: dict = None
    locators: dict = None
    driver: Driver = None
    parsing_method: str = None

    def __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | Driver | bool = 'default', *attrs, **kwargs):
        """
        Инициализирует объект поставщика.

        :param supplier_prefix: Префикс поставщика, например, 'aliexpress'.
        :type supplier_prefix: str
        :param locale: Код локализации, например, 'en' или 'ru'.
        :type locale: str, optional
        :param webdriver: Веб-драйвер или его настройка, например, 'chrome', 'firefox' или экземпляр Driver.
        :type webdriver: str | Driver | bool, optional
        :raises ValueError: Если префикс поставщика не указан.
        """
        if not supplier_prefix:
            logger.error("Необходимо указать префикс поставщика.")
            raise ValueError("Supplier prefix is required")
        #  Устанавливаем префикс поставщика.
        self.supplier_prefix = supplier_prefix
        #  Устанавливаем локаль.
        self.locale = locale
        #  Выполняем загрузку данных и инициализируем веб-драйвер.
        self._payload(webdriver, *attrs, **kwargs)

    def _payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool:
        """
        Загружает конфигурации поставщика, локаторы и инициализирует веб-драйвер.

        :param webdriver: Веб-драйвер или его настройка.
        :type webdriver: str | Driver | bool
        :raises FileNotFoundError: Если файл настроек или локаторов не найден.
        :raises Exception: Если произошла ошибка при загрузке файла.
        :return: True, если загрузка прошла успешно, False в противном случае.
        :rtype: bool
        """
        #  Формируем пути к файлам настроек и локаторов.
        settings_path = os.path.join('settings', f'{self.supplier_prefix}.json')
        locators_path = os.path.join('locators', f'{self.supplier_prefix}.json')
        # Загружаем настройки поставщика из JSON файла
        try:
            # Загружаем настройки поставщика из JSON файла
            self.supplier_settings = j_loads(settings_path)
            # Загружаем локаторы элементов поставщика из JSON файла
            self.locators = j_loads(locators_path)
        except FileNotFoundError as e:
            logger.error(f'Файл настроек или локаторов не найден: {e}')
            return False
        except Exception as e:
            logger.error(f'Ошибка при загрузке файла: {e}')
            return False

        # Устанавливаем ID поставщика.
        self.supplier_id = self.supplier_settings.get('supplier_id')
        #  Устанавливаем метод парсинга.
        self.parsing_method = self.supplier_settings.get('parsing_method', 'webdriver')
        #  Инициализируем веб-драйвер.
        try:
             #  Проверяем тип веб-драйвера и инициализируем.
            if isinstance(webdriver, Driver):
                 self.driver = webdriver
            elif webdriver == 'default' or not webdriver:
                 self.driver = Driver()
            elif isinstance(webdriver, str):
                 self.driver = Driver(webdriver)
            else:
                self.driver = None
        except Exception as e:
            logger.error(f'Ошибка инициализации веб-драйвера: {e}')
            return False

        #  Проверяем, есть ли логин данные в настройках.
        if self.supplier_settings.get('login_data'):
             #  Устанавливаем данные для логина
            self.login_data = self.supplier_settings.get('login_data')

        return True


    def login(self) -> bool:
        """
        Выполняет вход на сайт поставщика, если требуется.

        :return: True, если вход выполнен успешно или не требуется, False в противном случае.
        :rtype: bool
        """
        #  Проверяем, есть ли данные для входа.
        if not self.login_data:
            logger.debug('Данные для входа не требуются.')
            return True
        # Код исполняет попытку входа на сайт используя драйвер
        try:
            #  Выполняем вход в систему.
            # TODO: Добавить реализацию логики входа.
            logger.debug('Выполняется вход в систему.')
            return True
        except Exception as e:
            #  Логируем ошибку, если не удалось войти.
            logger.error(f'Ошибка при входе в систему: {e}')
            return False

    def run_scenario_files(self, scenario_files: str | List[str] = None) -> bool:
        """
        Выполняет сценарии из одного или нескольких файлов.

        :param scenario_files: Список файлов со сценариями или путь к одному файлу.
        :type scenario_files: str | List[str], optional
        :return: True, если все сценарии выполнены успешно, False в противном случае.
        :rtype: bool
        """
        #  Если файлы сценариев не указаны, берем из настроек.
        if not scenario_files:
            scenario_files = self.supplier_settings.get('scenario_files')
        #  Проверяем, что файлы сценариев есть
        if not scenario_files:
            logger.error('Файлы сценариев не найдены.')
            return False
        #  Приводим к списку если это строка
        if isinstance(scenario_files, str):
            scenario_files = [scenario_files]
        #  Выполняем сценарии.
        try:
           #  Запускаем каждый сценарий из файла.
           for file in scenario_files:
                #  Загружаем сценарии из файла.
               scenarios = j_loads(file)
               #  Выполняем загруженные сценарии.
               if not self.run_scenarios(scenarios):
                   return False
           return True
        except Exception as e:
            #  Логируем ошибку, если выполнение сценариев не удалось.
            logger.error(f'Ошибка при выполнении файлов сценариев: {e}')
            return False


    def run_scenarios(self, scenarios: dict | list[dict]) -> bool:
        """
        Выполняет один или несколько сценариев.

        :param scenarios: Список или словарь сценариев для выполнения.
        :type scenarios: dict | list[dict]
        :return: True, если все сценарии выполнены успешно, False в противном случае.
        :rtype: bool
        """
        #  Проверяем что есть сценарии.
        if not scenarios:
            logger.error('Сценарии для выполнения не найдены.')
            return False
        #  Приводим к списку если это словарь.
        if isinstance(scenarios, dict):
            scenarios = [scenarios]
        #  Запускаем сценарии по очереди.
        for scenario in scenarios:
            #  Устанавливаем текущий сценарий.
            self.current_scenario = scenario
            #  Логируем, какой сценарий исполняется.
            logger.debug(f'Выполняется сценарий: {scenario}')
            try:
                # TODO:  Выполняем сценарий (добавить реализацию).
                ...
                #  Если выполнение сценария не удалось
            except Exception as e:
                #  Логируем ошибку
                logger.error(f'Ошибка при выполнении сценария: {e}')
                return False
        #  Если все сценарии были выполнены, возвращаем True
        return True
```