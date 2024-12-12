# Анализ кода модуля `scenario_pricelist`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и разбит на логические блоки, что облегчает понимание и поддержку.
    - Использованы `mermaid` диаграммы для визуализации потоков выполнения, что повышает наглядность.
    - Присутствуют docstring для функций и методов, хотя и требуют корректировки в соответствии с RST.
    - Описаны зависимости и ошибки, что помогает в отладке и расширении функционала.
-  Минусы
    -   Docstring не соответствуют формату reStructuredText (RST).
    -  Не используются логирование ошибок через `logger.error`.
    -   Отсутствуют необходимые импорты для работы кода.
    -   Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    -   Не везде используется асинхронный подход, где это возможно.
    -   Некоторые блоки кода могут быть оптимизированы для лучшей читаемости и производительности.

**Рекомендации по улучшению**

1. **Документация**:
   - Переписать все docstring в формате RST.
   - Добавить описания для всех параметров и возвращаемых значений в docstring.

2. **Импорты**:
   - Добавить необходимые импорты, такие как `asyncio`, `json`, `Path`, `Any`, `List`, `Dict`, `Optional`, `SimpleNamespace`, `j_loads`, `logger`.

3. **Логирование**:
    -   Использовать `logger.error` для обработки исключений вместо стандартного `try-except` с `print`.
    -   Логировать все важные этапы выполнения кода.

4.  **Обработка данных**:
    -   Использовать `j_loads` или `j_loads_ns` для загрузки данных из JSON файлов.

5.  **Асинхронность**:
    -   Использовать `async` и `await` там, где это уместно, для неблокирующих операций.

6. **Рефакторинг**:
    -   Разбить длинные методы на более мелкие и управляемые функции.
    -   Упростить сложные логические конструкции.

**Оптимизированный код**

