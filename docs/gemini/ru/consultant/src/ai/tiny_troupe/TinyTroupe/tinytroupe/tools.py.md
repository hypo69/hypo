## Анализ кода модуля `tools.py`

**Качество кода**
7
-  Плюсы
    - Код разбит на классы, что способствует его структурированию и организации.
    - Используется `logger` для логирования, что помогает в отладке и мониторинге работы программы.
    - Присутствует базовая обработка ошибок, например, `JSONDecodeError` в `TinyWordProcessor`.
    - Используется `JsonSerializableRegistry`, что позволяет сериализовать объекты в JSON.
-  Минусы
    - Отсутствует reStructuredText (RST) документация для модуля, классов и методов.
    - Не все функции и методы имеют docstring.
    - Не используется `from src.logger.logger import logger` для логирования.
    - Стандартный `json.loads` используется вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Есть потенциальные места для улучшения обработки ошибок.
    - Некоторые комментарии после `#` не объясняют код достаточно подробно, а также не приведены в стиле RST.
    - В `TinyCalendar` и `TinyWordProcessor` методы `_process_action` содержат много однотипного кода, который можно вынести в отдельную функцию.
    - В `TinyCalendar`  методе `find_events`  есть  `# TODO` без пояснения.
    - В `TinyCalendar` и `TinyWordProcessor` методах `actions_constraints_prompt` присутствует  `# TODO`.
    - Метод `add_event` в  `TinyCalendar` принимает аргументы, а не словарь.
    - Некоторые docstring не имеют описания параметров и возвращаемых значений.

**Рекомендации по улучшению**
1. Добавить RST-документацию для модуля, классов, методов и переменных.
2. Использовать `from src.logger.logger import logger` для логирования.
3. Заменить `json.loads` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
4. Улучшить обработку ошибок с использованием `logger.error` и `return`.
5. Добавить более подробные комментарии в стиле RST к коду.
6. Рефакторить дублирующийся код в методах `_process_action`.
7. Уточнить и детализировать `# TODO` в коде.
8. В методе `add_event` в  `TinyCalendar` принимать словарь, а не список аргументов.
9. Добавить описания параметров и возвращаемых значений в docstring.

