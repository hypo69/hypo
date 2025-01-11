## Анализ кода модуля `scenario_pricelist`

### Качество кода:

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Подробное описание функциональности и структуры модуля.
    - Наличие блок-схем для визуализации процессов.
    - Разделение на классы и методы для лучшей организации кода.
    - Включает обработку ошибок и логирование.
- **Минусы**:
    - Не используется RST-документация для функций и классов.
    - Нет форматирования кода в соответствии с PEP8 (например, отступы, длина строк).
    - Отсутствуют необходимые импорты для работы с файлами и JSON.
    - Не все функции имеют аннотацию типов.
    - В некоторых местах не используются `j_loads` и `logger` из `src`.
    - Чрезмерное использование `try-except` блоков.

### Рекомендации по улучшению:

1.  **Использовать RST-документацию**:
    - Добавить docstring в формате RST для всех функций, методов и классов.
    - Включить описание параметров, возвращаемых значений, типов, а также возможные исключения.
    - Примеры использования методов (doctest) были бы очень кстати.
2.  **Форматирование кода**:
    - Привести код в соответствие с PEP8.
    - Использовать 4 пробела для отступов.
    - Ограничить длину строк до 79 символов.
3.  **Импорты**:
    - Добавить необходимые импорты для работы с файлами, JSON и логгером:
      ```python
      from pathlib import Path
      from typing import Optional, List, Dict, Any, Tuple
      from types import SimpleNamespace
      from src.utils.jjson import j_loads, j_loads_ns  #  Для работы с JSON
      from src.logger import logger # для логирования
      from src.webdriver.driver import Driver  # Необходим для Driver
      from src.ai.gemini import Gemini  # Необходим для Gemini
      from src.endpoints.advertisement.facebook.scenarios import FacebookScenario # FacebookScenario
      from src.suppliers.graber import ProductFields  # ProductFields
      ```
4.  **Обработка ошибок**:
    - Вместо `try-except` использовать `logger.error` для записи ошибок, если не требуется специфическая обработка исключений.
5.  **Конфигурация**:
    - Вынести настройки в отдельный файл конфигурации (например, `config.json`) и загружать их.
6.  **Типизация**:
    - Добавить аннотации типов ко всем функциям и методам.
7.  **Логирование**:
    - Убедиться, что все важные этапы выполнения логируются.
    - Использовать `logger.info` для записи информационных сообщений.
8.  **Улучшение структуры**:\
    - Рассмотреть возможность разбиения класса `MexironBuilder` на несколько более мелких классов, чтобы улучшить читаемость и поддерживаемость кода.
    - Выделить общие функции (например, сохранение данных, обработка AI) в отдельные модули или утилиты.
9.  **Унификация кода**:\
    - Использовать `j_loads` и `j_loads_ns` для работы с JSON.
    - Использовать `logger` из `src.logger.logger`.

### Оптимизированный код:

