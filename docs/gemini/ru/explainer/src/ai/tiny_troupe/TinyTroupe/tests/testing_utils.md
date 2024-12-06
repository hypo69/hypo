```MD
# <input code>

```python
"""
Testing utilities.
"""
import os
import sys
from time import sleep
sys.path.append('../../tinytroupe/')
sys.path.append('../../')
sys.path.append('..')

import tinytroupe.openai_utils as openai_utils
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld, TinySocialNetwork
import pytest
import importlib

# force caching, in order to save on API usage
openai_utils.force_api_cache(True, "tests_cache.pickle")

def contains_action_type(actions, action_type):
    """
    Checks if the given list of actions contains an action of the given type.
    """
    for action in actions:
        if action["action"]["type"] == action_type:
            return True
    return False

def contains_action_content(actions:list, action_content: str):
    """
    Checks if the given list of actions contains an action with the given content.
    """
    for action in actions:
        if action_content.lower() in action["action"]["content"].lower():
            return True
    return False

def contains_stimulus_type(stimuli, stimulus_type):
    """
    Checks if the given list of stimuli contains a stimulus of the given type.
    """
    for stimulus in stimuli:
        if stimulus["type"] == stimulus_type:
            return True
    return False

def contains_stimulus_content(stimuli, stimulus_content):
    """
    Checks if the given list of stimuli contains a stimulus with the given content.
    """
    for stimulus in stimuli:
        if stimulus_content.lower() in stimulus["content"].lower():
            return True
    return False

def terminates_with_action_type(actions, action_type):
    """
    Checks if the given list of actions terminates with an action of the given type.
    """
    if len(actions) == 0:
        return False
    return actions[-1]["action"]["type"] == action_type

