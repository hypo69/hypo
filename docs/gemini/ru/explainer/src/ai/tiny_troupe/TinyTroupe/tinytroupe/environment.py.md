## <алгоритм>

**`TinyWorld` Class:**

1.  **`__init__(self, name, agents, initial_datetime, broadcast_if_no_target)`**:
    *   Инициализирует окружение с заданным именем, списком агентов, начальной датой и временем, а также флагом для широковещания действий при отсутствии цели.
    *   Примеры:
        *   Создание окружения без агентов с текущим временем: `world = TinyWorld(name="MyWorld")`
        *   Создание окружения с несколькими агентами и заданной датой: `world = TinyWorld(name="TestWorld", agents=[agent1, agent2], initial_datetime=datetime(2024, 1, 1))`
        *   Создание окружения с отключенным широковещанием при отсутствии цели: `world = TinyWorld(name="SilentWorld", broadcast_if_no_target=False)`
2.  **`_step(self, timedelta_per_step)`**:
    *   Увеличивает время окружения на `timedelta_per_step`.
    *   Для каждого агента в окружении вызывает `agent.act()` для выполнения действия.
    *   Обрабатывает действия агента с помощью `_handle_actions()`.
    *   Примеры:
        *   Выполнение одного шага с продвижением времени на 1 час: `world._step(timedelta_per_step=timedelta(hours=1))`
        *   Выполнение одного шага без продвижения времени (если `timedelta_per_step=None`): `world._step()`
3.  **`run(self, steps, timedelta_per_step, return_actions)`**:
    *   Циклически выполняет `_step()` указанное количество раз (`steps`).
    *   Отображает информацию о текущем шаге.
    *   Возвращает действия агентов, если `return_actions` равен `True`.
    *   Примеры:
        *   Запуск симуляции на 10 шагов, каждый шаг 1 день: `world.run(steps=10, timedelta_per_step=timedelta(days=1))`
        *   Запуск симуляции на 5 шагов, без возврата действий: `world.run(steps=5)`
        *   Запуск симуляции на 3 шага, с возвратом действий: `actions = world.run(steps=3, return_actions=True)`
4.  **`skip(self, steps, timedelta_per_step)`**:
    *   Увеличивает текущее время на заданное количество шагов без выполнения действий.
    *   Примеры:
        *   Пропуск 5 шагов по 1 часу: `world.skip(steps=5, timedelta_per_step=timedelta(hours=1))`
        *   Пропуск 2 дней: `world.skip(steps=2, timedelta_per_step=timedelta(days=1))`
5.  **`add_agent(self, agent)`**:
    *   Добавляет агента в окружение. Проверяет уникальность имени агента.
    *   Примеры:
        *   Добавление агента: `world.add_agent(agent1)`
    *   Если агент с таким именем уже существует, вызывает `ValueError`.
6.  **`remove_agent(self, agent)`**:
    *   Удаляет агента из окружения.
    *   Примеры:
        *   Удаление агента: `world.remove_agent(agent1)`
7.  **`_handle_actions(self, source, actions)`**:
    *   Обрабатывает список действий, полученный от агента.
    *   Вызывает соответствующие обработчики для каждого типа действия (`REACH_OUT`, `TALK`).
8.  **`_handle_reach_out(self, source_agent, content, target)`**:
    *   Обрабатывает действие `REACH_OUT`, устанавливает доступность агентов друг к другу.
    *   Примеры:
        *   Агент1 пытается "достучаться" до Агента2: `world._handle_reach_out(agent1, content="Hello", target="Agent2")`
9.  **`_handle_talk(self, source_agent, content, target)`**:
    *   Обрабатывает действие `TALK`, доставляет сообщение целевому агенту. Если цель не найдена, выполняет широковещание (если `broadcast_if_no_target` включено).
    *   Примеры:
        *   Агент1 говорит Агенту2: `world._handle_talk(agent1, content="Hello Agent2", target="Agent2")`
        *   Агент1 говорит, но Агент3 не существует (широковещание): `world._handle_talk(agent1, content="Hello World", target="Agent3")`
10. **`broadcast(self, speech, source)`**:
    *   Отправляет сообщение всем агентам в окружении, исключая отправителя.
    *   Примеры:
        *   Окружение сообщает всем агентам: `world.broadcast(speech="Attention, please!")`
