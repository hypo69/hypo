## <алгоритм>

### TinyWorld:

1. **Инициализация (`__init__`)**:
   - Создаёт экземпляр `TinyWorld` с заданным именем, списком агентов, начальным временем и флагом широковещания.
   - Инициализирует внутренние переменные, такие как `agents`, `name_to_agent`, `_displayed_communications_buffer` и `console`.
   - Добавляет мир в общий список `all_environments`.
   - Добавляет переданных агентов в мир.
   - _Пример:_ `world = TinyWorld(name="MyWorld", agents=[agent1, agent2], initial_datetime=datetime.datetime(2024, 1, 1))`

2. **Шаг симуляции (`_step`)**:
   - Увеличивает текущее время мира на заданный `timedelta_per_step`.
   - Проходит по всем агентам в мире.
   - Каждый агент выполняет действие (`agent.act()`).
   - Обрабатывает действия, возвращенные агентом (`_handle_actions`).
   - _Пример:_ `world._step(timedelta_per_step=timedelta(minutes=10))`

3. **Выполнение симуляции (`run`)**:
   - Запускает симуляцию на заданное количество `steps`.
   - На каждом шаге вызывает `_step()`.
   - Собирает действия агентов, если `return_actions` установлен в `True`.
   - _Пример:_ `world.run(steps=10, timedelta_per_step=timedelta(hours=1))`

4. **Пропуск шагов (`skip`)**:
   - Увеличивает текущее время мира на заданное количество шагов, без действий со стороны агентов.
   - _Пример:_ `world.skip(steps=5, timedelta_per_step=timedelta(minutes=30))`

5. **Добавление агентов (`add_agent`, `add_agents`)**:
   - Добавляет агентов в мир, проверяя уникальность их имен.
   - _Пример:_ `world.add_agent(agent3)`

6. **Удаление агентов (`remove_agent`, `remove_all_agents`)**:
   - Удаляет агентов из мира.
    - _Пример_: `world.remove_agent(agent1)`

7. **Получение агента по имени (`get_agent_by_name`)**:
   - Возвращает агента по его имени, или `None`, если агент не найден.
   - _Пример:_ `agent = world.get_agent_by_name("Agent1")`

8. **Обработка действий (`_handle_actions`)**:
   - Определяет тип действия (`REACH_OUT`, `TALK`) и вызывает соответствующие обработчики.
   - _Пример_: действие `{"type": "REACH_OUT", "content": "Hello", "target": "Agent2"}` вызывает `_handle_reach_out`

9. **Обработка действия "REACH_OUT" (`_handle_reach_out`)**:
   - Позволяет агентам устанавливать связь друг с другом (по умолчанию).
   - _Пример_: Агент 1 отправляет REACH_OUT агенту 2, что делает их доступными друг для друга

10. **Обработка действия "TALK" (`_handle_talk`)**:
    - Доставляет сообщение целевому агенту, если он найден.
    - В противном случае, если `broadcast_if_no_target` True, сообщение широковещается всем агентам
    - _Пример_: Агент 1 отправляет TALK агенту 2, что приводит к тому, что агент 2 получает сообщение

11. **Широковещание (`broadcast`, `broadcast_thought`, `broadcast_internal_goal`, `broadcast_context_change`)**:
    - Отправляет сообщения, мысли, внутренние цели и изменения контекста всем агентам.
    - _Пример:_ `world.broadcast("Important announcement")`

12. **Взаимодействие между агентами (`make_everyone_accessible`)**:
   - Делает всех агентов в среде доступными для взаимодействия друг с другом.

13. **Управление выводом (`_display_communication`, `_push_and_display_latest_communication`, `pop_and_display_latest_communications`, `_display`, `clear_communications_buffer`)**:
   - Управляет тем, как выводятся сообщения о ходе симуляции.
   - `_display_communication` форматирует сообщение, `_push_and_display_latest_communication` сохраняет и выводит, `pop_and_display_latest_communications` выводит все накопленные сообщения, `_display` отвечает за отображение, `clear_communications_buffer` очищает буфер.
   - _Пример:_ Шаг симуляции выводится с помощью `_display_communication`
