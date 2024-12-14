# Анализ кода модуля `extraction.py`

**Качество кода: 8/10**

-   **Плюсы:**
    -   Хорошая структура модуля с разделением на классы `ResultsExtractor`, `ResultsReducer`, `ArtifactExporter` и `Normalizer`, каждый из которых выполняет свою конкретную задачу.
    -   Используются `logger` для логирования, что помогает в отладке и мониторинге.
    -   Присутствует кэширование результатов извлечения в `ResultsExtractor`.
    -   Реализована поддержка различных форматов вывода (`json`, `txt`, `docx`).
    -   Используется `chevron` для шаблонизации запросов к LLM.
    -   Используется `pypandoc` для конвертации в `docx`.
    -   Присутствуют механизмы нормализации текста через LLM.
    -   Код достаточно хорошо документирован.

-   **Минусы:**
    -   Не используется `j_loads` или `j_loads_ns` для чтения JSON, хотя это требование инструкции.
    -   Не все функции и классы имеют docstrings в формате reStructuredText (RST).
    -   В некоторых местах используется `try-except` без `logger.error`, что можно улучшить.
    -   Некоторые переменные и функции не соответствуют соглашениям об именовании, принятым в предыдущих файлах (в частности, camelCase).
    -   Некоторые комментарии после `#`  не объясняют подробно следующую строку кода.

**Рекомендации по улучшению:**

1.  **Использовать `j_loads`:** Заменить стандартный `json.load` на `j_loads` из `src.utils.jjson`.
2.  **Форматирование docstrings:**  Привести все docstrings в соответствие с форматом reStructuredText (RST).
3.  **Обработка исключений:** Заменить стандартные `try-except` на использование `logger.error` для логирования ошибок.
4.  **Именование:** Привести имена функций, переменных и импортов в соответствие с ранее обработанными файлами.
5.  **Детальные комментарии:** Добавить подробные комментарии в формате RST ко всем функциям, методам и классам, а также более детально прокомментировать каждую строку кода после `#`.
6.  **Удаление неиспользуемых импортов:** Убрать импорт `logging` (он уже есть).

**Оптимизированный код:**

