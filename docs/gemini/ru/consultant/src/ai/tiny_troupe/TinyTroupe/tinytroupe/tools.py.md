# Анализ кода модуля tools

**Качество кода**
6
- Плюсы
    - Код достаточно хорошо структурирован и разбит на классы.
    - Используются логирование для отладки.
    - Присутствует базовая обработка ошибок.
- Минусы
    - Отсутствует документация в формате reStructuredText (RST).
    - Используется стандартный `json.loads` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Есть потенциальные места для улучшения обработки ошибок.
    - Некоторые комментарии не соответствуют стилю RST.
    - Присутствуют `TODO` комментарии, которые необходимо обработать.

**Рекомендации по улучшению**

1. **Документация**:
   - Добавить docstring в формате reStructuredText (RST) для всех классов, методов и функций.

2. **Импорты**:
    - Добавить недостающие импорты: `from src.logger.logger import logger`
    - Использовать `from src.utils.jjson import j_loads` или `j_loads_ns` вместо `json.loads`

3. **Обработка ошибок**:
   - Заменить стандартные блоки `try-except` на использование `logger.error` для логирования ошибок.
    - Добавить обработку ошибок при чтении JSON, чтобы избежать падения программы.

4. **Рефакторинг**:
    - Упростить логику `_process_action` в классах `TinyCalendar` и `TinyWordProcessor`.
    - Использовать более конкретные сообщения об ошибках.

5. **Комментарии**:
   - Переписать все комментарии в формате reStructuredText (RST).
   -  Удалить комментарии `# TODO` если они не несут смысловой нагрузки.

