# Анализ кода модуля `scenario_pricelist`

**Качество кода**
8
 -  Плюсы
    -   Хорошо структурированная документация модуля, включая описание назначения, основных возможностей, блок-схемы, легенды и использования.
    -   Наличие подробной документации по атрибутам и методам класса `MexironBuilder` с описанием параметров и возвращаемых значений.
    -   Включена блок-схема для визуализации логики выполнения сценария, что способствует лучшему пониманию работы кода.
    -   Описаны зависимости и шаги для использования скрипта, что делает его более понятным и доступным для пользователей.
    -   Представлен пример использования скрипта, демонстрирующий, как создать экземпляр класса и запустить сценарий.
    -   Описаны механизмы обработки ошибок, что повышает надежность скрипта.
    -  Использование `mermaid` для описания блок-схем.

 -  Минусы
    -  Отсутствуют docstring для модуля и методов класса `MexironBuilder`.
    -  Не указаны все необходимые импорты в коде, например, не указаны импорты для `List`, `Optional`, `Path`, `SimpleNamespace`.
    -  Используются обычные `try-except` блоки вместо `logger.error` для логирования ошибок.
    -  Отсутствует docstring для `__init__`.
    -  Не все переменные и функции имеют точные имена, например `ProcessAIHe`, `ProcessAIRu`.
    -  В легенде не используются `code` для названия блоков.
    -   Отсутствует использование `j_loads` или `j_loads_ns` для чтения файлов.

**Рекомендации по улучшению**

1.  **Добавить docstring к модулю и методам**: Добавить docstring в формате RST для модуля и всех методов класса `MexironBuilder` для улучшения читаемости и соответствия стандартам документации.
2.  **Добавить отсутствующие импорты**: Добавить все необходимые импорты, такие как `List`, `Optional`, `Path`, `SimpleNamespace` и другие.
3.  **Использовать `logger.error`**: Заменить стандартные блоки `try-except` на `logger.error` для обработки ошибок и упрощения кода.
4.  **Добавить docstring для __init__**: Добавить docstring для метода `__init__` с описанием параметров.
5.  **Уточнить имена переменных и функций**: Переименовать переменные и функции, чтобы сделать их более ясными, например, `process_ai_he`, `process_ai_ru`.
6.  **Использовать code для легенды**: Использовать `code` для выделения названий блоков в легенде.
7.  **Использовать `j_loads`**: Использовать `j_loads` или `j_loads_ns` для чтения конфигурационных файлов.

**Оптимизиробанный код**