14. **Вывод текущих взаимодействий (`pp_current_interactions`, `pretty_current_interactions`)**:
    - Выводит или возвращает строку, форматированную, с текущими сообщениями агентов.
    - _Пример:_ `world.pp_current_interactions()`

15. **Кодирование и декодирование состояния (`encode_complete_state`, `decode_complete_state`)**:
    - Кодирует состояние мира в словарь, который может быть сохранён и восстановлен.
    - _Пример_: `encoded_state = world.encode_complete_state()`

16. **Управление средами (`add_environment`, `set_simulation_for_free_environments`, `get_environment_by_name`, `clear_environments`)**:
   - Статические методы для управления списком всех созданных сред.
   - `add_environment` регистрирует среду, `set_simulation_for_free_environments` связывает среды с симуляцией, `get_environment_by_name` получает среду по имени, `clear_environments` очищает список сред.

### TinySocialNetwork (подкласс TinyWorld):

1. **Инициализация (`__init__`)**:
   - Вызывает конструктор `TinyWorld`.
   - Инициализирует словарь `relations`.

2. **Добавление отношений (`add_relation`)**:
   - Добавляет отношения между агентами.
   - _Пример:_ `network.add_relation(agent1, agent2, name="friends")`

3. **Обновление контекстов агентов (`_update_agents_contexts`)**:
   - Обновляет доступность агентов друг для друга на основе отношений.
    - Сначала делает недоступными всех агентов, а затем через отношения переопределяет доступность.

4. **Шаг симуляции (`_step`)**:
   - Обновляет контексты агентов, а затем вызывает `_step()` родительского класса.

5. **Обработка действия "REACH_OUT" (`_handle_reach_out`)**:
   - Проверяет, находятся ли агенты в отношениях, прежде чем разрешить `REACH_OUT`.
   - _Пример_: Если агент 1 и агент 2 в отношениях, REACH_OUT сработает; иначе нет

6.  **Проверка отношений (`is_in_relation_with`)**:
   - Проверяет, находятся ли два агента в заданном отношении, или в любом.

## <mermaid>

