## <алгоритм>

### `TinyPerson` Class

1.  **Инициализация (`__init__`)**:
    *   Принимает `name` (обязательное), `episodic_memory`, `semantic_memory`, и `mental_faculties`.
    *   Сохраняет переданные аргументы, если они не `None`.
    *   `@post_init` гарантирует, что метод `_post_init` будет вызван после `__init__`.
    *   Пример: `agent = TinyPerson(name="Alice", episodic_memory=EpisodicMemory(), semantic_memory=SemanticMemory())`

2.  **Пост-инициализация (`_post_init`)**:
    *   Устанавливает дефолтные значения для `current_messages`, `environment`, `_actions_buffer`, `_accessible_agents`, и `_displayed_communications_buffer`.
    *   Инициализирует `episodic_memory`, `semantic_memory` и `_mental_faculties`, если они не были переданы при создании объекта.
    *   Создаёт дефолтную конфигурацию агента (словарь), включая имя, возраст, местоположение, текущее состояние, цели, эмоции, и т. д.
    *   Определяет путь к файлу с шаблоном для промпта агента (`tinyperson.mustache`).
    *   Вызывает метод `_rename` если передан параметр `new_agent_name` при десериализации.
    *   Регистрирует агента, если не передан параметр `auto_rename` или использует auto_rename + уникальный идентификатор в противном случае.
    *   Вызывает `reset_prompt()` для инициализации промпта.
    *   Добавляет агента в текущую симуляцию, если она существует.
    *   Пример: Автоматически вызывается после `__init__`.

3.  **Переименование (`_rename`)**:
    *   Изменяет имя агента.
    *   Обновляет имя в конфигурации агента.
    *   Пример: `agent._rename("NewName")`.

4.  **Генерация промпта (`generate_agent_prompt`)**:
    *   Читает шаблон промпта из файла `.mustache`.
    *   Создаёт копию текущей конфигурации агента.
    *   Собирает определения действий и ограничения из всех ментальных факультетов.
    *   Добавляет в конфигурацию дополнительные переменные.
    *   Рендерит шаблон с помощью `chevron`.
    *   Пример: `prompt = agent.generate_agent_prompt()`

5.  **Сброс промпта (`reset_prompt`)**:
    *   Генерирует промпт на основе текущей конфигурации.
    *   Устанавливает начальное системное сообщение (`system`) в `current_messages`.
    *   Добавляет недавние сообщения из `episodic_memory` в `current_messages`.
    *   Пример: `agent.reset_prompt()`

6.  **Получение значения конфигурации (`get`)**:
    *   Возвращает значение из конфигурации по ключу, или `None` если ключ отсутствует.
    *   Пример: `age = agent.get("age")`

7.  **Определение значения конфигурации (`define`)**:
    *   Принимает ключ, значение и опционально группу.
    *   Добавляет значение в конфигурацию (в группу или на верхний уровень).
    *   Сбрасывает промпт после обновления конфигурации.
    *   Пример: `agent.define("age", 30)` или `agent.define("skill", "coding", group="skills")`.

8.  **Определение нескольких значений конфигурации (`define_several`)**:
    *   Добавляет список значений в указанную группу.
    *   Пример: `agent.define_several("routines", ["wake up", "go to work", "sleep"])`

9.  **Определение отношений (`define_relationships`)**:
    *   Добавляет или заменяет отношения агента.
    *   Принимает список словарей или один словарь, отображающий имена агентов на описания отношений.
    *    `replace = True` - полностью перезаписывает список отношений, `replace = False` - добавляет новые отношения к текущему списку.
    *   Пример: `agent.define_relationships([{"Name": "Bob", "Description": "Friend"}])`

10. **Очистка отношений (`clear_relationships`)**:
    *   Очищает список отношений агента.
    *   Пример: `agent.clear_relationships()`

11. **Определение отношений с другим агентом (`related_to`)**:
    *   Определяет отношение между двумя агентами.
    *   Также устанавливает симметричное отношение если `symmetric_description` не `None`.
    *   Пример: `agent1.related_to(agent2, "colleague", "colleague")`

