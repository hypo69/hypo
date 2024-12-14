# Анализ кода модуля `scenario_executor.mmd`

**Качество кода**
8
-   Плюсы
    - Код представляет собой диаграмму, хорошо отражает логику процесса выполнения сценариев.
    - Диаграмма четко структурирована и понятна, легко читается.
    - Используются стандартные обозначения для описания процессов и решений.
-   Минусы
    - Отсутствует текстовое описание к диаграмме, что затрудняет понимание её контекста.
    - Не используется reStructuredText (RST) для документирования.
    - Код представлен в виде диаграммы, а не в виде исполняемого кода.
    - Отсутствуют импорты, поскольку это диаграмма.

**Рекомендации по улучшению**

1.  Добавить текстовое описание к диаграмме для пояснения контекста.
2.  Преобразовать диаграмму в исполняемый код, добавив необходимые импорты, функции и классы.
3.  Использовать reStructuredText (RST) для документирования кода, включая описание модуля, классов, функций и переменных.
4.  При реализации кода, использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.load` для чтения файлов.
5.  Обрабатывать ошибки с помощью `logger.error` вместо стандартных блоков `try-except`.
6.  В комментариях к коду избегать слов типа 'получаем', 'делаем'. Использовать конкретные формулировки, такие как 'проверка', 'отправка', 'код исполняет ...'.
7.  Добавить логирование всех важных этапов выполнения сценариев.

**Оптимизированный код**

```markdown
    """
    Диаграмма процесса выполнения сценариев
    =========================================================================================

    Эта диаграмма описывает процесс выполнения сценариев для сбора данных о продуктах из веб-сайта и их последующей вставки в PrestaShop.
    Процесс начинается с экземпляра поставщика, затем проходит через проверку и запуск сценариев, сбор данных о продуктах,
    и завершается вставкой продуктов в PrestaShop и обновлением журнала.

    Описание процесса
    --------------------

    1. **Supplier Instance (A)**: Начальная точка, представляющая экземпляр поставщика.

    2. **Scenario Files List (B)**: Список файлов сценариев, которые необходимо обработать.

        -   **Valid List**: Список валидных файлов сценариев, которые будут выполнены.
        -   **Invalid List**: Список невалидных файлов сценариев, которые будут обработаны через механизм обработки ошибок.

    3. **Run Scenario Files (C)**: Запуск обработки валидных файлов сценариев.

    4. **Error Handling (D)**: Обработка ошибок, возникающих при работе с невалидными файлами сценариев.

    5. **Iterate Through Each Scenario File (E)**: Цикл перебора каждого файла сценария.

    6. **Run Scenario File (F)**: Запуск выполнения отдельного файла сценария.

    7. **Load Scenarios (G)**: Загрузка сценариев из файла.

    8. **Iterate Through Each Scenario (H)**: Цикл перебора каждого сценария в файле.

    9. **Run Scenario (I)**: Запуск выполнения отдельного сценария.

    10. **Navigate to URL (J)**: Переход на URL, указанный в сценарии.

    11. **Get List of Products (K)**: Получение списка продуктов с веб-страницы.

    12. **Iterate Through Products (L)**: Цикл перебора каждого продукта в списке.

    13. **Navigate to Product Page (M)**: Переход на страницу отдельного продукта.

    14. **Grab Product Fields (N)**: Получение полей продукта со страницы.

    15. **Create Product Object (O)**: Создание объекта продукта на основе полученных данных.

    16. **Insert Product into PrestaShop (P)**: Вставка продукта в PrestaShop.

        -   **Success**: Успешная вставка продукта.
        -   **Failure**: Неуспешная вставка продукта.

    17. **Success (Q)**: Успешное завершение процесса вставки продукта.

    18. **Error Handling (R)**: Обработка ошибок, возникающих при вставке продукта.

    19. **Update Journal (S)**: Обновление журнала с результатами выполнения сценария.

    20. **Return True/False (T)**: Возврат результата выполнения процесса - True, если все прошло успешно, иначе False.

    """
