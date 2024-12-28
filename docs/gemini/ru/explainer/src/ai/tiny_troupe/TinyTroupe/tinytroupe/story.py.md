## <алгоритм>

1. **Инициализация `TinyStory`:**
   - При создании объекта `TinyStory` (вызов `__init__`) проверяется, что передан либо `environment`, либо `agent`, но не оба одновременно. Если не передан ни один из них, или оба сразу, выбрасывается исключение.
   - Сохраняются переданные `environment` (объект `TinyWorld`), `agent` (объект `TinyPerson`), `purpose`, `context`, `first_n`, `last_n` и `include_omission_info`. `purpose` - это цель истории, `context` - это текущий контекст, `first_n` и `last_n` определяют, сколько первых и последних взаимодействий включать в историю, `include_omission_info` - флаг, указывающий нужно ли включать информацию об опущенных взаимодействиях.
   - Пример: `story = TinyStory(agent=my_agent, purpose="Tell a tale of exploration")`

2. **Начало истории (`start_story`):**
   - При вызове `start_story` формируется словарь `rendering_configs` с данными о цели истории (`purpose`), требованиях к началу (`requirements`), текущей истории (`_current_story()`), количестве слов (`number_of_words`) и необходимости сюжетного поворота (`include_plot_twist`).
   - Используется функция `utils.compose_initial_LLM_messages_with_templates` для создания сообщений для LLM на основе шаблонов "story.start.system.mustache" и "story.start.user.mustache", подставляя данные из `rendering_configs`.
     Пример:
        ```
         rendering_configs = {
             "purpose": "Be a realistic simulation.",
             "requirements": "Start some interesting story about the agents.",
             "current_simulation_trace":  "## New simulation interactions to consider\n\n            ...",
             "number_of_words": 100,
             "include_plot_twist": False
        }
        ```
   - Отправляется сообщение в LLM через `openai_utils.client().send_message` с температурой 1.5.
   - Полученный ответ (начало истории) добавляется к текущей истории `self.current_story`.
   - Пример: `start = story.start_story(requirements="The agent starts their journey", number_of_words=150)`

3. **Продолжение истории (`continue_story`):**
   - При вызове `continue_story` формируется словарь `rendering_configs`, аналогично `start_story`, но с другими требованиями `requirements`.
    Пример:
        ```
         rendering_configs = {
             "purpose": "Be a realistic simulation.",
             "requirements": "Continue the story in an interesting way.",
             "current_simulation_trace":  "## New simulation interactions to consider\n\n            ...",
             "number_of_words": 100,
             "include_plot_twist": False
        }
        ```
   - Используется функция `utils.compose_initial_LLM_messages_with_templates` для создания сообщений для LLM на основе шаблонов "story.continuation.system.mustache" и "story.continuation.user.mustache", подставляя данные из `rendering_configs`.
   - Отправляется сообщение в LLM через `openai_utils.client().send_message` с температурой 1.5.
   - Полученный ответ (продолжение истории) добавляется к текущей истории `self.current_story`.
   - Пример: `continuation = story.continue_story(requirements="A plot twist occurs", number_of_words=120)`

4. **Получение текущей истории (`_current_story`):**
   - При вызове `_current_story` формируется строка `interaction_history`, которая содержит историю взаимодействий.
   - Если в `TinyStory` задан `agent`, то вызывается метод `pretty_current_interactions` агента, иначе (если задан `environment`) вызывается метод `pretty_current_interactions` окружения.
   - Информация о взаимодействиях (либо агента, либо окружения) добавляется к `interaction_history`.
   - `interaction_history` добавляется к `self.current_story`.
   - Возвращается значение `self.current_story`.
    Пример:
        ```
        if self.agent is not None:
            interaction_history += self.agent.pretty_current_interactions(first_n=self.first_n, last_n=self.last_n, include_omission_info=self.include_omission_info)
        elif self.environment is not None:
            interaction_history += self.environment.pretty_current_interactions(first_n=self.first_n, last_n=self.last_n, include_omission_info=self.include_omission_info)
        ```
        `interaction_history` будет иметь вид "## New simulation interactions to consider\n\n ..."

## <mermaid>

