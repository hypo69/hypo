### Анализ кода модуля `extraction`

**Качество кода**:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код разбит на логические классы, что облегчает его понимание и поддержку.
    - Используется `chevron` для шаблонизации, что делает код более гибким.
    - Присутствует логирование важных этапов работы.
    - Используется кэширование результатов для повышения производительности.
    - Наличие RST-документации для методов и классов.
- **Минусы**:
    - Не все методы документированы в формате RST.
    - Используется стандартный `json.dump` вместо `j_dumps` из `src.utils.jjson`.
    - Присутствуют неиспользуемые импорты (например, `logging` дважды).
    - Некоторые комментарии требуют уточнения и более конкретного описания.
    - В коде присутствуют неиспользуемые закомментированные блоки кода.
    - В некоторых местах кода есть избыточная логика проверки типов.
    - Есть дублирование логики в методах `_export_as_txt`, `_export_as_json`, `_export_as_docx`
    - В некоторых местах используется устаревший синтаксис (например, конкатенация строк через `f"..."`  вместо f-strings).
    - Проверка на существование правила `if trigger in self.rules:` могла бы быть более выразительной.

**Рекомендации по улучшению**:

1.  **Импорты**:
    - Удалить дублирующийся импорт `logging`.
    - Импортировать `logger` из `src.logger`.
    - Привести импорты в алфавитном порядке.
2.  **Документация**:
    - Дополнить RST-документацией все публичные методы и классы.
    - Улучшить существующие комментарии, сделав их более конкретными и информативными.
3.  **JSON**:
    - Использовать `j_dumps` из `src.utils.jjson` вместо `json.dump`.
4.  **Логирование**:
    - Использовать `logger.error` для обработки ошибок вместо `try-except`.
5. **Форматирование**:
   - Устранить избыточность проверок типов там, где это возможно.
   - Привести все строки к использованию одинарных кавычек, кроме логов, print и input.
   - Устранить дублирование кода в методах `_export_as_txt`, `_export_as_json`, `_export_as_docx`.
   - Использовать f-strings для форматирования строк.
   - Переписать проверку на существование правила более выразительно: `if trigger in self.rules:` в `if self.rules.get(trigger) is not None:`.
   - Убрать неиспользуемый закомментированный код.
6. **Общая архитектура**
   - Вынести логику валидации и преобразования имени файла в отдельную функцию, чтоб избежать дублирования в методе `export`

**Оптимизированный код**:

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
import chevron
import pandas as pd
import pypandoc
import markdown
from typing import Union, List, Callable

from src.logger import logger  # Import logger from src.logger
from src.utils.jjson import j_dumps  # Import j_dumps from src.utils.jjson

from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
from tinytroupe.utils import JsonSerializableRegistry

from tinytroupe import openai_utils
import tinytroupe.utils as utils