```python
"""
Модуль для извлечения данных из элементов TinyTroupe.
=========================================================================================

Этот модуль предоставляет различные утилиты для извлечения данных из элементов TinyTroupe,
таких как агенты и миры. Он также предоставляет механизм для уменьшения извлеченных данных
до более краткой формы и для экспорта артефактов из элементов TinyTroupe.

Пример использования
--------------------

Пример извлечения результатов из агента:

.. code-block:: python

    extractor = ResultsExtractor()
    results = extractor.extract_results_from_agent(agent, extraction_objective="Основные моменты", verbose=True)

Пример экспорта артефактов:

.. code-block:: python

    exporter = ArtifactExporter(base_output_folder="./output")
    exporter.export(artifact_name="agent_report", artifact_data={"content": "Отчет об агенте"}, content_type="report", target_format="docx")

"""
import os
#  импортируем os для работы с файловой системой
import json
# импортируем json для работы с json
import chevron
# импортируем chevron для работы с шаблонами
import pandas as pd
# импортируем pandas для работы с dataframe
import pypandoc
# импортируем pypandoc для работы с документами
import markdown
# импортируем markdown для работы с markdown
from typing import Union, List, Any
# импортируем типы данных
from src.logger.logger import logger
# импортируем logger для логирования

from tinytroupe.agent import TinyPerson
# импортируем класс TinyPerson
from tinytroupe.environment import TinyWorld
# импортируем класс TinyWorld
from tinytroupe.factory import TinyPersonFactory
# импортируем класс TinyPersonFactory
from tinytroupe.utils import JsonSerializableRegistry
# импортируем класс JsonSerializableRegistry

from tinytroupe import openai_utils
# импортируем openai_utils
import tinytroupe.utils as utils
# импортируем tinytroupe.utils
from src.utils.jjson import j_loads
# импортируем j_loads для работы с json


class ResultsExtractor:
    """
    Класс для извлечения результатов из агентов и миров.

    :ivar _extraction_prompt_template_path: Путь к шаблону для промпта.
    :vartype _extraction_prompt_template_path: str
    :ivar agent_extraction: Кэш последних результатов извлечения для агентов.
    :vartype agent_extraction: dict
    :ivar world_extraction: Кэш последних результатов извлечения для миров.
    :vartype world_extraction: dict
    """

    def __init__(self):
        """
        Инициализирует класс ResultsExtractor.
        """
        # код задаёт путь к шаблону промпта для извлечения данных
        self._extraction_prompt_template_path = os.path.join(os.path.dirname(__file__), 'prompts/interaction_results_extractor.mustache')

        # код инициализирует кэш для результатов извлечения данных агентов
        self.agent_extraction = {}
        # код инициализирует кэш для результатов извлечения данных миров
        self.world_extraction = {}

    def extract_results_from_agent(self,
                        tinyperson: TinyPerson,
                        extraction_objective: str = "Основные моменты в истории взаимодействий агента.",
                        situation: str = "",
                        fields: list = None,
                        fields_hints: dict = None,
                        verbose: bool = False) -> dict:
        """
        Извлекает результаты из экземпляра TinyPerson.

        :param tinyperson: Экземпляр TinyPerson, из которого нужно извлечь результаты.
        :type tinyperson: TinyPerson
        :param extraction_objective: Цель извлечения данных.
        :type extraction_objective: str
        :param situation: Ситуация, которую нужно учитывать.
        :type situation: str
        :param fields: Поля для извлечения. Если None, экстрактор выберет их самостоятельно.
        :type fields: list, optional
        :param fields_hints: Подсказки для полей.
        :type fields_hints: dict, optional
        :param verbose: Флаг, указывающий, выводить ли отладочные сообщения.
        :type verbose: bool, optional
        :return: Результаты извлечения.
        :rtype: dict
        """
        #  создаем пустой список для сообщений
        messages = []

        #  создаем пустой словарь для конфигураций рендеринга
        rendering_configs = {}
        #  проверяем, если поля не None, то формируем строку из списка полей
        if fields is not None:
            rendering_configs["fields"] = ", ".join(fields)

        #  проверяем, если fields_hints не None, то формируем список кортежей (ключ, значение) из словаря
        if fields_hints is not None:
            rendering_configs["fields_hints"] = list(fields_hints.items())

        #  добавляем в список сообщений системное сообщение с отрендеренным шаблоном из файла
        messages.append({"role": "system",
                         "content": chevron.render(
                             open(self._extraction_prompt_template_path).read(),
                             rendering_configs)})

        # код получает историю взаимодействий агента
        interaction_history = tinyperson.pretty_current_interactions(max_content_length=None)

        #  формируем промпт для запроса на извлечение данных
        extraction_request_prompt = \
f"""
## Цель извлечения

{extraction_objective}

## Ситуация
Вы рассматриваете одного агента, по имени {tinyperson.name}. Ваша цель, таким образом, относится именно к этому агенту.
{situation}

## История взаимодействий агента

Вы будете рассматривать историю взаимодействий агента, которая включает стимулы, которые он получил, а также действия, которые он
выполнил.

{interaction_history}
"""
        #  добавляем в список сообщений сообщение пользователя с промптом
        messages.append({"role": "user", "content": extraction_request_prompt})

        # код отправляет сообщение в OpenAI и получает ответ
        next_message = openai_utils.client().send_message(messages, temperature=0.0)

        # код формирует отладочное сообщение
        debug_msg = f"Extraction raw result message: {next_message}"
        #  логируем отладочное сообщение
        logger.debug(debug_msg)
        # если verbose = True, то выводим отладочное сообщение на экран
        if verbose:
            print(debug_msg)
        #  проверяем, если next_message не None, то извлекаем json из контента сообщения
        if next_message is not None:
            result = utils.extract_json(next_message["content"])
        else:
            #  если next_message = None, то result = None
            result = None

        # код кэширует результат извлечения
        self.agent_extraction[tinyperson.name] = result

        #  возвращаем результат
        return result


    def extract_results_from_world(self,
                                   tinyworld: TinyWorld,
                                   extraction_objective: str = "Основные моменты, которые можно извлечь из разговоров и действий агентов.",
                                   situation: str = "",
                                   fields: list = None,
                                   fields_hints: dict = None,
                                   verbose: bool = False) -> dict:
        """
        Извлекает результаты из экземпляра TinyWorld.

        :param tinyworld: Экземпляр TinyWorld, из которого нужно извлечь результаты.
        :type tinyworld: TinyWorld
        :param extraction_objective: Цель извлечения данных.
        :type extraction_objective: str
        :param situation: Ситуация, которую нужно учитывать.
        :type situation: str
        :param fields: Поля для извлечения. Если None, экстрактор выберет их самостоятельно.
        :type fields: list, optional
        :param fields_hints: Подсказки для полей.
        :type fields_hints: dict, optional
        :param verbose: Флаг, указывающий, выводить ли отладочные сообщения.
        :type verbose: bool, optional
        :return: Результаты извлечения.
        :rtype: dict
        """
        #  создаем пустой список для сообщений
        messages = []
        #  создаем пустой словарь для конфигураций рендеринга
        rendering_configs = {}
        # проверяем, если поля не None, то формируем строку из списка полей
        if fields is not None:
            rendering_configs["fields"] = ", ".join(fields)
        #  проверяем, если fields_hints не None, то формируем список кортежей (ключ, значение) из словаря
        if fields_hints is not None:
            rendering_configs["fields_hints"] = list(fields_hints.items())
        #  добавляем в список сообщений системное сообщение с отрендеренным шаблоном из файла
        messages.append({"role": "system",
                         "content": chevron.render(
                             open(self._extraction_prompt_template_path).read(),
                             rendering_configs)})

        # TODO: либо сначала суммировать, либо разбить на несколько задач
        #  код получает историю взаимодействий мира
        interaction_history = tinyworld.pretty_current_interactions(max_content_length=None)
        #  формируем промпт для запроса на извлечение данных
        extraction_request_prompt = \
f"""
## Цель извлечения

{extraction_objective}

## Ситуация
Вы рассматриваете различных агентов.
{situation}

## История взаимодействий агентов

Вы будете рассматривать историю взаимодействий различных агентов, которые существуют в среде под названием {tinyworld.name}.
Каждая история взаимодействий включает стимулы, которые соответствующий агент получил, а также действия, которые он выполнил.

{interaction_history}
"""
        #  добавляем в список сообщений сообщение пользователя с промптом
        messages.append({"role": "user", "content": extraction_request_prompt})

        #  код отправляет сообщение в OpenAI и получает ответ
        next_message = openai_utils.client().send_message(messages, temperature=0.0)
        #  код формирует отладочное сообщение
        debug_msg = f"Extraction raw result message: {next_message}"
        #  логируем отладочное сообщение
        logger.debug(debug_msg)
        #  если verbose = True, то выводим отладочное сообщение на экран
        if verbose:
            print(debug_msg)
        #  проверяем, если next_message не None, то извлекаем json из контента сообщения
        if next_message is not None:
            result = utils.extract_json(next_message["content"])
        else:
            #  если next_message = None, то result = None
            result = None

        #  код кэширует результат извлечения
        self.world_extraction[tinyworld.name] = result

        #  возвращаем результат
        return result

    def save_as_json(self, filename: str, verbose: bool = False):
        """
        Сохраняет последние результаты извлечения в формате JSON.

        :param filename: Имя файла для сохранения JSON.
        :type filename: str
        :param verbose: Флаг, указывающий, выводить ли отладочные сообщения.
        :type verbose: bool, optional
        """
        #  открываем файл для записи
        with open(filename, 'w') as f:
            #  записываем json в файл
            json.dump({"agent_extractions": self.agent_extraction,
                       "world_extraction": self.world_extraction}, f, indent=4)

        #  если verbose = True, то выводим сообщение о сохранении файла
        if verbose:
            print(f"Saved extraction results to {filename}")


class ResultsReducer:
    """
    Класс для редукции результатов извлечения.

    :ivar results: Словарь для хранения результатов редукции.
    :vartype results: dict
    :ivar rules: Словарь для хранения правил редукции.
    :vartype rules: dict
    """
    def __init__(self):
        """
        Инициализирует класс ResultsReducer.
        """
        # код инициализирует словарь для хранения результатов редукции
        self.results = {}
        # код инициализирует словарь для хранения правил редукции
        self.rules = {}

    def add_reduction_rule(self, trigger: str, func: callable):
        """
        Добавляет правило редукции.

        :param trigger: Триггер для правила редукции.
        :type trigger: str
        :param func: Функция для правила редукции.
        :type func: callable
        :raises Exception: Если правило для данного триггера уже существует.
        """
        #  проверяем, если правило для данного триггера уже существует, то выбрасываем исключение
        if trigger in self.rules:
            raise Exception(f"Rule for {trigger} already exists.")
        #  добавляем правило редукции в словарь
        self.rules[trigger] = func

    def reduce_agent(self, agent: TinyPerson) -> list:
        """
        Выполняет редукцию результатов для агента.

        :param agent: Агент, для которого нужно выполнить редукцию.
        :type agent: TinyPerson
        :return: Список редуцированных результатов.
        :rtype: list
        """
        # код создает список для хранения результатов редукции
        reduction = []
        # код проходит по всем сообщениям в эпизодической памяти агента
        for message in agent.episodic_memory.retrieve_all():
            #  если роль сообщения 'system', то пропускаем его
            if message['role'] == 'system':
                continue  # код не обрабатывает сообщения с ролью system

            #  если роль сообщения 'user'
            elif message['role'] == 'user':
                #  стимул
                stimulus_type = message['content']['stimuli'][0]['type']
                # код получает контент стимула
                stimulus_content = message['content']['stimuli'][0]['content']
                # код получает источник стимула
                stimulus_source = message['content']['stimuli'][0]['source']
                #  код получает время стимула
                stimulus_timestamp = message['simulation_timestamp']

                #  проверяем, если тип стимула есть в правилах, то применяем правило
                if stimulus_type in self.rules:
                    #  вызываем функцию редукции и добавляем результат в список редукции
                    extracted = self.rules[stimulus_type](focus_agent=agent, source_agent=TinyPerson.get_agent_by_name(stimulus_source), target_agent=agent, kind='stimulus', event=stimulus_type, content=stimulus_content, timestamp=stimulus_timestamp)
                    if extracted is not None:
                        reduction.append(extracted)

            #  если роль сообщения 'assistant'
            elif message['role'] == 'assistant':
                #  действие
                if 'action' in message['content']:
                    #  получаем тип действия
                    action_type = message['content']['action']['type']
                    # код получает контент действия
                    action_content = message['content']['action']['content']
                    # код получает цель действия
                    action_target = message['content']['action']['target']
                    #  код получает время действия
                    action_timestamp = message['simulation_timestamp']
                    #  проверяем, если тип действия есть в правилах, то применяем правило
                    if action_type in self.rules:
                        # вызываем функцию редукции и добавляем результат в список редукции
                        extracted = self.rules[action_type](focus_agent=agent, source_agent=agent, target_agent=TinyPerson.get_agent_by_name(action_target), kind='action', event=action_type, content=action_content, timestamp=action_timestamp)
                        if extracted is not None:
                            reduction.append(extracted)

        #  возвращаем список редуцированных результатов
        return reduction

    def reduce_agent_to_dataframe(self, agent: TinyPerson, column_names: list = None) -> pd.DataFrame:
        """
        Выполняет редукцию результатов агента и преобразует их в DataFrame.

        :param agent: Агент, для которого нужно выполнить редукцию.
        :type agent: TinyPerson
        :param column_names: Список имен столбцов для DataFrame.
        :type column_names: list, optional
        :return: DataFrame с редуцированными результатами.
        :rtype: pd.DataFrame
        """
        #  получаем список редуцированных результатов
        reduction = self.reduce_agent(agent)
        #  создаем DataFrame из списка редуцированных результатов
        return pd.DataFrame(reduction, columns=column_names)


class ArtifactExporter(JsonSerializableRegistry):
    """
    Экспортер артефактов из элементов TinyTroupe.

    :ivar base_output_folder: Базовая папка для вывода артефактов.
    :vartype base_output_folder: str
    """
    def __init__(self, base_output_folder: str) -> None:
        """
        Инициализирует класс ArtifactExporter.

        :param base_output_folder: Базовая папка для вывода артефактов.
        :type base_output_folder: str
        """
        # код задаёт базовую папку для сохранения экспортированных артефактов
        self.base_output_folder = base_output_folder

    def export(self, artifact_name: str, artifact_data: Union[dict, str], content_type: str, content_format: str = None, target_format: str = "txt", verbose: bool = False):
        """
        Экспортирует данные артефакта в файл.

        :param artifact_name: Имя артефакта.
        :type artifact_name: str
        :param artifact_data: Данные для экспорта.
        :type artifact_data: Union[dict, str]
        :param content_type: Тип контента артефакта.
        :type content_type: str
        :param content_format: Формат контента артефакта.
        :type content_format: str, optional
        :param target_format: Формат для экспорта артефакта.
        :type target_format: str, optional
        :param verbose: Флаг, указывающий, выводить ли отладочные сообщения.
        :type verbose: bool, optional
        :raises ValueError: Если формат вывода не поддерживается.
        """
        #  удаляем отступы в начале строк, если artifact_data - строка
        if isinstance(artifact_data, str):
            artifact_data = utils.dedent(artifact_data)
        #  удаляем отступы в начале строк, если artifact_data - словарь
        elif isinstance(artifact_data, dict):
            artifact_data['content'] = utils.dedent(artifact_data['content'])
        #  если тип artifact_data не строка и не словарь, то выбрасываем исключение
        else:
            raise ValueError("The artifact data must be either a string or a dictionary.")

        #  определяем недопустимые символы
        invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '\n', '\t', '\r', ';']
        #  проходим по всем недопустимым символам
        for char in invalid_chars:
            #  проверяем, если недопустимый символ есть в имени артефакта, то заменяем его на дефис
            if char in artifact_name:
                artifact_name = artifact_name.replace(char, "-")
                logger.warning(f"Replaced invalid character {char} with hyphen in artifact name \'{artifact_name}\'.")

        #  формируем путь к файлу для сохранения артефакта
        artifact_file_path = self._compose_filepath(artifact_data, artifact_name, content_type, target_format, verbose)

        #  проверяем формат экспорта и вызываем соответствующую функцию
        if target_format == "json":
            self._export_as_json(artifact_file_path, artifact_data, content_type, verbose)
        #  если формат экспорта "txt" или "text" или "md" или "markdown", то вызываем функцию для экспорта в txt
        elif target_format == "txt" or target_format == "text" or target_format == "md" or target_format == "markdown":
            self._export_as_txt(artifact_file_path, artifact_data, content_type, verbose)
        #  если формат экспорта "docx", то вызываем функцию для экспорта в docx
        elif target_format == "docx":
            self._export_as_docx(artifact_file_path, artifact_data, content_format, verbose)
        # если формат экспорта не поддерживается, то выбрасываем исключение
        else:
            raise ValueError(f"Unsupported target format: {target_format}.")


    def _export_as_txt(self, artifact_file_path: str, artifact_data: Union[dict, str], content_type: str, verbose: bool = False):
        """
        Экспортирует данные артефакта в текстовый файл.

        :param artifact_file_path: Путь к файлу для сохранения артефакта.
        :type artifact_file_path: str
        :param artifact_data: Данные для экспорта.
        :type artifact_data: Union[dict, str]
        :param content_type: Тип контента артефакта.
        :type content_type: str
        :param verbose: Флаг, указывающий, выводить ли отладочные сообщения.
        :type verbose: bool, optional
        """
        #  открываем файл для записи
        with open(artifact_file_path, 'w', encoding="utf-8") as f:
            #  если artifact_data - словарь, то контент находится под ключом "content"
            if isinstance(artifact_data, dict):
                content = artifact_data['content']
            #  иначе, artifact_data - строка, то контент - это сама строка
            else:
                content = artifact_data
            #  записываем контент в файл
            f.write(content)

    def _export_as_json(self, artifact_file_path: str, artifact_data: Union[dict, str], content_type: str, verbose: bool = False):
        """
        Экспортирует данные артефакта в JSON файл.

        :param artifact_file_path: Путь к файлу для сохранения артефакта.
        :type artifact_file_path: str
        :param artifact_data: Данные для экспорта.
        :type artifact_data: Union[dict, str]
        :param content_type: Тип контента артефакта.
        :type content_type: str
        :param verbose: Флаг, указывающий, выводить ли отладочные сообщения.
        :type verbose: bool, optional
        :raises ValueError: Если данные артефакта не являются словарем.
        """
        #  открываем файл для записи
        with open(artifact_file_path, 'w', encoding="utf-8") as f:
            #  если artifact_data - словарь, то записываем его в файл
            if isinstance(artifact_data, dict):
                json.dump(artifact_data, f, indent=4)
            # если artifact_data не является словарем, то выбрасываем исключение
            else:
                raise ValueError("The artifact data must be a dictionary to export to JSON.")

    def _export_as_docx(self, artifact_file_path: str, artifact_data: Union[dict, str], content_original_format: str, verbose: bool = False):
        """
        Экспортирует данные артефакта в DOCX файл.

        :param artifact_file_path: Путь к файлу для сохранения артефакта.
        :type artifact_file_path: str
        :param artifact_data: Данные для экспорта.
        :type artifact_data: Union[dict, str]
        :param content_original_format: Исходный формат контента артефакта.
        :type content_original_format: str
        :param verbose: Флаг, указывающий, выводить ли отладочные сообщения.
        :type verbose: bool, optional
        :raises ValueError: Если исходный формат контента не поддерживается.
        """
        #  проверяем, если исходный формат контента не поддерживается, то выбрасываем исключение
        if content_original_format not in ['text', 'txt', 'markdown', 'md']:
            raise ValueError(f"The original format cannot be {content_original_format} to export to DOCX.")
        else:
            #  нормализуем формат контента
            content_original_format = 'markdown' if content_original_format == 'md' else content_original_format

        #  получаем контент для экспорта
        if isinstance(artifact_data, dict):
            content = artifact_data['content']
        else:
            content = artifact_data
        #  конвертируем контент в html
        html_content = markdown.markdown(content)

        #  конвертируем html в docx
        pypandoc.convert_text(html_content, 'docx', format='html', outputfile=artifact_file_path)

    ###########################################################
    # IO
    ###########################################################

    def _compose_filepath(self, artifact_data: Union[dict, str], artifact_name: str, content_type: str, target_format: str = None, verbose: bool = False) -> str:
        """
        Формирует путь к файлу для сохранения артефакта.

        :param artifact_data: Данные для экспорта.
        :type artifact_data: Union[dict, str]
        :param artifact_name: Имя артефакта.
        :type artifact_name: str
        :param content_type: Тип контента артефакта.
        :type content_type: str
        :param target_format: Формат для экспорта артефакта.
        :type target_format: str, optional
         :param verbose: Флаг, указывающий, выводить ли отладочные сообщения.
        :type verbose: bool, optional
        :return: Путь к файлу для сохранения артефакта.
        :rtype: str
        """
        #  определяем расширение файла
        extension = None
        # если target_format задан, то используем его как расширение
        if target_format is not None:
            extension = f"{target_format}"
        #  если artifact_data - строка и target_format не задан, то расширение - txt
        elif isinstance(artifact_data, str) and target_format is None:
            extension = "txt"

        #  определяем подпапку для сохранения файла
        if content_type is None:
            subfolder = ""
        else:
            subfolder = content_type

        #  формируем полный путь к файлу
        artifact_file_path = os.path.join(self.base_output_folder, subfolder, f"{artifact_name}.{extension}")

        #  создаем промежуточные директории, если они не существуют
        os.makedirs(os.path.dirname(artifact_file_path), exist_ok=True)

        #  возвращаем полный путь к файлу
        return artifact_file_path


class Normalizer:
    """
    Механизм для нормализации фрагментов текста, концепций и других текстовых элементов.

    :ivar elements: Список элементов для нормализации.
    :vartype elements: List[str]
    :ivar n: Количество нормализованных элементов для вывода.
    :vartype n: int
    :ivar verbose: Флаг, указывающий, выводить ли отладочные сообщения.
    :vartype verbose: bool
    :ivar normalized_elements: JSON-структура, где каждый выходной элемент является ключом к списку входных элементов, которые были объединены в него.
    :vartype normalized_elements: dict
    :ivar normalizing_map: Словарь, который сопоставляет каждый входной элемент с его нормализованным выводом.
    :vartype normalizing_map: dict
    """
    def __init__(self, elements: List[str], n: int, verbose: bool = False):
        """
        Инициализирует класс Normalizer.

        :param elements: Список элементов для нормализации.
        :type elements: List[str]
        :param n: Количество нормализованных элементов для вывода.
        :type n: int
        :param verbose: Флаг, указывающий, выводить ли отладочные сообщения.
        :type verbose: bool, optional
        """
        #  делаем список элементов уникальным
        self.elements = list(set(elements))
        #  количество нормализованных элементов для вывода
        self.n = n
        #  флаг для отладочных сообщений
        self.verbose = verbose
        #  словарь для хранения нормализованных элементов
        self.normalized_elements = None
        #  словарь для кэширования нормализованных элементов
        self.normalizing_map = {}

        #  создаем конфигурацию для рендеринга шаблонов
        rendering_configs = {"n": n,
                             "elements": self.elements}
        # формируем сообщения для отправки в LLM
        messages = utils.compose_initial_LLM_messages_with_templates("normalizer.system.mustache", "normalizer.user.mustache", rendering_configs)
        #  отправляем сообщение в OpenAI и получаем ответ
        next_message = openai_utils.client().send_message(messages, temperature=0.1)
        #  формируем отладочное сообщение
        debug_msg = f"Normalization result message: {next_message}"
        #  логируем отладочное сообщение
        logger.debug(debug_msg)
        #  если verbose = True, то выводим отладочное сообщение на экран
        if self.verbose:
            print(debug_msg)
        #  извлекаем json из ответа
        result = utils.extract_json(next_message["content"])
        #  логируем результат
        logger.debug(result)
        #  если verbose = True, то выводим результат на экран
        if self.verbose:
            print(result)
        # сохраняем результат
        self.normalized_elements = result


    def normalize(self, element_or_elements: Union[str, List[str]]) -> Union[str, List[str]]:
        """
        Нормализует указанный элемент или список элементов.

        Этот метод использует механизм кэширования для повышения производительности. Если элемент был нормализован ранее,
        его нормализованная форма сохраняется в кэше (self.normalizing_map). Когда тот же элемент нужно нормализовать снова,
        метод сначала проверит кэш и использует сохраненную нормализованную форму, если она доступна,
        вместо того, чтобы нормализовать элемент снова.

        Порядок элементов в выводе будет таким же, как и во вводе. Это обеспечивается путем обработки
        элементов в том порядке, в котором они появляются во входных данных, и добавления нормализованных элементов в выходной
        список в том же порядке.

        :param element_or_elements: Элемент или список элементов для нормализации.
        :type element_or_elements: Union[str, List[str]]
        :return: Нормализованный элемент или список нормализованных элементов.
        :rtype: Union[str, List[str]]
        :raises ValueError: Если тип входных данных не является строкой или списком.
        """
        #  если element_or_elements - строка, то преобразуем её в список
        if isinstance(element_or_elements, str):
            denormalized_elements = [element_or_elements]
        #  если element_or_elements - список, то присваиваем его