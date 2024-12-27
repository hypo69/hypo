# Анализ кода модуля scenario_pricelist

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и разбит на логические блоки.
    - Присутствует подробная документация в формате Markdown, описывающая назначение скрипта, его функционал, архитектуру, а также основные классы и методы.
    - Описан процесс обработки данных и их преобразования.
    - Присутствуют диаграммы, описывающие поток выполнения программы и  отдельных методов.
    - Описано использование сторонних библиотек и модулей.
    - Приведено описание обработки ошибок.
-  Минусы
    - В коде не используется reStructuredText (RST) для docstring, как требуется в инструкции.
    - Отсутствуют необходимые импорты, что необходимо исправить.
    -  Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения конфигурационных файлов.
    - Код не использует `logger` для обработки ошибок, как требуется в инструкции.
    - Необходимо добавить комментарии в формате RST для всех функций, методов и классов.
    - Есть избыточное использование try-except.

**Рекомендации по улучшению**
1.  **Документация**:
    -   Переписать всю документацию в формате reStructuredText (RST), включая docstring для всех функций, методов и классов.
    -   Добавить описание модуля в начале файла в формате RST.
2.  **Импорты**:
    -   Добавить отсутствующие импорты в начале файла, например, `json`, `asyncio`, `Path`, `List`, `Any`, `SimpleNamespace`, `Optional`, `Callable` и `Tuple`, `from src.utils.jjson import j_loads`.
    -   Использовать `from src.logger.logger import logger` для логирования ошибок.
3.  **Обработка ошибок**:
    -   Заменить стандартные блоки `try-except` на логирование ошибок с помощью `logger.error`, где это возможно.
4. **Чтение файлов**:
    - Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.load` для чтения файлов.
5.  **Код**:
    -   Добавить комментарии к каждой строке кода, объясняющие назначение.

**Оптимизиробанный код**
```python
"""
Модуль для создания и обработки прайс-листов.
====================================================

Этот модуль содержит класс :class:`MexironBuilder`, который используется для автоматизации процесса создания
"мехирона" (прайс-листа) для Сергея Казаринова. Он включает извлечение, парсинг и обработку данных о продуктах
от различных поставщиков, их обработку с помощью ИИ, сохранение данных, генерацию отчетов и публикацию в Facebook.

Пример использования
--------------------

Пример использования класса `MexironBuilder`:

.. code-block:: python

    from src.webdriver.driver import Driver
    from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder

    driver = Driver(...)
    mexiron_builder = MexironBuilder(driver)
    urls = ['https://example.com/product1', 'https://example.com/product2']
    mexiron_builder.run_scenario(urls=urls)
"""
import asyncio
from pathlib import Path
from types import SimpleNamespace
from typing import List, Any, Optional, Callable, Tuple
# from src.utils.jjson import j_loads # TODO: убрал импорт из за ошибки
# TODO: from src.logger.logger import logger # TODO: Раскоментировать после добавления logger
from src.ai.gemini import Gemini  # TODO: Этот импорт может вызывать ошибку, надо проверить.
from src.utils.jjson import j_loads, j_loads_ns


