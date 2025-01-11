# Анализ кода модуля `extraction.py`

**Качество кода: 7/10**

- **Плюсы:**
    - Код имеет модульную структуру, разделенную на классы `ResultsExtractor`, `ResultsReducer`, `ArtifactExporter` и `Normalizer`, что способствует лучшей организации и читаемости.
    - Используется `logger` для отладки и обработки ошибок.
    - Применяется шаблонизация с использованием библиотеки `chevron` для генерации промптов.
    -  Присутствует кэширование результатов извлечения.
    -  Есть механизмы для преобразования данных в различные форматы (JSON, TXT, DOCX).
    -  Реализована нормализация текста с использованием LLM.
    - Документация для класса присутствует.
- **Минусы:**
    -  Не все функции и методы имеют docstring.
    -  Используется `json.dump` вместо `j_loads` или `j_loads_ns`.
    -  Не всегда используются одинарные кавычки в коде, как указано в инструкции.
    -  Много где не используется `from src.logger.logger import logger`
    -  Не везде есть обработка ошибок с помощью `logger.error`.
    - В некоторых местах используется `print` вместо `logger.debug`.

**Рекомендации по улучшению:**

1.  **Документация:** Добавить docstring ко всем функциям, методам и переменным. Использовать формат RST.
2.  **Импорты:** Использовать `from src.logger.logger import logger` для импорта `logger`.
3.  **Обработка ошибок:** Заменить блоки `try-except` на использование `logger.error` для логирования ошибок.
4.  **Формат кода:** Привести все строки к использованию одинарных кавычек, за исключением операций вывода.
5.  **JSON:** Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо `json.dump`.
6.  **Логирование:** Заменить `print` на `logger.debug` для отладочных сообщений.
7.  **Улучшить форматирование:** Привести в соответствие код с ранее обработанными файлами
8.  **Улучшение производительности:** Рассмотреть возможность использования асинхронности для операций ввода/вывода, чтобы улучшить общую производительность.

**Оптимизированный код**

