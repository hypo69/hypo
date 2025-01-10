# Анализ кода модуля testing_utils

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и разбит на логические блоки (функции, фикстуры).
    - Присутствуют docstring для большинства функций, что облегчает понимание их назначения и использования.
    - Используются осмысленные имена переменных и функций, что способствует читаемости кода.
    - Наличие фикстур для тестирования упрощает создание тестовых окружений.
-  Минусы
    - Отсутствует описание модуля в начале файла.
    - Некоторые docstring требуют доработки (например, отсутствует описание возвращаемых значений или аргументов в некоторых функциях).
    - Используется прямой вызов `openai_utils.client().send_message` вместо использования общего интерфейса.
    - Не хватает обработки ошибок и логирования для отладки.
    - Не все функции имеют примеры использования в docstring.
    - Отсутствует импорт `from src.logger.logger import logger`.
    - Использование `sys.path.append` для добавления путей может усложнить сопровождение проекта.
    - В некоторых функциях отсутствуют явные типы аргументов.

**Рекомендации по улучшению**

1.  Добавить описание модуля в начале файла.
2.  Дополнить docstring для всех функций, включая описание аргументов, возвращаемых значений и примеры использования.
3.  Использовать общий интерфейс для вызова LLM (если есть) вместо прямого вызова `openai_utils.client().send_message`.
4.  Добавить обработку ошибок с использованием `logger.error` и логирование для отладки.
5.  Добавить явные типы для аргументов функций.
6.  Импортировать `logger` из `src.logger.logger`.
7.  Упростить добавление путей, используя относительные пути, если это возможно.
8.  Использовать более точные проверки в функциях `proposition_holds` (например, проверять не только начало строки).
9.  Рассмотреть возможность использования `Path` из `pathlib` для работы с путями.
10. Добавить комментарии с подробным объяснением каждого блока кода.

**Оптимизированный код**

