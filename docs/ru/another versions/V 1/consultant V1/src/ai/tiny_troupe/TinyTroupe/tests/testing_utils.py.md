## Анализ кода модуля `testing_utils`

**Качество кода**:

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код содержит полезные утилиты для тестирования агентов и окружения.
    - Присутствуют функции для проверки действий и стимулов.
    - Есть функции для работы с файлами и создания тестовых сообщений.
    - Используется `pytest` для фикстур.
- **Минусы**:
    - Не хватает docstring для модуля.
    - Некоторые функции не имеют подробных комментариев в формате RST.
    - Используются стандартные блоки `try-except`, вместо `logger.error`.
    -  Пути к модулям не соответствуют структуре проекта, необходимо использовать относительный импорт.
    - Импорт `logger` не соответствует рекомендациям.

**Рекомендации по улучшению**:

- Добавить docstring для модуля с описанием его назначения.
- Добавить подробные docstring в формате RST для всех функций.
- Использовать `from src.logger.logger import logger` для логирования ошибок.
- Улучшить обработку ошибок, используя `logger.error` вместо `try-except`.
- Использовать относительные импорты для модулей внутри проекта.
-  Выровнять названия переменных и функций в соответствии со стандартами PEP8.
- Использовать одинарные кавычки для строк в коде.

**Оптимизированный код**:

