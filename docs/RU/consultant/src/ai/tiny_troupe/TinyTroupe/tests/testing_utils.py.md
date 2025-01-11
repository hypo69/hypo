## Анализ кода модуля testing_utils

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разбит на логические блоки (функции проверок, утилиты ввода/вывода, фикстуры).
    - Присутствуют docstring для большинства функций, что облегчает понимание их назначения и использования.
    - Используются импорты для вызова внешних функций.
    - Есть общие функции для упрощения тестирования.
- Минусы
    - Не все функции имеют docstring в формате RST.
    - Есть использование `sys.path.append` для добавления путей, что может быть нежелательно.
    - Отсутствует единая точка для логирования.

**Рекомендации по улучшению**
1.  Добавить недостающие docstring в формате RST.
2.  Использовать `from src.logger.logger import logger` для логирования.
3.  Избегать `sys.path.append` путем использования относительных путей или настройки `PYTHONPATH`.
4.  Улучшить docstring, добавив примеры использования.
5.  Унифицировать использование одинарных кавычек (`'`) в коде и двойных (`"`) в операциях вывода.
6.  Добавить docstring для модуля.

**Оптимизированный код**
```python
"""
Модуль содержит набор утилит для тестирования агентов TinyTroupe.
=========================================================================================

Этот модуль предоставляет набор функций и фикстур для облегчения тестирования
поведения агентов и их взаимодействия в среде TinyTroupe.
Он включает в себя функции для проверки действий и стимулов, создания тестовых сообщений,
сравнения конфигураций агентов, а также для работы с файловой системой.

Примеры:
    
    Использование фикстуры `focus_group_world`:
    
    .. code-block:: python
        
        def test_something(focus_group_world):
            assert isinstance(focus_group_world, TinyWorld)
            # выполнение тестов с использованием `focus_group_world`

    Использование функции `contains_action_type`:

    .. code-block:: python
    
        actions = [{"action": {"type": "speak", "content": "hello"}}]
        assert contains_action_type(actions, "speak") == True
"""
import os
import sys
from time import sleep
# sys.path.append('../../tinytroupe/') # использование sys.path.append не рекомендуется
# sys.path.append('../../') # использование sys.path.append не рекомендуется
# sys.path.append('..')  # использование sys.path.append не рекомендуется
from src.logger.logger import logger
import tinytroupe.openai_utils as openai_utils
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld, TinySocialNetwork
import pytest
import importlib
from src.utils.jjson import j_loads, j_loads_ns


# force caching, in order to save on API usage
openai_utils.force_api_cache(True, 'tests_cache.pickle')

def contains_action_type(actions, action_type) -> bool:
    """
    Проверяет, содержит ли список действий действие заданного типа.

    Args:
        actions (list): Список действий.
        action_type (str): Тип действия для проверки.

    Returns:
        bool: True, если действие заданного типа найдено, False в противном случае.
    
    Example:
        >>> actions = [{"action": {"type": "speak", "content": "hello"}}]
        >>> contains_action_type(actions, "speak")
        True
        >>> contains_action_type(actions, "move")
        False
    """
    
    for action in actions:
        if action['action']['type'] == action_type:
            return True
    
    return False

def contains_action_content(actions: list, action_content: str) -> bool:
    """
    Проверяет, содержит ли список действий действие с заданным содержимым.

    Args:
        actions (list): Список действий.
        action_content (str): Содержимое действия для проверки.

    Returns:
        bool: True, если действие с заданным содержимым найдено, False в противном случае.
    
    Example:
        >>> actions = [{"action": {"type": "speak", "content": "hello world"}}]
        >>> contains_action_content(actions, "world")
        True
        >>> contains_action_content(actions, "bye")
        False
    """
    
    for action in actions:
        # проверка, содержится ли желаемое содержимое в содержимом действия
        if action_content.lower() in action['action']['content'].lower():
            return True
    
    return False

def contains_stimulus_type(stimuli, stimulus_type) -> bool:
    """
    Проверяет, содержит ли список стимулов стимул заданного типа.
    
    Args:
        stimuli (list): Список стимулов.
        stimulus_type (str): Тип стимула для проверки.
    
    Returns:
        bool: True, если стимул заданного типа найден, False в противном случае.
    
    Example:
        >>> stimuli = [{"type": "visual", "content": "image"}]
        >>> contains_stimulus_type(stimuli, "visual")
        True
        >>> contains_stimulus_type(stimuli, "audio")
        False
    """
    
    for stimulus in stimuli:
        if stimulus['type'] == stimulus_type:
            return True
    
    return False

def contains_stimulus_content(stimuli, stimulus_content) -> bool:
    """
    Проверяет, содержит ли список стимулов стимул с заданным содержимым.
    
    Args:
        stimuli (list): Список стимулов.
        stimulus_content (str): Содержимое стимула для проверки.
    
    Returns:
        bool: True, если стимул с заданным содержимым найден, False в противном случае.
        
    Example:
        >>> stimuli = [{"type": "visual", "content": "image of a cat"}]
        >>> contains_stimulus_content(stimuli, "cat")
        True
        >>> contains_stimulus_content(stimuli, "dog")
        False
    """
    
    for stimulus in stimuli:
        # проверка, содержится ли желаемое содержимое в содержимом стимула
        if stimulus_content.lower() in stimulus['content'].lower():
            return True
    
    return False

def terminates_with_action_type(actions, action_type) -> bool:
    """
    Проверяет, заканчивается ли список действий действием заданного типа.
    
    Args:
        actions (list): Список действий.
        action_type (str): Тип действия для проверки.

    Returns:
        bool: True, если последнее действие в списке имеет заданный тип, False в противном случае.
    
    Example:
        >>> actions = [{"action": {"type": "move"}}, {"action": {"type": "speak"}}]
        >>> terminates_with_action_type(actions, "speak")
        True
        >>> terminates_with_action_type(actions, "move")
        False
        >>> terminates_with_action_type([], "speak")
        False
    """
    
    if len(actions) == 0:
        return False
    
    return actions[-1]['action']['type'] == action_type


def proposition_holds(proposition: str) -> bool:
    """
    Проверяет, является ли данное утверждение истинным согласно вызову LLM.
    Используется для проверки текстовых свойств, которые сложно проверить механически.
    Например, "текст содержит идеи для продукта".
    
    Args:
        proposition (str): Утверждение для проверки.
    
    Returns:
        bool: True, если утверждение истинно, False в противном случае.
    
    Raises:
        Exception: Если LLM возвращает неожиданный результат.
    
    Example:
        # Предположим, что LLM может определить, является ли утверждение "текст содержит идеи" истинным.
        # result = proposition_holds("текст содержит идеи")
        # print(result)  #  выведет True или False в зависимости от ответа LLM.
        ...
    """

    system_prompt = f"""
    Check whether the following proposition is true or false. If it is
    true, write "true", otherwise write "false". Don't write anything else!
    """

    user_prompt = f"""
    Proposition: {proposition}
    """

    messages = [{'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_prompt}]
    
    # вызов LLM
    next_message = openai_utils.client().send_message(messages)

    # проверка результата
    cleaned_message = only_alphanumeric(next_message['content'])
    if cleaned_message.lower().startswith('true'):
        return True
    elif cleaned_message.lower().startswith('false'):
        return False
    else:
        raise Exception(f'LLM returned unexpected result: {cleaned_message}')

def only_alphanumeric(string: str) -> str:
    """
    Возвращает строку, содержащую только буквенно-цифровые символы.
    
    Args:
        string (str): Исходная строка.

    Returns:
        str: Строка, содержащая только буквенно-цифровые символы.
    
    Example:
        >>> only_alphanumeric("hello world 123!")
        'helloworld123'
    """
    return ''.join(c for c in string if c.isalnum())

def create_test_system_user_message(user_prompt, system_prompt='You are a helpful AI assistant.') -> list:
    """
    Создает список, содержащий одно системное сообщение и одно пользовательское сообщение.
    
    Args:
        user_prompt (str): Пользовательское сообщение.
        system_prompt (str, optional): Системное сообщение. По умолчанию 'You are a helpful AI assistant.'.

    Returns:
        list: Список сообщений, где первое сообщение - системное, а второе - пользовательское.
    
    Example:
        >>> create_test_system_user_message("What is the capital of France?")
        [{'role': 'system', 'content': 'You are a helpful AI assistant.'}, {'role': 'user', 'content': 'What is the capital of France?'}]
    """
    
    messages = [{'role': 'system', 'content': system_prompt}]
    
    if user_prompt is not None:
        messages.append({'role': 'user', 'content': user_prompt})
    
    return messages

def agents_configs_are_equal(agent1, agent2, ignore_name=False) -> bool:
    """
    Проверяет, равны ли конфигурации двух агентов.

    Args:
        agent1: Первый агент.
        agent2: Второй агент.
        ignore_name (bool, optional): Игнорировать ли поле 'name' при сравнении. По умолчанию False.

    Returns:
        bool: True, если конфигурации агентов равны, False в противном случае.

    Example:
        >>> from tinytroupe.agent import TinyPerson
        >>> agent1 = TinyPerson(name='Agent1', role='tester')
        >>> agent2 = TinyPerson(name='Agent2', role='tester')
        >>> agents_configs_are_equal(agent1, agent2, ignore_name=True)
        True
        >>> agent3 = TinyPerson(name='Agent3', role='developer')
        >>> agents_configs_are_equal(agent1, agent3, ignore_name=True)
        False
    """

    ignore_keys = []
    if ignore_name:
        ignore_keys.append('name')
    
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
    Удаляет файл по заданному пути, если он существует.
    
    Args:
        file_path (str): Путь к файлу.
    
    Example:
        >>> file_path = 'test_file.txt'
        >>> with open(file_path, 'w') as f:
        ...     f.write('some content')
        >>> remove_file_if_exists(file_path)
        # После выполнения, файл 'test_file.txt' будет удален, если он существовал.
    """
    
    if os.path.exists(file_path):
        os.remove(file_path)

def get_relative_to_test_path(path_suffix) -> str:
    """
    Возвращает путь к тестовому файлу с заданным суффиксом.
    
    Args:
        path_suffix (str): Суффикс пути к файлу.
    
    Returns:
        str: Полный путь к файлу.
    
    Example:
        >>> get_relative_to_test_path('data/test.txt')
        '/path/to/your/testing_utils_directory/data/test.txt' # Зависит от текущей директории.
    """
    
    return os.path.join(os.path.dirname(__file__), path_suffix)


############################################################################################################
# Fixtures
############################################################################################################

@pytest.fixture(scope='function')
def focus_group_world():
    """
    Фикстура для создания мира с несколькими агентами для тестирования.
    
    Returns:
        TinyWorld: Экземпляр TinyWorld с тремя агентами.
    
    Example:
        def test_something(focus_group_world):
            assert isinstance(focus_group_world, TinyWorld)
            # Проверка наличия агентов в мире
            assert len(focus_group_world.agents) == 3
    """
    import tinytroupe.examples as examples   
    
    world = TinyWorld('Focus group', [examples.create_lisa_the_data_scientist(), examples.create_oscar_the_architect(), examples.create_marcos_the_physician()])
    return world

@pytest.fixture(scope='function')
def setup():
    """
    Фикстура для настройки тестов, очищает агентов и окружения перед выполнением каждого теста.
    
    Example:
        def test_something(setup):
            # Тест, который начинается с чистого состояния TinyPerson и TinyWorld
            ...
    """
    TinyPerson.clear_agents()
    TinyWorld.clear_environments()

    yield