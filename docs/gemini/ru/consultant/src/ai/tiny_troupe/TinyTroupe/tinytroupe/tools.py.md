### Анализ кода модуля `tools`

**Качество кода**:

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код хорошо структурирован, с разделением на классы `TinyTool`, `TinyCalendar` и `TinyWordProcessor`.
    - Используется `JsonSerializableRegistry` для управления инструментами.
    - Присутствует базовая обработка ошибок и логирование.
    - Имеется поддержка экспорта и обогащения контента.
- **Минусы**:
    - Некоторые комментарии не соответствуют стандарту RST.
    - Используется стандартный `json.loads` вместо `j_loads` из `src.utils.jjson`.
    - Логирование ошибок не использует `from src.logger.logger import logger`.
    - В классе `TinyCalendar`  есть нереализованные методы.
    - В классе `TinyCalendar` не все переменные используются `self.calendar`, а есть `self.calenar`
    - Отсутствует полная документация в формате RST для функций и классов.
    - Не всегда корректно используется `textwrap.dedent`, в одном месте `textwrap`, в другом `utils.dedent`.

**Рекомендации по улучшению**:

-   Использовать `from src.logger import logger` для логирования ошибок.
-   Заменить `json.loads` на `j_loads` из `src.utils.jjson`.
-   Добавить RST-документацию для всех классов, методов и функций.
-   Устранить несоответствия в именовании переменных, например `self.calenar` исправить на `self.calendar`.
-   Использовать `utils.dedent` вместо `textwrap.dedent` для единообразия.
-   Реализовать заглушки методов в `TinyCalendar`.
-   Удалить `textwrap`, так как `utils.dedent` делает тоже самое.
-   Добавить проверки на типы данных.

**Оптимизированный код**:

