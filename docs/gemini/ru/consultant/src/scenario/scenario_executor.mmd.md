# Анализ кода модуля `scenario_executor.mmd`

**Качество кода**

10
-  Плюсы
    -  Представленна схема последовательности действий в формате mermaid.
    -  Схема является наглядным представлением работы модуля.
-  Минусы
    -  Файл не является исполняемым кодом на python, поэтому большая часть инструкций не применима.
    -  Необходимо переработать код в исполняемый код на python.
    -  Отсутствует описание модуля.

**Рекомендации по улучшению**

1. Необходимо переписать mmd файл в python файл, который будет соответствовать описанной логике.
2. Добавить описание модуля в формате reStructuredText (RST).
3. Реализовать функции и классы, соответствующие описанным операциям.
4. Добавить логирование для отслеживания ошибок и хода выполнения.
5. Добавить docstring к каждой функции, методу и классу.

**Оптимизированный код**

```python
"""
Модуль для выполнения сценариев сбора данных о продуктах.
===========================================================

Этот модуль содержит классы и функции для загрузки, итерации и запуска
сценариев, направленных на сбор информации о продуктах с веб-сайтов.
Он включает в себя навигацию по страницам, извлечение данных и сохранение
результатов.

Пример использования
--------------------

.. code-block:: python

    from src.scenario.scenario_executor import ScenarioExecutor

    executor = ScenarioExecutor()
    executor.run_all_scenarios()
"""

import asyncio
import json
from typing import List, Dict, Any

from src.utils.jjson import j_loads_ns
from src.logger.logger import logger # импортируем logger

# TODO: Добавить импорты для работы с Selenium, PrestaShop API, и другими необходимыми модулями

class ScenarioExecutor:
    """
    Класс для выполнения сценариев сбора данных о продуктах.

    :ivar scenario_files: Список путей к файлам сценариев.
    :vartype scenario_files: List[str]
    """
    def __init__(self, scenario_files: List[str] = None):
        """
        Инициализирует экземпляр класса ScenarioExecutor.

        :param scenario_files: Список путей к файлам сценариев.
        :type scenario_files: List[str], optional
        """
        self.scenario_files = scenario_files or []

    def _load_scenarios(self, file_path: str) -> List[Dict]:
        """
        Загружает сценарии из файла JSON.

        :param file_path: Путь к файлу JSON.
        :type file_path: str
        :return: Список словарей, представляющих сценарии.
        :rtype: List[Dict]
        :raises FileNotFoundError: Если файл не найден.
        :raises json.JSONDecodeError: Если файл не является валидным JSON.
        """
        try:
            # Загружаем сценарии из файла
            with open(file_path, 'r', encoding='utf-8') as f:
                scenarios = j_loads_ns(f)
            return scenarios
        except FileNotFoundError as e:
            logger.error(f'Файл не найден: {file_path}', exc_info=True)
            return []
        except json.JSONDecodeError as e:
             logger.error(f'Ошибка декодирования JSON в файле: {file_path}', exc_info=True)
             return []


    async def _run_scenario(self, scenario: Dict):
        """
        Выполняет один сценарий.

        :param scenario: Словарь, представляющий сценарий.
        :type scenario: Dict
        :raises Exception: В случае ошибки во время выполнения сценария.
        """
        try:
            # TODO: Реализация логики навигации, сбора данных и сохранения в PrestaShop
            logger.info(f'Начало выполнения сценария: {scenario.get("name", "Без имени")}')
            url = scenario.get('url')
            if not url:
                logger.error(f'URL не найден в сценарии: {scenario.get("name", "Без имени")}')
                return
            # Навигация к URL
            # TODO: Добавить реализацию навигации
            logger.info(f'Навигация к {url}')
            # Получаем список продуктов
            # TODO: Добавить реализацию получения списка продуктов
            products = ['product1', 'product2']
            for product in products:
                # TODO: Добавить реализацию навигации к странице продукта
                logger.info(f'Навигация к странице продукта: {product}')
                # TODO: Добавить реализацию сбора данных о продукте
                product_fields = {'name': 'Test Product', 'price': 100}
                # TODO: Добавить реализацию создания объекта продукта
                # TODO: Добавить реализацию вставки продукта в PrestaShop
                logger.info(f'Продукт {product} обработан и добавлен в PrestaShop')
            logger.info(f'Сценарий {scenario.get("name", "Без имени")} выполнен.')

        except Exception as ex:
             logger.error(f'Ошибка при выполнении сценария: {scenario.get("name", "Без имени")}', exc_info=True)
             ...

    async def _run_scenario_file(self, file_path: str):
        """
        Выполняет все сценарии, содержащиеся в файле.

        :param file_path: Путь к файлу сценария.
        :type file_path: str
        """
        scenarios = self._load_scenarios(file_path)
        if not scenarios:
            logger.warning(f'Нет сценариев для выполнения в файле: {file_path}')
            return
        tasks = [self._run_scenario(scenario) for scenario in scenarios]
        await asyncio.gather(*tasks)
    
    async def run_all_scenarios(self):
        """
        Выполняет все сценарии из списка файлов.

        """
        if not self.scenario_files:
             logger.warning('Список файлов сценариев пуст.')
             return
        tasks = [self._run_scenario_file(file_path) for file_path in self.scenario_files]
        await asyncio.gather(*tasks)
        logger.info('Завершено выполнение всех сценариев.')

    @staticmethod
    def validate_scenario_files(files: List[str]) -> (List[str], List[str]):
        """
         Проверяет список файлов на существование и возвращает два списка: валидные и невалидные файлы.

         :param files: Список путей к файлам.
         :type files: List[str]
         :return: Кортеж из двух списков - валидные и невалидные файлы.
         :rtype: (List[str], List[str])
         """
        valid_files = []
        invalid_files = []
        for file in files:
             try:
                # Проверяем, существует ли файл
                with open(file, 'r', encoding='utf-8') as f:
                    pass # Файл существует и открыт, добавляем его в список валидных
                valid_files.append(file)
             except FileNotFoundError:
                 invalid_files.append(file)
                 logger.error(f'Файл не найден: {file}', exc_info=True)
        return valid_files, invalid_files

if __name__ == '__main__':
     # Пример использования
     scenario_files = ['scenario1.json', 'scenario2.json', 'non_existent_file.json']  # Замените на ваши пути к файлам
     valid_files, invalid_files = ScenarioExecutor.validate_scenario_files(scenario_files)
     executor = ScenarioExecutor(valid_files)
     asyncio.run(executor.run_all_scenarios())
```