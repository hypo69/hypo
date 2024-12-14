## Анализ кода модуля `agent.py`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и разбит на классы и функции, что способствует его читаемости и поддержке.
    - Присутствует документация в формате docstring, что облегчает понимание назначения классов и методов.
    - Используются декораторы для управления транзакциями и инициализацией.
    - Присутствуют механизмы для сериализации и десериализации объектов, что позволяет сохранять и восстанавливать состояние агентов.
-  Минусы
    - Некоторые docstring требуют доработки для соответствия формату reStructuredText (RST).
    - В коде используется `json.dumps`, но не используется `j_loads` или `j_loads_ns` для чтения данных.
    - Есть участки, где не используется `logger.error` для обработки исключений.
    - Некоторые комментарии после `#` можно переписать в стиле RST.
    - Есть участки кода с `# TODO`, требующие внимания.
    - Использование `print` для вывода, вместо `logger.info` или `logger.debug`.

**Рекомендации по улучшению**

1.  **Документация**:
    - Переписать docstring в соответствии с форматом reStructuredText (RST).
    - Описать все параметры функций и возвращаемые значения.
    - Переписать комментарии после `#` в стиле RST.
2.  **Обработка данных**:
    - Заменить `json.dumps` на `j_dumps` из `src.utils.jjson` там, где это уместно.
    - При чтении файлов использовать `j_loads` или `j_loads_ns`.
3.  **Логирование**:
    - Использовать `logger.error` для обработки исключений вместо `try-except` с `print`.
    - Использовать `logger.info` или `logger.debug` вместо `print` для вывода.
4.  **Рефакторинг**:
    - Заменить `json.dumps` и `json.loads` на `j_dumps` и `j_loads` из `src.utils.jjson`.
    - Улучшить обработку ошибок, используя `logger.error` с исключением.
    - Добавить проверку типов для параметров функций.
    - Улучшить форматирование кода, сделав его более читаемым.
5.  **Импорты**:
    - Добавить отсутствующие импорты, если они необходимы.
6.  **Комментарии**:
    - Заменить комментарии `#` на `reStructuredText` комментарии.
7. **`TODO`**:
    - Обратить внимание на места в коде, где есть `# TODO` и выполнить необходимые доработки.

**Оптимизированный код**

