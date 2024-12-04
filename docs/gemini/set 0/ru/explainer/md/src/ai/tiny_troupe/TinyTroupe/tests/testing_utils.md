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
    subgraph "tinytroupe"
        openai_utils --> TinyPerson
        openai_utils --> TinyWorld
        openai_utils --> TinySocialNetwork
        TinyPerson --> contains_action_type
        TinyPerson --> contains_action_content
        TinyWorld --> contains_stimulus_type
        TinyWorld --> contains_stimulus_content
    end
    contains_action_type --> return
    contains_action_content --> return
    contains_stimulus_type --> return
    contains_stimulus_content --> return
    proposition_holds --> openai_utils
    proposition_holds --> return
    only_alphanumeric --> return
    create_test_system_user_message --> return
    agents_configs_are_equal --> return
    remove_file_if_exists --> os.path
    get_relative_to_test_path --> os.path
    focus_group_world --> TinyWorld
    focus_group_world --> examples.create_lisa_the_data_scientist
    focus_group_world --> examples.create_oscar_the_architect
    focus_group_world --> examples.create_marcos_the_physician
    setup --> TinyPerson.clear_agents
    setup --> TinyWorld.clear_environments
    setup --> yield
    examples.create_lisa_the_data_scientist --> return
    examples.create_oscar_the_architect --> return
    examples.create_marcos_the_physician --> return
    openai_utils --> client()
    openai_utils --> force_api_cache

```

# <explanation>

**Импорты**:

- `os`, `sys`, `time`: Стандартные библиотеки Python для работы с операционной системой, командной строкой и временем соответственно.
- `tinytroupe.openai_utils`: Модуль, вероятно, содержащий функции для взаимодействия с API OpenAI. Наследует `src`.
- `tinytroupe.agent`: Модуль с классом `TinyPerson`,  вероятно, представляющий агентов. Наследует `src`.
- `tinytroupe.environment`: Модуль с классами `TinyWorld`, `TinySocialNetwork`, вероятно, определяющими окружения и социальные сети. Наследует `src`.
- `pytest`: Библиотека для тестирования Python. Используется для организации и выполнения тестов.
- `importlib`: Модуль для динамической загрузки модулей.  Используется не явно, но может быть полезен при импорте модулей.

**Классы**:

- `TinyPerson`: Вероятно, представляет агента в системе.  Ключевой атрибут – `_configuration`, содержащий настройки агента.  Метод `clear_agents` предназначен для очищения агентов.  Наследует `src`.
- `TinyWorld`: Вероятно, описывает среду, в которой взаимодействуют агенты. Метод `clear_environments` предназначен для удаления окружений. Наследует `src`.
- `TinySocialNetwork`: Вероятно, представляет социальную сеть в системе. Наследует `src`.

**Функции**:

- `contains_action_type`, `contains_action_content`, `contains_stimulus_type`, `contains_stimulus_content`: Проверяют наличие действий и стимулов определённого типа/содержания в списках. Принимают список действий/стимулов и тип/содержание для проверки.
- `terminates_with_action_type`: Проверяет, заканчивается ли список действий заданным типом действия.
- `proposition_holds`: Проверяет истинность утверждения (пропозиции) с помощью вызова LLM (OpenAI). Валидирует ответ LLM на корректность.
- `only_alphanumeric`: Возвращает строку, содержащую только алфавитно-цифровые символы.  Полезная функция для очистки выходов LLM.
- `create_test_system_user_message`: Создает список сообщений для OpenAI, содержащий системное сообщение и пользовательское сообщение.
- `agents_configs_are_equal`:  Сравнивает конфигурации двух агентов, игнорируя имя (по умолчанию).
- `remove_file_if_exists`: Удаляет файл, если он существует по указанному пути.
- `get_relative_to_test_path`: Создает относительный путь к файлу в папке тестов.

**Переменные**:

- `openai_utils.force_api_cache`: Принудительно включает кэширование API OpenAI.

**Возможные ошибки и улучшения**:

- Нет явного контроля за исключениями. При неправильном ответе LLM (`proposition_holds`) возникает `Exception`. Стоит добавить более подробную обработку исключений для более устойчивого кода.
- Отсутствует документирование для `examples.create_*`.  Необходимо добавить документацию для функций `create_lisa_the_data_scientist`, `create_oscar_the_architect`, `create_marcos_the_physician`.
-  Функции для проверки `contains_*` и `terminates_with_*` работают со словарными структурами, но  нет явных указаний типов.
-  Необходимо пояснить, как используются `sys.path.append`, а также добавить пояснения о структуре папок проекта (`src.tinytroupe`)  и зависимости между модулями.  Отсутствие комментариев о роли `sleep`


**Цепочка взаимосвязей**:

Код тестов `testing_utils` использует функции и классы из модулей `openai_utils`, `agent`, `environment`, `examples`.  Эти модули, скорее всего, находятся в подпапке `src` и тесно связаны с логикой агентов, их взаимодействием со средой и хранением конфигураций.  Файлы из папки `tinytroupe` вероятно содержат определения данных классов и функций, которые используются в этих тестах.