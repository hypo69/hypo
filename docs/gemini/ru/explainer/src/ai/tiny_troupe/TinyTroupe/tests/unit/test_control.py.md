## <алгоритм>

### `test_begin_checkpoint_end_with_agent_only`
1. **Подготовка:**
   - Удаление файла `control_test.cache.json`, если он существует.
   - Вызов `control.reset()` для сброса состояния симуляции.
   - Проверка, что нет запущенных симуляций (`control._current_simulations["default"] is None`).
2. **Начало симуляции:**
   - Вызов `control.begin("control_test.cache.json")` для запуска симуляции.
   - Проверка, что симуляция запущена (`control._current_simulations["default"].status == Simulation.STATUS_STARTED`).
3. **Инициализация агентов и инструментов:**
   - Создание `ArtifactExporter` для экспорта данных.
   - Создание `TinyEnricher` для обогащения данных.
   - Создание `TinyToolUse` с `TinyWordProcessor`.
   - Создание агентов `agent_1` (Оскар) и `agent_2` (Лиза) с инструментами.
   - Определение возраста и национальности для каждого агента.
4. **Проверка трейсов:**
   - Проверка, что кэшированный и исполняемый трейсы не `None`.
5. **Создание чекпоинта:**
   - Вызов `control.checkpoint()` для сохранения состояния симуляции.
6. **Действия агентов:**
   - Агенты задают вопросы.
7. **Проверка чекпоинта:**
   - Проверка, что файл `control_test.cache.json` был создан.
8. **Окончание симуляции:**
   - Вызов `control.end()` для остановки симуляции.
   - Проверка, что симуляция остановлена (`control._current_simulations["default"].status == Simulation.STATUS_STOPPED`).

### `test_begin_checkpoint_end_with_world`
1. **Подготовка:**
    - Удаление файла `control_test_world.cache.json`, если он существует.
    - Вызов `control.reset()` для сброса состояния симуляции.
    - Проверка, что нет запущенных симуляций (`control._current_simulations["default"] is None`).
2. **Начало симуляции:**
    - Вызов `control.begin("control_test_world.cache.json")` для запуска симуляции.
    - Проверка, что симуляция запущена (`control._current_simulations["default"].status == Simulation.STATUS_STARTED`).
3. **Создание мира:**
    - Создание `TinyWorld` с агентами Оскаром и Лизой.
    - Установка доступности всех агентов друг другу.
4. **Проверка трейсов:**
   - Проверка, что кэшированный и исполняемый трейсы не `None`.
5. **Запуск мира:**
    - Запуск мира на 2 шага (`world.run(2)`).
6. **Создание чекпоинта:**
    - Вызов `control.checkpoint()` для сохранения состояния симуляции.
7. **Проверка чекпоинта:**
    - Проверка, что файл `control_test_world.cache.json` был создан.
8. **Окончание симуляции:**
    - Вызов `control.end()` для остановки симуляции.
    - Проверка, что симуляция остановлена (`control._current_simulations["default"].status == Simulation.STATUS_STOPPED`).

### `test_begin_checkpoint_end_with_factory`
1. **Вспомогательная функция `aux_simulation_to_repeat`:**
    - Принимает номер итерации и флаг `verbose` для отладки.
    - **Подготовка:**
        - Вызов `control.reset()` для сброса состояния симуляции.
        - Проверка, что нет запущенных симуляций (`control._current_simulations["default"] is None`).
    - **Начало симуляции:**
        - Вызов `control.begin("control_test_personfactory.cache.json")` для запуска симуляции.
        - Проверка, что симуляция запущена (`control._current_simulations["default"].status == Simulation.STATUS_STARTED`).
    - **Создание фабрики:**
        - Создание `TinyPersonFactory` для генерации агентов.
    - **Проверка трейсов:**
       - Проверка, что кэшированный и исполняемый трейсы не `None`.
    - **Генерация агента:**
        - Генерация агента с помощью фабрики.
        - Проверка, что кэшированный и исполняемый трейсы не `None`.
    - **Создание чекпоинта:**
        - Вызов `control.checkpoint()` для сохранения состояния симуляции.
    - **Проверка чекпоинта:**
        - Проверка, что файл `control_test_personfactory.cache.json` был создан.
    - **Окончание симуляции:**
        - Вызов `control.end()` для остановки симуляции.
        - Проверка, что симуляция остановлена (`control._current_simulations["default"].status == Simulation.STATUS_STOPPED`).
    - **Отладка (опционально):**
        - Если `verbose` установлен в `True`, вывод отладочной информации.
    - Возврат созданного агента.
2. **Запуск симуляции №1:**
    - Вызов `aux_simulation_to_repeat(1, verbose=True)` для первой симуляции.
    - Получение возраста и национальности агента.
