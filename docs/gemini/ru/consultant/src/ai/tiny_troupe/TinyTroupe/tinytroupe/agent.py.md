# Анализ кода модуля `agent.py`

**Качество кода**

*   Соответствие требованиям по оформлению кода: 8/10
    *   **Плюсы:**
        *   Код хорошо структурирован, с разделением на логические блоки.
        *   Используются `logger` для логирования.
        *   Присутствуют docstrings для классов и методов.
        *   Используются `j_loads` и `j_loads_ns` (хотя в данном коде не используются напрямую, но они есть в `utils`)
        *   Присутствуют `@post_init`, `@transactional` декораторы.
        *   Используются `from src.logger.logger import logger`
    *   **Минусы:**
        *   Не все docstring соответствуют формату RST.
        *   Иногда используются комментарии `#`, которые не соответствуют reStructuredText
        *   Не все импорты отсортированы или сгруппированы (например, `logging`).
        *   Избыточное использование try-except (например, `_pretty_timestamp` или `pretty_current_interactions`).
        *   Некоторые функции не имеют документации или имеют неполную.
        *   Используются магические константы (например, 10000 в `retrieve_document_content_by_name`).
        *   В некоторых местах используется `print`, а не `logger` для вывода информации.

**Рекомендации по улучшению**

1.  **Документация:**
    *   Переписать все docstring в формате RST, используя :param:, :return: и другие директивы.
    *   Добавить docstring к методам и переменным, где они отсутствуют.
    *   Избегать общих фраз в комментариях, например, "код исполняет ...".
2.  **Импорты:**
    *   Сгруппировать и отсортировать импорты (стандартная библиотека, сторонние, локальные).
3.  **Логирование:**
    *   Заменить `print` на `logger` для вывода отладочной информации.
    *   Упростить try-except, где возможно, используя `logger.error` для обработки исключений.
4.  **Структура кода:**
    *   Разделить длинные функции на более мелкие и читаемые.
    *   Использовать константы для магических чисел.
    *   Улучшить форматирование строк с помощью f-strings.
5.  **Обработка ошибок:**
    *   Добавить обработку ошибок там, где это необходимо, и убедиться, что ошибки логируются.
6.  **Производительность:**
    *   Оптимизировать методы, которые могут вызывать снижение производительности (например, при большом количестве документов).

**Оптимизированный код**

