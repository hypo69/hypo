## <алгоритм>

### Общая схема тестирования TinyPerson
1. **Инициализация:**
   - Запускается pytest, который автоматически находит и выполняет тестовые функции.
   - Логгер `tinytroupe` инициализируется для записи отладочных сообщений.
   - Добавляются пути к директориям проекта в `sys.path` для корректного импорта модулей (что не рекомендуется, лучше использовать пакетный импорт).
   - Импортируются функции `create_oscar_the_architect` и `create_lisa_the_data_scientist` для создания тестовых агентов.
   - Импортируются вспомогательные функции тестирования `testing_utils`.

2. **Тесты (основной цикл):**
   - Для каждой тестовой функции:
      - Создается экземпляр агента `Oscar` и `Lisa` (оба наследники от `TinyPerson`).
      - Выполняются действия, специфичные для теста (описаны ниже).
      - Делаются утверждения (assert), чтобы убедиться, что агенты работают как ожидается.
   - Тестовые функции включают:
      - **test_act**: Проверяет, что агент выполняет как минимум одно действие, включая `TALK` и завершающее `DONE`.
      - **test_listen**: Проверяет, что агент принимает реплики и обновляет свою память.
      - **test_define**: Проверяет, что агент сохраняет и использует заданные конфигурации.
      - **test_define_several**: Проверяет, что агент сохраняет несколько параметров в группу.
      - **test_socialize**: Проверяет, что агент взаимодействует с другими агентами.
      - **test_see**: Проверяет, что агент реагирует на визуальные стимулы и записывает их в память.
      - **test_think**: Проверяет, что агент реагирует на свои мысли и формирует намерения.
      - **test_internalize_goal**: Проверяет, что агент реагирует на цели и формирует планы.
      - **test_move_to**: Проверяет, что агент изменяет свое местоположение и контекст.
      - **test_change_context**: Проверяет, что агент меняет контекст.
      - **test_save_spec**: Проверяет, что агент сохраняет свою спецификацию в файл и загружает ее.

3. **test_act**:
   - Создаются агенты Оскар и Лиза.
   - Для каждого агента выполняется запрос `Tell me a bit about your life.` и возвращаются действия.
   - Проверяется, что количество действий не менее 1, и что они содержат тип `TALK` и завершаются `DONE`.

4. **test_listen**:
   - Создаются агенты Оскар и Лиза.
   - Для каждого агента выполняется действие `listen("Hello, how are you?")`.
   - Проверяется, что сообщения были добавлены в память, последняя роль была `user` , тип стимула `CONVERSATION` и контент соответствовал ожидаемому.

5. **test_define**:
   - Создаются агенты Оскар и Лиза.
   - Сохраняется оригинальный промпт.
   - Выполняется `define('age', 25)`.
   - Проверяется, что значение `age` добавлено в конфигурацию, промпт изменился и содержит значение `age`.

6. **test_define_several**:
   - Создаются агенты Оскар и Лиза.
   - Выполняется `define_several(group="skills", records=["Python", "Machine learning", "GPT-3"])`.
   - Проверяется, что каждое значение добавилось в группу `skills`.

7. **test_socialize**:
   - Создаются агенты Оскар и Лиза.
   - Агент Оскар устанавливает Лизу как доступную, и наоборот.
   - Агенты обмениваются приветствиями.
   - Проверяется, что агент выполняет как минимум одно действие, тип `TALK` и упоминание имени другого агента.

8. **test_see**:
   - Создаются агенты Оскар и Лиза.
   - Для каждого агента выполняется действие `see("A beautiful sunset over the ocean.")`.
   - Проверяется, что агент выполняет как минимум одно действие, тип `THINK` и упоминание `sunset`.

9. **test_think**:
    - Создаются агенты Оскар и Лиза.
    - Для каждого агента выполняется действие `think("I will tell everyone right now how awesome life is!")`.
    - Проверяется, что агент выполняет как минимум одно действие, тип `TALK` и упоминание `life`.

