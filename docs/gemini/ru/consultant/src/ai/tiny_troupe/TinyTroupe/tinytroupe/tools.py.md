## Анализ кода модуля `tools.py`

**Качество кода**
7
-   Плюсы
    - Код достаточно хорошо структурирован, с разделением на классы и методы.
    - Используется логирование для отслеживания действий и ошибок.
    - Присутствует базовая обработка ошибок и валидация входных данных.
    - Есть разделение на классы инструментов с абстрактным базовым классом `TinyTool`.
    - Используется `JsonSerializableRegistry` для регистрации инструментов.
-   Минусы
    - Не все функции и методы имеют docstring в формате reStructuredText (RST).
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.loads`.
    - В некоторых местах используется `try-except` без логирования ошибки через `logger.error`.
    - Присутствуют TODO комментарии, указывающие на незаконченные части функциональности.
    - Не все классы и методы имеют подробные docstring, включая информацию о параметрах и возвращаемых значениях.
    - Отсутствуют явные импорты `Any` и `List` из `typing`.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Необходимо добавить docstring в формате reStructuredText (RST) ко всем функциям, методам и классам.
    -   Документация должна включать описание параметров, возвращаемых значений и исключений.
2.  **Использование `j_loads`**:
    -   Заменить `json.loads` на `j_loads` или `j_loads_ns` из `src.utils.jjson` для загрузки JSON данных.
3.  **Логирование ошибок**:
    -   Использовать `logger.error` для логирования ошибок вместо стандартного `try-except`.
4.  **Обработка исключений**:
    -   Использовать `try-except` только там, где это действительно необходимо, и всегда логировать ошибки.
5.  **Типизация**:
    -   Использовать `typing` для аннотации типов, включая `Any` и `List`.
6.  **TODO**:
    -   Рассмотреть и проработать все TODO комментарии.
7.  **Соответствие стилю**:
    -   Привести код в соответствие с ранее обработанными файлами, включая стили именования и импортов.

**Оптимизированный код**

```python
"""
Модуль для работы с инструментами агентов.
=========================================================================================

Этот модуль содержит классы для создания и управления инструментами,
которые агенты могут использовать для выполнения различных задач.

Пример использования
--------------------

Пример создания инструмента:

.. code-block:: python

    tool = TinyWordProcessor(owner="agent1", exporter=exporter, enricher=enricher)
    action = {"type": "WRITE_DOCUMENT", "content": {"title": "My Document", "content": "# Hello World", "author": "agent1"}}
    tool.process_action(agent="agent1", action=action)
"""
import textwrap
# сохраняем импорт json
import copy
from typing import Any, List
# сохраняем импорт logging
import logging
from src.utils.jjson import j_loads  # импортируем j_loads из src.utils.jjson
from src.logger.logger import logger # импортируем logger
import tinytroupe.utils as utils
from tinytroupe.extraction import ArtifactExporter
from tinytroupe.enrichment import TinyEnricher
from tinytroupe.utils import JsonSerializableRegistry