3. **Запуск симуляции №2:**
    - Вывод отладочного сообщения.
    - Вызов `aux_simulation_to_repeat(2, verbose=True)` для второй симуляции.
    - Получение возраста и национальности агента.
4. **Проверка результатов:**
    - Проверка, что возраст и национальность агентов в обеих симуляциях совпадают.

## <mermaid>

```mermaid
flowchart TD
    Start(Start) --> Reset[control.reset() <br> Reset Simulation State]
    Reset --> CheckNoSim[Assert: <br>No Simulation Running]
    CheckNoSim --> BeginSim[control.begin(cache_file) <br> Start Simulation with Cache]
    BeginSim --> CheckSimStarted[Assert: <br> Simulation Started]
    
    subgraph test_begin_checkpoint_end_with_agent_only
        BeginSim --> CreateExporter[ArtifactExporter(output_folder) <br> Create Artifact Exporter]
        CreateExporter --> CreateEnricher[TinyEnricher() <br> Create Data Enricher]
        CreateEnricher --> CreateToolUse[TinyToolUse(tools) <br> Create Tool Usage Faculty]
        CreateToolUse --> CreateAgent1[create_oscar_the_architect() <br> Create Agent 1 (Oscar)]
         CreateAgent1 --> ConfigureAgent1[agent_1.add_mental_faculties([tooluse_faculty]) <br> Set Agent 1 Mental Faculties]
        ConfigureAgent1 --> DefineAgent1Attr[agent_1.define("age", 19) <br> agent_1.define("nationality", "Brazilian")<br> Define Agent 1 Attributes]
        DefineAgent1Attr --> CreateAgent2[create_lisa_the_data_scientist() <br> Create Agent 2 (Lisa)]
        CreateAgent2 --> ConfigureAgent2[agent_2.add_mental_faculties([tooluse_faculty]) <br> Set Agent 2 Mental Faculties]
        ConfigureAgent2 --> DefineAgent2Attr[agent_2.define("age", 80) <br> agent_2.define("nationality", "Argentinian") <br> Define Agent 2 Attributes]
        DefineAgent2Attr --> CheckTraces[Assert: <br> Cached and Execution Traces Exist]
        CheckTraces --> Checkpoint[control.checkpoint() <br> Save Simulation State]
        Checkpoint --> Agent1Act[agent_1.listen_and_act("How are you doing?") <br> Agent 1 Action]
        Agent1Act --> Agent2Act[agent_2.listen_and_act("What\'s up?") <br> Agent 2 Action]
        Agent2Act --> CheckFileCreated[Assert: <br> Checkpoint File Created]
        CheckFileCreated --> EndSim[control.end() <br> Stop Simulation]
        EndSim --> CheckSimStopped[Assert: <br> Simulation Stopped]
       
    end
    
    subgraph test_begin_checkpoint_end_with_world
        BeginSim_World[control.begin(cache_file) <br> Start Simulation with Cache]
        CheckSimStarted --> BeginSim_World
        BeginSim_World --> CreateWorld[TinyWorld(name, agents) <br> Create Simulation World]
        CreateWorld --> MakeAccessible[world.make_everyone_accessible() <br> Make Agents Accessible to Each Other]
        MakeAccessible --> CheckTraces_World[Assert: <br> Cached and Execution Traces Exist]
        CheckTraces_World --> RunWorld[world.run(2) <br> Run World Simulation]
        RunWorld --> Checkpoint_World[control.checkpoint() <br> Save Simulation State]
        Checkpoint_World --> CheckFileCreated_World[Assert: <br> Checkpoint File Created]
        CheckFileCreated_World --> EndSim_World[control.end() <br> Stop Simulation]
        EndSim_World --> CheckSimStopped_World[Assert: <br> Simulation Stopped]
        
    end
    
   subgraph test_begin_checkpoint_end_with_factory
        BeginSim_Factory[control.begin(cache_file) <br> Start Simulation with Cache]
       CheckSimStarted --> BeginSim_Factory
       BeginSim_Factory --> CreateFactory[TinyPersonFactory(description) <br> Create Agent Factory]
       CreateFactory --> CheckTraces_Factory[Assert: <br> Cached and Execution Traces Exist]
        CheckTraces_Factory --> GenerateAgent[factory.generate_person(description) <br> Generate Agent from Factory]
        GenerateAgent --> CheckTraces_Factory2[Assert: <br> Cached and Execution Traces Exist]
        CheckTraces_Factory2 --> Checkpoint_Factory[control.checkpoint() <br> Save Simulation State]
        Checkpoint_Factory --> CheckFileCreated_Factory[Assert: <br> Checkpoint File Created]
        CheckFileCreated_Factory --> EndSim_Factory[control.end() <br> Stop Simulation]
        EndSim_Factory --> CheckSimStopped_Factory[Assert: <br> Simulation Stopped]
        CheckSimStopped_Factory --> GetAge1[agent_1.get("age") <br> Get Agent 1 Age]
        GetAge1 --> GetNationality1[agent_1.get("nationality") <br> Get Agent 1 Nationality]
        GetNationality1 --> BeginSim_Factory_2[control.begin(cache_file) <br> Start Simulation with Cache]
         BeginSim_Factory_2 --> CreateFactory_2[TinyPersonFactory(description) <br> Create Agent Factory]
          CreateFactory_2 --> CheckTraces_Factory_2[Assert: <br> Cached and Execution Traces Exist]
        CheckTraces_Factory_2 --> GenerateAgent_2[factory.generate_person(description) <br> Generate Agent from Factory]
        GenerateAgent_2 --> CheckTraces_Factory3[Assert: <br> Cached and Execution Traces Exist]
        CheckTraces_Factory3 --> Checkpoint_Factory_2[control.checkpoint() <br> Save Simulation State]
        Checkpoint_Factory_2 --> CheckFileCreated_Factory_2[Assert: <br> Checkpoint File Created]
         CheckFileCreated_Factory_2 --> EndSim_Factory_2[control.end() <br> Stop Simulation]
         EndSim_Factory_2 --> CheckSimStopped_Factory_2[Assert: <br> Simulation Stopped]
         CheckSimStopped_Factory_2 --> GetAge2[agent_2.get("age") <br> Get Agent 2 Age]
         GetAge2 --> GetNationality2[agent_2.get("nationality") <br> Get Agent 2 Nationality]
        GetNationality2 --> AssertAgeEqual[Assert: <br> Agent Ages Are Equal]
        AssertAgeEqual --> AssertNationalityEqual[Assert: <br> Agent Nationalities Are Equal]
       
    end

    AssertNationalityEqual --> End(End)
    CheckSimStopped --> End
    CheckSimStopped_World --> End
```