10. **test_internalize_goal**:
    - Создаются агенты Оскар и Лиза.
    - Для каждого агента выполняется действие `internalize_goal("I want to learn more about GPT-3.")`.
    - Проверяется, что агент выполняет как минимум одно действие, тип `SEARCH` и упоминание `GPT-3`.

11. **test_move_to**:
    - Создаются агенты Оскар и Лиза.
    - Для каждого агента выполняется действие `move_to("New York", context=["city", "busy", "diverse"])`.
    - Проверяется, что текущее местоположение агента изменилось и контекст также обновился.

12. **test_change_context**:
     - Создаются агенты Оскар и Лиза.
     - Для каждого агента выполняется действие `change_context(["home", "relaxed", "comfortable"])`.
     - Проверяется, что текущий контекст агента изменился.

13. **test_save_spec**:
    - Создаются агенты Оскар и Лиза.
    - Спецификация агента сохраняется в файл, и проверяется наличие файла.
    - Загружается спецификация агента из файла.
    - Проверяется, что загруженный агент имеет ожидаемое имя, и что его конфигурация соответствует оригиналу.

### Поток данных
- Агенты создаются через функции `create_oscar_the_architect` и `create_lisa_the_data_scientist`.
- Действия агентов (`listen`, `act`, `define`, `define_several`, `make_agent_accessible`, `see`, `think`, `internalize_goal`, `move_to`, `change_context`, `save_spec`, `load_spec`) взаимодействуют с внутренними состояниями агента (сообщения, память, конфигурация).
- Вспомогательные функции `testing_utils` используются для проверок (например, `contains_action_type`, `terminates_with_action_type`, `contains_action_content`).
- Результаты тестов выводятся через `assert`.