11. **`encode_complete_state(self)`**:
    *   Кодирует текущее состояние окружения в словарь.
    *   Примеры:
        *   Кодирование состояния в словарь: `state = world.encode_complete_state()`
12. **`decode_complete_state(self, state)`**:
    *   Декодирует состояние окружения из словаря.
    *   Примеры:
        *   Декодирование состояния из словаря: `new_world = TinyWorld().decode_complete_state(state)`

**`TinySocialNetwork` Class:**

1.  **`__init__(self, name, broadcast_if_no_target)`**:
    *   Инициализирует социальную сеть, наследуя от `TinyWorld`, добавляя атрибут `relations` для хранения связей между агентами.
    *   Пример: `network = TinySocialNetwork(name="MyNetwork")`
2.  **`add_relation(self, agent_1, agent_2, name)`**:
    *   Добавляет связь между двумя агентами в социальной сети.
    *   Примеры:
        *   Создание связи "дружба" между агентами: `network.add_relation(agent1, agent2, name="friendship")`
3.  **`_update_agents_contexts(self)`**:
    *   Обновляет контекст агентов, делая их доступными друг другу в соответствии с установленными связями.
4.  **`_step(self)`**:
    *   Обновляет контекст агентов (`_update_agents_contexts()`) и затем выполняет шаг симуляции через вызов метода `_step()` базового класса `TinyWorld`.
5.  **`_handle_reach_out(self, source_agent, content, target)`**:
    *   Обрабатывает действие `REACH_OUT`. Проверяет, что целевой агент находится в тех же отношениях, что и исходный агент. В противном случае, действие отклоняется.
    *   Примеры:
        *   Если агенты связаны, то вызов родительского метода `_handle_reach_out`: `network._handle_reach_out(agent1, "Hello", "Agent2")`
        *   Если агенты не связаны, то действие отклоняется, но вызывается метод `agent.socialize` для информирования агента `agent1`

## <mermaid>