## <объяснение>

### Импорты

-   **`pytest`**: Используется для написания и запуска тестов.
-   **`os`**: Предоставляет функции для взаимодействия с операционной системой, такие как работа с файлами.
-   **`sys`**: Предоставляет доступ к параметрам и функциям интерпретатора Python. В данном случае, используется для добавления путей к модулям.
-   **`tinytroupe.examples`**: Содержит функции для создания предустановленных агентов, таких как `create_oscar_the_architect` и `create_lisa_the_data_scientist`.
-   **`tinytroupe.agent`**: Содержит классы для представления агентов (`TinyPerson`, `TinyToolUse`).
-   **`tinytroupe.environment`**: Содержит классы для представления окружения (`TinyWorld`).
-   **`tinytroupe.control`**: Содержит класс `Simulation` и функции для управления симуляциями (`begin`, `checkpoint`, `end`, `reset`).
-   **`tinytroupe.factory`**: Содержит класс `TinyPersonFactory` для генерации агентов.
-   **`tinytroupe.enrichment`**: Содержит класс `TinyEnricher` для обогащения данных.
-   **`tinytroupe.extraction`**: Содержит класс `ArtifactExporter` для экспорта артефактов.
-   **`tinytroupe.tools`**: Содержит класс `TinyWordProcessor` для обработки текста.
-   **`logging`**: Используется для логирования сообщений.
-   **`importlib`**: Используется для динамической загрузки модулей.
-   **`testing_utils`**: Содержит вспомогательные функции для тестирования, такие как `remove_file_if_exists`.

#### Взаимосвязи с другими пакетами `src.`
-   `tinytroupe` - это основной пакет, который содержит все компоненты симуляции.

### Функции
#### `test_begin_checkpoint_end_with_agent_only`
-   **Назначение**: Тестирует процесс начала, создания чекпоинта и окончания симуляции с использованием только агентов.
-   **Алгоритм**:
    1. Инициализирует симуляцию и создает агентов.
    2. Проверяет, что трейсы (кэшированный и исполняемый) существуют.
    3. Создает чекпоинт.
    4. Запускает действия агентов.
    5. Проверяет, что файл чекпоинта был создан.
    6. Завершает симуляцию.
    7. Проверяет, что симуляция остановлена.

#### `test_begin_checkpoint_end_with_world`
-   **Назначение**: Тестирует процесс начала, создания чекпоинта и окончания симуляции с использованием мира (`TinyWorld`).
-   **Алгоритм**:
    1. Инициализирует симуляцию и создает мир с агентами.
    2. Делает всех агентов доступными друг другу.
     3. Проверяет, что трейсы (кэшированный и исполняемый) существуют.
    4. Запускает мир на два шага.
    5. Создает чекпоинт.
    6. Проверяет, что файл чекпоинта был создан.
    7. Завершает симуляцию.
    8. Проверяет, что симуляция остановлена.