## <mermaid>
```mermaid
flowchart TD
    Start[Start Test] --> CreateAgents[Create Oscar and Lisa Agents];
    
    subgraph test_act
    CreateAgents --> testAct_loop[Loop for Each Agent]
    testAct_loop --> ListenAndAct[agent.listen_and_act("Tell me a bit about your life.", return_actions=True)]
    ListenAndAct --> AssertActionsLength[assert len(actions) >= 1]
    AssertActionsLength --> AssertTalkAction[assert contains_action_type(actions, "TALK")]
    AssertTalkAction --> AssertDoneAction[assert terminates_with_action_type(actions, "DONE")]
    AssertDoneAction --> testAct_loop_next[Next Agent or End test_act]
    end
        testAct_loop_next --> test_listen[Test Listen]
    
    subgraph test_listen
    CreateAgents --> testListen_loop[Loop for Each Agent]
    testListen_loop --> ListenMethod[agent.listen("Hello, how are you?")]
    ListenMethod --> AssertMessageLength[assert len(agent.current_messages) > 0]
    AssertMessageLength --> AssertUserRole[assert agent.episodic_memory.retrieve_all()[-1]['role'] == 'user']
    AssertUserRole --> AssertConversationType[assert agent.episodic_memory.retrieve_all()[-1]['content']['stimuli'][0]['type'] == 'CONVERSATION']
    AssertConversationType --> AssertMessageContent[assert agent.episodic_memory.retrieve_all()[-1]['content']['stimuli'][0]['content'] == 'Hello, how are you?']
    AssertMessageContent --> testListen_loop_next[Next Agent or End test_listen]
    end
    testListen_loop_next --> test_define[Test Define]
    
    subgraph test_define
    CreateAgents --> testDefine_loop[Loop for Each Agent]
    testDefine_loop --> SaveOriginalPrompt[original_prompt = agent.current_messages[0]['content']]
    SaveOriginalPrompt --> DefineValue[agent.define('age', 25)]
    DefineValue --> AssertConfigValue[assert agent._configuration['age'] == 25]
    AssertConfigValue --> AssertPromptChanged[assert agent.current_messages[0]['content'] != original_prompt]
    AssertPromptChanged --> AssertPromptContainsValue[assert '25' in agent.current_messages[0]['content']]
    AssertPromptContainsValue --> testDefine_loop_next[Next Agent or End test_define]
    end
    testDefine_loop_next --> test_define_several[Test Define Several]

     subgraph test_define_several
    CreateAgents --> testDefineSeveral_loop[Loop for Each Agent]
    testDefineSeveral_loop --> DefineSeveralValues[agent.define_several(group="skills", records=["Python", "Machine learning", "GPT-3"])]
    DefineSeveralValues --> AssertPythonSkill[assert "Python" in agent._configuration["skills"]]
    AssertPythonSkill --> AssertMachineLearningSkill[assert "Machine learning" in agent._configuration["skills"]]
    AssertMachineLearningSkill --> AssertGPT3Skill[assert "GPT-3" in agent._configuration["skills"]]
        AssertGPT3Skill --> testDefineSeveral_loop_next[Next Agent or End test_define_several]
    end
     testDefineSeveral_loop_next --> test_socialize[Test Socialize]

    subgraph test_socialize
    CreateAgents --> Socialize_Setup[an_oscar = create_oscar_the_architect(); a_lisa = create_lisa_the_data_scientist()]
    Socialize_Setup --> Socialize_loop[Loop for Each Agent]
        Socialize_loop --> DefineOtherAgent[other = a_lisa if agent.name == "Oscar" else an_oscar]
    DefineOtherAgent --> MakeAccessible[agent.make_agent_accessible(other, relation_description="My friend")]
    MakeAccessible --> AgentListen[agent.listen(f"Hi {agent.name}, I am {other.name}.")]
        AgentListen --> AgentAct[actions = agent.act(return_actions=True)]
    AgentAct --> AssertSocializeActionsLength[assert len(actions) >= 1]
    AssertSocializeActionsLength --> AssertSocializeTalkAction[assert contains_action_type(actions, "TALK")]
        AssertSocializeTalkAction --> AssertSocializeMentionOther[assert contains_action_content(actions, other.name)]
        AssertSocializeMentionOther --> Socialize_loop_next[Next Agent or End test_socialize]
    end
     Socialize_loop_next --> test_see[Test See]
    
    subgraph test_see
     CreateAgents --> testSee_loop[Loop for Each Agent]
    testSee_loop --> AgentSee[agent.see("A beautiful sunset over the ocean.")]
     AgentSee --> AgentActSee[actions = agent.act(return_actions=True)]
    AgentActSee --> AssertSeeActionsLength[assert len(actions) >= 1]
        AssertSeeActionsLength --> AssertSeeThinkAction[assert contains_action_type(actions, "THINK")]
    AssertSeeThinkAction --> AssertSeeMentionContent[assert contains_action_content(actions, "sunset")]
    AssertSeeMentionContent --> testSee_loop_next[Next Agent or End test_see]
    end
    testSee_loop_next --> test_think[Test Think]
   
   subgraph test_think
    CreateAgents --> testThink_loop[Loop for Each Agent]
    testThink_loop --> AgentThink[agent.think("I will tell everyone right now how awesome life is!")]
        AgentThink --> AgentActThink[actions = agent.act(return_actions=True)]
    AgentActThink --> AssertThinkActionsLength[assert len(actions) >= 1]
    AssertThinkActionsLength --> AssertThinkTalkAction[assert contains_action_type(actions, "TALK")]
        AssertThinkTalkAction --> AssertThinkMentionContent[assert contains_action_content(actions, "life")]
         AssertThinkMentionContent --> testThink_loop_next[Next Agent or End test_think]
    end
    testThink_loop_next --> test_internalize_goal[Test Internalize Goal]
    
    subgraph test_internalize_goal
    CreateAgents --> testInternalize_loop[Loop for Each Agent]
    testInternalize_loop --> InternalizeGoal[agent.internalize_goal("I want to learn more about GPT-3.")]
    InternalizeGoal --> AgentActInternalize[actions = agent.act(return_actions=True)]
    AgentActInternalize --> AssertInternalizeActionsLength[assert len(actions) >= 1]
        AssertInternalizeActionsLength --> AssertInternalizeSearchAction[assert contains_action_type(actions, "SEARCH")]
    AssertInternalizeSearchAction --> AssertInternalizeMentionContent[assert contains_action_content(actions, "GPT-3")]
      AssertInternalizeMentionContent --> testInternalize_loop_next[Next Agent or End test_internalize_goal]
    end
    testInternalize_loop_next --> test_move_to[Test Move To]
    
    subgraph test_move_to
    CreateAgents --> testMoveTo_loop[Loop for Each Agent]
    testMoveTo_loop --> MoveToLocation[agent.move_to("New York", context=["city", "busy", "diverse"])]
        MoveToLocation --> AssertCurrentLocation[assert agent._configuration["current_location"] == "New York"]
       AssertCurrentLocation --> AssertCityInContext[assert "city" in agent._configuration["current_context"]]
        AssertCityInContext --> AssertBusyInContext[assert "busy" in agent._configuration["current_context"]]
        AssertBusyInContext --> AssertDiverseInContext[assert "diverse" in agent._configuration["current_context"]]
          AssertDiverseInContext --> testMoveTo_loop_next[Next Agent or End test_move_to]
    end
    testMoveTo_loop_next --> test_change_context[Test Change Context]
    
    subgraph test_change_context
    CreateAgents --> testChangeContext_loop[Loop for Each Agent]
    testChangeContext_loop --> ChangeContextMethod[agent.change_context(["home", "relaxed", "comfortable"])]
     ChangeContextMethod --> AssertHomeInContext[assert "home" in agent._configuration["current_context"]]
        AssertHomeInContext --> AssertRelaxedInContext[assert "relaxed" in agent._configuration["current_context"]]
        AssertRelaxedInContext --> AssertComfortableInContext[assert "comfortable" in agent._configuration["current_context"]]
         AssertComfortableInContext --> testChangeContext_loop_next[Next Agent or End test_change_context]
    end
    testChangeContext_loop_next --> test_save_spec[Test Save Spec]
    
   subgraph test_save_spec
     CreateAgents --> testSaveSpec_loop[Loop for Each Agent]
    testSaveSpec_loop --> SaveSpecMethod[agent.save_spec(get_relative_to_test_path(f"test_exports/serialization/{agent.name}.tinyperson.json"), include_memory=True)]
      SaveSpecMethod --> AssertFileExists[assert os.path.exists(get_relative_to_test_path(f"test_exports/serialization/{agent.name}.tinyperson.json"))]
    AssertFileExists --> LoadSpecMethod[loaded_agent = TinyPerson.load_spec(get_relative_to_test_path(f"test_exports/serialization/{agent.name}.tinyperson.json"), new_agent_name=loaded_name)]
     LoadSpecMethod --> AssertLoadedAgentName[assert loaded_agent.name == loaded_name]
        AssertLoadedAgentName --> AssertConfigEqual[assert agents_configs_are_equal(agent, loaded_agent, ignore_name=True)]
          AssertConfigEqual --> testSaveSpec_loop_next[Next Agent or End test_save_spec]
    end
     testSaveSpec_loop_next --> End[End Test]
```