12. **Добавление ментальных факультетов (`add_mental_faculties`, `add_mental_faculty`)**:
    *   Добавляет один или несколько ментальных факультетов в список ментальных факультетов агента.
    *    Проверяет, не был ли факультет уже добавлен.
    *   Пример: `agent.add_mental_faculty(RecallFaculty())`

13. **Действие (`act`)**:
    *   Агент выполняет действие, основываясь на своем состоянии и окружении.
    *   Может выполняться либо пока не получит действие `DONE`, либо заданное количество раз (`n`).
    *   Вызывает вспомогательную функцию `aux_act_once` для выполнения одного действия.
    *   Добавляет действие в буфер `_actions_buffer`.
    *   Обновляет внутреннее состояние агента.
    *    Выводит сообщение о действии на экран если `communication_display` = True.
    *   Обрабатывает побочные эффекты действий через ментальные факультеты.
     *  Пример: `agent.act(until_done=True)` или `agent.act(n=3)`

14. **Слушание (`listen`)**:
    *   Агент воспринимает речь как стимул.
    *   Сохраняет в памяти эпизод с типом `CONVERSATION`.
    *   Пример: `agent.listen("Hello, world!", source=another_agent)`

15. **Социализация (`socialize`)**:
    *   Агент воспринимает социальный стимул.
    *   Сохраняет в памяти эпизод с типом `SOCIAL`.
    *   Пример: `agent.socialize("Someone smiled at you.", source=another_agent)`

16. **Зрение (`see`)**:
    *   Агент воспринимает визуальный стимул.
    *   Сохраняет в памяти эпизод с типом `VISUAL`.
    *   Пример: `agent.see("The sky is blue.", source=another_agent)`

17. **Мышление (`think`)**:
    *   Агент думает о чем-то.
    *    Сохраняет в памяти эпизод с типом `THOUGHT`.
    *   Пример: `agent.think("I need to do something.")`

18. **Интернализация цели (`internalize_goal`)**:
    *   Агент интернализирует цель.
    *   Сохраняет в памяти эпизод с типом `INTERNAL_GOAL_FORMULATION`.
    *   Пример: `agent.internalize_goal("Become rich.")`

19. **Наблюдение (`_observe`)**:
    *   Сохраняет стимул в памяти как `user` сообщение.
    *   Выводит сообщение если `communication_display` = True.
    *    Пример: вызывается из `listen`, `see`, `think`, `internalize_goal`

20. **Совместные действия (`listen_and_act`, `see_and_act`, `think_and_act`)**:
    *   Удобные методы для объединения прослушивания/зрения/мышления с действием.
    *   Пример: `agent.listen_and_act("What's up?")`

21. **Чтение документов (`read_documents_from_folder`, `read_documents_from_web`)**:
    *   Загружает документы из папки или URL-адресов в семантическую память.
    *   Пример: `agent.read_documents_from_folder("/path/to/docs")`

22. **Перемещение (`move_to`)**:
    *   Перемещает агента в новое местоположение.
    *   Обновляет контекст агента.
    *   Пример: `agent.move_to("park", ["trees", "people"])`

23. **Изменение контекста (`change_context`)**:
    *   Обновляет контекст агента.
    *   Пример: `agent.change_context(["sunny", "quiet"])`

24. **Добавление доступных агентов (`make_agent_accessible`)**:
    *   Делает агента доступным для взаимодействия с текущим агентом.
    *   Пример: `agent1.make_agent_accessible(agent2)`

25. **Удаление доступных агентов (`make_agent_inaccessible`)**:
    *   Делает агента недоступным для взаимодействия с текущим агентом.
    *   Пример: `agent1.make_agent_inaccessible(agent2)`

26. **Удаление всех доступных агентов (`make_all_agents_inaccessible`)**:
    *   Делает всех агентов недоступными для взаимодействия с текущим агентом.
    *   Пример: `agent1.make_all_agents_inaccessible()`

27. **Формирование сообщения (`_produce_message`)**:
    *   Получает промпт.
    *   Отправляет сообщения в OpenAI API.
    *   Возвращает роль и JSON контент.
    *   Пример: Внутренний метод, вызываемый из `act`.

