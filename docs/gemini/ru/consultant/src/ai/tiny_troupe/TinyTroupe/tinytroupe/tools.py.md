## Анализ кода модуля `tools.py`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован, используется наследование для создания инструментов.
    - Присутствует базовая обработка ошибок.
    - Используется `logger` для логирования.
    - Есть разделение ответственности между классами инструментов.
    - Применение `JsonSerializableRegistry` для сериализации.
    - Использование `textwrap.dedent` для форматирования строк.
- Минусы
    -  Не все методы и классы имеют docstring.
    -  Не используется `j_loads` или `j_loads_ns` для загрузки json.
    -  Не везде используется `logger.error` вместо `try-except`.
    -  Используется стандартный `json.loads`.
    -  В `TinyCalendar` метод `find_events` не реализован.
    -  В `TinyCalendar` при создании события не проверяются поля `date`.

**Рекомендации по улучшению**

1.  Добавить docstring для всех классов, методов и переменных.
2.  Использовать `j_loads` или `j_loads_ns` для загрузки JSON данных.
3.  Заменить `try-except` на `logger.error` там, где это возможно.
4.  Реализовать метод `find_events` в `TinyCalendar`.
5.  Добавить проверку на валидность `date` при создании события в `TinyCalendar`.
6.  В `TinyCalendar` метод `add_event`  принимает словарь, хотя должен принимать отдельные параметры.
7.  Использовать `from src.logger.logger import logger`.
8.  Использовать одинарные кавычки для строк в коде, двойные только в `print`, `input` и `logger.error`.

**Оптимизированный код**

