# <input code>

```python
"""
Every simulation tells a story. This module provides helper mechanisms to help with crafting appropriate stories in TinyTroupe.
"""

from typing import List
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
import tinytroupe.utils as utils
from tinytroupe import openai_utils

class TinyStory:

    def __init__(self, environment:TinyWorld=None, agent:TinyPerson=None, purpose:str="Be a realistic simulation.", context:str="",
                 first_n=10, last_n=20, include_omission_info:bool=True) -> None:
        """
        Initialize the story. The story can be about an environment or an agent. It also has a purpose, which
        is used to guide the story generation. Stories are aware that they are related to simulations, so one can
        specify simulation-related purposes.

        Args:
            environment (TinyWorld, optional): The environment in which the story takes place. Defaults to None.
            agent (TinyPerson, optional): The agent in the story. Defaults to None.
            purpose (str, optional): The purpose of the story. Defaults to "Be a realistic simulation.".
            context (str, optional): The current story context. Defaults to "". The actual story will be appended to this context.
            first_n (int, optional): The number of first interactions to include in the story. Defaults to 10.
            last_n (int, optional): The number of last interactions to include in the story. Defaults to 20.
            include_omission_info (bool, optional): Whether to include information about omitted interactions. Defaults to True.
        """

        # exactly one of these must be provided
        if environment and agent:
            raise Exception("Either \'environment\' or \'agent\' should be provided, not both")
        if not (environment or agent):
            raise Exception("At least one of the parameters should be provided")

        self.environment = environment
        self.agent = agent

        self.purpose = purpose

        self.current_story = context

        self.first_n = first_n
        self.last_n = last_n
        self.include_omission_info = include_omission_info
    
    def start_story(self, requirements="Start some interesting story about the agents.", number_of_words:int=100, include_plot_twist:bool=False) -> str:
        """
        Start a new story.
        """
        
        rendering_configs = {
                             "purpose": self.purpose,
                             "requirements": requirements,
                             "current_simulation_trace": self._current_story(),
                             "number_of_words": number_of_words,
                             "include_plot_twist": include_plot_twist
                            }

        messages = utils.compose_initial_LLM_messages_with_templates("story.start.system.mustache", "story.start.user.mustache", rendering_configs)
        next_message = openai_utils.client().send_message(messages, temperature=1.5)

        start = next_message["content"]

        self.current_story += utils.dedent(
            f"""

            ## The story begins

            {start}

            """
            )

        return start
    
    # ... (rest of the code)
```

# <algorithm>

**Шаг 1. Инициализация (метод __init__)**:

*   Проверяет, что предоставлен либо `environment`, либо `agent`, но не оба одновременно.
*   Инициализирует атрибуты `self.environment`, `self.agent`, `self.purpose`, `self.current_story`, `self.first_n`, `self.last_n`, `self.include_omission_info`.

**Пример:**
```
story = TinyStory(environment=some_environment, first_n=5, last_n=15)
```


**Шаг 2. Начать историю (метод start_story)**:

*   Создает словарь `rendering_configs` с параметрами для генерации истории.
*   Использует `utils.compose_initial_LLM_messages_with_templates` для создания сообщений для LLM.
*   Отправляет сообщения LLM через `openai_utils.client().send_message`.
*   Получает ответ от LLM.
*   Добавляет полученный текст к `self.current_story`.
*   Возвращает полученный текст.

**Пример:**
```
story.start_story()
```

**Шаг 3. Продолжить историю (метод continue_story)**:  Аналогичен шагу 2, но использует другие шаблоны сообщений и сохраняет продолжение в истории.

**Пример:**
```
story.continue_story()
```


**Шаг 4. Получить текущую историю (метод _current_story)**:

*   Собирает данные из `self.agent` или `self.environment` с помощью метода `pretty_current_interactions`.
*   Формирует строку истории, включая взаимодействия.
*   Обновляет `self.current_story` с добавлением новых данных.
*   Возвращает текущую историю.

**Пример:**
```
story._current_story()
```


Данные передаются между функциями и методами в виде аргументов и через атрибуты класса `TinyStory`.


# <mermaid>

