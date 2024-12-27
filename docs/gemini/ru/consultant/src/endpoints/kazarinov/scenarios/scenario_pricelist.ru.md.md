# Анализ кода модуля `scenario_pricelist`

**Качество кода: 7**
-   **Плюсы**
    -   Документация представлена в формате Markdown, что обеспечивает хорошую читаемость.
    -   Подробное описание основных возможностей, блок-схемы и легенды облегчают понимание работы скрипта.
    -   Структурированное описание класса `MexironBuilder` с атрибутами и методами.
    -   Описание процесса выполнения сценария с блок-схемой и легендой для наглядности.
    -   Примеры использования и описание зависимостей предоставляют контекст для разработчиков.
-   **Минусы**
    -   Отсутствует документация в формате reStructuredText (RST) для Python кода, что требуется по инструкции.
    -   Нет явного указания на использование `j_loads` или `j_loads_ns` для загрузки конфигурации из JSON.
    -   Отсутствуют импорты модулей, используемых в коде.
    -   Методы класса не имеют docstring в формате RST.
    -   Присутствует избыточное использование стандартных `try-except` блоков.
    -   Нет примеров кода с комментариями в формате RST.

**Рекомендации по улучшению**
1.  Переписать документацию в формате RST, особенно для кода Python.
2.  Добавить импорты необходимых модулей, включая `src.utils.jjson`, `src.logger.logger`.
3.  Использовать `j_loads` или `j_loads_ns` для загрузки конфигурационных файлов.
4.  Добавить docstring в формате RST для всех методов класса `MexironBuilder`.
5.  Улучшить обработку ошибок, заменив избыточные `try-except` блоки на использование `logger.error`.
6.  Предоставить примеры кода с комментариями в формате RST, как указано в инструкции.
7.  Переписать комментарии к коду в формате RST.
8.  Уточнить использование асинхронных операций, если это необходимо.
9.  Убедиться, что переменные и методы названы в соответствии с ранее обработанными файлами.