```mermaid
flowchart TD
    subgraph TinyWorld
        Start_TinyWorld[Start: Initialize TinyWorld] --> Init_TinyWorld{__init__}
        Init_TinyWorld --> Set_Name[Set Environment Name]
        Init_TinyWorld --> Set_DateTime[Set Initial DateTime]
        Init_TinyWorld --> Set_BroadcastFlag[Set Broadcast Flag]
        Init_TinyWorld --> Init_AgentList[Initialize Agent List]
        Init_TinyWorld --> Init_NameToAgentMap[Initialize Name-to-Agent Map]
        Init_TinyWorld --> Init_CommunicationBuffer[Initialize Communication Buffer]
        Init_TinyWorld --> Init_Console[Initialize Console]
        Init_TinyWorld --> Add_Env_To_AllEnv[Add Env to All Env]
        Add_Env_To_AllEnv --> Add_Agents[Add Initial Agents]
        
        Add_Agents --> Agent_Added{Agent Added?}
        Agent_Added -- Yes --> Add_Agent_Loop[Loop: add_agent()]
        Agent_Added -- No --> End_Init_TinyWorld[End: Initialization]

        Add_Agent_Loop --> Check_Agent_UniqueName{Check Unique Agent Name?}
        Check_Agent_UniqueName -- Yes --> Set_Agent_Env[Set Agent Environment]
        Set_Agent_Env --> Append_Agent_List[Append Agent to List]
        Append_Agent_List --> Update_NameToAgentMap[Update Name to Agent Map]
        Update_NameToAgentMap --> End_Add_Agent_Loop[End Loop]
        Check_Agent_UniqueName -- No --> Throw_ValueError_Agent[Throw ValueError]
        Throw_ValueError_Agent --> End_Add_Agent_Loop
        End_Add_Agent_Loop --> Agent_Added

        Start_Step[Start: _step()] --> Advance_DateTime[Advance DateTime]
        Advance_DateTime --> Agent_Actions[Agent Actions: Loop through agents]
        Agent_Actions --> Agent_Act{agent.act()}
        Agent_Act -- Actions --> Handle_Actions[_handle_actions()]
        Handle_Actions --> End_Agent_Actions[End Agent Actions]
        End_Agent_Actions --> return_actions[Return Agents Actions]
        
        Start_Run[Start: run()] --> Run_Steps[Run Steps: Loop through steps]
        Run_Steps --> Display_Communication[_display_communication()]
        Display_Communication --> Perform_Step[_step()]
        Perform_Step --> End_Run_Steps[End Loop: Steps]
        End_Run_Steps --> Return_Actions[Return Actions List]

        Start_Skip[Start: skip()] --> Skip_Advance_DateTime[Advance DateTime by Steps]
        Skip_Advance_DateTime --> End_Skip[End: Skip Steps]
        
        Start_Handle_Actions[Start:_handle_actions()] --> Handle_Action_Loop[Handle Action: Loop through actions]
        Handle_Action_Loop --> Get_Action_Type[Get Action Type]
        Get_Action_Type --> Action_Type_Check{Check Action Type}
        Action_Type_Check -- "REACH_OUT" --> Handle_ReachOut[_handle_reach_out()]
        Action_Type_Check -- "TALK" --> Handle_Talk[_handle_talk()]
        Handle_ReachOut --> End_Handle_Actions_Loop[End Handle Action Loop]
        Handle_Talk --> End_Handle_Actions_Loop
         End_Handle_Actions_Loop --> Handle_Action_Loop
        
        Start_Handle_Reach_Out[Start:_handle_reach_out()] --> Get_Target_Agent[Get Target Agent by Name]
        Get_Target_Agent --> Make_Source_Accessible[Make Target Accessible To Source]
        Make_Source_Accessible --> Make_Target_Accessible[Make Source Accessible to Target]
        Make_Target_Accessible --> Inform_Source[Inform Source]
        Inform_Source --> Inform_Target[Inform Target]
        Inform_Target --> End_Handle_Reach_Out[End: _handle_reach_out()]
        
        Start_Handle_Talk[Start: _handle_talk()] --> Get_Target_Agent_Talk[Get Target Agent by Name]
        Get_Target_Agent_Talk --> Target_Found{Target Agent Found?}
        Target_Found -- Yes --> Deliver_Message[Deliver Message to Target]
        Deliver_Message --> End_Handle_Talk[End: _handle_talk()]
        Target_Found -- No --> Broadcast_Message[Broadcast Message]
        Broadcast_Message --> End_Handle_Talk
        
        Start_Broadcast[Start: broadcast()] --> Broadcast_Message_Loop[Broadcast Message Loop]
        Broadcast_Message_Loop --> Listen_To_Agent{agent.listen()}
        Listen_To_Agent --> End_Broadcast_Loop[End Broadcast Message Loop]
        End_Broadcast_Loop --> End_Broadcast[End: Broadcast Message]

        Start_Encode[Start: encode_complete_state()] --> Copy_State[Copy State Dict]
        Copy_State --> Remove_Attributes[Remove Attributes]
        Remove_Attributes --> Deepcopy_State[Deepcopy State]
         Deepcopy_State --> Encode_Agents[Encode Agents]
         Encode_Agents --> Encode_DateTime[Encode DateTime]
         Encode_DateTime --> Return_State_Encode[Return Complete State]

         Start_Decode[Start: decode_complete_state()] --> Deepcopy_State_Decode[Deepcopy State]
         Deepcopy_State_Decode --> Remove_Agents_From_Env[Remove All Agents From Environment]
        Remove_Agents_From_Env --> Restore_Agents_Loop[Restore Agents Loop]
         Restore_Agents_Loop --> Get_Agent_From_State{Try to get agent by name}
         Get_Agent_From_State --> Restore_Agent_State{Restore agent state}
        Restore_Agent_State --> Add_Agent_Env[Add Agent To Environment]
         Add_Agent_Env --> End_Restore_Agent_Loop[End Restore Agent Loop]
        End_Restore_Agent_Loop --> Remove_Agents_From_State[Remove Agent from State]
        Remove_Agents_From_State --> Restore_DateTime[Restore DateTime from State]
        Restore_DateTime --> Update_State[Update State]
        Update_State --> Return_Self[Return Self]
    end

   subgraph TinySocialNetwork
        Start_SocialNetwork[Start: Initialize TinySocialNetwork] --> Init_SocialNetwork{__init__}
        Init_SocialNetwork --> Init_TinyWorld_SuperCall[Initialize TinyWorld (super().__init__)]
        Init_TinyWorld_SuperCall --> Init_Relations[Initialize Relations]

       Start_Add_Relation[Start: add_relation()] --> Check_Agent1_In_Env{Check if agent 1 is in env}
       Check_Agent1_In_Env -- No --> Append_Agent1_To_Env[Append agent 1 to Env]
       Check_Agent1_In_Env -- Yes -->  Check_Agent2_In_Env[Check if agent 2 is in env]
        Append_Agent1_To_Env --> Check_Agent2_In_Env
        Check_Agent2_In_Env -- No --> Append_Agent2_To_Env[Append agent 2 to Env]
        Check_Agent2_In_Env -- Yes --> Check_Relation_Exists{Check if relation exists}
        Append_Agent2_To_Env --> Check_Relation_Exists
        Check_Relation_Exists -- Yes --> Append_Relation[Append relation to existing]
        Check_Relation_Exists -- No --> Create_Relation[Create relation and append]
        Append_Relation --> End_Add_Relation[End: Add Relation]
       Create_Relation --> End_Add_Relation
       

       Start_Update_Context[Start: _update_agents_contexts()] --> Clear_All_Accessibility[Clear All Agents Accessibility]
       Clear_All_Accessibility --> Update_Access_From_Relation[Update Access From Relation: Loop Through Relations]
       Update_Access_From_Relation --> Make_Accessible[Make Agents Accessible From Current Relation]
       Make_Accessible --> End_Update_Context_Loop[End: Update Context Loop]
       End_Update_Context_Loop --> End_Update_Context[End: _update_agents_contexts()]


       Start_Social_Step[Start: TinySocialNetwork._step()] --> Update_Agent_Contexts[_update_agents_contexts()]
       Update_Agent_Contexts --> Super_Step[TinyWorld._step()]
       Super_Step --> End_Social_Step[End: TinySocialNetwork._step()]

       Start_Social_Handle_Reach_Out[Start:TinySocialNetwork._handle_reach_out()] --> Is_In_Relation{Is In Relation With Target Agent?}
       Is_In_Relation -- Yes --> Super_Handle_Reach_Out[Call super()._handle_reach_out()]
       Super_Handle_Reach_Out --> End_Social_Handle_Reach_Out[End:TinySocialNetwork._handle_reach_out()]
        Is_In_Relation -- No --> Inform_Source_Social[Inform Source]
        Inform_Source_Social --> End_Social_Handle_Reach_Out
    end
   
   
    classDef classFill fill:#f9f,stroke:#333,stroke-width:2px
    class TinyWorld, TinySocialNetwork classFill
```

