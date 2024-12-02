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
        # checks whether the desired content is contained in the action content
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
        # checks whether the desired content is contained in the stimulus content
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
    
    # call the LLM
    next_message = openai_utils.client().send_message(messages)

    # check the result
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
        E[contains_action_content] --> F{action_content in action content?};
        F -- yes --> G[return True];
        F -- no --> H[return False];
        I[contains_stimulus_type] --> J{stimulus type match?};
        J -- yes --> K[return True];
        J -- no --> L[return False];
        M[contains_stimulus_content] --> N{stimulus content match?};
        N -- yes --> O[return True];
        N -- no --> P[return False];
        Q[terminates_with_action_type] --> R{len(actions) == 0?};
        R -- yes --> S[return False];
        R -- no --> T[return actions[-1].action.type == action_type];
        U[proposition_holds] --> V{LLM result "true"?};
        V -- yes --> W[return True];
        V -- no --> X{LLM result "false"?};
        X -- yes --> Y[return False];
        X -- no --> Z[raise Exception];
        AA[only_alphanumeric] --> AB{is char alphanumeric?};
        AB -- yes --> AC[''.join(c)];
        AB -- no --> AD[skip char];
        AE[create_test_system_user_message] --> AF[messages = [system_prompt]];
        AF --> AG{user_prompt is not None?};
        AG -- yes --> AH[messages.append(user_prompt)];
        AG -- no --> AI[return messages];
        AJ[agents_configs_are_equal] --> AK{key in ignore_keys?};
        AK -- yes --> AL[continue];
        AK -- no --> AM{agent1[key] != agent2[key]?};
        AM -- yes --> AN[return False];
        AM -- no --> AO[continue];
        AP[remove_file_if_exists] --> AQ[os.path.exists(file_path)?];
        AQ -- yes --> AR[os.remove(file_path)];
        AQ -- no --> AS[do nothing];
        AT[get_relative_to_test_path] --> AU[os.path.join(os.path.dirname(__file__), path_suffix)];
        
        subgraph "Fixtures"
            AV[focus_group_world] --> AW[TinyWorld];
            AX[setup] --> AY[TinyPerson.clear_agents()];
            AY --> AZ[TinyWorld.clear_environments()];
    end
    
    
    
    
    
    
    
```

```markdown
# <algorithm>

**contains_action_type(actions, action_type):**

1. Итерируется по списку действий `actions`.
2. Для каждого действия проверяет, совпадает ли тип действия `action["action"]["type"]` с заданным типом `action_type`.
3. Если совпадение найдено, возвращает `True`.
4. Если итерация завершена без совпадения, возвращает `False`.

**contains_action_content(actions, action_content):**

1. Итерируется по списку действий `actions`.
2. Для каждого действия проверяет, содержится ли `action_content` (в нижнем регистре) в `action["action"]["content"]` (в нижнем регистре).
3. Если совпадение найдено, возвращает `True`.
4. Если итерация завершена без совпадения, возвращает `False`.

**Остальные функции:**

Аналогично содержат цикл по списку `stimuli` или `actions`, проверяя заданные условия на соответствие.

**proposition_holds(proposition):**

1. Формирует систему и пользовательский запросы для LLM.
2. Вызывает `openai_utils.client().send_message` для получения ответа от LLM.
3. Очищает ответ от не-алфавитно-цифровых символов.
4. Проверяет, начинается ли ответ с "true" или "false".
5. Возвращает `True` или `False` соответственно, иначе выбрасывает исключение.


**only_alphanumeric(string):**
1. Итерируется по каждому символу `string`.
2. Если символ является буквой или цифрой, добавляет его к новой строке.
3. Возвращает новую строку.



**create_test_system_user_message(user_prompt, system_prompt):**

1. Создает список сообщений, содержащий системное сообщение.
2. Если передан `user_prompt`, добавляет его в список.
3. Возвращает список сообщений.

**agents_configs_are_equal(agent1, agent2, ignore_name=False):**