```mermaid
flowchart TD
    Start(Start) --> InitializeStory[Initialize TinyStory Class: <br><code>__init__</code> method]
    InitializeStory -- Parameters: environment or agent, purpose, context, etc. --> CheckParameters{Check Parameters:<br> Exactly one of <br> environment or agent is provided?}
    CheckParameters -- Yes --> SaveParameters[Save Parameters: environment, agent, purpose, etc.]
    CheckParameters -- No --> Exception[Raise Exception: <br>Invalid Parameters]
    SaveParameters --> StartStory[Start the Story: <br><code>start_story</code> method]
    StartStory --> CreateRenderingConfigsStart[Create Rendering Configurations:  <br>Purpose, Requirements, <br>Current Story, Number of Words, etc.]
    CreateRenderingConfigsStart --> GetCurrentStoryFrom_current_story[Get current story  <br>from <code>_current_story</code> method]
     GetCurrentStoryFrom_current_story --> CheckAgentOrEnvironment{Check if Agent or Environment exists}
    CheckAgentOrEnvironment -- Agent Exists --> AgentPrettyInteractions[Get agent's interactions using: <br><code>agent.pretty_current_interactions</code>]
    CheckAgentOrEnvironment -- Environment Exists --> EnvironmentPrettyInteractions[Get environment's interactions using:  <br> <code>environment.pretty_current_interactions</code>]
    AgentPrettyInteractions --> AddInteractionsToCurrentStory[Add interactions to current story.]
    EnvironmentPrettyInteractions --> AddInteractionsToCurrentStory
    AddInteractionsToCurrentStory --> CreateLLMStartMessages[Create LLM Messages Using Templates: <br><code>utils.compose_initial_LLM_messages_with_templates</code>]
    CreateLLMStartMessages --> SendLLMStartMessage[Send Message to OpenAI:  <br><code>openai_utils.client().send_message</code>]
    SendLLMStartMessage --> GetLLMStartResponse[Get Story Start Response from OpenAI]
    GetLLMStartResponse --> AddStartToStory[Add Story Start to  <br><code>self.current_story</code>]
    AddStartToStory --> ReturnStartStory[Return Story Start]
    ReturnStartStory --> ContinueStory[Continue the Story: <br><code>continue_story</code> method]
    ContinueStory --> CreateRenderingConfigsContinue[Create Rendering Configurations: <br>Purpose, Requirements, <br>Current Story, Number of Words, etc.]
    CreateRenderingConfigsContinue --> GetCurrentStoryFrom_current_story_cont[Get current story  <br>from <code>_current_story</code> method]
       GetCurrentStoryFrom_current_story_cont --> CheckAgentOrEnvironment_cont{Check if Agent or Environment exists}
    CheckAgentOrEnvironment_cont -- Agent Exists --> AgentPrettyInteractions_cont[Get agent's interactions using: <br><code>agent.pretty_current_interactions</code>]
    CheckAgentOrEnvironment_cont -- Environment Exists --> EnvironmentPrettyInteractions_cont[Get environment's interactions using:  <br> <code>environment.pretty_current_interactions</code>]
    AgentPrettyInteractions_cont --> AddInteractionsToCurrentStory_cont[Add interactions to current story.]
    EnvironmentPrettyInteractions_cont --> AddInteractionsToCurrentStory_cont
    AddInteractionsToCurrentStory_cont --> CreateLLMContinueMessages[Create LLM Messages Using Templates: <br><code>utils.compose_initial_LLM_messages_with_templates</code>]
     CreateLLMContinueMessages --> SendLLMContinueMessage[Send Message to OpenAI:  <br><code>openai_utils.client().send_message</code>]
    SendLLMContinueMessage --> GetLLMContinueResponse[Get Story Continuation Response from OpenAI]
    GetLLMContinueResponse --> AddContinuationToStory[Add Story Continuation to  <br><code>self.current_story</code>]
    AddContinuationToStory --> ReturnContinueStory[Return Story Continuation]
     ReturnContinueStory --> End(End)
```

**Зависимости:**

- **`typing.List`**: Используется для аннотации типов, хотя в этом коде он не используется напрямую.
- **`tinytroupe.agent.TinyPerson`**: Представляет агента в симуляции.
- **`tinytroupe.environment.TinyWorld`**: Представляет среду в симуляции.
- **`tinytroupe.utils`**: Содержит вспомогательные функции, такие как `dedent` и `compose_initial_LLM_messages_with_templates`.
- **`tinytroupe.openai_utils`**: Содержит функции для взаимодействия с OpenAI API, включая `client().send_message`.

## <объяснение>

### Импорты

-   **`typing.List`**:  Импортируется для использования типов коллекций, хотя конкретно `List` здесь не используется напрямую, но может пригодится в дальнейшем для аннотации типов.
-   **`tinytroupe.agent.TinyPerson`**:  Импортируется для представления агента в симуляции. Класс `TinyPerson` используется для хранения информации об агентах, их действиях и взаимодействиях. Он используется в `TinyStory` для формирования истории с точки зрения агента.
-   **`tinytroupe.environment.TinyWorld`**: Импортируется для представления окружения в симуляции. Класс `TinyWorld` используется для хранения информации об окружении, его состоянии и взаимодействиях. Он используется в `TinyStory` для формирования истории с точки зрения окружения.
-   **`tinytroupe.utils`**: Импортируется как `utils` и содержит ряд вспомогательных функций, таких как `dedent` для удаления лишних отступов и `compose_initial_LLM_messages_with_templates` для формирования сообщений для LLM на основе шаблонов.
-   **`tinytroupe.openai_utils`**: Импортируется для взаимодействия с OpenAI API. Содержит класс `client()` для отправки сообщений в OpenAI API и получения ответов.

### Класс `TinyStory`