def proposition_holds(proposition: str) -> bool:
    """
    Checks if the given proposition is true according to an LLM call.
    This can be used to check for text properties that are hard to
    verify mechanically, such as "the text contains some ideas for a product".
    """
    system_prompt = f"""
    Check whether the following proposition is true or false. If it is
    true, write "true", otherwise write "false". Don't write anything else!
    """
    user_prompt = f"""
    Proposition: {proposition}
    """
    messages = [{"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}]
    next_message = openai_utils.client().send_message(messages)
    cleaned_message = only_alphanumeric(next_message["content"])
    if cleaned_message.lower().startswith("true"):
        return True
    elif cleaned_message.lower().startswith("false"):
        return False
    else:
        raise Exception(f"LLM returned unexpected result: {cleaned_message}")

def only_alphanumeric(string: str):
    """
    Returns a string containing only alphanumeric characters.
    """
    return ''.join(c for c in string if c.isalnum())

def create_test_system_user_message(user_prompt, system_prompt="You are a helpful AI assistant."):
    """
    Creates a list containing one system message and one user message.
    """
    messages = [{"role": "system", "content": system_prompt}]
    if user_prompt is not None:
        messages.append({"role": "user", "content": user_prompt})
    return messages

def agents_configs_are_equal(agent1, agent2, ignore_name=False):
    """
    Checks if the configurations of two agents are equal.
    """
    ignore_keys = []
    if ignore_name:
        ignore_keys.append("name")
    for key in agent1._configuration.keys():
        if key in ignore_keys:
            continue
        if agent1._configuration[key] != agent2._configuration[key]:
            return False
    return True

############################################################################################################
# I/O utilities
############################################################################################################

def remove_file_if_exists(file_path):
    """
    Removes the file at the given path if it exists.
    """
    if os.path.exists(file_path):
        os.remove(file_path)

def get_relative_to_test_path(path_suffix):
    """
    Returns the path to the test file with the given suffix.
    """
    return os.path.join(os.path.dirname(__file__), path_suffix)


############################################################################################################
# Fixtures
############################################################################################################

@pytest.fixture(scope="function")
def focus_group_world():
    import tinytroupe.examples as examples
    world = TinyWorld("Focus group", [examples.create_lisa_the_data_scientist(), examples.create_oscar_the_architect(), examples.create_marcos_the_physician()])
    return world

@pytest.fixture(scope="function")
def setup():
    TinyPerson.clear_agents()
    TinyWorld.clear_environments()
    yield
```

```mermaid
graph TD
    subgraph "Testing Utilities"
        A[contains_action_type] --> B{action in actions?};
        B -- yes --> C[return True];
        B -- no --> D[return False];
        
        E[contains_action_content] --> F{action_content in action["action"]["content"]?};
        F -- yes --> G[return True];
        F -- no --> H[return False];

        I[contains_stimulus_type] --> J{stimulus in stimuli?};
        J -- yes --> K[return True];
        J -- no --> L[return False];

        M[contains_stimulus_content] --> N{stimulus_content in stimulus["content"]?};
        N -- yes --> O[return True];
        N -- no --> P[return False];
  
        Q[terminates_with_action_type] --> R{len(actions) == 0?};
        R -- yes --> S[return False];
        R -- no --> T[return actions[-1]["action"]["type"] == action_type];
        
        U[proposition_holds] --> V[LLM call];
        V --> W{result "true"?};
        W -- yes --> X[return True];
        W -- no --> Y{result "false"?};
        Y -- yes --> Z[return False];
        Y -- no --> AA[Exception];
        
        AB[only_alphanumeric] --> AC[return filtered string];

        AD[create_test_system_user_message] --> AE[return messages list];

        AF[agents_configs_are_equal] --> AG{key in agent1._configuration?};
        AG -- yes --> AH{agent1._configuration[key] != agent2._configuration[key]?};
        AH -- yes --> AI[return False];
        AH -- no --> AJ[continue];
        AJ --> AK[return True];
    end
    
    openai_utils --> U;
    openai_utils --> AB;
    TinyPerson --> AF;
    TinyWorld --> AF;
    examples --> focus_group_world;
    pytest --> focus_group_world;
    os --> remove_file_if_exists;
    os --> get_relative_to_test_path;
    sys --> remove_file_if_exists;

    focus_group_world --> setup;
    TinyPerson --> setup;
    TinyWorld --> setup;
```

# <explanation>

**Импорты:**

- `import os`: Импортирует модуль для работы с операционной системой (например, чтение/запись файлов). Связь с `src` косвенна, так как это стандартный Python-модуль.
- `import sys`: Импортирует модуль для работы со средой выполнения Python. Связь с `src` косвенна, так как это стандартный Python-модуль.
- `from time import sleep`: Импортирует функцию `sleep` для задержек в коде. Связь с `src` косвенна, так как это стандартный Python-модуль.
- `import tinytroupe.openai_utils as openai_utils`: Импортирует утилиты для работы с OpenAI API из подпакета `tinytroupe`. Подключение к `src` явное и прямое.
- `from tinytroupe.agent import TinyPerson`: Импортирует класс `TinyPerson` из пакета `tinytroupe.agent`, который, вероятно, представляет агента в системе. Подключение к `src` явное и прямое.
- `from tinytroupe.environment import TinyWorld, TinySocialNetwork`: Импортирует классы `TinyWorld` и `TinySocialNetwork` из пакета `tinytroupe.environment`. Вероятно, они представляют среду и социальную сеть в системе. Подключение к `src` явное и прямое.
- `import pytest`: Импортирует фреймворк для тестирования pytest, предназначенный для написания тестов. Связь с `src` косвенна, так как это стандартный фреймворк Python.
- `import importlib`: Импортирует модуль `importlib`, используемый для динамической загрузки модулей. Связь с `src` косвенна, так как это стандартный Python-модуль.

**Классы:**

- `TinyPerson`: Представляет агента.  Описание его атрибутов и методов должно находиться в файле `tinytroupe/agent.py`.  
- `TinyWorld`: Представляет среду. Описание его атрибутов и методов должно находиться в файле `tinytroupe/environment.py`.
- `TinySocialNetwork`: Представляет социальную сеть. Описание его атрибутов и методов должно находиться в файле `tinytroupe/environment.py`.  Эти классы, вероятно, взаимодействуют с агентами (`TinyPerson`) и средой.

**Функции:**

- `contains_action_type`, `contains_action_content`, `contains_stimulus_type`, `contains_stimulus_content`: проверяют наличие определенного типа действий или содержания в списках действий или стимулов.  Они важны для проверки сценариев тестирования.
- `terminates_with_action_type`: Проверяет, завершается ли список действий заданным типом действия.
- `proposition_holds`: Использует OpenAI API для проверки истинности утверждения.
- `only_alphanumeric`: Удаляет из строки все символы, кроме букв и цифр. Используется для очистки вывода от OpenAI.
- `create_test_system_user_message`: Создает список сообщений для OpenAI запроса, что полезно для тестирования и имитации диалогов.
- `agents_configs_are_equal`: Сравнивает конфигурации агентов, игнорируя (при необходимости) имя.  Позволяет сравнивать конфигурации агентов без учета имени.
- `remove_file_if_exists`: Удаляет файл, если он существует.
- `get_relative_to_test_path`: Возвращает путь к тесту.


**Переменные:**

- `actions`: Список действий.
- `action_type`: Тип действия.
- `action_content`: Содержание действия.
- `stimuli`: Список стимулов.
- `stimulus_type`: Тип стимула.
- `stimulus_content`: Содержание стимула.
- `proposition`: Утверждение для проверки.

**Ошибки и улучшения:**

- Не хватает документации, объяснения поведения в необычных случаях.
- Можно улучшить код функций `proposition_holds` и `only_alphanumeric` для повышения читаемости и расширяемости.

**Взаимосвязи с другими частями проекта:**

- `tinytroupe.openai_utils`: Подключается к OpenAI API и, вероятно, используется для обработки сообщений и запросов.
- `tinytroupe.agent`: Содержит класс `TinyPerson` и, вероятно, логику работы агента.
- `tinytroupe.environment`: Содержит классы `TinyWorld` и `TinySocialNetwork`, обеспечивающие окружение для агентов.
- `tinytroupe.examples`: Вероятно, содержит примеры создания агентов и миров.


В целом, код написан для тестирования функций `TinyPerson`, `TinyWorld` и связанных компонентов в проекте. Он предоставляет набор инструментов для проверки поведения агентов в различных ситуациях, используя OpenAI.