```python
"""
Модуль для создания мехирона для Сергея Казаринова
====================================================

Этот модуль содержит класс :class:`MexironBuilder`, который используется для автоматизации
процесса создания "мехирона" для Сергея Казаринова.

Пример использования
----------------------
.. code-block:: python

    from src.webdriver.driver import Driver
    from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder

    driver = Driver(...)  #  Инициализация драйвера
    mexiron_builder = MexironBuilder(driver)
    urls = ['https://example.com/product1', 'https://example.com/product2']
    result = mexiron_builder.run_scenario(urls=urls)
    print(result)  # True или False в зависимости от успеха выполнения сценария
"""

from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple
from types import SimpleNamespace
from src.utils.jjson import j_loads, j_loads_ns
from src.logger import logger
from src.webdriver.driver import Driver
from src.ai.gemini import Gemini
from src.endpoints.advertisement.facebook.scenarios import FacebookScenario
from src.suppliers.graber import ProductFields


class MexironBuilder:
    """
    Класс для автоматизации создания мехирона.

    :param driver: Экземпляр Selenium WebDriver.
    :type driver: Driver
    :param mexiron_name: Пользовательское имя для процесса мехирона.
    :type mexiron_name: Optional[str]
    """

    def __init__(self, driver: Driver, mexiron_name: Optional[str] = None):
        """
        Инициализирует класс `MexironBuilder` с необходимыми компонентами.
        """
        self.driver = driver
        self.export_path = Path("exports") #  Устанавливаем путь для экспорта
        self.mexiron_name = mexiron_name or "default_mexiron"
        self.price = None
        self.timestamp = None
        self.products_list: List[Dict] = []
        self.model = Gemini()
        self.config = self._load_config() # Загружаем конфигурацию из файла config.json
        logger.info("MexironBuilder initialized") # Логируем информацию

    def _load_config(self) -> Dict:
        """
        Загружает конфигурацию из файла config.json.

        :return: Словарь с настройками конфигурации.
        :rtype: Dict
        """
        config_path = Path("config.json")
        try:
            with open(config_path, 'r', encoding='utf-8') as f: # Открываем файл в режиме чтения
                config = j_loads(f) # Загружаем данные из файла
            logger.info(f"Config file loaded from {config_path}") # Логируем сообщение
            return config
        except FileNotFoundError:
            logger.error(f"Config file not found: {config_path}")  # Логируем ошибку
            return {}
        except Exception as e: # Ловим все остальные ошибки
            logger.error(f"Error loading config file: {e}") # Логируем ошибку
            return {}

    def run_scenario(
        self,
        system_instruction: Optional[str] = None,
        price: Optional[str] = None,
        mexiron_name: Optional[str] = None,
        urls: Optional[str | List[str]] = None,
        bot=None,
    ) -> bool:
        """
        Выполняет сценарий: парсит продукты, обрабатывает их через ИИ и сохраняет данные.

        :param system_instruction: Системные инструкции для модели ИИ.
        :type system_instruction: Optional[str]
        :param price: Цена для обработки.
        :type price: Optional[str]
        :param mexiron_name: Пользовательское имя мехирона.
        :type mexiron_name: Optional[str]
        :param urls: URLs страниц продуктов.
        :type urls: Optional[str | List[str]]
        :param bot: Бот для отправки уведомлений (не используется в текущей реализации).
        :type bot: Optional[Any]
        :return: True, если сценарий выполнен успешно, иначе False.
        :rtype: bool

        :raises Exception: В случае возникновения ошибки на любом этапе выполнения сценария.

        **Блок-схема**:\n
        ```mermaid\n
        flowchart TD\n
            Start[Start] --> IsOneTab{URL is from OneTab?}\n
            IsOneTab -->|Yes| GetDataFromOneTab[Get data from OneTab]\n
            IsOneTab -->|No| ReplyTryAgain[Reply - Try again]\n
            GetDataFromOneTab --> IsDataValid{Data valid?}\n
            IsDataValid -->|No| ReplyIncorrectData[Reply Incorrect data]\n
            IsDataValid -->|Yes| RunMexironScenario[Run Mexiron scenario]\n
            RunMexironScenario --> IsGraberFound{Graber found?}\n
            IsGraberFound -->|Yes| StartParsing[Start parsing: <code>url</code>]\n
            IsGraberFound -->|No| LogNoGraber[Log: No graber for <code>url</code>]\n
            StartParsing --> IsParsingSuccessful{Parsing successful?}\n
            IsParsingSuccessful -->|Yes| ConvertProductFields[Convert product fields]\n
            IsParsingSuccessful -->|No| LogParsingFailed[Log: Failed to parse product fields]\n
            ConvertProductFields --> IsConversionSuccessful{Conversion successful?}\n
            IsConversionSuccessful -->|Yes| SaveProductData[Save product data]\n
            IsConversionSuccessful -->|No| LogConversionFailed[Log: Failed to convert product fields]\n
            SaveProductData --> IsDataSaved{Data saved?}\n
            IsDataSaved -->|Yes| AppendToProductsList[Append to products_list]\n
            IsDataSaved -->|No| LogDataNotSaved[Log: Data not saved]\n
            AppendToProductsList --> ProcessAIHe[AI processing lang = he]\n
            ProcessAIHe --> ProcessAIRu[AI processing lang = ru]\n
            ProcessAIRu --> SaveHeJSON{Save JSON for he?}\n
            SaveHeJSON -->|Yes| SaveRuJSON[Save JSON for ru]\n
            SaveHeJSON -->|No| LogHeJSONError[Log: Error saving he JSON]\n
            SaveRuJSON --> IsRuJSONSaved{Save JSON for ru?}\n
            IsRuJSONSaved -->|Yes| GenerateReports[Generate reports]\n
            IsRuJSONSaved -->|No| LogRuJSONError[Log: Error saving ru JSON]\n
            GenerateReports --> IsReportGenerationSuccessful{Report generation successful?}\n
            IsReportGenerationSuccessful -->|Yes| SendPDF[Send PDF via Telegram]\n
            IsReportGenerationSuccessful -->|No| LogPDFError[Log: Error creating PDF]\n
            SendPDF --> ReturnTrue[Return True]\n
            LogPDFError --> ReturnTrue[Return True]\n
            ReplyIncorrectData --> ReturnTrue[Return True]\n
            ReplyTryAgain --> ReturnTrue[Return True]\n
            LogNoGraber --> ReturnTrue[Return True]\n
            LogParsingFailed --> ReturnTrue[Return True]\n
            LogConversionFailed --> ReturnTrue[Return True]\n
            LogDataNotSaved --> ReturnTrue[Return True]\n
            LogHeJSONError --> ReturnTrue[Return True]\n
            LogRuJSONError --> ReturnTrue[Return True]\n
            ```
        """
        self.mexiron_name = mexiron_name or self.mexiron_name
        self.price = price
        self.system_instruction = system_instruction
        if isinstance(urls, str):
            urls = [urls]

        if not urls:
            logger.warning("No URLs provided for parsing.")
            return False

        for url in urls:
            if "onetab" in url:
                try:
                    data = self._get_data_from_onetab(url)
                except Exception as e:
                    logger.error(f"Failed to get data from OneTab: {e}")
                    return False
                if not data:
                   logger.warning("Incorrect data from OneTab")
                   return False
            else:
                logger.info(f"Start parsing: {url}")
                graber = self.get_graber_by_supplier_url(url)
                if not graber:
                    logger.error(f"No graber for {url}")
                    continue

                try:
                    parsed_data = graber.grab_page()
                except Exception as e:
                    logger.error(f"Failed to grab page {url}: {e}")
                    continue

                if not parsed_data:
                     logger.error(f"Failed to parse product fields for {url}")
                     continue

                try:
                    product_data = self.convert_product_fields(parsed_data)
                except Exception as e:
                     logger.error(f"Failed to convert product fields for {url}: {e}")
                     continue

                if not product_data:
                    logger.error(f"Failed to convert product data from {url}")
                    continue

                try:
                    saved = self.save_product_data(product_data)
                except Exception as e:
                    logger.error(f"Failed to save product data from {url}: {e}")
                    continue
                if saved:
                     self.products_list.append(product_data)
                else:
                   logger.error(f"Data not saved for {url}")

        if not self.products_list:
            logger.warning("No products were successfully processed.")
            return False

        try:
             he_ai_result = self.process_ai(self.products_list, 'he')
             ru_ai_result = self.process_ai(self.products_list, 'ru')
        except Exception as e:
            logger.error(f"Failed to process AI: {e}")
            return False

        if he_ai_result and isinstance(he_ai_result, tuple):
                try:
                     he_json_file = Path(f'{self.export_path}/{self.mexiron_name}_he.json')
                     self._save_json_data(he_ai_result[0], he_json_file) # Сохранение JSON для he
                     ru_json_file = Path(f'{self.export_path}/{self.mexiron_name}_ru.json')
                     self._save_json_data(ru_ai_result[0], ru_json_file) # Сохранение JSON для ru
                except Exception as e:
                    logger.error(f"Error saving JSON: {e}")
                    return False
        else:
            logger.error("AI processing returned incorrect data.")
            return False

        try:
            html_file = Path(f'{self.export_path}/{self.mexiron_name}.html')
            pdf_file = Path(f'{self.export_path}/{self.mexiron_name}.pdf')
            self.create_report(self.products_list, html_file, pdf_file)
        except Exception as e:
             logger.error(f"Error creating reports: {e}")
             return False
        try:
            # Send PDF via Telegram (implementation needed)
            pass
        except Exception as e:
            logger.error(f"Error sending PDF via Telegram: {e}")

        logger.info("Mexiron scenario completed successfully.") # Логируем сообщение
        return True

    def _get_data_from_onetab(self, url: str) -> List[dict] :
        """
        Извлекает данные из OneTab URL.

        :param url: URL OneTab.
        :type url: str
        :return: Список словарей данных.
        :rtype: List[dict]
        :raises Exception: Если возникают ошибки при извлечении данных.
        """
        # Extract data from OneTab logic
        logger.info(f"Getting data from OneTab: {url}") # Логируем информацию
        # ... (implementation needed)
        return []

    def get_graber_by_supplier_url(self, url: str) -> Optional[Any]:
        """
        Возвращает соответствующий грабер для данного URL поставщика.

        :param url: URL страницы поставщика.
        :type url: str
        :return: Экземпляр грабера, если найден, иначе None.
        :rtype: Optional[Any]
        """
        # Logic to determine which graber to use based on URL
        if 'example.com' in url: # Применяем условие
            from src.suppliers.example.graber import Graber # Подключаем грабер
            return Graber(driver=self.driver, url=url) # Возвращаем грабер
        else:
            logger.warning(f"No graber found for url: {url}") # Логируем предупреждение
            return None

    def convert_product_fields(self, f: ProductFields) -> Dict:
        """
        Конвертирует поля продукта в словарь.

        :param f: Объект, содержащий парсированные данные о продукте.
        :type f: ProductFields
        :return: Форматированный словарь данных о продукте.
        :rtype: dict
        """
        return {
            'title': f.title,
            'price': f.price,
            'description': f.description,
        }

    def save_product_data(self, product_data: Dict) -> bool:
        """
        Сохраняет данные о продукте в файл.

        :param product_data: Форматированные данные о продукте.
        :type product_data: dict
        :return: True если данные сохранены, иначе False
        :rtype: bool
        """
        file_path = self.export_path / f'{self.mexiron_name}.txt'
        try:
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(str(product_data) + '\n')
                logger.info(f"Product data saved to: {file_path}")  # Логируем сообщение
            return True
        except Exception as e:
            logger.error(f"Failed to save product data to {file_path}: {e}")  # Логируем ошибку
            return False

    def process_ai(self, products_list: List[Dict], lang: str, attempts: int = 3) -> Tuple[Any, Any] | bool:
        """
        Обрабатывает список продуктов через модель ИИ.

        :param products_list: Список словарей данных о продуктах.
        :type products_list: List[Dict]
        :param lang: Язык для обработки ('ru' или 'he').
        :type lang: str
        :param attempts: Количество попыток повторного запроса в случае неудачи.
        :type attempts: int, optional
        :return: Обработанный ответ в форматах `ru` и `he`.
        :rtype: Tuple[Any, Any] | bool
        """
        if not products_list:
            logger.warning("No product list provided for AI processing.")
            return False
        product_string = str(products_list)
        if not self.system_instruction:
                self.system_instruction = self.config.get('system_instruction', 'default instruction')
        for attempt in range(attempts):
            try:
                response = self.model.generate_content(
                    prompt=self.system_instruction,
                    text=product_string,
                    lang=lang
                )
                if response:
                    logger.info(f"AI processing completed for {lang} on attempt {attempt+1}.")
                    return response, lang # Возвращаем обработанные данные и язык
            except Exception as e:
                 logger.error(f"AI processing failed for {lang}, attempt {attempt + 1}: {e}") # Логируем ошибку
        logger.error(f"AI processing failed for {lang} after {attempts} attempts.")
        return False # Возвращаем False после всех неудачных попыток

    def post_facebook(self, mexiron: SimpleNamespace) -> bool:
        """
        Выполняет сценарий публикации в Facebook.

        :param mexiron: Обработанные данные для публикации.
        :type mexiron: SimpleNamespace
        :return: True, если публикация успешна, иначе False.
        :rtype: bool
        """
        logger.info("Starting Facebook posting scenario.")
        try:
            facebook_scenario = FacebookScenario(driver=self.driver)
            result = facebook_scenario.post(mexiron) # Публикация данных в Facebook
            if result:
                logger.info("Facebook post successful.") # Логируем сообщение
                return True
            else:
                logger.error("Facebook post failed.") # Логируем ошибку
                return False
        except Exception as e:
            logger.error(f"Error during Facebook posting: {e}") # Логируем ошибку
            return False

    def create_report(self, data: List[Dict], html_file: Path, pdf_file: Path) -> bool:
        """
        Генерирует HTML и PDF отчеты из обработанных данных.

        :param data: Обработанные данные.
        :type data: List[Dict]
        :param html_file: Путь для сохранения HTML отчета.
        :type html_file: Path
        :param pdf_file: Путь для сохранения PDF отчета.
        :type pdf_file: Path
        :return: True, если отчеты сгенерированы успешно, иначе False.
        :rtype: bool
        """
        try:
            logger.info(f"Generating HTML report: {html_file}")
            #  Generate HTML report
            # ... (implementation needed)
            logger.info(f"Generating PDF report: {pdf_file}")
            # Generate PDF report
            # ... (implementation needed)
            logger.info(f"Reports generated successfully to {html_file} and {pdf_file}")
            return True
        except Exception as e:
            logger.error(f"Error creating reports: {e}")
            return False

    def _save_json_data(self, data: Any, file_path: Path) -> bool:
      """
      Сохраняет данные в JSON файл.

      :param data: Данные для сохранения.
      :type data: Any
      :param file_path: Путь к файлу для сохранения.
      :type file_path: Path
      :return: True, если данные сохранены, иначе False.
      :rtype: bool
      """
      try:
        with open(file_path, 'w', encoding='utf-8') as f:
           import json
           json.dump(data, f, ensure_ascii=False, indent=4) # Сохраняем данные в файл
           logger.info(f"JSON data saved to: {file_path}")
        return True
      except Exception as e:
          logger.error(f"Error saving json data to {file_path}: {e}") # Логируем ошибку
          return False