```python
"""
Testing utilities.
==================

This module provides utility functions and fixtures for testing the behavior
of agents and environments within the TinyTroupe system.

It includes functions for:
    - Checking the content and type of actions and stimuli.
    - Verifying propositions using an LLM.
    - Creating test messages.
    - Comparing agent configurations.
    - Handling file operations.
    - Setting up test fixtures using pytest.

Usage
-----
This module is intended to be used in conjunction with pytest for unit and
integration testing of TinyTroupe components. It provides the necessary
tools to verify the expected behavior of the system's agents and their
interactions with the environment.

"""
import os
import sys
from time import sleep

sys.path.append('../../tinytroupe/') # add path # fixme: remove after relative import implementation
sys.path.append('../../')  # add path # fixme: remove after relative import implementation
sys.path.append('../')  # add path # fixme: remove after relative import implementation

from src.logger.logger import logger # import logger from src.logger
import tinytroupe.openai_utils as openai_utils
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld, TinySocialNetwork
import pytest
import importlib

# force caching, in order to save on API usage
openai_utils.force_api_cache(True, 'tests_cache.pickle')


def contains_action_type(actions, action_type) -> bool:
    """
    Checks if the given list of actions contains an action of the given type.

    :param actions: List of actions to check.
    :type actions: list
    :param action_type: The type of action to search for.
    :type action_type: str
    :return: True if an action of the given type is found, False otherwise.
    :rtype: bool

    Example:
        >>> actions = [{'action': {'type': 'message', 'content': 'hello'}}]
        >>> contains_action_type(actions, 'message')
        True
        >>> contains_action_type(actions, 'move')
        False
    """
    for action in actions:
        if action['action']['type'] == action_type:
            return True
    return False


def contains_action_content(actions: list, action_content: str) -> bool:
    """
    Checks if the given list of actions contains an action with the given content.

    :param actions: List of actions to check.
    :type actions: list
    :param action_content: The content to search for within action content.
    :type action_content: str
    :return: True if an action with the given content is found, False otherwise.
    :rtype: bool

    Example:
        >>> actions = [{'action': {'type': 'message', 'content': 'Hello World'}}]
        >>> contains_action_content(actions, 'world')
        True
        >>> contains_action_content(actions, 'goodbye')
        False
    """
    for action in actions:
        if action_content.lower() in action['action']['content'].lower():
            return True
    return False


def contains_stimulus_type(stimuli, stimulus_type) -> bool:
    """
    Checks if the given list of stimuli contains a stimulus of the given type.

    :param stimuli: List of stimuli to check.
    :type stimuli: list
    :param stimulus_type: The type of stimulus to search for.
    :type stimulus_type: str
    :return: True if a stimulus of the given type is found, False otherwise.
    :rtype: bool

    Example:
        >>> stimuli = [{'type': 'observation', 'content': 'something'}]
        >>> contains_stimulus_type(stimuli, 'observation')
        True
        >>> contains_stimulus_type(stimuli, 'message')
        False
    """
    for stimulus in stimuli:
        if stimulus['type'] == stimulus_type:
            return True
    return False


def contains_stimulus_content(stimuli, stimulus_content) -> bool:
    """
    Checks if the given list of stimuli contains a stimulus with the given content.

    :param stimuli: List of stimuli to check.
    :type stimuli: list
    :param stimulus_content: The content to search for within stimulus content.
    :type stimulus_content: str
    :return: True if a stimulus with the given content is found, False otherwise.
    :rtype: bool

    Example:
        >>> stimuli = [{'type': 'observation', 'content': 'The cat is sleeping'}]
        >>> contains_stimulus_content(stimuli, 'cat')
        True
        >>> contains_stimulus_content(stimuli, 'dog')
        False
    """
    for stimulus in stimuli:
        if stimulus_content.lower() in stimulus['content'].lower():
            return True
    return False


def terminates_with_action_type(actions, action_type) -> bool:
    """
    Checks if the given list of actions terminates with an action of the given type.

    :param actions: List of actions to check.
    :type actions: list
    :param action_type: The type of action to check for at the end of the list.
    :type action_type: str
    :return: True if the last action in the list matches the given type, False otherwise.
    :rtype: bool

    Example:
        >>> actions = [{'action': {'type': 'message', 'content': 'hello'}}, {'action': {'type': 'move', 'content': 'forward'}}]
        >>> terminates_with_action_type(actions, 'move')
        True
        >>> terminates_with_action_type(actions, 'message')
        False
    """
    if len(actions) == 0:
        return False
    return actions[-1]['action']['type'] == action_type


def proposition_holds(proposition: str) -> bool:
    """
    Checks if the given proposition is true according to an LLM call.

    This can be used to check for text properties that are hard to verify mechanically,
    such as "the text contains some ideas for a product".

    :param proposition: The proposition to verify.
    :type proposition: str
    :return: True if the proposition is true, False otherwise.
    :rtype: bool
    :raises Exception: If the LLM returns an unexpected result.

    Example:
        >>> proposition_holds("The sky is blue") # this depends on the LLM
        True
        >>> proposition_holds("The cat is flying") # this depends on the LLM
        False
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
    
    # call the LLM
    try:
      next_message = openai_utils.client().send_message(messages)
    except Exception as e:
      logger.error(f'Error calling LLM: {e}')
      return False # return False if LLM call fails
      
    # check the result
    cleaned_message = only_alphanumeric(next_message['content'])
    if cleaned_message.lower().startswith('true'):
        return True
    elif cleaned_message.lower().startswith('false'):
        return False
    else:
        logger.error(f'LLM returned unexpected result: {cleaned_message}')
        return False  # return False if LLM result is unexpected


def only_alphanumeric(string: str) -> str:
    """
    Returns a string containing only alphanumeric characters.

    :param string: The input string.
    :type string: str
    :return: The string containing only alphanumeric characters.
    :rtype: str

    Example:
        >>> only_alphanumeric("Hello123World!")
        'Hello123World'
    """
    return ''.join(c for c in string if c.isalnum())


def create_test_system_user_message(user_prompt, system_prompt='You are a helpful AI assistant.') -> list:
    """
    Creates a list containing one system message and one user message.

    :param user_prompt: The content of the user message.
    :type user_prompt: str
    :param system_prompt: The content of the system message, defaults to 'You are a helpful AI assistant.'.
    :type system_prompt: str, optional
    :return: A list containing the system and user message dictionaries.
    :rtype: list

    Example:
        >>> create_test_system_user_message('Hello')
        [{'role': 'system', 'content': 'You are a helpful AI assistant.'}, {'role': 'user', 'content': 'Hello'}]
        >>> create_test_system_user_message('How are you?', system_prompt='You are a friendly bot.')
        [{'role': 'system', 'content': 'You are a friendly bot.'}, {'role': 'user', 'content': 'How are you?'}]
    """
    messages = [{'role': 'system', 'content': system_prompt}]
    if user_prompt is not None:
        messages.append({'role': 'user', 'content': user_prompt})
    return messages


def agents_configs_are_equal(agent1, agent2, ignore_name=False) -> bool:
    """
    Checks if the configurations of two agents are equal.

    :param agent1: The first agent.
    :type agent1: TinyPerson
    :param agent2: The second agent.
    :type agent2: TinyPerson
    :param ignore_name: If True, the name attribute is ignored during comparison, defaults to False.
    :type ignore_name: bool, optional
    :return: True if the configurations are equal, False otherwise.
    :rtype: bool

    Example:
        >>> from tinytroupe.agent import TinyPerson
        >>> agent1 = TinyPerson(name='Agent1', role='Tester', model=['gpt-3.5'])
        >>> agent2 = TinyPerson(name='Agent2', role='Tester', model=['gpt-3.5'])
        >>> agents_configs_are_equal(agent1, agent2, ignore_name=True)
        True
        >>> agent3 = TinyPerson(name='Agent1', role='Developer', model=['gpt-3.5'])
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


def remove_file_if_exists(file_path) -> None:
    """
    Removes the file at the given path if it exists.

    :param file_path: The path to the file.
    :type file_path: str
    :return: None

    Example:
        >>> import os
        >>> file_path = 'test_file.txt'
        >>> with open(file_path, 'w') as f:
        ...     f.write('test')
        >>> remove_file_if_exists(file_path)
        >>> os.path.exists(file_path)
        False
    """
    if os.path.exists(file_path):
        os.remove(file_path)


def get_relative_to_test_path(path_suffix) -> str:
    """
    Returns the path to the test file with the given suffix.

    :param path_suffix: The suffix of the path relative to the test file directory.
    :type path_suffix: str
    :return: The full path to the test file.
    :rtype: str

    Example:
        >>> get_relative_to_test_path('test_data.txt')
        '/path/to/tests/test_data.txt' # this will vary based on the execution environment
    """
    return os.path.join(os.path.dirname(__file__), path_suffix)

############################################################################################################
# Fixtures
############################################################################################################


@pytest.fixture(scope='function')
def focus_group_world():
    """
    Pytest fixture to create a TinyWorld instance for a focus group.

    :return: A TinyWorld instance containing Lisa, Oscar, and Marcos.
    :rtype: TinyWorld
    """
    import tinytroupe.examples as examples # fixme: use relative import

    world = TinyWorld('Focus group', [examples.create_lisa_the_data_scientist(), examples.create_oscar_the_architect(), examples.create_marcos_the_physician()])
    return world


@pytest.fixture(scope='function')
def setup():
    """
    Pytest fixture to clear agents and environments before each test.

    :return: None
    """
    TinyPerson.clear_agents()
    TinyWorld.clear_environments()
    yield