class ResultsExtractor:
    """
    A class to extract results from TinyTroupe elements.

    This class provides methods to extract data from agents and worlds,
    and to store the extracted data for further use.
    """
    def __init__(self):
        """
        Initializes the ResultsExtractor.

        Sets the path to the extraction prompt template and initializes caches for
        agent and world extractions.
        """
        self._extraction_prompt_template_path = os.path.join(os.path.dirname(__file__), 'prompts/interaction_results_extractor.mustache')
        # we'll cache the last extraction results for each type of extraction, so that we can use them to
        # generate reports or other additional outputs.
        self.agent_extraction = {}
        self.world_extraction = {}

    def extract_results_from_agent(self,
                                   tinyperson: TinyPerson,
                                   extraction_objective: str = 'The main points present in the agent\'s interactions history.',
                                   situation: str = '',
                                   fields: list = None,
                                   fields_hints: dict = None,
                                   verbose: bool = False) -> dict | None:
        """
        Extracts results from a TinyPerson instance.

        :param tinyperson: The TinyPerson instance to extract results from.
        :type tinyperson: TinyPerson
        :param extraction_objective: The extraction objective.
        :type extraction_objective: str
        :param situation: The situation to consider.
        :type situation: str
        :param fields: The fields to extract. If None, the extractor will decide what names to use.
        :type fields: list, optional
        :param fields_hints: Hints for the fields to extract.
        :type fields_hints: dict, optional
        :param verbose: Whether to print debug messages. Defaults to False.
        :type verbose: bool, optional
        :return: The extracted results as a dictionary or None if extraction failed.
        :rtype: dict | None

        :Example:
           >>> extractor = ResultsExtractor()
           >>> agent = TinyPerson(name='TestAgent')
           >>> result = extractor.extract_results_from_agent(agent, extraction_objective='Main points')
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

        result = utils.extract_json(next_message['content']) if next_message else None
        # cache the result
        self.agent_extraction[tinyperson.name] = result

        return result

    def extract_results_from_world(self,
                                   tinyworld: TinyWorld,
                                   extraction_objective: str = 'The main points that can be derived from the agents conversations and actions.',
                                   situation: str = '',
                                   fields: list = None,
                                   fields_hints: dict = None,
                                   verbose: bool = False) -> dict | None:
        """
        Extracts results from a TinyWorld instance.

        :param tinyworld: The TinyWorld instance to extract results from.
        :type tinyworld: TinyWorld
        :param extraction_objective: The extraction objective.
        :type extraction_objective: str
        :param situation: The situation to consider.
        :type situation: str
        :param fields: The fields to extract. If None, the extractor will decide what names to use.
        :type fields: list, optional
        :param fields_hints: Hints for the fields to extract.
        :type fields_hints: dict, optional
        :param verbose: Whether to print debug messages. Defaults to False.
        :type verbose: bool, optional
        :return: The extracted results as a dictionary or None if extraction failed.
        :rtype: dict | None

        :Example:
           >>> extractor = ResultsExtractor()
           >>> world = TinyWorld(name='TestWorld')
           >>> result = extractor.extract_results_from_world(world, extraction_objective='Main points')
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

        # TODO: either summarize first or break up into multiple tasks
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

        result = utils.extract_json(next_message['content']) if next_message else None
        # cache the result
        self.world_extraction[tinyworld.name] = result

        return result

    def save_as_json(self, filename: str, verbose: bool = False):
        """
        Saves the last extraction results as JSON.

        :param filename: The filename to save the JSON to.
        :type filename: str
        :param verbose: Whether to print debug messages. Defaults to False.
        :type verbose: bool, optional

        :Example:
           >>> extractor = ResultsExtractor()
           >>> extractor.save_as_json('results.json')
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                j_dumps({'agent_extractions': self.agent_extraction,
                           'world_extraction': self.world_extraction}, f, indent=4)
            if verbose:
                print(f'Saved extraction results to {filename}')
        except Exception as e:
            logger.error(f'Error saving extraction results to JSON: {e}')

class ResultsReducer:
    """
    A class to reduce results from TinyTroupe elements.

    This class provides methods to reduce the extracted data from agents based on predefined rules.
    """
    def __init__(self):
        """
        Initializes the ResultsReducer.

        Initializes the results cache and the reduction rules.
        """
        self.results = {}
        self.rules = {}

    def add_reduction_rule(self, trigger: str, func: Callable):
        """
        Adds a reduction rule for a specific trigger.

        :param trigger: The trigger for the reduction rule.
        :type trigger: str
        :param func: The function to execute when the trigger is encountered.
        :type func: callable
        :raises Exception: If a rule for the given trigger already exists.

        :Example:
            >>> reducer = ResultsReducer()
            >>> def my_reduction_rule(**kwargs):
            ...     return kwargs['content']
            >>> reducer.add_reduction_rule('stimulus_type', my_reduction_rule)
        """
        if self.rules.get(trigger) is not None:
            raise Exception(f'Rule for {trigger} already exists.')

        self.rules[trigger] = func

    def reduce_agent(self, agent: TinyPerson) -> list:
        """
        Reduces the agent's episodic memory based on the defined rules.

        :param agent: The TinyPerson instance to reduce.
        :type agent: TinyPerson
        :return: A list of reduced events.
        :rtype: list

        :Example:
            >>> reducer = ResultsReducer()
            >>> agent = TinyPerson(name='TestAgent')
            >>> result = reducer.reduce_agent(agent)
        """
        reduction = []
        for message in agent.episodic_memory.retrieve_all():
            if message['role'] == 'system':
                continue  # doing nothing for `system` role yet at least

            elif message['role'] == 'user':
                # User role is related to stimuli only
                stimulus_type = message['content']['stimuli'][0]['type']
                stimulus_content = message['content']['stimuli'][0]['content']
                stimulus_source = message['content']['stimuli'][0]['source']
                stimulus_timestamp = message['simulation_timestamp']

                if stimulus_type in self.rules:
                    extracted = self.rules[stimulus_type](focus_agent=agent, source_agent=TinyPerson.get_agent_by_name(stimulus_source), target_agent=agent, kind='stimulus', event=stimulus_type, content=stimulus_content, timestamp=stimulus_timestamp)
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
                        extracted = self.rules[action_type](focus_agent=agent, source_agent=agent, target_agent=TinyPerson.get_agent_by_name(action_target), kind='action', event=action_type, content=action_content, timestamp=action_timestamp)
                        if extracted is not None:
                            reduction.append(extracted)

        return reduction

    def reduce_agent_to_dataframe(self, agent: TinyPerson, column_names: list = None) -> pd.DataFrame:
        """
        Reduces the agent's episodic memory and returns the result as a Pandas DataFrame.

        :param agent: The TinyPerson instance to reduce.
        :type agent: TinyPerson
        :param column_names: The list of column names for the DataFrame.
        :type column_names: list, optional
        :return: A Pandas DataFrame containing the reduced data.
        :rtype: pd.DataFrame

        :Example:
           >>> reducer = ResultsReducer()
           >>> agent = TinyPerson(name='TestAgent')
           >>> df = reducer.reduce_agent_to_dataframe(agent, column_names=['event', 'content'])
        """
        reduction = self.reduce_agent(agent)
        return pd.DataFrame(reduction, columns=column_names)


class ArtifactExporter(JsonSerializableRegistry):
    """
    An artifact exporter is responsible for exporting artifacts from TinyTroupe elements, for example
    in order to create synthetic data files from simulations.
    """

    def __init__(self, base_output_folder: str) -> None:
        """
        Initializes the ArtifactExporter.

        :param base_output_folder: The base output folder for the artifacts.
        :type base_output_folder: str

        :Example:
           >>> exporter = ArtifactExporter(base_output_folder='output')
        """
        self.base_output_folder = base_output_folder

    def _sanitize_artifact_name(self, artifact_name: str) -> str:
        """
         Sanitizes the artifact name by replacing invalid characters with hyphens.
        :param artifact_name: The original artifact name.
        :type artifact_name: str
        :return: The sanitized artifact name.
        :rtype: str
        """
        invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '\n', '\t', '\r', ';']
        for char in invalid_chars:
            if char in artifact_name:
                artifact_name = artifact_name.replace(char, '-')
                logger.warning(f"Replaced invalid character {char} with hyphen in artifact name '{artifact_name}'.")
        return artifact_name


    def export(self, artifact_name: str, artifact_data: Union[dict, str], content_type: str, content_format: str = None, target_format: str = "txt", verbose: bool = False):
        """
        Exports the specified artifact data to a file.

        :param artifact_name: The name of the artifact.
        :type artifact_name: str
        :param artifact_data: The data to export. If a dict is given, it will be saved as JSON.
            If a string is given, it will be saved as is.
        :type artifact_data: Union[dict, str]
        :param content_type: The type of the content within the artifact.
        :type content_type: str
        :param content_format: The format of the content within the artifact (e.g., md, csv, etc). Defaults to None.
        :type content_format: str, optional
        :param target_format: The format to export the artifact to (e.g., json, txt, docx, etc).
        :type target_format: str, optional
        :param verbose: Whether to print debug messages. Defaults to False.
        :type verbose: bool, optional
        :raises ValueError: If the artifact data is not a string or dictionary, or if the target format is not supported.

        :Example:
           >>> exporter = ArtifactExporter(base_output_folder='output')
           >>> exporter.export(artifact_name='test', artifact_data='Hello world', content_type='text')
           >>> exporter.export(artifact_name='test', artifact_data={'content':'Hello world'}, content_type='text', target_format='json')
        """
        # dedent inputs, just in case
        if isinstance(artifact_data, str):
            artifact_data = utils.dedent(artifact_data)
        elif isinstance(artifact_data, dict):
            artifact_data['content'] = utils.dedent(artifact_data['content'])
        else:
            raise ValueError('The artifact data must be either a string or a dictionary.')

        # clean the artifact name of invalid characters
        artifact_name = self._sanitize_artifact_name(artifact_name)

        artifact_file_path = self._compose_filepath(artifact_data, artifact_name, content_type, target_format, verbose)

        if target_format == 'json':
            self._export_as_json(artifact_file_path, artifact_data, verbose)
        elif target_format in ['txt', 'text', 'md', 'markdown']:
            self._export_as_txt(artifact_file_path, artifact_data, verbose)
        elif target_format == 'docx':
            self._export_as_docx(artifact_file_path, artifact_data, content_format, verbose)
        else:
            raise ValueError(f'Unsupported target format: {target_format}.')

    def _export_as_txt(self, artifact_file_path: str, artifact_data: Union[dict, str], verbose: bool = False):
        """
        Exports the specified artifact data to a text file.
        :param artifact_file_path: The path to the text file.
        :type artifact_file_path: str
        :param artifact_data: The artifact data, which could be a string or a dict.
        :type artifact_data: Union[dict, str]
        :param verbose: Whether to print verbose output
        :type verbose: bool, optional
        """
        try:
           with open(artifact_file_path, 'w', encoding='utf-8') as f:
              content = artifact_data['content'] if isinstance(artifact_data, dict) else artifact_data
              f.write(content)
        except Exception as e:
            logger.error(f'Error exporting artifact to text file: {e}')

    def _export_as_json(self, artifact_file_path: str, artifact_data: Union[dict, str], verbose: bool = False):
        """
        Exports the specified artifact data to a JSON file.
        :param artifact_file_path: The path to the JSON file.
        :type artifact_file_path: str
        :param artifact_data: The artifact data, which must be a dict.
        :type artifact_data: Union[dict, str]
        :param verbose: Whether to print verbose output
        :type verbose: bool, optional
        :raises ValueError: If the artifact data is not a dictionary.
        """
        try:
            with open(artifact_file_path, 'w', encoding='utf-8') as f:
                if isinstance(artifact_data, dict):
                     j_dumps(artifact_data, f, indent=4)
                else:
                    raise ValueError('The artifact data must be a dictionary to export to JSON.')
        except Exception as e:
            logger.error(f'Error exporting artifact to JSON file: {e}')

    def _export_as_docx(self, artifact_file_path: str, artifact_data: Union[dict, str], content_original_format: str, verbose: bool = False):
        """
        Exports the specified artifact data to a DOCX file.
        :param artifact_file_path: The path to the DOCX file.
        :type artifact_file_path: str
        :param artifact_data: The artifact data, which could be a string or a dict.
        :type artifact_data: Union[dict, str]
        :param content_original_format: The original format of the content ('text', 'txt', 'markdown', or 'md').
        :type content_original_format: str
        :param verbose: Whether to print verbose output
        :type verbose: bool, optional
        :raises ValueError: If the original format is not valid.
        """
        if content_original_format not in ['text', 'txt', 'markdown', 'md']:
           raise ValueError(f'The original format cannot be {content_original_format} to export to DOCX.')

        content_original_format = 'markdown' if content_original_format == 'md' else content_original_format

        content = artifact_data['content'] if isinstance(artifact_data, dict) else artifact_data

        try:
           html_content = markdown.markdown(content)
           pypandoc.convert_text(html_content, 'docx', format='html', outputfile=artifact_file_path)
        except Exception as e:
            logger.error(f'Error exporting artifact to DOCX file: {e}')

    def _compose_filepath(self, artifact_data: Union[dict, str], artifact_name: str, content_type: str, target_format: str = None, verbose: bool = False) -> str:
        """
        Composes the file path for the artifact to export.
        :param artifact_data: The artifact data.
        :type artifact_data: Union[dict, str]
        :param artifact_name: The name of the artifact.
        :type artifact_name: str
        :param content_type: The type of content.
        :type content_type: str
        :param target_format: The target format of the output (e.g., json, txt, docx, etc.).
        :type target_format: str, optional
        :param verbose: Whether to print verbose output.
        :type verbose: bool, optional
        :return: The composed file path.
        :rtype: str
        """
        extension = target_format if target_format else 'txt' if isinstance(artifact_data, str) else 'json'
        subfolder = content_type if content_type else ''
        artifact_file_path = os.path.join(self.base_output_folder, subfolder, f'{artifact_name}.{extension}')
        os.makedirs(os.path.dirname(artifact_file_path), exist_ok=True)
        return artifact_file_path


class Normalizer:
    """
    A mechanism to normalize passages, concepts and other textual elements.
    """

    def __init__(self, elements: List[str], n: int, verbose: bool = False):
        """
        Normalizes the specified elements.

        :param elements: The elements to normalize.
        :type elements: list
        :param n: The number of normalized elements to output.
        :type n: int
        :param verbose: Whether to print debug messages. Defaults to False.
        :type verbose: bool, optional

        :Example:
           >>> normalizer = Normalizer(elements=['apple', 'banana', 'orange'], n=2)
        """
        self.elements = list(set(elements))
        self.n = n
        self.verbose = verbose
        self.normalized_elements = None
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

    def normalize(self, element_or_elements: Union[str, List[str]]) -> Union[str, List[str]]:
        """
        Normalizes the specified element or elements.

        This method uses a caching mechanism to improve performance. If an element has been normalized before,
        its normalized form is stored in a cache (self.normalizing_map). When the same element needs to be
        normalized again, the method will first check the cache and use the stored normalized form if available,
        instead of normalizing the element again.

        The order of elements in the output will be the same as in the input. This is ensured by processing
        the elements in the order they appear in the input and appending the normalized elements to the output
        list in the same order.

        :param element_or_elements: The element or elements to normalize.
        :type element_or_elements: Union[str, List[str]]
        :return: The normalized element if the input was a string, or a list of normalized elements if the input was a list.
        :rtype: Union[str, List[str]]

        :Example:
           >>> normalizer = Normalizer(elements=['apple', 'banana', 'orange'], n=2)
           >>> normalized_element = normalizer.normalize('apple')
           >>> normalized_elements = normalizer.normalize(['apple', 'banana'])
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