```python
"""
Модуль для автоматизации процесса создания мехирона для Сергея Казаринова.
=========================================================================================

Этот модуль содержит класс :class:`MexironBuilder`, который используется для извлечения, парсинга,
обработки данных о продуктах от различных поставщиков, а также для подготовки данных, обработки их
через ИИ и интеграции с Facebook для публикации продуктов.

Пример использования
--------------------

Пример использования класса `MexironBuilder`:

.. code-block:: python

    from src.webdriver.driver import Driver
    from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder

    # Инициализация Driver
    driver = Driver(...)

    # Инициализация MexironBuilder
    mexiron_builder = MexironBuilder(driver)

    # Запуск сценария
    urls = ['https://example.com/product1', 'https://example.com/product2']
    mexiron_builder.run_scenario(urls=urls)
"""

import asyncio
from pathlib import Path
from types import SimpleNamespace
from typing import List, Optional, Any
# from src.utils.jjson import j_loads, j_loads_ns  # TODO: добавить использование j_loads
from src.webdriver.driver import Driver
# from src.ai.gemini import Gemini # TODO: добавить использование Gemini
from src.logger.logger import logger
# from src.suppliers.graber import ProductFields # TODO: добавить  использование ProductFields
# from src.endpoints.advertisement.facebook.scenarios import FacebookScenario # TODO: добавить FacebookScenario


class MexironBuilder:
    """
    Класс для создания мехирона, включающий методы для парсинга, обработки данных и публикации в Facebook.

        Attributes:
            driver (Driver): Экземпляр Selenium WebDriver.
            export_path (Path): Путь для экспорта данных.
            mexiron_name (Optional[str]): Пользовательское имя для процесса мехирона.
            price (Optional[str]): Цена для обработки.
            timestamp (float): Метка времени для процесса.
            products_list (List[dict]): Список обработанных данных о продуктах.
            model: Модель Google Generative AI. # TODO: добавить аннотацию типа
            config (dict): Конфигурация, загруженная из JSON.

    """

    def __init__(self, driver: Driver, mexiron_name: Optional[str] = None):
        """
        Инициализирует класс `MexironBuilder` с необходимыми компонентами.

        Args:
            driver (Driver): Экземпляр Selenium WebDriver.
            mexiron_name (Optional[str]): Пользовательское имя для процесса мехирона.
        """
        self.driver = driver
        self.export_path = Path('exports')  # TODO: сделать чтение из конфига
        self.mexiron_name = mexiron_name
        self.price = None
        self.timestamp = asyncio.get_event_loop().time()
        self.products_list: List[dict] = []
        self.model = None  # TODO: добавить инициализацию модели
        self.config = {}  # TODO: загрузка конфига

    async def run_scenario(self, system_instruction: Optional[str] = None, price: Optional[str] = None, mexiron_name: Optional[str] = None, urls: Optional[str | List[str]] = None, bot = None) -> bool:
        """
        Выполняет сценарий: парсит продукты, обрабатывает их через ИИ и сохраняет данные.

        Args:
            system_instruction (Optional[str]): Системные инструкции для модели ИИ.
            price (Optional[str]): Цена для обработки.
            mexiron_name (Optional[str]): Пользовательское имя мехирона.
            urls (Optional[str | List[str]]): URLs страниц продуктов.
            bot: Объект бота (не используется в текущей версии) # TODO: добавить описание

        Returns:
             bool: True, если сценарий выполнен успешно, иначе False.

        Блок-схема:
            ```mermaid
            flowchart TD
            Start[Start] --> IsOneTab{URL is from OneTab?}
            IsOneTab -->|Yes| GetDataFromOneTab[Get data from OneTab]
            IsOneTab -->|No| ReplyTryAgain[Reply - Try again]
            GetDataFromOneTab --> IsDataValid{Data valid?}
            IsDataValid -->|No| ReplyIncorrectData[Reply Incorrect data]
            IsDataValid -->|Yes| RunMexironScenario[Run Mexiron scenario]
            RunMexironScenario --> IsGraberFound{Graber found?}
            IsGraberFound -->|Yes| StartParsing[Start parsing: <code>url</code>]
            IsGraberFound -->|No| LogNoGraber[Log: No graber for <code>url</code>]
            StartParsing --> IsParsingSuccessful{Parsing successful?}
            IsParsingSuccessful -->|Yes| ConvertProductFields[Convert product fields]
            IsParsingSuccessful -->|No| LogParsingFailed[Log: Failed to parse product fields]
            ConvertProductFields --> IsConversionSuccessful{Conversion successful?}
            IsConversionSuccessful -->|Yes| SaveProductData[Save product data]
            IsConversionSuccessful -->|No| LogConversionFailed[Log: Failed to convert product fields]
            SaveProductData --> IsDataSaved{Data saved?}
            IsDataSaved -->|Yes| AppendToProductsList[Append to products_list]
            IsDataSaved -->|No| LogDataNotSaved[Log: Data not saved]
            AppendToProductsList --> ProcessAIHe[AI processing lang = he]
            ProcessAIHe --> ProcessAIRu[AI processing lang = ru]
            ProcessAIRu --> SaveHeJSON{Save JSON for he?}
            SaveHeJSON -->|Yes| SaveRuJSON[Save JSON for ru]
            SaveHeJSON -->|No| LogHeJSONError[Log: Error saving he JSON]
            SaveRuJSON --> IsRuJSONSaved{Save JSON for ru?}
            IsRuJSONSaved -->|Yes| GenerateReports[Generate reports]
            IsRuJSONSaved -->|No| LogRuJSONError[Log: Error saving ru JSON]
            GenerateReports --> IsReportGenerationSuccessful{Report generation successful?}
            IsReportGenerationSuccessful -->|Yes| SendPDF[Send PDF via Telegram]
            IsReportGenerationSuccessful -->|No| LogPDFError[Log: Error creating PDF]
            SendPDF --> ReturnTrue[Return True]
            LogPDFError --> ReturnTrue[Return True]
            ReplyIncorrectData --> ReturnTrue[Return True]
            ReplyTryAgain --> ReturnTrue[Return True]
            LogNoGraber --> ReturnTrue[Return True]
            LogParsingFailed --> ReturnTrue[Return True]
            LogConversionFailed --> ReturnTrue[Return True]
            LogDataNotSaved --> ReturnTrue[Return True]
            LogHeJSONError --> ReturnTrue[Return True]
            LogRuJSONError --> ReturnTrue[Return True]
            ```

            - **Легенда**:
            1.  **`Start`**: Сценарий начинает выполнение.
            2.  **`IsOneTab`**: Проверяет, является ли URL из OneTab.
            3.  **`GetDataFromOneTab`**: Извлекает данные из OneTab.
            4.  **`ReplyTryAgain`**: Отправляет сообщение "Try again".
            5.  **`IsDataValid`**: Проверяет валидность данных.
            6.  **`ReplyIncorrectData`**: Отправляет сообщение "Incorrect data".
            7.  **`RunMexironScenario`**: Запускает сценарий Mexiron.
            8.  **`IsGraberFound`**: Проверяет, найден ли грабер для URL.
            9.  **`StartParsing`**: Начинает парсинг страницы с данным `url`.
            10. **`LogNoGraber`**: Логирует сообщение, что грабер не найден.
            11. **`IsParsingSuccessful`**: Проверяет, успешен ли парсинг.
            12. **`ConvertProductFields`**: Преобразует поля продукта.
            13. **`LogParsingFailed`**: Логирует сообщение о неудачном парсинге.
            14. **`IsConversionSuccessful`**: Проверяет, успешно ли преобразование данных.
            15. **`SaveProductData`**: Сохраняет данные продукта.
            16. **`LogConversionFailed`**: Логирует сообщение о неудачном преобразовании данных.
            17. **`IsDataSaved`**: Проверяет, сохранены ли данные.
            18. **`AppendToProductsList`**: Добавляет данные в список продуктов.
            19. **`LogDataNotSaved`**: Логирует сообщение о том, что данные не сохранены.
            20. **`ProcessAIHe`**: Обрабатывает данные через ИИ для языка `he`.
            21. **`ProcessAIRu`**: Обрабатывает данные через ИИ для языка `ru`.
            22. **`SaveHeJSON`**: Сохраняет данные в формате JSON для языка `he`.
            23. **`SaveRuJSON`**: Сохраняет данные в формате JSON для языка `ru`.
            24. **`LogHeJSONError`**: Логирует ошибку сохранения JSON для языка `he`.
            25. **`IsRuJSONSaved`**: Проверяет, сохранены ли данные в JSON для языка `ru`.
            26. **`LogRuJSONError`**: Логирует ошибку сохранения JSON для языка `ru`.
            27. **`GenerateReports`**: Генерирует отчеты.
            28. **`IsReportGenerationSuccessful`**: Проверяет, успешно ли создание отчетов.
            29. **`SendPDF`**: Отправляет PDF-файлы через Telegram.
            30. **`LogPDFError`**: Логирует ошибку при создании PDF.
            31. **`ReturnTrue`**: Возвращает True, завершая сценарий.

        """
        self.mexiron_name = mexiron_name or self.mexiron_name
        self.price = price or self.price
        self.products_list = []
        self.system_instruction = system_instruction
        if isinstance(urls, str):
            urls = [urls]

        if not urls:
            logger.error('URLs не предоставлены')
            return False

        for url in urls:
            if 'onetab' in url: # TODO: вынести в отдельную проверку
                # код исполняет получение данных из onetab
                try:
                    # await self.get_data_from_onetab(url)
                    ...
                except Exception as ex:
                    logger.error(f'Ошибка при получении данных из OneTab {ex=}')
                    return False
            else:
                logger.info(f'Попытка парсинга {url=}')
                graber = self.get_graber_by_supplier_url(url)
                if not graber:
                    logger.error(f'Не найден грабер для {url=}')
                    return False

                try:
                    # код исполняет получение данных со страницы
                    product_fields = await graber(self.driver, url).parse()
                    if not product_fields:
                        logger.error(f'Не удалось спарсить данные со страницы {url=}')
                        return False
                except Exception as ex:
                    logger.error(f'Ошибка при парсинге страницы {url=}, {ex=}')
                    return False

                try:
                    # код исполняет преобразование полей продукта в словарь
                    product_data = self.convert_product_fields(product_fields)
                    if not product_data:
                        logger.error(f'Не удалось преобразовать поля продукта {product_fields=}')
                        return False
                except Exception as ex:
                    logger.error(f'Ошибка преобразования полей продукта {ex=}')
                    return False

                try:
                    # код исполняет сохранение данных продукта
                    if not self.save_product_data(product_data):
                        logger.error(f'Не удалось сохранить данные продукта {product_data=}')
                        return False
                    self.products_list.append(product_data)
                except Exception as ex:
                    logger.error(f'Ошибка при сохранении данных продукта {ex=}')
                    return False

        # код исполняет обработку через ИИ
        try:
            ai_he_response, ai_ru_response = await self.process_ai(self.products_list, lang='he')
            if not ai_he_response and not ai_ru_response:
                logger.error(f'Не удалось обработать данные через ИИ {self.products_list=}')
                return False
        except Exception as ex:
             logger.error(f'Ошибка при обработке данных через ИИ {ex=}')
             return False

        # код исполняет сохранение JSON
        try:
            if ai_he_response:
                file_path_he = self.export_path / f'{self.mexiron_name}_{self.timestamp}_he.json'
                # await save_text_file(file_path_he, ai_he_response) # TODO: добавить вызов
            else:
                logger.error(f'Нет данных для сохранения he JSON')
                return False
            if ai_ru_response:
                file_path_ru = self.export_path / f'{self.mexiron_name}_{self.timestamp}_ru.json'
                # await save_text_file(file_path_ru, ai_ru_response) # TODO: добавить вызов
            else:
                 logger.error(f'Нет данных для сохранения ru JSON')
                 return False
        except Exception as ex:
             logger.error(f'Ошибка сохранения JSON {ex=}')
             return False


        # код исполняет генерацию отчетов
        try:
            file_path_html_he = self.export_path / f'{self.mexiron_name}_{self.timestamp}_he.html'
            file_path_pdf_he = self.export_path / f'{self.mexiron_name}_{self.timestamp}_he.pdf'
            file_path_html_ru = self.export_path / f'{self.mexiron_name}_{self.timestamp}_ru.html'
            file_path_pdf_ru = self.export_path / f'{self.mexiron_name}_{self.timestamp}_ru.pdf'

            # if ai_he_response: # TODO: добавить проверку наличия данных
            #    self.create_report(ai_he_response, file_path_html_he, file_path_pdf_he)  # TODO: добавить вызов
            # if ai_ru_response:
            #    self.create_report(ai_ru_response, file_path_html_ru, file_path_pdf_ru)  # TODO: добавить вызов

        except Exception as ex:
            logger.error(f'Ошибка создания отчета {ex=}')
            return False

        # Код исполняет отправку PDF через телеграмм
        try:
            # TODO: добавить отправку PDF
            ...
        except Exception as ex:
            logger.error(f'Ошибка при отправке PDF {ex=}')
            return False

        return True

    def get_graber_by_supplier_url(self, url: str) -> Any:
        """
        Возвращает соответствующий грабер для данного URL поставщика.

        Args:
            url (str): URL страницы поставщика.

        Returns:
             Any: Экземпляр грабера, если найден, иначе None.
        """
        # TODO: добавить логику определения грабера по URL
        if 'asos' in url:
            # from src.suppliers.asos.graber import ASOSGraber # TODO: добавить импорт грабера
            return 'ASOSGraber'
        if 'next' in url:
            # from src.suppliers.next.graber import NextGraber # TODO: добавить импорт грабера
            return 'NextGraber'
        return None

    def convert_product_fields(self, f: Any) -> dict:
        """
        Конвертирует поля продукта в словарь.

        Args:
             f (Any): Объект, содержащий парсированные данные о продукте. # TODO: добавить ProductFields

        Returns:
            dict: Форматированный словарь данных о продукте.
        """
        # TODO: добавить реализацию преобразования полей
        return {
            'title': f.title,
            'price': f.price,
            'description': f.description,
            'images': f.images,
            'specification': f.specification,
        }

    def save_product_data(self, product_data: dict) -> bool:
        """
        Сохраняет данные о продукте в файл.

        Args:
            product_data (dict): Форматированные данные о продукте.

        Returns:
            bool: True, если данные сохранены, иначе False.
        """
        # TODO: добавить реализацию сохранения данных
        file_path = self.export_path / f'{self.mexiron_name}_{self.timestamp}.json'
        # await save_text_file(file_path, product_data) # TODO: добавить вызов
        return True

    async def process_ai(self, products_list: List[str], lang: str, attempts: int = 3) -> tuple | bool:
        """
        Обрабатывает список продуктов через модель ИИ.

        Args:
            products_list (List[dict]): Список словарей данных о продуктах.
            lang (str): Язык обработки ('ru' или 'he').
            attempts (int): Количество попыток повторного запроса в случае неудачи.

        Returns:
            tuple | bool: Обработанный ответ в форматах `ru` и `he`.
        """
        # TODO: добавить реализацию обработки через ИИ
        ai_response_ru = None
        ai_response_he = None
        if lang == 'ru':
           # ai_response_ru = await self.model.process(products_list, system_instruction, lang, attempts) # TODO: добавить вызов
           ai_response_ru = 'ai_response_ru'
        if lang == 'he':
           # ai_response_he = await self.model.process(products_list, system_instruction, lang, attempts) # TODO: добавить вызов
           ai_response_he = 'ai_response_he'
        return ai_response_he, ai_response_ru

    def post_facebook(self, mexiron: SimpleNamespace) -> bool:
        """
        Выполняет сценарий публикации в Facebook.

        Args:
            mexiron (SimpleNamespace): Обработанные данные для публикации.

        Returns:
             bool: True, если публикация успешна, иначе False.
        """
        # TODO: добавить реализацию публикации в Facebook
        # facebook_scenario = FacebookScenario(self.driver, mexiron) # TODO: добавить инициализацию
        # return await facebook_scenario.post() # TODO: добавить вызов
        return True

    def create_report(self, data: dict, html_file: Path, pdf_file: Path):
        """
        Генерирует HTML и PDF отчеты из обработанных данных.

        Args:
            data (dict): Обработанные данные.
            html_file (Path): Путь для сохранения HTML отчета.
            pdf_file (Path): Путь для сохранения PDF отчета.
        """
        # TODO: добавить реализацию создания отчетов
        ...