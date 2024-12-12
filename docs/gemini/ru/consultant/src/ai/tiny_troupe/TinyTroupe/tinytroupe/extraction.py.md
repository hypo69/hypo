# Анализ кода модуля `extraction.py`

**Качество кода**

- **Соответствие требованиям по оформлению кода**: 8/10
    - **Плюсы**:
        - Код в целом хорошо структурирован и читаем.
        - Используются docstring для описания функций и классов.
        - Присутствует логирование.
        - Используется `chevron` для работы с шаблонами.
        - Есть кэширование результатов извлечения.
    - **Минусы**:
        -  Не все комментарии и docstring соответствуют формату RST.
        -  Используется `json.dump` вместо `j_loads` или `j_loads_ns`.
        -  Иногда излишнее использование `try-except`, хотя есть logger.error.
        -  Не везде используются `logger.debug`, где это уместно.
        -  Импорты не все отсортированы по алфавиту.

**Рекомендации по улучшению**

1.  **Формат документации**:
    -   Переписать все комментарии и docstring в формате reStructuredText (RST).
    -   Использовать правильное оформление docstring для Sphinx (например, `:param`, `:return`).
2.  **Обработка данных**:
    -   Заменить `json.dump` на `j_loads` или `j_loads_ns` из `src.utils.jjson`, где это необходимо.
3.  **Логирование**:
    -   Использовать `logger.error` для обработки исключений вместо общих `try-except` блоков.
    -   Добавить `logger.debug` в начале и в конце функций для отслеживания их выполнения.
4.  **Импорты**:
    -   Отсортировать импорты по алфавиту.
    -   Проверить и добавить недостающие импорты, если такие имеются.
5.  **Рефакторинг**:
    -   Убрать дублирование кода (например, в `extract_results_from_agent` и `extract_results_from_world`).
    -   Улучшить читаемость кода, разделив сложные функции на более мелкие.
6.  **Комментарии**:
    -   Добавить комментарии, объясняющие сложные участки кода.
    -   Избегать в комментариях слов вроде "получаем", "делаем".