**Оптимизированный код**
```python
"""
Модуль для инструментов, позволяющих агентам выполнять специализированные задачи.
==============================================================================

Этот модуль определяет базовый класс :class:`TinyTool` и его производные,
которые предоставляют агентам различные возможности, такие как ведение календаря
и обработка текстовых документов.

Пример использования
--------------------

Пример создания и использования инструмента `TinyWordProcessor`:

.. code-block:: python

    from tinytroupe.tools import TinyWordProcessor
    from tinytroupe.enrichment import TinyEnricher
    from tinytroupe.extraction import ArtifactExporter
    from src.logger.logger import logger


    exporter = ArtifactExporter(output_dir="output")
    enricher = TinyEnricher(api_key="your_api_key")
    word_processor = TinyWordProcessor(exporter=exporter, enricher=enricher)
    word_processor.write_document(title="My Document", content="This is a test document", author="Test Agent")
    

"""
import textwrap
import copy
from src.utils.jjson import j_loads # импортируем j_loads для загрузки json
from src.logger.logger import logger # импортируем logger для логирования
import logging

import tinytroupe.utils as utils
from tinytroupe.extraction import ArtifactExporter
from tinytroupe.enrichment import TinyEnricher
from tinytroupe.utils import JsonSerializableRegistry

class TinyTool(JsonSerializableRegistry):
    """
    Базовый класс для всех инструментов.

    Предоставляет общую структуру и функциональность для инструментов,
    используемых агентами.

    :param name: Имя инструмента.
    :type name: str
    :param description: Описание инструмента.
    :type description: str
    :param owner: Агент, владеющий инструментом. Если `None`, инструмент может использоваться любым агентом.
    :type owner: str, optional
    :param real_world_side_effects: Указывает, имеет ли инструмент побочные эффекты в реальном мире.
    :type real_world_side_effects: bool, optional
    :param exporter: Экспортер для сохранения результатов работы инструмента.
    :type exporter: ArtifactExporter, optional
    :param enricher: Обогатитель для обработки результатов работы инструмента.
    :type enricher: TinyEnricher, optional

    """
    def __init__(self, name, description, owner=None, real_world_side_effects=False, exporter=None, enricher=None):
        
        self.name = name
        self.description = description
        self.owner = owner
        self.real_world_side_effects = real_world_side_effects
        self.exporter = exporter
        self.enricher = enricher

    def _process_action(self, agent, action: dict) -> bool:
        """
        Обрабатывает действие агента.

        Этот метод должен быть переопределен в подклассах.

        :param agent: Агент, выполняющий действие.
        :type agent: Agent
        :param action: Словарь, описывающий действие.
        :type action: dict
        :raises NotImplementedError: Если метод не переопределен в подклассе.
        """
        raise NotImplementedError("Subclasses must implement this method.")
    
    def _protect_real_world(self):
        """
        Предупреждает о реальных побочных эффектах инструмента.

        Выводит предупреждение в лог, если инструмент имеет реальные побочные эффекты.
        """
        if self.real_world_side_effects:
            logger.warning(f" !!!!!!!!!! Tool {self.name} has REAL-WORLD SIDE EFFECTS. This is NOT just a simulation. Use with caution. !!!!!!!!!!")
        
    def _enforce_ownership(self, agent):
        """
        Проверяет владельца инструмента.

        Вызывает ошибку, если агент не является владельцем инструмента.

        :param agent: Агент, пытающийся использовать инструмент.
        :type agent: Agent
        :raises ValueError: Если агент не является владельцем инструмента.
        """
        if self.owner is not None and agent.name != self.owner.name:
            raise ValueError(f"Agent {agent.name} does not own tool {self.name}, which is owned by {self.owner.name}.")
    
    def set_owner(self, owner):
        """
        Устанавливает владельца инструмента.

        :param owner: Агент, который станет владельцем инструмента.
        :type owner: Agent
        """
        self.owner = owner

    def actions_definitions_prompt(self) -> str:
        """
        Возвращает описание доступных действий инструмента.

        Этот метод должен быть переопределен в подклассах.

        :raises NotImplementedError: Если метод не переопределен в подклассе.
        """
        raise NotImplementedError("Subclasses must implement this method.")
    
    def actions_constraints_prompt(self) -> str:
        """
        Возвращает ограничения на действия инструмента.

        Этот метод должен быть переопределен в подклассах.

        :raises NotImplementedError: Если метод не переопределен в подклассе.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def process_action(self, agent, action: dict) -> bool:
        """
        Обрабатывает действие агента, проверяя владельца и побочные эффекты.

        :param agent: Агент, выполняющий действие.
        :type agent: Agent
        :param action: Словарь, описывающий действие.
        :type action: dict
        :return: `True`, если действие выполнено успешно, иначе `False`.
        :rtype: bool
        """
        self._protect_real_world()
        self._enforce_ownership(agent)
        return self._process_action(agent, action)


class TinyCalendar(TinyTool):
    """
    Инструмент календаря для агентов.

    Позволяет агентам отслеживать встречи и события.

    :param owner: Агент, владеющий календарем. Если `None`, календарь может использоваться любым агентом.
    :type owner: str, optional
    """
    def __init__(self, owner=None):
        super().__init__("calendar", "A basic calendar tool that allows agents to keep track meetings and appointments.", owner=owner, real_world_side_effects=False)
        
        #: Словарь, отображающий дату на список событий. Каждое событие является словарем с ключами "title", "description", "owner", "mandatory_attendees", "optional_attendees", "start_time", "end_time".
        self.calendar = {}
    
    def add_event(self, date, title, description=None, owner=None, mandatory_attendees=None, optional_attendees=None, start_time=None, end_time=None):
        """
        Добавляет новое событие в календарь.

        :param date: Дата события.
        :type date: str
        :param title: Название события.
        :type title: str
        :param description: Описание события.
        :type description: str, optional
        :param owner: Владелец события.
        :type owner: str, optional
        :param mandatory_attendees: Список агентов, которые обязательно должны присутствовать.
        :type mandatory_attendees: list, optional
        :param optional_attendees: Список агентов, которые приглашены на событие.
        :type optional_attendees: list, optional
        :param start_time: Время начала события.
        :type start_time: str, optional
        :param end_time: Время окончания события.
        :type end_time: str, optional
        """
        if date not in self.calendar:
            self.calendar[date] = []
        self.calendar[date].append({"title": title, "description": description, "owner": owner, "mandatory_attendees": mandatory_attendees, "optional_attendees": optional_attendees, "start_time": start_time, "end_time": end_time})
    
    def find_events(self, year, month, day, hour=None, minute=None):
        """
        Находит события в календаре.
        
        :param year: Год.
        :type year: int
        :param month: Месяц.
        :type month: int
        :param day: День.
        :type day: int
        :param hour: Час.
        :type hour: int, optional
        :param minute: Минута.
        :type minute: int, optional
        """
        # TODO implementation
        pass

    def _process_action(self, agent, action) -> bool:
        """
        Обрабатывает действие агента, связанное с календарем.

        :param agent: Агент, выполняющий действие.
        :type agent: Agent
        :param action: Словарь, описывающий действие.
        :type action: dict
        :return: `True`, если действие выполнено успешно, иначе `False`.
        :rtype: bool
        """
        if action.get('type') == "CREATE_EVENT" and action.get('content') is not None:
            try:
                #  код исполняет загрузку содержимого из JSON
                event_content = j_loads(action['content'])
                
                # проверка наличия недопустимых полей
                valid_keys = ["title", "description", "mandatory_attendees", "optional_attendees", "start_time", "end_time"]
                utils.check_valid_fields(event_content, valid_keys)
                
                #  код исполняет добавление события в календарь
                self.add_event(**event_content)
                return True
            except Exception as e:
                 logger.error(f"Ошибка обработки действия CREATE_EVENT: {e}. Содержимое: {action.get('content')}")
                 return False

        else:
            return False

    def actions_definitions_prompt(self) -> str:
        """
        Возвращает описание действий, которые можно выполнить с календарем.

        :return: Описание доступных действий.
        :rtype: str
        """
        prompt = """
              - CREATE_EVENT: Вы можете создать новое событие в своем календаре. Содержание события имеет много полей, и вы должны использовать формат JSON, чтобы указать их. Вот возможные поля:
                * title: Название события. Обязательно.
                * description: Краткое описание события. Необязательно.
                * mandatory_attendees: Список имен агентов, которые должны присутствовать на событии. Необязательно.
                * optional_attendees: Список имен агентов, которые приглашены на событие, но не обязаны присутствовать. Необязательно.
                * start_time: Время начала события. Необязательно.
                * end_time: Время окончания события. Необязательно.
            """
        # TODO how the atendee list will be handled? How will they be notified of the invitation? I guess they must also have a calendar themselves. <-------------------------------------
        return utils.dedent(prompt)
        
    
    def actions_constraints_prompt(self) -> str:
        """
         Возвращает ограничения на действия календаря.

        :return: Описание ограничений.
        :rtype: str
        """
        prompt = """
              
            """
            # TODO 
        return textwrap.dedent(prompt)
    


class TinyWordProcessor(TinyTool):
    """
    Инструмент текстового процессора для агентов.

    Позволяет агентам создавать и редактировать текстовые документы.

    :param owner: Агент, владеющий текстовым процессором. Если `None`, текстовый процессор может использоваться любым агентом.
    :type owner: str, optional
    :param exporter: Экспортер для сохранения документов.
    :type exporter: ArtifactExporter, optional
    :param enricher: Обогатитель для улучшения содержания документов.
    :type enricher: TinyEnricher, optional
    """
    def __init__(self, owner=None, exporter=None, enricher=None):
        super().__init__("wordprocessor", "A basic word processor tool that allows agents to write documents.", owner=owner, real_world_side_effects=False, exporter=exporter, enricher=enricher)
        
    def write_document(self, title, content, author=None):
        """
        Создает и сохраняет документ.

        :param title: Название документа.
        :type title: str
        :param content: Содержание документа.
        :type content: str
        :param author: Автор документа.
        :type author: str, optional
        """
        logger.debug(f"Writing document with title {title} and content: {content}")

        if self.enricher is not None:
            requirements = """
            Turn any draft or outline into an actual and long document, with many, many details. Include tables, lists, and other elements.
            The result **MUST** be at least 5 times larger than the original content in terms of characters - do whatever it takes to make it this long and detailed.
            """
            content = self.enricher.enrich_content(requirements=requirements, 
                                                    content=content, 
                                                    content_type="Document", 
                                                    context_info=None,
                                                    context_cache=None, verbose=False)    
            
        if self.exporter is not None:
            self.exporter.export(artifact_name=f"{title}.{author}", artifact_data= content, content_type="Document", content_format="md", target_format="md")
            self.exporter.export(artifact_name=f"{title}.{author}", artifact_data= content, content_type="Document", content_format="md", target_format="docx")

            json_doc = {"title": title, "content": content, "author": author}
            self.exporter.export(artifact_name=f"{title}.{author}", artifact_data= json_doc, content_type="Document", content_format="md", target_format="json")

    def _process_action(self, agent, action) -> bool:
        """
        Обрабатывает действие агента, связанное с текстовым процессором.

        :param agent: Агент, выполняющий действие.
        :type agent: Agent
        :param action: Словарь, описывающий действие.
        :type action: dict
        :return: `True`, если действие выполнено успешно, иначе `False`.
        :rtype: bool
        """
        if action.get('type') == "WRITE_DOCUMENT" and action.get('content') is not None:
            try:
                # код исполняет загрузку содержимого документа из JSON
                if isinstance(action['content'], str):
                    doc_spec = j_loads(action['content'])
                else:
                    doc_spec = action['content']
                
                # проверка наличия недопустимых полей
                valid_keys = ["title", "content", "author"]
                utils.check_valid_fields(doc_spec, valid_keys)
                
                #  код исполняет создание нового документа
                self.write_document(**doc_spec)
                return True
            except Exception as e:
                logger.error(f"Ошибка обработки действия WRITE_DOCUMENT: {e}. Содержимое: {action.get('content')}")
                return False
        else:
            return False

    def actions_definitions_prompt(self) -> str:
        """
         Возвращает описание действий, которые можно выполнить с текстовым процессором.

        :return: Описание доступных действий.
        :rtype: str
        """
        prompt = """
            - WRITE_DOCUMENT: вы можете создать новый документ. Содержание документа имеет много полей, и вы должны использовать формат JSON, чтобы указать их. Вот возможные поля:
                * title: Название документа. Обязательно.
                * content: Фактическое содержание документа. Вы **должны** использовать Markdown для форматирования этого содержания. Обязательно.
                * author: Автор документа. Вы должны указать свое имя. Необязательно.
            """
        return utils.dedent(prompt)
        
    
    def actions_constraints_prompt(self) -> str:
        """
        Возвращает ограничения на действия текстового процессора.

        :return: Описание ограничений.
        :rtype: str
        """
        prompt = """
            - Whenever you WRITE_DOCUMENT, you write all the content at once. Moreover, the content should be long and detailed, unless there's a good reason for it not to be.
            - When you WRITE_DOCUMENT, you follow these additional guidelines:
                * For any milestones or timelines mentioned, try mentioning specific owners or partner teams, unless there's a good reason not to do so.
            """
        return utils.dedent(prompt)