```python
"""
Модуль для определения инструментов агентов
=========================================================================================

Этот модуль содержит набор классов, которые представляют собой различные инструменты,
доступные для использования агентами. Инструменты позволяют агентам выполнять различные
специализированные задачи, такие как ведение календаря, обработка текста и т.д.

Пример использования
--------------------

Пример использования класса `TinyWordProcessor`:

.. code-block:: python

    exporter = ArtifactExporter()
    enricher = TinyEnricher()
    word_processor = TinyWordProcessor(exporter=exporter, enricher=enricher)
    word_processor.write_document(title='My Document', content='This is a test document.', author='User')
"""
import textwrap
from pathlib import Path
import copy

from src.logger.logger import logger
from src.utils.jjson import j_loads
import src.utils as utils
from tinytroupe.extraction import ArtifactExporter
from tinytroupe.enrichment import TinyEnricher
from tinytroupe.utils import JsonSerializableRegistry


class TinyTool(JsonSerializableRegistry):
    """
    Базовый класс для всех инструментов.

    Args:
        name (str): Имя инструмента.
        description (str): Краткое описание инструмента.
        owner (str, optional): Агент, которому принадлежит инструмент. Если `None`, инструмент может использовать любой агент.
            Defaults to None.
        real_world_side_effects (bool, optional): Указывает, имеет ли инструмент побочные эффекты в реальном мире. Defaults to False.
        exporter (ArtifactExporter, optional): Экспортер для экспорта результатов работы инструмента. Defaults to None.
        enricher (Enricher, optional): Обогатитель для обогащения результатов работы инструмента. Defaults to None.
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
        Абстрактный метод для обработки действия. Должен быть реализован в подклассах.

        Args:
            agent: Агент, выполняющий действие.
            action (dict): Словарь с данными действия.

        Raises:
            NotImplementedError: Если метод не реализован в подклассе.
        """
        raise NotImplementedError('Subclasses must implement this method.')
    
    def _protect_real_world(self):
        """
        Выводит предупреждение, если инструмент имеет побочные эффекты в реальном мире.
        """
        if self.real_world_side_effects:
            logger.warning(f'!!!!!!!!!! Tool {self.name} has REAL-WORLD SIDE EFFECTS. This is NOT just a simulation. Use with caution. !!!!!!!!!!')
        
    def _enforce_ownership(self, agent):
        """
        Проверяет, имеет ли агент право использовать инструмент.

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
        Абстрактный метод для определения подсказки для действий. Должен быть реализован в подклассах.

        Raises:
            NotImplementedError: Если метод не реализован в подклассе.
        """
        raise NotImplementedError('Subclasses must implement this method.')
    
    def actions_constraints_prompt(self) -> str:
        """
        Абстрактный метод для определения подсказки с ограничениями для действий. Должен быть реализован в подклассах.

        Raises:
            NotImplementedError: Если метод не реализован в подклассе.
        """
        raise NotImplementedError('Subclasses must implement this method.')

    def process_action(self, agent, action: dict) -> bool:
        """
        Обрабатывает действие агента.

        Args:
            agent: Агент, выполняющий действие.
            action (dict): Словарь с данными действия.

        Returns:
            bool: `True`, если действие обработано успешно, `False` в противном случае.
        """
        self._protect_real_world()
        self._enforce_ownership(agent)
        return self._process_action(agent, action)


class TinyCalendar(TinyTool):
    """
    Инструмент для ведения календаря.

    Args:
        owner (str, optional): Владелец календаря. Defaults to None.
    """
    def __init__(self, owner=None):
        super().__init__('calendar', 'A basic calendar tool that allows agents to keep track meetings and appointments.', owner=owner, real_world_side_effects=False)
        
        # Словарь, где ключ - дата, значение - список событий. Событие - словарь с ключами "title", "description", "owner", "mandatory_attendees", "optional_attendees", "start_time", "end_time"
        self.calendar = {}
    
    def add_event(self, date, title, description=None, owner=None, mandatory_attendees=None, optional_attendees=None, start_time=None, end_time=None):
        """
        Добавляет событие в календарь.

        Args:
            date: Дата события.
            title: Название события.
            description: Описание события.
            owner: Владелец события.
            mandatory_attendees: Список обязательных участников.
            optional_attendees: Список необязательных участников.
            start_time: Время начала события.
            end_time: Время окончания события.
        """
        if date not in self.calendar:
            self.calendar[date] = []
        self.calendar[date].append({'title': title, 'description': description, 'owner': owner, 'mandatory_attendees': mandatory_attendees, 'optional_attendees': optional_attendees, 'start_time': start_time, 'end_time': end_time})
    
    def find_events(self, year, month, day, hour=None, minute=None):
        """
        Ищет события в календаре.

        Args:
            year: Год события.
            month: Месяц события.
            day: День события.
            hour: Час события.
            minute: Минута события.
        """
        # TODO
        pass

    def _process_action(self, agent, action) -> bool:
        """
        Обрабатывает действие с календарем.

        Args:
            agent: Агент, выполняющий действие.
            action: Словарь с данными действия.

        Returns:
            bool: `True`, если действие обработано успешно, `False` в противном случае.
        """
        if action['type'] == 'CREATE_EVENT' and action['content'] is not None:
            # код исполняет чтение контента из json
            try:
                event_content = j_loads(action['content'])
            except Exception as e:
                logger.error(f'Ошибка при чтении JSON: {e}. Оригинальный контент: {action["content"]}')
                return False
            
            # проверка наличия недопустимых ключей
            valid_keys = ['title', 'description', 'mandatory_attendees', 'optional_attendees', 'start_time', 'end_time', 'date']
            utils.check_valid_fields(event_content, valid_keys)

            # код исполняет добавление события в календарь
            self.add_event(**event_content)

            return True
        else:
            return False

    def actions_definitions_prompt(self) -> str:
        """
        Возвращает строку с описанием возможных действий с календарем.

        Returns:
            str: Строка с описанием действий.
        """
        prompt = """
              - CREATE_EVENT: Вы можете создать новое событие в календаре. Содержимое события имеет много полей, и вы должны использовать формат JSON, чтобы их указать. Вот возможные поля:
                * title: Название события. Обязательное поле.
                * description: Краткое описание события. Необязательное поле.
                * mandatory_attendees: Список имен агентов, которые должны присутствовать на мероприятии. Необязательное поле.
                * optional_attendees: Список имен агентов, которые приглашены на мероприятие, но не обязаны присутствовать. Необязательное поле.
                * start_time: Время начала события. Необязательное поле.
                * end_time: Время окончания события. Необязательное поле.
                * date: Дата события. Обязательное поле.
            """
        # TODO как будет обрабатываться список участников? Как они будут уведомлены о приглашении? Я думаю, что у них тоже должен быть календарь. <-------------------------------------

        return utils.dedent(prompt)
    
    def actions_constraints_prompt(self) -> str:
        """
        Возвращает строку с ограничениями для действий с календарем.

        Returns:
            str: Строка с ограничениями.
        """
        prompt = """
              
            """
            # TODO

        return textwrap.dedent(prompt)
    

class TinyWordProcessor(TinyTool):
    """
    Инструмент для обработки текста.

    Args:
        owner (str, optional): Владелец инструмента. Defaults to None.
        exporter (ArtifactExporter, optional): Экспортер для экспорта документов. Defaults to None.
        enricher (Enricher, optional): Обогатитель для обогащения документов. Defaults to None.
    """

    def __init__(self, owner=None, exporter=None, enricher=None):
        super().__init__('wordprocessor', 'A basic word processor tool that allows agents to write documents.', owner=owner, real_world_side_effects=False, exporter=exporter, enricher=enricher)
        
    def write_document(self, title, content, author=None):
        """
        Создает и сохраняет документ.

        Args:
            title: Заголовок документа.
            content: Содержание документа.
            author: Автор документа.
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
            self.exporter.export(artifact_name=f'{title}.{author}', artifact_data= content, content_type='Document', content_format='md', target_format='md')
            self.exporter.export(artifact_name=f'{title}.{author}', artifact_data= content, content_type='Document', content_format='md', target_format='docx')

            json_doc = {'title': title, 'content': content, 'author': author}
            self.exporter.export(artifact_name=f'{title}.{author}', artifact_data= json_doc, content_type='Document', content_format='md', target_format='json')

    def _process_action(self, agent, action) -> bool:
        """
        Обрабатывает действие с текстовым процессором.

        Args:
            agent: Агент, выполняющий действие.
            action: Словарь с данными действия.

        Returns:
            bool: `True`, если действие обработано успешно, `False` в противном случае.
        """
        try:
            if action['type'] == 'WRITE_DOCUMENT' and action['content'] is not None:
                # код исполняет чтение контента из json
                if isinstance(action['content'], str):
                    try:
                        doc_spec = j_loads(action['content'])
                    except Exception as e:
                         logger.error(f'Ошибка при чтении JSON: {e}. Оригинальный контент: {action["content"]}')
                         return False
                else:
                    doc_spec = action['content']
                
                # проверка наличия недопустимых ключей
                valid_keys = ['title', 'content', 'author']
                utils.check_valid_fields(doc_spec, valid_keys)

                # код исполняет создание нового документа
                self.write_document(**doc_spec)

                return True

            else:
                return False
        except Exception as e:
            logger.error(f'Error processing action: {e}. Original content: {action.get("content")}')
            return False

    def actions_definitions_prompt(self) -> str:
        """
        Возвращает строку с описанием возможных действий с текстовым процессором.

        Returns:
            str: Строка с описанием действий.
        """
        prompt = """
            - WRITE_DOCUMENT: вы можете создать новый документ. Содержимое документа имеет много полей, и вы должны использовать формат JSON, чтобы их указать. Вот возможные поля:
                * title: Название документа. Обязательное поле.
                * content: Фактическое содержание документа. Вы **должны** использовать Markdown для форматирования этого содержания. Обязательное поле.
                * author: Автор документа. Вы должны указать свое имя. Необязательное поле.
            """
        return utils.dedent(prompt)
    
    def actions_constraints_prompt(self) -> str:
        """
        Возвращает строку с ограничениями для действий с текстовым процессором.

        Returns:
            str: Строка с ограничениями.
        """
        prompt = """
            - Whenever you WRITE_DOCUMENT, you write all the content at once. Moreover, the content should be long and detailed, unless there's a good reason for it not to be.
            - When you WRITE_DOCUMENT, you follow these additional guidelines:
                * For any milestones or timelines mentioned, try mentioning specific owners or partner teams, unless there's a good reason not to do so.
            """
        return utils.dedent(prompt)