1. Создает список `ignore_keys`, если требуется игнорировать поле "name".
2. Итерируется по ключам в конфигурации `agent1`.
3. Игнорирует ключи из `ignore_keys`.
4. Если значение ключа в `agent1` отличается от значения в `agent2`, возвращает `False`.
5. Если цикл завершен без отличий, возвращает `True`.

**remove_file_if_exists(file_path):**

1. Проверяет существование файла по пути `file_path` с помощью `os.path.exists`.
2. Если файл существует, удаляет его с помощью `os.remove`.

**get_relative_to_test_path(path_suffix):**

1. Получает путь к текущему файлу с помощью `os.path.dirname(__file__)`.
2. Объединяет этот путь с `path_suffix` для получения полного пути.
3. Возвращает полный путь.

**focus_group_world():**

1. Импортирует `tinytroupe.examples`.
2. Создает экземпляр `TinyWorld` с заданным именем и списком агентов, созданных с помощью `examples.create_...`.
3. Возвращает созданный объект `TinyWorld`.

**setup():**

1. Очищает список агентов `TinyPerson` и сред `TinyWorld`.
2. Использует `yield` для передачи управления обратно вызывающему коду.


**Пример данных:**

Для `contains_action_type`:

`actions` = [{"action": {"type": "speak"}}, {"action": {"type": "listen"}}]
`action_type` = "speak"
Результат: `True`

**Взаимосвязь с другими частями проекта:**

Функции используют классы и методы из `tinytroupe.agent`, `tinytroupe.environment`, и `tinytroupe.openai_utils`, что указывает на тесную связь с другими модулями в рамках проекта. Функция `proposition_holds` использует `openai_utils` для взаимодействия с LLM API. Фикстуры `focus_group_world` и `setup` используются в тестировании, указывая на то, что эти функции необходимы для настройки и выполнения тестов.


```

```markdown
# <mermaid>

```mermaid
graph TD
    subgraph "Testing Utilities"
        A[contains_action_type] --> B{action in actions?};
        B -- yes --> C[return True];
        B -- no --> D[return False];
        E[contains_action_content] --> F{action_content in action content?};
        F -- yes --> G[return True];
        F -- no --> H[return False];
        I[contains_stimulus_type] --> J{stimulus type match?};
        J -- yes --> K[return True];
        J -- no --> L[return False];
        M[contains_stimulus_content] --> N{stimulus content match?};
        N -- yes --> O[return True];
        N -- no --> P[return False];
        Q[terminates_with_action_type] --> R{len(actions) == 0?};
        R -- yes --> S[return False];
        R -- no --> T[return actions[-1].action.type == action_type];
        U[proposition_holds] --> V{LLM result "true"?};
        V -- yes --> W[return True];
        V -- no --> X{LLM result "false"?};
        X -- yes --> Y[return False];
        X -- no --> Z[raise Exception];
        AA[only_alphanumeric] --> AB{is char alphanumeric?};
        AB -- yes --> AC[''.join(c)];
        AB -- no --> AD[skip char];
        AE[create_test_system_user_message] --> AF[messages = [system_prompt]];
        AF --> AG{user_prompt is not None?};
        AG -- yes --> AH[messages.append(user_prompt)];
        AG -- no --> AI[return messages];
        AJ[agents_configs_are_equal] --> AK{key in ignore_keys?};
        AK -- yes --> AL[continue];
        AK -- no --> AM{agent1[key] != agent2[key]?};
        AM -- yes --> AN[return False];
        AM -- no --> AO[continue];
        AP[remove_file_if_exists] --> AQ[os.path.exists(file_path)?];
        AQ -- yes --> AR[os.remove(file_path)];
        AQ -- no --> AS[do nothing];
        AT[get_relative_to_test_path] --> AU[os.path.join(os.path.dirname(__file__), path_suffix)];

        subgraph "Fixtures"
            AV[focus_group_world] --> AW[TinyWorld];
            AX[setup] --> AY[TinyPerson.clear_agents()];
            AY --> AZ[TinyWorld.clear_environments()];
    end
    
    
    
    
    
    
    
```