### Зависимости `mermaid`:

1.  `flowchart TD`: Объявляет, что это диаграмма потока.
2.  `Start[Start Test]`: Начало тестового процесса.
3.  `CreateAgents[Create Oscar and Lisa Agents]`: Создание экземпляров агентов Oscar и Lisa.
4.  `testAct_loop`, `testListen_loop`, `testDefine_loop`, `testDefineSeveral_loop`, `Socialize_loop`, `testSee_loop`, `testThink_loop`, `testInternalize_loop`, `testMoveTo_loop`, `testChangeContext_loop`, `testSaveSpec_loop`: циклы для каждого агента в каждой тестовой функции.
5.  `ListenAndAct`: Вызов метода `listen_and_act` агента и возврат списка действий.
6.  `AssertActionsLength`, `AssertTalkAction`, `AssertDoneAction`: утверждения, проверяющие длину списка действий, тип действия TALK и завершающее действие DONE.
7.  `ListenMethod`: Вызов метода `listen` агента для добавления сообщения.
8.  `AssertMessageLength`, `AssertUserRole`, `AssertConversationType`, `AssertMessageContent`: Утверждения проверяющие длину списка сообщений, роль последнего сообщения, тип стимула и его содержимое.
9.  `SaveOriginalPrompt`: Сохранение оригинального промпта агента.
10. `DefineValue`: Вызов метода `define` для установки значения конфигурации.
11. `AssertConfigValue`, `AssertPromptChanged`, `AssertPromptContainsValue`: Утверждения проверяющие конфигурации агента.
12. `DefineSeveralValues`: Вызов метода `define_several` для установки нескольких значений конфигурации.
13. `AssertPythonSkill`, `AssertMachineLearningSkill`, `AssertGPT3Skill`: Утверждения проверяющие конфигурации агента, связанные со скилами.
14. `Socialize_Setup`: Установка переменных для агентов во время социализации.
15. `DefineOtherAgent`: Установка переменной с другим агентом.
16. `MakeAccessible`: Вызов метода `make_agent_accessible` для установки отношений между агентами.
17. `AgentListen`: Вызов метода `listen` для социального взаимодействия.
18. `AgentAct`: Вызов метода `act` для возвращения действий.
19. `AssertSocializeActionsLength`, `AssertSocializeTalkAction`, `AssertSocializeMentionOther`: Утверждения для социальных взаимодействий.
20. `AgentSee`: Вызов метода `see`.
21. `AgentActSee`: Вызов метода `act` после `see`.
22. `AssertSeeActionsLength`, `AssertSeeThinkAction`, `AssertSeeMentionContent`: Утверждения после `see`.
23. `AgentThink`: Вызов метода `think`.
24. `AgentActThink`: Вызов метода `act` после `think`.
25. `AssertThinkActionsLength`, `AssertThinkTalkAction`, `AssertThinkMentionContent`: Утверждения после `think`.
26. `InternalizeGoal`: Вызов метода `internalize_goal`.
27. `AgentActInternalize`: Вызов метода `act` после `internalize_goal`.
28. `AssertInternalizeActionsLength`, `AssertInternalizeSearchAction`, `AssertInternalizeMentionContent`: Утверждения после `internalize_goal`.
29. `MoveToLocation`: Вызов метода `move_to` для смены локации.
30. `AssertCurrentLocation`, `AssertCityInContext`, `AssertBusyInContext`, `AssertDiverseInContext`: Утверждения после `move_to`.
31. `ChangeContextMethod`: Вызов метода `change_context` для смены контекста.
32. `AssertHomeInContext`, `AssertRelaxedInContext`, `AssertComfortableInContext`: Утверждения после `change_context`.
33. `SaveSpecMethod`: Вызов метода `save_spec` для сохранения конфигурации.
34. `AssertFileExists`: Проверка существования файла после сохранения.
35. `LoadSpecMethod`: Загрузка конфигурации агента из файла.
36. `AssertLoadedAgentName`: Проверка имени загруженного агента.
37. `AssertConfigEqual`: Проверка равенства конфигурации оригинального и загруженного агента.
38. `End[End Test]`: Завершение теста.