28. **Обновление когнитивного состояния (`_update_cognitive_state`)**:
    *   Обновляет внутреннее состояние агента (цели, контекст, внимание, эмоции).
    *   Сбрасывает промпт после обновления.
    *   Пример: Внутренний метод, вызываемый из `act`, `_observe`, `move_to`, `change_context`.

29. **Отображение коммуникации (`_display_communication`)**:
    *   Форматирует и отображает коммуникацию на основе типа (стимул или действие).
    *   Вызывает `_push_and_display_latest_communication` чтобы сохранить сообщение в буфер.
    *   Пример: Внутренний метод, вызываемый из `act`, `_observe`.

30. **Сохранение и отображение коммуникации (`_push_and_display_latest_communication`)**:
    *   Сохраняет отрендеренное сообщение в буфер и отображает его.
    *   Пример: Внутренний метод, вызываемый из `_display_communication`.

31.  **Получение и отображение коммуникации (`pop_and_display_latest_communications`)**:
    *   Отображает все сохраненные коммуникации и очищает буфер.
    *   Пример: `communications = agent.pop_and_display_latest_communications()`

32.  **Очистка буфера коммуникации (`clear_communications_buffer`)**:
    *   Очищает буфер сохраненных коммуникаций.
    *   Пример: `agent.clear_communications_buffer()`

33. **Получение последних действий (`pop_latest_actions`)**:
    *   Возвращает и очищает буфер последних действий.
    *   Пример: `actions = agent.pop_latest_actions()`

34.  **Получение контента действий (`pop_actions_and_get_contents_for`)**:
    *   Возвращает контент из действий указанного типа.
    *   Пример: `content = agent.pop_actions_and_get_contents_for("TALK", only_last_action=True)`

35. **Строковое представление (`__repr__`)**:
    *   Возвращает строковое представление агента.
    *   Пример: `print(agent)`

36.  **Мини-биография (`minibio`)**:
    *   Возвращает строку с краткой биографией агента.
    *   Пример: `print(agent.minibio())`

37.  **Отображение текущих взаимодействий (`pp_current_interactions`)**:
    *   Отображает текущие сообщения на экране.
    *   Пример: `agent.pp_current_interactions()`

38. **Получение текущих взаимодействий как форматированной строки (`pretty_current_interactions`)**:
    *   Возвращает отформатированную строку с текущими сообщениями.
    *   Пример: `formatted_interactions = agent.pretty_current_interactions()`

39. **Форматирование стимула (`_pretty_stimuli`)**:
    *   Форматирует стимул для отображения.
    *   Пример: Внутренний метод, вызываемый из `_display_communication`.

40. **Форматирование действия (`_pretty_action`)**:
    *   Форматирует действие для отображения.
    *   Пример: Внутренний метод, вызываемый из `_display_communication`.

41. **Форматирование времени (`_pretty_timestamp`)**:
    *   Форматирует время события для отображения.
    *   Пример: Внутренний метод, вызываемый из `pretty_current_interactions`.

42. **ISO-формат времени (`iso_datetime`)**:
    *   Возвращает текущее время окружения в ISO формате.
    *   Пример: `timestamp = agent.iso_datetime()`

43. **Сохранение спецификации (`save_spec`)**:
    *   Сохраняет спецификацию агента в JSON файл.
    *   Пример: `agent.save_spec("agent.json")`

44. **Загрузка спецификации (`load_spec`)**:
    *   Загружает спецификацию агента из JSON файла.
    *   Пример: `agent = TinyPerson.load_spec("agent.json")`

45.  **Кодирование полного состояния (`encode_complete_state`)**:
    *   Кодирует всё внутреннее состояние агента в словарь, пригодный для сериализации.
    *   Пример: `state = agent.encode_complete_state()`

46. **Декодирование полного состояния (`decode_complete_state`)**:
    *   Декодирует сохранённое состояние и обновляет атрибуты экземпляра `TinyPerson`.
    *   Пример: `agent.decode_complete_state(state)`

47. **Создание нового агента на основе текущего (`create_new_agent_from_current_spec`)**:
    *   Создает нового агента на основе спецификации текущего агента.
    *   Пример: `new_agent = agent.create_new_agent_from_current_spec("NewAgent")`