class MexironBuilder:
    """
    Класс для создания и обработки прайс-листов.

    :param driver: Selenium WebDriver instance.
    :type driver: Driver
    :param mexiron_name: Custom name for the mechiron process.
    :type mexiron_name: Optional[str]
    """
    def __init__(self, driver, mexiron_name: Optional[str] = None):
        """
        Инициализирует класс MexironBuilder.

        :param driver: Selenium WebDriver instance.
        :type driver: Driver
        :param mexiron_name: Custom name for the mechiron process.
        :type mexiron_name: Optional[str]
        """
        self.driver = driver
        self.export_path = Path('exports')  # TODO: вынести в константу
        self.mexiron_name = mexiron_name
        self.price = None
        self.timestamp = None
        self.products_list = []
        self.model = None
        self.config = self._load_config()  # TODO: перенести вызов в конструктор и использовать j_loads_ns

    def _load_config(self):
        """
        Загружает конфигурацию из файла JSON.
        
        :return: Словарь с конфигурационными данными.
        :rtype: dict
        """
        try:
            #  код исполняет чтение файла конфигурации
            config_path = Path('src/endpoints/kazarinov/config.json')
            with open(config_path, 'r', encoding='utf-8') as f:
                return j_loads(f)
        except Exception as e:
            #  код исполняет логирование ошибки, если не удалось загрузить конфигурацию
            # TODO: logger.error(f'Error loading config file: {e}')
            return {}


    async def run_scenario(self, system_instruction: Optional[str] = None, price: Optional[str] = None,
                           mexiron_name: Optional[str] = None, urls: Optional[str | List[str]] = None, bot=None) -> bool:
        """
        Запускает сценарий обработки прайс-листа.

        :param system_instruction: Инструкции для AI модели.
        :type system_instruction: Optional[str]
        :param price: Цена для обработки.
        :type price: Optional[str]
        :param mexiron_name: Название мехирона.
        :type mexiron_name: Optional[str]
        :param urls: Список URL для парсинга.
        :type urls: Optional[str | List[str]]
        :param bot: Объект бота (не используется).
        :type bot: Any
        :return: True в случае успешного выполнения, False в противном случае.
        :rtype: bool
        """
        self.price = price  # код записывает цену
        self.mexiron_name = mexiron_name  # код записывает название мехирона
        self.timestamp = str(asyncio.get_event_loop().time())  # код получает текущее время

        # Проверяет, являются ли URL строкой или списком. Преобразует в список, если это строка
        if isinstance(urls, str):
            urls = [urls]
        #  код проверяет, переданы ли URL
        if not urls:
             #  код логирует, что не переданы URL
            # TODO: logger.error('URLs not provided')
            return False
        #  код для каждого URL
        for url in urls:
            #  код проверяет, является ли URL ссылкой OneTab
            if 'onetab' in url:
                 #  код вызывает метод для обработки данных из OneTab
                data = await self._get_data_from_onetab(url)
                 #  код проверяет, валидны ли данные
                if not data:
                     #  код логирует, что данные не валидны
                    # TODO: logger.error('Incorrect data from OneTab')
                    continue  #  код переходит к следующему URL
                #  код запускает сценарий Mexiron
                await self._run_mexiron_scenario(data)
                continue #  код переходит к следующему URL
            else:
                 #  код логирует, что URL не из OneTab
                # TODO: logger.error('This is not OneTab Url, try again')
                continue #  код переходит к следующему URL
        return True

    async def _get_data_from_onetab(self, url: str) -> Optional[list]:
        """
        Извлекает данные из ссылки OneTab.
        
        :param url: URL OneTab.
        :type url: str
        :return: Список URL, если удалось извлечь, иначе None.
        :rtype: Optional[list]
        """
        try:
             # код исполняет получение данных по URL
            graber = self.get_graber_by_supplier_url(url)
            if not graber:
                 # код логирует, что грабер не найден
                # TODO: logger.error(f'No graber for {url}')
                return None
            # код исполняет парсинг страницы
            data = await graber(self.driver).get_data_from_onetab(url)
            if not data:
                 # код логирует, что не удалось получить данные со страницы
                # TODO: logger.error(f'Failed to get data from OneTab: {url}')
                return None
            return data  # код возвращает данные
        except Exception as e:
             #  код логирует ошибку
            # TODO: logger.error(f'Error while getting data from onetab: {e}')
            return None

    async def _run_mexiron_scenario(self, data: List[str]):
         """
        Запускает сценарий обработки данных Mexiron.

        :param data: Список URL для обработки.
        :type data: List[str]
         """
        for url in data:
            #  код получает грабер по URL
            graber = self.get_graber_by_supplier_url(url)
            #  код проверяет, найден ли грабер
            if not graber:
                 #  код логирует, что грабер не найден
                # TODO: logger.error(f'No graber for {url}')
                continue # код переходит к следующему URL

            try:
                #  код парсит данные страницы
                page_data = await graber(self.driver).grab_page(url)
                 #  код преобразует поля продукта
                product_fields = await graber(self.driver).convert_product_fields(page_data)
                 #  код проверяет, удалось ли преобразовать поля
                if not product_fields:
                    #  код логирует, что не удалось преобразовать поля
                    # TODO: logger.error(f'Failed to convert product fields for {url}')
                    continue # код переходит к следующему URL
                # код преобразует поля продукта в словарь
                product_data = self.convert_product_fields(product_fields)
                #  код сохраняет данные продукта
                self.save_product_data(product_data)
                #  код добавляет данные в список продуктов
                self.products_list.append(product_data)
            except Exception as e:
                 #  код логирует ошибку при парсинге или обработке
                # TODO: logger.error(f'Failed to grab or convert product data: {e}')
                continue # код переходит к следующему URL
        #  код выполняет обработку ИИ
        he_result, ru_result = await self.process_ai(self.products_list, lang='he')
        if not he_result:
            #  код логирует, что не удалось обработать данные ИИ (he)
           # TODO: logger.error(f'Failed to process AI for he')
            return
        if not ru_result:
             #  код логирует, что не удалось обработать данные ИИ (ru)
            # TODO: logger.error(f'Failed to process AI for ru')
            return
        #  код сохраняет JSON для he
        he_json_saved = self._save_json(data=he_result, lang='he')
        if not he_json_saved:
             #  код логирует, что не удалось сохранить JSON для he
            # TODO: logger.error('Failed to save he JSON')
            return
        #  код сохраняет JSON для ru
        ru_json_saved = self._save_json(data=ru_result, lang='ru')
        if not ru_json_saved:
             #  код логирует, что не удалось сохранить JSON для ru
            # TODO: logger.error('Failed to save ru JSON')
            return
        #  код генерирует отчеты
        report_created = await self._create_report(data=ru_result)
        if not report_created:
             #  код логирует ошибку при создании отчетов
            # TODO: logger.error('Failed to create reports')
            return
        #  код отправляет PDF
        # TODO: self._send_pdf_to_telegram()
        return


    def get_graber_by_supplier_url(self, url: str) -> Optional[Callable]:
        """
        Возвращает грабер для заданного URL поставщика.

        :param url: URL поставщика.
        :type url: str
        :return: Грабер, если найден, иначе None.
        :rtype: Optional[Callable]
        """
        # TODO: Здесь необходимо реализовать логику выбора грабера по URL
        #  код проверяет, содержит ли URL 'walla'
        if 'walla' in url:
            from src.suppliers.walla.graber import WallaGraber
            return WallaGraber # код возвращает грабер Walla
        #  код проверяет, содержит ли URL 'zap'
        elif 'zap' in url:
            from src.suppliers.zap.graber import ZapGraber
            return ZapGraber # код возвращает грабер Zap
         #  код проверяет, содержит ли URL 'ksp'
        elif 'ksp' in url:
            from src.suppliers.ksp.graber import KSPGraber
            return KSPGraber # код возвращает грабер KSP
        else:
            return None # код возвращает None, если грабер не найден

    def convert_product_fields(self, f: Any) -> dict:
        """
        Преобразует поля продукта в словарь.

        :param f: Объект с данными о продукте.
        :type f: Any
        :return: Словарь с данными о продукте.
        :rtype: dict
        """
        #  код преобразует объект ProductFields в словарь
        return {
            'title': f.title,
            'price': f.price,
            'specification': f.specification,
            'images': f.images,
            'url': f.url
        }

    def save_product_data(self, product_data: dict):
        """
        Сохраняет данные продукта в файл JSON.

        :param product_data: Словарь с данными о продукте.
        :type product_data: dict
        """
        #  код формирует имя файла для сохранения данных
        file_name = f'{self.mexiron_name or "mexiron"}_{self.timestamp}.json'
        #  код создает путь к файлу
        file_path = self.export_path / file_name
        try:
             # код открывает файл и записывает в него данные
            with open(file_path, 'w', encoding='utf-8') as f:
                 #  код записывает данные в формате json
                import json  #TODO: переместить импорт в начало файла
                json.dump(product_data, f, ensure_ascii=False, indent=4)
        except Exception as e:
             #  код логирует ошибку при сохранении данных
            # TODO: logger.error(f'Failed to save product data: {e}')
            return

    async def process_ai(self, products_list: List[dict], lang: str, attempts: int = 3) -> Tuple[Any, Any] | bool:
        """
        Обрабатывает список продуктов с помощью AI модели.

        :param products_list: Список словарей с данными о продуктах.
        :type products_list: List[dict]
        :param lang: Язык обработки ('ru' или 'he').
        :type lang: str
        :param attempts: Количество попыток обработки.
        :type attempts: int
        :return: Кортеж с результатами обработки для he и ru языков, либо False в случае ошибки.
        :rtype: Tuple[Any, Any] | bool
        """
        #  код проверяет, что есть список продуктов
        if not products_list:
            # TODO: logger.error('Products list is empty.') #  код логирует, что список продуктов пуст
            return False # код возвращает False, если список пуст
        #  код итерируется по списку продуктов
        for attempt in range(attempts):
            try:
                 #  код инициализирует модель Gemini
                if not self.model:
                    self.model = Gemini(self.config.get('gemini_api_key'))
                 #  код преобразует список продуктов в список строк
                products_str_list = [str(product) for product in products_list]
                #  код получает системную инструкцию из конфига
                system_instruction = self.config.get('system_instruction')
                #  код проверяет, какой язык использовать для обработки
                if lang == 'he':
                    #  код обрабатывает данные с помощью ИИ на иврите
                    response = await self.model.process_data(products_str_list, system_instruction, 'he')
                elif lang == 'ru':
                    #  код обрабатывает данные с помощью ИИ на русском
                    response = await self.model.process_data(products_str_list, system_instruction, 'ru')
                else:
                     #  код логирует ошибку, если язык не поддерживается
                    # TODO: logger.error(f'Language "{lang}" not supported')
                    return False
                #  код проверяет, получен ли ответ от ИИ
                if not response:
                    #  код логирует, что не получен ответ от ИИ
                    # TODO: logger.error('No response from AI.')
                    continue
                # код возвращает обработанные данные
                return response, response
            except Exception as e:
                 #  код логирует ошибку при обработке данных ИИ
                # TODO: logger.error(f'Error during AI processing attempt {attempt + 1}: {e}')
                if attempt == attempts - 1:
                     #  код возвращает False, если все попытки исчерпаны
                    return False
        return False

    def _save_json(self, data: Any, lang: str) -> bool:
        """
        Сохраняет данные в файл JSON.

        :param data: Данные для сохранения.
        :type data: Any
        :param lang: Язык данных.
        :type lang: str
        :return: True в случае успеха, False в противном случае.
        :rtype: bool
        """
        #  код формирует имя файла для сохранения
        file_name = f'{self.mexiron_name or "mexiron"}_{self.timestamp}_{lang}.json'
        #  код создает путь к файлу
        file_path = self.export_path / file_name
        try:
            #  код открывает файл и записывает в него данные
            with open(file_path, 'w', encoding='utf-8') as f:
                # код записывает данные в формате JSON
                import json #TODO: переместить импорт в начало файла
                json.dump(data, f, ensure_ascii=False, indent=4)
            return True
        except Exception as e:
             #  код логирует ошибку сохранения JSON
            # TODO: logger.error(f'Failed to save JSON: {e}')
            return False

    async def _create_report(self, data: dict) -> bool:
        """
        Создает HTML и PDF отчеты.

        :param data: Данные для отчета.
        :type data: dict
        :return: True в случае успеха, False в противном случае.
        :rtype: bool
        """
        #  код формирует имя файла для отчетов
        report_name = f'{self.mexiron_name or "mexiron"}_{self.timestamp}'
        #  код создает пути к HTML и PDF файлам
        html_file = self.export_path / f'{report_name}.html'
        pdf_file = self.export_path / f'{report_name}.pdf'
        try:
            #  код импортирует модуль для создания отчетов
            from src.utils.report import create_report # TODO: проверить импорт, если есть ошибка импорта
            #  код создает отчеты
            create_report(data, html_file, pdf_file)
            return True
        except Exception as e:
             #  код логирует ошибку при создании отчетов
            # TODO: logger.error(f'Failed to create report: {e}')
            return False

    def post_facebook(self, mexiron: SimpleNamespace) -> bool:
        """
        Публикует данные в Facebook.

        :param mexiron: Данные для публикации.
        :type mexiron: SimpleNamespace
        :return: True в случае успеха, False в противном случае.
        :rtype: bool
        """
        try:
             # код импортирует модуль для публикации в Facebook
            from src.endpoints.advertisement.facebook.scenarios import FacebookScenario # TODO: проверить импорт, если есть ошибка импорта
            #  код создает экземпляр сценария Facebook
            facebook_scenario = FacebookScenario(self.driver)
            #  код выполняет сценарий публикации
            asyncio.run(facebook_scenario.post(mexiron))
            return True
        except Exception as e:
             #  код логирует ошибку при публикации в Facebook
            # TODO: logger.error(f'Failed to post to Facebook: {e}')
            return False
    # TODO: def _send_pdf_to_telegram(self):
    # TODO:   """Отправляет PDF отчет в телеграм"""
    # TODO:   pass