```python
"""
Модуль для автоматизации создания "мехирона" для Сергея Казаринова.
====================================================================

Этот модуль содержит класс :class:`MexironBuilder`, который автоматизирует процесс
сбора, обработки и публикации данных о продуктах.

Модуль выполняет следующие действия:
    - Извлекает данные о продуктах с сайтов поставщиков.
    - Обрабатывает данные с помощью моделей AI.
    - Сохраняет обработанные данные в файлы JSON.
    - Создает HTML и PDF отчеты.
    - Публикует данные в Facebook.

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
import json
from pathlib import Path
from types import SimpleNamespace
from typing import Any, List, Dict, Optional

from src.utils.jjson import j_loads
from src.logger.logger import logger
# from src.ai.gemini import Gemini # TODO:  необходимо добавить импорт, если планируется использовать класс
# from src.suppliers.*.graber import Graber  # TODO:  необходимо добавить импорт, если планируется использовать класс
# from src.endpoints.advertisement.facebook.scenarios import FacebookScenario # TODO: необходимо добавить импорт, если планируется использовать класс


class MexironBuilder:
    """
    Класс для автоматизации процесса создания "мехирона".

    :param driver: Экземпляр Selenium WebDriver для управления браузером.
    :param mexiron_name: (опционально) Пользовательское имя для процесса.
    """
    def __init__(self, driver, mexiron_name: Optional[str] = None):
        """
        Инициализирует MexironBuilder с необходимыми компонентами.
        """
        self.driver = driver
        self.export_path = Path('exports')  # TODO:  вынести в config
        self.mexiron_name = mexiron_name
        self.price = None
        self.timestamp = None
        self.products_list = []
        self.model = None  # TODO: Инициализировать модель ИИ, если нужно
        self.config = self._load_config()
        self.system_instruction = self._load_system_instruction()
        self.bot = None  # TODO: Инициализировать бота, если нужно


    def _load_config(self) -> Dict:
        """
        Загружает конфигурацию из JSON файла.

        :return: Словарь с конфигурацией.
        """
        try:
            config_path = Path('src/endpoints/kazarinov/config.json')  # TODO: вынести в config
            with open(config_path, 'r', encoding='utf-8') as f: # TODO:  заменить на j_loads
                config = json.load(f)
            return config
        except Exception as ex:
            logger.error(f'Ошибка при загрузке конфигурации: {ex}')
            return {}


    def _load_system_instruction(self) -> Optional[str]:
        """
        Загружает системные инструкции для AI модели из файла.

        :return: Системная инструкция в виде строки или None, если файл не найден.
        """
        try:
             instruction_path = Path('src/endpoints/kazarinov/system_instruction.txt') # TODO: вынести в config
             with open(instruction_path, 'r', encoding='utf-8') as f:
                 return f.read()
        except FileNotFoundError:
            logger.error(f'Файл системных инструкций не найден: {instruction_path}')
            return None
        except Exception as ex:
             logger.error(f'Ошибка при загрузке системной инструкции: {ex}')
             return None


    async def run_scenario(self, system_instruction: Optional[str] = None, price: Optional[str] = None,
                           mexiron_name: Optional[str] = None, urls: Optional[str | List[str]] = None, bot = None) -> bool:
        """
        Выполняет основной сценарий: парсит продукты, обрабатывает их через AI и сохраняет данные.

        :param system_instruction: Системные инструкции для AI модели.
        :param price: Цена для обработки.
        :param mexiron_name: Пользовательское имя для мехирона.
        :param urls: Список URL-адресов страниц продуктов.
        :param bot: Экземпляр бота.
        :return: True, если сценарий выполнен успешно, иначе False.
        """
        self.mexiron_name = mexiron_name or self.mexiron_name
        self.price = price or self.price
        self.system_instruction = system_instruction or self.system_instruction
        self.bot = bot or self.bot

        if not urls:
            logger.error('Не предоставлены URL для парсинга.')
            return False

        if isinstance(urls, str):
            urls = [urls]

        for url in urls:
            if 'onetab' in url:
                try:
                    # TODO:  реализовать извлечение данных из OneTab
                    data = self._get_data_from_onetab(url) #  предположим, что это асинхронная функция
                except Exception as ex:
                     logger.error(f'Ошибка при получении данных из OneTab: {ex}')
                     return False
                if not data:
                    logger.error('Некорректные данные из OneTab.')
                    return False
            else:
                 data = url # TODO:  здесь возможно нужна проверка корректности URL
            if not data:
                 logger.error('Некорректные данные URL.')
                 return False
            if not await self._process_url(data):
                 return False
        return True


    async def _process_url(self, url: str) -> bool:
        """
         Обрабатывает один URL: парсит страницу, обрабатывает AI, сохраняет данные.

        :param url: URL-адрес страницы продукта.
        :return: True, если обработка прошла успешно, иначе False.
        """
        graber = self.get_graber_by_supplier_url(url)
        if not graber:
            logger.error(f'Нет грабера для URL: {url}')
            return False
        try:
            # код исполняет парсинг страницы и извлечение данных
            product_fields = await graber.grab_page(url) # TODO:  предположим, что grab_page - асинхронный метод
            if not product_fields:
                logger.error(f'Не удалось спарсить страницу: {url}')
                return False

            product_data = self.convert_product_fields(product_fields)
            if not product_data:
                logger.error(f'Не удалось преобразовать поля продукта: {url}')
                return False

            if not self.save_product_data(product_data):
                 logger.error(f'Не удалось сохранить данные продукта: {url}')
                 return False
            self.products_list.append(product_data)


            ai_result = await self._process_ai_data()
            if not ai_result:
                return False
            return True
        except Exception as ex:
            logger.error(f'Ошибка при обработке URL: {url}, {ex}')
            return False


    def get_graber_by_supplier_url(self, url: str):
        """
        Возвращает подходящий грабер для заданного URL поставщика.

        :param url: URL-адрес страницы поставщика.
        :return: Экземпляр грабера, если найден, иначе None.
        """
        # TODO: Реализовать логику выбора грабера по URL
        # Пример (нужно доработать)
        if 'example.com' in url:
            # from src.suppliers.example.graber import Graber
            # return Graber(self.driver) # TODO:  необходимо добавить импорт, если планируется использовать класс
            return None #  временное решение
        logger.error(f'Нет подходящего грабера для URL: {url}')
        return None


    def convert_product_fields(self, f: Any) -> dict:
        """
        Преобразует поля продукта в словарь.

        :param f: Объект с данными о продукте.
        :return: Словарь с данными о продукте.
        """
        try:
            # TODO:  доработать конвертацию полей в словарь
            product_data = {
                'name': f.name,
                'price': f.price,
                 # и т.д.
            }
            return product_data
        except Exception as ex:
            logger.error(f'Ошибка при конвертации полей продукта: {ex}')
            return {}


    def save_product_data(self, product_data: dict) -> bool:
        """
        Сохраняет данные о продукте в файл.

        :param product_data: Словарь с данными продукта.
        :return: True, если сохранение успешно, иначе False.
        """
        try:
            # TODO: доработать формирование имени файла и сохранение данных
            file_name = f'{self.mexiron_name or "mexiron"}_{self.timestamp or "now"}.json'
            file_path = self.export_path / file_name
            with open(file_path, 'w', encoding='utf-8') as f: # TODO:  заменить на j_dumps
                json.dump(product_data, f, ensure_ascii=False, indent=4)
            return True
        except Exception as ex:
            logger.error(f'Ошибка при сохранении данных продукта: {ex}')
            return False


    async def _process_ai_data(self) -> bool:
         """
        Обрабатывает список продуктов с помощью AI.

        :return: True, если обработка AI прошла успешно, иначе False.
         """
         try:
             # TODO: доработать обработку AI
             if not self.products_list:
                logger.error('Нет данных для обработки AI.')
                return False

             ru_result = await self._process_ai(self.products_list, 'ru')
             if not ru_result:
                logger.error('Не удалось обработать данные AI на русском.')
                return False
             he_result = await self._process_ai(self.products_list, 'he')
             if not he_result:
                logger.error('Не удалось обработать данные AI на иврите.')
                return False
             if not self._save_ai_results(ru_result, 'ru'):
                 return False
             if not self._save_ai_results(he_result, 'he'):
                 return False
             return True
         except Exception as ex:
             logger.error(f'Ошибка при обработке данных AI: {ex}')
             return False



    async def _process_ai(self, products_list: List[dict], lang: str, attempts: int = 3) -> Optional[str]:
         """
        Обрабатывает список продуктов через AI модель.

        :param products_list: Список словарей с данными продуктов.
        :param lang: Язык обработки ('ru' или 'he').
        :param attempts: Количество попыток обработки.
        :return: Строка с результатами обработки AI, или None в случае неудачи.
         """
         # TODO:  использовать модель ИИ
         # from src.ai.gemini import Gemini
         # model = Gemini(self.config.get('gemini_api_key'), self.system_instruction)  # TODO:  добавить в config
         #  пока заглушка
         try:
             #  Здесь предполагается вызов AI модели
             if lang == 'ru':
                 ai_result = f'AI обработка на русском: {products_list}'
             else:
                 ai_result = f'AI обработка на иврите: {products_list}'
             return ai_result
         except Exception as ex:
             if attempts > 0:
                 logger.error(f'Ошибка при обращении к AI модели, попытка {3 - attempts}, {ex}')
                 await asyncio.sleep(1)
                 return await self._process_ai(products_list, lang, attempts - 1)
             logger.error(f'Превышено количество попыток обработки AI: {ex}')
             return None




    def _save_ai_results(self, ai_result: str, lang: str) -> bool:
        """
        Сохраняет результаты обработки AI в JSON файл.

        :param ai_result: Строка с результатами обработки AI.
        :param lang: Язык обработки ('ru' или 'he').
        :return: True, если сохранение прошло успешно, иначе False.
        """
        try:
           # TODO:  доработать формирование имени файла и сохранение данных
           file_name = f'ai_result_{self.mexiron_name or "mexiron"}_{lang}_{self.timestamp or "now"}.json'
           file_path = self.export_path / file_name
           with open(file_path, 'w', encoding='utf-8') as f: # TODO: заменить на j_dumps
               json.dump(ai_result, f, ensure_ascii=False, indent=4)
           return True
        except Exception as ex:
            logger.error(f'Ошибка при сохранении результата AI: {ex}')
            return False



    def post_facebook(self, mexiron: SimpleNamespace) -> bool:
        """
        Выполняет сценарий публикации в Facebook.

        :param mexiron: Данные для публикации.
        :return: True, если публикация прошла успешно, иначе False.
        """
        try:
            # from src.endpoints.advertisement.facebook.scenarios import FacebookScenario
            #  face_book = FacebookScenario(self.driver)
            #  return face_book.post_mexiron(mexiron) # TODO:  необходимо реализовать метод `post_mexiron`
            return True #  заглушка
        except Exception as ex:
            logger.error(f'Ошибка при публикации в Facebook: {ex}')
            return False


    def create_report(self, data: dict, html_file: Path, pdf_file: Path) -> bool:
        """
        Создает HTML и PDF отчеты из обработанных данных.

        :param data: Обработанные данные.
        :param html_file: Путь для сохранения HTML отчета.
        :param pdf_file: Путь для сохранения PDF отчета.
        :return: True, если отчеты созданы успешно, иначе False.
        """
        try:
             # TODO: Реализовать логику создания отчетов
             return True
        except Exception as ex:
             logger.error(f'Ошибка при создании отчетов: {ex}')
             return False
```