```python
"""
Модуль, предоставляющий основные классы и функции для агентов TinyTroupe.
======================================================================

Агенты являются ключевой абстракцией, используемой в TinyTroupe. Агент - это имитированный человек или сущность,
которая может взаимодействовать с другими агентами и средой, получая стимулы и производя действия.
Агенты имеют когнитивные состояния, которые обновляются по мере их взаимодействия со средой и другими агентами.
Агенты также могут хранить и извлекать информацию из памяти и выполнять действия в среде.
В отличие от агентов, цель которых - обеспечить поддержку для AI-ассистентов или других подобных инструментов повышения производительности,
**агенты TinyTroupe нацелены на представление человекоподобного поведения**, которое включает идиосинкразии,
эмоции и другие человеческие черты, которые не ожидаются от инструментов повышения производительности.

Общая основная конструкция вдохновлена главным образом когнитивной психологией, поэтому агенты имеют различные
внутренние когнитивные состояния, такие как внимание, эмоции и цели.
Также именно поэтому память агента, в отличие от других платформ агентов на основе LLM, имеет тонкие внутренние
разделения, особенно между эпизодической и семантической памятью.
Также присутствуют некоторые бихевиористские концепции, такие как идея "стимула" и "реакции" в методах `listen` и `act`,
которые являются ключевыми абстракциями для понимания того, как агенты взаимодействуют со средой и другими агентами.
"""

import os
import textwrap
import datetime
import chevron
import copy
from typing import Any, TypeVar, Union, List, Dict
from src.utils.jjson import j_dumps, j_loads, j_loads_ns
from src.logger.logger import logger

import logging # to suppress the llama-index logging messages, that are too verbose
logging.getLogger("llama_index").setLevel(logging.WARNING)

import tinytroupe.utils as utils
from tinytroupe.utils import post_init
from tinytroupe.control import transactional
from tinytroupe.control import current_simulation
from rich import print

from tinytroupe.utils import JsonSerializableRegistry

Self = TypeVar("Self", bound="TinyPerson")
AgentOrWorld = Union[Self, "TinyWorld"]

###########################################################################
# Default parameter values
###########################################################################
# Используются различные элементы конфигурации
config = utils.read_config_file()

default = {}
default["embedding_model"] = config["OpenAI"].get("EMBEDDING_MODEL", "text-embedding-3-small")
default["max_content_display_length"] = config["OpenAI"].getint("MAX_CONTENT_DISPLAY_LENGTH", 1024)


## LLaMa-Index configs ########################################################
#from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader
from llama_index.readers.web import SimpleWebPageReader


# Кэширование будет выполняться локально llama-index в зависящем от ОС местоположении

##Settings.embed_model = HuggingFaceEmbedding(
##    model_name="BAAI/bge-small-en-v1.5"
##)

llmaindex_openai_embed_model = OpenAIEmbedding(model=default["embedding_model"], embed_batch_size=10)
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
    Представляет собой имитацию человека во вселенной TinyTroupe.
    
    :cvar MAX_ACTIONS_BEFORE_DONE: Максимальное количество действий, которое агенту разрешено выполнять до DONE.
        Это предотвращает бесконечные действия агента.
    :cvar PP_TEXT_WIDTH: Ширина текста для предварительного просмотра.
    :cvar serializable_attributes: Список атрибутов, подлежащих сериализации.
    :cvar all_agents: Словарь всех созданных агентов.
    :cvar communication_style: Стиль общения для всех агентов: "simplified" или "full".
    :cvar communication_display: Флаг, указывающий, отображать ли общение. True для интерактивных приложений.
    """

    # Максимальное количество действий, которое агенту разрешено выполнять до DONE.
    # Это предотвращает бесконечные действия агента.
    MAX_ACTIONS_BEFORE_DONE = 15

    PP_TEXT_WIDTH = 100

    serializable_attributes = ["name", "episodic_memory", "semantic_memory", "_mental_faculties", "_configuration"]

    # Словарь всех созданных агентов.
    all_agents = {}  # name -> agent

    # Стиль общения для всех агентов: "simplified" или "full".
    communication_style:str="simplified"
    
    # Флаг, указывающий, отображать ли общение. True для интерактивных приложений.
    communication_display:bool=True
    

    def __init__(self, name:str=None, 
                 episodic_memory=None,
                 semantic_memory=None,
                 mental_faculties:list=None):
        """
        Создает объект TinyPerson.

        :param name: Имя агента TinyPerson.
        :type name: str, optional
        :param episodic_memory: Реализация памяти для эпизодической памяти.
        :type episodic_memory: EpisodicMemory, optional
        :param semantic_memory: Реализация памяти для семантической памяти.
        :type semantic_memory: SemanticMemory, optional
        :param mental_faculties: Список ментальных способностей для добавления агенту.
        :type mental_faculties: list, optional
        :raises AssertionError: Если имя агента не указано.
        
        .. note::
           Значения по умолчанию будут заданы в методе `_post_init`, так как он используется как
           при прямой инициализации, так и при десериализации.
        """

        # NOTE: значения по умолчанию будут даны в методе _post_init, так как он используется как
        #       при прямой инициализации, так и при десериализации.

        if episodic_memory is not None:
            self.episodic_memory = episodic_memory
        
        if semantic_memory is not None:
            self.semantic_memory = semantic_memory

        # Ментальные способности
        if mental_faculties is not None:
            self._mental_faculties = mental_faculties
        
        assert name is not None, "A TinyPerson must have a name."
        self.name = name

        # @post_init обеспечивает вызов _post_init после __init__


    
    def _post_init(self, **kwargs):
        """
        Выполняется после `__init__`, так как класс имеет декоратор `@post_init`.
        Удобно разделять некоторые процессы инициализации, чтобы упростить десериализацию.

        :param kwargs: Дополнительные параметры.
        :type kwargs: dict
        """

        ############################################################
        # Значения по умолчанию
        ############################################################

        self.current_messages = []
        
        # Текущее окружение, в котором действует агент
        self.environment = None

        # Список действий, которые этот агент выполнил к настоящему времени, но еще не
        # обработанные средой.
        self._actions_buffer = []

        # Список агентов, с которыми этот агент может в настоящее время взаимодействовать.
        # Это может меняться со временем, по мере того как агенты перемещаются по миру.
        self._accessible_agents = []

        # Буфер коммуникаций, которые были отображены к настоящему времени, используется для
        # сохранения этих коммуникаций в другой выходной форме позже (например, кэширование)
        self._displayed_communications_buffer = []

        if not hasattr(self, 'episodic_memory'):
            # Значение по умолчанию НЕ должно быть в сигнатуре метода, иначе оно будет использоваться всеми экземплярами.
            self.episodic_memory = EpisodicMemory()
        
        if not hasattr(self, 'semantic_memory'):
            # Значение по умолчанию НЕ должно быть в сигнатуре метода, иначе оно будет использоваться всеми экземплярами.
            self.semantic_memory = SemanticMemory()
        
        # _mental_faculties
        if not hasattr(self, '_mental_faculties'):
            # Значение по умолчанию НЕ должно быть в сигнатуре метода, иначе оно будет использоваться всеми экземплярами.
            self._mental_faculties = []

        # создание словаря конфигурации
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
        self._init_system_message = None  # инициализируется позже


        ############################################################
        # Специальные механизмы, используемые во время десериализации
        ############################################################

        # Переименовать агента в какое-то конкретное имя?
        if kwargs.get("new_agent_name") is not None:
            self._rename(kwargs.get("new_agent_name"))
        
        # Если автоматическое переименование, использовать данное имя плюс какой-то новый номер...
        if kwargs.get("auto_rename") is True:
            new_name = self.name # начать с текущего имени
            rename_succeeded = False
            while not rename_succeeded:
                try:
                    self._rename(new_name)
                    TinyPerson.add_agent(self)
                    rename_succeeded = True                
                except ValueError:
                    new_id = utils.fresh_id()
                    new_name = f"{self.name}_{new_id}"
        
        # ... в противном случае, просто зарегистрировать агента
        else:
            # зарегистрировать агента в глобальном списке агентов
            TinyPerson.add_agent(self)

        # Начать с чистого листа
        self.reset_prompt()

        # Может быть так, что агент создается в рамках области моделирования, и в этом случае
        # simulation_id должен быть установлен соответствующим образом.
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
        Генерирует промпт агента, используя шаблон.

        :return: Сгенерированный промпт агента.
        :rtype: str
        """
        with open(self._prompt_template_path, "r") as f:
            agent_prompt_template = f.read()

        # Давайте работать поверх копии конфигурации, потому что нам нужно будет добавить больше переменных и т.д.
        template_variables = self._configuration.copy()    

        # Подготовить дополнительные определения и ограничения действий
        actions_definitions_prompt = ""
        actions_constraints_prompt = ""
        for faculty in self._mental_faculties:
            actions_definitions_prompt += f"{faculty.actions_definitions_prompt()}\\n"
            actions_constraints_prompt += f"{faculty.actions_constraints_prompt()}\\n"
        
        # сделать дополнительные фрагменты промпта доступными для шаблона
        template_variables['actions_definitions_prompt'] = textwrap.indent(actions_definitions_prompt, "")
        template_variables['actions_constraints_prompt'] = textwrap.indent(actions_constraints_prompt, "")

        # Компоненты промпта RAI, если запрошено
        template_variables = utils.add_rai_template_variables_if_enabled(template_variables)

        return chevron.render(agent_prompt_template, template_variables)

    def reset_prompt(self):
        """
        Сбрасывает промпт агента, используя текущую конфигурацию.
        """

        # Отрисовать шаблон с текущей конфигурацией
        self._init_system_message = self.generate_agent_prompt()

        # TODO: на самом деле, придумайте другой способ обновления состояния агента без "изменения истории"

        # сбросить системное сообщение
        self.current_messages = [
            {"role": "system", "content": self._init_system_message}
        ]

        # настраивает фактические сообщения взаимодействия, используемые для промптинга
        self.current_messages += self.episodic_memory.retrieve_recent()

    def get(self, key):
        """
        Возвращает определение ключа в конфигурации TinyPerson.

        :param key: Ключ для получения.
        :type key: str
        :return: Значение ключа или None, если ключ не найден.
        :rtype: Any
        """
        return self._configuration.get(key, None)
    
    @transactional
    def define(self, key, value, group=None):
        """
        Определяет значение в конфигурации TinyPerson.

        :param key: Ключ для добавления значения.
        :type key: str, optional
        :param value: Значение для установки.
        :type value: Any
        :param group: Группа, к которой добавить значение.
        :type group: str, optional
        """

        # Убрать отступ от значения, если это строка
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

        # Сбросить промпт после добавления в конфигурацию
        self.reset_prompt()

    def define_several(self, group, records):
        """
        Определяет несколько значений в конфигурации TinyPerson, все из одной группы.

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
        :param replace: Следует ли заменить текущие отношения или просто добавить к ним.
        :type replace: bool, optional
        :raises Exception: Если аргументы недействительны.
        
        .. note::
            Отношения могут быть списком словарей, где каждый словарь связывает имя агента с его описанием отношений.
            Или одиночным словарем, связывающим имя агента с описанием его отношений.
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

        :return: Объект агента.
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
        :param description: Описание отношений.
        :type description: str
        :param symmetric_description: Являются ли отношения симметричными.
        :type symmetric_description: str, optional
        :return: Объект агента.
        :rtype: TinyPerson
        
        .. note::
            Если отношения симметричны, то они определяются для обоих агентов.
        """
        self.define_relationships([{"Name": other_agent.name, "Description": description}], replace=False)
        if symmetric_description is not None:
            other_agent.define_relationships([{"Name": self.name, "Description": symmetric_description}], replace=False)
        
        return self
    
    def add_mental_faculties(self, mental_faculties: list) -> Self:
        """
        Добавляет список ментальных способностей агенту.

        :param mental_faculties: Список ментальных способностей.
        :type mental_faculties: list
        :return: Объект агента.
        :rtype: Self
        """
        for faculty in mental_faculties:
            self.add_mental_faculty(faculty)
        
        return self

    def add_mental_faculty(self, faculty) -> Self:
        """
        Добавляет ментальную способность агенту.

        :param faculty: Ментальная способность.
        :type faculty: TinyMentalFaculty
        :return: Объект агента.
        :rtype: Self
        :raises Exception: Если ментальная способность уже присутствует у агента.
        """
        # проверить, есть ли уже эта способность или нет
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
        Выполняет действия в среде и обновляет свое внутреннее когнитивное состояние.

        :param until_done: Следует ли продолжать действовать до тех пор, пока агент не будет готов и не потребует дополнительного стимула.
        :type until_done: bool, optional
        :param n: Количество действий для выполнения.
        :type n: int, optional
        :param return_actions: Следует ли возвращать действия.
        :type return_actions: bool, optional
        :param max_content_length: Максимальная длина контента для отображения.
        :type max_content_length: int, optional
        :return: Список действий (если `return_actions` True).
        :rtype: list, optional
        :raises AssertionError: Если одновременно указаны `until_done` и `n`.
        
        .. note::
            Либо действует до тех пор, пока агент не будет готов и не потребует дополнительных стимулов, либо действует фиксированное количество раз, но не оба варианта одновременно.
        """

        # Либо действовать до готовности, либо действовать фиксированное количество раз, но не одновременно
        assert not (until_done and n is not None)
        if n is not None:
            assert n < TinyPerson.MAX_ACTIONS_BEFORE_DONE

        contents = []

        # Вспомогательная функция для выполнения ровно одного действия.
        # Иногда модель возвращает JSON, в котором отсутствуют важные ключи, поэтому мы просто просим ее попробовать еще раз
        @repeat_on_error(retries=5, exceptions=[KeyError])
        def aux_act_once():
            # Быстрая мысль перед действием. Кажется, это помогает получать лучшие ответы модели, возможно, потому что
            # это чередует сообщения пользователя с сообщениями помощника.
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
            # Некоторые действия вызывают немедленный стимул или другие побочные эффекты. Нам нужно обработать их здесь с помощью ментальных способностей.
            #
            for faculty in self._mental_faculties:
                faculty.process_action(self, action)             
            

        #
        # Как продолжить с последовательностью действий.
        #
        ##### Вариант 1: выполнить N действий ######
        if n is not None:
            for i in range(n):
                aux_act_once()

        ##### Вариант 2: выполнять до DONE ######
        elif until_done:
            while (len(contents) == 0) or (
                not contents[-1]["action"]["type"] == "DONE"
            ):


                # проверить, не действует ли агент, никогда не останавливаясь
                if len(contents) > TinyPerson.MAX_ACTIONS_BEFORE_DONE:
                    logger.warning(f"[{self.name}] Agent {self.name} is acting without ever stopping. This may be a bug. Let's stop it here anyway.")
                    break
                if len(contents) > 4: # просто какое-то минимальное количество действий для проверки повторения, может быть любым >= 3
                    # если последние три действия были одинаковыми, то мы, вероятно, в цикле
                    if contents[-1]['action'] == contents[-2]['action'] == contents[-3]['action']:
                        logger.warning(f"[{self.name}] Agent {self.name} is acting in a loop. This may be a bug. Let's stop it here anyway.")
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
        Слушает другого агента (искусственного или человеческого) и обновляет свое внутреннее когнитивное состояние.

        :param speech: Речь для прослушивания.
        :type speech: str
        :param source: Источник речи.
        :type source: AgentOrWorld, optional
        :param max_content_length: Максимальная длина содержимого.
        :type max_content_length: int, optional
        :return: Объект агента.
        :rtype: Self
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
        :param max_content_length: Максимальная длина содержимого.
        :type max_content_length: int, optional
        :return: Объект агента.
        :rtype: Self
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
        :param max_content_length: Максимальная длина содержимого.
        :type max_content_length: int, optional
        :return: Объект агента.
        :rtype: Self
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
        Заставляет агента думать о чем-то и обновляет его внутреннее когнитивное состояние.

        :param thought: Мысль для обдумывания.
        :type thought: str
        :param max_content_length: Максимальная длина содержимого.
        :type max_content_length: int, optional
        :return: Объект агента.
        :rtype: Self
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
        :param max_content_length: Максимальная длина содержимого.
        :type max_content_length: int, optional
        :return: Объект агента.
        :rtype: Self
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
        Наблюдает стимул и обновляет свое внутреннее когнитивное состояние.

        :param stimulus: Стимул для наблюдения.
        :type stimulus: dict
        :param max_content_length: Максимальная длина содержимого.
        :type max_content_length: int, optional
        :return: Объект агента.
        :rtype: Self
        """
        stimuli = [stimulus]

        content = {"stimuli": stimuli}

        logger.debug(f"[{self.name}] Observing stimuli: {content}")

        # Все, что приходит извне, будет интерпретироваться как исходящее от "пользователя", просто потому, что
        # это аналог "помощника"

        self.episodic_memory.store({'role': 'user', 'content': content, 'simulation_timestamp': self.iso_datetime()})

        if TinyPerson.communication_display:
            self._display_communication(
                role="user",
                content=content,
                kind="stimuli",
                simplified=True,
                max_content_length=max_content_length,
            )

        return self  # позволяет упростить цепочку методов

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
        :param return_actions: Следует ли возвращать действия.
        :type return_actions: bool, optional
        :param max_content_length: Максимальная длина содержимого.
        :type max_content_length: int, optional
        :return: Список действий (если `return_actions` True).
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
        :param return_actions: Следует ли возвращать действия.
        :type return_actions: bool, optional
        :param max_content_length: Максимальная длина содержимого.
        :type max_content_length: int, optional
        :return: Список действий (если `return_actions` True).
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
        max