```python
"""
Simulations produce a lot of data, and it is often useful to extract these data in a structured way. For instance, you might wish to:
  - Extract the main points from an agent's interactions history, so that you can consult them later in a concise form.
  - Generate synthetic data from a simulation, so that you can use it for training machine learning models or testing software.
  - Simply turn some of the data into a more machine-readable format, such as JSON or CSV, so that you can analyze it more easily.

This module provides various utilities to help you extract data from TinyTroupe elements, such as agents and worlds. It also provides a 
mechanism to reduce the extracted data to a more concise form, and to export artifacts from TinyTroupe elements. Incidentaly, it showcases 
one of the many ways in which agent simulations differ from AI assistants, as the latter are not designed to be introspected in this way.
"""

import os
import json
import chevron
# from typing import Union, List # исправлено
import pandas as pd
import pypandoc
import markdown
from typing import Union, List
from src.logger.logger import logger # изменено
from pathlib import Path # добавлено
from src.utils.jjson import j_loads # добавлено

from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
from tinytroupe.factory import TinyPersonFactory
from tinytroupe.utils import JsonSerializableRegistry


from tinytroupe import openai_utils
import tinytroupe.utils as utils

class ResultsExtractor:
    """
    Класс для извлечения результатов из TinyTroupe элементов, таких как агенты и миры.

    Предоставляет методы для извлечения данных из объектов TinyPerson и TinyWorld,
    а также для сохранения результатов в формате JSON.

    Attributes:
        _extraction_prompt_template_path (str): Путь к файлу шаблона для промптов извлечения.
        agent_extraction (dict): Словарь для хранения последних извлеченных результатов для агентов.
        world_extraction (dict): Словарь для хранения последних извлеченных результатов для миров.
    """
    def __init__(self):
        """
        Инициализирует ResultsExtractor.

        Устанавливает путь к шаблону промптов и создает словари для кэширования результатов извлечения.
        """
        self._extraction_prompt_template_path = os.path.join(os.path.dirname(__file__), 'prompts/interaction_results_extractor.mustache')
        # кэшируем результаты последнего извлечения для каждого типа извлечения
        # чтобы их можно было использовать для генерации отчетов или других дополнительных результатов.
        self.agent_extraction = {}
        self.world_extraction = {}

    def extract_results_from_agent(self,
                        tinyperson:TinyPerson,
                        extraction_objective:str="The main points present in the agent's interactions history.",
                        situation:str = "",
                        fields:list=None,
                        fields_hints:dict=None,
                        verbose:bool=False):
        """
        Извлекает результаты из экземпляра TinyPerson.

        Args:
            tinyperson (TinyPerson): Экземпляр TinyPerson, из которого извлекаются результаты.
            extraction_objective (str): Цель извлечения.
            situation (str): Ситуация, которую нужно учитывать.
            fields (list, optional): Поля для извлечения. Если None, извлекатель решит, какие имена использовать. По умолчанию None.
            fields_hints (dict, optional): Словарь с подсказками для полей. По умолчанию None.
            verbose (bool, optional): Флаг для вывода отладочных сообщений. По умолчанию False.

        Returns:
            dict: Результаты извлечения или None в случае ошибки.
        """
        messages = []
        rendering_configs = {}
        if fields is not None:
            rendering_configs['fields'] = ', '.join(fields)

        if fields_hints is not None:
            rendering_configs['fields_hints'] = list(fields_hints.items())
        messages.append({'role': 'system',
                         'content': chevron.render(
                             open(self._extraction_prompt_template_path).read(),
                             rendering_configs)})
        interaction_history = tinyperson.pretty_current_interactions(max_content_length=None)
        extraction_request_prompt = f"""
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
        messages.append({'role': 'user', 'content': extraction_request_prompt})
        next_message = openai_utils.client().send_message(messages, temperature=0.0)

        debug_msg = f'Extraction raw result message: {next_message}'
        logger.debug(debug_msg)
        if verbose:
            print(debug_msg)

        if next_message is not None:
            result = utils.extract_json(next_message['content'])
        else:
            result = None
        # кэшируем результат
        self.agent_extraction[tinyperson.name] = result
        return result

    def extract_results_from_world(self,
                                   tinyworld:TinyWorld,
                                   extraction_objective:str="The main points that can be derived from the agents conversations and actions.",
                                   situation:str="",
                                   fields:list=None,
                                   fields_hints:dict=None,
                                   verbose:bool=False):
        """
        Извлекает результаты из экземпляра TinyWorld.

        Args:
            tinyworld (TinyWorld): Экземпляр TinyWorld, из которого извлекаются результаты.
            extraction_objective (str): Цель извлечения.
            situation (str): Ситуация, которую нужно учитывать.
            fields (list, optional): Поля для извлечения. Если None, извлекатель решит, какие имена использовать. По умолчанию None.
            fields_hints (dict, optional): Словарь с подсказками для полей. По умолчанию None.
            verbose (bool, optional): Флаг для вывода отладочных сообщений. По умолчанию False.

        Returns:
            dict: Результаты извлечения или None в случае ошибки.
        """
        messages = []
        rendering_configs = {}
        if fields is not None:
            rendering_configs['fields'] = ', '.join(fields)
        if fields_hints is not None:
            rendering_configs['fields_hints'] = list(fields_hints.items())

        messages.append({'role': 'system',
                         'content': chevron.render(
                             open(self._extraction_prompt_template_path).read(),
                             rendering_configs)})

        # TODO: либо сначала суммировать, либо разбить на несколько задач
        interaction_history = tinyworld.pretty_current_interactions(max_content_length=None)
        extraction_request_prompt = f"""
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
        messages.append({'role': 'user', 'content': extraction_request_prompt})
        next_message = openai_utils.client().send_message(messages, temperature=0.0)

        debug_msg = f'Extraction raw result message: {next_message}'
        logger.debug(debug_msg)
        if verbose:
            print(debug_msg)

        if next_message is not None:
            result = utils.extract_json(next_message['content'])
        else:
            result = None
        # кэшируем результат
        self.world_extraction[tinyworld.name] = result
        return result

    def save_as_json(self, filename:str, verbose:bool=False):
        """
        Сохраняет последние извлеченные результаты в формате JSON.

        Args:
            filename (str): Имя файла для сохранения JSON.
            verbose (bool, optional): Флаг для вывода отладочных сообщений. По умолчанию False.
        """
        try: # добавлено
            with open(filename, 'w') as f: # изменено
                json.dump({'agent_extractions': self.agent_extraction,
                           'world_extraction': self.world_extraction}, f, indent=4)

            if verbose:
                print(f'Saved extraction results to {filename}')
        except Exception as ex: # добавлено
                logger.error(f'Error saving extraction results to {filename}', ex) # добавлено

class ResultsReducer:
    """
    Класс для сокращения результатов на основе заданных правил.

    Attributes:
        results (dict): Словарь для хранения результатов.
        rules (dict): Словарь для хранения правил сокращения.
    """
    def __init__(self):
        """
        Инициализирует ResultsReducer.

        Создает словари для хранения результатов и правил сокращения.
        """
        self.results = {}
        self.rules = {}

    def add_reduction_rule(self, trigger: str, func: callable):
        """
        Добавляет правило сокращения.

        Args:
            trigger (str): Триггер, при котором применяется правило.
            func (callable): Функция, выполняющая сокращение.

        Raises:
            Exception: Если правило для данного триггера уже существует.
        """
        if trigger in self.rules:
            raise Exception(f'Rule for {trigger} already exists.')
        self.rules[trigger] = func

    def reduce_agent(self, agent: TinyPerson) -> list:
        """
        Сокращает результаты для агента.

        Args:
            agent (TinyPerson): Экземпляр TinyPerson, результаты которого нужно сократить.

        Returns:
            list: Список сокращенных результатов.
        """
        reduction = []
        for message in agent.episodic_memory.retrieve_all():
            if message['role'] == 'system':
                continue # пока ничего не делаем для роли system
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

    def reduce_agent_to_dataframe(self, agent: TinyPerson, column_names: list=None) -> pd.DataFrame:
        """
        Сокращает результаты агента до DataFrame.

        Args:
            agent (TinyPerson): Экземпляр TinyPerson, результаты которого нужно сократить.
            column_names (list, optional): Имена столбцов DataFrame. По умолчанию None.

        Returns:
            pd.DataFrame: DataFrame с сокращенными результатами.
        """
        reduction = self.reduce_agent(agent)
        return pd.DataFrame(reduction, columns=column_names)


class ArtifactExporter(JsonSerializableRegistry):
    """
    Экспортер артефактов из элементов TinyTroupe.

    Отвечает за экспорт артефактов из элементов TinyTroupe, например,
    для создания синтетических файлов данных из симуляций.
    """
    def __init__(self, base_output_folder:str) -> None:
        """
        Инициализирует ArtifactExporter.

        Args:
            base_output_folder (str): Базовая папка для вывода экспортированных артефактов.
        """
        self.base_output_folder = base_output_folder

    def export(self, artifact_name:str, artifact_data:Union[dict, str], content_type:str, content_format:str=None, target_format:str="txt", verbose:bool=False):
        """
        Экспортирует указанные данные артефакта в файл.

        Args:
            artifact_name (str): Имя артефакта.
            artifact_data (Union[dict, str]): Данные для экспорта. Если дан словарь, он будет сохранен как JSON.
                Если дана строка, она будет сохранена как есть.
            content_type (str): Тип содержимого внутри артефакта.
            content_format (str, optional): Формат содержимого внутри артефакта (например, md, csv и т.д.). По умолчанию None.
            target_format (str): Формат для экспорта артефакта (например, json, txt, docx и т.д.).
            verbose (bool, optional): Флаг для вывода отладочных сообщений. По умолчанию False.
        """
        # удаляем лишние отступы, на всякий случай
        if isinstance(artifact_data, str):
            artifact_data = utils.dedent(artifact_data)
        elif isinstance(artifact_data, dict):
            artifact_data['content'] = utils.dedent(artifact_data['content'])
        else:
            raise ValueError('The artifact data must be either a string or a dictionary.')
        # очищаем имя артефакта от недопустимых символов
        invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '\n', '\t', '\r', ';']
        for char in invalid_chars:
            # проверяем, есть ли символ в имени артефакта
            if char in artifact_name:
                # заменяем символ на дефис
                artifact_name = artifact_name.replace(char, '-')
                logger.warning(f'Replaced invalid character {char} with hyphen in artifact name \'{artifact_name}\'.')

        artifact_file_path = self._compose_filepath(artifact_data, artifact_name, content_type, target_format, verbose)
        if target_format == 'json':
            self._export_as_json(artifact_file_path, artifact_data, content_type, verbose)
        elif target_format == 'txt' or target_format == 'text' or target_format == 'md' or target_format == 'markdown':
            self._export_as_txt(artifact_file_path, artifact_data, content_type, verbose)
        elif target_format == 'docx':
            self._export_as_docx(artifact_file_path, artifact_data, content_format, verbose)
        else:
            raise ValueError(f'Unsupported target format: {target_format}.')

    def _export_as_txt(self, artifact_file_path:str, artifact_data:Union[dict, str], content_type:str, verbose:bool=False):
        """
        Экспортирует указанные данные артефакта в текстовый файл.

        Args:
            artifact_file_path (str): Путь к файлу для сохранения.
            artifact_data (Union[dict, str]): Данные для экспорта.
            content_type (str): Тип содержимого внутри артефакта.
            verbose (bool, optional): Флаг для вывода отладочных сообщений. По умолчанию False.
        """
        try:
            with open(artifact_file_path, 'w', encoding='utf-8') as f:
                if isinstance(artifact_data, dict):
                    content = artifact_data['content']
                else:
                    content = artifact_data

                f.write(content)
        except Exception as ex:
            logger.error(f'Error exporting artifact to {artifact_file_path}', ex)

    def _export_as_json(self, artifact_file_path:str, artifact_data:Union[dict, str], content_type:str, verbose:bool=False):
        """
        Экспортирует указанные данные артефакта в JSON-файл.

        Args:
            artifact_file_path (str): Путь к файлу для сохранения.
            artifact_data (Union[dict, str]): Данные для экспорта.
            content_type (str): Тип содержимого внутри артефакта.
            verbose (bool, optional): Флаг для вывода отладочных сообщений. По умолчанию False.
        """
        try:
            with open(artifact_file_path, 'w', encoding='utf-8') as f:
                if isinstance(artifact_data, dict):
                    json.dump(artifact_data, f, indent=4)
                else:
                    raise ValueError('The artifact data must be a dictionary to export to JSON.')
        except Exception as ex:
            logger.error(f'Error exporting artifact to {artifact_file_path}', ex)

    def _export_as_docx(self, artifact_file_path:str, artifact_data:Union[dict, str], content_original_format:str, verbose:bool=False):
        """
        Экспортирует указанные данные артефакта в DOCX-файл.

        Args:
            artifact_file_path (str): Путь к файлу для сохранения.
            artifact_data (Union[dict, str]): Данные для экспорта.
            content_original_format (str): Исходный формат содержимого (например, text, markdown).
            verbose (bool, optional): Флаг для вывода отладочных сообщений. По умолчанию False.
        """
        # исходный формат должен быть 'text' или 'markdown'
        if content_original_format not in ['text', 'txt', 'markdown', 'md']:
            raise ValueError(f'The original format cannot be {content_original_format} to export to DOCX.')
        else:
            # нормализуем значение контента
            content_original_format = 'markdown' if content_original_format == 'md' else content_original_format
        # сначала получаем контент для экспорта. Если `artifact_date` является словарем, константа должна быть под ключом `content`.
        # Если это строка, контент - это сама строка.
        # используем pypandoc
        if isinstance(artifact_data, dict):
            content = artifact_data['content']
        else:
            content = artifact_data

        # сначала конвертируем в HTML. Это необходимо, поскольку pypandoc не поддерживает ХОРОШУЮ прямую конвертацию из markdown в DOCX.
        html_content = markdown.markdown(content)

        ## записываем этот промежуточный HTML в файл
        #html_file_path = artifact_file_path.replace(".docx", ".html")
        #with open(html_file_path, 'w', encoding="utf-8") as f:
        #    f.write(html_content)

        # затем конвертируем в DOCX
        try:
          pypandoc.convert_text(html_content, 'docx', format='html', outputfile=artifact_file_path)
        except Exception as ex:
            logger.error(f'Error exporting artifact to {artifact_file_path}', ex)

    ###########################################################
    # IO
    ###########################################################

    def _compose_filepath(self, artifact_data:Union[dict, str], artifact_name:str, content_type:str, target_format:str=None, verbose:bool=False):
        """
        Составляет путь к файлу для экспортируемого артефакта.

        Args:
            artifact_data (Union[dict, str]): Данные для экспорта.
            artifact_name (str): Имя артефакта.
            content_type (str): Тип содержимого внутри артефакта.
            target_format (str, optional): Формат содержимого внутри артефакта (например, md, csv и т.д.). По умолчанию None.
            verbose (bool, optional): Флаг для вывода отладочных сообщений. По умолчанию False.
        """
        # Определение расширения:
        #
        # - Если указан формат содержимого, мы используем его как часть расширения.
        # - Если artificat_data является словарем, мы добавляем .json к расширению. Обратите внимание, что если бы формат содержимого был указан, мы бы получили <content_format>.json.
        # - Если artifact_data является строкой и формат содержимого не указан, мы добавляем .txt к расширению.
        extension = None
        if target_format is not None:
            extension = f'{target_format}'
        elif isinstance(artifact_data, str) and target_format is None:
            extension = 'txt'
        # определение типа контента
        if content_type is None:
            subfolder = ''
        else:
            subfolder = content_type
        # сохраняем в указанное имя файла или путь, учитывая базовую выходную папку.
        artifact_file_path = os.path.join(self.base_output_folder, subfolder, f'{artifact_name}.{extension}')
        # создаем промежуточные каталоги, если необходимо
        os.makedirs(os.path.dirname(artifact_file_path), exist_ok=True)
        return artifact_file_path


class Normalizer:
    """
    Механизм для нормализации отрывков, концепций и других текстовых элементов.
    """
    def __init__(self, elements:List[str], n:int, verbose:bool=False):
        """
        Инициализирует Normalizer.

        Args:
            elements (list): Элементы для нормализации.
            n (int): Количество нормализованных элементов для вывода.
            verbose (bool, optional): Флаг для вывода отладочных сообщений. По умолчанию False.
        """
        # убеждаемся, что элементы уникальны
        self.elements = list(set(elements))
        self.n = n
        self.verbose = verbose

        # JSON-основанная структура, где каждый выходной элемент является ключом к списку входных элементов, которые были объединены в него
        self.normalized_elements = None
        # словарь, который сопоставляет каждый входной элемент с его нормализованным выводом. Это будет использоваться в качестве кэша позже.
        self.normalizing_map = {}

        rendering_configs = {'n': n,
                             'elements': self.elements}

        messages = utils.compose_initial_LLM_messages_with_templates('normalizer.system.mustache', 'normalizer.user.mustache', rendering_configs)
        next_message = openai_utils.client().send_message(messages, temperature=0.1)
        debug_msg = f'Normalization result message: {next_message}'
        logger.debug(debug_msg)
        if self.verbose:
            print(debug_msg)
        result = utils.extract_json(next_message['content'])
        logger.debug(result)
        if self.verbose:
            print(result)

        self.normalized_elements = result


    def normalize(self, element_or_elements:Union[str, List[str]]) -> Union[str, List[str]]:
        """
        Нормализует указанный элемент или элементы.

        Этот метод использует механизм кэширования для повышения производительности. Если элемент был нормализован ранее,
        его нормализованная форма хранится в кэше (self.normalizing_map). Когда один и тот же элемент необходимо
        нормализовать снова, метод сначала проверит кэш и использует сохраненную нормализованную форму, если она доступна,
        вместо повторной нормализации элемента.

        Порядок элементов на выходе будет таким же, как и на входе. Это обеспечивается путем обработки
        элементов в порядке их появления на входе и добавления нормализованных элементов к выходу
        списку в том же порядке.

        Args:
            element_or_elements (Union[str, List[str]]): Элемент или элементы для нормализации.

        Returns:
            str: Нормализованный элемент, если на входе была строка.
            list: Нормализованные элементы, если на входе был список, сохраняя порядок элементов на входе.
        """
        if isinstance(element_or_elements, str):
            denormalized_elements = [element_or_elements]
        elif isinstance(element_or_elements, list):
            denormalized_elements = element_or_elements
        else:
            raise ValueError('The element_or_elements must be either a string or a list.')

        normalized_elements = []
        elements_to_normalize = []
        for element in denormalized_elements:
            if element not in self.normalizing_map:
                elements_to_normalize.append(element)

        if elements_to_normalize:
            rendering_configs = {'categories': self.normalized_elements,
                                    'elements': elements_to_normalize}
            messages = utils.compose_initial_LLM_messages_with_templates('normalizer.applier.system.mustache', 'normalizer.applier.user.mustache', rendering_configs)
            next_message = openai_utils.client().send_message(messages, temperature=0.1)
            debug_msg = f'Normalization result message: {next_message}'
            logger.debug(debug_msg)
            if self.verbose:
                print(debug_msg)
            normalized_elements_from_llm = utils.extract_json(next_message['content'])
            assert isinstance(normalized_elements_from_llm, list), 'The normalized element must be a list.'
            assert len(normalized_elements_from_llm) == len(elements_to_normalize), 'The number of normalized elements must be equal to the number of elements to normalize.'

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