```mermaid
flowchart TD
    subgraph TinyWorld
        A[<code>__init__</code>: Initialize Environment] --> B{Check if environment name is unique}
        B -- Yes --> C[Initialize agents, datetime, etc.]
        C --> D[Add environment to all_environments]
        D --> E[Add agents to environment]

        E --> F[<code>_step</code>: Perform Simulation Step]
        F --> G{Advance datetime?}
        G -- Yes --> H[Advance datetime]
        H --> I[Agents act]
        I --> J[Handle agent actions]

        E --> K[<code>run</code>: Run Simulation]
        K --> L[Loop through steps]
        L --> F

        E --> M[<code>skip</code>: Skip Simulation Steps]
        M --> N[Advance datetime by steps]

        E --> O[<code>add_agent</code>: Add Agent]
        O --> P{Check if agent name is unique}
        P -- Yes --> Q[Add agent to environment]

        E --> R[<code>remove_agent</code>: Remove Agent]
        R --> S[Remove agent from environment]

        E --> T[<code>remove_all_agents</code>: Remove All Agents]
        T --> U[Remove all agents from environment]

        E --> V[<code>get_agent_by_name</code>: Get Agent By Name]
        V --> W{Check if agent exists}
        W -- Yes --> X[Return agent]
        W -- No --> Y[Return None]

        J --> Z[<code>_handle_actions</code>: Handle Actions]
        Z --> AA{Action type is "REACH_OUT"?}
        AA -- Yes --> AB[<code>_handle_reach_out</code>: Handle Reach Out]
        Z --> AC{Action type is "TALK"?}
        AC -- Yes --> AD[<code>_handle_talk</code>: Handle Talk]

         AB --> AE[Make agents accessible]
        
        AD --> AF{Find target agent}
        AF -- Yes --> AG[Deliver message to target]
        AF -- No --> AH{Broadcast if no target}
        AH -- Yes --> AI[Broadcast message]

       
         E --> AJ[<code>broadcast</code>: Broadcast Message]
         AJ --> AK[Deliver message to all agents]
        
        E --> AL[<code>broadcast_thought</code>: Broadcast Thought]
        AL --> AM[Deliver thought to all agents]

        E --> AN[<code>broadcast_internal_goal</code>: Broadcast Internal Goal]
        AN --> AO[Deliver goal to all agents]
        
        E --> AP[<code>broadcast_context_change</code>: Broadcast Context Change]
        AP --> AQ[Deliver context change to all agents]

         E --> AR[<code>make_everyone_accessible</code>: Make Everyone Accessible]
         AR --> AS[Make all agents accessible to each other]

        E --> AT[<code>_display_communication</code>: Display Communication]
        AT --> AU[Format communication]
        AU --> AV[<code>_push_and_display_latest_communication</code>: Push and Display Communication]

        E --> AW[<code>pop_and_display_latest_communications</code>: Pop and Display Latest Communications]
        AW --> AX[Retrieve all communications]
        AX --> AY[Display each communication]
        
        E --> AZ[<code>_display</code>: Display]
        
        E --> BA[<code>clear_communications_buffer</code>: Clear Communications Buffer]
        BA --> BB[Clear communication buffer]
    
        E --> BC[<code>encode_complete_state</code>: Encode Complete State]
        BC --> BD[Encode all environment parameters]
        
        E --> BE[<code>decode_complete_state</code>: Decode Complete State]
        BE --> BF[Decode all environment parameters]

        subgraph Static Methods
          BG[<code>add_environment</code>: Add Environment to All Environments]
          BG --> BH[Add environment to global list]
          
          BI[<code>set_simulation_for_free_environments</code>: Set Simulation for Free Environments]
          BI --> BJ[Set simulation for environments without a specific simulation id]
        
          BK[<code>get_environment_by_name</code>: Get Environment By Name]
           BK --> BL{Check if environment exists}
           BL -- Yes --> BM[Return environment]
           BL -- No --> BN[Return None]

            BO[<code>clear_environments</code>: Clear All Environments]
            BO --> BP[Clear the global list of environments]
        end

    end

   subgraph TinySocialNetwork
       CA[<code>__init__</code>: Initialize TinySocialNetwork] --> CB[Initialize TinyWorld]
        CB --> CC[Initialize relations]
       CC --> CD[<code>add_relation</code>: Add Relation]
        CD --> CE[Add a relation between two agents]
        
       CC --> CF[<code>_update_agents_contexts</code>: Update Agent Contexts]
        CF --> CG[Make all agents inaccessible]
        CG --> CH[Make agents accessible based on relations]
         
        CC --> CI[<code>_step</code>: Perform Step (Overrides TinyWorld)]
        CI --> CJ[Update agent contexts]
        CJ --> CK[Call TinyWorld._step()]
        
        CC --> CL[<code>_handle_reach_out</code>: Handle Reach Out (Overrides TinyWorld)]
        CL --> CM{Is target in the same relation?}
        CM -- Yes --> CN[Call TinyWorld._handle_reach_out]
        CM -- No --> CO[Inform agent that the target is not reachable]
        
        CC --> CP[<code>is_in_relation_with</code>: Check Relation]
        CP --> CQ{Check if agents are in given relation}
        CQ -- Yes --> CR[Return true]
        CQ -- No --> CS[Return false]

    end
```

## <объяснение>

### Импорты:

-   `logging`: Используется для записи отладочной и информационной информации. Помогает отслеживать ход выполнения программы и отлавливать ошибки.
-   `copy`: Используется для создания глубоких копий объектов, что позволяет избежать нежелательных изменений в оригинальных данных.
-   `datetime` и `timedelta`: Используются для работы со временем, позволяют вычислять временные интервалы и управлять временем симуляции.
-   `tinytroupe.agent.*`: Импортирует всё из модуля `agent`, вероятно, содержит базовый класс `TinyPerson`.
-   `tinytroupe.utils`: Импортирует `name_or_empty` и `pretty_datetime`, вероятно, вспомогательные функции для работы с именами и датами.
-    `tinytroupe.control`: Импортирует `transactional`, который, вероятно, используется для обёртывания методов, которые должны быть транзакционными.
-    `rich.console`: Используется для создания форматированного вывода в консоль.
-  `typing`: Используется для указания типов переменных и параметров функций (например, `AgentOrWorld`, `Any`, `TypeVar`, `Union`).