```python
"""
Модуль для работы с агентами в TinyTroupe.
=========================================================================================

Этот модуль предоставляет основные классы и функции для агентов TinyTroupe.

Агенты являются ключевой абстракцией, используемой в TinyTroupe. Агент - это симулированный человек или сущность,
который может взаимодействовать с другими агентами и окружающей средой, получая стимулы и производя действия.
У агентов есть когнитивные состояния, которые обновляются по мере их взаимодействия с окружающей средой и другими агентами.
Агенты также могут хранить и извлекать информацию из памяти, а также могут выполнять действия в окружающей среде.
В отличие от агентов, чья цель - предоставлять поддержку для помощников на основе ИИ или других подобных инструментов повышения
производительности, **агенты TinyTroupe предназначены для представления человекоподобного поведения**, которое включает в себя
идиосинкразии, эмоции и другие человеческие черты, которых не ожидают от инструмента повышения производительности.

Общая базовая конструкция вдохновлена в основном когнитивной психологией, поэтому агенты имеют различные внутренние
когнитивные состояния, такие как внимание, эмоции и цели. Именно поэтому память агента, в отличие от других платформ агентов
на основе LLM, имеет тонкие внутренние разделения, особенно между эпизодической и семантической памятью.
Также присутствуют некоторые бихевиористские концепции, такие как идея "стимула" и "реакции" в методах
`listen` и `act`, которые являются ключевыми абстракциями для понимания того, как агенты взаимодействуют с окружающей средой и другими агентами.
"""

import os
import csv
import json
import ast
import textwrap  # to dedent strings
import datetime  # to get current datetime
import chevron  # to parse Mustache templates
import copy
from typing import Any, TypeVar, Union
import logging

from rich import print

from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader
from llama_index.readers.web import SimpleWebPageReader

from tinytroupe import openai_utils
import tinytroupe.utils as utils
from tinytroupe.utils import post_init, name_or_empty, break_text_at_length, repeat_on_error
from tinytroupe.control import transactional, current_simulation
from tinytroupe.utils import JsonSerializableRegistry

from src.logger.logger import logger

Self = TypeVar("Self", bound="TinyPerson")
AgentOrWorld = Union[Self, "TinyWorld"]

###########################################################################
# Default parameter values
###########################################################################
# We'll use various configuration elements below
config = utils.read_config_file()

default = {}
default["embedding_model"] = config["OpenAI"].get("EMBEDDING_MODEL", "text-embedding-3-small")
default["max_content_display_length"] = config["OpenAI"].getint("MAX_CONTENT_DISPLAY_LENGTH", 1024)


## LLaMa-Index configs ########################################################
# from llama_index.embeddings.huggingface import HuggingFaceEmbedding


# this will be cached locally by llama-index, in a OS-dependend location

##Settings.embed_model = HuggingFaceEmbedding(
##    model_name="BAAI/bge-small-en-v1.5"
##)

llmaindex_openai_embed_model = OpenAIEmbedding(model=default["embedding_model"], embed_batch_size=10)
Settings.embed_model = llmaindex_openai_embed_model
###############################################################################


#######################################################################################################################
# TinyPerson itself
#######################################################################################################################
@post_init
class TinyPerson(JsonSerializableRegistry):
    """
    Представляет симулированного человека во вселенной TinyTroupe.

    :ivar MAX_ACTIONS_BEFORE_DONE: Максимальное количество действий, которые агент может выполнить до завершения.
    :vartype MAX_ACTIONS_BEFORE_DONE: int
    :ivar PP_TEXT_WIDTH: Ширина текста для красивого вывода.
    :vartype PP_TEXT_WIDTH: int
    :ivar serializable_attributes: Список атрибутов, которые можно сериализовать в JSON.
    :vartype serializable_attributes: list
    :ivar all_agents: Словарь всех созданных агентов (имя -> агент).
    :vartype all_agents: dict
    :ivar communication_style: Стиль общения агентов ("simplified" или "full").
    :vartype communication_style: str
    :ivar communication_display: Флаг, определяющий, отображать ли общение (True для интерактивных приложений).
    :vartype communication_display: bool
    """
    # The maximum number of actions that an agent is allowed to perform before DONE.
    # This prevents the agent from acting without ever stopping.
    MAX_ACTIONS_BEFORE_DONE = 15

    PP_TEXT_WIDTH = 100

    serializable_attributes = ["name", "episodic_memory", "semantic_memory", "_mental_faculties", "_configuration"]

    # A dict of all agents instantiated so far.
    all_agents = {}  # name -> agent

    # The communication style for all agents: "simplified" or "full".
    communication_style:str="simplified"
    
    # Whether to display the communication or not. True is for interactive applications, when we want to see simulation
    # outputs as they are produced.
    communication_display:bool=True
    

    def __init__(self, name:str=None, 
                 episodic_memory=None,
                 semantic_memory=None,
                 mental_faculties:list=None):
        """
        Создает экземпляр TinyPerson.

        :param name: Имя TinyPerson.
        :type name: str
        :param episodic_memory: Реализация эпизодической памяти.
        :type episodic_memory: EpisodicMemory, optional
        :param semantic_memory: Реализация семантической памяти.
        :type semantic_memory: SemanticMemory, optional
        :param mental_faculties: Список умственных способностей агента.
        :type mental_faculties: list, optional
        """

        # NOTE: default values will be given in the _post_init method, as that\'s shared by 
        #       direct initialization as well as via deserialization.

        if episodic_memory is not None:
            self.episodic_memory = episodic_memory
        
        if semantic_memory is not None:
            self.semantic_memory = semantic_memory

        # Mental faculties
        if mental_faculties is not None:
            self._mental_faculties = mental_faculties
        
        assert name is not None, "A TinyPerson must have a name."
        self.name = name

        # @post_init makes sure that _post_init is called after __init__

    
    def _post_init(self, **kwargs):
        """
        Выполняется после __init__, так как класс имеет декоратор @post_init.
        Удобно разделять некоторые процессы инициализации, чтобы упростить десериализацию.
        """

        ############################################################
        # Default values
        ############################################################

        self.current_messages = []
        
        # the current environment in which the agent is acting
        self.environment = None

        # The list of actions that this agent has performed so far, but which have not been
        # consumed by the environment yet.
        self._actions_buffer = []

        # The list of agents that this agent can currently interact with.
        # This can change over time, as agents move around the world.
        self._accessible_agents = []

        # the buffer of communications that have been displayed so far, used for
        # saving these communications to another output form later (e.g., caching)
        self._displayed_communications_buffer = []

        if not hasattr(self, 'episodic_memory'):
            # This default value MUST NOT be in the method signature, otherwise it will be shared across all instances.
            self.episodic_memory = EpisodicMemory()
        
        if not hasattr(self, 'semantic_memory'):
            # This default value MUST NOT be in the method signature, otherwise it will be shared across all instances.
            self.semantic_memory = SemanticMemory()
        
        # _mental_faculties
        if not hasattr(self, '_mental_faculties'):
            # This default value MUST NOT be in the method signature, otherwise it will be shared across all instances.
            self._mental_faculties = []

        # create the configuration dictionary
        if not hasattr(self, '_configuration'):          
            self._configuration = {
                "name": self.name,
                "age": None,
                "nationality": None,
                "country_of_residence": None,
                "occupation": None,
                "routines": [],
                "occupation_description": None,
                "personality_traits": [],
                "professional_interests": [],
                "personal_interests": [],
                "skills": [],
                "relationships": [],
                "current_datetime": None,
                "current_location": None,
                "current_context": [],
                "current_attention": None,
                "current_goals": [],
                "current_emotions": "Currently you feel calm and friendly.",
                "currently_accessible_agents": [],  # [{"agent": agent_1, "relation": "My friend"}, {"agent": agent_2, "relation": "My colleague"}, ...]
            }

        self._prompt_template_path = os.path.join(
            os.path.dirname(__file__), "prompts/tinyperson.mustache"
        )
        self._init_system_message = None  # initialized later


        ############################################################
        # Special mechanisms used during deserialization
        ############################################################

        # rename agent to some specific name?
        if kwargs.get("new_agent_name") is not None:
            self._rename(kwargs.get("new_agent_name"))
        
        # If auto-rename, use the given name plus some new number ...
        if kwargs.get("auto_rename") is True:
            new_name = self.name # start with the current name
            rename_succeeded = False
            while not rename_succeeded:
                try:
                    self._rename(new_name)
                    TinyPerson.add_agent(self)
                    rename_succeeded = True                
                except ValueError:
                    new_id = utils.fresh_id()
                    new_name = f"{self.name}_{new_id}"
        
        # ... otherwise, just register the agent
        else:
            # register the agent in the global list of agents
            TinyPerson.add_agent(self)

        # start with a clean slate
        self.reset_prompt()

        # it could be the case that the agent is being created within a simulation scope, in which case
        # the simulation_id must be set accordingly
        if current_simulation() is not None:
            current_simulation().add_agent(self)
        else:
            self.simulation_id = None
    
    def _rename(self, new_name:str):
        """
        Переименовывает агента.

        :param new_name: Новое имя агента.
        :type new_name: str
        """    
        self.name = new_name
        self._configuration["name"] = self.name


    def generate_agent_prompt(self):
        """
        Генерирует промпт агента на основе шаблона и конфигурации.

        :return: Сгенерированный промпт агента.
        :rtype: str
        """
        with open(self._prompt_template_path, "r") as f:
            agent_prompt_template = f.read()

        # let\'s operate on top of a copy of the configuration, because we\'ll need to add more variables, etc.
        template_variables = self._configuration.copy()    

        # Prepare additional action definitions and constraints
        actions_definitions_prompt = ""
        actions_constraints_prompt = ""
        for faculty in self._mental_faculties:
            actions_definitions_prompt += f"{faculty.actions_definitions_prompt()}\\n"
            actions_constraints_prompt += f"{faculty.actions_constraints_prompt()}\\n"
        
        # make the additional prompt pieces available to the template
        template_variables['actions_definitions_prompt'] = textwrap.indent(actions_definitions_prompt, "")
        template_variables['actions_constraints_prompt'] = textwrap.indent(actions_constraints_prompt, "")

        # RAI prompt components, if requested
        template_variables = utils.add_rai_template_variables_if_enabled(template_variables)

        return chevron.render(agent_prompt_template, template_variables)

    def reset_prompt(self):
        """
        Сбрасывает промпт агента, перегенерируя его с текущей конфигурацией и эпизодической памятью.
        """

        # render the template with the current configuration
        self._init_system_message = self.generate_agent_prompt()

        # TODO actually, figure out another way to update agent state without "changing history"

        # reset system message
        self.current_messages = [
            {"role": "system", "content": self._init_system_message}
        ]

        # sets up the actual interaction messages to use for prompting
        self.current_messages += self.episodic_memory.retrieve_recent()

    def get(self, key):
        """
        Возвращает значение ключа из конфигурации TinyPerson.

        :param key: Ключ для поиска значения.
        :type key: str
        :return: Значение ключа или None, если ключ не найден.
        :rtype: Any
        """
        return self._configuration.get(key, None)
    
    @transactional
    def define(self, key, value, group=None):
        """
        Определяет значение в конфигурации TinyPerson.

        :param key: Ключ для определения.
        :type key: str
        :param value: Значение для ключа.
        :type value: Any
        :param group: Группа, к которой добавить значение (необязательно).
        :type group: str, optional
        """

        # dedent value if it is a string
        if isinstance(value, str):
            value = textwrap.dedent(value)

        if group is None:
            # logger.debug(f"[{self.name}] Defining {key}={value} in the person.")
            self._configuration[key] = value
        else:
            if key is not None:
                # logger.debug(f"[{self.name}] Adding definition to {group} += [ {key}={value} ] in the person.")
                self._configuration[group].append({key: value})
            else:
                # logger.debug(f"[{self.name}] Adding definition to {group} += [ {value} ] in the person.")
                self._configuration[group].append(value)

        # must reset prompt after adding to configuration
        self.reset_prompt()

    def define_several(self, group, records):
        """
        Определяет несколько значений в конфигурации TinyPerson, принадлежащих к одной группе.

        :param group: Группа, к которой добавить значения.
        :type group: str
        :param records: Список записей для добавления.
        :type records: list
        """
        for record in records:
            self.define(key=None, value=record, group=group)
    
    @transactional
    def define_relationships(self, relationships, replace=True):
        """
        Определяет или обновляет отношения TinyPerson.

        :param relationships: Отношения для добавления или замены.
        :type relationships: list or dict
        :param replace: Флаг, определяющий, заменять ли текущие отношения или просто добавлять к ним.
        :type replace: bool, optional
        :raises Exception: Если аргументы недействительны.
        """
        
        if (replace == True) and (isinstance(relationships, list)):
            self._configuration['relationships'] = relationships

        elif replace == False:
            current_relationships = self._configuration['relationships']
            if isinstance(relationships, list):
                for r in relationships:
                    current_relationships.append(r)
                
            elif isinstance(relationships, dict) and len(relationships) == 2: #{"Name": ..., "Description": ...}
                current_relationships.append(relationships)

            else:
                raise Exception("Only one key-value pair is allowed in the relationships dict.")

        else:
            raise Exception("Invalid arguments for define_relationships.")

    @transactional
    def clear_relationships(self):
        """
        Очищает отношения TinyPerson.

        :return: TinyPerson, для поддержки цепочек вызовов.
        :rtype: TinyPerson
        """
        self._configuration['relationships'] = []  

        return self      
    
    @transactional
    def related_to(self, other_agent, description, symmetric_description=None):
        """
        Определяет отношение между этим агентом и другим агентом.

        :param other_agent: Другой агент.
        :type other_agent: TinyPerson
        :param description: Описание отношения.
        :type description: str
        :param symmetric_description: Симметричное описание отношения (необязательно).
        :type symmetric_description: str, optional
        :return: Агент, для поддержки цепочек вызовов.
        :rtype: TinyPerson
        """
        self.define_relationships([{"Name": other_agent.name, "Description": description}], replace=False)
        if symmetric_description is not None:
            other_agent.define_relationships([{"Name": self.name, "Description": symmetric_description}], replace=False)
        
        return self
    
    def add_mental_faculties(self, mental_faculties):
        """
        Добавляет список умственных способностей к агенту.

        :param mental_faculties: Список умственных способностей.
        :type mental_faculties: list
        :return: Агент, для поддержки цепочек вызовов.
        :rtype: TinyPerson
        """
        for faculty in mental_faculties:
            self.add_mental_faculty(faculty)
        
        return self

    def add_mental_faculty(self, faculty):
        """
        Добавляет умственную способность к агенту.

        :param faculty: Умственная способность для добавления.
        :type faculty: TinyMentalFaculty
        :raises Exception: Если умственная способность уже существует у агента.
        :return: Агент, для поддержки цепочек вызовов.
        :rtype: TinyPerson
        """
        # check if the faculty is already there or not
        if faculty not in self._mental_faculties:
            self._mental_faculties.append(faculty)
        else:
            raise Exception(f"The mental faculty {faculty} is already present in the agent.")
        
        return self

    @transactional
    def act(
        self,
        until_done=True,
        n=None,
        return_actions=False,
        max_content_length=default["max_content_display_length"],
    ):
        """
        Действует в окружающей среде и обновляет свое внутреннее когнитивное состояние.

        :param until_done: Флаг, определяющий, действовать ли до завершения и необходимости дополнительных стимулов.
        :type until_done: bool
        :param n: Количество действий для выполнения.
        :type n: int, optional
        :param return_actions: Флаг, определяющий, возвращать ли действия.
        :type return_actions: bool, optional
        :raises AssertionError: Если `until_done` и `n` одновременно не None.
        :return: Список действий, если `return_actions` True.
        :rtype: list, optional
        """

        # either act until done or act a fixed number of times, but not both
        assert not (until_done and n is not None)
        if n is not None:
            assert n < TinyPerson.MAX_ACTIONS_BEFORE_DONE

        contents = []

        # Aux function to perform exactly one action.
        # Occasionally, the model will return JSON missing important keys, so we just ask it to try again
        @repeat_on_error(retries=5, exceptions=[KeyError])
        def aux_act_once():
            """
            Вспомогательная функция для выполнения одного действия.
            """
            # A quick thought before the action. This seems to help with better model responses, perhaps because
            # it interleaves user with assistant messages.
            self.think("I will now act a bit, and then issue DONE.")

          
            role, content = self._produce_message()

            self.episodic_memory.store({'role': role, 'content': content, 'simulation_timestamp': self.iso_datetime()})

            cognitive_state = content["cognitive_state"]


            action = content['action']

            self._actions_buffer.append(action)
            self._update_cognitive_state(goals=cognitive_state['goals'],
                                        attention=cognitive_state['attention'],
                                        emotions=cognitive_state['emotions'])
            
            contents.append(content)          
            if TinyPerson.communication_display:
                self._display_communication(role=role, content=content, kind='action', simplified=True, max_content_length=max_content_length)
            
            #
            # Some actions induce an immediate stimulus or other side-effects. We need to process them here, by means of the mental faculties.
            #
            for faculty in self._mental_faculties:
                faculty.process_action(self, action)             
            

        #
        # How to proceed with a sequence of actions.
        #
        ##### Option 1: run N actions ######
        if n is not None:
            for i in range(n):
                aux_act_once()

        ##### Option 2: run until DONE ######
        elif until_done:
            while (len(contents) == 0) or (
                not contents[-1]["action"]["type"] == "DONE"
            ):


                # check if the agent is acting without ever stopping
                if len(contents) > TinyPerson.MAX_ACTIONS_BEFORE_DONE:
                    logger.warning(f"[{self.name}] Agent {self.name} is acting without ever stopping. This may be a bug. Let\'s stop it here anyway.")
                    break
                if len(contents) > 4: # just some minimum number of actions to check for repetition, could be anything >= 3
                    # if the last three actions were the same, then we are probably in a loop
                    if contents[-1]['action'] == contents[-2]['action'] == contents[-3]['action']:
                        logger.warning(f"[{self.name}] Agent {self.name} is acting in a loop. This may be a bug. Let\'s stop it here anyway.")
                        break

                aux_act_once()

        if return_actions:
            return contents

    @transactional
    def listen(
        self,
        speech,
        source: AgentOrWorld = None,
        max_content_length=default["max_content_display_length"],
    ):
        """
        Слушает другого агента (искусственного или человека) и обновляет свое внутреннее когнитивное состояние.

        :param speech: Речь для прослушивания.
        :type speech: str
        :param source: Источник речи.
        :type source: AgentOrWorld, optional
        :return: Агент, для поддержки цепочек вызовов.
        :rtype: TinyPerson
        """

        return self._observe(
            stimulus={
                "type": "CONVERSATION",
                "content": speech,
                "source": name_or_empty(source),
            },
            max_content_length=max_content_length,
        )

    def socialize(
        self,
        social_description: str,
        source: AgentOrWorld = None,
        max_content_length=default["max_content_display_length"],
    ):
        """
        Воспринимает социальный стимул через описание и обновляет свое внутреннее когнитивное состояние.

        :param social_description: Описание социального стимула.
        :type social_description: str
        :param source: Источник социального стимула.
        :type source: AgentOrWorld, optional
         :return: Агент, для поддержки цепочек вызовов.
        :rtype: TinyPerson
        """
        return self._observe(
            stimulus={
                "type": "SOCIAL",
                "content": social_description,
                "source": name_or_empty(source),
            },
            max_content_length=max_content_length,
        )

    def see(
        self,
        visual_description,
        source: AgentOrWorld = None,
        max_content_length=default["max_content_display_length"],
    ):
        """
        Воспринимает визуальный стимул через описание и обновляет свое внутреннее когнитивное состояние.

        :param visual_description: Описание визуального стимула.
        :type visual_description: str
        :param source: Источник визуального стимула.
        :type source: AgentOrWorld, optional
        :return: Агент, для поддержки цепочек вызовов.
        :rtype: TinyPerson
        """
        return self._observe(
            stimulus={
                "type": "VISUAL",
                "content": visual_description,
                "source": name_or_empty(source),
            },
            max_content_length=max_content_length,
        )

    def think(self, thought, max_content_length=default["max_content_display_length"]):
        """
        Заставляет агента думать о чем-то и обновляет свое внутреннее когнитивное состояние.

        :param thought: Мысль для обдумывания.
        :type thought: str
         :return: Агент, для поддержки цепочек вызовов.
        :rtype: TinyPerson
        """
        return self._observe(
            stimulus={
                "type": "THOUGHT",
                "content": thought,
                "source": name_or_empty(self),
            },
            max_content_length=max_content_length,
        )

    def internalize_goal(
        self, goal, max_content_length=default["max_content_display_length"]
    ):
        """
        Интернализирует цель и обновляет свое внутреннее когнитивное состояние.

        :param goal: Цель для интернализации.
        :type goal: str
         :return: Агент, для поддержки цепочек вызовов.
        :rtype: TinyPerson
        """
        return self._observe(
            stimulus={
                "type": "INTERNAL_GOAL_FORMULATION",
                "content": goal,
                "source": name_or_empty(self),
            },
            max_content_length=max_content_length,
        )

    @transactional
    def _observe(self, stimulus, max_content_length=default["max_content_display_length"]):
        """
        Наблюдает за стимулом и обновляет внутреннее когнитивное состояние.

        :param stimulus: Стимул для наблюдения.
        :type stimulus: dict
         :return: Агент, для поддержки цепочек вызовов.
        :rtype: TinyPerson
        """
        stimuli = [stimulus]

        content = {"stimuli": stimuli}

        logger.debug(f"[{self.name}] Observing stimuli: {content}")

        # whatever comes from the outside will be interpreted as coming from 'user', simply because
        # this is the counterpart of 'assistant'

        self.episodic_memory.store({'role': 'user', 'content': content, 'simulation_timestamp': self.iso_datetime()})

        if TinyPerson.communication_display:
            self._display_communication(
                role="user",
                content=content,
                kind="stimuli",
                simplified=True,
                max_content_length=max_content_length,
            )

        return self  # allows easier chaining of methods

    @transactional
    def listen_and_act(
        self,
        speech,
        return_actions=False,
        max_content_length=default["max_content_display_length"],
    ):
        """
        Удобный метод, который объединяет методы `listen` и `act`.

        :param speech: Речь для прослушивания.
        :type speech: str
        :param return_actions: Флаг, определяющий, возвращать ли действия.
        :type return_actions: bool, optional
        :return: Список действий, если `return_actions` True.
        :rtype: list, optional
        """

        self.listen(speech, max_content_length=max_content_length)
        return self.act(
            return_actions=return_actions, max_content_length=max_content_length
        )

    @transactional
    def see_and_act(
        self,
        visual_description,
        return_actions=False,
        max_content_length=default["max_content_display_length"],
    ):
        """
        Удобный метод, который объединяет методы `see` и `act`.

        :param visual_description: Описание визуального стимула.
        :type visual_description: str
        :param return_actions: Флаг, определяющий, возвращать ли действия.
        :type return_actions: bool, optional
        :return: Список действий, если `return_actions` True.
        :rtype: list, optional
        """

        self.see(visual_description, max_content_length=max_content_length)
        return self.act(
            return_actions=return_actions, max_content_length=max_content_length
        )

    @transactional
    def think_and_act(
        self,
        thought,
        return_actions=False,
        max_content_length=default["max_content_display_length"],
    ):
        """
        Удобный метод, который объединяет методы `think` и `act`.

        :param thought: Мысль для обдумывания.
        :type thought: str
        :param return_actions: Флаг, определяющий, возвращать ли действия.
        :type return_actions: bool, optional
        :return: Список действий, если `return_actions` True.
        :rtype: list, optional
        """

        self.think(thought, max_content_length=max_content_length)
        return self.act(return_actions=return_actions, max_content_length=max_content_length)

    def read_documents_from_folder(self, documents_path:str):
        """
        Считывает документы из папки и загружает их в семантическую память.

        :param documents_path: Путь к папке с документами.
        :type documents_path: str
        """
        logger.info(f"Setting documents path to {documents_path} and loading documents.")

        self.semantic_memory.add_documents_path(documents_path)
    
    def read_documents_from_web(self, web_urls:list):
        """
        Считывает документы из веб-URL и загружает их в семантическую память.

        :param web_urls: Список веб-URL.
        :type web_urls: list
        """
        logger.info(f"Reading documents from the following web URLs: {web_urls}")

        self.semantic_memory.add_web_urls(web_urls)
    
    @transactional
    def move_to(self, location, context=[]):
        """
        Перемещается в новое местоположение и обновляет свое внутреннее когнитивное состояние.

        :param location: Новое местоположение.
        :type location: str