```
```python
"""
Модуль для выполнения сценариев сбора данных о продуктах и их вставки в PrestaShop.
=========================================================================================

Этот модуль содержит логику выполнения сценариев для сбора данных о продуктах с веб-сайтов и их последующей вставки в PrestaShop.
Он включает в себя чтение файлов сценариев, навигацию по страницам продуктов, извлечение полей продукта и вставку данных в PrestaShop.

Пример использования
--------------------

Пример использования класса ScenarioExecutor:

.. code-block:: python

    executor = ScenarioExecutor(driver, prestashop_api)
    executor.run_scenarios('path/to/scenarios')
"""
import asyncio
import os
from typing import List, Dict, Any
# from src.utils.jjson import j_loads #TODO: Раскоментировать когда будет реализован этот функционал
from src.logger.logger import logger
# from src.prestashop_api import PrestaShopAPI #TODO: Раскоментировать когда будет реализован этот функционал
# from selenium.webdriver.remote.webdriver import WebDriver #TODO: Раскоментировать когда будет реализован этот функционал


class ScenarioExecutor:
    """
    Класс для выполнения сценариев сбора данных о продуктах и их вставки в PrestaShop.
    """

    def __init__(self, driver: Any, prestashop_api: Any):
        """
        Инициализирует ScenarioExecutor.

        :param driver: Экземпляр веб-драйвера Selenium.
        :param prestashop_api: Экземпляр PrestaShopAPI для взаимодействия с PrestaShop.
        """
        self.driver = driver
        self.prestashop_api = prestashop_api

    async def _load_scenarios(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Загружает сценарии из файла JSON.

        :param file_path: Путь к файлу со сценариями.
        :return: Список словарей, представляющих сценарии.
        :raises FileNotFoundError: Если файл не найден.
        """
        try:
            # Код загружает сценарии из файла, используя j_loads_ns
            # with open(file_path, 'r', encoding='utf-8') as file: #TODO: Закоментировать когда будет реализован этот функционал
            #    return j_loads_ns(file) #TODO: Заменить на j_loads_ns когда будет реализован этот функционал
            ... # TODO: заменить на реальный код
        except FileNotFoundError as e:
            logger.error(f'Файл не найден: {file_path}', exc_info=True)
            raise e
        except Exception as e:
            logger.error(f'Ошибка при загрузке сценариев из файла: {file_path}', exc_info=True)
            return []

    async def _run_scenario(self, scenario: Dict[str, Any]) -> bool:
        """
        Выполняет один сценарий.

        :param scenario: Словарь, представляющий сценарий.
        :return: True, если сценарий выполнен успешно, иначе False.
        """
        try:
            # Код исполняет навигацию к URL из сценария
            url = scenario.get('url')
            if not url:
                logger.error(f'URL не найден в сценарии: {scenario}')
                return False
            await self.driver.get(url)

            # Код исполняет получение списка продуктов
            products = await self._get_products(scenario)
            if not products:
                logger.warning(f'Список продуктов не получен для сценария: {scenario}')
                return False

            # Код исполняет итерацию по продуктам и вставку каждого из них
            for product_data in products:
                 if not await self._process_product(product_data, scenario):
                    return False
            return True
        except Exception as e:
            logger.error(f'Ошибка при выполнении сценария: {scenario}', exc_info=True)
            return False

    async def _get_products(self, scenario: Dict[str, Any]) -> List[Dict[str, Any]]:
          """
          Извлекает список продуктов, используя локаторы из сценария.

          :param scenario: Словарь, представляющий сценарий.
          :return: Список словарей, представляющих продукты.
          """
          try:
              # Код исполняет получение списка продуктов
              # products_locator = scenario.get('products_locator') #TODO: Раскоментировать когда будет реализован этот функционал
              # if not products_locator: #TODO: Раскоментировать когда будет реализован этот функционал
              #     logger.error(f'Локатор продуктов не найден в сценарии: {scenario}') #TODO: Раскоментировать когда будет реализован этот функционал
              #     return [] #TODO: Раскоментировать когда будет реализован этот функционал
              # products = await self.driver.find_elements(products_locator['by'], products_locator['value']) #TODO: Раскоментировать когда будет реализован этот функционал
              # return products #TODO: Заменить на реальный код
              ...  # TODO: заменить на реальный код
          except Exception as e:
              logger.error(f'Ошибка при получении списка продуктов: {scenario}', exc_info=True)
              return []
    
    async def _process_product(self, product_data: Any, scenario: Dict[str, Any]) -> bool:
        """
        Обрабатывает один продукт, извлекая его данные и вставляя в PrestaShop.

        :param product_data: Данные продукта.
        :param scenario: Словарь, представляющий сценарий.
        :return: True, если продукт обработан успешно, иначе False.
        """
        try:
            # Код исполняет переход на страницу продукта
            product_url = product_data.get('url')
            if not product_url:
                logger.error(f'URL продукта не найден: {product_data}')
                return False
            await self.driver.get(product_url)
            # Код исполняет извлечение полей продукта
            product_fields = await self._grab_product_fields(scenario)
            if not product_fields:
                logger.warning(f'Поля продукта не получены: {product_data}')
                return False
            # Код исполняет создание объекта продукта
            product_object = self._create_product_object(product_fields)
             # Код исполняет вставку продукта в PrestaShop
            if not await self.prestashop_api.insert_product(product_object):
                logger.error(f'Не удалось вставить продукт в PrestaShop: {product_object}')
                return False
            return True
        except Exception as e:
            logger.error(f'Ошибка при обработке продукта: {product_data}', exc_info=True)
            return False

    async def _grab_product_fields(self, scenario: Dict[str, Any]) -> Dict[str, Any]:
      """
      Извлекает поля продукта, используя локаторы из сценария.

      :param scenario: Словарь, представляющий сценарий.
      :return: Словарь с полями продукта.
      """
      try:
          # Код исполняет извлечение полей продукта
          # fields_locators = scenario.get('fields_locators') #TODO: Раскоментировать когда будет реализован этот функционал
          # if not fields_locators: #TODO: Раскоментировать когда будет реализован этот функционал
          #     logger.error(f'Локаторы полей не найдены в сценарии: {scenario}') #TODO: Раскоментировать когда будет реализован этот функционал
          #     return {} #TODO: Раскоментировать когда будет реализован этот функционал
          # product_fields = {} #TODO: Раскоментировать когда будет реализован этот функционал
          # for field, locator in fields_locators.items(): #TODO: Раскоментировать когда будет реализован этот функционал
          #     value = await self.driver.find_element(locator['by'], locator['value']).text #TODO: Раскоментировать когда будет реализован этот функционал
          #     product_fields[field] = value #TODO: Раскоментировать когда будет реализован этот функционал
          # return product_fields #TODO: Заменить на реальный код
          ...  # TODO: заменить на реальный код
      except Exception as e:
          logger.error(f'Ошибка при извлечении полей продукта: {scenario}', exc_info=True)
          return {}

    def _create_product_object(self, product_fields: Dict[str, Any]) -> Dict[str, Any]:
        """
        Создает объект продукта для вставки в PrestaShop.

        :param product_fields: Словарь с полями продукта.
        :return: Словарь, представляющий объект продукта.
        """
        # Код создает объект продукта из полей
        product_object = {
            'name': product_fields.get('name'),
            'description': product_fields.get('description'),
            'price': product_fields.get('price'),
             #TODO: Добавить другие поля по мере необходимости
        }
        return product_object

    async def run_scenarios(self, scenarios_path: str) -> bool:
        """
        Запускает выполнение сценариев из указанной директории.

        :param scenarios_path: Путь к директории со сценариями.
        :return: True, если все сценарии выполнены успешно, иначе False.
        """
        try:
            # Код исполняет проверку существования директории
            if not os.path.exists(scenarios_path):
                logger.error(f'Директория не найдена: {scenarios_path}')
                return False

            # Код исполняет итерацию по файлам в директории
            for file_name in os.listdir(scenarios_path):
                if file_name.endswith('.json'):
                     file_path = os.path.join(scenarios_path, file_name)
                     # Код исполняет загрузку сценариев из файла
                     scenarios = await self._load_scenarios(file_path)
                     if not scenarios:
                         logger.warning(f'Сценарии не загружены из файла: {file_path}')
                         continue
                      # Код исполняет итерацию по сценариям и запуск каждого из них
                     for scenario in scenarios:
                        if not await self._run_scenario(scenario):
                            logger.warning(f'Сценарий не выполнен: {scenario}')
                            return False

            return True
        except Exception as e:
            logger.error(f'Ошибка при выполнении сценариев: {scenarios_path}', exc_info=True)
            return False

```