```python
"""
Модуль для работы с инструментами агентов.
============================================

Этот модуль содержит базовый класс :class:`TinyTool` и его производные классы,
которые представляют различные инструменты, доступные агентам.
Инструменты позволяют агентам выполнять специализированные задачи, такие как
ведение календаря и обработка текстовых документов.

Пример использования:
----------------------
.. code-block:: python

    from tinytroupe.tools import TinyWordProcessor
    from src.logger import logger
    
    tool = TinyWordProcessor(owner='Agent1')
    tool.write_document(title='Example Document', content='This is an example document.', author='Agent1')
"""
import copy
from pathlib import Path
# from typing import List, Dict, Optional
# from textwrap import dedent #удаляем так как есть utils.dedent
from src.logger import logger  # исправлено: импорт logger
from src.utils.jjson import j_loads  # исправлено: импорт j_loads
import tinytroupe.utils as utils
from tinytroupe.extraction import ArtifactExporter
from tinytroupe.enrichment import TinyEnricher
from tinytroupe.utils import JsonSerializableRegistry


class TinyTool(JsonSerializableRegistry):
    """
    Базовый класс для всех инструментов агентов.

    Этот класс предоставляет основные методы и атрибуты для управления инструментами,
    включая проверку владельца, управление побочными эффектами и обработку действий.

    :param name: Название инструмента.
    :type name: str
    :param description: Описание инструмента.
    :type description: str
    :param owner: Владелец инструмента (агент).
    :type owner: str, optional
    :param real_world_side_effects: Указывает, имеет ли инструмент побочные эффекты в реальном мире.
    :type real_world_side_effects: bool, optional
    :param exporter: Экспортер для сохранения артефактов.
    :type exporter: ArtifactExporter, optional
    :param enricher: Обогатитель контента.
    :type enricher: TinyEnricher, optional

    """
    def __init__(self, name, description, owner=None, real_world_side_effects=False, exporter=None, enricher=None):
        """
        Инициализация нового инструмента.
        """
        self.name = name
        self.description = description
        self.owner = owner
        self.real_world_side_effects = real_world_side_effects
        self.exporter = exporter
        self.enricher = enricher

    def _process_action(self, agent, action: dict) -> bool:
        """
        Абстрактный метод для обработки действия.

        :param agent: Агент, выполняющий действие.
        :type agent: object
        :param action: Словарь, содержащий информацию о действии.
        :type action: dict
        :raises NotImplementedError: Если метод не реализован в подклассе.
        """
        raise NotImplementedError("Subclasses must implement this method.")
    
    def _protect_real_world(self):
        """
        Предупреждает о побочных эффектах в реальном мире.
        """
        if self.real_world_side_effects:
            logger.warning(f" !!!!!!!!!! Tool {self.name} has REAL-WORLD SIDE EFFECTS. This is NOT just a simulation. Use with caution. !!!!!!!!!!")
        
    def _enforce_ownership(self, agent):
        """
        Проверяет, имеет ли агент право использовать инструмент.

        :param agent: Агент, пытающийся использовать инструмент.
        :type agent: object
        :raises ValueError: Если агент не является владельцем инструмента.
        """
        if self.owner is not None and agent.name != self.owner.name:
            raise ValueError(f"Agent {agent.name} does not own tool {self.name}, which is owned by {self.owner.name}.")
    
    def set_owner(self, owner):
        """
        Устанавливает владельца инструмента.

        :param owner: Агент, который становится владельцем инструмента.
        :type owner: object
        """
        self.owner = owner

    def actions_definitions_prompt(self) -> str:
        """
        Абстрактный метод для генерации подсказок по действиям.

         :raises NotImplementedError: Если метод не реализован в подклассе.
        """
        raise NotImplementedError("Subclasses must implement this method.")
    
    def actions_constraints_prompt(self) -> str:
        """
        Абстрактный метод для генерации подсказок по ограничениям.
        
         :raises NotImplementedError: Если метод не реализован в подклассе.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def process_action(self, agent, action: dict) -> bool:
        """
        Обрабатывает действие агента.

        :param agent: Агент, выполняющий действие.
        :type agent: object
        :param action: Словарь, содержащий информацию о действии.
        :type action: dict
        :return: True, если действие успешно обработано, иначе False.
        :rtype: bool
        """
        self._protect_real_world()
        self._enforce_ownership(agent)
        return self._process_action(agent, action)


class TinyCalendar(TinyTool):
    """
    Инструмент для управления календарем.

    Позволяет агентам добавлять и находить события в календаре.
    """
    def __init__(self, owner=None):
        """
        Инициализация календаря.

        :param owner: Владелец календаря (агент).
        :type owner: str, optional
        """
        super().__init__("calendar", "A basic calendar tool that allows agents to keep track meetings and appointments.", owner=owner, real_world_side_effects=False)
        
        # maps date to list of events. Each event itself is a dictionary with keys "title", "description", "owner", "mandatory_attendees", "optional_attendees", "start_time", "end_time"
        self.calendar = {} # исправлено calenar -> calendar
    
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
        :param mandatory_attendees: Список обязательных участников.
        :type mandatory_attendees: list, optional
        :param optional_attendees: Список дополнительных участников.
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
        Находит события в календаре по дате и времени.

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
        :return: Список событий, соответствующих критериям поиска.
        :rtype: list
        """
        # TODO: Реализовать поиск событий
        pass

    def _process_action(self, agent, action) -> bool:
        """
        Обрабатывает действия с календарем.

        :param agent: Агент, выполняющий действие.
        :type agent: object
        :param action: Словарь, содержащий информацию о действии.
        :type action: dict
        :return: True, если действие успешно обработано, иначе False.
        :rtype: bool
        """
        if action.get('type') == "CREATE_EVENT" and action.get('content') is not None: # исправлено: проверка через get
            # parse content json
            try:
                event_content = j_loads(action['content']) # исправлено: использование j_loads
            except Exception as e:
                logger.error(f"Error parsing JSON content: {e}. Original content: {action.get('content')}")
                return False
            
            # checks whether there are any kwargs that are not valid
            valid_keys = ["title", "description", "mandatory_attendees", "optional_attendees", "start_time", "end_time"]
            utils.check_valid_fields(event_content, valid_keys)

            # uses the kwargs to create a new event
            self.add_event(**event_content)

            return True
        else:
            return False

    def actions_definitions_prompt(self) -> str:
        """
        Возвращает описание возможных действий для календаря.

        :return: Описание возможных действий.
        :rtype: str
        """
        prompt = """
              - CREATE_EVENT: You can create a new event in your calendar. The content of the event has many fields, and you should use a JSON format to specify them. Here are the possible fields:
                * title: The title of the event. Mandatory.
                * description: A brief description of the event. Optional.
                * mandatory_attendees: A list of agent names who must attend the event. Optional.
                * optional_attendees: A list of agent names who are invited to the event, but are not required to attend. Optional.
                * start_time: The start time of the event. Optional.
                * end_time: The end time of the event. Optional.
            """
        # TODO how the atendee list will be handled? How will they be notified of the invitation? I guess they must also have a calendar themselves. <-------------------------------------

        return utils.dedent(prompt)
    
    def actions_constraints_prompt(self) -> str:
        """
        Возвращает ограничения для действий календаря.

        :return: Ограничения для действий.
        :rtype: str
        """
        prompt = """
              
            """
            # TODO: добавить ограничения
        return utils.dedent(prompt)
    

class TinyWordProcessor(TinyTool):
    """
    Инструмент для обработки текстовых документов.

    Позволяет агентам создавать и редактировать документы.
    """
    def __init__(self, owner=None, exporter=None, enricher=None):
        """
        Инициализация текстового процессора.

        :param owner: Владелец инструмента.
        :type owner: str, optional
        :param exporter: Экспортер для сохранения документов.
        :type exporter: ArtifactExporter, optional
        :param enricher: Обогатитель контента.
        :type enricher: TinyEnricher, optional
        """
        super().__init__("wordprocessor", "A basic word processor tool that allows agents to write documents.", owner=owner, real_world_side_effects=False, exporter=exporter, enricher=enricher)
        
    def write_document(self, title, content, author=None):
        """
        Создает новый документ.

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
        Обрабатывает действия с текстовым процессором.

        :param agent: Агент, выполняющий действие.
        :type agent: object
        :param action: Словарь, содержащий информацию о действии.
        :type action: dict
        :return: True, если действие успешно обработано, иначе False.
        :rtype: bool
        """
        try:
            if action.get('type') == "WRITE_DOCUMENT" and action.get('content') is not None: # исправлено: проверка через get
                # parse content json
                if isinstance(action['content'], str):
                    doc_spec = j_loads(action['content']) # исправлено: использование j_loads
                else:
                    doc_spec = action['content']
                
                # checks whether there are any kwargs that are not valid
                valid_keys = ["title", "content", "author"]
                utils.check_valid_fields(doc_spec, valid_keys)

                # uses the kwargs to create a new document
                self.write_document(**doc_spec)

                return True
            else:
                return False
        except Exception as e: # Исправлено: обрабатываем все исключения
            logger.error(f"Error processing document action: {e}. Original content: {action.get('content')}") # исправлено логирование
            return False

    def actions_definitions_prompt(self) -> str:
        """
        Возвращает описание возможных действий для текстового процессора.

        :return: Описание возможных действий.
        :rtype: str
        """
        prompt = """
            - WRITE_DOCUMENT: you can create a new document. The content of the document has many fields, and you should use a JSON format to specify them. Here are the possible fields:
                * title: The title of the document. Mandatory.
                * content: The actual content of the document. You **must** use Markdown to format this content. Mandatory.
                * author: The author of the document. You should put your own name. Optional.
            """
        return utils.dedent(prompt)
    
    def actions_constraints_prompt(self) -> str:
        """
        Возвращает ограничения для действий текстового процессора.

        :return: Ограничения для действий.
        :rtype: str
        """
        prompt = """
            - Whenever you WRITE_DOCUMENT, you write all the content at once. Moreover, the content should be long and detailed, unless there's a good reason for it not to be.
            - When you WRITE_DOCUMENT, you follow these additional guidelines:
                * For any milestones or timelines mentioned, try mentioning specific owners or partner teams, unless there's a good reason not to do so.
            """
        return utils.dedent(prompt)