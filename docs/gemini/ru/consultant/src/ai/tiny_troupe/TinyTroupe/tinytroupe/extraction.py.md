# Анализ кода модуля `extraction.py`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разбит на классы, что облегчает его понимание и поддержку.
    - Используется `logger` для логирования, что позволяет отслеживать ошибки и процесс работы программы.
    - Присутствует кэширование результатов извлечения данных, что повышает производительность.
    - Применяется шаблонизация через `chevron`, что упрощает формирование промптов.
    - Есть механизм нормализации текста, полезный для унификации данных.
- Минусы
    -  Не все функции и методы документированы в формате RST.
    -  Используется `json.dump` вместо `j_dumps` или `j_dumps_ns` (хотя в этом файле нет `j_dumps`, нужно использовать `json.dumps`)
    -  Иногда используются стандартные конструкции `try-except` вместо обработки ошибок через `logger.error`.
    -  В некоторых местах отсутствуют проверки на корректность входных данных.
    -  Некоторые комментарии могут быть более подробными.
    -  Смешаны стили форматирования (где-то есть пустые строки после определения функции, где-то нет)

**Рекомендации по улучшению**

1.  **Документация:**
    -   Добавить docstrings в формате RST ко всем классам, методам и функциям, включая описание параметров, возвращаемых значений и возможных исключений.

2.  **Использование `j_dumps`:**
    -   Заменить `json.dump` на `json.dumps` (так как нет `j_dumps` в импортах), обеспечивая согласованность в обработке JSON.

3.  **Обработка ошибок:**
    -   Заменить стандартные блоки `try-except` на обработку ошибок с помощью `logger.error` для централизованного логирования.

4.  **Проверки входных данных:**
    -   Добавить проверки на корректность входных данных, чтобы предотвратить ошибки во время выполнения.

5.  **Комментарии:**
    -   Сделать комментарии более подробными, особенно в сложных участках кода, чтобы упростить понимание.
    -   Использовать reStructuredText (RST) для всех комментариев.

6.  **Стиль кода:**
    -   Унифицировать стиль кода (например, добавить или удалить пустые строки после определений функций).