class TinyTool(JsonSerializableRegistry):
    """
    Базовый класс для инструментов.

    :param name: Название инструмента.
    :type name: str
    :param description: Краткое описание инструмента.
    :type description: str
    :param owner: Агент, владеющий инструментом. Если None, инструмент может использовать любой агент.
    :type owner: str, optional
    :param real_world_side_effects: Флаг, указывающий, имеет ли инструмент реальные побочные эффекты.
    :type real_world_side_effects: bool
    :param exporter: Экспортер, используемый для экспорта результатов.
    :type exporter: ArtifactExporter, optional
    :param enricher: Обогатитель, используемый для обогащения результатов.
    :type enricher: TinyEnricher, optional
    """
    def __init__(self, name: str, description: str, owner: str = None, real_world_side_effects: bool = False, exporter: ArtifactExporter = None, enricher: TinyEnricher = None):
        """
        Инициализирует новый инструмент.
        """
        self.name = name
        self.description = description
        self.owner = owner
        self.real_world_side_effects = real_world_side_effects
        self.exporter = exporter
        self.enricher = enricher

    def _process_action(self, agent: Any, action: dict) -> bool:
        """
        Обрабатывает действие инструмента.

        :param agent: Агент, выполняющий действие.
        :type agent: Any
        :param action: Словарь, представляющий действие.
        :type action: dict
        :raises NotImplementedError: Если метод не реализован в подклассе.
        :return: True, если действие выполнено успешно, False в противном случае.
        :rtype: bool
        """
        raise NotImplementedError("Subclasses must implement this method.")
    
    def _protect_real_world(self):
        """
        Проверяет наличие реальных побочных эффектов и выводит предупреждение.
        """
        if self.real_world_side_effects:
            logger.warning(f" !!!!!!!!!! Tool {self.name} has REAL-WORLD SIDE EFFECTS. This is NOT just a simulation. Use with caution. !!!!!!!!!!")
        
    def _enforce_ownership(self, agent: Any):
        """
        Проверяет, является ли агент владельцем инструмента.

        :param agent: Агент, выполняющий действие.
        :type agent: Any
        :raises ValueError: Если агент не является владельцем инструмента.
        """
        if self.owner is not None and agent.name != self.owner.name:
            raise ValueError(f"Agent {agent.name} does not own tool {self.name}, which is owned by {self.owner.name}.")
    
    def set_owner(self, owner: Any):
        """
        Устанавливает владельца инструмента.

        :param owner: Агент, являющийся владельцем инструмента.
        :type owner: Any
        """
        self.owner = owner

    def actions_definitions_prompt(self) -> str:
        """
        Возвращает подсказку с определениями действий инструмента.

        :raises NotImplementedError: Если метод не реализован в подклассе.
        :return: Подсказка с определениями действий.
        :rtype: str
        """
        raise NotImplementedError("Subclasses must implement this method.")
    
    def actions_constraints_prompt(self) -> str:
        """
        Возвращает подсказку с ограничениями действий инструмента.

        :raises NotImplementedError: Если метод не реализован в подклассе.
        :return: Подсказка с ограничениями действий.
        :rtype: str
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def process_action(self, agent: Any, action: dict) -> bool:
        """
        Обрабатывает действие инструмента, включая проверку побочных эффектов и владения.

        :param agent: Агент, выполняющий действие.
        :type agent: Any
        :param action: Словарь, представляющий действие.
        :type action: dict
        :return: Результат выполнения действия.
        :rtype: bool
        """
        self._protect_real_world()
        self._enforce_ownership(agent)
        return self._process_action(agent, action)


# TODO under development
class TinyCalendar(TinyTool):
    """
    Инструмент для работы с календарем.

    :param owner: Агент, владеющий инструментом. Если None, инструмент может использовать любой агент.
    :type owner: str, optional
    """
    def __init__(self, owner: str = None):
        """
        Инициализирует календарь.
        """
        super().__init__("calendar", "A basic calendar tool that allows agents to keep track meetings and appointments.", owner=owner, real_world_side_effects=False)
        
        # maps date to list of events. Each event itself is a dictionary with keys "title", "description", "owner", "mandatory_attendees", "optional_attendees", "start_time", "end_time"
        self.calendar = {}
    
    def add_event(self, date: str, title: str, description: str = None, owner: str = None, mandatory_attendees: List[str] = None, optional_attendees: List[str] = None, start_time: str = None, end_time: str = None):
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
        :type mandatory_attendees: List[str], optional
        :param optional_attendees: Список приглашенных участников.
        :type optional_attendees: List[str], optional
        :param start_time: Время начала события.
        :type start_time: str, optional
        :param end_time: Время окончания события.
        :type end_time: str, optional
        """
        if date not in self.calendar:
            self.calendar[date] = []
        self.calendar[date].append({"title": title, "description": description, "owner": owner, "mandatory_attendees": mandatory_attendees, "optional_attendees": optional_attendees, "start_time": start_time, "end_time": end_time})
    
    def find_events(self, year: int, month: int, day: int, hour: int = None, minute: int = None):
        """
        Находит события в календаре.

        :param year: Год события.
        :type year: int
        :param month: Месяц события.
        :type month: int
        :param day: День события.
        :type day: int
        :param hour: Час события.
        :type hour: int, optional
        :param minute: Минута события.
        :type minute: int, optional
        :return: Список событий, соответствующих критериям поиска.
        :rtype: List[dict]
        """
        # TODO
        pass

    def _process_action(self, agent: Any, action: dict) -> bool:
        """
        Обрабатывает действие календаря.

        :param agent: Агент, выполняющий действие.
        :type agent: Any
        :param action: Словарь, представляющий действие.
        :type action: dict
        :return: True, если действие выполнено успешно, False в противном случае.
        :rtype: bool
        """
        if action['type'] == "CREATE_EVENT" and action['content'] is not None:
            # Проверяем что контент это строка иначе считаем что это уже словарь
            if isinstance(action['content'], str):
                # используем j_loads для преобразования JSON строки в словарь
                try:
                   event_content = j_loads(action['content'])
                except Exception as e:
                    logger.error(f"Ошибка при разборе JSON: {e}")
                    return False

            else:
                event_content = action['content']
            # Проверяем, что есть недопустимые ключи
            valid_keys = ["title", "description", "mandatory_attendees", "optional_attendees", "start_time", "end_time"]
            utils.check_valid_fields(event_content, valid_keys)

            # Используем kwargs для создания нового события
            self.add_event(**event_content)

            return True

        else:
            return False

    def actions_definitions_prompt(self) -> str:
        """
        Возвращает подсказку с определениями действий календаря.

        :return: Подсказка с определениями действий.
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
        Возвращает подсказку с ограничениями действий календаря.

        :return: Подсказка с ограничениями действий.
        :rtype: str
        """
        prompt = """
              
            """
            # TODO

        return textwrap.dedent(prompt)
    