**Импорты в Mermaid:**

*   `logging`:  Используется для ведения журнала событий внутри окружения, отладки и мониторинга работы агентов.
*   `copy`: Позволяет создавать копии объектов, чтобы избежать нежелательных изменений при работе с данными окружения.
*   `datetime`, `timedelta`: Используются для управления временем в симуляциях, включая отслеживание текущего времени и вычисление интервалов времени.
*   `tinytroupe.agent`: Импортирует базовые классы агентов, которые взаимодействуют в среде.
*   `tinytroupe.utils`: Содержит вспомогательные функции, такие как `name_or_empty`, используемые для работы с именами агентов, и `pretty_datetime`, для форматирования дат.
*   `tinytroupe.control`: Содержит инструменты для управления транзакциями, обеспечивая атомарность операций.
*    `rich.console`: Используется для красивого отображения сообщений в консоли.
*   `typing`: Используется для определения типов переменных, улучшая читаемость и предотвращая ошибки.

## <объяснение>

### Импорты

*   **`import logging`**: Используется для логирования событий в приложении. Помогает в отладке и мониторинге работы. Логгер `tinytroupe` используется для записи сообщений, связанных с работой окружения.
*   **`import copy`**: Предоставляет операции для создания копий объектов. Используется для копирования состояния окружения и агентов при сохранении и загрузке.
*   **`from datetime import datetime, timedelta`**: Используется для работы с датами и временными интервалами. Класс `datetime` представляет конкретный момент времени, а `timedelta` — промежуток времени, что необходимо для моделирования динамики окружения.
*   **`from tinytroupe.agent import *`**: Импортирует все классы и функции, связанные с агентами, определенные в модуле `tinytroupe.agent`. Это необходимо для взаимодействия агентов в окружении.
*   **`from tinytroupe.utils import name_or_empty, pretty_datetime`**: Импортирует функции `name_or_empty` для получения имени агента или пустой строки, если имя отсутствует, и `pretty_datetime` для форматирования даты/времени.
*    **`import tinytroupe.control as control`**: Импортирует модуль `tinytroupe.control`, который отвечает за управление транзакциями. Это позволяет обеспечить атомарность операций.
*   **`from rich.console import Console`**: Импортирует класс `Console` из библиотеки `rich`, который используется для красивого вывода сообщений в консоль.
*   **`from typing import Any, TypeVar, Union`**: Импортирует инструменты для определения типов переменных. Это повышает читаемость кода и помогает предотвратить ошибки, например `AgentOrWorld` для указания, что переменная может быть либо агентом, либо окружением.