**Оптимизированный код**
```python
"""
Модуль для извлечения данных из TinyTroupe
=========================================================================================

Этот модуль предоставляет утилиты для извлечения данных из элементов TinyTroupe,
таких как агенты и миры. Он также предоставляет механизм для сокращения извлеченных данных
до более краткой формы и для экспорта артефактов из элементов TinyTroupe.

Пример использования
--------------------

Пример использования класса `ResultsExtractor`:

.. code-block:: python

    extractor = ResultsExtractor()
    agent = TinyPerson(name='Alice')
    results = extractor.extract_results_from_agent(agent, extraction_objective='Summary of interactions')
"""

import os
import logging
import chevron
import pandas as pd
import pypandoc
import markdown
from typing import Union, List, Dict, Any
#from typing import Any # TODO: check if this is still needed after deleting this import on the top of the file
from src.utils.jjson import j_loads
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
from tinytroupe.utils import JsonSerializableRegistry

from tinytroupe import openai_utils
import tinytroupe.utils as utils

from src.logger.logger import logger

class ResultsExtractor:
    """
    Класс для извлечения результатов из TinyTroupe.

    Этот класс предоставляет методы для извлечения данных из агентов и миров,
    а также для сохранения результатов в формате JSON.
    """

    def __init__(self):
        """
        Инициализирует ResultsExtractor.

        Устанавливает путь к шаблону для извлечения и кэширует результаты извлечения.
        """
        self._extraction_prompt_template_path = os.path.join(os.path.dirname(__file__), 'prompts/interaction_results_extractor.mustache')
        # Кэширование последних результатов извлечения для каждого типа извлечения
        self.agent_extraction = {}
        self.world_extraction = {}

    def _compose_messages(self,
                         tinytroupe_object: Union[TinyPerson, TinyWorld],
                         extraction_objective: str,
                         situation: str,
                         fields: List[str] = None,
                         fields_hints: Dict[str, str] = None) -> List[Dict[str, str]]:
        """
        Составляет сообщения для отправки в LLM.

        :param tinytroupe_object: Объект TinyPerson или TinyWorld.
        :param extraction_objective: Цель извлечения.
        :param situation: Описание ситуации.
        :param fields: Список полей для извлечения.
        :param fields_hints: Словарь с подсказками для полей.
        :return: Список сообщений.
        """
        logger.debug(f"Начало составления сообщения для объекта: {tinytroupe_object}")
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

        if isinstance(tinytroupe_object, TinyPerson):
            interaction_history = tinytroupe_object.pretty_current_interactions(max_content_length=None)
            extraction_request_prompt = f"""
            ## Extraction objective

            {extraction_objective}

            ## Situation
            You are considering a single agent, named {tinytroupe_object.name}. Your objective thus refers to this agent specifically.
            {situation}

            ## Agent Interactions History

            You will consider an agent's history of interactions, which include stimuli it received as well as actions it 
            performed.

            {interaction_history}
            """
        elif isinstance(tinytroupe_object, TinyWorld):
            interaction_history = tinytroupe_object.pretty_current_interactions(max_content_length=None)
            extraction_request_prompt = f"""
            ## Extraction objective

            {extraction_objective}

            ## Situation
            You are considering various agents.
            {situation}

            ## Agents Interactions History

            You will consider the history of interactions from various agents that exist in an environment called {tinytroupe_object.name}. 
            Each interaction history includes stimuli the corresponding agent received as well as actions it performed.

            {interaction_history}
            """
        else:
            raise ValueError(f"Unsupported object type: {type(tinytroupe_object)}")

        messages.append({"role": "user", "content": extraction_request_prompt})
        logger.debug(f"Сообщения составлены для объекта: {tinytroupe_object}")
        return messages


    def _extract_and_cache(self,
                          tinytroupe_object: Union[TinyPerson, TinyWorld],
                          messages: List[Dict[str, str]],
                          verbose: bool) -> Any:
        """
        Отправляет сообщения в LLM, извлекает и кэширует результаты.

        :param tinytroupe_object: Объект TinyPerson или TinyWorld.
        :param messages: Список сообщений для отправки.
        :param verbose: Флаг для вывода отладочной информации.
        :return: Извлеченные результаты.
        """
        logger.debug(f"Начало извлечения и кэширования для объекта: {tinytroupe_object}")
        next_message = openai_utils.client().send_message(messages, temperature=0.0)

        debug_msg = f"Extraction raw result message: {next_message}"
        logger.debug(debug_msg)
        if verbose:
            print(debug_msg)

        if next_message is not None:
            result = utils.extract_json(next_message["content"])
        else:
            result = None

        if isinstance(tinytroupe_object, TinyPerson):
            self.agent_extraction[tinytroupe_object.name] = result
        elif isinstance(tinytroupe_object, TinyWorld):
            self.world_extraction[tinytroupe_object.name] = result

        logger.debug(f"Завершено извлечение и кэширование для объекта: {tinytroupe_object}, результат: {result}")
        return result



    def extract_results_from_agent(self,
                                   tinyperson: TinyPerson,
                                   extraction_objective: str = "The main points present in the agent's interactions history.",
                                   situation: str = "",
                                   fields: list = None,
                                   fields_hints: dict = None,
                                   verbose: bool = False) -> Any:
        """
        Извлекает результаты из экземпляра TinyPerson.

        :param tinyperson: Экземпляр TinyPerson.
        :param extraction_objective: Цель извлечения.
        :param situation: Описание ситуации.
        :param fields: Список полей для извлечения.
        :param fields_hints: Словарь с подсказками для полей.
        :param verbose: Флаг для вывода отладочной информации.
        :return: Извлеченные результаты.
        """
        logger.debug(f"Начало извлечения результатов из агента: {tinyperson.name}")
        messages = self._compose_messages(tinyperson, extraction_objective, situation, fields, fields_hints)
        result = self._extract_and_cache(tinyperson, messages, verbose)
        logger.debug(f"Завершено извлечение результатов из агента: {tinyperson.name}, результат: {result}")
        return result


    def extract_results_from_world(self,
                                   tinyworld: TinyWorld,
                                   extraction_objective: str = "The main points that can be derived from the agents conversations and actions.",
                                   situation: str = "",
                                   fields: list = None,
                                   fields_hints: dict = None,
                                   verbose: bool = False) -> Any:
        """
        Извлекает результаты из экземпляра TinyWorld.

        :param tinyworld: Экземпляр TinyWorld.
        :param extraction_objective: Цель извлечения.
        :param situation: Описание ситуации.
        :param fields: Список полей для извлечения.
        :param fields_hints: Словарь с подсказками для полей.
        :param verbose: Флаг для вывода отладочной информации.
        :return: Извлеченные результаты.
        """
        logger.debug(f"Начало извлечения результатов из мира: {tinyworld.name}")
        messages = self._compose_messages(tinyworld, extraction_objective, situation, fields, fields_hints)
        result = self._extract_and_cache(tinyworld, messages, verbose)
        logger.debug(f"Завершено извлечение результатов из мира: {tinyworld.name}, результат: {result}")
        return result


    def save_as_json(self, filename: str, verbose: bool = False):
        """
        Сохраняет последние результаты извлечения в формате JSON.

        :param filename: Имя файла для сохранения JSON.
        :param verbose: Флаг для вывода отладочной информации.
        """
        logger.debug(f"Начало сохранения результатов в JSON: {filename}")
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump({"agent_extractions": self.agent_extraction,
                           "world_extraction": self.world_extraction}, f, indent=4)

            if verbose:
                print(f"Saved extraction results to {filename}")
            logger.debug(f"Успешно сохранены результаты в JSON: {filename}")
        except Exception as e:
            logger.error(f"Ошибка при сохранении в JSON: {filename}", exc_info=True)
            ...


class ResultsReducer:
    """
    Класс для сокращения результатов.

    Этот класс предоставляет методы для сокращения данных из агентов на основе заданных правил.
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
        :param func: Функция для применения правила.
        """
        if trigger in self.rules:
            raise Exception(f"Rule for {trigger} already exists.")

        self.rules[trigger] = func

    def reduce_agent(self, agent: TinyPerson) -> list:
        """
        Сокращает результаты агента на основе заданных правил.

        :param agent: Экземпляр TinyPerson.
        :return: Список сокращенных данных.
        """
        reduction = []
        for message in agent.episodic_memory.retrieve_all():
            if message['role'] == 'system':
                continue  # пропускаем `system` role

            elif message['role'] == 'user':
                # User role is related to stimuli only
                stimulus_type = message['content']['stimuli'][0]['type']
                stimulus_content = message['content']['stimuli'][0]['content']
                stimulus_source = message['content']['stimuli'][0]['source']
                stimulus_timestamp = message['simulation_timestamp']

                if stimulus_type in self.rules:
                    extracted = self.rules[stimulus_type](focus_agent=agent,
                                                          source_agent=TinyPerson.get_agent_by_name(stimulus_source),
                                                          target_agent=agent, kind='stimulus', event=stimulus_type,
                                                          content=stimulus_content, timestamp=stimulus_timestamp)
                    if extracted is not None:
                        reduction.append(extracted)

            elif message['role'] == 'assistant':
                # Assistant role is related to actions only
                if 'action' in message['content']:
                    action_type = message['content']['action']['type']
                    action_content = message['content']['action']['content']
                    action_target = message['content']['action']['target']
                    action_timestamp = message['simulation_timestamp']

                    if action_type in self.rules:
                        extracted = self.rules[action_type](focus_agent=agent, source_agent=agent,
                                                          target_agent=TinyPerson.get_agent_by_name(action_target),
                                                          kind='action', event=action_type, content=action_content,
                                                          timestamp=action_timestamp)
                        if extracted is not None:
                            reduction.append(extracted)

        return reduction

    def reduce_agent_to_dataframe(self, agent: TinyPerson, column_names: list = None) -> pd.DataFrame:
        """
        Сокращает результаты агента до DataFrame.

        :param agent: Экземпляр TinyPerson.
        :param column_names: Список названий столбцов.
        :return: DataFrame с сокращенными данными.
        """
        reduction = self.reduce_agent(agent)
        return pd.DataFrame(reduction, columns=column_names)


class ArtifactExporter(JsonSerializableRegistry):
    """
    Класс для экспорта артефактов из TinyTroupe.

    Этот класс предоставляет методы для экспорта данных в различные форматы,
    такие как JSON, TXT, DOCX.
    """

    def __init__(self, base_output_folder: str) -> None:
        """
        Инициализирует ArtifactExporter.

        :param base_output_folder: Базовая папка для вывода.
        """
        self.base_output_folder = base_output_folder

    def export(self, artifact_name: str, artifact_data: Union[dict, str], content_type: str,
               content_format: str = None, target_format: str = "txt", verbose: bool = False):
        """
        Экспортирует указанные данные артефакта в файл.

        :param artifact_name: Имя артефакта.
        :param artifact_data: Данные для экспорта.
        :param content_type: Тип содержимого артефакта.
        :param content_format: Формат содержимого артефакта.
        :param target_format: Формат экспорта артефакта.
        :param verbose: Флаг для вывода отладочной информации.
        """
        logger.debug(f"Начало экспорта артефакта: {artifact_name}")
        # удаляет отступы
        if isinstance(artifact_data, str):
            artifact_data = utils.dedent(artifact_data)
        elif isinstance(artifact_data, dict):
            if 'content' in artifact_data:
                artifact_data['content'] = utils.dedent(artifact_data['content'])
            else:
                logger.warning(f"Ключ 'content' не найден в данных артефакта: {artifact_name}")
        else:
            logger.error(f"Недопустимый тип данных артефакта: {type(artifact_data)}. Ожидается строка или словарь.")
            raise ValueError("The artifact data must be either a string or a dictionary.")


        # очищает имя артефакта от недопустимых символов
        invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '\n', '\t', '\r', ';']
        for char in invalid_chars:
            if char in artifact_name:
                artifact_name = artifact_name.replace(char, "-")
                logger.warning(f"Заменен недопустимый символ {char} дефисом в имени артефакта: '{artifact_name}'.")

        artifact_file_path = self._compose_filepath(artifact_data, artifact_name, content_type, target_format,
                                                    verbose)

        if target_format == "json":
            self._export_as_json(artifact_file_path, artifact_data, content_type, verbose)
        elif target_format in ["txt", "text", "md", "markdown"]:
            self._export_as_txt(artifact_file_path, artifact_data, content_type, verbose)
        elif target_format == "docx":
            self._export_as_docx(artifact_file_path, artifact_data, content_format, verbose)
        else:
            logger.error(f"Неподдерживаемый формат экспорта: {target_format}")
            raise ValueError(f"Unsupported target format: {target_format}.")
        logger.debug(f"Завершено экспорта артефакта: {artifact_name} в {artifact_file_path}")


    def _export_as_txt(self, artifact_file_path: str, artifact_data: Union[dict, str], content_type: str,
                       verbose: bool = False):
        """
        Экспортирует данные артефакта в текстовый файл.

        :param artifact_file_path: Путь к файлу для сохранения.
        :param artifact_data: Данные для экспорта.
        :param content_type: Тип содержимого артефакта.
        :param verbose: Флаг для вывода отладочной информации.
        """
        logger.debug(f"Начало экспорта в TXT: {artifact_file_path}")
        try:
            with open(artifact_file_path, 'w', encoding="utf-8") as f:
                if isinstance(artifact_data, dict):
                    content = artifact_data.get('content', '')
                else:
                    content = artifact_data
                f.write(content)
            logger.debug(f"Успешно экспортирован в TXT: {artifact_file_path}")
        except Exception as e:
            logger.error(f"Ошибка при экспорте в TXT: {artifact_file_path}", exc_info=True)
            ...


    def _export_as_json(self, artifact_file_path: str, artifact_data: Union[dict, str], content_type: str,
                        verbose: bool = False):
        """
        Экспортирует данные артефакта в JSON файл.

        :param artifact_file_path: Путь к файлу для сохранения.
        :param artifact_data: Данные для экспорта.
        :param content_type: Тип содержимого артефакта.
        :param verbose: Флаг для вывода отладочной информации.
        """
        logger.debug(f"Начало экспорта в JSON: {artifact_file_path}")
        try:
            with open(artifact_file_path, 'w', encoding="utf-8") as f:
                if isinstance(artifact_data, dict):
                    json.dump(artifact_data, f, indent=4)
                else:
                    logger.error("Данные артефакта должны быть словарем для экспорта в JSON.")
                    raise ValueError("The artifact data must be a dictionary to export to JSON.")
            logger.debug(f"Успешно экспортирован в JSON: {artifact_file_path}")
        except Exception as e:
            logger.error(f"Ошибка при экспорте в JSON: {artifact_file_path}", exc_info=True)
            ...


    def _export_as_docx(self, artifact_file_path: str, artifact_data: Union[dict, str], content_original_format: str,
                        verbose: bool = False):
        """
        Экспортирует данные артефакта в DOCX файл.

        :param artifact_file_path: Путь к файлу для сохранения.
        :param artifact_data: Данные для экспорта.
        :param content_original_format: Формат исходного содержимого.
        :param verbose: Флаг для вывода отладочной информации.
        """
        logger.debug(f"Начало экспорта в DOCX: {artifact_file_path}")
        if content_original_format not in ['text', 'txt', 'markdown', 'md']:
            logger.error(f"Недопустимый исходный формат: {content_original_format} для экспорта в DOCX.")
            raise ValueError(f"The original format cannot be {content_original_format} to export to DOCX.")
        else:
            content_original_format = 'markdown' if content_original_format == 'md' else content_original_format
        try:
            if isinstance(artifact_data, dict):
                content = artifact_data.get('content', '')
            else:
                content = artifact_data
            html_content = markdown.markdown(content)
            pypandoc.convert_text(html_content, 'docx', format='html', outputfile=artifact_file_path)
            logger.debug(f"Успешно экспортирован в DOCX: {artifact_file_path}")
        except Exception as e:
            logger.error(f"Ошибка при экспорте в DOCX: {artifact_file_path}", exc_info=True)
            ...


    def _compose_filepath(self, artifact_data: Union[dict, str], artifact_name: str, content_type: str,
                          target_format: str = None, verbose: bool = False) -> str:
        """
        Составляет путь к файлу для экспорта артефакта.

        :param artifact_data: Данные для экспорта.
        :param artifact_name: Имя артефакта.
        :param content_type: Тип содержимого артефакта.
        :param target_format: Формат экспорта артефакта.
        :param verbose: Флаг для вывода отладочной информации.
        :return: Путь к файлу.
        """
        logger.debug(f"Составление пути к файлу для артефакта: {artifact_name}")
        extension = None
        if target_format is not None:
            extension = f"{target_format}"
        elif isinstance(artifact_data, str) and target_format is None:
            extension = "txt"

        if content_type is None:
            subfolder = ""
        else:
            subfolder = content_type

        artifact_file_path = os.path.join(self.base_output_folder, subfolder, f"{artifact_name}.{extension}")
        os.makedirs(os.path.dirname(artifact_file_path), exist_ok=True)
        logger.debug(f"Путь к файлу для артефакта: {artifact_file_path}")
        return artifact_file_path


class Normalizer:
    """
    Класс для нормализации текстовых элементов.

    Предоставляет механизм для нормализации фрагментов текста, концепций и других текстовых элементов.
    """
    def __init__(self, elements: List[str], n: int, verbose: bool = False):
        """
        Инициализирует Normalizer.

        :param elements: Список элементов для нормализации.
        :param n: Количество нормализованных элементов для вывода.
        :param verbose: Флаг для вывода отладочной информации.
        """
        self.elements = list(set(elements))
        self.n = n
        self.verbose = verbose
        self.normalized_elements = None
        self.normalizing_map = {}

        rendering_configs = {"n": n,
                             "elements": self.elements}
        messages = utils.compose_initial_LLM_messages_with_templates("normalizer.system.mustache",
                                                                       "normalizer.user.mustache",
                                                                       rendering_configs)
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

        Использует кэширование для повышения производительности. Если элемент был нормализован ранее,
        его нормализованная форма берется из кэша.

        :param element_or_elements: Элемент или список элементов для нормализации.
        :return: Нормализованный элемент или список элементов.
        """
        if isinstance(element_or_elements, str):
            denormalized_elements = [element_or_elements]
        elif isinstance(element_or_elements, list):
            denormalized_elements = element_or_elements
        else:
            logger.error("element_or_elements должен быть строкой или списком.")
            raise ValueError("The element_or_elements must be either a string or a list.")

        normalized_elements = []
        elements_to_normalize = []
        for element in denormalized_elements:
            if element not in self.normalizing_map:
                elements_to_normalize.append(element)

        if elements_to_normalize:
            rendering_configs = {"categories": self.normalized_elements,
                                    "elements": elements_to_normalize}

            messages = utils.compose_initial_LLM_messages_with_templates("normalizer.applier.system.mustache",
                                                                           "normalizer.applier.user.mustache",
                                                                           rendering_configs)
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
# Convenience mechanisms
################################################################################

# default extractor
default_extractor = ResultsExtractor()