class TinyWordProcessor(TinyTool):
    """
    Инструмент для работы с текстовым процессором.

    :param owner: Агент, владеющий инструментом. Если None, инструмент может использовать любой агент.
    :type owner: str, optional
    :param exporter: Экспортер, используемый для экспорта результатов.
    :type exporter: ArtifactExporter, optional
    :param enricher: Обогатитель, используемый для обогащения результатов.
    :type enricher: TinyEnricher, optional
    """
    def __init__(self, owner: str = None, exporter: ArtifactExporter = None, enricher: TinyEnricher = None):
        """
        Инициализирует текстовый процессор.
        """
        super().__init__("wordprocessor", "A basic word processor tool that allows agents to write documents.", owner=owner, real_world_side_effects=False, exporter=exporter, enricher=enricher)
        
    def write_document(self, title: str, content: str, author: str = None):
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

    def _process_action(self, agent: Any, action: dict) -> bool:
        """
        Обрабатывает действие текстового процессора.

        :param agent: Агент, выполняющий действие.
        :type agent: Any
        :param action: Словарь, представляющий действие.
        :type action: dict
        :return: True, если действие выполнено успешно, False в противном случае.
        :rtype: bool
        """
        try:
            if action['type'] == "WRITE_DOCUMENT" and action['content'] is not None:
                # Проверяем что контент это строка иначе считаем что это уже словарь
                if isinstance(action['content'], str):
                    # используем j_loads для преобразования JSON строки в словарь
                    try:
                       doc_spec = j_loads(action['content'])
                    except Exception as e:
                        logger.error(f"Ошибка при разборе JSON: {e}")
                        return False
                else:
                    doc_spec = action['content']
                
                # Проверяем, что есть недопустимые ключи
                valid_keys = ["title", "content", "author"]
                utils.check_valid_fields(doc_spec, valid_keys)

                # Используем kwargs для создания нового документа
                self.write_document(**doc_spec)

                return True

            else:
                return False
        except Exception as e:
            logger.error(f"Error parsing JSON content: {e}. Original content: {action['content']}", exc_info=True)
            return False

    def actions_definitions_prompt(self) -> str:
        """
        Возвращает подсказку с определениями действий текстового процессора.

        :return: Подсказка с определениями действий.
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
        Возвращает подсказку с ограничениями действий текстового процессора.

        :return: Подсказка с ограничениями действий.
        :rtype: str
        """
        prompt = """
            - Whenever you WRITE_DOCUMENT, you write all the content at once. Moreover, the content should be long and detailed, unless there's a good reason for it not to be.
            - When you WRITE_DOCUMENT, you follow these additional guidelines:
                * For any milestones or timelines mentioned, try mentioning specific owners or partner teams, unless there's a good reason not to do so.
            """
        return utils.dedent(prompt)