### Класс `TinyWorld`

*   **Роль**: Базовый класс для всех окружений, в которых действуют агенты. Определяет структуру и методы управления окружением.
*   **Атрибуты**:
    *   `all_environments` (static dict): Словарь, хранящий все созданные окружения (`name` -> `environment`).
    *   `communication_display` (static bool): Флаг, определяющий, нужно ли отображать коммуникации в окружении.
    *   `name` (str): Имя окружения.
    *   `current_datetime` (datetime): Текущее время в окружении.
    *   `broadcast_if_no_target` (bool): Флаг, указывающий, нужно ли широковещать сообщения, если целевой агент не найден.
    *   `simulation_id` (Any): ID симуляции, в рамках которой используется окружение.
    *   `agents` (list): Список агентов, находящихся в окружении.
    *   `name_to_agent` (dict): Словарь, связывающий имена агентов с их объектами (`name` -> `agent`).
    *   `_displayed_communications_buffer` (list): Буфер для хранения сообщений, отображенных в консоли.
    *   `console` (Console): Объект для вывода сообщений в консоль.

*   **Методы**:
    *   `__init__(self, name, agents, initial_datetime, broadcast_if_no_target)`: Конструктор класса, инициализирует окружение.
    *   `_step(self, timedelta_per_step)`: Выполняет один шаг симуляции, позволяя агентам действовать и обновляя время.
    *   `run(self, steps, timedelta_per_step, return_actions)`: Запускает симуляцию на заданное количество шагов.
    *   `skip(self, steps, timedelta_per_step)`: Пропускает заданное количество шагов, только обновляя время.
    *   `add_agent(self, agent)`: Добавляет агента в окружение.
    *   `remove_agent(self, agent)`: Удаляет агента из окружения.
    *    `get_agent_by_name(self, name: str) -> TinyPerson`: Возвращает агента по имени.
    *   `_handle_actions(self, source, actions)`: Обрабатывает действия, исходящие от агентов.
    *   `_handle_reach_out(self, source_agent, content, target)`: Обрабатывает действие `REACH_OUT`.
    *   `_handle_talk(self, source_agent, content, target)`: Обрабатывает действие `TALK`.
    *   `broadcast(self, speech, source)`: Рассылает сообщение всем агентам в окружении.
    *  `broadcast_thought(self, thought: str, source: AgentOrWorld=None)`: Рассылает мысль всем агентам в окружении.
    *  `broadcast_internal_goal(self, internal_goal: str)`: Рассылает внутреннюю цель всем агентам в окружении.
    *   `broadcast_context_change(self, context:list)`: Рассылает изменение контекста всем агентам в окружении.
    *    `make_everyone_accessible(self)`: Делает всех агентов в окружении доступными друг другу.
    *   `_display_communication(self, cur_step, total_steps, kind, timedelta_per_step=None)`: Отображает информацию о текущем шаге.
    *   `_push_and_display_latest_communication(self, rendering)`: Добавляет сообщение в буфер и отображает его.
    *    `pop_and_display_latest_communications(self)`: Извлекает и отображает все сообщения из буфера.
    *   `_display(self, communication)`: Отображает сообщение, используя `rich.Console`.
    *    `clear_communications_buffer(self)`: Очищает буфер сообщений.
    *   `__repr__(self)`: Возвращает строковое представление объекта.
    *   `_pretty_step(self, cur_step, total_steps, timedelta_per_step=None)`: Форматирует сообщение о текущем шаге.
     *   `pp_current_interactions(self, simplified=True, skip_system=True)`: Красиво выводит текущие сообщения агентов
     *   `pretty_current_interactions(self, simplified=True, skip_system=True, max_content_length=default["max_content_display_length"], first_n=None, last_n=None, include_omission_info:bool=True)`: Возвращает строку с сообщениями агентов в окружении.
    *   `encode_complete_state(self)`: Кодирует полное состояние окружения в словарь для сохранения.
    *   `decode_complete_state(self, state)`: Восстанавливает состояние окружения из словаря.
    *   `add_environment(environment)` (static): Добавляет окружение в список всех окружений.
    *    `set_simulation_for_free_environments(simulation)` (static): Устанавливает симуляцию для окружений, которые не принадлежат какой-либо симуляции.
    *   `get_environment_by_name(name)` (static): Возвращает окружение по его имени.
    *    `clear_environments()` (static): Очищает список всех окружений.