## <объяснение>

### Импорты:
-   `pytest`: Фреймворк для написания и запуска тестов.
-   `logging`: Модуль для логирования событий в приложении.
    -   `logger = logging.getLogger("tinytroupe")`: Создается логгер с именем "tinytroupe" для записи отладочной информации.
-   `sys`: Модуль для доступа к параметрам и функциям интерпретатора Python.
    -   `sys.path.insert(0, ...)`: Добавление путей к директориям проекта в `sys.path`. Это необходимо для того, чтобы Python мог находить модули проекта, которые не находятся в стандартных путях. **(Обратите внимание, что изменение sys.path не является лучшей практикой для структурирования проекта. Лучше использовать пакетный импорт)**
-   `tinytroupe.examples`: Импортируются функции `create_oscar_the_architect` и `create_lisa_the_data_scientist` для создания тестовых агентов.
-   `testing_utils`: Импортируются вспомогательные функции для тестирования, такие как `contains_action_type`, `terminates_with_action_type`, `contains_action_content` и `agents_configs_are_equal`.
-  `os`: Импортируется для работы с файловой системой.

### Классы:
-   `TinyPerson`: класс агента, который тестируется в данном файле. Он не импортируется явно, но его методы используются через экземпляры, созданные функциями `create_oscar_the_architect` и `create_lisa_the_data_scientist`.