48. **Добавление агента в список (`add_agent`)**:
    *   Добавляет агента в глобальный список агентов.
    *   Пример: `TinyPerson.add_agent(agent)`

49. **Проверка наличия агента (`has_agent`)**:
    *   Проверяет, зарегистрирован ли агент с указанным именем.
    *   Пример: `exists = TinyPerson.has_agent("Alice")`

50. **Установка симуляции для свободных агентов (`set_simulation_for_free_agents`)**:
    *   Добавляет агентов без симуляции в указанную симуляцию.
    *   Пример: `TinyPerson.set_simulation_for_free_agents(simulation)`

51. **Получение агента по имени (`get_agent_by_name`)**:
    *   Получает агента из глобального списка по имени.
    *   Пример: `agent = TinyPerson.get_agent_by_name("Alice")`

52. **Очистка списка агентов (`clear_agents`)**:
    *   Очищает глобальный список агентов.
    *   Пример: `TinyPerson.clear_agents()`

### `TinyMentalFaculty` Class

1.  **Инициализация (`__init__`)**:
    *   Принимает `name` и список `requires_faculties`.
    *   Сохраняет значения.
    *   Пример: `faculty = TinyMentalFaculty("Reasoning")`

2.  **Строковое представление (`__str__`)**:
    *   Возвращает строковое представление факультета.
    *   Пример: `print(faculty)`

3.  **Сравнение (`__eq__`)**:
    *   Сравнивает два факультета на основе их имени.
    *   Пример: `faculty1 == faculty2`

4.  **Обработка действия (`process_action`)**:
    *   Абстрактный метод, который обрабатывает действие, связанное с факультетом.
    *   Пример: Этот метод нужно переопределять в дочерних классах.

5.  **Определение действий (`actions_definitions_prompt`)**:
    *   Абстрактный метод, который возвращает строку с определениями действий факультета.
    *   Пример: Этот метод нужно переопределять в дочерних классах.

6.  **Ограничения действий (`actions_constraints_prompt`)**:
    *   Абстрактный метод, который возвращает строку с ограничениями действий факультета.
    *   Пример: Этот метод нужно переопределять в дочерних классах.

### `RecallFaculty` Class

1.  **Инициализация (`__init__`)**:
    *   Вызывает конструктор родительского класса с именем "Memory Recall".
    *   Пример: `recall_faculty = RecallFaculty()`

2.  **Обработка действия (`process_action`)**:
    *   Проверяет, является ли действие типом `RECALL`.
    *   Извлекает семантические воспоминания, соответствующие запросу.
    *   Отправляет агенту сообщение о найденной или ненайденной информации.
    *   Пример: `recall_faculty.process_action(agent, {"type": "RECALL", "content": "information about cats"})`

3.  **Определение действий (`actions_definitions_prompt`)**:
    *   Возвращает строку с описанием действия `RECALL`.
    *   Пример: `prompt = recall_faculty.actions_definitions_prompt()`

4.  **Ограничения действий (`actions_constraints_prompt`)**:
    *   Возвращает строку с описанием ограничений действия `RECALL`.
    *   Пример: `prompt = recall_faculty.actions_constraints_prompt()`

### `FilesAndWebGroundingFaculty` Class

1.  **Инициализация (`__init__`)**:
    *   Вызывает конструктор родительского класса с именем "Local Grounding".
    *   Пример: `grounding_faculty = FilesAndWebGroundingFaculty()`

2.  **Обработка действия (`process_action`)**:
    *   Проверяет, является ли действие типом `CONSULT` или `LIST_DOCUMENTS`.
    *   Извлекает контент документа или список документов из семантической памяти.
    *   Отправляет агенту сообщение о найденном контенте или списке документов.
    *   Пример:
        `grounding_faculty.process_action(agent, {"type": "CONSULT", "content": "document1.txt"})`
        `grounding_faculty.process_action(agent, {"type": "LIST_DOCUMENTS", "content": True})`

3.  **Определение действий (`actions_definitions_prompt`)**:
    *   Возвращает строку с описанием действий `LIST_DOCUMENTS` и `CONSULT`.
    *   Пример: `prompt = grounding_faculty.actions_definitions_prompt()`