### Классы:

#### `TinyWorld`:

-   **Роль**: Базовый класс для всех окружений (миров). Определяет общую логику для взаимодействия агентов и управления временем.
-   **Атрибуты**:
    -   `all_environments`: Словарь, хранящий все созданные экземпляры `TinyWorld`.
    -   `communication_display`: Флаг, управляющий отображением сообщений.
    -   `name`: Имя мира.
    -   `current_datetime`: Текущее время в мире.
    -   `broadcast_if_no_target`: Флаг, определяющий, нужно ли транслировать сообщения, если цель не найдена.
    -   `simulation_id`: Идентификатор симуляции, к которой принадлежит мир.
    -   `agents`: Список агентов в мире.
    -   `name_to_agent`: Словарь для быстрого доступа к агентам по имени.
    -   `_displayed_communications_buffer`: Буфер для хранения сообщений, которые должны быть отображены.
    -    `console`: Экземпляр `rich.console` для вывода.
-   **Методы**:
    -   `__init__`: Конструктор, инициализирует атрибуты и добавляет мир в `all_environments`.
    -   `_step`: Выполняет один шаг симуляции (передвигает время, вызывает действия агентов).
    -   `_advance_datetime`: Увеличивает текущее время на заданный интервал.
    -   `run`: Запускает симуляцию на несколько шагов.
    -   `skip`: Пропускает несколько шагов, не выполняя действия.
    -   `run_minutes`, `run_hours`, `run_days`, `run_weeks`, `run_months`, `run_years`: Запускают симуляцию на заданное количество минут, часов, дней и т.д.
    -   `skip_minutes`, `skip_hours`, `skip_days`, `skip_weeks`, `skip_months`, `skip_years`: Пропускают заданное количество времени.
    -   `add_agent`, `add_agents`: Добавляют агентов в мир.
    -   `remove_agent`, `remove_all_agents`: Удаляют агентов из мира.
    -   `get_agent_by_name`: Возвращает агента по имени.
    -   `_handle_actions`: Обрабатывает действия агентов.
    -   `_handle_reach_out`: Обрабатывает действие `REACH_OUT`.
    -   `_handle_talk`: Обрабатывает действие `TALK`.
    -   `broadcast`: Отправляет сообщение всем агентам.
    -   `broadcast_thought`: Отправляет мысль всем агентам.
    -   `broadcast_internal_goal`: Отправляет внутреннюю цель всем агентам.
    -   `broadcast_context_change`: Отправляет изменение контекста всем агентам.
    -    `make_everyone_accessible`: Делает всех агентов доступными друг для друга.
    -   `_display_communication`: Форматирует вывод для отображения шага симуляции.
    -   `_push_and_display_latest_communication`: Сохраняет и отображает сообщение.
    -   `pop_and_display_latest_communications`: Выводит все накопленные сообщения.
    -   `_display`: Отображает сообщение в консоли.
    -   `clear_communications_buffer`: Очищает буфер сообщений.
    -   `__repr__`: Возвращает строковое представление мира.
    -   `_pretty_step`: Создаёт строковое представление для шага симуляции.
    -   `pp_current_interactions`: Выводит текущие взаимодействия агентов в консоль.
    -   `pretty_current_interactions`: Возвращает форматированную строку с текущими взаимодействиями агентов.
    -   `encode_complete_state`: Кодирует состояние мира в словарь.
    -   `decode_complete_state`: Декодирует состояние мира из словаря.
    -   `add_environment`: Добавляет мир в общий список (`all_environments`).
    -    `set_simulation_for_free_environments`: Связывает свободные окружения с симуляцией.
    -   `get_environment_by_name`: Возвращает мир по имени из общего списка.
    -   `clear_environments`: Очищает общий список миров.
