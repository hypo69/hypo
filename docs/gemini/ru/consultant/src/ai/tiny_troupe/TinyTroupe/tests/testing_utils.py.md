# Анализ кода модуля testing_utils

**Качество кода**
8
 -  Плюсы
    - Код содержит функции для проверки действий и стимулов, что полезно для тестирования агентов.
    - Присутствуют функции для сравнения конфигураций агентов и создания сообщений.
    - Используются фикстуры pytest для настройки тестовой среды.
    - Код соответствует PEP8 в большинстве случаев.
 -  Минусы
    - Отсутствует документация в формате RST для функций, классов и модулей.
    - Используется `sys.path.append`, что может быть не лучшей практикой.
    - Нет обработки ошибок с использованием `logger.error` для `openai_utils.client().send_message`.
    - Нет явной обработки исключений в некоторых функциях, например, `only_alphanumeric`.

**Рекомендации по улучшению**
1. Добавить документацию в формате RST для всех функций, классов и модуля.
2. Заменить использование `sys.path.append` на более надежный способ импорта, если это возможно.
3. Добавить обработку ошибок с использованием `logger.error` для вызова LLM.
4. Добавить обработку исключений в `only_alphanumeric`.
5. Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для загрузки JSON, если это применимо.
6. Привести в соответствие имена функций, переменных и импортов с ранее обработанными файлами.
7. Избегать избыточного использования `try-except`, предпочитая обработку ошибок с помощью `logger.error`.