```mermaid
graph TD
    A[TinyStory] --> B{__init__};
    B --> C[environment/agent];
    C -- environment --> D[self.environment];
    C -- agent --> E[self.agent];
    B --> F[self.purpose];
    B --> G[self.current_story];
    B --> H[self.first_n];
    B --> I[self.last_n];
    B --> J[self.include_omission_info];
    A --> K[start_story];
    K --> L{rendering_configs};
    L --> M[utils.compose_initial_LLM_messages_with_templates];
    M --> N[openai_utils.client().send_message];
    N --> O[next_message];
    O --> P[self.current_story];
    P --> Q[return start];
    A --> R[continue_story];
    R --> L;
    A --> S[_current_story];
    S --> T[self.agent.pretty_current_interactions];
    S --> U[self.environment.pretty_current_interactions];
    T -- or -- U --> V[interaction_history];
    V --> W[self.current_story];
    W --> X[return self.current_story];
```

**Объяснение зависимостей:**

*   `tinytroupe.agent.TinyPerson`: Класс, содержащий данные об агенте.
*   `tinytroupe.environment.TinyWorld`: Класс, содержащий данные об окружении.
*   `tinytroupe.utils`: Модуль, предоставляющий утилиты для работы с текстом.
*   `tinytroupe.openai_utils`: Модуль, содержащий методы для взаимодействия с OpenAI API.  `openai_utils.client()` представляет собой некоторый клиент или объект, отвечающий за взаимодействие с API OpenAI.

# <explanation>

**Импорты:**

*   `from typing import List`: Импортирует тип данных `List` для типизации, но в коде не используется.
*   `from tinytroupe.agent import TinyPerson`: Импортирует класс `TinyPerson` из модуля `tinytroupe.agent`, вероятно, для работы с данными агентов.
*   `from tinytroupe.environment import TinyWorld`: Импортирует класс `TinyWorld` из модуля `tinytroupe.environment`, для работы с окружением.
*   `import tinytroupe.utils as utils`: Импортирует модуль `tinytroupe.utils`, содержащий вспомогательные функции (например, для работы с текстом).
*   `from tinytroupe import openai_utils`: Импортирует модуль `openai_utils`, предоставляющий инструменты для взаимодействия с API OpenAI.

**Классы:**

*   `TinyStory`: Этот класс отвечает за создание и управление историей симуляции. Он хранит информацию об окружении (`environment`), агенте (`agent`), цели (`purpose`), текущем контексте истории (`current_story`) и параметрах для получения части истории (`first_n`, `last_n`, `include_omission_info`).  Методы `start_story` и `continue_story` взаимодействуют с LLM (через `openai_utils`), чтобы сгенерировать новые части истории, а `_current_story` собирает текущее состояние моделирования для включения в контекст.


**Функции:**

*   `__init__`: Инициализирует объект `TinyStory`.  Важно, что `environment` или `agent` должны быть указаны, но не оба.
*   `start_story`: Запускает новую историю с использованием OpenAI API и формирует соответствующий контекст.
*   `continue_story`: Продолжает существующую историю.
*   `_current_story`: Формирует текущую историю на основе данных из `environment` или `agent`.

**Переменные:**

*   `self.environment`, `self.agent`, `self.purpose`, `self.current_story`, `self.first_n`, `self.last_n`, `self.include_omission_info`: Атрибуты класса, хранящие информацию о симуляции и историю. `environment` и `agent` не должны оба присутствовать, что важно для корректной работы.

**Возможные ошибки и улучшения:**

*   **Обработка ошибок:**  В `__init__` проверка на отсутствие или наличие обоих параметров `environment` и `agent` очень важна.  Но стоило бы добавить более расширенную проверку типов для аргументов.
*   **Чёткость требований к LLM:**  Описание запросов к LLM может быть улучшено.   Указание более конкретных параметров для LLM (например, какие данные учитывать, какого типа должна быть история) может улучшить качество генерации.
*   **Управление состоянием**:  Класс `TinyStory` не содержит механизмов для сохранения и загрузки состояния.

**Взаимосвязь с другими частями проекта:**

*   `TinyStory` зависит от классов `TinyPerson` и `TinyWorld`, а также от функций/модулей из `tinytroupe.utils` и `tinytroupe.openai_utils`.  Эти зависимости означают, что для работы `TinyStory` необходимо корректно определить классы `TinyPerson` и `TinyWorld`, а также соответствующий OpenAI API.