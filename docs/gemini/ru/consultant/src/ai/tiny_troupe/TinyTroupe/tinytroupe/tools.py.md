# Анализ кода модуля `tools`

**Качество кода: 7/10**

*   **Плюсы:**
    *   Хорошая базовая структура классов `TinyTool`, `TinyCalendar` и `TinyWordProcessor`.
    *   Использование `JsonSerializableRegistry` для регистрации инструментов.
    *   Реализация базовой логики проверки владельца и защиты от реальных побочных эффектов.
    *   Наличие методов для формирования подсказок (`actions_definitions_prompt`, `actions_constraints_prompt`).
    *   Использование `logger` для логирования.
    *   Наличие механизмов для расширения функциональности через `ArtifactExporter` и `TinyEnricher`.
*   **Минусы:**
    *   Неполная реализация методов `find_events` в `TinyCalendar`.
    *   `TODO` комментарии указывают на незавершённость некоторых частей кода (например, обработка приглашений в `TinyCalendar`).
    *   Использование стандартного `json.loads` вместо `j_loads` или `j_loads_ns`.
    *   Отсутствие обработки ошибок при работе с файлами и при экспорте.
    *   Использование `textwrap.dedent` вместо `utils.dedent` в `TinyCalendar`.
    *   Недостаточно подробные docstring для некоторых методов и классов.
    *   Не всегда соблюдается использование одинарных кавычек.
    *   Использование `logging` вместо `from src.logger.logger import logger`
    *   Использование `json.JSONDecodeError` вместо общей обработки ошибок с помощью `logger.error`.
    *   Не всегда используется `utils.dedent` для форматирования строк.

**Рекомендации по улучшению:**

1.  **Импорты:** Добавить импорт `Path` из `pathlib` для будущей работы с путями, а также `from src.logger.logger import logger`.
2.  **Использование `j_loads`:** Заменить все `json.loads` на `j_loads` из `src.utils.jjson`.
3.  **Обработка ошибок:** Улучшить обработку ошибок, используя `logger.error` вместо общих `try-except` блоков.
4.  **Документация:** Добавить docstring в формате RST для всех классов, методов, переменных.
5.  **Комментарии:** Уточнить и добавить комментарии к коду для лучшего понимания.
6.  **Форматирование строк:** Использовать `utils.dedent` вместо `textwrap.dedent` для единообразия.
7.  **Обработка JSON:** Переработать обработку JSON, чтобы использовать `j_loads` из `src.utils.jjson` вместо стандартного `json.loads`.
8.  **Использование кавычек:** Использовать одинарные кавычки (`'`) в Python коде. Двойные только в операциях вывода.
9.  **Улучшения:**
    *   В `TinyCalendar` доработать метод `find_events`.
    *   В `TinyCalendar` реализовать механизм уведомлений для приглашенных агентов.
    *   Добавить обработку ошибок при экспорте в `TinyWordProcessor`.

**Оптимизированный код:**