# <explanation>

**Импорты:**

- `os`, `sys`, `time`: Стандартные библиотеки Python для работы с операционной системой, системными переменными и временем соответственно.
- `tinytroupe.openai_utils`: Модуль, предоставляющий функции для взаимодействия с API OpenAI.  Связь с проектом: этот модуль находится в подпакете `src.tinytroupe`, предоставляет интерфейс для вызова API, необходимый для работы функций, например, `proposition_holds`.
- `tinytroupe.agent`, `tinytroupe.environment`: Модули, содержащие классы и функции для работы с агентами и средами. Они являются частью пакета `tinytroupe`. Эти модули содержат определения и методы для `TinyPerson`, `TinyWorld` и других компонентов.
- `pytest`: Библиотека для написания и запуска автоматизированных тестов.
- `importlib`: Библиотека для динамической загрузки модулей. (Используется для импорта `tinytroupe.examples` в фикстуре `focus_group_world`).


**Классы:**

- `TinyPerson`: Класс, представляющий агента. Не показаны его атрибуты и методы, но вероятно, он хранит информацию о настройках агента, его действиях.
- `TinyWorld`: Класс, представляющий среду. Не показаны его атрибуты и методы, но он определенно хранит данные об окружении, агентах в нём, и их взаимодействии.
- `TinySocialNetwork`: Класс, вероятно, представляет социальную сеть, которая является частью `TinyWorld` и содержит данные об агентах и их взаимодействии.

**Функции:**

- `contains_action_type`, `contains_action_content`, `contains_stimulus_type`, `contains_stimulus_content`:  Проверяют наличие определенного типа действия или содержимого в списке действий или стимулов.
- `terminates_with_action_type`: Проверяет, заканчивается ли список действий заданным типом действия.
- `proposition_holds`: Проверяет утверждение, вызывая LLM для проверки.  Это полезно для проверок, которые сложно автоматизировать. Аргумент `proposition` - строка с утверждением.
- `only_alphanumeric`: Возвращает строку, содержащую только алфавитно-цифровые символы. Это полезно для очистки выходных данных от нежелательных символов.
- `create_test_system_user_message`: Создает список сообщений для LLM, содержащих системный и пользовательский запросы.
- `agents_configs_are_equal`: Проверяет равенство конфигураций двух агентов.
- `remove_file_if_exists`, `get_relative_to_test_path`: Служебные функции для работы с файлами.
- `focus_group_world`: Фикстура для создания тестовой среды.
- `setup`: Фикстура для очистки агентов и сред перед каждым тестом.


**Переменные:**

- `actions`, `stimuli`: Списки, содержащие действия и стимулы.
- `action_type`, `stimulus_type`, `action_content`, `stimulus_content`:  Данные, используемые для поиска в списках действий и стимулов.
- `proposition`:  Предложение, проверяемое LLM.


**Возможные ошибки или области для улучшений:**

- Отсутствуют явные проверки типов аргументов в некоторых функциях (например, для `contains_action_content`).
- Отсутствие документации для методов классов `TinyPerson`, `TinyWorld`, `TinySocialNetwork`.
- В `proposition_holds` нет обработки ошибок при вызове LLM (например, отключения). Возможно, стоит включить обработку потенциальных исключений.
- В `only_alphanumeric` можно было бы использовать регулярные выражения для более гибкой очистки.
- Непонятно, как `TinyPerson` и `TinyWorld` взаимодействуют друг с другом.


**Цепочка взаимосвязей:**

Тесты (`pytest`) вызывают фикстуры (`focus_group_world`, `setup`), которые в свою очередь используют классы (`TinyWorld`, `TinyPerson`, etc.) и функции из других модулей `tinytroupe` для создания и настройки среды для тестирования функциональности агентов.  `openai_utils` выступает как мост к API OpenAI.  Это указывает на архитектуру, ориентированную на тестирование (TDD), в которой сначала определяются тесты, а затем реализуются необходимые функции и классы для их прохождения.