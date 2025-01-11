### Анализ кода модуля `agent`

**Качество кода**:

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Хорошо структурированный код с использованием классов для представления агентов и их ментальных способностей.
    - Применение декораторов `@post_init` и `@transactional` для управления жизненным циклом и транзакциями агентов.
    - Использование `rich` для форматированного вывода.
    - Реализация механизмов памяти (эпизодической и семантической) для агентов.
- **Минусы**:
    -  Непоследовательное использование кавычек (в основном используются двойные кавычки для строк, вместо одинарных).
    -  Отсутствует  `from src.logger.logger import logger` для логирования ошибок, используется  `import logging` и `logger = logging.getLogger("tinytroupe")`.
    -  Использование стандартного `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -  Смешанное использование комментариев `#` и `"""` для документирования.
    -  Многословные комментарии, которые можно сократить.
    -  Не хватает RST-документации для функций и методов.

**Рекомендации по улучшению**:

-   Привести все строки кода к использованию одинарных кавычек (`'`).
-   Заменить `import logging` на `from src.logger.logger import logger`.
-   Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для обработки JSON.
-   Заменить все  `"""` на RST-комментарии для документирования функций, методов и классов.
-   Использовать более точные формулировки в комментариях.
-   Удалить  ненужные комментарии, сосредоточившись на более содержательных описаниях.
-   Добавить RST-документацию для всех функций, методов и классов.
-   Соблюдать стандарты PEP8 для улучшения читаемости кода.
-   Избегать чрезмерного использования стандартных блоков `try-except`.

**Оптимизированный код**:

```python
"""
Модуль предоставляет основные классы и функции для агентов TinyTroupe.
===================================================================

Агенты являются ключевой абстракцией, используемой в TinyTroupe. Агент — это имитированный человек или сущность,
которая может взаимодействовать с другими агентами и средой, получая стимулы и производя действия.
Агенты имеют когнитивные состояния, которые обновляются по мере их взаимодействия со средой и другими агентами.
Агенты также могут хранить и извлекать информацию из памяти, а также выполнять действия в среде.
В отличие от агентов, целью которых является обеспечение поддержки ассистентов на основе ИИ или других подобных инструментов
повышения производительности, **агенты TinyTroupe нацелены на представление человекоподобного поведения**,
которое включает в себя идиосинкразии, эмоции и другие человекоподобные черты, которых не ожидают от инструмента повышения
производительности.

Общая лежащая в основе конструкция вдохновлена в основном когнитивной психологией, поэтому агенты имеют
различные внутренние когнитивные состояния, такие как внимание, эмоции и цели.
Именно поэтому память агента, в отличие от других платформ агентов на основе LLM, имеет тонкие внутренние
разделения, в частности, между эпизодической и семантической памятью.
Также присутствуют некоторые бихевиористские концепции, такие как идея «стимула» и «реакции» в методах
`listen` и `act`, которые являются ключевыми абстракциями для понимания того, как агенты взаимодействуют
со средой и другими агентами.
"""
import os
import textwrap  # to dedent strings
import datetime  # to get current datetime
import chevron  # to parse Mustache templates
import copy
from typing import Any, TypeVar, Union
from pathlib import Path

from src.logger.logger import logger # Изменено: импорт logger
import tinytroupe.utils as utils
from tinytroupe.utils import post_init, j_loads  # Изменено: импорт j_loads
from tinytroupe.control import transactional
from tinytroupe.control import current_simulation
from rich import print
from tinytroupe.utils import JsonSerializableRegistry

Self = TypeVar('Self', bound='TinyPerson')
AgentOrWorld = Union[Self, 'TinyWorld']

###########################################################################
# Default parameter values
###########################################################################
# We'll use various configuration elements below
config = utils.read_config_file()

default = {}
default['embedding_model'] = config['OpenAI'].get('EMBEDDING_MODEL', 'text-embedding-3-small')
default['max_content_display_length'] = config['OpenAI'].getint('MAX_CONTENT_DISPLAY_LENGTH', 1024)


## LLaMa-Index configs ########################################################
#from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader
from llama_index.readers.web import SimpleWebPageReader


# this will be cached locally by llama-index, in a OS-dependend location

##Settings.embed_model = HuggingFaceEmbedding(
##    model_name="BAAI/bge-small-en-v1.5"
##)

llmaindex_openai_embed_model = OpenAIEmbedding(model=default['embedding_model'], embed_batch_size=10)
Settings.embed_model = llmaindex_openai_embed_model
###############################################################################


from tinytroupe import openai_utils
from tinytroupe.utils import name_or_empty, break_text_at_length, repeat_on_error


#######################################################################################################################
# TinyPerson itself
#######################################################################################################################
@post_init
class TinyPerson(JsonSerializableRegistry):
    """
    Представляет собой имитированного человека во вселенной TinyTroupe.
    
    :cvar MAX_ACTIONS_BEFORE_DONE: Максимальное количество действий, которое может выполнить агент до завершения.
    :vartype MAX_ACTIONS_BEFORE_DONE: int
    :cvar PP_TEXT_WIDTH: Ширина текста для форматированного вывода.
    :vartype PP_TEXT_WIDTH: int
    :cvar serializable_attributes: Список сериализуемых атрибутов.
    :vartype serializable_attributes: list[str]
    :cvar all_agents: Словарь всех созданных агентов (имя -> агент).
    :vartype all_agents: dict[str, TinyPerson]
    :cvar communication_style: Стиль общения агента ('simplified' или 'full').
    :vartype communication_style: str
    :cvar communication_display: Флаг, определяющий, выводить ли сообщения в консоль.
    :vartype communication_display: bool
    """

    # The maximum number of actions that an agent is allowed to perform before DONE.
    # This prevents the agent from acting without ever stopping.
    MAX_ACTIONS_BEFORE_DONE = 15

    PP_TEXT_WIDTH = 100

    serializable_attributes = ['name', 'episodic_memory', 'semantic_memory', '_mental_faculties', '_configuration']

    # A dict of all agents instantiated so far.
    all_agents = {}  # name -> agent

    # The communication style for all agents: "simplified" or "full".
    communication_style:str='simplified'
    
    # Whether to display the communication or not. True is for interactive applications, when we want to see simulation
    # outputs as they are produced.
    communication_display:bool=True
    

    def __init__(self, name:str=None, 
                 episodic_memory=None,
                 semantic_memory=None,
                 mental_faculties:list=None):
        """
        Инициализирует объект TinyPerson.

        :param name: Имя агента.
        :type name: str, optional
        :param episodic_memory: Реализация эпизодической памяти.
        :type episodic_memory: EpisodicMemory, optional
        :param semantic_memory: Реализация семантической памяти.
        :type semantic_memory: SemanticMemory, optional
        :param mental_faculties: Список ментальных способностей агента.
        :type mental_faculties: list, optional
        """

        # NOTE: default values will be given in the _post_init method, as that's shared by 
        #       direct initialization as well as via deserialization.

        if episodic_memory is not None:
            self.episodic_memory = episodic_memory
        
        if semantic_memory is not None:
            self.semantic_memory = semantic_memory

        # Mental faculties
        if mental_faculties is not None:
            self._mental_faculties = mental_faculties
        
        assert name is not None, 'A TinyPerson must have a name.'
        self.name = name

        # @post_init makes sure that _post_init is called after __init__

    
    def _post_init(self, **kwargs):
        """
        Выполняет постобработку после инициализации объекта.

        Этот метод вызывается после __init__ благодаря декоратору @post_init.
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
                'name': self.name,
                'age': None,
                'nationality': None,
                'country_of_residence': None,
                'occupation': None,
                'routines': [],
                'occupation_description': None,
                'personality_traits': [],
                'professional_interests': [],
                'personal_interests': [],
                'skills': [],
                'relationships': [],
                'current_datetime': None,
                'current_location': None,
                'current_context': [],
                'current_attention': None,
                'current_goals': [],
                'current_emotions': 'Currently you feel calm and friendly.',
                'currently_accessible_agents': [],  # [{'agent': agent_1, 'relation': 'My friend'}, {'agent': agent_2, 'relation': 'My colleague'}, ...]
            }

        self._prompt_template_path = os.path.join(
            os.path.dirname(__file__), 'prompts/tinyperson.mustache'
        )
        self._init_system_message = None  # initialized later


        ############################################################
        # Special mechanisms used during deserialization
        ############################################################

        # rename agent to some specific name?
        if kwargs.get('new_agent_name') is not None:
            self._rename(kwargs.get('new_agent_name'))
        
        # If auto-rename, use the given name plus some new number ...
        if kwargs.get('auto_rename') is True:
            new_name = self.name # start with the current name
            rename_succeeded = False
            while not rename_succeeded:
                try:
                    self._rename(new_name)
                    TinyPerson.add_agent(self)
                    rename_succeeded = True                
                except ValueError:
                    new_id = utils.fresh_id()
                    new_name = f'{self.name}_{new_id}'
        
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
        self._configuration['name'] = self.name


    def generate_agent_prompt(self):
        """
        Генерирует промпт для агента на основе шаблона.

        :return: Строка промпта.
        :rtype: str
        """
        with open(self._prompt_template_path, 'r') as f:
            agent_prompt_template = f.read()

        # let's operate on top of a copy of the configuration, because we'll need to add more variables, etc.
        template_variables = self._configuration.copy()
    
        # Prepare additional action definitions and constraints
        actions_definitions_prompt = ''
        actions_constraints_prompt = ''
        for faculty in self._mental_faculties:
            actions_definitions_prompt += f'{faculty.actions_definitions_prompt()}\\n'
            actions_constraints_prompt += f'{faculty.actions_constraints_prompt()}\\n'
        
        # make the additional prompt pieces available to the template
        template_variables['actions_definitions_prompt'] = textwrap.indent(actions_definitions_prompt, '')
        template_variables['actions_constraints_prompt'] = textwrap.indent(actions_constraints_prompt, '')

        # RAI prompt components, if requested
        template_variables = utils.add_rai_template_variables_if_enabled(template_variables)

        return chevron.render(agent_prompt_template, template_variables)

    def reset_prompt(self):
        """
        Сбрасывает промпт агента к начальному состоянию.
        """

        # render the template with the current configuration
        self._init_system_message = self.generate_agent_prompt()

        # TODO actually, figure out another way to update agent state without "changing history"

        # reset system message
        self.current_messages = [
            {'role': 'system', 'content': self._init_system_message}
        ]

        # sets up the actual interaction messages to use for prompting
        self.current_messages += self.episodic_memory.retrieve_recent()

    def get(self, key):
        """
        Возвращает значение ключа из конфигурации агента.

        :param key: Ключ для поиска.
        :type key: str
        :return: Значение ключа или None, если ключ не найден.
        :rtype: Any
        """
        return self._configuration.get(key, None)
    
    @transactional
    def define(self, key, value, group=None):
        """
        Определяет или обновляет значение в конфигурации агента.

        :param key: Ключ для определения.
        :type key: str
        :param value: Значение для сохранения.
        :type value: Any
        :param group: Группа, к которой принадлежит ключ.
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
        Определяет несколько значений в конфигурации агента в одной группе.

        :param group: Группа, к которой принадлежат значения.
        :type group: str
        :param records: Список записей для добавления в группу.
        :type records: list
        """
        for record in records:
            self.define(key=None, value=record, group=group)
    
    @transactional
    def define_relationships(self, relationships, replace=True):
        """
        Определяет или обновляет отношения агента с другими агентами.

        :param relationships: Отношения для добавления или замены.
        :type relationships: list | dict
        :param replace: Флаг, указывающий, нужно ли заменять существующие отношения.
        :type replace: bool, optional
        :raises Exception: Если аргументы неверны.
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
                raise Exception('Only one key-value pair is allowed in the relationships dict.')

        else:
            raise Exception('Invalid arguments for define_relationships.')

    @transactional
    def clear_relationships(self):
        """
        Очищает список отношений агента.

        :return: Агент.
        :rtype: TinyPerson
        """
        self._configuration['relationships'] = []
        return self
    
    @transactional
    def related_to(self, other_agent, description, symmetric_description=None):
        """
        Устанавливает связь между двумя агентами.

        :param other_agent: Другой агент.
        :type other_agent: TinyPerson
        :param description: Описание отношений.
        :type description: str
        :param symmetric_description: Описание симметричных отношений.
        :type symmetric_description: str, optional
        :return: Агент.
        :rtype: TinyPerson
        """
        self.define_relationships([{'Name': other_agent.name, 'Description': description}], replace=False)
        if symmetric_description is not None:
            other_agent.define_relationships([{'Name': self.name, 'Description': symmetric_description}], replace=False)
        
        return self
    
    def add_mental_faculties(self, mental_faculties):
        """
        Добавляет список ментальных способностей агенту.

        :param mental_faculties: Список ментальных способностей.
        :type mental_faculties: list
        :return: Агент.
        :rtype: TinyPerson
        """
        for faculty in mental_faculties:
            self.add_mental_faculty(faculty)
        
        return self

    def add_mental_faculty(self, faculty):
        """
        Добавляет ментальную способность агенту.

        :param faculty: Ментальная способность для добавления.
        :type faculty: TinyMentalFaculty
        :return: Агент.
        :rtype: TinyPerson
        :raises Exception: Если ментальная способность уже присутствует.
        """
        # check if the faculty is already there or not
        if faculty not in self._mental_faculties:
            self._mental_faculties.append(faculty)
        else:
            raise Exception(f'The mental faculty {faculty} is already present in the agent.')
        
        return self

    @transactional
    def act(
        self,
        until_done=True,
        n=None,
        return_actions=False,
        max_content_length=default['max_content_display_length'],
    ):
        """
        Выполняет действия агента в среде и обновляет его когнитивное состояние.

        :param until_done: Выполнять действия, пока агент не завершит работу и не потребуются дополнительные стимулы.
        :type until_done: bool, optional
        :param n: Количество действий для выполнения.
        :type n: int, optional
        :param return_actions: Флаг, указывающий, нужно ли возвращать действия.
        :type return_actions: bool, optional
        :param max_content_length: Максимальная длина выводимого контента.
        :type max_content_length: int, optional
        :return: Список действий, если `return_actions` равен True, иначе None.
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
            # A quick thought before the action. This seems to help with better model responses, perhaps because
            # it interleaves user with assistant messages.
            self.think('I will now act a bit, and then issue DONE.')

          
            role, content = self._produce_message()

            self.episodic_memory.store({'role': role, 'content': content, 'simulation_timestamp': self.iso_datetime()})

            cognitive_state = content['cognitive_state']


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
                not contents[-1]['action']['type'] == 'DONE'
            ):


                # check if the agent is acting without ever stopping
                if len(contents) > TinyPerson.MAX_ACTIONS_BEFORE_DONE:
                    logger.warning(f'[{self.name}] Agent {self.name} is acting without ever stopping. This may be a bug. Let\'s stop it here anyway.')
                    break
                if len(contents) > 4: # just some minimum number of actions to check for repetition, could be anything >= 3
                    # if the last three actions were the same, then we are probably in a loop
                    if contents[-1]['action'] == contents[-2]['action'] == contents[-3]['action']:
                        logger.warning(f'[{self.name}] Agent {self.name} is acting in a loop. This may be a bug. Let\'s stop it here anyway.')
                        break

                aux_act_once()

        if return_actions:
            return contents

    @transactional
    def listen(
        self,
        speech,
        source: AgentOrWorld = None,
        max_content_length=default['max_content_display_length'],
    ):
        """
        Слушает речь другого агента или мира и обновляет свое внутреннее когнитивное состояние.

        :param speech: Речь для прослушивания.
        :type speech: str
        :param source: Источник речи.
        :type source: AgentOrWorld, optional
        :param max_content_length: Максимальная длина выводимого контента.
        :type max_content_length: int, optional
        :return: Агент.
        :rtype: TinyPerson
        """

        return self._observe(
            stimulus={
                'type': 'CONVERSATION',
                'content': speech,
                'source': name_or_empty(source),
            },
            max_content_length=max_content_length,
        )

    def socialize(
        self,
        social_description: str,
        source: AgentOrWorld = None,
        max_content_length=default['max_content_display_length'],
    ):
        """
        Воспринимает социальный стимул через описание и обновляет свое внутреннее когнитивное состояние.

        :param social_description: Описание социального стимула.
        :type social_description: str
        :param source: Источник социального стимула.
        :type source: AgentOrWorld, optional
        :param max_content_length: Максимальная длина выводимого контента.
        :type max_content_length: int, optional
        :return: Агент.
        :rtype: TinyPerson
        """
        return self._observe(
            stimulus={
                'type': 'SOCIAL',
                'content': social_description,
                'source': name_or_empty(source),
            },
            max_content_length=max_content_length,
        )

    def see(
        self,
        visual_description,
        source: AgentOrWorld = None,
        max_content_length=default['max_content_display_length'],
    ):
        """
        Воспринимает визуальный стимул через описание и обновляет свое внутреннее когнитивное состояние.

        :param visual_description: Описание визуального стимула.
        :type visual_description: str
        :param source: Источник визуального стимула.
        :type source: AgentOrWorld, optional
        :param max_content_length: Максимальная длина выводимого контента.
        :type max_content_length: int, optional
         :return: Агент.
        :rtype: TinyPerson
        """
        return self._observe(
            stimulus={
                'type': 'VISUAL',
                'content': visual_description,
                'source': name_or_empty(source),
            },
            max_content_length=max_content_length,
        )

    def think(self, thought, max_content_length=default['max_content_display_length']):
        """
        Заставляет агента думать о чем-то и обновляет его внутреннее когнитивное состояние.

        :param thought: Мысль агента.
        :type thought: str
        :param max_content_length: Максимальная длина выводимого контента.
        :type max_content_length: int, optional
        :return: Агент.
        :rtype: TinyPerson
        """
        return self._observe(
            stimulus={
                'type': 'THOUGHT',
                'content': thought,
                'source': name_or_empty(self),
            },
            max_content_length=max_content_length,
        )

    def internalize_goal(
        self, goal, max_content_length=default['max_content_display_length']
    ):
        """
        Интернализирует цель и обновляет когнитивное состояние.

        :param goal: Цель для интернализации.
        :type goal: str
        :param max_content_length: Максимальная длина выводимого контента.
        :type max_content_length: int, optional
        :return: Агент.
        :rtype: TinyPerson
        """
        return self._observe(
            stimulus={
                'type': 'INTERNAL_GOAL_FORMULATION',
                'content': goal,
                'source': name_or_empty(self),
            },
            max_content_length=max_content_length,
        )

    @transactional
    def _observe(self, stimulus, max_content_length=default['max_content_display_length']):
        """
        Наблюдает за стимулом и обновляет когнитивное состояние.

        :param stimulus: Стимул для наблюдения.
        :type stimulus: dict
        :param max_content_length: Максимальная длина выводимого контента.
        :type max_content_length: int, optional
        :return: Агент.
        :rtype: TinyPerson
        """
        stimuli = [stimulus]

        content = {'stimuli': stimuli}

        logger.debug(f'[{self.name}] Observing stimuli: {content}')

        # whatever comes from the outside will be interpreted as coming from 'user', simply because
        # this is the counterpart of 'assistant'

        self.episodic_memory.store({'role': 'user', 'content': content, 'simulation_timestamp': self.iso_datetime()})

        if TinyPerson.communication_display:
            self._display_communication(
                role='user',
                content=content,
                kind='stimuli',
                simplified=True,
                max_content_length=max_content_length,
            )

        return self  # allows easier chaining of methods

    @transactional
    def listen_and_act(
        self,
        speech,
        return_actions=False,
        max_content_length=default['max_content_display_length'],
    ):
        """
        Комбинирует методы `listen` и `act`.

        :param speech: Речь для прослушивания.
        :type speech: str
        :param return_actions: Флаг, указывающий, нужно ли возвращать действия.
        :type return_actions: bool, optional
         :param max_content_length: Максимальная длина выводимого контента.
        :type max_content_length: int, optional
        :return: Список действий, если `return_actions` равен True, иначе None.
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
        max_content_length=default['max_content_display_length'],
    ):
        """
        Комбинирует методы `see` и `act`.

        :param visual_description: Описание визуального стимула.
        :type visual_description: str
        :param return_actions: Флаг, указывающий, нужно ли возвращать действия.
        :type return_actions: bool, optional
         :param max_content_length: Максимальная длина выводимого контента.
        :type max_content_length: int, optional
        :return: Список действий, если `return_actions` равен True, иначе None.
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
        max_content_length=default['max_content_display_length'],
    ):
        """
        Комбинирует методы `think` и `act`.

        :param thought: Мысль для обдумывания.
        :type thought: str
        :param return_actions: Флаг, указывающий, нужно ли возвращать действия.
        :type return_actions: bool, optional
        :param max_content_length: Максимальная длина выводимого контента.
        :type max_content_length: int, optional
        :return: Список действий, если `return_actions` равен True, иначе None.
        :rtype: list, optional
        """

        self.think(thought, max_content_length=max_content_length)
        return self.act(return_actions=return_actions, max_content_length=max_content_length)

    def read_documents_from_folder(self, documents_path:str):
        """
        Читает документы из указанной папки и загружает их в семантическую память.

        :param documents_path: Путь к папке с документами.
        :type documents_path: str
        """
        logger.info(f'Setting documents path to {documents_path} and loading documents.')

        self.semantic_memory.add_documents_path(documents_path)
    
    def read_documents_from_web(self, web_urls:list):
        """
        Читает документы из указанных веб-адресов и загружает их в семантическую память.

        :param web_urls: Список веб-адресов.
        :type web_urls: list
        """
        logger.info(f'Reading documents