#### `test_begin_checkpoint_end_with_factory`
-   **Назначение**: Тестирует процесс начала, создания чекпоинта и окончания симуляции с использованием фабрики агентов (`TinyPersonFactory`).
-   **Алгоритм**:
    1. Использует вспомогательную функцию `aux_simulation_to_repeat` для запуска симуляций.
    2. Внутри `aux_simulation_to_repeat`:
        - Инициализирует симуляцию и создает фабрику агентов.
        - Генерирует агента с помощью фабрики.
        - Проверяет, что трейсы (кэшированный и исполняемый) существуют.
        - Создает чекпоинт.
        - Проверяет, что файл чекпоинта был создан.
        - Завершает симуляцию.
    3. Запускает две симуляции.
    4. Получает возраст и национальность агентов из каждой симуляции.
    5. Проверяет, что возраст и национальность агентов в обеих симуляциях совпадают.

### Вспомогательная Функция `aux_simulation_to_repeat`
-   **Аргументы**:
    -   `iteration`: Номер итерации симуляции.
    -   `verbose`: Флаг для включения отладочного вывода.
-   **Назначение**: Выполняет шаги симуляции для тестирования с фабрикой.
-   **Возвращает**: Сгенерированного агента.

### Переменные

-   `control._current_simulations`: Словарь, содержащий текущие симуляции. Ключом является "default".
-   `exporter`: Экземпляр класса `ArtifactExporter` для экспорта данных.
-   `enricher`: Экземпляр класса `TinyEnricher` для обогащения данных.
-   `tooluse_faculty`: Экземпляр класса `TinyToolUse` для использования инструментов.
-   `agent_1`, `agent_2`: Экземпляры класса `TinyPerson`, представляющие агентов.
-   `world`: Экземпляр класса `TinyWorld`, представляющий окружение.
-    `factory`: Экземпляр класса `TinyPersonFactory`, представляющий фабрику агентов.
-   `age_1`, `age_2`, `nationality_1`, `nationality_2`: Переменные, хранящие возраст и национальность агентов.

### Классы

-   **`Simulation`**: Класс из `tinytroupe.control`, управляющий состоянием симуляции. Имеет константы статуса `STATUS_STARTED` и `STATUS_STOPPED`.
-   **`TinyPerson`**: Класс из `tinytroupe.agent`, представляющий агента.
-   **`TinyToolUse`**: Класс из `tinytroupe.agent`, представляющий возможность использования инструментов агентом.
-   **`TinyWorld`**: Класс из `tinytroupe.environment`, представляющий окружение, в котором действуют агенты.
-   **`TinyPersonFactory`**: Класс из `tinytroupe.factory`, создающий агентов.
-   **`TinyEnricher`**: Класс из `tinytroupe.enrichment`, обогащающий данные.
-   **`ArtifactExporter`**: Класс из `tinytroupe.extraction`, экспортирующий артефакты.
-  **`TinyWordProcessor`**: Класс из `tinytroupe.tools`, обрабатывающий текст.

### Потенциальные ошибки и области для улучшения

-   **Жестко заданные имена файлов**: Имена файлов, такие как `"control_test.cache.json"`, жестко заданы в коде. Это может затруднить масштабирование и тестирование с различными файлами.
-   **Магические значения**: Числа `19` и `80` для возраста, а также `"Brazilian"` и `"Argentinian"` для национальности, могут быть вынесены в константы или параметры.
-   **Повторение кода**: Код для проверки наличия трейсов повторяется в каждом тестовом сценарии, что может быть вынесено в отдельную функцию.
-   **Отсутствие проверок на ошибки**:  В коде нет обработки исключений (например, если файл не может быть создан или удален).
-   **Зависимость от `default` ключа**: Использование  `_current_simulations["default"]`  может создать проблемы, если понадобится поддерживать несколько одновременных симуляций.

### Цепочка взаимосвязей с другими частями проекта

-   Тесты используют `tinytroupe.examples` для создания предустановленных агентов, что демонстрирует зависимость от модуля примеров.
-   Агенты из `tinytroupe.agent` взаимодействуют с инструментами из `tinytroupe.tools` и окружением из `tinytroupe.environment`, показывая взаимодействие между различными компонентами проекта.
-   Симуляция, управляемая через `tinytroupe.control`, зависит от классов агентов и окружения, что подчеркивает центральную роль управления симуляцией.
-   Фабрика из `tinytroupe.factory` используется для создания агентов, что показывает взаимосвязь между фабрикой и агентами.
-   Экспортер из `tinytroupe.extraction` используется для сохранения данных, что показывает, как данные перемещаются между разными частями проекта.
-   Обогатитель из `tinytroupe.enrichment` используется для модификации данных, что показывает, как данные могут быть обработаны во время выполнения симуляции.