-   **Роль**: Класс `TinyStory` предназначен для создания и управления историями, основанными на данных симуляции. Он может создавать истории либо с точки зрения агента (`TinyPerson`), либо с точки зрения среды (`TinyWorld`). Класс использует LLM для генерации текста истории.
-   **Атрибуты**:
    -   `environment` (`TinyWorld`): Ссылка на окружение, если история строится на его основе.
    -   `agent` (`TinyPerson`): Ссылка на агента, если история строится на его основе.
    -   `purpose` (`str`): Назначение истории, используется для указания LLM контекста.
    -   `current_story` (`str`): Текущий текст истории.
    -   `first_n` (`int`): Количество первых взаимодействий для включения в историю.
    -   `last_n` (`int`): Количество последних взаимодействий для включения в историю.
    -   `include_omission_info` (`bool`): Флаг, определяющий, нужно ли включать информацию об опущенных взаимодействиях.
-   **Методы**:
    -   `__init__(self, environment:TinyWorld=None, agent:TinyPerson=None, purpose:str="Be a realistic simulation.", context:str="", first_n=10, last_n=20, include_omission_info:bool=True)`:
        -   Конструктор класса, принимающий окружение или агента, цель, контекст и другие параметры.
        -   Проверяет, что задан либо `environment`, либо `agent`, но не оба одновременно.
    -   `start_story(self, requirements="Start some interesting story about the agents.", number_of_words:int=100, include_plot_twist:bool=False) -> str`:
        -   Начинает новую историю, используя LLM.
        -   Формирует контекст для LLM, включая текущую историю, цель и требования.
        -   Отправляет запрос в LLM и добавляет полученный текст к `self.current_story`.
    -   `continue_story(self, requirements="Continue the story in an interesting way.", number_of_words:int=100, include_plot_twist:bool=False) -> str`:
        -   Продолжает историю, используя LLM.
        -   Аналогично `start_story`, но с другими шаблонами и требованиями.
    -   `_current_story(self) -> str`:
        -   Возвращает текущую историю с добавлением последних взаимодействий агента или среды.
        -   Использует методы `pretty_current_interactions` агента или среды для получения информации о взаимодействиях.

### Функции

-   `__init__`: Конструктор класса. Занимается валидацией входных параметров и инициализацией атрибутов объекта `TinyStory`.
-   `start_story`: Запускает генерацию истории, используя LLM. Формирует запрос к LLM на основе предоставленных параметров.
-   `continue_story`: Продолжает ранее начатую историю. Формирует запрос к LLM для генерации продолжения истории на основе предоставленных параметров.
-   `_current_story`: Формирует текущую часть истории, получая информацию о последних взаимодействиях либо от агента, либо от окружения.

### Переменные

-   `environment`, `agent`, `purpose`, `context`, `first_n`, `last_n`, `include_omission_info`, `current_story` - это атрибуты класса, описанные выше.
-   `requirements`, `number_of_words`, `include_plot_twist`: локальные переменные функций, описывающие требования к генерации истории, количество слов и необходимость сюжетного поворота.
-   `rendering_configs`: словарь, содержащий данные, необходимые для формирования запроса к LLM.
-   `messages`: список сообщений для LLM, формируемых на основе шаблонов и `rendering_configs`.
-   `next_message`: ответ от LLM, содержащий сгенерированный текст.
-   `start`, `continuation`:  содержат фрагменты текста, сгенерированного LLM.
-   `interaction_history`: строка, содержащая информацию о взаимодействиях агента или окружения.

### Потенциальные ошибки и области для улучшения

- **Обработка ошибок**: В конструкторе есть простая проверка, что передан либо `environment`, либо `agent`, но не оба. Желательно добавить более детальную обработку ошибок и валидацию входных данных, например, проверку на типы.
- **Температура LLM**: Температура LLM установлена на 1.5. Было бы лучше сделать ее настраиваемой через параметры конструктора или функций, чтобы пользователи могли контролировать креативность ответов LLM.
- **Шаблоны**: Шаблоны для LLM ("story.start.system.mustache", "story.start.user.mustache", "story.continuation.system.mustache", "story.continuation.user.mustache") должны быть хорошо продуманы, чтобы получать релевантные ответы.
- **Кеширование**: Результаты запросов к LLM не кешируются, что может привести к лишним вызовам API. Было бы полезно добавить кеширование результатов.
- **Разделение ответственности**:  Можно было бы выделить логику работы с LLM в отдельный класс, чтобы уменьшить размер класса `TinyStory`.
- **Логирование**: Можно было бы добавить логирование для отладки и мониторинга.

### Взаимосвязи с другими частями проекта

- **`tinytroupe.agent` и `tinytroupe.environment`**: `TinyStory` зависит от классов `TinyPerson` и `TinyWorld` для получения информации о взаимодействиях. Эти классы должны предоставлять метод `pretty_current_interactions` для форматирования истории взаимодействий.
- **`tinytroupe.utils`**: Используется для форматирования текста и создания сообщений для LLM.
- **`tinytroupe.openai_utils`**: Используется для взаимодействия с LLM через API OpenAI.

Этот код предоставляет гибкий механизм для генерации историй на основе симуляций, позволяя создавать повествования либо с точки зрения агента, либо с точки зрения окружения, используя LLM для генерации текста.