```python
"""
Tools allow agents to accomplish specialized tasks.
=========================================================================================

Этот модуль содержит класс :class:`TinyTool`, который является базовым классом для всех инструментов, которые могут использовать агенты.
Он также содержит производные классы, такие как :class:`TinyCalendar` и :class:`TinyWordProcessor`,
которые представляют собой конкретные инструменты для управления календарем и работы с текстовыми документами.

Пример использования
--------------------

Пример использования класса `TinyTool`:

.. code-block:: python

    tool = TinyTool(name='example_tool', description='This is an example tool.')
    print(tool.name)
    print(tool.description)

"""
import copy
from pathlib import Path
import textwrap

from src.logger.logger import logger
# from tinytroupe.utils import j_loads
from tinytroupe.extraction import ArtifactExporter
from tinytroupe.enrichment import TinyEnricher
from tinytroupe.utils import JsonSerializableRegistry, j_loads, dedent, check_valid_fields #utils
# from tinytroupe.utils import dedent, check_valid_fields

class TinyTool(JsonSerializableRegistry):
    """
    Базовый класс для всех инструментов.

    Args:
        name (str): Название инструмента.
        description (str): Краткое описание инструмента.
        owner (str, optional): Агент, владеющий инструментом. Если `None`, инструмент может использовать любой агент.
        real_world_side_effects (bool, optional): Указывает, имеет ли инструмент реальные побочные эффекты, то есть может ли он изменять состояние мира вне симуляции.
        exporter (ArtifactExporter, optional): Экспортер, используемый для экспорта результатов действий инструмента.
        enricher (TinyEnricher, optional): Обогатитель, используемый для обогащения результатов действий инструмента.
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
        Абстрактный метод для обработки действия. Должен быть переопределен в подклассах.

        Args:
            agent: Агент, выполняющий действие.
            action (dict): Словарь, представляющий действие.

        Raises:
            NotImplementedError: Если метод не переопределен в подклассе.
        """
        raise NotImplementedError('Subclasses must implement this method.')
    
    def _protect_real_world(self):
        """
        Выводит предупреждение, если инструмент имеет реальные побочные эффекты.
        """
        if self.real_world_side_effects:
            logger.warning(f'!!!!!!!!!! Tool {self.name} has REAL-WORLD SIDE EFFECTS. This is NOT just a simulation. Use with caution. !!!!!!!!!!')
        
    def _enforce_ownership(self, agent):
        """
        Проверяет, является ли агент владельцем инструмента.

        Args:
            agent: Агент, пытающийся использовать инструмент.

        Raises:
            ValueError: Если агент не является владельцем инструмента.
        """
        if self.owner is not None and agent.name != self.owner.name:
            raise ValueError(f'Agent {agent.name} does not own tool {self.name}, which is owned by {self.owner.name}.')
    
    def set_owner(self, owner):
        """
        Устанавливает владельца инструмента.

        Args:
             owner: Агент, который становится владельцем инструмента.
        """
        self.owner = owner

    def actions_definitions_prompt(self) -> str:
        """
        Возвращает строку с определением действий инструмента. Должен быть переопределен в подклассах.

        Raises:
             NotImplementedError: Если метод не переопределен в подклассе.
        """
        raise NotImplementedError('Subclasses must implement this method.')
    
    def actions_constraints_prompt(self) -> str:
        """
        Возвращает строку с ограничениями на действия инструмента. Должен быть переопределен в подклассах.

         Raises:
             NotImplementedError: Если метод не переопределен в подклассе.
        """
        raise NotImplementedError('Subclasses must implement this method.')

    def process_action(self, agent, action: dict) -> bool:
        """
        Обрабатывает действие, выполняемое агентом.

        Args:
            agent: Агент, выполняющий действие.
            action (dict): Словарь, представляющий действие.

        Returns:
            bool: `True`, если действие успешно обработано, `False` в противном случае.
        """
        self._protect_real_world()
        self._enforce_ownership(agent)
        return self._process_action(agent, action)

class TinyCalendar(TinyTool):
    """
    Инструмент для ведения календаря.
    Позволяет агентам отслеживать встречи и события.

    Args:
        owner (str, optional): Агент, владеющий инструментом.
    """
    def __init__(self, owner=None):
        super().__init__('calendar', 'A basic calendar tool that allows agents to keep track meetings and appointments.', owner=owner, real_world_side_effects=False)
        # maps date to list of events. Each event itself is a dictionary with keys 'title', 'description', 'owner', 'mandatory_attendees', 'optional_attendees', 'start_time', 'end_time'
        self.calendar = {}
    
    def add_event(self, date, title, description=None, owner=None, mandatory_attendees=None, optional_attendees=None, start_time=None, end_time=None):
        """
        Добавляет событие в календарь.

        Args:
            date (str): Дата события.
            title (str): Название события.
            description (str, optional): Описание события.
            owner (str, optional): Владелец события.
            mandatory_attendees (list, optional): Список обязательных участников.
            optional_attendees (list, optional): Список приглашенных участников.
            start_time (str, optional): Время начала события.
            end_time (str, optional): Время окончания события.
        """
        if date not in self.calendar:
            self.calendar[date] = []
        self.calendar[date].append({'title': title, 'description': description, 'owner': owner, 'mandatory_attendees': mandatory_attendees, 'optional_attendees': optional_attendees, 'start_time': start_time, 'end_time': end_time})
    
    def find_events(self, year, month, day, hour=None, minute=None):
        """
        Находит события в календаре по дате и времени.
        TODO: Реализовать поиск событий.

        Args:
            year (int): Год события.
            month (int): Месяц события.
            day (int): День события.
            hour (int, optional): Час события.
            minute (int, optional): Минута события.
        """
        # TODO
        pass

    def _process_action(self, agent, action) -> bool:
        """
        Обрабатывает действие для инструмента календаря.

        Args:
            agent: Агент, выполняющий действие.
            action (dict): Словарь, представляющий действие.

        Returns:
            bool: `True`, если действие успешно обработано, `False` в противном случае.
        """
        if action['type'] == 'CREATE_EVENT' and action['content'] is not None:
             # Парсинг содержимого json
            try:
                event_content = j_loads(action['content'])
                # Проверка наличия недопустимых ключей
                valid_keys = ['title', 'description', 'mandatory_attendees', 'optional_attendees', 'start_time', 'end_time']
                check_valid_fields(event_content, valid_keys)
                # Создание нового события с использованием переданных аргументов
                self.add_event(**event_content)
                return True
            except Exception as e:
                logger.error(f'Error parsing or adding calendar event: {e}')
                return False
        else:
            return False

    def actions_definitions_prompt(self) -> str:
        """
        Возвращает строку с определением действий инструмента календаря.

        Returns:
             str: Строка с описанием действий.
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

        return dedent(prompt)
    
    def actions_constraints_prompt(self) -> str:
        """
        Возвращает строку с ограничениями на действия инструмента календаря.
        
        Returns:
            str: Строка с описанием ограничений.
        """
        prompt = """
              
            """
            # TODO
        return textwrap.dedent(prompt)

class TinyWordProcessor(TinyTool):
    """
    Инструмент для работы с текстовыми документами.

    Args:
        owner (str, optional): Агент, владеющий инструментом.
        exporter (ArtifactExporter, optional): Экспортер для сохранения документов.
        enricher (TinyEnricher, optional): Обогатитель для расширения контента документов.
    """
    def __init__(self, owner=None, exporter=None, enricher=None):
        super().__init__('wordprocessor', 'A basic word processor tool that allows agents to write documents.', owner=owner, real_world_side_effects=False, exporter=exporter, enricher=enricher)
        
    def write_document(self, title, content, author=None):
        """
        Создает и сохраняет документ.

        Args:
            title (str): Название документа.
            content (str): Содержание документа.
            author (str, optional): Автор документа.
        """
        logger.debug(f'Writing document with title {title} and content: {content}')

        if self.enricher is not None:
            requirements = """
            Turn any draft or outline into an actual and long document, with many, many details. Include tables, lists, and other elements.
            The result **MUST** be at least 5 times larger than the original content in terms of characters - do whatever it takes to make it this long and detailed.
            """
            content = self.enricher.enrich_content(requirements=requirements, 
                                                    content=content, 
                                                    content_type='Document', 
                                                    context_info=None,
                                                    context_cache=None, verbose=False)    
            
        if self.exporter is not None:
            try:
               self.exporter.export(artifact_name=f'{title}.{author}', artifact_data= content, content_type='Document', content_format='md', target_format='md')
               self.exporter.export(artifact_name=f'{title}.{author}', artifact_data= content, content_type='Document', content_format='md', target_format='docx')
               json_doc = {'title': title, 'content': content, 'author': author}
               self.exporter.export(artifact_name=f'{title}.{author}', artifact_data= json_doc, content_type='Document', content_format='md', target_format='json')
            except Exception as e:
                logger.error(f'Error during document export: {e}')

    def _process_action(self, agent, action) -> bool:
        """
        Обрабатывает действие для инструмента текстового процессора.

        Args:
            agent: Агент, выполняющий действие.
            action (dict): Словарь, представляющий действие.

        Returns:
            bool: `True`, если действие успешно обработано, `False` в противном случае.
        """
        try:
            if action['type'] == 'WRITE_DOCUMENT' and action['content'] is not None:
                # Парсинг содержимого json
                if isinstance(action['content'], str):
                    doc_spec = j_loads(action['content'])
                else:
                    doc_spec = action['content']
                
                # Проверка наличия недопустимых ключей
                valid_keys = ['title', 'content', 'author']
                check_valid_fields(doc_spec, valid_keys)
                # Создание нового документа с использованием переданных аргументов
                self.write_document(**doc_spec)
                return True

            else:
                return False
        except Exception as e:
            logger.error(f'Error processing document action: {e}. Original content: {action.get("content")}')
            return False

    def actions_definitions_prompt(self) -> str:
        """
        Возвращает строку с определением действий инструмента текстового процессора.

        Returns:
             str: Строка с описанием действий.
        """
        prompt = """
            - WRITE_DOCUMENT: you can create a new document. The content of the document has many fields, and you should use a JSON format to specify them. Here are the possible fields:
                * title: The title of the document. Mandatory.
                * content: The actual content of the document. You **must** use Markdown to format this content. Mandatory.
                * author: The author of the document. You should put your own name. Optional.
            """
        return dedent(prompt)
        
    
    def actions_constraints_prompt(self) -> str:
        """
        Возвращает строку с ограничениями на действия инструмента текстового процессора.

        Returns:
             str: Строка с описанием ограничений.
        """
        prompt = """
            - Whenever you WRITE_DOCUMENT, you write all the content at once. Moreover, the content should be long and detailed, unless there's a good reason for it not to be.
            - When you WRITE_DOCUMENT, you follow these additional guidelines:
                * For any milestones or timelines mentioned, try mentioning specific owners or partner teams, unless there's a good reason not to do so.
            """
        return dedent(prompt)
```