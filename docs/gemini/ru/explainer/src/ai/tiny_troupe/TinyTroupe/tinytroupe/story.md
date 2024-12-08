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

**Шаг 1:** Инициализация `TinyStory`
- Принимает на вход параметры: `environment`, `agent`, `purpose`, `context`, `first_n`, `last_n`, `include_omission_info`.
- Проверяет, что предоставлен либо `environment`, либо `agent`, но не оба одновременно.
- Сохраняет переданные параметры в соответствующие атрибуты класса.

**Шаг 2:** `start_story`
- Создаёт словарь `rendering_configs`, содержащий данные для генерации истории.
- Использует `utils.compose_initial_LLM_messages_with_templates` для создания запроса к LLM.
- Отправляет запрос к LLM через `openai_utils.client().send_message`.
- Получает ответ от LLM.
- Добавляет ответ в `self.current_story`.
- Возвращает сгенерированную часть истории.


**Шаг 3:** `continue_story` (аналогично `start_story`)
- Создаёт словарь `rendering_configs`, содержащий данные для продолжения истории.
- Использует `utils.compose_initial_LLM_messages_with_templates` для создания запроса к LLM.
- Отправляет запрос к LLM через `openai_utils.client().send_message`.
- Получает ответ от LLM.
- Добавляет ответ в `self.current_story`.
- Возвращает сгенерированную часть истории.


**Шаг 4:** `_current_story`
- Создаёт пустую строку `interaction_history`.
- Если `self.agent` не равен `None`, то собирает историю взаимодействия агента.
- Если `self.environment` не равен `None`, то собирает историю взаимодействия среды.
- Добавляет `interaction_history` в `self.current_story`.
- Возвращает `self.current_story`.

Пример:
При вызове `start_story` с агентом и параметрами, `_current_story` будет генерировать строку `interaction_history` из взаимодействия агента, и эта строка будет использоваться LLM для генерации истории. Затем LLM сгенерирует текст для начала истории, который будет добавлен к `current_story`.


# <mermaid>

```mermaid
graph TD
    A[TinyStory] --> B(init);
    B --> C{environment or agent?};
    C -- environment --> D[environment.pretty_current_interactions];
    C -- agent --> E[agent.pretty_current_interactions];
    D --> F[compose_initial_LLM_messages_with_templates];
    E --> F;
    F --> G[openai_utils.client().send_message];
    G --> H[start/continue];
    H --> I[self.current_story +=];
    I --> J[return];
    I --> K[self._current_story];
    K --> F;
    subgraph TinyWorld
        D --> L[interaction_history];
    end
    subgraph TinyPerson
        E --> L;
    end
    subgraph utils
      F -- story.start.system.mustache --> N[messages];
      F -- story.start.user.mustache --> N;

    end

```


# <explanation>

**Импорты:**

- `from typing import List`:  Импортирует тип данных `List` для возможного использования списков в будущем, но в данном коде не используется.
- `from tinytroupe.agent import TinyPerson`: Импортирует класс `TinyPerson` из модуля `agent` внутри пакета `tinytroupe`.  Это класс, вероятно, представляющий агента в симуляции.
- `from tinytroupe.environment import TinyWorld`: Импортирует класс `TinyWorld` из модуля `environment` внутри пакета `tinytroupe`. Вероятно, представляет окружающую среду симуляции.
- `import tinytroupe.utils as utils`: Импортирует модуль `utils` из пакета `tinytroupe`. Этот модуль, скорее всего, содержит вспомогательные функции, например, для форматирования строк.
- `from tinytroupe import openai_utils`: Импортирует модуль `openai_utils` из пакета `tinytroupe`.  Этот модуль, вероятно, предоставляет интерфейс для взаимодействия с API OpenAI.

**Классы:**

- `TinyStory`: Этот класс отвечает за создание и управление историями, связанными с симуляциями.  Он хранит информацию о текущей истории (`current_story`), агенте (`agent`), среде (`environment`), целях (`purpose`) и других характеристиках. `start_story` и `continue_story` методы  используют OpenAI API для генерации текста истории.


**Функции:**

- `__init__`: Инициализирует экземпляр класса `TinyStory`. Важно, что она проверяет, что в качестве аргументов передаётся либо `environment`, либо `agent`, но не оба одновременно.
- `start_story`:  Начинает новую историю, используя `openai_utils` для генерации текста с помощью LLM.  Аргументы `requirements`, `number_of_words`, `include_plot_twist` настраивают этот процесс.
- `continue_story`:  Продолжает существующую историю, аналогично `start_story`, но использует другую шаблонную информацию.
- `_current_story`: Возвращает строку, представляющую текущее состояние взаимодействия (`interaction_history`).


**Переменные:**

- `environment`, `agent`, `purpose`, `current_story`, `first_n`, `last_n`, `include_omission_info`:  Сохраняют различные характеристики истории и симуляции.

**Возможные ошибки/улучшения:**

- **Обработка исключений:**  В методе `__init__` проверки на корректность входных данных являются хорошим шагом, но можно добавить более подробную обработку исключений.
- **Постоянство данных:**  В случае продолжения работы с историей, нужно продумать, как сохранить состояние `current_story`, чтобы при последующих вызовах `continue_story` история продолжалась, а не начиналась с нуля.
- **Управление зависимостями:** Есть зависимость от `openai_utils`, `utils` и самих агента и среды симуляции. При возникновении проблем с этими компонентами, необходимо проверить их работу и корректность их использования.
- **Логирование:** Введение логирования поможет отслеживать ход выполнения и выявлять ошибки в процессе работы.
- **Оптимизация:** Для больших объёмов данных может потребоваться оптимизация работы с `interaction_history`.


**Взаимосвязи с другими частями проекта:**

Код зависит от классов `TinyPerson` и `TinyWorld` (определённых в других файлах пакета `tinytroupe`),  модуля `utils` (для форматирования текста),  и модуля `openai_utils` (для взаимодействия с API OpenAI).  Этот модуль `story` координирует генерацию истории, используя информацию, полученную из `TinyPerson` и `TinyWorld`.