**Оптимизированный код**
```python
"""
Модуль для работы с инструментами агентов
=========================================================================================

Этот модуль определяет базовый класс :class:`TinyTool` и производные от него классы
для реализации различных инструментов, которые могут использовать агенты.
Включает в себя инструменты для работы с календарем (:class:`TinyCalendar`)
и текстовым редактором (:class:`TinyWordProcessor`).

Примеры использования
--------------------

Пример создания и использования инструмента:

.. code-block:: python

    tool = TinyWordProcessor(owner="agent1", exporter=ArtifactExporter(), enricher=TinyEnricher())
    tool.process_action(agent="agent1", action={"type": "WRITE_DOCUMENT", "content": {"title": "My Document", "content": "# Hello", "author": "agent1"}})

"""
import textwrap
#  Импортируем модуль json
#  Модуль copy для создания копий объектов
import copy
#  Импортируем модуль logging
#  Импортируем logger из src.logger.logger
from src.logger.logger import logger
# Импортируем utils
import tinytroupe.utils as utils
# Импортируем ArtifactExporter
from tinytroupe.extraction import ArtifactExporter
# Импортируем TinyEnricher
from tinytroupe.enrichment import TinyEnricher
# Импортируем JsonSerializableRegistry
from tinytroupe.utils import JsonSerializableRegistry
# Импортируем j_loads из src.utils.jjson
from src.utils.jjson import j_loads

class TinyTool(JsonSerializableRegistry):
    """
    Базовый класс для инструментов агентов.

    :param name: Название инструмента.
    :type name: str
    :param description: Краткое описание инструмента.
    :type description: str
    :param owner: Агент, владеющий инструментом. Если None, инструмент может использовать любой агент.
    :type owner: str, optional
    :param real_world_side_effects: Указывает, имеет ли инструмент побочные эффекты в реальном мире.
    :type real_world_side_effects: bool, optional
    :param exporter: Экспортер для сохранения результатов работы инструмента.
    :type exporter: ArtifactExporter, optional
    :param enricher: Обогатитель для улучшения результатов работы инструмента.
    :type enricher: TinyEnricher, optional
    """
    def __init__(self, name, description, owner=None, real_world_side_effects=False, exporter=None, enricher=None):
        """
        Инициализирует новый инструмент.

        :param name: Название инструмента.
        :type name: str
        :param description: Краткое описание инструмента.
        :type description: str
        :param owner: Агент, владеющий инструментом. Если None, инструмент может использовать любой агент.
        :type owner: str, optional
        :param real_world_side_effects: Указывает, имеет ли инструмент побочные эффекты в реальном мире.
        :type real_world_side_effects: bool, optional
        :param exporter: Экспортер для сохранения результатов работы инструмента.
        :type exporter: ArtifactExporter, optional
        :param enricher: Обогатитель для улучшения результатов работы инструмента.
        :type enricher: TinyEnricher, optional
        """
        self.name = name
        self.description = description
        self.owner = owner
        self.real_world_side_effects = real_world_side_effects
        self.exporter = exporter
        self.enricher = enricher

    def _process_action(self, agent, action: dict) -> bool:
        """
        Обрабатывает действие агента. Метод должен быть переопределен в подклассах.

        :param agent: Агент, выполняющий действие.
        :type agent: str
        :param action: Словарь, содержащий информацию о действии.
        :type action: dict
        :raises NotImplementedError: Если метод не реализован в подклассе.
        """
        raise NotImplementedError("Subclasses must implement this method.")
    
    def _protect_real_world(self):
        """
        Предупреждает о реальных побочных эффектах инструмента.
        """
        if self.real_world_side_effects:
            logger.warning(f" !!!!!!!!!! Tool {self.name} has REAL-WORLD SIDE EFFECTS. This is NOT just a simulation. Use with caution. !!!!!!!!!!")
        
    def _enforce_ownership(self, agent):
        """
        Проверяет, имеет ли агент право использовать инструмент.

        :param agent: Агент, пытающийся использовать инструмент.
        :type agent: str
        :raises ValueError: Если агент не является владельцем инструмента.
        """
        if self.owner is not None and agent.name != self.owner.name:
            raise ValueError(f"Agent {agent.name} does not own tool {self.name}, which is owned by {self.owner.name}.")
    
    def set_owner(self, owner):
        """
        Устанавливает владельца инструмента.

        :param owner: Агент, который будет владеть инструментом.
        :type owner: str
        """
        self.owner = owner

    def actions_definitions_prompt(self) -> str:
        """
        Возвращает описание возможных действий инструмента для использования в запросах к языковой модели. Метод должен быть переопределен в подклассах.

        :raises NotImplementedError: Если метод не реализован в подклассе.
        """
        raise NotImplementedError("Subclasses must implement this method.")
    
    def actions_constraints_prompt(self) -> str:
        """
        Возвращает ограничения на действия инструмента. Метод должен быть переопределен в подклассах.

         :raises NotImplementedError: Если метод не реализован в подклассе.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def process_action(self, agent, action: dict) -> bool:
        """
        Обрабатывает действие агента, проверяя владельца и побочные эффекты.

        :param agent: Агент, выполняющий действие.
        :type agent: str
        :param action: Словарь, содержащий информацию о действии.
        :type action: dict
        :return: True, если действие успешно выполнено, иначе False.
        :rtype: bool
        """
        # Выполняется проверка на побочные эффекты в реальном мире
        self._protect_real_world()
        # Выполняется проверка на владение инструментом
        self._enforce_ownership(agent)
        # Выполняется обработка действия
        self._process_action(agent, action)
        

# TODO under development
class TinyCalendar(TinyTool):
    """
    Инструмент для работы с календарем.

    :param owner: Агент, владеющий инструментом.
    :type owner: str, optional
    """
    def __init__(self, owner=None):
        """
        Инициализирует календарь.

        :param owner: Агент, владеющий календарем.
        :type owner: str, optional
        """
        super().__init__("calendar", "A basic calendar tool that allows agents to keep track meetings and appointments.", owner=owner, real_world_side_effects=False)
        
        # Словарь, где ключ - дата, значение - список событий.
        # Каждое событие - словарь с ключами "title", "description", "owner", "mandatory_attendees", "optional_attendees", "start_time", "end_time"
        self.calendar = {}
    
    def add_event(self, event: dict):
        """
        Добавляет событие в календарь.

        :param event: Словарь с данными о событии.
        :type event: dict
        """
        date = event.get('date')
        if date not in self.calendar:
            self.calendar[date] = []
        self.calendar[date].append(event)
    
    def find_events(self, year, month, day, hour=None, minute=None):
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
        """
        # TODO: Реализовать поиск событий по дате и времени
        pass

    def _process_action(self, agent, action) -> bool:
        """
        Обрабатывает действие агента для календаря.

        :param agent: Агент, выполняющий действие.
        :type agent: str
        :param action: Словарь, содержащий информацию о действии.
        :type action: dict
        :return: True, если действие успешно выполнено, иначе False.
        :rtype: bool
        """
        if action['type'] == "CREATE_EVENT" and action['content'] is not None:
            # Код исполняет преобразование JSON контента в словарь Python
            try:
                event_content = j_loads(action['content'])
            except Exception as e:
                 logger.error(f"Ошибка разбора JSON: {e}", exc_info=True)
                 return False
             # Проверка валидности ключей
            valid_keys = ["date", "title", "description", "mandatory_attendees", "optional_attendees", "start_time", "end_time"]
            try:
                utils.check_valid_fields(event_content, valid_keys)
            except ValueError as e:
                logger.error(f"Недопустимые поля в запросе: {e}", exc_info=True)
                return False

            # Выполняется добавление нового события
            self.add_event(event_content)

            return True

        else:
            return False

    def actions_definitions_prompt(self) -> str:
        """
        Возвращает описание возможных действий для календаря.
        
        :return: Строка с описанием действий.
        :rtype: str
        """
        prompt = """
              - CREATE_EVENT: Вы можете создать новое событие в своем календаре. Содержимое события имеет множество полей, и вы должны использовать формат JSON, чтобы указать их. Вот возможные поля:
                * date: Дата события. Обязательное поле.
                * title: Название события. Обязательное поле.
                * description: Краткое описание события. Необязательное поле.
                * mandatory_attendees: Список имен агентов, которые должны присутствовать на событии. Необязательное поле.
                * optional_attendees: Список имен агентов, которые приглашены на событие, но не обязаны присутствовать. Необязательное поле.
                * start_time: Время начала события. Необязательное поле.
                * end_time: Время окончания события. Необязательное поле.
            """
        # TODO: Как будет обрабатываться список участников? Как они будут уведомлены о приглашении? Я думаю, что у них тоже должен быть свой календарь. <-------------------------------------

        return utils.dedent(prompt)
        
    
    def actions_constraints_prompt(self) -> str:
        """
        Возвращает ограничения на действия календаря.
        
        :return: Строка с описанием ограничений.
        :rtype: str
        """
        prompt = """
              
            """
        # TODO
        return textwrap.dedent(prompt)
    

class TinyWordProcessor(TinyTool):
    """
    Инструмент для работы с текстовым редактором.

    :param owner: Агент, владеющий инструментом.
    :type owner: str, optional
    :param exporter: Экспортер для сохранения документов.
    :type exporter: ArtifactExporter, optional
    :param enricher: Обогатитель для улучшения документов.
    :type enricher: TinyEnricher, optional
    """
    def __init__(self, owner=None, exporter=None, enricher=None):
        """
        Инициализирует текстовый редактор.

        :param owner: Агент, владеющий текстовым редактором.
        :type owner: str, optional
        :param exporter: Экспортер для сохранения документов.
        :type exporter: ArtifactExporter, optional
        :param enricher: Обогатитель для улучшения документов.
        :type enricher: TinyEnricher, optional
        """
        super().__init__("wordprocessor", "A basic word processor tool that allows agents to write documents.", owner=owner, real_world_side_effects=False, exporter=exporter, enricher=enricher)
        
    def write_document(self, title, content, author=None):
        """
        Создает и сохраняет документ.

        :param title: Заголовок документа.
        :type title: str
        :param content: Содержание документа.
        :type content: str
        :param author: Автор документа.
        :type author: str, optional
        """
        logger.debug(f"Writing document with title {title} and content: {content}")

        if self.enricher is not None:
            requirements = """
            Превратите любой черновик или набросок в фактический и длинный документ со множеством деталей. Включите таблицы, списки и другие элементы.
            Результат **ДОЛЖЕН** быть как минимум в 5 раз больше исходного содержания по количеству символов - сделайте все возможное, чтобы сделать его таким длинным и подробным.
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
        Обрабатывает действие агента для текстового редактора.

        :param agent: Агент, выполняющий действие.
        :type agent: str
        :param action: Словарь, содержащий информацию о действии.
        :type action: dict
        :return: True, если действие успешно выполнено, иначе False.
        :rtype: bool
        """
        if action['type'] == "WRITE_DOCUMENT" and action['content'] is not None:
             # Код исполняет преобразование JSON контента в словарь Python
            try:
                if isinstance(action['content'], str):
                    doc_spec = j_loads(action['content'])  
                else:
                    doc_spec = action['content']
            except Exception as e:
                 logger.error(f"Ошибка разбора JSON: {e}", exc_info=True)
                 return False
            # Проверка валидности ключей
            valid_keys = ["title", "content", "author"]
            try:
                utils.check_valid_fields(doc_spec, valid_keys)
            except ValueError as e:
                logger.error(f"Недопустимые поля в запросе: {e}", exc_info=True)
                return False
            # Выполняется запись нового документа
            self.write_document(**doc_spec)
            return True

        else:
            return False

    def actions_definitions_prompt(self) -> str:
        """
        Возвращает описание возможных действий для текстового редактора.
        
        :return: Строка с описанием действий.
        :rtype: str
        """
        prompt = """
            - WRITE_DOCUMENT: вы можете создать новый документ. Содержимое документа имеет множество полей, и вы должны использовать формат JSON, чтобы указать их. Вот возможные поля:
                * title: Заголовок документа. Обязательное поле.
                * content: Фактическое содержание документа. Вы **должны** использовать Markdown для форматирования этого содержимого. Обязательное поле.
                * author: Автор документа. Вы должны указать свое имя. Необязательное поле.
            """
        return utils.dedent(prompt)
        
    
    def actions_constraints_prompt(self) -> str:
        """
        Возвращает ограничения на действия текстового редактора.
        
        :return: Строка с описанием ограничений.
        :rtype: str
        """
        prompt = """
            - Всякий раз, когда вы используете WRITE_DOCUMENT, вы записываете все содержимое сразу. Более того, содержимое должно быть длинным и подробным, если нет веской причины для обратного.
            - Когда вы используете WRITE_DOCUMENT, вы следуете этим дополнительным рекомендациям:
                * Для любых упоминаемых вех или сроков старайтесь указывать конкретных владельцев или партнерские команды, если нет веской причины не делать этого.
            """
        return utils.dedent(prompt)