4.  **Ограничения действий (`actions_constraints_prompt`)**:
    *   Возвращает строку с описанием ограничений действий `LIST_DOCUMENTS` и `CONSULT`.
    *   Пример: `prompt = grounding_faculty.actions_constraints_prompt()`

### `TinyToolUse` Class

1.  **Инициализация (`__init__`)**:
     *   Принимает список инструментов `tools` и вызывает конструктор родительского класса с именем "Tool Use".
     *   Сохраняет список инструментов.
    *   Пример: `tool_use_faculty = TinyToolUse([Tool1(), Tool2()])`

2.  **Обработка действия (`process_action`)**:
    *   Вызывает метод `process_action` для каждого инструмента в списке инструментов, пока какой-либо не вернет `True`.
    *    Возвращает `True` если какой-то инструмент обработал действие, иначе `False`.
    *   Пример: `tool_use_faculty.process_action(agent, {"type": "USE_TOOL_A", "content": "tool_param_1"})`

3. **Определение действий (`actions_definitions_prompt`)**:
    *   Возвращает строку с описаниями действий от всех инструментов.
    *   Пример: `prompt = tool_use_faculty.actions_definitions_prompt()`

4. **Ограничения действий (`actions_constraints_prompt`)**:
    *   Возвращает строку с ограничениями действий от всех инструментов.
    *   Пример: `prompt = tool_use_faculty.actions_constraints_prompt()`

### `TinyMemory` Class

1.  **Хранение значения (`store`)**:
    *   Абстрактный метод для хранения значения.
    *   Пример: Этот метод нужно переопределять в дочерних классах.

2.  **Извлечение значения (`retrieve`)**:
    *   Абстрактный метод для извлечения значений (первых `n` или последних `n`).
    *   Пример: Этот метод нужно переопределять в дочерних классах.

3.  **Извлечение недавних значений (`retrieve_recent`)**:
    *   Абстрактный метод для извлечения последних значений.
    *   Пример: Этот метод нужно переопределять в дочерних классах.

4.  **Извлечение всех значений (`retrieve_all`)**:
    *   Абстрактный метод для извлечения всех значений.
    *   Пример: Этот метод нужно переопределять в дочерних классах.

5.  **Извлечение релевантных значений (`retrieve_relevant`)**:
    *   Абстрактный метод для извлечения релевантных значений.
    *   Пример: Этот метод нужно переопределять в дочерних классах.

### `EpisodicMemory` Class

1.  **Инициализация (`__init__`)**:
    *   Принимает `fixed_prefix_length` и `lookback_length`.
    *   Инициализирует память (список).
    *   Пример: `memory = EpisodicMemory(fixed_prefix_length=50, lookback_length=50)`

2.  **Хранение значения (`store`)**:
    *   Добавляет значение в конец списка.
    *   Пример: `memory.store({"role": "user", "content": "Hello"})`

3.  **Получение количества элементов (`count`)**:
    *   Возвращает количество элементов в памяти.
    *    Пример: `count = memory.count()`

4.  **Извлечение значений (`retrieve`)**:
    *   Извлекает первые `n` и/или последние `n` значения из памяти.
    *   Возвращает все значения если `n=None`.
    *   Пример: `messages = memory.retrieve(first_n=10, last_n=5)`

5.  **Извлечение недавних значений (`retrieve_recent`)**:
    *   Извлекает фиксированный префикс и последние `n` значений.
    *   Пример: `recent_messages = memory.retrieve_recent()`

6.  **Извлечение всех значений (`retrieve_all`)**:
    *   Возвращает копию всех значений.
    *   Пример: `all_messages = memory.retrieve_all()`

7.  **Извлечение релевантных значений (`retrieve_relevant`)**:
    *   Этот метод пока не реализован.
    *   Пример: вызывает ошибку `NotImplementedError`.

8.  **Извлечение первых n значений (`retrieve_first`)**:
    *   Возвращает первые n значений из памяти.
    *   Пример: `messages = memory.retrieve_first(5)`

9. **Извлечение последних n значений (`retrieve_last`)**:
    *   Возвращает последние n значений из памяти.
    *   Пример: `messages = memory.retrieve_last(5)`

### `SemanticMemory` Class