**Оптимизированный код**
```python
"""
Модуль для создания мехирона для Сергея Казаринова
====================================================

Этот модуль содержит класс :class:`MexironBuilder`, который используется для автоматизации процесса создания
"мехирона". Он включает в себя функциональность для извлечения, обработки и публикации данных о продуктах.

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
from typing import Any, List, Optional, Tuple, Dict
#  Добавлены импорты
from src.webdriver.driver import Driver
from src.utils.jjson import j_loads, j_loads_ns
from src.logger.logger import logger
from src.ai.gemini import Gemini
# from src.suppliers.*.graber import Graber # TODO: import specific grabber
# from src.endpoints.advertisement.facebook.scenarios import FacebookScenario # TODO: import specific scenario
# from src.suppliers.ozon.graber import OzonGraber #TODO: импортировать все необходимые граберы
# from src.suppliers.yandex.graber import YandexGraber
from src.endpoints.kazarinov.scenarios.product_fields import ProductFields


class MexironBuilder:
    """
    Класс для автоматизации процесса создания мехирона.

    :param driver: Экземпляр Selenium WebDriver.
    :param mexiron_name: Пользовательское имя для процесса мехирона.
    :ivar driver: Экземпляр Selenium WebDriver.
    :ivar export_path: Путь для экспорта данных.
    :ivar mexiron_name: Пользовательское имя для процесса мехирона.
    :ivar price: Цена для обработки.
    :ivar timestamp: Метка времени для процесса.
    :ivar products_list: Список обработанных данных о продуктах.
    :ivar model: Модель Google Generative AI.
    :ivar config: Конфигурация, загруженная из JSON.
    """
    def __init__(self, driver: Driver, mexiron_name: Optional[str] = None):
        """
        Инициализирует класс `MexironBuilder` с необходимыми компонентами.

        :param driver: Экземпляр Selenium WebDriver.
        :param mexiron_name: Пользовательское имя для процесса мехирона.
        """
        self.driver = driver
        self.export_path = Path('export') # TODO: проверить что путь есть в конфиге
        self.mexiron_name = mexiron_name or 'mexiron'
        self.price = None
        self.timestamp = None
        self.products_list = []
        self.model = None
        self.config = self._load_config() #  конфиг загружается при инициализации класса

    def _load_config(self) -> dict:
        """
        Загружает конфигурацию из JSON файла.

        :return: Словарь с конфигурационными данными.
        """
        try:
            #  Используется j_loads_ns для загрузки конфигурации
            config_path = Path('src/endpoints/kazarinov/config.json') # TODO: вынести путь в config
            config = j_loads_ns(config_path)
            return config
        except Exception as ex:
            logger.error(f'Ошибка загрузки конфигурации из файла {config_path}', exc_info=ex)
            return {}

    def run_scenario(self, system_instruction: Optional[str] = None, price: Optional[str] = None, mexiron_name: Optional[str] = None, urls: Optional[str | List[str]] = None, bot = None) -> bool:
        """
        Выполняет сценарий: парсит продукты, обрабатывает их через ИИ и сохраняет данные.

        :param system_instruction: Системные инструкции для модели ИИ.
        :param price: Цена для обработки.
        :param mexiron_name: Пользовательское имя мехирона.
        :param urls: URLs страниц продуктов.
        :param bot: Экземпляр бота.
        :return: `True`, если сценарий выполнен успешно, иначе `False`.
        """
        self.mexiron_name = mexiron_name or self.mexiron_name
        self.price = price or self.price
        self.system_instruction = system_instruction or 'Выведи список продуктов' # TODO: вынести в конфиг
        self._init_model()  #  Инициализация модели
        if not urls:
           logger.error('Не предоставлены URLs для парсинга.')
           return False #  если URL-ов нет, возвращается False

        if isinstance(urls, str):
            urls = [urls]

        for url in urls:
            if 'onetab' in url:
                #  логика обработки onetab не реализована
                logger.error('Обработка OneTab не реализована. Попробуйте снова.')
                return False # TODO: доработать логику onetab
            else:
                graber = self.get_graber_by_supplier_url(url)
                if not graber:
                    logger.error(f'Нет грабера для URL: {url}')
                    continue #  если грабер не найден, переходим к следующему URL
                try:
                   #  код выполняет парсинг страницы
                    f = graber.grab_page(url=url)
                except Exception as ex:
                    logger.error(f'Ошибка парсинга страницы {url}', exc_info=ex)
                    continue #  если произошла ошибка парсинга, переходим к следующему URL

                if not f:
                    logger.error(f'Не удалось спарсить страницу {url}')
                    continue #  если данные не получены, переходим к следующему URL

                product_data = self.convert_product_fields(f)
                if not product_data:
                    logger.error(f'Ошибка конвертации полей продукта {url}')
                    continue # если не удалось конвертировать данные, переходим к следующему URL
                if not self.save_product_data(product_data):
                     logger.error(f'Не удалось сохранить данные продукта {url}')
                     continue #  если не удалось сохранить данные, переходим к следующему URL

                self.products_list.append(product_data)


        #  после обработки всех URL-ов запускаем обработку через ИИ
        if self.products_list:
            ai_result_he, ai_result_ru = self.process_ai(self.products_list, attempts=3) #  выполняется обработка через ИИ
            if ai_result_he:
                #  сохраняем JSON для he
                if not self._save_json_data(data=ai_result_he, lang='he'):
                    logger.error('Ошибка сохранения JSON для he')
            else:
               logger.error('Не удалось получить результат от ИИ для he')

            if ai_result_ru:
                #  сохраняем JSON для ru
                if not self._save_json_data(data=ai_result_ru, lang='ru'):
                    logger.error('Ошибка сохранения JSON для ru')
            else:
               logger.error('Не удалось получить результат от ИИ для ru')


            #  генерация отчетов
            if ai_result_ru:
                report_path_he = self.export_path / f'{self.mexiron_name}_he'
                report_path_ru = self.export_path / f'{self.mexiron_name}_ru'
                if not self.create_report(data=ai_result_he, html_file=report_path_he.with_suffix('.html'), pdf_file=report_path_he.with_suffix('.pdf')):
                    logger.error('Ошибка создания отчета для he')

                if not self.create_report(data=ai_result_ru, html_file=report_path_ru.with_suffix('.html'), pdf_file=report_path_ru.with_suffix('.pdf')):
                     logger.error('Ошибка создания отчета для ru')
            else:
                logger.error('Не удалось сгенерировать отчеты, т.к. не получен результат от ИИ для ru')


        # TODO:  добавить отправку PDF через Telegram
        return True


    def _init_model(self):
        """
        Инициализирует модель Google Generative AI.
        """
        if not self.config:
            logger.error('Не удалось загрузить конфигурацию для инициализации модели.')
            return
        try:
           #  создаем экземпляр модели Gemini
            self.model = Gemini(
                api_key=self.config.gemini_api_key,  # TODO: вынести ключи в secrets
                system_instruction=self.system_instruction
            )
        except Exception as ex:
            logger.error('Ошибка инициализации модели Gemini', exc_info=ex)


    def get_graber_by_supplier_url(self, url: str):
        """
        Возвращает соответствующий грабер для данного URL поставщика.

        :param url: URL страницы поставщика.
        :return: Экземпляр грабера, если найден, иначе `None`.
        """
        # TODO: Реализовать логику выбора грабера на основе URL
        #  Пример
        if 'ozon.ru' in url:
            # from src.suppliers.ozon.graber import OzonGraber #  импорт грабера
            return OzonGraber(self.driver)
        elif 'yandex.ru' in url:
             # from src.suppliers.yandex.graber import YandexGraber #  импорт грабера
             return YandexGraber(self.driver)
        else:
           logger.error(f'Не найден грабер для URL: {url}')
           return None


    def convert_product_fields(self, f: ProductFields) -> dict:
        """
        Конвертирует поля продукта в словарь.

        :param f: Объект, содержащий парсированные данные о продукте.
        :return: Форматированный словарь данных о продукте.
        """
        try:
            return f.to_dict()
        except Exception as ex:
            logger.error('Ошибка конвертации полей продукта в словарь', exc_info=ex)
            return {}



    def save_product_data(self, product_data: dict) -> bool:
        """
        Сохраняет данные о продукте в файл.

        :param product_data: Форматированные данные о продукте.
        :return: `True` если данные сохранены, иначе `False`.
        """
        try:
             #  путь формируется на основе имени мехирона и текущего времени
             file_path = self.export_path / f'{self.mexiron_name}_{self.timestamp}.json'
             if not self.export_path.exists():
                 self.export_path.mkdir(parents=True)
             with open(file_path, 'w', encoding='utf-8') as f:
                 #  сохраняем данные в json файл
                 import json #TODO: убрать импорт
                 json.dump(product_data, f, ensure_ascii=False, indent=4) #  используем json.dump
             return True
        except Exception as ex:
            logger.error('Ошибка сохранения данных продукта в файл', exc_info=ex)
            return False

    def _save_json_data(self, data: dict, lang: str) -> bool:
        """
        Сохраняет данные в JSON файл.

        :param data: Данные для сохранения.
        :param lang: Язык данных ('ru' или 'he').
        :return: `True` если данные сохранены, иначе `False`.
        """
        try:
            file_path = self.export_path / f'{self.mexiron_name}_{lang}.json'
            if not self.export_path.exists():
                self.export_path.mkdir(parents=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                 #  сохраняем данные в json файл
                 import json #TODO: убрать импорт
                 json.dump(data, f, ensure_ascii=False, indent=4)
            return True
        except Exception as ex:
            logger.error(f'Ошибка сохранения JSON файла для языка {lang}', exc_info=ex)
            return False


    def process_ai(self, products_list: List[dict], attempts: int = 3) -> Tuple[Optional[dict], Optional[dict]]:
        """
        Обрабатывает список продуктов через модель ИИ.

        :param products_list: Список словарей данных о продуктах.
        :param attempts: Количество попыток повторного запроса в случае неудачи.
        :return: Обработанный ответ в форматах `he` и `ru`.
        """
        products_list_str = [str(item) for item in products_list] #  преобразуем данные в строку
        ru_result = None
        he_result = None
        try:
            if self.model:
                #  обрабатываем данные на русском
                ru_result = self.model.process(products_list_str, lang='ru', attempts=attempts)
                #  обрабатываем данные на иврите
                he_result = self.model.process(products_list_str, lang='he', attempts=attempts)
            else:
                logger.error('Модель ИИ не инициализирована.')
            return  he_result, ru_result
        except Exception as ex:
            logger.error('Ошибка обработки данных через ИИ', exc_info=ex)
            return None, None



    def post_facebook(self, mexiron: SimpleNamespace) -> bool:
        """
        Выполняет сценарий публикации в Facebook.

        :param mexiron: Обработанные данные для публикации.
        :return: `True`, если публикация успешна, иначе `False`.
        """
        # TODO: Реализовать публикацию в Facebook
        # from src.endpoints.advertisement.facebook.scenarios import FacebookScenario
        try:
            #  пример вызова сценария
            fb_scenario = FacebookScenario(driver=self.driver, mexiron=mexiron)
            result = fb_scenario.run_scenario()
            return result
        except Exception as ex:
             logger.error('Ошибка публикации в Facebook', exc_info=ex)
             return False

    def create_report(self, data: dict, html_file: Path, pdf_file: Path) -> bool:
        """
        Генерирует HTML и PDF отчеты из обработанных данных.

        :param data: Обработанные данные.
        :param html_file: Путь для сохранения HTML отчета.
        :param pdf_file: Путь для сохранения PDF отчета.
        :return: `True`, если отчеты успешно созданы, иначе `False`.
        """
        try:
           #  код выполняет генерацию отчетов
            from src.report.report import Report #  импорт класса Report
            report = Report()
            report.generate_report(data=data, html_file=html_file, pdf_file=pdf_file)
            return True
        except Exception as ex:
            logger.error('Ошибка генерации отчетов', exc_info=ex)
            return False


if __name__ == '__main__':
    #  Пример использования
    from src.webdriver.driver import Driver

    driver = Driver() # TODO: добавьте параметры драйвера
    mexiron_builder = MexironBuilder(driver=driver, mexiron_name='test_mexiron')
    urls = [
        'https://www.ozon.ru/product/smartfon-samsung-galaxy-s23-8-256gb-lavandovyy-1014414844/?advert=fCj-q0m914v1bXk31Y6zN16i-P7_u6P2eB7B625lGf7tQn5rI3E0e-3-zWf_18&from=cart&sh=0y0k1g',
        'https://www.ozon.ru/product/smartfon-realme-gt-master-edition-8-256gb-seryy-1014414844/?advert=fCj-q0m914v1bXk31Y6zN16i-P7_u6P2eB7B625lGf7tQn5rI3E0e-3-zWf_18&from=cart&sh=0y0k1g'
        ]

    mexiron_builder.run_scenario(urls=urls)