-   **Взаимодействие**:
    -   `TinyWorld` взаимодействует с `TinyPerson` (агентом), вызывая его методы `act`, `listen`, `socialize`, `think`, `internalize_goal`, `change_context`, `make_agent_accessible`, `encode_complete_state`, `decode_complete_state`, и управляет его временем и контекстом.
    -   Использует `transactional` декоратор для обеспечения транзакционности методов.
    -   `_handle_actions` вызывает `_handle_reach_out` и `_handle_talk`, что в свою очередь взаимодействуют с агентами.

#### `TinySocialNetwork`:

-   **Роль**: Подкласс `TinyWorld`, реализующий социальную сеть. Управляет отношениями между агентами.
-   **Атрибуты**:
    -   `relations`: Словарь, хранящий отношения между агентами (например, "друзья", "семья").
-   **Методы**:
    -   `__init__`: Конструктор, вызывает конструктор `TinyWorld` и инициализирует `relations`.
    -   `add_relation`: Добавляет связь между двумя агентами.
    -    `_update_agents_contexts`: Обновляет доступность агентов друг к другу, основываясь на отношениях.
    -   `_step`: Переопределяет метод `_step` родительского класса. Обновляет доступность агентов, перед тем, как вызвать шаг из базового класса.
    -   `_handle_reach_out`: Переопределяет метод родительского класса. Проверяет наличие отношения между агентами, прежде чем разрешить действие `REACH_OUT`.
    -   `is_in_relation_with`: Проверяет, есть ли связь между агентами.
-   **Взаимодействие**:
    -   Наследует от `TinyWorld` и использует его логику, но добавляет свою логику для управления отношениями между агентами.
    -  `_update_agents_contexts` обновляет доступность, взаимодействуя с `make_agent_accessible` из класса `TinyPerson`.
    -    `_handle_reach_out` проверяет `is_in_relation_with` перед тем, как вызвать `_handle_reach_out` родительского класса.

### Функции:

-   `name_or_empty(agent)` (из `tinytroupe.utils`): Функция для получения имени агента или пустой строки, если агент не задан.
-   `pretty_datetime(datetime)` (из `tinytroupe.utils`): Функция для форматированного представления даты и времени.

### Переменные:

-   `logger`: Объект логирования, используемый для записи сообщений отладки и информации.
-   `AgentOrWorld`: Type hint, указывающий, что переменная может быть либо `TinyPerson`, либо `TinyWorld`.

### Потенциальные ошибки и области для улучшения:

1.  **Обработка ошибок**: В некоторых местах есть `try-except` блоки, но более детальная обработка ошибок может быть полезна, например, конкретизировать типы исключений и их обработку.
2.  **Типизация**: Добавление type hints (например, для возвращаемых значений функций) сделает код более читаемым и устойчивым.
3.  **Масштабируемость**: Хотя код структурирован, большие социальные сети могут привести к замедлению производительности при обновлении контекстов агентов.
4.  **Действия агентов**: В настоящее время действия ограничены `REACH_OUT` и `TALK`. Добавление новых типов действий потребует изменения в `_handle_actions` и соответствующих обработчиках.

### Цепочка взаимосвязей:

1.  **`environment.py`**:
    -   Определяет базовый класс `TinyWorld` и его подкласс `TinySocialNetwork`.
    -   Управляет окружением агентов, их взаимодействием и временем.
    -   Зависит от `agent.py`, `utils.py`, `control.py`
2.  **`agent.py`**:
    -   Определяет класс `TinyPerson`.
    -   `TinyPerson` взаимодействует с `TinyWorld`, `TinySocialNetwork` через вызов методов.
3.  **`utils.py`**:
    -   Содержит вспомогательные функции, такие как `name_or_empty` и `pretty_datetime`.
    -   Используется в `environment.py` для форматирования вывода и обработки имен.
4.  **`control.py`**:
    -   Содержит декоратор `transactional` для методов.
    -   Используется в `environment.py` для обеспечения транзакционности операций.

Этот анализ предоставляет подробное понимание структуры и функциональности кода, его взаимосвязей и потенциальных областей для улучшения.