1.  **Инициализация (`__init__`)**:
    *   Принимает списки `documents_paths` и `web_urls`.
    *   Инициализирует пустой `index`, `documents_paths` и `documents_web_urls`.
    *   Вызывает методы `add_documents_paths` и `add_web_urls` для загрузки данных.
    *   Пример: `memory = SemanticMemory(documents_paths=["/docs"], web_urls=["https://example.com"])`

2.  **Извлечение релевантных значений (`retrieve_relevant`)**:
    *   Использует векторное представление текста для поиска наиболее релевантных документов.
    *   Пример: `relevant_documents = memory.retrieve_relevant("AI investments", top_k=3)`

3.  **Получение контента документа по имени (`retrieve_document_content_by_name`)**:
    *   Извлекает контент документа по его имени.
    *   Пример: `content = memory.retrieve_document_content_by_name("document1.txt")`

4.  **Получение имен документов (`list_documents_names`)**:
    *   Возвращает список имен документов в памяти.
    *   Пример: `document_names = memory.list_documents_names()`

5.  **Добавление путей к папкам с документами (`add_documents_paths`)**:
    *   Добавляет список папок с документами в семантическую память.
    *   Пример: `memory.add_documents_paths(["/path/to/docs1", "/path/to/docs2"])`

6.  **Добавление пути к папке с документами (`add_documents_path`)**:
    *   Добавляет папку с документами в семантическую память.
    *   Пример: `memory.add_documents_path("/path/to/docs")`

7.  **Добавление веб-адресов (`add_web_urls`)**:
    *   Добавляет список URL-адресов в семантическую память.
    *   Пример: `memory.add_web_urls(["https://example.com/1", "https://example.com/2"])`

8. **Добавление веб-адреса (`add_web_url`)**:
    *   Добавляет веб-адрес в семантическую память.
    *    Пример: `memory.add_web_url("https://example.com")`

9.  **Добавление документов (`_add_documents`)**:
    *   Индексирует документы и сохраняет их для дальнейшего использования.
    *   Пример: Внутренний метод, вызываемый из `add_documents_path`, `add_web_urls`.

10. **Пост-десериализационная инициализация (`_post_deserialization_init`)**:
     *    Вызывает метод родительского класса.
     *    Вызывает методы `add_documents_paths` и `add_web_urls` для повторной инициализации после десериализации.
     *   Пример: Внутренний метод вызываемый после десериализации

### Поток данных

1.  **Создание `TinyPerson`**:
    *   Инициализация параметров (`__init__`) -> вызов `_post_init`.
    *   `_post_init`: инициализация дефолтных параметров, регистрация, сброс промпта.
2.  **Настройка агента**:
    *   `define` / `define_several`: обновление конфигурации -> `reset_prompt`.
    *   `add_mental_faculty` / `add_mental_faculties`: добавление ментальных факультетов.
    *   `read_documents_from_folder` / `read_documents_from_web`: загрузка документов в семантическую память.
    *   `related_to` / `define_relationships`: определение отношений между агентами.
    *   `move_to` / `change_context`: изменение контекста агента.
3.  **Взаимодействие агента**:
    *   `listen` / `socialize` / `see` / `think` / `internalize_goal` -> `_observe`: сохранение стимула в `episodic_memory`.
    *   `act`: генерация промпта -> отправка сообщения в OpenAI -> обновление когнитивного состояния -> выполнение действия, сохранение действия в `_actions_buffer`.
4.  **Получение информации об агенте**:
    *   `get`: получение значения из конфигурации.
    *   `pp_current_interactions` / `pretty_current_interactions`: форматирование текущих взаимодействий.
    *   `minibio`: получение краткой биографии.
    *   `pop_latest_actions`: получение последних действий.
5.  **Сохранение и загрузка состояния агента**:
    *   `save_spec`: сохранение конфигурации агента в файл.
    *   `load_spec`: загрузка конфигурации агента из файла.
    *   `encode_complete_state`: кодирование полного состояния агента.
    *   `decode_complete_state`: декодирование состояния и создание нового экземпляра агента.