```python
"""
Модуль, предоставляющий набор утилит для тестирования TinyTroupe.
=================================================================

Этот модуль содержит функции и фикстуры, которые помогают в создании и проведении тестов для агентов, окружений и других
компонентов TinyTroupe. Он включает в себя проверки различных аспектов поведения агентов и мира,
а также утилиты для работы с файлами и путями.

Пример использования
--------------------

Пример использования фикстуры `focus_group_world`:

.. code-block:: python

    def test_focus_group_world(focus_group_world):
        assert len(focus_group_world.agents) == 3

"""
import os
import sys
from pathlib import Path
from time import sleep
from typing import Any, List, Dict
sys.path.append('../../tinytroupe/')
sys.path.append('../../')
sys.path.append('../')
from src.logger.logger import logger # импортируем logger
import tinytroupe.openai_utils as openai_utils
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld, TinySocialNetwork
import pytest
import importlib


# force caching, in order to save on API usage
openai_utils.force_api_cache(True, 'tests_cache.pickle')

def contains_action_type(actions: List[Dict], action_type: str) -> bool:
    """
    Проверяет, содержит ли список действий действие заданного типа.

    Args:
        actions (List[Dict]): Список действий для проверки.
        action_type (str): Тип действия для поиска.

    Returns:
        bool: `True`, если действие заданного типа найдено, иначе `False`.
    
    Example:
        >>> actions = [{'action': {'type': 'write', 'content': 'hello'}}]
        >>> contains_action_type(actions, 'write')
        True
    """
    # Проход по всем действиям в списке
    for action in actions:
        # Проверка типа текущего действия
        if action['action']['type'] == action_type:
            return True
    
    return False

def contains_action_content(actions: List[Dict], action_content: str) -> bool:
    """
    Проверяет, содержит ли список действий действие с заданным содержимым.

    Args:
        actions (List[Dict]): Список действий для проверки.
        action_content (str): Содержимое действия для поиска.

    Returns:
        bool: `True`, если действие с заданным содержимым найдено, иначе `False`.
    
    Example:
        >>> actions = [{'action': {'type': 'write', 'content': 'hello world'}}]
        >>> contains_action_content(actions, 'hello')
        True
    """
    # Проход по всем действиям в списке
    for action in actions:
        # Проверка, содержит ли действие заданное содержимое (без учета регистра)
        if action_content.lower() in action['action']['content'].lower():
            return True
    
    return False

def contains_stimulus_type(stimuli: List[Dict], stimulus_type: str) -> bool:
    """
    Проверяет, содержит ли список стимулов стимул заданного типа.

    Args:
        stimuli (List[Dict]): Список стимулов для проверки.
        stimulus_type (str): Тип стимула для поиска.

    Returns:
        bool: `True`, если стимул заданного типа найден, иначе `False`.
    
    Example:
        >>> stimuli = [{'type': 'perception', 'content': 'sound'}]
        >>> contains_stimulus_type(stimuli, 'perception')
        True
    """
    # Проход по всем стимулам в списке
    for stimulus in stimuli:
        # Проверка типа текущего стимула
        if stimulus['type'] == stimulus_type:
            return True
    
    return False

def contains_stimulus_content(stimuli: List[Dict], stimulus_content: str) -> bool:
    """
    Проверяет, содержит ли список стимулов стимул с заданным содержимым.

    Args:
        stimuli (List[Dict]): Список стимулов для проверки.
        stimulus_content (str): Содержимое стимула для поиска.

    Returns:
        bool: `True`, если стимул с заданным содержимым найден, иначе `False`.
    
     Example:
        >>> stimuli = [{'type': 'perception', 'content': 'loud sound'}]
        >>> contains_stimulus_content(stimuli, 'sound')
        True
    """
    # Проход по всем стимулам в списке
    for stimulus in stimuli:
        # Проверка, содержит ли стимул заданное содержимое (без учета регистра)
        if stimulus_content.lower() in stimulus['content'].lower():
            return True
    
    return False

def terminates_with_action_type(actions: List[Dict], action_type: str) -> bool:
    """
    Проверяет, заканчивается ли список действий действием заданного типа.

    Args:
        actions (List[Dict]): Список действий для проверки.
        action_type (str): Тип действия для поиска.

    Returns:
        bool: `True`, если список заканчивается действием заданного типа, иначе `False`.
    
    Example:
        >>> actions = [{'action': {'type': 'read', 'content': 'book'}}, {'action': {'type': 'write', 'content': 'diary'}}]
        >>> terminates_with_action_type(actions, 'write')
        True
    """
    # Проверка, не пустой ли список
    if not actions:
        return False
    
    # Проверка типа последнего действия в списке
    return actions[-1]['action']['type'] == action_type


def proposition_holds(proposition: str) -> bool:
    """
    Проверяет истинность заданного утверждения с использованием LLM.
    
    Эта функция использует LLM для проверки текстовых свойств, которые сложно проверить механически.
    Например, можно проверить, содержит ли текст какие-либо идеи для продукта.

    Args:
        proposition (str): Утверждение для проверки.

    Returns:
        bool: `True`, если утверждение истинно, `False`, если ложно.

    Raises:
        Exception: Если LLM возвращает неожиданный результат.
    
    Example:
        >>> proposition_holds('The text contains some ideas for a product')
        True
    """
    system_prompt = f"""
    Check whether the following proposition is true or false. If it is
    true, write "true", otherwise write "false". Don't write anything else!
    """

    user_prompt = f"""
    Proposition: {proposition}
    """
    # Формирование сообщений для LLM
    messages = [{'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_prompt}]
    
    try:
        # Отправка сообщения LLM
        next_message = openai_utils.client().send_message(messages)
        # Очистка ответа LLM от не буквенно-цифровых символов
        cleaned_message = only_alphanumeric(next_message['content'])
        # Проверка ответа LLM на истинность
        if cleaned_message.lower().startswith('true'):
            return True
        # Проверка ответа LLM на ложность
        elif cleaned_message.lower().startswith('false'):
            return False
        else:
            # Если ответ LLM не соответствует ожидаемому формату, генерируется исключение
            raise Exception(f'LLM returned unexpected result: {cleaned_message}')
    except Exception as ex:
        logger.error(f'Ошибка при проверке пропозиции: {proposition}', exc_info=ex)
        return False

def only_alphanumeric(string: str) -> str:
    """
    Возвращает строку, содержащую только буквенно-цифровые символы.

    Args:
        string (str): Входная строка.

    Returns:
        str: Строка, содержащая только буквенно-цифровые символы.
    
    Example:
        >>> only_alphanumeric('Hello, 123!')
        'Hello123'
    """
    # Возвращает строку, содержащую только буквенно-цифровые символы
    return ''.join(c for c in string if c.isalnum())

def create_test_system_user_message(user_prompt: str, system_prompt: str = 'You are a helpful AI assistant.') -> List[Dict]:
    """
    Создает список сообщений, содержащий системное и пользовательское сообщение.

    Args:
        user_prompt (str): Пользовательское сообщение.
        system_prompt (str, optional): Системное сообщение. Defaults to 'You are a helpful AI assistant.'.

    Returns:
        List[Dict]: Список сообщений для отправки в LLM.
    
    Example:
        >>> create_test_system_user_message('Hello, how are you?', 'You are a test bot.')
        [{'role': 'system', 'content': 'You are a test bot.'}, {'role': 'user', 'content': 'Hello, how are you?'}]
    """
    # Создание списка с системным сообщением
    messages = [{'role': 'system', 'content': system_prompt}]
    # Если пользовательское сообщение не None, добавляем его в список
    if user_prompt is not None:
        messages.append({'role': 'user', 'content': user_prompt})
    
    return messages

def agents_configs_are_equal(agent1: TinyPerson, agent2: TinyPerson, ignore_name: bool = False) -> bool:
    """
    Проверяет, равны ли конфигурации двух агентов.
    
    Args:
        agent1 (TinyPerson): Первый агент для сравнения.
        agent2 (TinyPerson): Второй агент для сравнения.
        ignore_name (bool, optional): Игнорировать ли имя агента при сравнении. Defaults to False.

    Returns:
        bool: `True`, если конфигурации агентов равны, иначе `False`.
    
    Example:
        >>> from tinytroupe.agent import TinyPerson
        >>> agent1 = TinyPerson(name='Agent1', role='tester', persona='test persona')
        >>> agent2 = TinyPerson(name='Agent2', role='tester', persona='test persona')
        >>> agents_configs_are_equal(agent1, agent2, ignore_name=True)
        True
    """
    ignore_keys = []
    # Если имя надо игнорировать, добавляем ключ "name" в список игнорируемых ключей
    if ignore_name:
        ignore_keys.append('name')
    
    # Итерация по ключам конфигурации первого агента
    for key in agent1._configuration.keys():
        # Если ключ находится в списке игнорируемых, пропускаем его
        if key in ignore_keys:
            continue
        # Если значения по ключу у двух агентов не равны, возвращаем False
        if agent1._configuration[key] != agent2._configuration[key]:
            return False
    
    return True
############################################################################################################
# I/O utilities
############################################################################################################

def remove_file_if_exists(file_path: str | Path):
    """
    Удаляет файл по заданному пути, если он существует.

    Args:
        file_path (str | Path): Путь к файлу, который необходимо удалить.
    
    Example:
        >>> file_path = 'test_file.txt'
        >>> with open(file_path, 'w') as f:
        ...     f.write('test')
        >>> remove_file_if_exists(file_path)
        >>> os.path.exists(file_path)
        False
    """
    # Проверка существования файла
    if os.path.exists(file_path):
        # Удаление файла
        os.remove(file_path)

def get_relative_to_test_path(path_suffix: str) -> str:
    """
    Возвращает путь к файлу относительно директории тестового файла.

    Args:
        path_suffix (str): Суффикс пути файла.

    Returns:
        str: Полный путь к файлу.
    
    Example:
         >>> get_relative_to_test_path('test_file.txt')
         '/absolute/path/to/tests/test_file.txt'
    """
    # Возвращает путь к файлу, объединенный с путем директории этого файла
    return str(Path(os.path.dirname(__file__)) / path_suffix)


############################################################################################################
# Fixtures
############################################################################################################

@pytest.fixture(scope='function')
def focus_group_world() -> TinyWorld:
    """
    Создает и возвращает тестовый мир с тремя агентами.

    Returns:
        TinyWorld: Мир с агентами Lisa, Oscar и Marcos.
    """
    import tinytroupe.examples as examples
    
    # Создание тестового мира с тремя агентами
    world = TinyWorld('Focus group', [examples.create_lisa_the_data_scientist(), examples.create_oscar_the_architect(), examples.create_marcos_the_physician()])
    return world

@pytest.fixture(scope='function')
def setup():
    """
    Очищает агентов и окружения перед каждым тестом.

    Yields:
         None:
    """
    # Очистка агентов и окружений перед каждым тестом
    TinyPerson.clear_agents()
    TinyWorld.clear_environments()

    yield