**Оптимизированный код**
```python
"""
Модуль содержит набор утилит для тестирования агентов в TinyTroupe.
==================================================================

Этот модуль предоставляет функции для проверки действий, стимулов, сравнения конфигураций агентов
и создания сообщений для тестов. Он также включает фикстуры для настройки тестовой среды.

Пример использования
--------------------

.. code-block:: python

    from tests.testing_utils import contains_action_type, create_test_system_user_message

    def test_some_function():
        actions = [{"action": {"type": "some_type", "content": "some content"}}]
        assert contains_action_type(actions, "some_type")

        messages = create_test_system_user_message("Hello, world!")
        assert len(messages) == 2
"""
import os
import sys
from time import sleep
# sys.path.append('../../tinytroupe/') #  Использование sys.path.append может быть проблематичным
# sys.path.append('../../') #  Использование sys.path.append может быть проблематичным
# sys.path.append('../') #  Использование sys.path.append может быть проблематичным

from src.logger.logger import logger
import src.ai.tiny_troupe.openai_utils as openai_utils
from src.ai.tiny_troupe.agent import TinyPerson
from src.ai.tiny_troupe.environment import TinyWorld, TinySocialNetwork
import pytest
import importlib

# force caching, in order to save on API usage
openai_utils.force_api_cache(True, "tests_cache.pickle")


def contains_action_type(actions, action_type) -> bool:
    """
    Проверяет, содержит ли данный список действий действие указанного типа.

    :param actions: Список действий для проверки.
    :type actions: list
    :param action_type: Тип действия для поиска.
    :type action_type: str
    :return: True, если действие указанного типа найдено, False в противном случае.
    :rtype: bool
    """
    for action in actions: # итерируемся по списку действий
        if action["action"]["type"] == action_type: # сравниваем тип действия с искомым
            return True
    
    return False


def contains_action_content(actions: list, action_content: str) -> bool:
    """
    Проверяет, содержит ли данный список действий действие с указанным содержимым.

    :param actions: Список действий для проверки.
    :type actions: list
    :param action_content: Содержимое действия для поиска.
    :type action_content: str
    :return: True, если действие с указанным содержимым найдено, False в противном случае.
    :rtype: bool
    """
    for action in actions: # итерируемся по списку действий
        # проверяем, содержится ли искомое содержимое в содержимом действия (без учета регистра)
        if action_content.lower() in action["action"]["content"].lower():
            return True
    
    return False


def contains_stimulus_type(stimuli, stimulus_type) -> bool:
    """
    Проверяет, содержит ли данный список стимулов стимул указанного типа.

    :param stimuli: Список стимулов для проверки.
    :type stimuli: list
    :param stimulus_type: Тип стимула для поиска.
    :type stimulus_type: str
    :return: True, если стимул указанного типа найден, False в противном случае.
    :rtype: bool
    """
    for stimulus in stimuli: # итерируемся по списку стимулов
        if stimulus["type"] == stimulus_type: # сравниваем тип стимула с искомым
            return True
    
    return False


def contains_stimulus_content(stimuli, stimulus_content) -> bool:
    """
    Проверяет, содержит ли данный список стимулов стимул с указанным содержимым.

    :param stimuli: Список стимулов для проверки.
    :type stimuli: list
    :param stimulus_content: Содержимое стимула для поиска.
    :type stimulus_content: str
    :return: True, если стимул с указанным содержимым найден, False в противном случае.
    :rtype: bool
    """
    for stimulus in stimuli: # итерируемся по списку стимулов
        # проверяем, содержится ли искомое содержимое в содержимом стимула (без учета регистра)
        if stimulus_content.lower() in stimulus["content"].lower():
            return True
    
    return False


def terminates_with_action_type(actions, action_type) -> bool:
    """
    Проверяет, заканчивается ли данный список действий действием указанного типа.

    :param actions: Список действий для проверки.
    :type actions: list
    :param action_type: Тип действия для поиска.
    :type action_type: str
    :return: True, если последнее действие в списке имеет указанный тип, False в противном случае.
    :rtype: bool
    """
    if len(actions) == 0: # проверяем, что список не пуст
        return False
    
    return actions[-1]["action"]["type"] == action_type # сравниваем тип последнего действия с искомым


def proposition_holds(proposition: str) -> bool:
    """
    Проверяет, является ли данное утверждение истинным с помощью вызова LLM.

    Это можно использовать для проверки текстовых свойств, которые сложно проверить механически,
    например, "текст содержит несколько идей для продукта".

    :param proposition: Утверждение для проверки.
    :type proposition: str
    :return: True, если утверждение истинно, False в противном случае.
    :rtype: bool
    :raises Exception: Если LLM возвращает неожиданный результат.
    """
    system_prompt = f"""
    Check whether the following proposition is true or false. If it is
    true, write "true", otherwise write "false". Don\'t write anything else!
    """

    user_prompt = f"""
    Proposition: {proposition}
    """

    messages = [{"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}]
    
    # вызываем LLM
    try:
        next_message = openai_utils.client().send_message(messages)
    except Exception as e:
        logger.error(f"Ошибка при вызове LLM: {e}")
        return False


    # проверяем результат
    cleaned_message = only_alphanumeric(next_message["content"])
    if cleaned_message.lower().startswith("true"):
        return True
    elif cleaned_message.lower().startswith("false"):
        return False
    else:
        raise Exception(f"LLM returned unexpected result: {cleaned_message}")


def only_alphanumeric(string: str) -> str:
    """
    Возвращает строку, содержащую только буквенно-цифровые символы.

    :param string: Строка для обработки.
    :type string: str
    :return: Строка, содержащая только буквенно-цифровые символы.
    :rtype: str
    """
    try:
        return ''.join(c for c in string if c.isalnum())
    except Exception as e:
        logger.error(f"Ошибка при удалении не буквенно-цифровых символов: {e}")
        return ""


def create_test_system_user_message(user_prompt, system_prompt="You are a helpful AI assistant.") -> list:
    """
    Создает список, содержащий одно системное сообщение и одно пользовательское сообщение.

    :param user_prompt: Пользовательское сообщение.
    :type user_prompt: str
    :param system_prompt: Системное сообщение.
    :type system_prompt: str
    :return: Список сообщений.
    :rtype: list
    """
    messages = [{"role": "system", "content": system_prompt}] # создаем список сообщений и добавляем системное сообщение
    
    if user_prompt is not None: # проверяем, есть ли пользовательское сообщение
        messages.append({"role": "user", "content": user_prompt}) # добавляем пользовательское сообщение в список
    
    return messages


def agents_configs_are_equal(agent1, agent2, ignore_name=False) -> bool:
    """
    Проверяет, равны ли конфигурации двух агентов.

    :param agent1: Первый агент для сравнения.
    :type agent1: TinyPerson
    :param agent2: Второй агент для сравнения.
    :type agent2: TinyPerson
    :param ignore_name: Игнорировать ли имя агента при сравнении.
    :type ignore_name: bool
    :return: True, если конфигурации агентов равны (с учетом ignore_name), False в противном случае.
    :rtype: bool
    """
    ignore_keys = [] # инициализируем список игнорируемых ключей
    if ignore_name: # проверяем, нужно ли игнорировать имя агента
        ignore_keys.append("name") # добавляем ключ 'name' в список игнорируемых
    
    for key in agent1._configuration.keys(): # итерируемся по ключам конфигурации первого агента
        if key in ignore_keys: # проверяем, нужно ли игнорировать текущий ключ
            continue # переходим к следующей итерации, если нужно игнорировать
        
        if agent1._configuration[key] != agent2._configuration[key]: # сравниваем значения конфигурации по текущему ключу
            return False # возвращаем False, если значения не совпадают
    
    return True # возвращаем True, если все значения конфигурации совпадают
############################################################################################################
# I/O utilities
############################################################################################################


def remove_file_if_exists(file_path):
    """
    Удаляет файл по указанному пути, если он существует.

    :param file_path: Путь к файлу для удаления.
    :type file_path: str
    """
    if os.path.exists(file_path): # проверяем существование файла
        os.remove(file_path) # удаляем файл


def get_relative_to_test_path(path_suffix) -> str:
    """
    Возвращает путь к тестовому файлу с указанным суффиксом.

    :param path_suffix: Суффикс пути к файлу.
    :type path_suffix: str
    :return: Полный путь к тестовому файлу.
    :rtype: str
    """
    return os.path.join(os.path.dirname(__file__), path_suffix) # формируем путь к файлу на основе текущего каталога


############################################################################################################
# Fixtures
############################################################################################################

@pytest.fixture(scope="function")
def focus_group_world():
    """
    Создает фикстуру мира для фокус-группы.

    :return: Мир TinyWorld.
    :rtype: TinyWorld
    """
    import src.ai.tiny_troupe.examples as examples   # импортируем примеры
    
    world = TinyWorld("Focus group", [examples.create_lisa_the_data_scientist(), examples.create_oscar_the_architect(), examples.create_marcos_the_physician()]) # создаем мир с агентами
    return world # возвращаем созданный мир


@pytest.fixture(scope="function")
def setup():
    """
    Создает фикстуру для настройки тестовой среды.

    Очищает агентов и окружения перед выполнением каждого теста.
    """
    TinyPerson.clear_agents() # очищаем список агентов
    TinyWorld.clear_environments() # очищаем список окружений

    yield