6.  **Использование памяти**:
     *  `EpisodicMemory`: `store` (сохранение), `retrieve`, `retrieve_recent`, `retrieve_first`, `retrieve_last` (извлечение).
     *  `SemanticMemory`: `add_documents_path` / `add_web_urls` (загрузка), `retrieve_relevant`, `retrieve_document_content_by_name`, `list_documents_names` (извлечение).
7. **Использование ментальных факультетов**:
    * `RecallFaculty`:  `process_action`: вызов `retrieve_relevant` из `semantic_memory`.
    * `FilesAndWebGroundingFaculty`: `process_action`: вызов `retrieve_document_content_by_name` / `list_documents_names` из `semantic_memory`.
    * `TinyToolUse`:  `process_action`: вызов `process_action` для каждого инструмента.

## <mermaid>

```mermaid
flowchart TD
    subgraph TinyPerson Class
        A[TinyPerson: __init__] --> B{Check if episodic_memory is not None}
        B -- Yes --> C[Set episodic_memory]
        B -- No --> D
        D --> E{Check if semantic_memory is not None}
        E -- Yes --> F[Set semantic_memory]
        E -- No --> G
        G --> H{Check if mental_faculties is not None}
        H -- Yes --> I[Set mental_faculties]
        H -- No --> J
        J --> K{Assert name is not None}
        K -- True --> L[Set name]
        L --> M[TinyPerson: _post_init]
    
        M --> N[Set current_messages to []]
        N --> O[Set environment to None]
        O --> P[Set _actions_buffer to []]
        P --> Q[Set _accessible_agents to []]
        Q --> R[Set _displayed_communications_buffer to []]
        R --> S{Check if episodic_memory attribute exists}
        S -- No --> T[Set episodic_memory to EpisodicMemory()]
        S -- Yes --> U
        U --> V{Check if semantic_memory attribute exists}
        V -- No --> W[Set semantic_memory to SemanticMemory()]
        V -- Yes --> X
        X --> Y{Check if _mental_faculties attribute exists}
        Y -- No --> Z[Set _mental_faculties to []]
        Y -- Yes --> AA
        AA --> AB[Create _configuration dict]
        AB --> AC[Set _prompt_template_path]
        AC --> AD[Set _init_system_message to None]
        AD --> AE{Check for new_agent_name}
        AE -- Yes --> AF[Call _rename with new_agent_name]
        AE -- No --> AG
        AG --> AH{Check for auto_rename}
        AH -- Yes --> AI[Try _rename with current name and add_agent()]
        AI -- Fail --> AJ[Generate new_id and try _rename again]
        AJ --> AI
        AH -- No --> AK[Call add_agent()]
        AK --> AL[Call reset_prompt()]
        AL --> AM{Check current_simulation}
        AM -- Yes --> AN[Add the agent to current_simulation]
        AM -- No --> AO[Set simulation_id to None]

        AO --> AP[TinyPerson: _rename]
        AP --> AQ[Set self.name to new_name]
        AQ --> AR[Update self._configuration["name"]]
       
        
        
        
    end
    subgraph Action Processing
        AS[TinyPerson: act] --> AT{Check if until_done and n is not None}
        AT -- True --> AU[Raise Assertion Error]
        AT -- False --> AV{Check if n is not None}
        AV -- True --> AW[Repeat aux_act_once n times]
        AV -- False --> AX{Check if until_done}
        AX -- True --> AY[Loop until action is DONE]
        AY --> AZ[Call aux_act_once]
        AZ --> BA
        BA --> BB{Check for maximum actions}
        BB -- Yes --> BC[Log warning and stop loop]
        BB -- No --> BD{Check for action repetition}
        BD -- Yes --> BE[Log warning and stop loop]
        BD -- No --> AY

        AW --> BF
        AY --> BF
        BF --> BG{Check for return_actions}
        BG -- Yes --> BH[Return contents]
    
        subgraph aux_act_once Function
            BI[aux_act_once] --> BJ[Call think function with a generic message]
            BJ --> BK[Call _produce_message to create role and content]
            BK --> BL[Store message to episodic_memory]
            BL --> BM[Get cognitive_state from content]
            BM --> BN[Get action from content]
            BN --> BO[Add action to _actions_buffer]
            BO --> BP[Call _update_cognitive_state