**Оптимизированный код**
```python
"""
Модуль для извлечения данных из симуляций TinyTroupe
=========================================================================================

Этот модуль предоставляет различные утилиты для извлечения данных из элементов TinyTroupe,
таких как агенты и миры. Он также предоставляет механизм для сокращения извлеченных данных
до более краткой формы и для экспорта артефактов из элементов TinyTroupe.

Пример использования
--------------------

Пример использования класса :class:`ResultsExtractor`:

.. code-block:: python

    extractor = ResultsExtractor()
    agent_results = extractor.extract_results_from_agent(agent, "Some objective")
    world_results = extractor.extract_results_from_world(world, "Some objective")
"""

import os
import json
import chevron
import logging
import pandas as pd
import pypandoc
import markdown
from typing import Union, List, Dict, Any
from src.utils.jjson import j_loads, j_loads_ns
from src.logger.logger import logger #  Импортируем logger

from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
from tinytroupe.factory import TinyPersonFactory
from tinytroupe.utils import JsonSerializableRegistry
from tinytroupe import openai_utils
import tinytroupe.utils as utils

class ResultsExtractor:
    """
    Класс для извлечения результатов из объектов TinyTroupe.

    :ivar _extraction_prompt_template_path: Путь к шаблону запроса для извлечения.
    :vartype _extraction_prompt_template_path: str
    :ivar agent_extraction: Словарь для хранения результатов извлечения из агентов.
    :vartype agent_extraction: dict
    :ivar world_extraction: Словарь для хранения результатов извлечения из миров.
    :vartype world_extraction: dict
    """
    def __init__(self):
        """
        Инициализирует ResultsExtractor.
        """
        self._extraction_prompt_template_path = os.path.join(os.path.dirname(__file__), 'prompts/interaction_results_extractor.mustache')
        # Кэшируем последние результаты извлечения для каждого типа, чтобы их можно было использовать для создания отчетов или других дополнительных выходных данных.
        self.agent_extraction = {}
        self.world_extraction = {}

    def extract_results_from_agent(self,
                        tinyperson: TinyPerson,
                        extraction_objective: str = "The main points present in the agent's interactions history.",
                        situation: str = "",
                        fields: list = None,
                        fields_hints: dict = None,
                        verbose: bool = False) -> dict:
        """
        Извлекает результаты из экземпляра TinyPerson.

        :param tinyperson: Экземпляр TinyPerson, из которого извлекаются результаты.
        :type tinyperson: TinyPerson
        :param extraction_objective: Цель извлечения.
        :type extraction_objective: str
        :param situation: Ситуация, которую нужно учитывать.
        :type situation: str
        :param fields: Поля для извлечения. Если None, извлекатель сам решает, какие имена использовать.
        :type fields: list, optional
        :param fields_hints: Подсказки для полей.
        :type fields_hints: dict, optional
        :param verbose: Выводить ли отладочные сообщения.
        :type verbose: bool, optional
        :return: Результаты извлечения.
        :rtype: dict
        """
        messages = []

        rendering_configs = {}
        if fields is not None:
            rendering_configs["fields"] = ", ".join(fields)

        if fields_hints is not None:
            rendering_configs["fields_hints"] = list(fields_hints.items())

        messages.append({"role": "system",
                         "content": chevron.render(
                             open(self._extraction_prompt_template_path).read(),
                             rendering_configs)})

        interaction_history = tinyperson.pretty_current_interactions(max_content_length=None)

        extraction_request_prompt = \
f"""
## Extraction objective

{extraction_objective}

## Situation
You are considering a single agent, named {tinyperson.name}. Your objective thus refers to this agent specifically.
{situation}

## Agent Interactions History

You will consider an agent's history of interactions, which include stimuli it received as well as actions it
performed.

{interaction_history}
"""
        messages.append({"role": "user", "content": extraction_request_prompt})

        next_message = openai_utils.client().send_message(messages, temperature=0.0)

        debug_msg = f"Extraction raw result message: {next_message}"
        logger.debug(debug_msg)
        if verbose:
            print(debug_msg)

        if next_message is not None:
            result = utils.extract_json(next_message["content"])
        else:
            result = None

        # Кэшируем результат
        self.agent_extraction[tinyperson.name] = result

        return result

    def extract_results_from_world(self,
                                   tinyworld: TinyWorld,
                                   extraction_objective: str = "The main points that can be derived from the agents conversations and actions.",
                                   situation: str = "",
                                   fields: list = None,
                                   fields_hints: dict = None,
                                   verbose: bool = False) -> dict:
        """
        Извлекает результаты из экземпляра TinyWorld.

        :param tinyworld: Экземпляр TinyWorld, из которого извлекаются результаты.
        :type tinyworld: TinyWorld
        :param extraction_objective: Цель извлечения.
        :type extraction_objective: str
        :param situation: Ситуация, которую нужно учитывать.
        :type situation: str
        :param fields: Поля для извлечения. Если None, извлекатель сам решает, какие имена использовать.
        :type fields: list, optional
        :param fields_hints: Подсказки для полей.
        :type fields_hints: dict, optional
        :param verbose: Выводить ли отладочные сообщения.
        :type verbose: bool, optional
        :return: Результаты извлечения.
        :rtype: dict
        """
        messages = []

        rendering_configs = {}
        if fields is not None:
            rendering_configs["fields"] = ", ".join(fields)

        if fields_hints is not None:
            rendering_configs["fields_hints"] = list(fields_hints.items())

        messages.append({"role": "system",
                         "content": chevron.render(
                             open(self._extraction_prompt_template_path).read(),
                             rendering_configs)})

        # TODO: либо сначала суммировать, либо разбивать на несколько задач
        interaction_history = tinyworld.pretty_current_interactions(max_content_length=None)

        extraction_request_prompt = \
f"""
## Extraction objective

{extraction_objective}

## Situation
You are considering various agents.
{situation}

## Agents Interactions History

You will consider the history of interactions from various agents that exist in an environment called {tinyworld.name}.
Each interaction history includes stimuli the corresponding agent received as well as actions it performed.

{interaction_history}
"""
        messages.append({"role": "user", "content": extraction_request_prompt})

        next_message = openai_utils.client().send_message(messages, temperature=0.0)

        debug_msg = f"Extraction raw result message: {next_message}"
        logger.debug(debug_msg)
        if verbose:
            print(debug_msg)

        if next_message is not None:
            result = utils.extract_json(next_message["content"])
        else:
            result = None

        # Кэшируем результат
        self.world_extraction[tinyworld.name] = result

        return result

    def save_as_json(self, filename: str, verbose: bool = False):
        """
        Сохраняет последние результаты извлечения в формате JSON.

        :param filename: Имя файла для сохранения JSON.
        :type filename: str
        :param verbose: Выводить ли отладочные сообщения.
        :type verbose: bool, optional
        """
        try:
            with open(filename, 'w') as f:
                json.dump({"agent_extractions": self.agent_extraction,
                           "world_extraction": self.world_extraction}, f, indent=4)
            if verbose:
                print(f"Saved extraction results to {filename}")
        except Exception as e:
            logger.error(f"Ошибка при сохранении в JSON файл {filename}: {e}", exc_info=True)


class ResultsReducer:
    """
    Класс для сокращения результатов.

    :ivar results: Словарь для хранения результатов.
    :vartype results: dict
    :ivar rules: Словарь для хранения правил сокращения.
    :vartype rules: dict
    """
    def __init__(self):
        """
        Инициализирует ResultsReducer.
        """
        self.results = {}
        self.rules = {}

    def add_reduction_rule(self, trigger: str, func: callable):
        """
        Добавляет правило сокращения.

        :param trigger: Триггер для правила.
        :type trigger: str
        :param func: Функция для применения правила.
        :type func: callable
        :raises Exception: Если правило для данного триггера уже существует.
        """
        if trigger in self.rules:
            raise Exception(f"Rule for {trigger} already exists.")
        self.rules[trigger] = func

    def reduce_agent(self, agent: TinyPerson) -> list:
        """
        Сокращает данные агента.

        :param agent: Экземпляр TinyPerson, данные которого сокращаются.
        :type agent: TinyPerson
        :return: Сокращенные данные.
        :rtype: list
        """
        reduction = []
        for message in agent.episodic_memory.retrieve_all():
            if message['role'] == 'system':
                continue # ничего не делаем для роли `system` пока что

            elif message['role'] == 'user':
                # Роль пользователя связана только со стимулами
                stimulus_type = message['content']['stimuli'][0]['type']
                stimulus_content = message['content']['stimuli'][0]['content']
                stimulus_source = message['content']['stimuli'][0]['source']
                stimulus_timestamp = message['simulation_timestamp']

                if stimulus_type in self.rules:
                    extracted = self.rules[stimulus_type](focus_agent=agent, source_agent=TinyPerson.get_agent_by_name(stimulus_source), target_agent=agent, kind='stimulus', event=stimulus_type, content=stimulus_content, timestamp=stimulus_timestamp)
                    if extracted is not None:
                        reduction.append(extracted)

            elif message['role'] == 'assistant':
                # Роль ассистента связана только с действиями
                if 'action' in message['content']:
                    action_type = message['content']['action']['type']
                    action_content = message['content']['action']['content']
                    action_target = message['content']['action']['target']
                    action_timestamp = message['simulation_timestamp']

                    if action_type in self.rules:
                        extracted = self.rules[action_type](focus_agent=agent, source_agent=agent, target_agent=TinyPerson.get_agent_by_name(action_target), kind='action', event=action_type, content=action_content, timestamp=action_timestamp)
                        if extracted is not None:
                            reduction.append(extracted)

        return reduction

    def reduce_agent_to_dataframe(self, agent: TinyPerson, column_names: list = None) -> pd.DataFrame:
        """
        Сокращает данные агента до DataFrame.

        :param agent: Экземпляр TinyPerson, данные которого сокращаются.
        :type agent: TinyPerson
        :param column_names: Имена столбцов DataFrame.
        :type column_names: list, optional
        :return: DataFrame с сокращенными данными.
        :rtype: pd.DataFrame
        """
        reduction = self.reduce_agent(agent)
        return pd.DataFrame(reduction, columns=column_names)


class ArtifactExporter(JsonSerializableRegistry):
    """
    Экспортер артефактов из элементов TinyTroupe.

    :ivar base_output_folder: Базовая папка для вывода.
    :vartype base_output_folder: str
    """
    def __init__(self, base_output_folder: str) -> None:
        """
        Инициализирует ArtifactExporter.

        :param base_output_folder: Базовая папка для вывода.
        :type base_output_folder: str
        """
        self.base_output_folder = base_output_folder

    def export(self, artifact_name: str, artifact_data: Union[dict, str], content_type: str, content_format: str = None, target_format: str = "txt", verbose: bool = False):
        """
        Экспортирует данные артефакта в файл.

        :param artifact_name: Имя артефакта.
        :type artifact_name: str
        :param artifact_data: Данные для экспорта. Если dict, то сохраняется как JSON. Если str, то сохраняется как есть.
        :type artifact_data: Union[dict, str]
        :param content_type: Тип контента внутри артефакта.
        :type content_type: str
        :param content_format: Формат контента внутри артефакта (например, md, csv и т.д.).
        :type content_format: str, optional
        :param target_format: Формат экспорта артефакта (например, json, txt, docx и т.д.).
        :type target_format: str, optional
        :param verbose: Выводить ли отладочные сообщения.
        :type verbose: bool, optional
        :raises ValueError: Если данные артефакта не являются строкой или словарем.
        :raises ValueError: Если указанный целевой формат не поддерживается.
        """
        # Убираем лишние отступы, на всякий случай
        if isinstance(artifact_data, str):
            artifact_data = utils.dedent(artifact_data)
        elif isinstance(artifact_data, dict):
            artifact_data['content'] = utils.dedent(artifact_data['content'])
        else:
            raise ValueError("The artifact data must be either a string or a dictionary.")

        # Очищаем имя артефакта от недопустимых символов
        invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '\n', '\t', '\r', ';']
        for char in invalid_chars:
            if char in artifact_name:
                artifact_name = artifact_name.replace(char, "-")
                logger.warning(f"Replaced invalid character {char} with hyphen in artifact name '{artifact_name}'.")

        artifact_file_path = self._compose_filepath(artifact_data, artifact_name, content_type, target_format, verbose)

        if target_format == "json":
            self._export_as_json(artifact_file_path, artifact_data, content_type, verbose)
        elif target_format == "txt" or target_format == "text" or target_format == "md" or target_format == "markdown":
            self._export_as_txt(artifact_file_path, artifact_data, content_type, verbose)
        elif target_format == "docx":
            self._export_as_docx(artifact_file_path, artifact_data, content_format, verbose)
        else:
            raise ValueError(f"Unsupported target format: {target_format}.")

    def _export_as_txt(self, artifact_file_path: str, artifact_data: Union[dict, str], content_type: str, verbose: bool = False):
        """
        Экспортирует данные артефакта в текстовый файл.

        :param artifact_file_path: Путь к файлу для экспорта.
        :type artifact_file_path: str
        :param artifact_data: Данные для экспорта.
        :type artifact_data: Union[dict, str]
        :param content_type: Тип контента внутри артефакта.
        :type content_type: str
        :param verbose: Выводить ли отладочные сообщения.
        :type verbose: bool, optional
        """
        try:
           with open(artifact_file_path, 'w', encoding="utf-8") as f:
               if isinstance(artifact_data, dict):
                   content = artifact_data['content']
               else:
                   content = artifact_data
               f.write(content)
        except Exception as e:
            logger.error(f"Ошибка при экспорте в текстовый файл {artifact_file_path}: {e}", exc_info=True)

    def _export_as_json(self, artifact_file_path: str, artifact_data: Union[dict, str], content_type: str, verbose: bool = False):
        """
        Экспортирует данные артефакта в JSON файл.

        :param artifact_file_path: Путь к файлу для экспорта.
        :type artifact_file_path: str
        :param artifact_data: Данные для экспорта.
        :type artifact_data: Union[dict, str]
        :param content_type: Тип контента внутри артефакта.
        :type content_type: str
        :param verbose: Выводить ли отладочные сообщения.
        :type verbose: bool, optional
         :raises ValueError: Если данные артефакта не являются словарем.
        """
        try:
            with open(artifact_file_path, 'w', encoding="utf-8") as f:
                if isinstance(artifact_data, dict):
                    json.dump(artifact_data, f, indent=4)
                else:
                   raise ValueError("The artifact data must be a dictionary to export to JSON.")
        except Exception as e:
            logger.error(f"Ошибка при экспорте в JSON файл {artifact_file_path}: {e}", exc_info=True)

    def _export_as_docx(self, artifact_file_path: str, artifact_data: Union[dict, str], content_original_format: str, verbose: bool = False):
        """
        Экспортирует данные артефакта в DOCX файл.

        :param artifact_file_path: Путь к файлу для экспорта.
        :type artifact_file_path: str
        :param artifact_data: Данные для экспорта.
        :type artifact_data: Union[dict, str]
        :param content_original_format: Исходный формат контента внутри артефакта.
        :type content_original_format: str
        :param verbose: Выводить ли отладочные сообщения.
        :type verbose: bool, optional
        :raises ValueError: Если исходный формат контента не поддерживается для экспорта в DOCX.
        """
        if content_original_format not in ['text', 'txt', 'markdown', 'md']:
            raise ValueError(f"The original format cannot be {content_original_format} to export to DOCX.")
        else:
            # Нормализуем значение content_original_format
            content_original_format = 'markdown' if content_original_format == 'md' else content_original_format

        # Сначала получаем контент для экспорта. Если `artifact_date` - словарь, контент должен быть под ключом `content`.
        # Если это строка, контент - это сама строка.
        # Используем pypandoc
        if isinstance(artifact_data, dict):
            content = artifact_data['content']
        else:
            content = artifact_data
        try:
            # Сначала преобразуем в HTML. Это необходимо, потому что pypandoc не поддерживает ХОРОШЕЕ прямое преобразование из markdown в DOCX.
            html_content = markdown.markdown(content)

            ## Записываем этот промежуточный HTML в файл
            #html_file_path = artifact_file_path.replace(".docx", ".html")
            #with open(html_file_path, 'w', encoding="utf-8") as f:
            #    f.write(html_content)

            # Затем преобразуем в DOCX
            pypandoc.convert_text(html_content, 'docx', format='html', outputfile=artifact_file_path)
        except Exception as e:
            logger.error(f"Ошибка при экспорте в DOCX файл {artifact_file_path}: {e}", exc_info=True)

    ###########################################################
    # IO
    ###########################################################

    def _compose_filepath(self, artifact_data: Union[dict, str], artifact_name: str, content_type: str, target_format: str = None, verbose: bool = False) -> str:
        """
        Составляет путь к файлу для экспорта артефакта.

        :param artifact_data: Данные для экспорта.
        :type artifact_data: Union[dict, str]
        :param artifact_name: Имя артефакта.
        :type artifact_name: str
        :param content_type: Тип контента внутри артефакта.
        :type content_type: str
        :param target_format: Формат экспорта артефакта (например, json, txt, docx и т.д.).
        :type target_format: str, optional
        :param verbose: Выводить ли отладочные сообщения.
        :type verbose: bool, optional
        :return: Путь к файлу.
        :rtype: str
        """
        # Определение расширения:
        #
        # - Если указан формат содержимого, используем его как часть расширения.
        # - Если artificat_data - это dict, добавляем .json к расширению. Обратите внимание, что если бы был указан формат содержимого, мы бы получили <content_format>.json.
        # - Если artifact_data - это строка и формат содержимого не указан, добавляем .txt к расширению.
        extension = None
        if target_format is not None:
            extension = f"{target_format}"
        elif isinstance(artifact_data, str) and target_format is None:
            extension = "txt"

        # Определение типа контента
        if content_type is None:
            subfolder = ""
        else:
            subfolder = content_type

        # Сохраняем в указанное имя файла или путь, учитывая базовую выходную папку.
        artifact_file_path = os.path.join(self.base_output_folder, subfolder, f"{artifact_name}.{extension}")

        # Создаем промежуточные каталоги, если необходимо
        os.makedirs(os.path.dirname(artifact_file_path), exist_ok=True)

        return artifact_file_path


class Normalizer:
    """
    Механизм для нормализации фрагментов текста, концепций и других текстовых элементов.

    :ivar elements: Список элементов для нормализации.
    :vartype elements: List[str]
    :ivar n: Количество нормализованных элементов для вывода.
    :vartype n: int
    :ivar verbose: Выводить ли отладочные сообщения.
    :vartype verbose: bool
    :ivar normalized_elements: JSON-структура, где каждый выходной элемент является ключом к списку входных элементов, объединенных в него.
    :vartype normalized_elements: dict
    :ivar normalizing_map: Словарь, который сопоставляет каждый входной элемент с его нормализованным выводом.
    :vartype normalizing_map: dict
    """
    def __init__(self, elements: List[str], n: int, verbose: bool = False):
        """
        Инициализирует Normalizer.

        :param elements: Элементы для нормализации.
        :type elements: list
        :param n: Количество нормализованных элементов для вывода.
        :type n: int
        :param verbose: Выводить ли отладочные сообщения.
        :type verbose: bool, optional
        """
        # Убедимся, что элементы уникальны
        self.elements = list(set(elements))

        self.n = n
        self.verbose = verbose

        # JSON-структура, где каждый выходной элемент является ключом к списку входных элементов, объединенных в него
        self.normalized_elements = None
        # Словарь, сопоставляющий каждый входной элемент с его нормализованным выводом. Это будет использоваться в качестве кэша позже.
        self.normalizing_map = {}

        rendering_configs = {"n": n,
                             "elements": self.elements}

        messages = utils.compose_initial_LLM_messages_with_templates("normalizer.system.mustache", "normalizer.user.mustache", rendering_configs)
        next_message = openai_utils.client().send_message(messages, temperature=0.1)

        debug_msg = f"Normalization result message: {next_message}"
        logger.debug(debug_msg)
        if self.verbose:
            print(debug_msg)

        result = utils.extract_json(next_message["content"])
        logger.debug(result)
        if self.verbose:
            print(result)

        self.normalized_elements = result

    def normalize(self, element_or_elements: Union[str, List[str]]) -> Union[str, List[str]]:
        """
        Нормализует указанный элемент или элементы.

        Этот метод использует механизм кэширования для повышения производительности. Если элемент был нормализован ранее,
        его нормализованная форма сохраняется в кэше (self.normalizing_map). Когда один и тот же элемент необходимо
        нормализовать снова, метод сначала проверит кэш и использует сохраненную нормализованную форму, если она доступна,
        вместо того, чтобы нормализовать элемент снова.

        Порядок элементов на выходе будет таким же, как и на входе. Это обеспечивается путем обработки элементов в том порядке,
        в котором они появляются на входе, и добавления нормализованных элементов в выходной список в том же порядке.

        :param element_or_elements: Элемент или элементы для нормализации.
        :type element_or_elements: Union[str, List[str]]
        :return: Нормализованный элемент, если вход был строкой, или список нормализованных элементов, если вход был списком.
        :rtype: Union[str, List[str]]
        :raises ValueError: Если element_or_elements не является строкой или списком.
        """
        if isinstance(element_or_elements, str):
            denormalized_elements = [element_or_elements]
        elif isinstance(element_or_elements, list):
            denormalized_elements = element_or_elements
        else:
            raise ValueError("The element_or_elements must be either a string or a list.")

        normalized_elements = []
        elements_to_normalize = []
        for element in denormalized_elements:
            if element not in self.normalizing_map:
                elements_to_normalize.append(element)

        if elements_to_normalize:
            rendering_configs = {"categories": self.normalized_elements,
                                    "elements": elements_to_normalize}

            messages = utils.compose_initial_LLM_messages_with_templates("normalizer.applier.system.mustache", "normalizer.applier.user.mustache", rendering_configs)
            next_message = openai_utils.client().send_message(messages, temperature=0.1)

            debug_msg = f"Normalization result message: {next_message}"
            logger.debug(debug_msg)
            if self.verbose:
                print(debug_msg)

            normalized_elements_from_llm = utils.extract_json(next_message["content"])
            assert isinstance(normalized_elements_from_llm, list), "The normalized element must be a list."
            assert len(normalized_elements_from_llm) == len(elements_to_normalize), "The number of normalized elements must be equal to the number of elements to normalize."

            for i, element in enumerate(elements_to_normalize):
                normalized_element = normalized_elements_from_llm[i]
                self.normalizing_map[element] = normalized_element

        for element in denormalized_elements:
            normalized_elements.append(self.normalizing_map[element])

        return normalized_elements

################################################################################
# Вспомогательные механизмы
################################################################################

# Стандартный извлекатель
default_extractor = ResultsExtractor()