### Класс `TinySocialNetwork`

*   **Роль**: Подкласс `TinyWorld`, представляющий социальную сеть, в которой агенты связаны отношениями.
*   **Атрибуты**:
    *   `relations` (dict): Словарь, хранящий отношения между агентами. Ключ - название отношения, значение - список кортежей агентов, связанных этим отношением.
*   **Методы**:
    *    `__init__(self, name, broadcast_if_no_target=True)`: Конструктор класса, инициализирует социальную сеть.
    *   `add_relation(self, agent_1, agent_2, name)`: Добавляет отношение между двумя агентами.
    *   `_update_agents_contexts(self)`: Обновляет контекст агентов, делая их доступными друг другу в соответствии с установленными отношениями.
    *   `_step(self)`: Выполняет шаг в социальной сети, сначала обновляя контекст, потом вызывая шаг базового класса.
    *   `_handle_reach_out(self, source_agent, content, target)`: Обрабатывает действие `REACH_OUT`, проверяя, есть ли отношение между агентами.
    *    `is_in_relation_with(self, agent_1:TinyPerson, agent_2:TinyPerson, relation_name=None) -> bool`: Проверяет, есть ли отношение между двумя агентами.

### Функции

*   `_step`, `run`, `skip`, `_handle_actions`, `_handle_reach_out`, `_handle_talk`, `broadcast`, `encode_complete_state`, `decode_complete_state`
    *   Описаны выше в контексте классов.

### Переменные

*   `all_environments`: Статический атрибут класса `TinyWorld`, словарь, содержащий все созданные экземпляры окружения.
*   `communication_display`: Статический атрибут класса `TinyWorld`, определяющий необходимость отображения коммуникаций.
*   `name`, `current_datetime`, `broadcast_if_no_target`, `simulation_id`, `agents`, `name_to_agent`, `_displayed_communications_buffer`, `console`: Атрибуты экземпляра `TinyWorld`.
*  `relations`: Атрибут экземпляра `TinySocialNetwork`.

### Потенциальные ошибки и улучшения

*   **Отсутствие проверки типов**: Некоторые аргументы функций могли бы использовать проверку типов `isinstance` или `assert`, что позволило бы избежать неочевидных ошибок.
*   **Обработка исключений**: Более подробная обработка исключений могла бы сделать код более надежным.
*   **Управление памятью**: Необходимо проверять, что агенты удаляются из памяти при удалении из окружения, чтобы не было утечек памяти.
*   **Масштабируемость**: При большом количестве агентов и отношений, производительность методов, таких как `broadcast` и `_update_agents_contexts` может стать узким местом. Требуется тестирование на производительность.

### Взаимосвязи с другими частями проекта

*   **`tinytroupe.agent`**: Окружение напрямую взаимодействует с агентами, вызывая их методы `act`, `listen`, `socialize` и т.д.
*   **`tinytroupe.control`**: Используется для обеспечения атомарности операций, таких как обновление состояния окружения.
*   **`tinytroupe.utils`**: Используется для работы с именами агентов и для форматирования даты и времени.
*   **`rich`**: Используется для красивого отображения сообщений в консоли.

Этот анализ предоставляет подробное описание кода, его функциональности, взаимодействий и потенциальных проблем. Он может служить основой для понимания и дальнейшей разработки проекта.