### Функции:

-   **Тестовые функции**: Все функции, начинающиеся с `test_`, являются тестовыми функциями, которые выполняются pytest.
    -   Каждая тестовая функция принимает аргумент `setup`, который является фикстурой pytest (не показана в коде, но предоставляется pytest).
    -   Внутри каждой тестовой функции создаются агенты Оскар и Лиза (экземпляры `TinyPerson`) и выполняются различные проверки с использованием методов агентов.
-   **`create_oscar_the_architect()`, `create_lisa_the_data_scientist()`:** Функции, создающие и возвращающие экземпляры агентов с предустановленной конфигурацией.
    -   Эти функции импортируются из `tinytroupe.examples` и используются для создания тестовых агентов.
-   **`get_relative_to_test_path(path)`:**  Функция, используемая для получения относительного пути к файлу от пути тестирования.
    -  Этот метод предполагается находиться в `testing_utils`

### Переменные:
-   `logger`: Логгер для записи сообщений.
-   `agent`:  Переменная, которая используется для хранения текущего агента в циклах.
-   `actions`:  Переменная, в которой сохраняются действия агента после вызова `act()` или `listen_and_act()`.
-   `original_prompt`: Переменная, хранящая оригинальный промпт агента перед его изменением.
-  `loaded_name`: Имя загруженного агента.
- `loaded_agent`: Загруженный агент из файла.
- `other`: Другой агент при тестировании социализации.

### Потенциальные ошибки и области для улучшения:

-   **`sys.path.insert`**: Использование `sys.path.insert` не является лучшей практикой, так как это изменяет глобальное состояние интерпретатора Python.
   -  Рекомендуется использовать пакетную структуру и указывать пути относительно рабочей директории или использовать менеджеры пакетов (например, poetry) для разрешения зависимостей.
-   **Повторяющийся код**: В каждом тесте создаются агенты, что можно вынести в фикстуру `pytest`. Это сделает код более чистым и уменьшит дублирование.
-   **Магические строки**: В тестах используются строки, например, `"Tell me a bit about your life."`, `"Hello, how are you?"` и т.д., которые можно вынести в константы, это сделает код более читабельным.
-   **Сложные утверждения**: Некоторые утверждения можно разбить на более мелкие для облегчения отладки.
-   **Отсутствие документации:** Код не содержит подробных комментариев, что затрудняет его понимание, особенно для новых разработчиков.

### Цепочка взаимосвязей с другими частями проекта:

-   Этот файл является частью тестового набора для `tinytroupe`.
-   Тесты используют функции `create_oscar_the_architect` и `create_lisa_the_data_scientist` из модуля `tinytroupe.examples`, подразумевая, что существует какой-то механизм создания тестовых агентов.
-   Тесты используют методы класса `TinyPerson` такие как: `listen`, `act`, `define`, `define_several`, `make_agent_accessible`, `see`, `think`, `internalize_goal`, `move_to`, `change_context`, `save_spec`, `load_spec`, предполагая, что данный класс имеет данную функциональность и является основным классом агента в системе `tinytroupe`.
-   Тесты зависят от вспомогательных функций из `testing_utils`, что говорит о наличии некоторого набора инструментов для тестирования.
-   Функция `save_spec` сохраняет состояние агента в файл, и `load_spec` его загружает, что подразумевает использование какой-то формы сериализации, вероятно, JSON.
-   Тесты используют логгер для записи отладочной информации, что является стандартной практикой для отладки приложений.